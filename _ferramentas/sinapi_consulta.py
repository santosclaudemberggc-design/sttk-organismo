"""Consulta de composições SINAPI por código ou palavra, para um estado.

Lê a pasta mais recente em _referencias_precos/SINAPI/AAAA-MM_baixado-AAAA-MM-DD/.
Uso:
    python _ferramentas/sinapi_consulta.py 97631              # código, RJ, sem desoneração
    python _ferramentas/sinapi_consulta.py "demolicao piso" --uf RJ --desonerado
Saída: mês de referência, planilha, código, descrição, unidade, custo da UF e %AS.
"""
import argparse
import glob
import os
import re
import sys
import unicodedata

import openpyxl

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_referencias_precos", "SINAPI")
HEADER_ROW = 10  # linha com "Grupo | Código | Descrição | Unidade | Custo | %AS ..."
UF_ROW = 9       # linha com as siglas dos estados
CODE_IN_LINK = re.compile(r",\s*(\d+)\)\s*$")


def normaliza(texto):
    sem_acento = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    return sem_acento.lower()


def pasta_mais_recente():
    pastas = sorted(glob.glob(os.path.join(BASE, "*_baixado-*")))
    if not pastas:
        sys.exit("Nenhuma pasta SINAPI encontrada em " + BASE)
    return pastas[-1]


def codigo_da_celula(valor):
    if valor is None:
        return None
    texto = str(valor).strip()
    if texto.isdigit():
        return texto
    achado = CODE_IN_LINK.search(texto)
    return achado.group(1) if achado else None


def consultar(termos, uf, desonerado, limite):
    pasta = pasta_mais_recente()
    arquivo = [f for f in glob.glob(os.path.join(pasta, "*.xlsx")) if "Refer" in f][0]
    aba = "CCD" if desonerado else "CSD"
    ws = openpyxl.load_workbook(arquivo, read_only=True)[aba]
    linhas = ws.iter_rows(values_only=True)
    cabecalho = [next(linhas) for _ in range(HEADER_ROW)]
    mes = cabecalho[2][1]
    ufs = [str(c).strip() if c else "" for c in cabecalho[UF_ROW - 1]]
    if uf not in ufs:
        sys.exit(f"UF {uf} não encontrada na planilha")
    col = ufs.index(uf)
    procura_codigo = termos.isdigit()
    palavras = normaliza(termos).split()
    print(f"SINAPI {mes} | {aba} ({'com' if desonerado else 'sem'} desoneração) | UF {uf} | {os.path.basename(pasta)}")
    achados = 0
    for linha in linhas:
        codigo = codigo_da_celula(linha[1])
        if not codigo:
            continue
        descricao = linha[2] or ""
        if procura_codigo:
            casa = codigo == termos
        else:
            casa = all(p in normaliza(descricao) for p in palavras)
        if casa:
            print(f"{codigo} | {descricao} | {linha[3]} | R$ {linha[col]} | %AS {linha[col + 1]}")
            achados += 1
            if achados >= limite:
                break
    if achados == 0:
        print("Nada encontrado.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("termos", help="código da composição ou palavras da descrição")
    ap.add_argument("--uf", default="RJ")
    ap.add_argument("--desonerado", action="store_true")
    ap.add_argument("--limite", type=int, default=15)
    a = ap.parse_args()
    consultar(a.termos.strip(), a.uf.upper(), a.desonerado, a.limite)
