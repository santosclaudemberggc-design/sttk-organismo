---
item: 5
data: 2026-08-13
responsavel: Wallenberg (CEO STTK)
---

# Drive Cache — Item 5 (Google Drive Cache Incremental)

Cache local (SQLite) de metadados do Google Drive para as 3 árvores que Hely,
Kelsen e Lúcio consultam com mais frequência: **POPs** (`001_PROCEDIMENTOS`),
**Memoriais** (`006_MEMORIAIS DESCRITIVOS`) e **Clientes** (`000_CLIENTES`).
Guarda `id`, `path` e `modifiedTime` de cada arquivo/pasta pra permitir que um
Agente confira "esse doc mudou desde a última vez que eu li?" com uma consulta
SQLite local (sub-milissegundo) em vez de um round-trip ao Drive via MCP.

## Como funciona (arquitetura real)

Diferente do índice de legislação do Item 4 (que processa PDFs já baixados
localmente), o Drive não tem um espelho local — a fonte de verdade é remota.
Por isso a responsabilidade é dividida:

1. **Descoberta** (quem tem as credenciais MCP do Drive): percorre as pastas
   via `search_files(parentId=...)` e grava um **snapshot JSON**
   (`drive_snapshot_full_AAAAMMDD.json`) — lista de records com
   `id/title/mimeType/parentId/modifiedTime/path/root_scope`.
2. **`build_drive_cache.py`** (reexecutável, puro stdlib): consome o
   snapshot, faz upsert no SQLite comparando `modified_time` contra o que já
   está cacheado, e reporta o diff (novos/atualizados/inalterados/removidos).

Rodar o script de novo com um snapshot mais recente = sync incremental. Ele
nunca fala com a API do Google sozinho — não guarda nem precisa de
credenciais.

## Schema (`drive_cache.sqlite3`)

**`drive_files`**
| coluna | conteúdo |
|---|---|
| `id` | fileId do Drive (PK) |
| `title`, `mime_type`, `parent_id`, `path` | metadados + caminho legível |
| `root_scope` | `POPs` / `Memoriais` / `Clientes` / `ROOT` |
| `modified_time` | `modifiedTime` do Drive — campo usado pro diff |
| `leaf_synced` | `0` = pasta descoberta mas conteúdo ainda não enumerado (ver "Cobertura" abaixo) |
| `first_seen_at`, `last_synced_at`, `removed_at` | controle de sync |

**`sync_runs`** — histórico de execuções (modo, contadores, timestamp), pra auditoria.

## Regra de integridade dos dados

Nenhum `modifiedTime` é inferido ou aproximado — vem literalmente do campo
`modifiedTime` retornado pelo Drive na descoberta. O diff (novo/atualizado/
inalterado) é uma comparação de string exata contra o valor já cacheado.
`removed_count` (sweep de exclusão) só roda em `--mode full`, porque exige
que o snapshot cubra 100% da árvore daquele `root_scope` — um snapshot
incremental parcial não pode ser usado pra concluir que algo sumiu.

## Cobertura da primeira sincronização (13/08/2026, 09:00 UTC)

94 objetos (52 pastas + 42 arquivos) descobertos em 23 chamadas
`search_files` (uma por pasta visitada — busca só metadados, sem baixar
conteúdo):

- **POPs**: 100% enumerado até o arquivo-folha (30 objetos) — as 5 pastas
  "GESTOR {ÁREA}" e seus documentos, exceto a subárvore `OUTROS/` (3 pastas
  descobertas, conteúdo não enumerado — fora do escopo dos 3 Gestores
  ativos).
- **Memoriais**: 100% enumerado até o arquivo-folha para as 4 pastas
  "GESTOR {ÁREA}" ativas (28 objetos). `ESPECIAIS/` (Reforma/Retrofit/Home
  Staging) foi descoberta mas não recursada — regra de escopo já confirmada
  em `memory/referencia/sttickler_drive_estrutura.md`: essas 3 subpastas
  ficam fora do organismo "Construção do Zero".
  Regra: pasta nomeada Reforma/Retrofit/Home Staging (Especiais) é excluída
  do organismo; o resto entra.
