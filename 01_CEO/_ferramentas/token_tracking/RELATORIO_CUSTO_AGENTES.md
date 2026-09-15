# Custo por Agente STTK — medição real

**Gerado:** 2026-09-14T20:27:11  
**Fonte:** transcripts de subagente do Claude Code (`<sessionId>/subagents/`)  
**Invocações medidas:** 299  
**Custo-equivalente total (subagentes):** 228.9M  
**Custo aproximado em USD (tabela pública, mix de modelos):** US$ 657.46

> `custo-eq` = input×1 + cache_write×1,25 + cache_read×0,10 + output×5. Unidade normalizada, comparável entre agentes. O USD usa preços de tabela por modelo — é estimativa, não a fatura real.

## 1. Quanto cada agente gasta HOJE

| Agente | Invoc. | Turnos | Saída | Cache read | custo-eq | % | USD aprox. | Período |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| **kelsen** | 86 | 2278 | 1.1M | 214.4M | 70.9M | 31.0% | US$ 209.44 | 2026-07-23 -> 2026-09-12 |
| **hely** | 32 | 2445 | 734.1k | 291.0M | 50.4M | 22.0% | US$ 152.21 | 2026-07-23 -> 2026-09-12 |
| **cardozo** | 35 | 1173 | 741.6k | 103.3M | 43.1M | 18.8% | US$ 121.30 | 2026-08-15 -> 2026-09-14 |
| **lucio** | 67 | 1217 | 459.9k | 77.2M | 30.8M | 13.5% | US$ 68.19 | 2026-07-27 -> 2026-09-02 |
| **mindlin** | 7 | 131 | 233.1k | 6.5M | 4.8M | 2.1% | US$ 14.32 | 2026-08-31 -> 2026-09-12 |
| **general-purpose** | 6 | 139 | 80.0k | 13.9M | 4.0M | 1.7% | US$ 11.02 | 2026-08-08 -> 2026-09-09 |
| **oscar** | 8 | 142 | 98.1k | 7.8M | 3.9M | 1.7% | US$ 11.61 | 2026-08-07 -> 2026-09-02 |
| **baumgart** | 6 | 120 | 157.4k | 5.3M | 2.8M | 1.2% | US$ 8.54 | 2026-08-31 -> 2026-09-12 |
| **tenreiro** | 6 | 131 | 149.8k | 5.2M | 2.8M | 1.2% | US$ 8.25 | 2026-08-31 -> 2026-09-12 |
| **burle** | 13 | 211 | 101.0k | 4.7M | 2.7M | 1.2% | US$ 5.19 | 2026-08-07 -> 2026-09-01 |
| **portinari** | 5 | 94 | 40.1k | 5.4M | 2.4M | 1.0% | US$ 7.11 | 2026-08-07 -> 2026-08-12 |
| **glaziou** | 5 | 100 | 136.9k | 4.3M | 2.4M | 1.0% | US$ 7.06 | 2026-08-31 -> 2026-09-12 |
| **landell** | 5 | 85 | 110.6k | 3.5M | 2.2M | 0.9% | US$ 6.47 | 2026-08-31 -> 2026-09-12 |
| **Explore** | 5 | 97 | 24.7k | 4.4M | 1.8M | 0.8% | US$ 3.78 | 2026-07-27 -> 2026-09-14 |
| **saturnino** | 5 | 80 | 104.3k | 3.1M | 1.8M | 0.8% | US$ 5.44 | 2026-08-31 -> 2026-09-12 |
| **guia-claude** | 3 | 71 | 20.3k | 2.2M | 979.3k | 0.4% | US$ 14.69 | 2026-08-03 -> 2026-08-03 |
| **claude** | 2 | 28 | 6.8k | 2.0M | 810.4k | 0.4% | US$ 1.05 | 2026-08-11 -> 2026-09-03 |
| **artigas** | 3 | 36 | 11.3k | 1.2M | 595.1k | 0.3% | US$ 1.79 | 2026-09-01 -> 2026-09-01 |
| **TOTAL** | 299 | | | | 228.9M | 100% | US$ 657.46 | |

