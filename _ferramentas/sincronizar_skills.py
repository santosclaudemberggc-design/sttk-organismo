"""Copia as Skills de .claude/skills (a original) para .agents/skills (a cópia).

Regra (Skill criando-skills-sttk): só se edita .claude/skills; .agents/skills é refeita por este script.

Uso:
    python _ferramentas/sincronizar_skills.py            # mostra o que mudaria, sem copiar
    python _ferramentas/sincronizar_skills.py --aplicar  # copia
    python _ferramentas/sincronizar_skills.py --aplicar --forcar  # copia mesmo cópia editada depois da original

Proteção: se um arquivo da cópia for mais novo que o da original, alguém editou a cópia.
Sem --forcar, esse arquivo não é copiado e aparece como CONFLITO para ser resolvido à mão.
Arquivo que só existe na cópia nunca é apagado; aparece como SOBRA.
"""
import filecmp
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAL = RAIZ / ".claude" / "skills"
COPIA = RAIZ / ".agents" / "skills"
IGNORAR = {"__pycache__", ".DS_Store"}


def arquivos(base: Path) -> set[Path]:
    return {
        p.relative_to(base)
        for p in base.rglob("*")
        if p.is_file() and not IGNORAR.intersection(p.parts)
    }


def classificar(forcar: bool) -> tuple[list, list, list, list]:
    orig, copia = arquivos(ORIGINAL), arquivos(COPIA)
    novos = sorted(orig - copia)
    sobras = sorted(copia - orig)
    mudados, conflitos = [], []
    for rel in sorted(orig & copia):
        a, b = ORIGINAL / rel, COPIA / rel
        if filecmp.cmp(a, b, shallow=False):
            continue
        if b.stat().st_mtime > a.stat().st_mtime and not forcar:
            conflitos.append(rel)
        else:
            mudados.append(rel)
    return novos, mudados, conflitos, sobras


def main() -> int:
    aplicar = "--aplicar" in sys.argv
    forcar = "--forcar" in sys.argv
    novos, mudados, conflitos, sobras = classificar(forcar)

    for titulo, lista in (("NOVO", novos), ("MUDOU", mudados), ("CONFLITO", conflitos), ("SOBRA", sobras)):
        for rel in lista:
            print(f"{titulo}: {rel.as_posix()}")

    if aplicar:
        for rel in novos + mudados:
            destino = COPIA / rel
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ORIGINAL / rel, destino)
        print(f"Copiados: {len(novos) + len(mudados)}.")
    else:
        print(f"Para copiar: {len(novos) + len(mudados)} (rode com --aplicar).")

    if conflitos:
        print(f"{len(conflitos)} conflito(s): a cópia foi editada depois da original. Resolver à mão.")
    return 1 if conflitos else 0


if __name__ == "__main__":
    sys.exit(main())