- **Clientes**: estrutura de pastas 100% mapeada (2 bairros, 3 clientes: 
  Daniel-OB, Maria Oliveira, Cidade Arte Barra); enumeração de arquivo-folha
  completa só para Daniel-OB (`00PN-PROGRAMA DE NECESSIDADES`) e o nível
  raiz de Cidade Arte Barra. **30 pastas ficaram com `leaf_synced=0`**
  (12 etapas de Maria Oliveira, 2 revisões de Daniel-OB, 9 pastas "Modelo"
  de Cidade Arte Barra, listadas no `drive_snapshot_full_20260813.json`) —
  não foram abertas nesta rodada por orçamento de tempo do bloco de 2h do
  Item 5. A estrutura (nomes, ids, modifiedTime das próprias pastas) já está
  cacheada; o conteúdo interno delas é preenchido na próxima execução do
  script com um snapshot mais completo. Nenhum dado foi inventado — o que
  não foi aberto está marcado como não aberto, não omitido silenciosamente.

## Validação (13/08/2026)

- ✅ Sync completo: 94/94 registros inseridos sem erro, banco de 60 KB.
- ✅ Consulta por `root_scope` (30-34 linhas): **0,024 ms/consulta** (média de 200 execuções).
- ✅ Lookup por `id` (ponto único): **0,007 ms/consulta** (média de 200 execuções).
- ✅ Teste de sync incremental (nº 1) — reprocessar o mesmo snapshot: `0 novos, 0 atualizados, 94 inalterados`. Confirma que o cache é estável quando nada mudou no Drive.
- ✅ Teste de sync incremental (nº 2) — snapshot sintético com 1 `modifiedTime` alterado (arquivo "POP – LIBERAÇÃO DE OBRA"): `0 novos, 1 atualizado, 93 inalterados`. Confirma que o diff por `modifiedTime` isola corretamente só o arquivo que mudou, sem re-marcar os outros 93. Cache restaurado ao estado real (full sync original) depois do teste — o dado sintético não ficou no banco final.
- **Fonte da verdade continua sendo o Google Drive** — o SQLite é cache derivado, reconstruível a qualquer momento rodando o script com um snapshot novo; não substitui uma leitura direta via MCP quando o Agente precisa do conteúdo completo de um arquivo (só evita ficar checando "mudou ou não" a cada conversa).

## Métricas

**Antes:**
- `search_files()` do Drive a cada conversa de um Agente (Hely/Kelsen/Lúcio) que precisa checar POPs/Memoriais/Clientes → overhead de 3-5 chamadas MCP por conversa (chamada de rede real ao Drive a cada vez).

**Depois:**
- Consulta ao cache SQLite local: 0,007-0,024 ms por consulta (sub-milissegundo, medido).
- Overhead de MCP por conversa cai para ~0 chamadas na maioria dos casos (Agente confere `modified_time` no cache); só volta a chamar o Drive quando o cache aponta uma mudança real ou quando o Agente precisa do conteúdo integral do arquivo (não só metadados).
- Sync (descoberta) roda fora da conversa do Agente — 1x por execução do processo de background, não por conversa.

**Redução:**
- Chamadas MCP por conversa: 3-5 → ~0-1 (próximo da meta de 90% ↓ do plano; não cravamos "90%" exato porque o baseline "3-5 chamadas/conversa" é uma estimativa do plano, não uma medição de produção).
- Economia de tokens por conversa: **estimativa de 10-15% (meta do plano), ainda a validar com uso real em produção** — mesma ressalva que o Item 4 registrou para sua própria estimativa (20-25%), a ser confirmada no item de Validação de 15/08.
- Acumulado Semana 2 (Itens 4+5, ambos parciais/estimados até validação real): 20-25% (Item 4, medido em latência mas estimado em token) + 10-15% (Item 5, estimado) ≈ **30-40%**.

## Reexecutar

```bash
# sync completo (recalcula removidos; usar quando o snapshot cobre a árvore inteira)
python3 build_drive_cache.py --input drive_snapshot_full_AAAAMMDD.json --mode full

# sync incremental (upsert; não mexe em removidos)
python3 build_drive_cache.py --input novo_snapshot.json --mode incremental
```

Um novo snapshot é gerado por quem tiver as ferramentas MCP do Drive
carregadas (`search_files(parentId=...)` por pasta), no mesmo formato de
`drive_snapshot_full_20260813.json`.
