# Custo por Agente STTK — medição real

**Gerado:** 2026-09-22T12:22:23  
**Fonte:** transcripts de subagente do Claude Code (`<sessionId>/subagents/`)  
**Invocações medidas:** 342  
**Custo-equivalente total (subagentes):** 255.0M  
**Custo aproximado em USD (tabela pública, mix de modelos):** US$ 727.89

> `custo-eq` = input×1 + cache_write×1,25 + cache_read×0,10 + output×5. Unidade normalizada, comparável entre agentes. O USD usa preços de tabela por modelo — é estimativa, não a fatura real.

## 1. Quanto cada agente gasta HOJE

| Agente | Invoc. | Turnos | Saída | Cache read | custo-eq | % | USD aprox. | Período |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| **kelsen** | 95 | 2401 | 1.1M | 223.9M | 75.2M | 29.5% | US$ 220.46 | 2026-07-23 -> 2026-09-21 |
| **hely** | 36 | 2554 | 786.2k | 300.1M | 52.6M | 20.6% | US$ 158.89 | 2026-07-23 -> 2026-09-19 |
| **cardozo** | 40 | 1249 | 778.7k | 108.5M | 46.1M | 18.1% | US$ 127.28 | 2026-08-15 -> 2026-09-22 |
| **lucio** | 73 | 1306 | 547.4k | 83.7M | 34.9M | 13.7% | US$ 78.49 | 2026-07-27 -> 2026-09-22 |
| **villaca** | 8 | 264 | 172.5k | 28.9M | 8.3M | 3.3% | US$ 24.87 | 2026-09-18 -> 2026-09-21 |
| **mindlin** | 8 | 135 | 235.3k | 6.6M | 4.9M | 1.9% | US$ 14.42 | 2026-08-31 -> 2026-09-16 |
| **oscar** | 9 | 165 | 112.6k | 9.3M | 4.6M | 1.8% | US$ 13.69 | 2026-08-07 -> 2026-09-21 |
| **general-purpose** | 6 | 139 | 80.0k | 13.9M | 4.0M | 1.6% | US$ 11.02 | 2026-08-08 -> 2026-09-09 |
| **Explore** | 8 | 248 | 64.7k | 11.8M | 3.3M | 1.3% | US$ 8.34 | 2026-07-27 -> 2026-09-16 |
| **baumgart** | 6 | 120 | 157.4k | 5.3M | 2.8M | 1.1% | US$ 8.54 | 2026-08-31 -> 2026-09-12 |
| **tenreiro** | 6 | 131 | 149.8k | 5.2M | 2.8M | 1.1% | US$ 8.25 | 2026-08-31 -> 2026-09-12 |
| **burle** | 13 | 211 | 101.0k | 4.7M | 2.7M | 1.0% | US$ 5.19 | 2026-08-07 -> 2026-09-01 |
| **portinari** | 5 | 94 | 40.1k | 5.4M | 2.4M | 0.9% | US$ 7.11 | 2026-08-07 -> 2026-08-12 |
| **glaziou** | 5 | 100 | 136.9k | 4.3M | 2.4M | 0.9% | US$ 7.06 | 2026-08-31 -> 2026-09-12 |
| **landell** | 6 | 93 | 114.2k | 3.7M | 2.3M | 0.9% | US$ 6.63 | 2026-08-31 -> 2026-09-16 |
| **saturnino** | 5 | 80 | 104.3k | 3.1M | 1.8M | 0.7% | US$ 5.44 | 2026-08-31 -> 2026-09-12 |
| **mascaro** | 3 | 59 | 31.3k | 2.3M | 1.0M | 0.4% | US$ 3.12 | 2026-09-18 -> 2026-09-21 |
| **guia-claude** | 3 | 71 | 20.3k | 2.2M | 979.3k | 0.4% | US$ 14.69 | 2026-08-03 -> 2026-08-03 |
| **claude** | 2 | 28 | 6.8k | 2.0M | 810.4k | 0.3% | US$ 1.05 | 2026-08-11 -> 2026-09-03 |
| **artigas** | 3 | 36 | 11.3k | 1.2M | 595.1k | 0.2% | US$ 1.79 | 2026-09-01 -> 2026-09-01 |
| **fiker** | 2 | 36 | 15.7k | 1.2M | 521.2k | 0.2% | US$ 1.56 | 2026-09-18 -> 2026-09-21 |
| **TOTAL** | 342 | | | | 255.0M | 100% | US$ 727.89 | |

