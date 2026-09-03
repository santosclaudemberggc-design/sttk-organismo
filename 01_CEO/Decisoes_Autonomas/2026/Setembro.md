# Livro-Razão de Decisões Autônomas — Setembro/2026

Registro de tudo que o Wallenberg decidiu e executou **sem aprovação prévia** de Claudemberg, sob o modelo de ratificação posterior instituído em 20/07/2026 (ver regra de ouro no `CLAUDE.md`). Continuação de [Agosto/2026](Agosto.md).

---

### [2026-09-03] Exclusão da rotina "STTK Consolidada" + medição de tokens movida para a Reunião Semanal — decisão de Claudemberg

**Decisão de Claudemberg (nesta conversa):** (1) excluir tudo que rodava antes com erros/falhas no thread de otimização de tokens; (2) a medição de token passa a rodar **toda segunda, dentro da Reunião Semanal**.

**Executado por Wallenberg:**
- **Tarefa agendada `sttk-consolidada-otimizacaotokens` EXCLUÍDA do agendador** (14 sessões arquivadas). Reportava métricas fabricadas ("96% ↓", "45-67%", "Item 7 aguardando API"). SKILL.md substituído por lápide apontando para o novo passo.
- **`01_CEO/Painel_Fundador/rotina_sttk_consolidada.py` + `.bat` + `ROTINA_STTK_CONSOLIDADA_README.md` REMOVIDOS do repo** (`git rm`). Script inerte (`repo_path` fixo em `D:\sttk-organismo`) cujo gerador de registro diário sobrescrevia arquivos escritos à mão com texto contraditório.
- **Pasta órfã `wallenberg-drenagem-continua`** (a que editei por engano em 02/09) — SKILL.md substituído por lápide apontando para `-local`.
- **`wallenberg-reuniao-semanal/SKILL.md` — novo Passo 2.5:** roda `medir_tokens.py` + `custo_por_agente.py`, lê os JSON e monta na pauta a seção "3. SAÚDE DE CONSUMO (medido, não projetado)" — cache hit, contexto por conversa (semana vs. base vs. semana passada), top-3 agentes por custo, custo por rotina, e quantas rodadas de Drenagem o Portão barrou por fila vazia. Números só dos JSON, nunca inventados.

**Backups (em `_backups/2026-09-02/`):** `DELETADO_sttk-consolidada-otimizacaotokens_SKILL.md`, `DELETADO_wallenberg-drenagem-continua_ORFAO_SKILL.md`, `DELETADO_rotina_sttk_consolidada.py`, `wallenberg-reuniao-semanal_SKILL_pos-passo2.5-tokens.md`.

**Pendente (Claudemberg decidiu adiar):** trim do `_estado_kelsen.md` (~40k tokens, append-only) e aperto do hand-off Kelsen→Hely — só **depois** que o Kelsen fechar o caso Daniel-OB.

**Nota:** as pastas `sttk-consolidada-otimizacaotokens/` e `wallenberg-drenagem-continua/` seguem no disco em `~/.claude/scheduled-tasks/` (só a lápide) — remoção física da pasta bloqueada por permissão; Claudemberg apaga pelo Explorer se quiser.

**Como desfazer:** restaurar os arquivos dos backups acima; recriar a tarefa `sttk-consolidada-otimizacaotokens` via MCP scheduled-tasks com o cron `30 9 * * 1-5`; remover o Passo 2.5 de `wallenberg-reuniao-semanal/SKILL.md`.

---

### [2026-09-02] Portão de Trabalho na Drenagem Contínua (Opção B / Alvo A) — decisão de Claudemberg, executada por Wallenberg

**Contexto:** medição real de tokens (ferramenta `01_CEO/_ferramentas/token_tracking/`, commits `e15d8d9`..`5fe1c87`) mostrou que a "otimização de tokens" não reduziu custo por agente e que o maior bloco de gasto é as rotinas agendadas — `wallenberg-drenagem-continua` rodou 48× (~US$ 488 em tokens-equivalentes de API), boa parte com fila vazia. No plano **Pro** (R$ ~1.200/ano fixo) o custo real não é dinheiro, é bater no teto de uso semanal e o organismo travar — o que acontece em algumas semanas.

