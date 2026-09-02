# Relatorio de Tokens — MEDICAO REAL

**Gerado em:** 2026-09-02T20:56:16  
**Fonte:** transcripts de sessao do Claude Code (`C:\Users\santo\.claude\projects\D--000-ESTRUTURA-DEPARTAMENTO-DE-PROJETO`)  
**Sessoes lidas:** 118 (**117** conversas de trabalho, >= 3 turnos)  
**Periodo:** 2026-07-16 -> 2026-09-02  

> Todo numero abaixo vem do campo `message.usage` de cada resposta do assistente. Nao ha projecao nem estimativa multiplicada.

## 1. Prompt caching — ja esta ligado?

- Sessoes com leitura de cache (`cache_read_input_tokens` > 0): **118 / 118**
- Cache hit ratio medio (conversas de trabalho): **91.3%** do contexto de entrada vem de cache

**Conclusao:** o prompt caching nativo da Anthropic **ja opera** nas sessoes deste projeto. O Item 7 ("aguardando API Claude v1.9+") descreve um bloqueio que nao existe — o ganho ja esta sendo colhido.

## 2. Contexto inicial por conversa — baseline vs. atual

- Base (2026-S30, 2026-S31): mediana **67.1k** tokens de contexto inicial
- Atual (2026-S35, 2026-S36): mediana **68.8k** tokens
- Resultado medido: **AUMENTO de 2.6%** (1.7k tokens)

> O plano projetava 45-70% de **reducao** de contexto por conversa. A medicao real mostra o contrario: o contexto inicial nao caiu apos os slices de CLAUDE.md (30/07) nem a consolidacao de MEMORY.md (29/07).

## 3. Evolucao semanal (mediana do contexto inicial)

| Semana | Inicio | Sessoes | Mediana | Media | Min | Max | Cache hit |
|---|---|--:|--:|--:|--:|--:|--:|
| 2026-S29 | 2026-07-13 | 1 | 49.5k | 49.5k | 49.5k | 49.5k | 91% |
| 2026-S30 | 2026-07-20 | 5 | 68.6k | 68.7k | 65.2k | 72.5k | 89% |
| 2026-S31 | 2026-07-27 | 20 | 65.5k | 64.7k | 45.3k | 72.7k | 94% |
| 2026-S32 | 2026-08-03 | 20 | 68.0k | 68.2k | 65.7k | 72.7k | 91% |
| 2026-S33 | 2026-08-10 | 22 | 68.6k | 65.2k | 53.8k | 74.3k | 91% |
| 2026-S34 | 2026-08-17 | 17 | 61.0k | 62.9k | 58.9k | 82.2k | 90% |
| 2026-S35 | 2026-08-24 | 18 | 64.0k | 65.7k | 60.1k | 85.8k | 90% |
| 2026-S36 | 2026-08-31 | 14 | 73.6k | 75.3k | 66.2k | 87.3k | 92% |

**Marcos do plano de otimizacao (para cruzar com a curva):**
- 2026-07-29 — Item 1: consolidacao MEMORY.md (18 -> 3 arquivos)
- 2026-07-30 — Item 2: CLAUDE.md fatiado em slices por papel
- 2026-08-05 — Item 3: arquivos de estado em JSON
- 2026-08-13 — Item 5: cache incremental do Google Drive

## 4. Sessoes (todas, mais recente primeiro)