O gasto é dominado por **cache read** (contexto relido a cada turno) e por **output**. Poucas horas de sessão longa de um agente pesam mais que dezenas de invocações curtas.

## 2. "Com vs sem otimização" — contexto inicial por invocação

Corte: **2026-07-30** (slices de CLAUDE.md + referências de slice em `.claude/agents/*.md`).

| Agente | ctx inicial ANTES | ctx inicial DEPOIS | variação |
|---|--:|--:|--:|
| kelsen | 22.6k | 30.2k | +33.3% |
| hely | 30.3k | 30.7k | +1.3% |
| cardozo | - | 49.8k | — |
| lucio | 20.3k | 29.6k | +45.9% |
| mindlin | - | 29.3k | — |
| general-purpose | - | 47.3k | — |
| oscar | - | 27.1k | — |
| baumgart | - | 35.1k | — |
| tenreiro | - | 28.0k | — |
| burle | - | 17.2k | — |
| portinari | - | 20.5k | — |
| glaziou | - | 35.5k | — |
| landell | - | 35.8k | — |
| Explore | 24.2k | 34.6k | +42.6% |
| saturnino | - | 35.5k | — |
| guia-claude | - | 25.8k | — |
| claude | - | 50.8k | — |
| artigas | - | 25.1k | — |

**Leitura honesta:** não existe medição de um mundo "sem otimização" — a otimização mexeu em arquivos compartilhados, não num parâmetro que dá para ligar/desligar. O que a tabela mostra é o antes/depois do corte, e em todos os agentes com histórico dos dois lados o contexto **subiu**, não caiu. A causa provável é o próprio projeto crescendo (estado dos agentes maior, mais pendências, mais agentes referenciados), não os slices. Ou seja: a economia atribuível ao plano de otimização, por agente, é **nula ou negativa** na medição real.

O único ganho de token de fato presente nos dados é o **prompt caching** (ver `RELATORIO_TOKENS.md`), que já vinha ativo e não faz parte do plano.

## 3. Contexto: custo das sessões principais (não-subagente)

Cada rodada de rotina roda numa sessão principal (Wallenberg) que **também** gasta token, à parte dos subagentes que ela invoca.

| Origem | Sessões | Turnos | custo-eq | USD aprox. | Período |
|---|--:|--:|--:|--:|---|
| (interativo / manual) | 20 | 3740 | 163.5M | US$ 1,081.42 | 2026-07-16 -> 2026-09-12 |
| wallenberg-reuniao-semanal | 17 | 4139 | 222.5M | US$ 661.16 | 2026-07-20 -> 2026-09-14 |
| wallenberg-drenagem-continua | 48 | 5299 | 187.5M | US$ 487.65 | 2026-07-27 -> 2026-08-28 |
| wallenberg-rotina-diaria-skills-v2-7 | 12 | 1361 | 42.2M | US$ 391.93 | 2026-08-29 -> 2026-09-14 |
| wallenberg-rotina-diaria-skills | 35 | 3417 | 98.2M | US$ 213.48 | 2026-07-22 -> 2026-08-28 |
| wallenberg-drenagem-continua-local | 12 | 1135 | 42.4M | US$ 88.38 | 2026-08-31 -> 2026-09-14 |
| wallenberg-cronjob-pdf-2000 | 10 | 126 | 4.2M | US$ 9.70 | 2026-08-31 -> 2026-09-14 |
| teste-kelsen-abre-hely | 1 | 3 | 108.5k | US$ 0.33 | 2026-07-23 -> 2026-07-23 |
| **subtotal sessões principais** | | | | US$ 2,934.05 | |

**Total geral aproximado (sessões principais + subagentes):** US$ 3,591.51 desde ~16/07/2026.

> USD por preço de tabela pública, mix de modelos — estimativa de ordem de grandeza, não a fatura. Serve para dizer onde o token vai: a cadeia Legal (Kelsen + Hely) é o maior bloco de subagente; as rotinas agendadas de Wallenberg são o maior bloco de sessão principal.
