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

### Custo por agente

```bash
python 01_CEO/_ferramentas/token_tracking/custo_por_agente.py
```

Lê os transcripts de **subagente** (`<sessionId>/subagents/agent-*.jsonl` +
`.meta.json` com o `agentType`) e mostra quanto cada agente (Kelsen, Lúcio, Hely,
Cardozo, …) gastou de fato, mais o antes/depois do corte de otimização (30/07) e
o custo das sessões principais por rotina agendada. Gera `custo_por_agente.json`
+ `RELATORIO_CUSTO_AGENTES.md`. USD por preço de tabela pública (estimativa de
ordem de grandeza, não a fatura).

Gera:
- `token_metrics.json` (nesta pasta) — por sessão + rollup semanal
- `RELATORIO_TOKENS.md` (nesta pasta) — relatório legível
- `01_CEO/Painel_Fundador/painel_economia_tokens.html` — painel do Fundador,
  estático, resolvido ao abrir; regenerado a cada execução com dados reais
  (use `--panel ""` para pular)

## Cadência — como fica registrado ao longo do tempo

Os transcripts são acumulativos: **cada execução reconstrói toda a série** desde
16/07. O histórico "de como está performando" mora em três lugares, atualizados
juntos a cada run:

1. `token_metrics.json` → chave `semanal` = uma linha por semana ISO, S29 até hoje
2. `RELATORIO_TOKENS.md` → tabela da evolução semanal + as 118 sessões
3. `painel_economia_tokens.html` → gráfico de barras da mediana semanal

Cada commit desses arquivos é um marco datado da métrica. Rodar 1x por semana
(segunda, junto da rotina) e commitar é suficiente — não precisa de cron.

> Nota: `01_CEO/Painel_Fundador/rotina_sttk_consolidada.py` está inerte
> (`repo_path` fixo em `D:\sttk-organismo`, que não existe aqui) e seu gerador de
> registro diário sobrescreve arquivos escritos à mão com texto contraditório.
> Não usar até ser consertado. Rodar `medir_tokens.py` direto.

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
