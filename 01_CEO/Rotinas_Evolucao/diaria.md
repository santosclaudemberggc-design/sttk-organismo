# Rotina Diária de Skills — evolução

Tarefa `wallenberg-rotina-diaria-skills-v2-7` · seg-sex 09:00 · referência `01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md`

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| v2.7 | 28/08/2026 | Redefinida com checklists visuais, dashboard e CronJob PDF 20:00 | Manual longo demais para rodar todo dia | Claudemberg |
| v2.9 | 08/09/2026 | Fluxo de Ativação: o Gestor dono valida e a Skill ativa no mesmo dia; selo de ressalva | Skills paravam semanas esperando a Semanal | Claudemberg |
| v3.0 | 10/09/2026 | Pesquisa por estratégia de domínio de cada Gestor; mentalidade de "brecha válida" | Pesquisa genérica de "tendência" rendia pouco | Claudemberg |
| v3.0 (sync) | 14/09/2026 | A v3.0 passou a constar também no Checklist e no prompt agendado | 2 rodadas rodaram raso: a v3.0 só existia no manual | Claudemberg |
| v3.3.1 | 17/09/2026 | `/watch:watch` obrigatório (pelo menos 1 busca de vídeo por Gestor) | Auditoria: 6 WebSearch e 0 vídeo numa rodada | Claudemberg |
| v3.3.2 | 17/09/2026 | Fronteira crítica de cliente restaurada no prompt; `New-Item -Force` preventivo | A fronteira tinha sumido do operativo | Claudemberg |
| v3.4.0 | 28-29/09/2026 | Livro-razão por Skill; checagem de coerência entre Skills; "não procede" arquiva na hora; treino fictício; acervo `D:\008`; seção "Macetes de quem faz" | Livro-razão faltava desde 10/09; havia contradições entre Skills | Claudemberg |
| **v3.5.0** | 30/09/2026 | Horário 08:00 → 09:00; **treino fictício RETIRADO**; Passo 0 lê `_passagem_do_dia.md`; fim do commit de PDF | Operações começam 08:30; o Ensaio Sombra virou o único teste; o template de 640 linhas custava cerca de 26 mil tokens por rodada | Claudemberg |

**Tentado e revertido (não repetir sem evidência nova):**
- Treino em caso fictício por Skill: entrou em 28/09 e saiu em 30/09. O motivo foi ter 3 mecanismos de teste sobrepostos; ficou só o Ensaio.
- PDF gêmeo de Skill: saiu em 30/09. Claudemberg não lê PDF.

## 2. Diário de funcionamento
| Data | Rodou? | Duração | Resultado | Observação |
|---|---|---|---|---|
| 24/09 | sim | ~6 min | 0 Skill nova, 2 correções | /watch falhou (429/403) |
| 25/09 | sim (sexta) | ~6 min | Painel + Learning + Dashboard | — |
| 28/09 | sim | ~12 min | 2 Skills ativas | 7 buscas (orçamento era 6) |
| 29/09 | sim | ~16 min | 2 Skills ativas, 4 treinos | — |
| 30/09 | interrompida | 8 s | — | Interrompida por Claudemberg para a revisão |
| 01/10 | sim | ~12 min | 2 Skills ativas-com-ressalva (SELCA Kelsen/Hely; Cobertura Lúcio/Oscar) | Passo 0 leu `_passagem_do_dia.md` corretamente (1ª vez); Cardozo sem Skill |
| 07/10 | sim | ~5h38min (09:07–14:45) | 0 Skill nova; 6 buscas (2/Gestor); contenção em argila mole já coberta pela Skill de fundações v1.3 | Passo 0 leu a passagem de **05/10** (a de 06/10 não existe). **Não tratou a lacuna `lacuna-kelsen-dimensao-minima-vaga-06-10-2026`** (prioridade zero), que a Drenagem acabou executando. LC 198 com PDF corrompido; /watch sem vídeo. Diário sem linhas de 02 a 06/10 |
| 09/10 | sim | ~13 min (09:07–09:20) | 0 Skill nova. Painel e métricas reescritos (10 Auto · 4 Assisted · 1 Shadow · 4 Formação); evento `status` gravado | Passo 0 leu a passagem das 08:23 de 09/10 (sem rastro de 09/10 na época). Passo 7 (Learning) não rodou |

## 3. Candidatas a melhoria
- (aberta) **Uso real de Skill = 0%.** Em setembro foram cerca de 28 Skills e nenhuma usada em caso real. O Ensaio 003 é a resposta; acompanhar se as Skills aparecem nos pareceres do Bardi.
  - (09/10) Primeiro dado de uso: na etapa 4 do Ensaio, Oscar declarou 3 de 10 Skills do enunciado, e o Bardi registrou que a Skill legal-oodc não foi lida (`parecer_bardi.md` da etapa 4, §3 e §6). Uso real ainda baixo.
- (aberta) **Bug do /watch:** `-vsync` no ffmpeg novo e 429/403 do YouTube, recorrentes desde 24/09.
- (fechada 01/10) **Kelsen sem Skill nova** desde 28/09 — rompido em 01/10 com a Skill SELCA v1.1.
- (nova 07/10) **Duração fora do padrão e lacuna de prioridade zero ignorada.**
  - Evidência (`list_task_runs`): 07/10 durou ~5h38min (09:07–14:45) contra ~14 min em 05/10, ~1h51min em 06/10, ~12 min em 01/10 e ~16 min em 29/09. É mais que o dobro da média, e a rodada não produziu Skill nova. No mesmo dia, a lacuna da vaga, aberta em 06/10 como prioridade zero da Diária, ficou para a Drenagem (livro-razão de 07/10).
  - Provável causa: a passagem estava velha (05/10), porque o Fechamento de 06/10 encerrou em 4 s. A lacuna só aparecia na passagem.
  - Sugestão: o Passo 0 da Diária deve ler direto em `pendencias.json` os itens `tipo: lacuna_conhecimento` abertos, sem depender só da passagem, e checar a data da passagem.
