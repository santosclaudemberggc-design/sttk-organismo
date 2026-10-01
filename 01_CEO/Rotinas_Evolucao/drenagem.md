# Drenagem Contínua — evolução

Tarefa `wallenberg-drenagem-continua-local` · seg-sex 11:00 · referência `01_CEO/wallenberg-drenagem-continua-v2_SKILL.md`

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| v2.3 | 28/08/2026 | Recriada do zero como tarefa agendada | A v2.3 nunca tinha ficado registrada como tarefa (wrapper órfão) | Claudemberg |
| v2.3 (J.1-J.3) | 31/08/2026 | Validação de Skill-ferramenta obrigatória; a cadeia não trava com Gestor abaixo de Autonomous; varredura de Drive | Lições da 1ª rodada real | Claudemberg |
| Portão B/A | 02/09/2026 | Portão de Trabalho: fila vazia encerra; só abre Gestor com item real | Abrir 3 Gestores para ouvir "nada a fazer" custava cerca de 90 mil tokens por rodada | Claudemberg |
| v2.4 | 16/09/2026 | Filtro geográfico, 3 travas do Notion, staging de MCP, log via `Append-STTKLog.ps1` | Mesclagem; a sobrescrita integral foi recusada | Claudemberg |
| v2.4.1 | 17/09/2026 | Proibido `Bash cd && powershell` | Rodada de 17/09 morreu por permissão negada e mesmo assim apareceu como "succeeded" | Wallenberg (incidente) |
| v2.4.2 | 28/09/2026 | Coerência entre Skills, arquivamento imediato, treino fictício | Espelho da Diária v3.4.0 | Claudemberg |
| **v2.5.0** | 30/09/2026 | Horário 10:15 → 11:00; **passa a EXECUTAR o Ensaio Sombra 003** (Passo 2.4 + FASE 4.5); refazer etapa reprovada; pede aprovação no fim do relatório; sem treino; sem PDF | Desde 08/09 a Diária ativa as Skills e a Drenagem rodava vazia (29/09 durou cerca de 1 min) | Claudemberg |

**Tentado e revertido:** treino fictício (J.7 item 3, revogado em 30/09).

## 2. Diário de funcionamento
| Data | Rodou? | Duração | Resultado | Observação |
|---|---|---|---|---|
| 23/09 | sim | ~42 min | trabalho real | Rodou às 17:25 (fora do horário) |
| 24/09 | sim | ~12 min | — | — |
| 25/09 | sim | ~2 min | — | — |
| 28/09 | sim | sessão aberta por cerca de 24 h | — | Anomalia: last_activity 29/09 10:11 |
| 29/09 | sim | ~1 min | fila vazia | Sintoma que motivou a v2.5.0 |
| 30/09 | pausada | — | — | Revisão das rotinas |

## 3. Candidatas a melhoria
- (aberta) **Sessão de 28/09 ficou aberta cerca de 24 h.** Verificar se ela se repete.
- (aberta) **Primeira execução do Ensaio em 01/10.** Observar duração, custo e se o Gestor respeita o gabarito lacrado.
