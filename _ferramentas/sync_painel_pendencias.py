"""
Gera o array `var pendencias = [...]` do Painel do Fundador a partir de pendencias.json,
substituindo a copia manual que ja causou 2 bugs de sincronia (04/08 e 07/08/2026).

Uso: python sync_painel_pendencias.py
Le:    01_CEO/Pendencias/pendencias.json
Edita: 01_CEO/Painel_Fundador/painel_fundador_sttk.html (so o bloco var pendencias = [...];)

So itens com status == "aberta" entram no Painel (mesmo criterio ja usado a mao).
Nao mexe em nenhum outro trecho do HTML (feed, R, cards, recToCard).
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PENDENCIAS_JSON = BASE / "01_CEO" / "Pendencias" / "pendencias.json"
PAINEL_HTML = BASE / "01_CEO" / "Painel_Fundador" / "painel_fundador_sttk.html"


def js_string(s):
    if s is None:
        s = ""
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return '"' + s + '"'


def build_pendencias_js(itens):
    abertos = [i for i in itens if i.get("status") == "aberta"]
    linhas = []
    for it in abertos:
        owner = js_string(it.get("owner", ""))
        txt = js_string(it.get("txt", ""))
        # Mantem AAAA-MM-DD integral (nao trunca para DD/MM): o Painel calcula
        # "ha N dias" em JS no carregamento da pagina, e isso exige o ano
        # (adicionado 10/08/2026, melhoria do indicador de dias parado).
        # A exibicao em DD/MM continua sendo feita no proprio JS (fmtDataBR).
        desde = js_string(it.get("desde", ""))
        crit = js_string(it.get("crit", ""))
        alc = js_string(it.get("alc", ""))
        res = js_string(it.get("res", ""))
        linha = (
            "    {owner:" + owner + ",txt:" + txt + ",desde:" + desde
            + ",crit:" + crit + ",alc:" + alc + ",res:" + res + "},"
        )
        linhas.append(linha)
    if linhas:
        linhas[-1] = linhas[-1][:-1]  # remove ultima virgula
    return "  var pendencias = [\n" + "\n".join(linhas) + "\n  ];"


def main():
    data = json.loads(PENDENCIAS_JSON.read_text(encoding="utf-8"))
    itens = data["itens"]
    novo_bloco = build_pendencias_js(itens)

    html = PAINEL_HTML.read_text(encoding="utf-8")
    padrao = re.compile(r"  var pendencias = \[.*?\n  \];", re.DOTALL)
    m = padrao.search(html)
    if not m:
        print("ERRO: bloco 'var pendencias = [...]' nao encontrado no HTML", file=sys.stderr)
        sys.exit(1)

    bloco_atual = m.group(0)
    if bloco_atual == novo_bloco:
        print("OK: sem mudanca (Painel ja reflete pendencias.json)")
        return

    novo_html = html[: m.start()] + novo_bloco + html[m.end():]
    PAINEL_HTML.write_text(novo_html, encoding="utf-8")
    n_abertos = len([i for i in itens if i.get("status") == "aberta"])
    print(f"OK: array pendencias regenerado ({n_abertos} itens abertos)")


if __name__ == "__main__":
    main()
