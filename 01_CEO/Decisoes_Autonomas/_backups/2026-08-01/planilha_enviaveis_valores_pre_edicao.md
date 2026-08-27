# Backup — valores pré-edição, Planilha de Enviáveis (item `planilha-enviaveis-recusada`)

**Data:** 01/08/2026, antes da execução da substituição via Google Sheets API (Service Account).

## Arquivo 1 — CANÔNICO — "Controle de entregáveis para arq. externos"
ID: `10i300eMN-r7iqLX2rQNet8hqQsygaOTvfmCo1N0nsMQ`, aba `ARQUITETÔNICA`

- linha 27: `['', 'Fachadas legais', 'Fachadas para aprovação legal ']`
- linha 29: `['', 'Memorial descritivo', 'Memorial para protocolo legal']`

## Arquivo 2 — DUPLICATA — "Controle Enviável Externos - ARQUITETÔNICO"
ID: `14xgk56lVAPzxD0S5OM_PICOx11HyVpuHZO_x4-aDFdk`, aba `Página1`

- linha 29: `['', 'Fachadas legais', 'Fachadas para aprovação legal']`
- linha 31: `['', 'Memorial descritivo', 'Memorial para protocolo legal']`

## Arquivo 3 — VARIANTE — "Controle Interno - Arquiteto"
ID: `1xSlZdU6DDWEChbZycis1WuGJgADFeBLJ1d4c8SleyCA`, aba `Página1`

- linha 37: `['', 'Fachadas legais', 'Fachadas aprovativas', ...]` (coluna C = descrição)
- linha 39: `['', 'Memorial legal', 'Memorial descritivo legal', ..., col N='Texto jurídico', ...]` (colunas B e C alteradas; coluna N não tocada)

## Como desfazer
Rodar `spreadsheets().values().update()` (Sheets API v4, Service Account `sttickler-ceo-bot`) restaurando os valores acima nas mesmas células (B/C das linhas indicadas).
