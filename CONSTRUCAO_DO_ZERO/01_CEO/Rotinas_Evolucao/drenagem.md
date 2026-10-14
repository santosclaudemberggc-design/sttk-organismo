# Drenagem Contínua — evolução

Tarefa `wallenberg-drenagem-continua-local` · seg-sex 11:00 · referência `CONSTRUCAO_DO_ZERO/01_CEO/wallenberg-drenagem-continua-v2_SKILL.md`

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
| **v2.6.0** | 09/10/2026 | (1) Auditoria só vale com prova (Bardi confere ≥ 3 afirmações por amostragem, −1,00 por afirmação falsa/sem prova); (2) teto de 3 versões por etapa do Ensaio: na 3ª reprovação a Drenagem para e grava `diagnostico_repeticao.md` para Claudemberg decidir | Etapa 2 com 9 versões e etapa 3 com 8; nota caiu de 10,00 (v7) para 7,00 (v8) na etapa 2; 4 declarações de verificação falsas do Gestor na etapa 3 | Claudemberg (análise do organismo, 09/10) |
| v2.6.1 | 10/10/2026 | (3) gabarito só entra no commit depois da aprovação, com `git add -f` do arquivo da etapa (pasta no `.gitignore`); (4) respeitar `trava_etapa_5` no estado do Ensaio | Gabarito da etapa 4 visível no `git status` e citado na nota do Lúcio; D4 segura a etapa 5 até o exame do Oscar no Revit | Claudemberg (D4 e D9a, 10/10) |
| v2.6.2 | 14/10/2026 | (5) Herança obrigatória: o pedido ao Gestor leva os caminhos das entregas aprovadas de todas as etapas anteriores, as erratas e o caso base; na Arquitetura, checklist de entrega do Oscar e de auditoria do Lúcio antes do Bardi | Etapa 4: SMD omitida nas 3 versões; o Oscar não recebeu as etapas 1 e 2 (treino do Lúcio, 14/10) | Claudemberg (14/10) |
| v2.6.3 | 14/10/2026 | (6) Etapa com desenho exige desenho de verdade no Revit: esquemático com lacunas marcadas, arquivo do caso (nunca .rte real nem arquivo de cliente), cotas conferidas, Lúcio devolve "não atende" sem lacuna provada; Revit fechado vira registro e pedido a Claudemberg | Drenagem de 14/10: Oscar não desenhou a etapa 5 ("falta programa") com Revit ligado; refeito ao vivo pelo Oscar via Lúcio (entrega/v2) | Claudemberg (14/10) |

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
| 01/10 | sim | ~2h25min (14:04-16:28) | Ensaio 003 etapa 1 executada e corrigida; varredura mensal de Drive; pós-aprovação: Kelsen corrigiu 4 Skills + 2 POPs e capacitou Hely | Duração bem acima da média das rodadas reais (~14 min, excluindo a anomalia de 28/09) — explicada pelo volume: 1ª execução do Ensaio + correções ordenadas ao vivo por Claudemberg na mesma sessão |
| 07/10 | sim | ~50 min (11:04–11:54) | Ensaio 003 etapa 3 v5 (Lúcio→Oscar) + Bardi (reprovar); lacuna da vaga → Skill nova do Kelsen; +2 lacunas abertas; Notion VILLACA-001 → aprovado | Fez a lacuna que a Diária não tratou. Notion LELE-002 e `auditoria_lele.json` negados pela permissão automática. Diário sem linhas de 02 a 06/10 |
| 09/10 | sim | ~47 min (11:03–11:50) | Ensaio 003 etapa 4 executada e corrigida (Lúcio 7,75; Oscar 6,25; Bardi reprovar). 5 itens de pendências resolvidos (Skills de vaga e de critérios, checagem de gabarito) | Trim dos 3 arquivos de estado não executado; fica para a próxima rodada. Sem candidata nova |
| 13/10 | sim, em curso às 20:04 | desde 11:03 (~9 h até agora, sem encerrar) | Registro gravado: 8 itens auto (Lúcio 4, Kelsen 2, Bardi 1, Wallenberg 1) e 1 conflito humano (COES, p. 15 × p. 19) | Sessão não encerrou no horário; ver a candidata de sessão aberta |

## 3. Candidatas a melhoria
- (aberta) **Sessão de 28/09 ficou aberta cerca de 24 h.** Verificar se ela se repete.
  - (dados 13/10, `list_task_runs`) Sessões que ficam abertas depois do trabalho, com última atividade horas depois do início (11:03): 09/10 até 21:51 (~10 h 45 min); 12/10 até 09:32 do dia 13 (~22 h 30 min); 13/10 ainda em curso às 20:04 (~9 h). Três de três dias úteis com sessão longa: o padrão se confirma. Sugestão: fechar a sessão ao fim da fila e separar "tempo da rotina" de "sessão aberta".
- (confirmada 01/10) **Primeira execução do Ensaio em 01/10.** Durou ~2h25min, cerca de 10x a média das rodadas anteriores (23-29/09, excluindo a anomalia de 28/09). Gabarito lacrado respeitado (SHA256 conferido antes/depois). Observar se a duração cai nas próximas etapas ou se é o novo normal com o Ensaio rodando.
- (dados novos 07/10, para a candidata "sessão aberta 24 h") Pelo `list_task_runs`, a sessão de 05/10 ficou aberta ~8h30 (11:03–19:33) e a de 06/10 ~9h09 (11:04–20:13). Nas duas datas o livro-razão registra decisões de Claudemberg ao vivo na mesma sessão, o que provavelmente explica a duração. 07/10 voltou a ~50 min. Sugestão: separar no diário "tempo da rotina" e "sessão ao vivo com Claudemberg", para a média não se misturar.
- (dados 09/10) Rodada de 09/10: 47 min (11:03–11:50). A de 08/10 durou 3h32 e tem decisões ao vivo de Claudemberg no livro-razão. Mais um dado para separar tempo da rotina e sessão ao vivo.
