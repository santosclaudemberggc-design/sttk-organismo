# Reunião Semanal — evolução

Tarefa `wallenberg-reuniao-semanal` · segunda 17:00 · pautas em `CONSTRUCAO_DO_ZERO/04_REUNIOES_SEMANAIS/`

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| — | 20/07/2026 | Redefinida: ratificação do que Wallenberg já fez + decisões reservadas a Claudemberg | Wallenberg passou a executar sozinho no escopo do organismo | Claudemberg |
| Saúde de consumo | 03/09/2026 | Medição real de tokens (substitui a rotina "STTK Consolidada", que fabricava métricas) | Métricas inventadas | Claudemberg |
| Quinzenal (teste) | 08/09/2026 | Teste quinzenal até 08/10 | Volume baixo de decisões | Claudemberg |
| Correção do cron | 22/09/2026 | Cron `30 10 * * 1` + Passo 0 (dia 8-14/22-28) | O cron antigo disparou quase todo dia (09-12, 14, 21, 22/09) | Wallenberg |
| **v2.0** | 30/09/2026 | **Semanal**, segunda 17:00; abre com a Verificação dos Ensaios; ratificação com a linha "COMO RESPONDER" e o contador ⏳; livro-razão do mês atual + anterior; sem PDF | As pautas tinham ☐ sem resposta (R1 esperando desde 14/09); a reunião rodava às 10:30 sem Claudemberg presente | Claudemberg |

**Tentado e revertido:** quinzenal (08/09 → 30/09, encerrado antes do prazo; a decisão foi voltar a semanal).

## 2. Diário de funcionamento
| Data | Rodou? | Resposta de Claudemberg? | Itens pendentes | Observação |
|---|---|---|---|---|
| 21/09 | sim | não | — | Cron antigo |
| 22/09 | sim | não | — | Cron antigo |
| 28/09 | sim | parcial (D1 em outra sessão) | R1-R4+ sem ☑ | — |
| 13/10 | sim, fora do cron (terça 08:03; cron é segunda 17:00). Segunda 12/10 sem execução | não verificado nesta rodada | — | ~2 min (08:03–08:05); a pauta de 12/10 não aparece no registro |

## 3. Candidatas a melhoria
- (observar) Com a linha "COMO RESPONDER" e às 17:00, as ratificações passam a ser respondidas? Se ficarem 2 semanas sem resposta, repensar o formato.
- (nova 13/10) **Segunda 12/10 sem reunião registrada; disparo recuperado na terça às 08:03.** Evidência: `list_task_runs` sem execução em 12/10 e execução em 13/10 (2 min). A pauta de 12/10 não chegou a Claudemberg pelo registro. Mesmo padrão do Acervo e do Fechamento.
