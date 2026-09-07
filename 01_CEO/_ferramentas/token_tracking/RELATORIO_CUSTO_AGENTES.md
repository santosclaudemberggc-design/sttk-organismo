# Custo por Agente STTK — medição real

**Gerado:** 2026-09-07T12:44:35  
**Fonte:** transcripts de subagente do Claude Code (`<sessionId>/subagents/`)  
**Invocações medidas:** 253  
**Custo-equivalente total (subagentes):** 188.1M  
**Custo aproximado em USD (tabela pública, mix de modelos):** US$ 532.76

> `custo-eq` = input×1 + cache_write×1,25 + cache_read×0,10 + output×5. Unidade normalizada, comparável entre agentes. O USD usa preços de tabela por modelo — é estimativa, não a fatura real.

## 1. Quanto cada agente gasta HOJE

| Agente | Invoc. | Turnos | Saída | Cache read | custo-eq | % | USD aprox. | Período |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| **kelsen** | 80 | 2158 | 993.4k | 201.9M | 65.9M | 35.0% | US$ 197.36 | 2026-07-23 -> 2026-09-04 |
| **hely** | 30 | 2256 | 642.8k | 267.3M | 46.5M | 24.7% | US$ 140.63 | 2026-07-23 -> 2026-09-04 |
| **lucio** | 67 | 1217 | 459.9k | 77.2M | 30.8M | 16.4% | US$ 68.19 | 2026-07-27 -> 2026-09-02 |
| **cardozo** | 17 | 598 | 321.9k | 41.6M | 19.0M | 10.1% | US$ 43.88 | 2026-08-15 -> 2026-09-07 |
| **mindlin** | 5 | 102 | 201.2k | 5.3M | 4.1M | 2.2% | US$ 12.44 | 2026-08-31 -> 2026-09-01 |
| **general-purpose** | 5 | 138 | 80.0k | 13.9M | 3.9M | 2.1% | US$ 10.72 | 2026-08-08 -> 2026-09-03 |
| **oscar** | 8 | 142 | 98.1k | 7.8M | 3.9M | 2.1% | US$ 11.61 | 2026-08-07 -> 2026-09-02 |
| **burle** | 13 | 211 | 101.0k | 4.7M | 2.7M | 1.4% | US$ 5.19 | 2026-08-07 -> 2026-09-01 |
| **portinari** | 5 | 94 | 40.1k | 5.4M | 2.4M | 1.3% | US$ 7.11 | 2026-08-07 -> 2026-08-12 |
| **tenreiro** | 4 | 103 | 116.0k | 4.0M | 2.1M | 1.1% | US$ 6.29 | 2026-08-31 -> 2026-09-01 |
| **glaziou** | 2 | 47 | 75.5k | 2.0M | 1.1M | 0.6% | US$ 3.23 | 2026-08-31 -> 2026-08-31 |
| **baumgart** | 2 | 45 | 64.7k | 1.8M | 1.0M | 0.5% | US$ 3.02 | 2026-08-31 -> 2026-08-31 |
| **guia-claude** | 3 | 71 | 20.3k | 2.2M | 979.3k | 0.5% | US$ 14.69 | 2026-08-03 -> 2026-08-03 |
| **landell** | 2 | 40 | 37.0k | 1.6M | 899.4k | 0.5% | US$ 2.70 | 2026-08-31 -> 2026-08-31 |
| **Explore** | 3 | 59 | 15.2k | 1.8M | 828.7k | 0.4% | US$ 0.83 | 2026-07-27 -> 2026-08-21 |
| **claude** | 2 | 28 | 6.8k | 2.0M | 810.4k | 0.4% | US$ 1.05 | 2026-08-11 -> 2026-09-03 |
| **saturnino** | 2 | 35 | 44.6k | 1.3M | 677.7k | 0.4% | US$ 2.03 | 2026-08-31 -> 2026-08-31 |
| **artigas** | 3 | 36 | 11.3k | 1.2M | 595.1k | 0.3% | US$ 1.79 | 2026-09-01 -> 2026-09-01 |
| **TOTAL** | 253 | | | | 188.1M | 100% | US$ 532.76 | |