O gasto é dominado por **cache read** (contexto relido a cada turno) e por **output**. Poucas horas de sessão longa de um agente pesam mais que dezenas de invocações curtas.

## 2. "Com vs sem otimização" — contexto inicial por invocação

Corte: **2026-07-30** (slices de CLAUDE.md + referências de slice em `.claude/agents/*.md`).

| Agente | ctx inicial ANTES | ctx inicial DEPOIS | variação |
|---|--:|--:|--:|
| kelsen | 22.6k | 30.7k | +35.5% |
| hely | 30.3k | 31.0k | +2.4% |
| cardozo | - | 50.6k | — |
| lucio | 20.3k | 29.7k | +46.2% |
| villaca | - | 78.6k | — |
| mindlin | - | 28.6k | — |
| oscar | - | 29.5k | — |
| general-purpose | - | 47.3k | — |
| Explore | 24.2k | 34.5k | +42.3% |
| baumgart | - | 35.1k | — |
| tenreiro | - | 28.0k | — |
| burle | - | 17.2k | — |
| portinari | - | 20.5k | — |
| glaziou | - | 35.5k | — |
| landell | - | 30.9k | — |
| saturnino | - | 35.5k | — |
| mascaro | - | 28.4k | — |
| guia-claude | - | 25.8k | — |
| claude | - | 50.8k | — |
| artigas | - | 25.1k | — |
| fiker | - | 28.7k | — |

**Leitura honesta:** não existe medição de um mundo "sem otimização" — a otimização mexeu em arquivos compartilhados, não num parâmetro que dá para ligar/desligar. O que a tabela mostra é o antes/depois do corte, e em todos os agentes com histórico dos dois lados o contexto **subiu**, não caiu. A causa provável é o próprio projeto crescendo (estado dos agentes maior, mais pendências, mais agentes referenciados), não os slices. Ou seja: a economia atribuível ao plano de otimização, por agente, é **nula ou negativa** na medição real.

O único ganho de token de fato presente nos dados é o **prompt caching** (ver `RELATORIO_TOKENS.md`), que já vinha ativo e não faz parte do plano.

## 3. Contexto: custo das sessões principais (não-subagente)

Cada rodada de rotina roda numa sessão principal (Wallenberg) que **também** gasta token, à parte dos subagentes que ela invoca.

| Origem | Sessões | Turnos | custo-eq | USD aprox. | Período |
|---|--:|--:|--:|--:|---|
| (interativo / manual) | 26 | 6951 | 355.4M | US$ 1,646.70 | 2026-07-16 -> 2026-09-22 |
| wallenberg-reuniao-semanal | 19 | 4507 | 236.6M | US$ 699.66 | 2026-07-20 -> 2026-09-22 |
| wallenberg-rotina-diaria-skills-v2-7 | 18 | 2135 | 63.3M | US$ 499.11 | 2026-08-29 -> 2026-09-22 |
| wallenberg-drenagem-continua | 48 | 5299 | 187.5M | US$ 487.65 | 2026-07-27 -> 2026-08-28 |
| wallenberg-rotina-diaria-skills | 35 | 3417 | 98.2M | US$ 213.48 | 2026-07-22 -> 2026-08-28 |
| wallenberg-drenagem-continua-local | 19 | 1484 | 55.2M | US$ 110.67 | 2026-08-31 -> 2026-09-22 |
| wallenberg-cronjob-pdf-2000 | 15 | 201 | 6.2M | US$ 15.70 | 2026-08-31 -> 2026-09-21 |
| teste-kelsen-abre-hely | 1 | 3 | 108.5k | US$ 0.33 | 2026-07-23 -> 2026-07-23 |
| **subtotal sessões principais** | | | | US$ 3,673.30 | |

**Total geral aproximado (sessões principais + subagentes):** US$ 4,401.19 desde ~16/07/2026.

> USD por preço de tabela pública, mix de modelos — estimativa de ordem de grandeza, não a fatura. Serve para dizer onde o token vai: a cadeia Legal (Kelsen + Hely) é o maior bloco de subagente; as rotinas agendadas de Wallenberg são o maior bloco de sessão principal.
