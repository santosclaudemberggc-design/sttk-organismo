"""Gancho PreToolUse: impede que subagentes examinados leiam ou alterem os gabaritos lacrados.

Liberados: a sessão principal (sem agent_type) e o examinador "bardi".
Bloqueados: qualquer outro subagente cuja chamada cite a pasta _gabaritos_LACRADO_bardi
em algum campo da ferramenta (caminho, padrão de busca ou comando de terminal).
Decisão de Claudemberg em 15/10/2026 (opção C da pendência gabaritos-exame-acessiveis-aos-agentes).
"""
import json
import sys

MARCAS = ("_gabaritos_lacrado_bardi", "gabarito_lacrado")
LIBERADOS = {"bardi"}


def textos(valor):
    if isinstance(valor, str):
        yield valor
    elif isinstance(valor, dict):
        for v in valor.values():
            yield from textos(v)
    elif isinstance(valor, list):
        for v in valor:
            yield from textos(v)


def main():
    try:
        dados = json.load(sys.stdin)
    except Exception as erro:
        print(f"bloquear_gabaritos: entrada inválida ({erro}); bloqueado por segurança", file=sys.stderr)
        sys.exit(2)

    agente = (dados.get("agent_type") or "").strip().lower()
    if not agente or agente in LIBERADOS:
        sys.exit(0)

    entrada = dados.get("tool_input") or {}
    for t in textos(entrada):
        normal = t.replace("\\", "/").lower()
        if any(m in normal for m in MARCAS):
            print(
                f"Bloqueado: o agente '{agente}' não pode acessar a pasta de gabaritos lacrados. "
                "Leia só o caso.md do exame.",
                file=sys.stderr,
            )
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
