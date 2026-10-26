# Conferência das vagas — EP_v3 — 21/10/2026 (Oscar) — BLOQUEADA no passo 0

Status: **NÃO EXECUTADA. Nenhuma medição feita no modelo.** Tarefa só de leitura, pedida por Lúcio (autorização de Claudemberg via Wallenberg).

## Passo 0 — prova colada

```
vitruvius_get_revit_status        -> Error: Plugin não está conectado
vitruvius_document listar_abertos -> Error: Plugin não está conectado
vitruvius_get_document_info       -> Error: Plugin não está conectado
```

Consequência: não sei qual documento está ativo nem o isModified do RDMOB-PBA-04.rvt. Não abri o EP_v3, não fechei, salvei ou descartei nada. Nenhuma escrita no Revit.

## Tarefa 1 — largura interna das vagas cobertas
Não verificado. Motivo: plugin desconectado (ids, coordenadas e espessuras de paredes/pilares não puderam ser lidos).

## Tarefa 2 — parecer Kelsen B1 (lido: `parecer_kelsen_pendencias_21-10.md` L31–42)
Trechos: L40 "As vagas descobertas 454843 e 454851 exigem 2 árvores, e elas não estão no modelo."; L41 "O piso das vagas é \"CALCADA\". Isso afeta a permeabilidade mínima."; L42 "A faixa tem exatamente 2,50 m."
- (a) 2 árvores: não verificado no modelo (plugin desconectado). O parecer afirma que não estão.
- (b) piso/permeabilidade vs. quadro v69 (28,33%): não verificado; área dos pisos 454843/454851 não lida, conta não feita.
- (c) faixa 2,50 m, acesso e manobra: não verificado; Skill de vaga não aplicada sem geometria.

## Para retomar
Plugin Vitruvius conectado, com o RDMOB ativo e preservado; repetir o passo 0 antes de qualquer abertura.
