# Rotina Acervo de Normas — evolução

Tarefa `wallenberg-rotina-acervo-normas` · segunda 13:00 · acervo `D:\008_Normas ABNT\` (índice `_indice_acervo.md`) · sem arquivo de referência (o prompt agendado é a fonte única)

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| v1.0 | 29/09/2026 | Criada (reorganização de `D:\008`, só fonte oficial, Substituídas sem apagar, lista de compra) | O acervo estava desorganizado; Skills saíam "com ressalva" com a norma disponível na pasta | Claudemberg |
| v1.1 | 29/09/2026 | O dono passa a ser Wallenberg (função do CEO); a legislação fica com Hely via Kelsen | O acervo é compartilhado por todos os Gestores | Claudemberg |
| **v1.2** | 30/09/2026 | Horário 07:00 → 13:00; texto do dono corrigido; semanal leve com portão + completa na 1ª segunda do mês; prioridade P1/P2 do Ensaio; norma que trava o Ensaio vai para o topo da lista de compra | Conferir cerca de 40 normas toda semana é caro; o Bardi corrige pela fonte primária | Claudemberg |

## 2. Diário de funcionamento
| Data | Rodou? | Modo | Resultado | Observação |
|---|---|---|---|---|
| — | nunca rodou | — | — | 1ª execução em 05/10 (modo completo, 1ª segunda do mês) |
| 13/10 | sim, fora do cron (terça 08:03; cron é só segunda 13:00). Segunda 12/10 sem execução | fora do cron | ~2 min (08:03–08:05) | Sem rastro de resultado lido nesta rodada |
| 14/10 | não rodou | — | — | Cron só segunda 13:00. Última execução 13/10 (08:03, recuperação) |
| 16/10 | não rodou | — | — | Cron só segunda 13:00 (hoje é sexta) |

## 3. Candidatas a melhoria
- (conhecida) NBR 15220-3 faltando no acervo (memória de referência).
- (nova 13/10) **Segunda 12/10 sem execução; disparo recuperado na terça às 08:03.** Evidência: `list_task_runs` sem registro em 12/10 e execução em 13/10. Mesmo padrão do Fechamento e da Reunião naquela segunda. Sugestão: a checagem de segunda (Fechamento de sexta/segunda) deve verificar se o disparo do dia aconteceu.
