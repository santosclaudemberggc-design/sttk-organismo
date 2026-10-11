#!/usr/bin/env python3
"""
Item 4 (12/08/2026) - Indexacao Local de Legislacao (SQLite)
Le os PDFs de Fontes_Legislacao/, extrai texto (pypdf) e grava um indice
SQLite local: metadados por norma (fontes), texto por pagina comprimido
(fontes_texto) e parametros urbanisticos ja confirmados/auditados pela
equipe de Kelsen/Hely (parametros_urbanisticos).

Nenhum valor de parametros_urbanisticos foi inventado por este script:
todos vem, transcritos com artigo exato, de `_indice_fontes.md` (base
curada e auditada em varias rodadas por Kelsen/Wallenberg/Claudemberg).
Este script e re-executavel: apaga e recria o .sqlite3 do zero a cada
rodada (fonte da verdade continua sendo _indice_fontes.md + os PDFs).
"""
import glob
import hashlib
import os
import sqlite3
import zlib

import pypdf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Fontes_Legislacao/
OUT_DIR = os.path.dirname(os.path.abspath(__file__))                    # Fontes_Legislacao/indice_sqlite/
DB_PATH = os.path.join(OUT_DIR, "legislacao_index.sqlite3")

SCHEMA = """
CREATE TABLE fontes (
    id               INTEGER PRIMARY KEY,
    arquivo          TEXT NOT NULL UNIQUE,
    norma            TEXT,               -- ex: "LC 270/2024"
    titulo           TEXT,
    data_publicacao  TEXT,               -- ISO 8601 quando conhecida
    status_juridico  TEXT,               -- Valido / Revogado (parcial) / Sem efeito / Interno
    paginas          INTEGER,
    tamanho_bytes    INTEGER,
    sha256           TEXT,
    oficial          INTEGER NOT NULL,   -- 1 = confirmado contra fonte oficial (Busca Facil SMU / portal SMDU / DO)
    url_oficial      TEXT,
    observacoes      TEXT
);

CREATE TABLE fontes_texto (
    id        INTEGER PRIMARY KEY,
    fonte_id  INTEGER NOT NULL REFERENCES fontes(id),
    pagina    INTEGER NOT NULL,
    texto_gz  BLOB,                      -- texto da pagina, zlib nivel 9
    UNIQUE(fonte_id, pagina)
);
CREATE INDEX idx_fontes_texto_fonte ON fontes_texto(fonte_id);

CREATE TABLE parametros_urbanisticos (
    id                 INTEGER PRIMARY KEY,
    bairro             TEXT,             -- NULL quando o parametro vale por zona, nao por bairro especifico
    subzona            TEXT NOT NULL,    -- ex: "ZRM3 D", "Setor III-H (OUC Legado Olimpico)"
    area_planejamento  TEXT,             -- ex: "AP4"
    parametro           TEXT NOT NULL,   -- ex: "CAB", "CAM", "TO", "Gabarito_afastado"
    valor              TEXT NOT NULL,
    unidade            TEXT,
    artigo             TEXT NOT NULL,    -- citacao literal do artigo/paragrafo
    fonte_id           INTEGER REFERENCES fontes(id),
    data_vigor         TEXT,             -- data de confirmacao/vigencia (ISO 8601)
    oficial            INTEGER NOT NULL, -- 1 = conferido contra texto oficial vigente
    observacoes        TEXT
);
CREATE INDEX idx_param_lookup ON parametros_urbanisticos(subzona, parametro);
CREATE INDEX idx_param_bairro ON parametros_urbanisticos(bairro);
"""

