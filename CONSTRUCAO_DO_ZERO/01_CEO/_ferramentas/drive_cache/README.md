# Cache Incremental do Google Drive — Item 5

**Status:** executado em 13/08/2026 (atrasado — previsto no plano para 13/08, executado retroativamente em 14/08 como parte da rotina que cobriu Item 3, 5 e 6 pendentes).

## O que existe

- `cache_recentes.json` — snapshot real de 15 arquivos do Drive (chamada única a `mcp__Google_Drive__list_recent_files`, `orderBy=lastModified`, só metadado — nenhum conteúdo de arquivo de cliente foi baixado). Chave: `fileId`. Valor: `title`, `modifiedTime`, `parentId`, `mimeType`, `fileSize`.
- `sync_incremental.py` — `diff(cache_antigo, arquivos_buscados)` compara `modifiedTime` por `fileId` e classifica em `novos` / `modificados` / `inalterados`; `is_cache_fresh(cache, ttl_horas)` decide se vale chamar a MCP de novo ou servir do cache local.

## Testes rodados (reais, não estimados)

1. Cache comparado contra si mesmo → `0 novos, 0 modificados, 15 inalterados`. Confirma que rodar a mesma sincronização duas vezes seguidas não gera trabalho redundante.
2. Cache vazio (primeira sincronização) → `15 novos`. Confirma que a primeira sincronização do dia busca tudo, como o plano previa.
3. 1 arquivo com `modifiedTime` alterado (simulado) → `1 modificado, 14 inalterados`. Confirma que o diff distingue corretamente arquivo mudado de arquivo parado.

`python3 sync_incremental.py` roda os três com `assert` — falha alto e visível se a lógica quebrar.

## Métrica — honesta, com o mesmo cuidado do Item 6

**O que foi medido de verdade nesta execução:** para obter metadado de 15 arquivos, esta rotina fez **1 chamada MCP** (`list_recent_files`), não 15 chamadas individuais de `get_file_metadata`. Isso é uma redução real de 15 → 1 (93%) **para a operação de listagem em si**.

**O que o plano pedia (10-15% de economia de tokens por conversa) não foi medido nem confirmado aqui** — depende da taxa de acerto do cache ao longo de múltiplas conversas em produção (quantas vezes um Gestor pergunta por um arquivo que já está no cache local vs. um que não está), e isso não existe ainda: é a primeira sincronização, cache_recentes.json tem 1 snapshot, não histórico. Mantenho a faixa do plano (10-15%) como estimativa não validada — mesmo tratamento dado ao Item 4 em 12/08.

## Limitações declaradas

- Cobre só os 15 arquivos mais recentes retornados por `list_recent_files` — não é uma sincronização completa das pastas POPs/Memoriais/Clientes citadas no plano original (isso exigiria `search_files` com `parentId` por pasta, varredura mais ampla; não foi feito aqui para manter o escopo de leitura mínima em uma rotina automática sem supervisão ao vivo).
- Nenhum conteúdo de arquivo foi baixado nem lido — só metadado (nome, id, data de modificação, tamanho, pasta). Adequado para decidir "isso mudou, vale a pena buscar o conteúdo" sem tocar em dado de cliente.
- Não há agendamento automático de resync ainda (a parte "1ª sincronização/hora" do plano) — `is_cache_fresh()` existe e está testada, mas não está conectada a um cron/trigger. Registrar como pendência, não como feito.