| Data | Sessao | Br. | Turnos | Ctx inicial | Ctx pico | Saida | Cache read | Custo-eq |
|---|---|---|--:|--:|--:|--:|--:|--:|
| 2026-09-02 | `2ba19103` | organismo-30-0 | 14 | 72.9k | 80.5k | 6.1k | 906.6k | 326.1k |
| 2026-09-02 | `d2254e84` | organismo-30-0 | 97 | 87.3k | 222.0k | 105.4k | 15.17M | 2.94M |
| 2026-09-02 | `b9957111` | organismo-30-0 | 18 | 87.3k | 121.3k | 15.7k | 1.58M | 595.1k |
| 2026-09-02 | `ff76dfd0` | organismo-30-0 | 46 | 74.3k | 153.7k | 35.2k | 5.58M | 1.18M |
| 2026-09-02 | `62d5dd97` | organismo-30-0 | 104 | 71.4k | 166.7k | 66.0k | 12.90M | 2.24M |
| 2026-09-01 | `85796aa8` | organismo-30-0 | 11 | 69.7k | 76.5k | 6.0k | 675.8k | 253.6k |
| 2026-09-01 | `487f8d9b` | organismo-30-0 | 197 | 83.0k | 347.4k | 189.6k | 41.73M | 5.86M |
| 2026-09-01 | `bb9c79eb` | organismo-30-0 | 100 | 70.5k | 192.1k | 90.3k | 14.09M | 2.78M |
| 2026-09-01 | `242af919` | organismo-30-0 | 429 | 78.7k | 619.9k | 506.8k | 156.87M | 20.42M |
| 2026-09-01 | `8894329b` | organismo-30-0 | 118 | 67.7k | 156.5k | 105.5k | 12.22M | 4.07M |
| 2026-08-31 | `d7bfa813` | organismo-30-0 | 14 | 77.0k | 90.4k | 12.7k | 961.0k | 444.1k |
| 2026-08-31 | `9127f07d` | organismo-30-0 | 226 | 66.2k | 403.0k | 240.8k | 45.31M | 10.66M |
| 2026-08-31 | `6126b1de` | organismo-30-0 | 219 | 81.8k | 441.0k | 245.9k | 61.06M | 9.75M |
| 2026-08-31 | `e3f145d9` | organismo-30-0 | 119 | 66.8k | 158.2k | 84.9k | 14.51M | 2.51M |
| 2026-08-29 | `ae5e3aa9` | organismo-30-0 | 2 | 66.8k | 66.8k | 988 | 61.3k | 101.5k |
| 2026-08-29 | `489ca2f9` | organismo-30-0 | 52 | 78.7k | 172.4k | 64.4k | 5.32M | 1.84M |
| 2026-08-28 | `891fe149` | organismo-30-0 | 83 | 65.6k | 193.1k | 105.0k | 10.95M | 2.71M |
| 2026-08-28 | `588921bf` | organismo-30-0 | 107 | 65.6k | 270.2k | 209.4k | 16.21M | 4.58M |
| 2026-08-28 | `e03bb2f5` | organismo-30-0 | 8 | 66.1k | 68.6k | 3.1k | 464.3k | 152.5k |
| 2026-08-28 | `bcaea611` | organismo-30-0 | 74 | 66.1k | 136.8k | 111.4k | 6.98M | 1.64M |
| 2026-08-28 | `2082f3de` | organismo-30-0 | 10 | 66.1k | 68.6k | 3.9k | 464.3k | 317.3k |
| 2026-08-28 | `24194d13` | organismo-30-0 | 28 | 64.3k | 137.2k | 24.4k | 2.75M | 933.9k |
| 2026-08-28 | `87c0f8cd` | organismo-30-0 | 278 | 65.0k | 168.4k | 394.5k | 31.97M | 8.53M |
| 2026-08-27 | `f5d5ee81` | organismo-30-0 | 300 | 63.0k | 470.0k | 336.9k | 66.87M | 12.43M |
| 2026-08-27 | `eca94e64` | organismo-30-0 | 385 | 63.7k | 428.9k | 545.4k | 62.70M | 18.07M |
| 2026-08-26 | `5b6cc165` | organismo-30-0 | 64 | 62.9k | 153.5k | 88.5k | 6.34M | 2.34M |
| 2026-08-26 | `704aceb9` | organismo-30-0 | 64 | 63.3k | 126.1k | 47.9k | 6.26M | 1.40M |
| 2026-08-25 | `63d0ff4f` | organismo-30-0 | 66 | 61.4k | 156.6k | 47.9k | 7.71M | 1.70M |
| 2026-08-25 | `7867fc8a` | organismo-30-0 | 131 | 62.1k | 297.2k | 134.2k | 25.39M | 5.16M |
| 2026-08-25 | `6c2dd46f` | organismo-30-0 | 45 | 62.1k | 138.3k | 22.5k | 4.50M | 1.11M |
| 2026-08-24 | `89e91b5e` | organismo-30-0 | 35 | 85.8k | 171.1k | 45.3k | 4.39M | 1.09M |
| 2026-08-24 | `98aa5d27` | organismo-30-0 | 55 | 61.4k | 177.9k | 41.0k | 7.44M | 1.58M |
| 2026-08-24 | `9d868239` | organismo-30-0 | 93 | 60.1k | 152.2k | 103.2k | 9.29M | 1.91M |
| 2026-08-23 | `bce0f41c` | organismo-30-0 | 51 | 61.5k | 145.7k | 35.5k | 5.37M | 1.53M |
| 2026-08-23 | `9024eaea` | organismo-30-0 | 54 | 61.5k | 120.8k | 77.1k | 4.27M | 1.52M |
| 2026-08-22 | `ea4518f0` | organismo-30-0 | 39 | 61.3k | 149.3k | 43.4k | 4.22M | 1.26M |
| 2026-08-22 | `c5ac5a66` | organismo-30-0 | 26 | 61.3k | 103.3k | 18.1k | 1.88M | 563.5k |
| 2026-08-21 | `0d47f04a` | organismo-30-0 | 178 | 61.1k | 197.3k | 169.0k | 22.41M | 4.87M |
| 2026-08-21 | `cfe21f49` | organismo-30-0 | 196 | 61.0k | 189.6k | 162.9k | 24.96M | 5.35M |
| 2026-08-20 | `58c841e1` | organismo-30-0 | 83 | 60.7k | 188.9k | 101.1k | 10.71M | 3.42M |
| 2026-08-20 | `4043c995` | organismo-30-0 | 105 | 59.4k | 161.8k | 120.6k | 10.92M | 2.71M |
| 2026-08-19 | `6633a11e` | organismo-30-0 | 42 | 61.2k | 146.3k | 27.5k | 4.65M | 1.12M |
| 2026-08-19 | `44d07cc5` | organismo-30-0 | 71 | 59.7k | 127.7k | 82.0k | 6.01M | 1.38M |
| 2026-08-18 | `7609f46c` | organismo-30-0 | 67 | 60.1k | 148.9k | 41.4k | 7.75M | 1.85M |
| 2026-08-18 | `f525e4da` | organismo-30-0 | 50 | 60.1k | 112.2k | 32.2k | 3.84M | 1.14M |
| 2026-08-17 | `fdac7303` | organismo-30-0 | 36 | 82.2k | 189.1k | 52.7k | 4.82M | 1.17M |
| 2026-08-17 | `0c2280ee` | organismo-30-0 | 239 | 82.2k | 411.5k | 278.2k | 64.74M | 13.66M |
| 2026-08-17 | `5ff3df19` | organismo-30-0 | 24 | 58.9k | 158.6k | 25.6k | 2.15M | 1.25M |
| 2026-08-17 | `97eae0f6` | organismo-30-0 | 162 | 58.9k | 197.7k | 90.2k | 16.30M | 5.23M |
| 2026-08-17 | `474c8dce` | organismo-30-0 | 84 | 58.9k | 139.0k | 79.6k | 7.47M | 2.31M |
| 2026-08-14 | `fef15fe1` | organismo-30-0 | 112 | 68.1k | 164.7k | 93.2k | 13.36M | 2.71M |
| 2026-08-14 | `6dac6954` | organismo-30-0 | 164 | 58.6k | 194.9k | 217.2k | 21.78M | 5.02M |
| 2026-08-14 | `3bbbca16` | organismo-30-0 | 25 | 58.6k | 142.8k | 22.9k | 2.31M | 878.0k |
| 2026-08-14 | `97e600b1` | organismo-30-0 | 38 | 56.3k | 156.6k | 47.3k | 4.40M | 1.15M |
| 2026-08-14 | `69267c46` | organismo-30-0 | 242 | 56.2k | 196.8k | 137.5k | 27.40M | 5.59M |
| 2026-08-13 | `7738b1ec` | organismo-30-0 | 25 | 55.2k | 134.5k | 21.2k | 2.27M | 896.4k |
| 2026-08-13 | `de1483c5` | organismo-30-0 | 20 | 55.1k | 118.6k | 24.1k | 1.58M | 712.9k |
| 2026-08-13 | `1023ba71` | organismo-30-0 | 52 | 53.8k | 113.3k | 44.5k | 4.38M | 1.03M |
| 2026-08-12 | `f151a84a` | organismo-30-0 | 81 | 55.1k | 184.3k | 104.3k | 10.10M | 2.54M |
| 2026-08-12 | `0a48f454` | organismo-30-0 | 74 | 74.3k | 212.5k | 61.3k | 9.39M | 3.16M |
| 2026-08-12 | `7bc807e9` | organismo-30-0 | 44 | 72.5k | 143.9k | 37.9k | 5.09M | 1.09M |
| 2026-08-11 | `06d955e0` | organismo-30-0 | 99 | 72.5k | 228.8k | 80.4k | 16.29M | 2.71M |
| 2026-08-11 | `e3712c53` | organismo-30-0 | 178 | 72.1k | 306.0k | 146.2k | 34.19M | 5.83M |
| 2026-08-11 | `fd0aebb9` | organismo-30-0 | 72 | 69.8k | 164.8k | 64.3k | 8.92M | 1.89M |
| 2026-08-10 | `2f01fe3c` | organismo-30-0 | 82 | 71.1k | 277.9k | 84.3k | 15.16M | 2.92M |
| 2026-08-10 | `f8cd6871` | organismo-30-0 | 56 | 68.6k | 194.3k | 57.0k | 7.03M | 2.22M |
| 2026-08-10 | `99133042` | organismo-30-0 | 93 | 68.6k | 222.5k | 78.3k | 14.44M | 3.52M |
| 2026-08-10 | `8ff752cf` | organismo-30-0 | 519 | 68.6k | 494.6k | 260.6k | 164.29M | 21.92M |
| 2026-08-10 | `e907a5bd` | organismo-30-0 | 284 | 71.1k | 399.5k | 221.2k | 70.35M | 11.57M |
| 2026-08-10 | `442b77ef` | organismo-30-0 | 50 | 69.2k | 126.5k | 40.0k | 4.79M | 1.06M |
| 2026-08-10 | `4e9ed1a5` | organismo-30-0 | 14 | 69.1k | 86.9k | 7.9k | 960.2k | 329.9k |
| 2026-08-10 | `fa51a6c2` | organismo-30-0 | 12 | 71.0k | 142.5k | 3.3k | 990.6k | 533.6k |
| 2026-08-08 | `d8269321` | organismo-30-0 | 238 | 71.6k | 321.4k | 151.8k | 51.12M | 7.63M |
| 2026-08-08 | `769819ae` | organismo-30-0 | 62 | 70.8k | 152.3k | 38.2k | 8.03M | 1.41M |
| 2026-08-08 | `552cf9ea` | organismo-30-0 | 59 | 72.7k | 182.7k | 93.3k | 8.09M | 2.02M |
| 2026-08-07 | `2d7d936b` | organismo-30-0 | 432 | 68.7k | 468.9k | 277.8k | 122.75M | 17.37M |
| 2026-08-07 | `4acb20a9` | organismo-30-0 | 177 | 69.5k | 317.5k | 149.1k | 37.19M | 5.32M |
| 2026-08-07 | `86d40c63` | organismo-30-0 | 50 | 69.1k | 184.6k | 39.9k | 7.28M | 1.60M |
| 2026-08-06 | `e38342f7` | organismo-30-0 | 19 | 68.4k | 125.6k | 19.8k | 1.57M | 691.7k |
| 2026-08-06 | `59e47f2f` | organismo-30-0 | 26 | 68.4k | 126.2k | 14.8k | 2.51M | 736.3k |
| 2026-08-06 | `05ffbaf3` | organismo-30-0 | 61 | 68.0k | 162.1k | 57.7k | 6.28M | 2.21M |
| 2026-08-05 | `4d38c07e` | organismo-30-0 | 69 | 68.4k | 177.2k | 47.8k | 9.07M | 2.02M |
| 2026-08-05 | `bc758de7` | organismo-30-0 | 59 | 68.0k | 177.9k | 45.2k | 8.31M | 1.66M |
| 2026-08-04 | `4a3a69c8` | organismo-30-0 | 35 | 67.6k | 123.5k | 23.0k | 3.37M | 985.9k |
| 2026-08-04 | `d5c3da4c` | organismo-30-0 | 151 | 67.3k | 187.7k | 124.7k | 20.52M | 4.62M |
| 2026-08-04 | `5616425f` | organismo-30-0 | 65 | 66.8k | 177.4k | 54.3k | 8.15M | 2.61M |
| 2026-08-03 | `b39b9108` | organismo-30-0 | 407 | 67.0k | 539.1k | 354.1k | 127.12M | 18.54M |
| 2026-08-03 | `c4a11674` | organismo-30-0 | 127 | 65.7k | 632.8k | 182.0k | 52.40M | 12.99M |
| 2026-08-03 | `97f7e640` | organismo-30-0 | 21 | 66.7k | 113.9k | 12.4k | 1.79M | 563.5k |
| 2026-08-03 | `4a123b53` | organismo-30-0 | 15 | 66.2k | 137.4k | 18.5k | 1.32M | 578.0k |
| 2026-08-03 | `48b6a2f9` | organismo-30-0 | 20 | 66.5k | 154.7k | 13.5k | 2.02M | 796.4k |
| 2026-08-03 | `06b89ff1` | organismo-30-0 | 62 | 66.1k | 143.8k | 54.5k | 6.83M | 1.52M |
| 2026-08-01 | `f903cade` | organismo-30-0 | 29 | 66.5k | 114.7k | 21.7k | 2.27M | 851.5k |
| 2026-08-01 | `b6c9d48d` | organismo-30-0 | 82 | 58.8k | 89.8k | 35.8k | 4.84M | 1.06M |
| 2026-08-01 | `6a4ec8e2` | organismo-30-0 | 156 | 66.4k | 305.1k | 167.5k | 27.77M | 5.52M |
| 2026-08-01 | `02362a2a` | organismo-30-0 | 128 | 65.9k | 215.2k | 138.4k | 18.59M | 3.79M |
| 2026-07-31 | `57550b01` | organismo-30-0 | 76 | 66.2k | 171.6k | 87.3k | 9.27M | 2.17M |
| 2026-07-31 | `2be49311` | organismo-30-0 | 188 | 65.8k | 292.2k | 141.4k | 36.79M | 6.17M |
| 2026-07-31 | `f75f0d1d` | organismo-30-0 | 115 | 65.0k | 186.1k | 99.9k | 14.05M | 3.02M |
| 2026-07-30 | `f134555e` | organismo-30-0 | 26 | 65.2k | 133.0k | 24.2k | 2.49M | 836.9k |
| 2026-07-30 | `2b02b755` | main | 88 | 66.3k | 239.8k | 134.3k | 13.69M | 3.30M |
| 2026-07-30 | `bdb02abf` | main | 320 | 65.7k | 195.6k | 227.9k | 40.86M | 8.08M |
| 2026-07-29 | `183890bc` | main | 47 | 64.8k | 148.5k | 41.3k | 4.52M | 1.23M |
| 2026-07-29 | `4a0410a2` | HEAD | 22 | 45.3k | 51.2k | 5.4k | 1.01M | 192.6k |
| 2026-07-29 | `853fc6da` | HEAD | 90 | 63.1k | 231.0k | 79.1k | 13.93M | 2.93M |
| 2026-07-29 | `14eb8e93` | HEAD | 54 | 62.7k | 130.8k | 47.6k | 5.24M | 1.05M |
| 2026-07-28 | `2ae1d943` | HEAD | 117 | 63.2k | 232.4k | 96.2k | 16.39M | 3.29M |
| 2026-07-28 | `4ed93ab6` | HEAD | 233 | 63.0k | 343.3k | 253.1k | 51.44M | 9.21M |
| 2026-07-28 | `51983fed` | HEAD | 125 | 62.5k | 244.2k | 94.2k | 21.26M | 3.23M |
| 2026-07-27 | `ab13fe2a` | HEAD | 354 | 72.6k | 372.1k | 316.5k | 84.63M | 13.28M |
| 2026-07-27 | `06fa07cd` | HEAD | 410 | 72.7k | 656.2k | 530.2k | 163.46M | 27.63M |
| 2026-07-27 | `49d14dd8` | HEAD | 90 | 72.2k | 162.9k | 54.6k | 11.68M | 2.00M |
| 2026-07-24 | `ff9504ed` | HEAD | 57 | 72.5k | 152.6k | 54.2k | 7.04M | 1.30M |
| 2026-07-23 | `41fefd31` | HEAD | 3 | 68.6k | 69.0k | 675 | 132.8k | 108.5k |
| 2026-07-23 | `7c87d9bf` | HEAD | 49 | 69.2k | 130.2k | 36.8k | 5.13M | 1.00M |
| 2026-07-22 | `a49bd4c3` | HEAD | 49 | 68.1k | 123.4k | 36.3k | 4.79M | 973.0k |
| 2026-07-20 | `50692f4a` | HEAD | 275 | 65.2k | 398.1k | 336.1k | 64.72M | 12.42M |
| 2026-07-16 | `3d61a6b3` | HEAD | 743 | 49.5k | 708.4k | 1.26M | 209.08M | 54.14M |

_Custo-eq = input*1 + cache_write*1.25 + cache_read*0.1 + output*5. Comparavel entre sessoes; nao e fatura._
