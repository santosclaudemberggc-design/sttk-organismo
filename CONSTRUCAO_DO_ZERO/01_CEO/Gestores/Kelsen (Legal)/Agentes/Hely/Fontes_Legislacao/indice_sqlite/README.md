---
item: 4 (Rotina de Otimizacao de Tokens - Semana 2)
data: 2026-08-12
responsavel: Wallenberg (CEO)
---

# Indice Local de Legislacao (SQLite)

Cache local, somente leitura, dos parametros urbanisticos ja confirmados
e auditados pela equipe de Kelsen/Hely a partir dos PDFs em
`Fontes_Legislacao/`. Objetivo: Hely (Agente) consultar um parametro
conhecido em <1ms, sem reabrir/reler PDF nenhum — só recorre ao RIU
oficial (fonte viva) quando o dado não estiver aqui ou estiver vencido.

## Como gerar

```
python3 indice_sqlite/build_index.py
```

Reexecutavel: apaga e recria `legislacao_index.sqlite3` do zero a cada
rodada. A fonte da verdade continua sendo `_indice_fontes.md` (base
curada) + os PDFs em si — este script nunca deve ser a unica copia dos
dados.

## Schema

### `fontes` — metadados de cada PDF/norma
| coluna | tipo | notas |
|---|---|---|
| arquivo | TEXT UNIQUE | nome do arquivo em `Fontes_Legislacao/` |
| norma | TEXT | ex: "LC 270/2024" |
| titulo | TEXT | |
| data_publicacao | TEXT | ISO 8601, quando conhecida |
| status_juridico | TEXT | Valido / Revogado (parcial) / Sem efeito / Interno |
| paginas | INTEGER | |
| tamanho_bytes | INTEGER | |
| sha256 | TEXT | checksum do PDF original, para detectar substituicao silenciosa |
| oficial | INTEGER | 1 = confirmado contra fonte oficial (Busca Facil SMU / portal SMDU / DO) |
| url_oficial | TEXT | |
| observacoes | TEXT | |

### `fontes_texto` — texto por pagina, comprimido
| coluna | tipo | notas |
|---|---|---|
| fonte_id | INTEGER | FK -> fontes.id |
| pagina | INTEGER | 1-indexado |
| texto_gz | BLOB | `zlib.compress(texto_utf8, 9)` — descomprimir com `zlib.decompress` |

Guardado para auditoria/citacao (poder conferir o texto literal de um
artigo sem reabrir o PDF de 42 MB), nao para full-text search — a
consulta principal e por `parametros_urbanisticos`, direta e indexada.

### `parametros_urbanisticos` — dados que Hely realmente consulta
| coluna | tipo | notas |
|---|---|---|
| bairro | TEXT | NULL quando o parametro vale por zona, nao por bairro especifico |
| subzona | TEXT | ex: "ZRM3 D", "Setor III-H (OUC Legado Olimpico)" |
| area_planejamento | TEXT | ex: "AP4" |
| parametro | TEXT | ex: "CAB", "TO", "Gabarito (regime afastado)" |
| valor | TEXT | |
| unidade | TEXT | |
| artigo | TEXT | citacao literal do artigo/paragrafo — nunca vazio |
| fonte_id | INTEGER | FK -> fontes.id |
| data_vigor | TEXT | data de confirmacao/vigencia, ISO 8601 |
| oficial | INTEGER | 1 = conferido contra texto oficial vigente |
| observacoes | TEXT | ressalvas, condicionantes, historico de erro corrigido |

Indices: `(subzona, parametro)` e `(bairro)`.

## Regra de integridade dos dados (nao violar em atualizacoes futuras)

Toda linha de `parametros_urbanisticos` foi transcrita de
`_indice_fontes.md` com o artigo exato ja auditado por Kelsen/Hely —
nenhum valor foi inferido ou calculado por este script. So os 2
enderecos/zonas ja testados e confirmados (ZRM3 D/AP4 - Recreio dos
Bandeirantes; Setor III-H - OUC Legado Olimpico) tem linha aqui. Isso e
proposital: este indice e um **cache do que ja foi confirmado**, nao uma
tabela completa de zoneamento da cidade — o RIU oficial
(`pgeo3.rio.rj.gov.br`, ver `_indice_fontes.md`) continua sendo a fonte
viva para lotes ainda nao testados. Ao adicionar um novo caso
confirmado, seguir o mesmo padrao: artigo exato, `oficial=1` so quando
conferido contra texto vigente, `observacoes` com qualquer condicionante.

## Validacao (12/08/2026)

- 27 PDFs processados, 1035 paginas, 0 falhas de parsing.
- 14 linhas em `parametros_urbanisticos`, 0 orfas (todas com `fonte_id`
  valido).
- Consulta pontual (`subzona`+`parametro`) medida em **0,05 ms**; leitura
  de 1 pagina de texto comprimido em **0,17 ms** — bem abaixo da meta de
  50-100 ms do plano da Semana 2.
- Tamanho final do `.sqlite3`: **1,18 MB** (meta: ate 2 MB).
- `Decreto55622_2025_AnexoI_ModelosDULI.pdf` extrai 0 bytes de texto —
  confirma o que `_indice_fontes.md` ja registrava (Anexo I e imagem
  pura, so legivel por rasterizacao).
