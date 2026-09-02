# Token Tracking — medição REAL de consumo

**Dono:** Wallenberg (CEO) · **Criado:** 02/09/2026

Ferramenta que responde, com número medido e não projetado, à pergunta que a
"Rotina de Otimização de Tokens" nunca respondeu: **o consumo de token por
conversa caiu de verdade?**

## O que é

`medir_tokens.py` lê os transcripts de sessão do Claude Code deste projeto
(`~/.claude/projects/D--000-ESTRUTURA-DEPARTAMENTO-DE-PROJETO/*.jsonl`) e extrai
o campo `message.usage` de **cada** resposta do assistente — `input_tokens`,
`cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`,
`thinking_tokens`. Sem estimativa, sem multiplicação.

Os transcripts são a fonte de verdade durável: nada a manter, é só re-rodar —
cada execução reconstrói todo o histórico desde 16/07/2026.

### Métrica principal — "contexto inicial"

No **primeiro turno real** do assistente em cada sessão:
`input_tokens + cache_creation_input_tokens + cache_read_input_tokens`.

É o tamanho do contexto montado **antes de qualquer trabalho**: system prompt +
CLAUDE.md + memória + definições de ferramentas/MCP + 1ª mensagem. É exatamente o
que os slices de CLAUDE.md (30/07) e a consolidação de MEMORY.md (29/07) deveriam
ter encolhido.

## Como rodar

```bash
python 01_CEO/_ferramentas/token_tracking/medir_tokens.py
```

ou `medir_tokens.bat` (Windows). Argumento opcional `--transcripts "<pasta>"`.

Gera, na própria pasta:
- `token_metrics.json` — por sessão + rollup semanal (consumível pelo Painel)
- `RELATORIO_TOKENS.md` — relatório legível

## Veredito da 1ª medição (02/09/2026 · 118 sessões · 16/07 → 02/09)

| Pergunta | Resposta medida |
|---|---|
| Prompt caching está ligado? | **Sim, nas 118/118 sessões.** Hit ratio médio **91,2%**. O bloqueio do Item 7 ("aguardando API Claude v1.9+") **não existe**. |
| O contexto inicial por conversa caiu? | **Não.** Base S30–S31: mediana **67,1k** → atual S35–S36: **68,8k**. Variação real: **+2,6% (aumento)**. |
| Os 45-70% de redução do plano aconteceram? | **Não há nenhum sinal disso nos dados.** A mediana semanal ficou entre 61k e 74k a rotina inteira, sem degrau após 29/07 ou 30/07. |

**Leitura:** os slices e a consolidação encolheram os *arquivos*, mas o contexto
por conversa é dominado por system prompt + definições de ferramentas/MCP, não
por CLAUDE.md. Cortar ~3k de um CLAUDE.md dentro de um contexto de ~65k é ruído.
O único ganho real e comprovado de token no período é o **prompt caching** — e
esse já vinha ligado sozinho, sem relação com o plano.

## Próximo passo sugerido

Substituir o passo "validação" da Rotina STTK Consolidada (que hoje só repete
"validado" sem medir nada) por uma execução real desta ferramenta, com o
`RELATORIO_TOKENS.md` anexado ao registro diário.