**Decisão de Claudemberg (nesta conversa):** (1) Alvo A — só cortes sem perda de qualidade de entrega; (2) modelo: Haiku só em varredura/reconciliação, Sonnet+ no Legal/Arquitetura; (3) **Opção B** — checagem barata antes de subir a rotina inteira. Pro fica.

**Executado por Wallenberg:**
- **Passo 2.5 (Portão de Trabalho)** novo: se `pendencias.json` (alc:auto + aberta), Skills propostas do mês e Notion "Treinos e Testes" estão os três vazios → registra 2 linhas no registro diário, atualiza `_estado_wallenberg` Seção 1 e **encerra a rodada** sem abrir Gestor nenhum. Se há fila, abre **só** os Gestores com item real (não os 3 sempre).
- **Passo 8a (Learning Agent)** passa a rodar só **segunda-feira E se houve execução real**; nos demais dias é pulado (a busca diária de vídeo YouTube/Instagram/watch queimava cota e rendia ~zero mudança).

**CORREÇÃO 03/09/2026:** a edição de 02/09 foi feita no arquivo errado — `wallenberg-drenagem-continua/SKILL.md`, que é órfão (não está nas tarefas agendadas). A tarefa que **de fato roda** (seg-sex 10:15, `enabled`) é **`wallenberg-drenagem-continua-local`**. As duas edições acima foram replicadas em `C:\Users\santo\.claude\scheduled-tasks\wallenberg-drenagem-continua-local\SKILL.md` em 03/09, antes da rodada das 10:22. O arquivo órfão fica com a mesma mudança (inócua). Mesmo padrão observado: nomes "-local"/"-v2-7" são as tarefas vivas; os nomes sem sufixo estão obsoletos.

**Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-02/wallenberg-drenagem-continua_SKILL_pre-portao-opcaoB.md` (arquivo órfão, versão longa). O `-local` (versão compacta) não teve backup pré-edição salvo; **como desfazer:** as duas mudanças são adições puras e delimitadas — remover o bloco "✅ Passo 2.5: PORTÃO DE TRABALHO ..." inteiro e o parágrafo "⚠️ EXECUTE SOMENTE SE ..." sob o Passo 8a.

**Não alterado:** `wallenberg-rotina-diaria-skills` (é geradora, não drenadora — "fila vazia" não se aplica; reduzir cadência dela é outra conversa) e `wallenberg-reuniao-semanal` (já é semanal, tem função de ratificação).

**Como desfazer:** restaurar o SKILL.md do backup acima para `C:\Users\santo\.claude\scheduled-tasks\wallenberg-drenagem-continua\SKILL.md`.

---

### [2026-09-03] Diária Skills v2.7 — Quinta-feira (Seg-Qui)

**Contexto:** rodada automática da `wallenberg-rotina-diaria-skills-v2-7`, 03/09/2026 (qui). Execução autônoma, Claudemberg ausente.

**Passo 1 — Pesquisa (5 eixos):**
- NBR 15575:2025 desempenho acústico pisos → ACHADO PRINCIPAL Complementares (publicada dez/2024, vigente jun/2025, ambientes sem dormitório agora obrigatórios)
- CAU-RJ + normativas RJ → Resolução SMDU 10/2026 (03/07/2026) → ACHADO PRINCIPAL Legal (Consulta Prévia + RDT obrigatório)
- Render/vídeo → nada novo (Remodel AI cloud, Redraw cloud, Leonardo cloud — violam critério 2)
- Apresentação interativa cliente → 3ª busca sem ferramenta gratuita viável (BIMx pago, pCon só interiores, Unreal Engine pesado)
- GitHub Revit/BIM → 2 novos achados para Vitruvius: BIMwright/rvt-mcp (229 tools, 166 commits, Apache-2.0) e UV-Tech/revit-claude-mcp (40 tools, MIT)

**Passo 2 — Consolidação:** 2 Skills novas (Trilha A), 0 Trilha B, 2 achados Vitruvius, 6 descartados com justificativa.

**Passo 3 — Redação:**
- `legal_resolucao-smdu-10-2026-consulta-previa-rdt-rj.md` (Trilha A, Legal — Kelsen/Hely + Lúcio/Oscar)
- `complementares_nbr15575-2025-desempenho-acustico-pisos.md` (Trilha A, cross-disciplina Baumgart/Saturnino/Tenreiro)
- `vitruvius_achados_candidatos.md` atualizado com 2 novos achados (BIMwright + UV-Tech)
- Ambas Skills v1.0, Status: proposta.

**Passo 4 — Salvamento:** `01_CEO/Skills_Propostas/2026/Setembro/`. Índice atualizado com 2 novas linhas + observações da rodada + prioridades atualizadas. Livro-razão registrado aqui.

**Passo 5 — PDF:** 3 gerados (2 Skills + índice).

**Passo 8 — Ferramentas:** nenhum achado novo que passe nos 4 critérios para Skill isolada de ferramenta. Os 2 achados Revit (BIMwright + UV-Tech) foram registrados em vitruvius_achados_candidatos.md conforme instrução de Claudemberg 27/08 — não viram Skill de usabilidade isolada porque são candidatos a agregar ao Vitruvius, não ferramentas independentes.

**Como desfazer:** apagar `legal_resolucao-smdu-10-2026-consulta-previa-rdt-rj.md` e `complementares_nbr15575-2025-desempenho-acustico-pisos.md`; reverter edições no `indice.md` (remover linhas 03/09 e observações da rodada 03/09); reverter entradas de 03/09 em `vitruvius_achados_candidatos.md`.

---

### [2026-09-02] Diária Skills v2.7 — Quarta-feira (Seg-Qui)

**Contexto:** rodada automática da `wallenberg-rotina-diaria-skills-v2-7`, 02/09/2026 (qua). Execução autônoma, Claudemberg ausente.

**Passo 1 — Pesquisa (5 eixos):**
- NBR 15220-3:2024 zoneamento bioclimático → JÁ coberto em 01/09
- CAU-RJ deliberações 2026 → 009 já coberta; 008 (ATHIS) fora de escopo STTK
- Render/vídeo IA → Luw.ai descartado (cloud + watermark + sem MCP); demais freemium
- NBR 15575 Emenda 1/2025 → dado novo confirmado: Upar ≤ 2,7 W/(m².K) zona 4A
- NBR 9575:2024 impermeabilização → ACHADO PRINCIPAL, prioridade do índice

**Passo 2 — Consolidação:** 1 Skill nova (NBR 9575), 0 Trilha B, 5 descartados com justificativa.

**Passo 3 — Redação:** `complementares_nbr9575-2024-impermeabilizacao-selecao-projeto.md` (Trilha A, cross-disciplina Saturnino/Baumgart/Tenreiro). v1.0, Status: proposta.

**Passo 4 — Salvamento:** `01_CEO/Skills_Propostas/2026/Setembro/`. Índice atualizado. Livro-razão registrado aqui.

**Passo 5 — PDF:** 2 gerados (Skill NBR 9575 + índice Setembro).

**Passo 8 — Ferramentas:** nenhum achado novo que passe nos 4 critérios. Burle bloqueado por config (não por ferramenta). Portinari sem ferramenta gratuita de apresentação self-hosted.

**Como desfazer:** apagar `complementares_nbr9575-2024-impermeabilizacao-selecao-projeto.md` e reverter edições no `indice.md` (remover linha 02/09 e observações da rodada 02/09).

---

### [2026-09-02] Drenagem Contínua v2.3 — 3ª execução real (10:15)

**Contexto:** terceira rodada da `wallenberg-drenagem-continua` sob tarefa agendada, 02/09/2026 (ter). Execução autônoma, Claudemberg ausente.

**Fila:** Zero item `alc:"auto"` + `status:"aberta"` em `pendencias.json` (limpa desde 31/08). 3 Skills propostas em Setembro (LC 281/2025, NBR 15220-3:2024, NBR 9575:2024).

**Execução real:**
- **Kelsen:** Varredura identificou 2 ações represadas (continuação de 01/09): (1) frases-genericas — executável, bloqueado por modo automático; (2) pops-cópias — confirmado, 4 documentos para remover/sincronizar. Wallenberg executa quando Claudemberg presente. Nenhum Hely acionado. Base estável.
- **Lúcio:** Fila reconciliada. WAN 2.2 reconfirmado vencido (28/08 → 05 dias sem progresso). Exame 2 dos 3 Agentes completo em 17/08. Varredura: nenhum achado novo. Estado estável, 3ª rodada consecutiva sem execução. Nenhum agente acionado.
- **Cardozo:** Fila reconciliada. Varredura de melhoria: **criado POP-COMPL-02** (bloqueador encontrado em execução), formalizado protocolo de diagnóstico/escalação. Item registrado em pendencias.json como resolvido. Nenhum agente acionado. Pronto para Exame 1 dos 6 quando Wallenberg administrar.

**Métricas:** 3 Gestores processados | 1 execução real (Cardozo POP) | 0 itens pendencias.json fechados (novo POP já é resolvido) | Learning Agent: nenhuma modificação ao SKILL.md (padrões de agosto funcionando).

**Próximas ações:**
- Wallenberg: executar 2 ações Drive Kelsen quando Claudemberg presente (modo manual, não automático)
- Wallenberg: administrar Exame 1 dos 6 Agentes de Cardozo (testes preparados)
- Wallenberg: verificar 2 conectores MCP (Lúcio, escalação 08/08) — Burle/Portinari
- Claudemberg: ratificar 3 Skills propostas (Setembro)

**Como desfazer:** remover entrada de POP-COMPL-02 em pendencias.json, deletar arquivo do POP.

---

### [2026-09-01] Drenagem Contínua v2.3 — 2ª execução real (10:15)

**Contexto:** segunda rodada da `wallenberg-drenagem-continua` sob tarefa agendada, 01/09/2026 (seg). Execução autônoma, Claudemberg ausente.

**Fila:** Zero item `alc:"auto"` + `status:"aberta"` em `pendencias.json` (limpa desde 31/08). 2 Skills propostas aguardam ratificação (LC 281/2025, NBR 15220-3:2024).

**Execução real:**
- **Kelsen:** Varredura identificou 2 ações represadas: (1) frases-genericas — 5 substituições redigidas, pronta para Service Account (bloqueada por modo automático); (2) pops-cópias — achado confirmado, recomendação feita. Base sincronizada. Próxima varredura 04/09.
- **Lúcio:** Varredura confirmou REGRA-ARQ-01 propagada, Exame 2 completo (Assisted). WAN 2.2 vencido sinalizado. Achados Drive consolidados: 4 POPs cabeçalho desatualizado. Estado estável.
- **Cardozo:** Varredura confirmou Trilha A completa (6 Skills + 2 propostas), 6 Agentes nomeados 26/08, 1 POP criado. Pronto para Exame 1 dos 6. **Ação pendente:** card Cardozo ao Painel (desde 31/08).

**Métricas:** 3 Gestores processados | 0 execução real fechada | 0 itens pendencias.json fechados | 0 Learning Agent (WebSearch bloqueado).

**Próximas ações:**
- Claudemberg: ratificar 2 Skills
- Wallenberg: card Cardozo ao Painel; 2 ações Drive Kelsen quando Claudemberg presente
- Wallenberg: verificar 2 conectores MCP (Lúcio, 08/08) antes de reportar Skill fechada

---