# Metadados por arquivo, transcritos de _indice_fontes.md (secoes "Status
# oficial das normas", "Arquivos acrescentados nesta data" e as entradas
# individuais por norma). Onde o indice nao descreve o arquivo em detalhe,
# isso fica registrado em observacoes em vez de inventado.
FONTES_META = {
    "COES_LeiComplementar198_2019.pdf": dict(
        norma="LC 198/2019", titulo="Codigo de Obras e Edificacoes Simplificado (COES) - texto original",
        data_publicacao="2019-01-14", status_juridico="Valido",
        oficial=1, url_oficial="data.rio (portal PrefeituraRio)",
        observacoes="Baixado 13/07/2026. Alterado 2x (LC 283/2025, LC 291/2025) - preferir a versao CONSOLIDADO_SMU para leitura corrente."),
    "COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf": dict(
        norma="LC 198/2019 (consolidada)", titulo="COES consolidado, PDF gerado pela Busca Facil da SMU",
        data_publicacao="2026-01-07", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Versao de referencia do COES a partir de 21/07/2026 - unica que traz as duas alteracoes (LC283, LC291) embutidas."),
    "COES_LeiComplementar198_2019_impressaoWeb_Claudemberg.pdf": dict(
        norma="LC 198/2019", titulo="COES, impressao web fornecida por Claudemberg",
        data_publicacao="2026-07-21", status_juridico="Valido",
        oficial=1, url_oficial=None,
        observacoes="Texto normativo identico a versao de 13/07/2026 - preservado para rastreabilidade (Principio 8)."),
    "Decreto42_2018_COSCIP_COMPILADO.pdf": dict(
        norma="Decreto Estadual 42/2018", titulo="COSCIP (Codigo de Seguranca Contra Incendio e Panico) - compilado",
        data_publicacao="2018-01-01", status_juridico="Valido",
        oficial=1, url_oficial=None,
        observacoes="Arquivado 28/07/2026 (pendencia B10). Auditoria de Kelsen em 28/07/2026 confirmou achado com uma correcao de precisao."),
    "Decreto51503_2022_CriteriosLAM_AnexoI.pdf": dict(
        norma="Decreto 51.503/2022", titulo="Criterios LAM, Anexo I",
        data_publicacao="2022-01-01", status_juridico=None,
        oficial=0, url_oficial=None,
        observacoes="Sem descricao detalhada no _indice_fontes.md ate esta rodada - nao auditado, nao usar como fonte de parametro sem conferencia."),
    "Decreto55621_2025_MemorialTecnicoAmbiental.pdf": dict(
        norma="Decreto 55.621/2025", titulo="Memorial Tecnico Ambiental",
        data_publicacao="2025-01-01", status_juridico=None,
        oficial=0, url_oficial=None,
        observacoes="Sem descricao detalhada no _indice_fontes.md ate esta rodada - nao auditado, nao usar como fonte de parametro sem conferencia."),
    "Decreto55622_2025_AnexoII_TermosDeclaracoes.pdf": dict(
        norma="Decreto 55.622/2025, Anexo II", titulo="LICIN 2.0 - Termos e Declaracoes",
        data_publicacao="2025-01-01", status_juridico="Valido",
        oficial=1, url_oficial="desenvolvimentourbano.prefeitura.rio/licenciamento-integrado-licin",
        observacoes="3 pp, texto extraivel. Usar este arquivo (nao as pp. 9-11 do corpo do decreto, que sao imagem)."),
    "Decreto55622_2025_AnexoI_ModelosDULI.pdf": dict(
        norma="Decreto 55.622/2025, Anexo I", titulo="LICIN 2.0 - Modelos graficos do DULI",
        data_publicacao="2025-01-01", status_juridico="Valido",
        oficial=1, url_oficial="desenvolvimentourbano.prefeitura.rio/licenciamento-integrado-licin",
        observacoes="2 pp em A0, IMAGEM PURA - extracao de texto retorna vazio (confirmado por este build; ler so por rasterizacao, pdftoppm -r 200)."),
    "Decreto55622_2025_LICIN2.0.pdf": dict(
        norma="Decreto 55.622/2025", titulo="LICIN 2.0 - corpo do decreto",
        data_publicacao="2025-01-01", status_juridico="Valido",
        oficial=1, url_oficial="desenvolvimentourbano.prefeitura.rio/licenciamento-integrado-licin/.../ato_55622.pdf",
        observacoes="14 pp. Lei central do Projeto Legal; ausente da pasta ate 21/07/2026. pp.9-11 sao imagem (usar AnexoII a parte)."),
    "Decreto55622_2025_PublicacaoDO.pdf": dict(
        norma="Decreto 55.622/2025", titulo="LICIN 2.0 - publicacao no Diario Oficial",
        data_publicacao="2025-01-01", status_juridico="Valido",
        oficial=1, url_oficial="desenvolvimentourbano.prefeitura.rio/.../Decreto-55.622-Versao-DO.pdf",
        observacoes="5 pp."),
    "Decreto56561_2025_UsosPorZona_AnexosICES.pdf": dict(
        norma="Decreto 56.561/2025", titulo="Regulamenta Anexo XVIII da LC 270/2024 - usos por CNAE e por zona",
        data_publicacao="2025-08-05", status_juridico="Valido",
        oficial=1, url_oficial="desenvolvimentourbano.prefeitura.rio",
        observacoes="Baixado 15/07/2026. 5 anexos (I a V, um por Area de Planejamento; IV=AP4). So legivel via pdftotext -layout local (WebFetch direto falhou)."),
    "LC270_2024_PlanoDiretorLUOS.pdf": dict(
        norma="LC 270/2024", titulo="Plano Diretor / LUOS (Politica Urbana e Ambiental do Municipio)",
        data_publicacao="2024-01-16", status_juridico="Valido",
        oficial=1, url_oficial="Camara Municipal do Rio de Janeiro",
        observacoes="384 pp, fornecida por Claudemberg 13/07/2026. Alterada 6x - Busca Facil SMU alerta para conferir LC301/2026."),
    "LC274_2024.pdf": dict(
        norma="LC 274/2024", titulo="Altera/regulamenta instrumentos da LC 270/2024 - texto original",
        data_publicacao="2024-07-17", status_juridico="Valido (parcialmente revogado)",
        oficial=1, url_oficial="desenvolvimento.prefeitura.rio",
        observacoes="SEM notas de revogacao. Arts. 5-14, 17-23, 26 e 38 REVOGADOS pela LC 281/2025 Art.42,II - preferir o CONSOLIDADO."),
    "LC274_2024_CONSOLIDADO.pdf": dict(
        norma="LC 274/2024 (consolidada)", titulo="LC 274/2024 com notas de revogacao embutidas",
        data_publicacao="2024-07-17", status_juridico="Valido (parcialmente revogado)",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Versao de referencia a partir de 21/07/2026 - traz as notas de revogacao que o arquivo original nao tem."),
    "LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf": dict(
        norma="LC 281/2025", titulo="Condicoes especiais de licenciamento (consolidada)",
        data_publicacao="2025-05-30", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Arts. 18-19 = calculo e pagamento de contrapartida (outorga onerosa). Revoga blocos da LC 274/2024."),
    "LC283_2025_AlteraCOES_Art35.pdf": dict(
        norma="LC 283/2025", titulo="Altera COES Art. 35 (dutos no passeio)",
        data_publicacao="2025-07-14", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Acrescenta COES Art.35 §7º - obrigatoriedade de dutos no passeio em toda edificacao nova."),
    "LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf": dict(
        norma="LC 284/2025", titulo="Operacao Urbana Consorciada do Parque do Legado Olimpico Rio 2016",
        data_publicacao="2025-07-17", status_juridico="Valido (vigencia escalonada)",
        oficial=1, url_oficial="mail.camara.rj.gov.br/APL/Legislativos/contlei.nsf",
        observacoes="Art.51: soh Arts.21,22,49 valem desde a publicacao; demais artigos (incl. Art.12, parametros por subsetor) dependem de condicionantes do Art.21 I e III, nao confirmadas nesta rodada."),
    "LC291_2025_SupermercadosShoppingsHospitais.pdf": dict(
        norma="LC 291/2025", titulo="Supermercados, shoppings e hospitais - altera LC 270 e LC 281",
        data_publicacao="2025-12-01", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Acrescenta COES Art.2º §7º via LC291 Art.8º (nao Arts.4/8/31, como uma fonte secundaria antiga sugeria)."),
    "LC292_2025_RiscoEstrutural.pdf": dict(
        norma="LC 292/2025", titulo="Risco estrutural - regulamenta LC 270 Art.284,III",
        data_publicacao="2025-12-02", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil", observacoes=None),
    "LC299_2026_AlteraLC270_Art371.pdf": dict(
        norma="LC 299/2026", titulo="Nova redacao ao LC 270 Art.371 §5º (grupamentos de interesse social)",
        data_publicacao="2026-01-09", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil", observacoes=None),
    "LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf": dict(
        norma="LC 301/2026", titulo="AEIU Praca Onze - altera LC 270 e LC 281",
        data_publicacao="2026-07-09", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="Norma mais recente da pasta. Prorroga o prazo do Art.40 da LC281/2025 para 01/12/2026 (Art.58)."),
    "NT1-07_AtividadesEconomicasBaixoRisco_2020.pdf": dict(
        norma="NT 1-07 CBMERJ", titulo="Atividades economicas de baixo risco",
        data_publicacao="2020-01-01", status_juridico="Valido",
        oficial=1, url_oficial=None,
        observacoes="Arquivado 28/07/2026 (pendencia B10) - nao reintroduz obrigacao para unifamiliar puro."),
    "ResolucaoSMAC512_2012_PGRCC_VALIDO.pdf": dict(
        norma="Resolucao SMAC 512/2012", titulo="PGRCC (Plano de Gerenciamento de Residuos da Construcao Civil)",
        data_publicacao="2012-01-01", status_juridico="Valido",
        oficial=1, url_oficial=None, observacoes=None),
    "ResolucaoSMDEIS03_2023_SubstituicaoPREO.pdf": dict(
        norma="Resolucao EIS-REN 3/2023", titulo="Procedimento de substituicao do PREO",
        data_publicacao="2023-03-03", status_juridico="Valido",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil", observacoes=None),
    "ResolucaoSMDEIS06_2023_ProcedimentosLAM_VALIDO.pdf": dict(
        norma="Resolucao SMDEIS 06/2023", titulo="Procedimentos LAM",
        data_publicacao="2023-01-01", status_juridico="Valido",
        oficial=1, url_oficial=None, observacoes=None),
    "ResolucaoSMDEIS27_2021_LICIN_BaixaComplexidade_SEM_EFEITO.pdf": dict(
        norma="Resolucao SMDEIS 27/2021", titulo="Rito simplificado LICIN para unifamiliar/bifamiliar",
        data_publicacao="2021-11-10", status_juridico="Sem efeito",
        oficial=1, url_oficial="www2.rio.rj.gov.br/smu/buscafacil",
        observacoes="NAO VALE MAIS - preservado na pasta so para rastreabilidade (Principio 8)."),
    "_indice_fontes.pdf": dict(
        norma=None, titulo="Indice de fontes legislativas - Kelsen (export em PDF do _indice_fontes.md)",
        data_publicacao=None, status_juridico="Interno",
        oficial=0, url_oficial=None,
        observacoes="Documento interno de curadoria (nao e norma primaria) - fonte dos dados de parametros_urbanisticos deste indice."),
}

# Parametros urbanisticos confirmados/auditados - transcritos com artigo
# exato de _indice_fontes.md. Nao inventar linha nova aqui sem o artigo
# correspondente conferido contra o texto oficial.
PARAMETROS = [
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="CAB",
         valor="0,8", unidade="coeficiente", artigo="LC 270/2024, Art. 345 §4º III 'e' item 2",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-21", oficial=1,
         observacoes="Regra geral CAB=1,0 e Art.103 par. unico. Endereco corrigido em 21/07/2026 (alineas estavam trocadas: base antiga citava 'f'/'e')."),
    dict(bairro=None, subzona="ZRM2 B, D, E, F, G, H, M", area_planejamento="AP4", parametro="CAB",
         valor="0,6", unidade="coeficiente", artigo="LC 270/2024, Art. 345 §4º III 'd' item 2",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-21", oficial=1, observacoes=None),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="CAM",
         valor="1,0", unidade="coeficiente", artigo="LC 270/2024, Art. 104, 107; Anexo XXI (AP4)",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1, observacoes=None),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="TO",
         valor="50", unidade="%", artigo="LC 270/2024, Art. 349 (formula); Anexo XXI (AP4)",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1,
         observacoes="Formula: (area de projecao horizontal x 100) / area do terreno."),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="SMD (taxa de permeabilidade)",
         valor="20", unidade="%", artigo="LC 270/2024, Art. 351-353",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1,
         observacoes="Regra geral (20% da area livre resultante da TO maxima). O valor 70% e so para bairros da AP3 (ilha de calor) - nao se aplica a AP4."),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="Gabarito (regime afastado)",
         valor="6 pav / 20 m", unidade="pavimentos/altura", artigo="LC 270/2024, Anexo XXI (AP4)",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1, observacoes=None),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="Gabarito (regime nao afastado)",
         valor="4 pav / 14 m", unidade="pavimentos/altura", artigo="LC 270/2024, Anexo XXI (AP4)",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1, observacoes=None),
    dict(bairro=None, subzona="ZRM3 D", area_planejamento="AP4", parametro="Afastamento frontal",
         valor="5", unidade="m", artigo="LC 270/2024, Anexo XXI (AP4); regra geral 3m no Art.363",
         fonte_arquivo="LC270_2024_PlanoDiretorLUOS.pdf", data_vigor="2026-07-13", oficial=1,
         observacoes="Excecao: lotes sob abrangencia do Decreto 3.046/1981 ficam fora da regra geral (Art.363 §1º III) - checar caso a caso, nao presumir aplicacao nem exclusao."),
    dict(bairro=None, subzona="qualquer (multifamiliar)", area_planejamento=None,
         parametro="Afastamento lateral/fundos - piso minimo", valor="2,50", unidade="m",
         artigo="COES (LC 198/2019), Art. 4º, II",
         fonte_arquivo="COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf", data_vigor="2026-07-20", oficial=1,
         observacoes="Piso INCONDICIONAL - nao depende de regime de gabarito. Corrigido em 20/07/2026 apos erro replicado em 3 rodadas do caso Bittencourt (ver _indice_fontes.md, secao COES)."),
    dict(bairro=None, subzona="qualquer (uni/bifamiliar)", area_planejamento=None,
         parametro="Afastamento lateral/fundos - piso minimo", valor="1,50", unidade="m",
         artigo="COES (LC 198/2019), Art. 31, paragrafo unico",
         fonte_arquivo="COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf", data_vigor="2026-07-20", oficial=1,
         observacoes="Aplica-se a edificacao unifamiliar ou bifamiliar - nao usar o piso de 2,50m do Art.4º sem passar por este artigo antes."),
    dict(bairro=None, subzona="Setor III-H (OUC Legado Olimpico, area receptora)", area_planejamento="AP4",
         parametro="CAM", valor="3", unidade="coeficiente",
         artigo="LC 284/2025, Art. 12, VI",
         fonte_arquivo="LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf", data_vigor="2026-07-15", oficial=1,
         observacoes="Condicionado a TDC formal (Art.9 §1º, Art.14) e a vigencia escalonada do Art.51 - condicionantes do Art.21 I/III nao confirmadas como satisfeitas nesta rodada."),
    dict(bairro=None, subzona="Setor III-H (OUC Legado Olimpico, area receptora)", area_planejamento="AP4",
         parametro="TO", valor="30", unidade="%",
         artigo="LC 284/2025, Art. 12, VI",
         fonte_arquivo="LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf", data_vigor="2026-07-15", oficial=1,
         observacoes="Mesma condicionante da linha de CAM acima."),
    dict(bairro=None, subzona="Setor III-H (OUC Legado Olimpico, area receptora)", area_planejamento="AP4",
         parametro="Gabarito", valor="12 pav / 36 m", unidade="pavimentos/altura",
         artigo="LC 284/2025, Art. 12, VI",
         fonte_arquivo="LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf", data_vigor="2026-07-15", oficial=1,
         observacoes="Uso permitido restrito a 'residencial multifamiliar' pela alinea 'd' - sem abertura para comercial/servicos, diferente de outros subsetores da mesma lei."),
    dict(bairro=None, subzona="ZRM3", area_planejamento="AP4", parametro="Uso permitido - CNAE 86.3 (clinica medica/odontologica)",
         valor="S-II (Uso de Servicos II)", unidade=None,
         artigo="Decreto 56.561/2025, Anexo IV (AP4), Secao Q, Grupo 86.3",
         fonte_arquivo="Decreto56561_2025_UsosPorZona_AnexosICES.pdf", data_vigor="2026-07-15", oficial=1,
         observacoes="Clinica privada com fins lucrativos NAO se enquadra em 'Uso Institucional de interesse publico' (LC270 Art.338 XVI)."),
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    fonte_id_by_arquivo = {}
    total_paginas = 0
    pdf_files = sorted(glob.glob(os.path.join(BASE_DIR, "*.pdf")))

    for path in pdf_files:
        arquivo = os.path.basename(path)
        meta = FONTES_META.get(arquivo, {})
        try:
            reader = pypdf.PdfReader(path)
            paginas = len(reader.pages)
        except Exception as exc:
            print(f"AVISO: falha ao abrir {arquivo}: {exc}")
            reader = None
            paginas = 0

        cur = conn.execute(
            """INSERT INTO fontes
               (arquivo, norma, titulo, data_publicacao, status_juridico,
                paginas, tamanho_bytes, sha256, oficial, url_oficial, observacoes)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (
                arquivo,
                meta.get("norma"),
                meta.get("titulo"),
                meta.get("data_publicacao"),
                meta.get("status_juridico"),
                paginas,
                os.path.getsize(path),
                sha256_of(path),
                meta.get("oficial", 0),
                meta.get("url_oficial"),
                meta.get("observacoes"),
            ),
        )
        fonte_id = cur.lastrowid
        fonte_id_by_arquivo[arquivo] = fonte_id
        total_paginas += paginas

        if reader is not None:
            for i, page in enumerate(reader.pages, start=1):
                try:
                    texto = page.extract_text() or ""
                except Exception:
                    texto = ""
                texto_gz = zlib.compress(texto.encode("utf-8"), 9)
                conn.execute(
                    "INSERT INTO fontes_texto (fonte_id, pagina, texto_gz) VALUES (?,?,?)",
                    (fonte_id, i, texto_gz),
                )
        print(f"  parsed {arquivo:55s} paginas={paginas:4d}")

    for p in PARAMETROS:
        fonte_id = fonte_id_by_arquivo.get(p["fonte_arquivo"])
        conn.execute(
            """INSERT INTO parametros_urbanisticos
               (bairro, subzona, area_planejamento, parametro, valor, unidade,
                artigo, fonte_id, data_vigor, oficial, observacoes)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (
                p["bairro"], p["subzona"], p["area_planejamento"], p["parametro"],
                p["valor"], p["unidade"], p["artigo"], fonte_id, p["data_vigor"],
                p["oficial"], p["observacoes"],
            ),
        )

    conn.commit()
    conn.execute("VACUUM")
    conn.close()

    size_mb = os.path.getsize(DB_PATH) / 1024 / 1024
    print(f"\nPDFs processados: {len(pdf_files)}")
    print(f"Paginas totais: {total_paginas}")
    print(f"Linhas de parametros_urbanisticos: {len(PARAMETROS)}")
    print(f"Banco gravado em: {DB_PATH}")
    print(f"Tamanho final: {size_mb:.2f} MB (meta: ate 2 MB)")


if __name__ == "__main__":
    build()