O gasto é dominado por **cache read** (contexto relido a cada turno) e por **output**. Poucas horas de sessão longa de um agente pesam mais que dezenas de invocações curtas.

## 2. "Com vs sem otimização" — contexto inicial por invocação

Corte: **2026-07-30** (slices de CLAUDE.md + referências de slice em `.claude/agents/*.md`).

| Agente | ctx inicial ANTES | ctx inicial DEPOIS | variação |
|---|--:|--:|--:|
| kelsen | 22.6k | 30.1k | +33.0% |
| hely | 30.3k | 30.6k | +1.0% |
| lucio | 20.3k | 29.6k | +45.9% |
| cardozo | - | 30.1k | — |
| mindlin | - | 27.8k | — |
| general-purpose | - | 46.9k | — |
| oscar | - | 27.1k | — |
| burle | - | 17.2k | — |
| portinari | - | 20.5k | — |
| tenreiro | - | 27.0k | — |
| glaziou | - | 26.0k | — |
| baumgart | - | 26.0k | — |
| guia-claude | - | 25.8k | — |
| landell | - | 26.0k | — |
| Explore | 24.2k | 27.0k | +11.4% |
| claude | - | 50.8k | — |
| saturnino | - | 26.0k | — |
| artigas | - | 25.1k | — |

**Leitura honesta:** não existe medição de um mundo "sem otimização" — a otimização mexeu em arquivos compartilhados, não num parâmetro que dá para ligar/desligar. O que a tabela mostra é o antes/depois do corte, e em todos os agentes com histórico dos dois lados o contexto **subiu**, não caiu. A causa provável é o próprio projeto crescendo (estado dos agentes maior, mais pendências, mais agentes referenciados), não os slices. Ou seja: a economia atribuível ao plano de otimização, por agente, é **nula ou negativa** na medição real.

O único ganho de token de fato presente nos dados é o **prompt caching** (ver `RELATORIO_TOKENS.md`), que já vinha ativo e não faz parte do plano.

## 3. Contexto: custo das sessões principais (não-subagente)

Cada rodada de rotina roda numa sessão principal (Wallenberg) que **também** gasta token, à parte dos subagentes que ela invoca.

| Origem | Sessões | Turnos | custo-eq | USD aprox. | Período |
|---|--:|--:|--:|--:|---|
| (interativo / manual) | 16 | 2674 | 123.3M | US$ 978.82 | 2026-07-16 -> 2026-09-04 |
| wallenberg-reuniao-semanal | 11 | 3079 | 182.5M | US$ 542.07 | 2026-07-20 -> 2026-09-07 |
| wallenberg-drenagem-continua | 48 | 5299 | 187.5M | US$ 487.65 | 2026-07-27 -> 2026-08-28 |
| wallenberg-rotina-diaria-skills-v2-7 | 7 | 782 | 24.8M | US$ 217.45 | 2026-08-29 -> 2026-09-07 |
| wallenberg-rotina-diaria-skills | 35 | 3417 | 98.2M | US$ 213.48 | 2026-07-22 -> 2026-08-28 |
| wallenberg-drenagem-continua-local | 6 | 597 | 22.2M | US$ 51.70 | 2026-08-31 -> 2026-09-07 |
| wallenberg-cronjob-pdf-2000 | 4 | 60 | 1.9M | US$ 3.83 | 2026-08-31 -> 2026-09-04 |
| teste-kelsen-abre-hely | 1 | 3 | 108.5k | US$ 0.33 | 2026-07-23 -> 2026-07-23 |
| **subtotal sessões principais** | | | | US$ 2,495.33 | |

**Total geral aproximado (sessões principais + subagentes):** US$ 3,028.09 desde ~16/07/2026.

> USD por preço de tabela pública, mix de modelos — estimativa de ordem de grandeza, não a fatura. Serve para dizer onde o token vai: a cadeia Legal (Kelsen + Hely) é o maior bloco de subagente; as rotinas agendadas de Wallenberg são o maior bloco de sessão principal.
