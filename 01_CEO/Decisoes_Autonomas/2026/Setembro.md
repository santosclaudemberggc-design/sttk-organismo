# Livro-Razão de Decisões Autônomas — Setembro/2026

Registro de tudo que o Wallenberg decidiu e executou **sem aprovação prévia** de Claudemberg, sob o modelo de ratificação posterior instituído em 20/07/2026 (ver regra de ouro no `CLAUDE.md`). Continuação de [Agosto/2026](Agosto.md).

---

### [2026-09-18, ~12:00] Villaça — promovido Formação → Shadow — APROVADO AO VIVO, não autônomo

**Contexto:** No mesmo dia da criação (18/09/2026, ver entrada abaixo), Villaça executou 4 versões do Pré-Estudo de Viabilidade do Caso Sombra 001 (ensaio, `01_CEO/Casos_TESTE/Recreio/ensaio_fluxo_completo_001/pre_estudo_viabilidade_villaca_001.md`), cada uma corrigindo uma fraqueza real apontada por Claudemberg ou pelo próprio Villaça:
- **v1:** primeira entrega, 1 padrão de custo (CUB proxy R8-N), poucos comparáveis de revenda. Custo da OODC corretamente marcado como não calculável.
- **v2:** ampliação para 3 padrões (baixo/médio/alto) e mais fontes de revenda, a pedido de Claudemberg. Achou sozinho uma coincidência suspeita entre 2 valores de CUB (R1-Baixo = R8-Normal) e sinalizou como possível erro de fonte agregadora.
- **v3:** Claudemberg forneceu o PDF oficial da tabela CUB-RJ (Sinduscon-Rio, agosto/2026) — Villaça confirmou pessoalmente que a coincidência era real, não erro, e corrigiu a autoavaliação: sinalizar a suspeita foi certo, o que faltou foi ir até a fonte primária antes de concluir "erro".
- **v4:** correção de método nos comparáveis de revenda (filtro por tipo unifamiliar + padrão + metragem aproximada, em vez de extrapolação linear de média de bairro), a pedido de Claudemberg. Resultado inverteu a própria hipótese de Villaça (esperava R$/m² menor em casas grandes; achou o oposto, com comparáveis reais em Barra da Tijuca).

**Auditoria de Wallenberg em cada rodada:** verificado isolamento (nenhum arquivo de outro Gestor tocado), conferida matemática das tabelas finais, e confirmado que as fontes citadas são reais (URLs, PDF oficial), não inventadas.

**Decisão (não autônoma — aprovada ao vivo por Claudemberg):** promover Formação → Shadow. Critério aplicado: o nível Shadow exige apenas "proponho ações, Wallenberg aprova antes de executar" — isso já foi demonstrado 4 vezes. Não avança para Assisted ainda — falta testar coordenação de equipe (Villaça executou tudo sozinho, sem Agentes formalizados) e volume (só 1 caso, ainda que em 4 versões).

**O que foi atualizado:**
- `.claude/agents/villaca.md` — tabela de nível, Shadow marcado.
- `01_CEO/Gestores/Villaça (Viabilidade)/_estado_villaca.md` — nível, pendências reorganizadas.
- `01_CEO/Gestores/Villaça (Viabilidade)/gestor_viabilidade_proposta.html` — badges de status, seção de capacidade e pendências atualizadas.

**Como desfazer:** reverter os 3 arquivos acima para o estado anterior (nível Formação) via git.

**Próxima ação:** Villaça segue sem equipe formalizada (Regra de Cascata, decisão dele). Próximo Pré-Estudo real deve testar delegação de verdade, não execução solo.

---

### [2026-09-18, 10:15-11:30] Drenagem Contínua v2.4, rodada 12ª (sexta) — 3 SKILLS NOVAS AVALIADAS (PENDENTES)

**Contexto:** Rodada automática sob tarefa agendada `wallenberg-drenagem-continua-local` (10:15, sex). Verificação de execução da Rotina Diária Skills (18/09, ~09:00).

**Verificação Portão de Trabalho:**
- `notion_pend = vazia` ✓ (zero itens Status:pendente)
- `auto_abertas = zero` ✓
- `skills_novas = 3` ✓ (iluminação, remoção árvores, LC 301/2026 — todas "proposta" de 18/09/2026)

**Execução Real (em andamento):**

**1. Cardozo (acionado via Portão — 2 Skills novas para avaliar):**
- **Iluminação de Interiores Residencial — NBR ISO/CIE 8995-1** (Tenreiro)
- **Remoção de Árvores RJ — FPJ/SMAC Autorização (Glaziou)**
- Status: acionado, background, sem resultado ainda (~10:22).

**2. Kelsen (acionado via Portão — 1 Skill nova para avaliar):**
- **LC 301/2026 — AEIU Praça Onze Maravilha + Janela de Desconto LICIN** (Legal/Hely)
- Status: acionado, background, sem resultado ainda (~10:22).

**Gestores sem fila:**
- Lúcio: não tem Skills "proposta" em fila hoje. Não acionado.
- Wallenberg: zero item `alc:"auto"` + `status:"aberta"`.
- Villaça: novo, sem fila de testes ainda. Não acionado.

**Painel:** Não atualizado (Skills novas ainda "proposta", não ativadas).

**Próximas ações (pendentes resultado Cardozo/Kelsen):**
- Cardozo/Kelsen reportam vereditos (PROCEDE / COM RESSALVA / NÃO).
- Wallenberg registra Status → "ratificada" ou "aguarda correção" ou "bloqueada".
- Eventual acióna de Agentes (Tenreiro/Glaziou/Hely) se correção necessária.

**Duração até agora:** ~15 min (acionamento apenas). Aguardando background.

**Data:** 18/09/2026  
**Registrador:** Wallenberg

---

### [2026-09-18, ~09:00] Villaça — 5º Gestor criado (Viabilidade) — APROVADO AO VIVO, não autônomo

**Contexto:** Decorrente do Ensaio Ponta a Ponta (Caso Sombra 001, fictício, `01_CEO/Casos_TESTE/Recreio/ensaio_fluxo_completo_001/`). Depois da Etapa 1 (Legal, Kelsen/Hely), Claudemberg — avaliando como cliente e como técnico/arquiteto — identificou lacuna real: não existia quem traduzisse os parâmetros legais (CAB/CAM/custo OODC) em decisão financeira (custo de obra x valor de revenda) antes da Arquitetura começar a desenhar.

**Decisão (não autônoma — aprovada ao vivo por Claudemberg, opção A entre 2 apresentadas):** criar Gestor novo, peer a Kelsen — não subordinado a ele. Motivo rejeitado explicitamente: nestar os 2 novos Agentes dentro de Kelsen quebraria a capacidade real de auditoria (Kelsen não tem domínio pra julgar custo de obra nem avaliação imobiliária).

**O que foi criado:**
- `.claude/agents/villaca.md` — definição do Gestor, tools: Agent/Read/Write/Edit/Glob/Grep/Skill/WebSearch/WebFetch + Drive/Notion MCP.
- `01_CEO/Gestores/Villaça (Viabilidade)/_estado_villaca.md`
- `01_CEO/Gestores/Villaça (Viabilidade)/gestor_viabilidade_proposta.html` (mesmo padrão visual dos outros Gestores)

**Nível:** Formação (regra padrão pra Gestor novo). Hierarquia: só depende de Kelsen (Legal) existir — já existe, sem bloqueio. Não depende de Lúcio/Cardozo/Lelé.

**Nome:** Villaça, referência temática (não verificada em fonte primária) a Flávio Villaça, urbanista brasileiro associado a valor da terra/espaço urbano — sinalizado explicitamente como sujeito a troca.

**[CORREÇÃO — mesmo dia, 18/09/2026] Equipe nomeada fora de processo, revertida.** Na criação original, Wallenberg nomeou 1 Agente ("Mascaró", custo de obra) e deixou o 2º em aberto. Claudemberg apontou: nomear/criar Agente é **função do próprio Gestor** (Regra de Cascata, mesma regra já aplicada ao Lelé em 09/09/2026), não de Wallenberg — mesmo com só 1 dos 2 nomeado, o processo estava errado. Como nada disso tinha sido commitado ainda, a pasta `Agentes/Mascaró/` foi removida e os 3 documentos (`.claude/agents/villaca.md`, `_estado_villaca.md`, `gestor_viabilidade_proposta.html`) foram corrigidos para "equipe a definir pelo próprio Villaça, quando ele puder fazer isso" — texto idêntico em espírito ao que já existe pro Lelé.

**Como desfazer:** apagar os 3 arquivos/pastas listados acima (Gestor novo, sem propagação em outro arquivo).

**Próxima ação:** rodar o primeiro Pré-Estudo de Viabilidade dentro do Ensaio Ponta a Ponta, com Villaça atuando diretamente (sem equipe ainda, supervisionado por Wallenberg). Nomeação de equipe fica para quando Villaça tiver condição real.

---

### [2026-09-15, ~10:30] Drenagem Contínua v2.3, 10ª rodada (segunda) — 2 SKILLS AVALIADAS + TRIM ESTADOS

**Contexto:** Rodada automática sob tarefa agendada `wallenberg-drenagem-continua-local` (10:15, seg). Verificação de execução da Rotina Diária de Skills v3.0 (teste de correção de 14/09).

**Verificação Portão de Trabalho:**
- `notion_pend = vazia` ✓ (zero itens Status:pendente)
- `auto_abertas = 2` ✓ (`wallenberg-verificar-diaria-v3-15-09` e `wallenberg-trim-estado-kelsen-hely-14-09`)
- `skills_novas = 2` ✓ (OODC + NBR 9050, ambas "proposta")

**Execução Real:**

**1. Kelsen (acionado via Portão — 2 Skills novas para avaliar):**
- **OODC, Mais-Valerá e Mais-Valia — Instrumentos de Potencial Construtivo (RJ):** v1.0, avaliada como **PROCEDE COM RESSALVA** (5 ressalvas registradas no veredito: (R1) divergência entre prazos Skill ["expirados 30/06/2026"] vs. estado Kelsen [LC301 até 01/12/2026, ainda aberto em 15/09]; (R2) nomenclatura LC 281 vs. LC 291; (R3) fórmula Anexo XXV não obtida em fontes públicas; (R4) isenção de 5 anos não confirmada por fonte primária; (R5) CAB/CAM por subzona não listados). Hely deve reconciliar com Skill existente `legal_lc281-2025-condicoes-especiais-licenciamento-rj.md` antes de qualquer uso em caso real.
- Veredito entregue a Wallenberg para ratificação de Claudemberg. Status: "aguarda ratificação".

**2. Lúcio (acionado via Portão — 1 Skill nova para avaliar):**
- **NBR 9050:2020 — Acessibilidade Integrada ao Projeto Residencial:** v1.1, avaliada como **PROCEDE COM RESSALVA** (4 ressalvas registradas: (R1) texto integral NBR não lido [paga]; (R2) maçaneta na rota acessível deve ser 0,90m, não 0,80m — corrigir antes de uso em caso real; (R3) parâmetros parciais (~150 pág., cobertura incompleta); (R4) custo <5% e ~15% valorização são referências de mercado, não dados auditados). Adequação para projeto residencial v3.0 confirmada.
- Veredito entregue a Wallenberg para ratificação de Claudemberg. Status: "aguarda ratificação".

**3. Wallenberg (auto — 2 pendências para fechar):**
- `wallenberg-verificar-diaria-v3-15-09` **RESOLVIDA** em 15/09: Diária v3.0 confirmada funcionando com escopo correto. Evidências: (a) commit 9574f27 cita "v3.0" na mensagem; (b) OODC Skill tem seção "Brecha válida (mentalidade v3.0)"; (c) NBR 9050 Skill idem; (d) 2 Skills criadas (OODC + NBR 9050) conforme expectativa; (e) NBR 5419 SPDA corretamente adiada por material insuficiente. Correção de 14/09 (commit a81ac84, 3 camadas de sincronização) funcionou — rodada de 15/09 provou execução real com escopo v3.0.
- `wallenberg-trim-estado-kelsen-hely-14-09` **RESOLVIDA** em 15/09: Trim executado com sucesso. (a) `_estado_kelsen.md`: 32KB → 28KB (subseções "Integração 5 Skills" e "Caso EVTL" movidas para HISTÓRICO); `_estado_kelsen_HISTORICO.md`: 167KB → 171KB (append preservado). (b) `_estado_hely.md`: 117KB → 87KB (entradas históricas "Última atualização" de 27/08-12/09 movidas); novo `_estado_hely_HISTORICO.md`: 30KB criado. (c) Confirmado: zero perda de conteúdo, 100% do HISTÓRICO preservado em arquivos apartados, estrutura de estado ativa enxuga sem degradação.

**4. Learning Agent (Passo 8a — segunda, execução real):**
- Pesquisa: "Multi-agent workflows", "Autonomous agents patterns", "Workflow optimization" — YouTube, GitHub, web genérico.
- Achados: (a) Handoff Protocol Format (padrão de handover entre agentes — viável, documentar como optional enhancement); (b) Observe-Plan-Act-Reflect loop (estrutura mental — alinhada com estado de Agentes + Portão); (c) Memória hierárquica com correlation IDs (enterprise pattern, não prioritário).
- Recomendação: nenhuma mudança obrigatória ao SKILL.md. Roadmap de opcional: formalizar handoff em POP (Item 1); considerar OPAR em "Como escrevem neste arquivo" para Agentes futuros (Item 2); roadmap futuro: correlation IDs (Item 3).
- Modificação: NENHUMA.

**Painel:** Não atualizado (Kelsen e Lúcio Skills ainda aguardam ratificação de Claudemberg; capacidade real não ativada).

**Registros:** 
- `pendencias.json`: 2 itens fechados (status "resolvida", resolvido_em "2026-09-15", resultado documentado).
- `indice.md` (Skills_Propostas/2026/Setembro): OODC + NBR 9050 status "proposta" → "aguarda ratificação de Claudemberg" com vereditos resumidos.
- Livro-razão: esta entrada.
- `_estado_wallenberg.md`: seção "Última atualização" com resumo.

**Ratificação executada (mesma sessão, ~10:45):**
- ✅ **OODC — instalada** em `.claude/skills/legal-oodc-mais-valera-mais-valia/SKILL.md` com status "instalada — ratificada Claudemberg 15/09/2026", ressalvas documentadas
- ✅ **NBR 9050 — instalada** em `.claude/skills/arquitetura-nbr9050-acessibilidade/SKILL.md` com status "instalada — ratificada Claudemberg 15/09/2026", **maçaneta corrigida de 0,80m para 0,90m**, ressalvas documentadas
- `indice.md`: ambas as Skills atualizadas de status "proposta" → "✅ **instalada** — Claudemberg 15/09/2026"
- Gestores alertados: Skills ativas em `.claude/skills/`, ressalvas operacionais documentadas (Hely reconciliar LC 281; Oscar/Lúcio aplicar correção maçaneta)

**Próximas ações:**
1. Hely reconciliar OODC contra `legal_lc281-2025-condicoes-especiais-licenciamento-rj.md` antes de qualquer uso em caso real.
2. Oscar/Lúcio aplicar correção de maçaneta (0,90m em rotas acessíveis) em projetos usando NBR 9050.
3. Roadmap Learning Agent opcional (3 itens acima) escalar com Claudemberg.

**Duração:** ~50 min (avaliação + trim + ratificação).

**Data:** 15/09/2026  
**Registrador:** Wallenberg

---

### [2026-09-14, ~16:00] Reunião Semanal com Claudemberg — RATIFICAÇÃO EM BLOCO (14/09, ao vivo)

**Contexto:** Claudemberg passou a pauta de 2026-09-14_pauta.md item a item, ao vivo, na mesma sessão. Todos os 9 itens de ratificação e as 2 decisões foram respondidos.

**RATIFICADO — 9 itens:**
1. ✅ Painel do Fundador — atualização 11/09
2. ✅ Criação do Gestor Lelé (Fechamento) — 09/09
3. ✅ Rotina Diária Skills v3.0 — mentalidade "brecha válida" (decisão de conteúdo, 10/09)
4. ✅ Skill NBR 8681:2025 — 1ª ativação fluxo v2.9
5. ✅ Exame 2 Cardozo: 6/6 Agentes concluído (Shadow→Assisted)
6. ✅ Skill NBR 10844:1989 — ativação v2.9 (Saturnino)
7. ✅ Skill NBR 6120:2019 — ações para cálculo de estruturas (Baumgart)
8. ✅ Exame 3 Cardozo: 6/6 Agentes Autonomous (marco)
9. ✅ Correção estrutural — Rotina Diária v3.0 não chegava ao fluxo real de execução (achado do próprio Claudemberg, apurado e corrigido nesta mesma sessão — commits `a81ac84`, `cf9b15c`, `757500a`)

**DECIDIDO — 2 itens:**
- ✅ **Saúde de Consumo:** destravar o trim de `_estado_kelsen.md`/`_estado_hely.md` AGORA, sem esperar a leitura de 28/09 — pendência criada (`wallenberg-trim-estado-kelsen-hely-14-09`, crit alta, alc auto) para execução dedicada, mesmo padrão do trim de `_estado_kelsen` de 03/09 (zero perda de HISTÓRICO/Aprendizados).
- ✅ **Próximas Prioridades:** sequência Oscar → Cardozo (Trilha B) → Lelé → Portinari aprovada sem ajustes.

**Status:** ✅ COMPLETO. Pauta 2026-09-14_pauta.md atualizada item a item com "Decisão: ✅ RATIFICADO/APROVADO — 14/09/2026" em cada seção. PDF regenerado.

**Data Ratificação:** 14/09/2026  
**Ratificador:** Claudemberg (Presidente)  
**Registrador:** Wallenberg

---

### [2026-09-14, ~13:30] Correção — Rótulo de versão da Rotina Diária Skills (v2.7/v2.8 → v3.0) + dúvida real sobre execução

**Contexto:** Claudemberg apontou que os commits de 11/09 e 14/09 diziam "Rotina Diária Skills v2.8", quando a v3.0 (Escopo Expandido por Gestor) foi decidida e mesclada no arquivo-fonte em 10/09.

**Achado:** `wallenberg-rotina-diaria-skills-v2_SKILL.md` tinha 3 rótulos de versão contraditórios — frontmatter `version: 3.0.0` (correto), título H1 "v2.7" (desatualizado), banner de status "🔴 v2.8 ATIVA DESDE 08/09" (desatualizado). O conteúdo do Passo 1 (escopo v3.0 por Gestor) estava de fato mesclado corretamente — o problema era só o rótulo visível no topo do arquivo, que é o que se copia para o título do commit.

**Corrigido (execução, dentro do escopo):**
- Título H1: v2.7 → v3.0
- Banner de status: "v2.8 ATIVA DESDE 08/09" → "v3.0 ATIVA DESDE 10/09 (Escopo Expandido por Gestor)"

**Investigação mais a fundo (mesma sessão, a pedido de Claudemberg) — causa raiz real encontrada, não era só rótulo:**

A rotina Seg-Qui instrui explicitamente a **não ler** a seção "Passo 1" do SKILL.md ("ABRA O CHECKLIST, NÃO LEIA ABAIXO") e seguir só `Checklist_Diaria.html`. Conferido o Checklist: seu Passo 1 continuava com a descrição **genérica anterior à v3.0** ("Trilha A: normas, técnicas, regras — qualquer fonte"), sem nenhuma menção a "brecha válida", sem o escopo por Gestor (OODC/Mais-Valerá/janelas de governo para Kelsen; partido/solar/conforto para Lúcio; técnica por disciplina + Vitruvius para Cardozo) que a v3.0 exige desde 10/09. **A v3.0 nunca chegou ao arquivo que a rotina de fato segue** — só ao arquivo de referência que a própria rotina instrui a não ler. Isso explica com muito mais força a lacuna do que só o rótulo do commit.

**Corrigido (execução, dentro do escopo):**
1. `Checklist_Diaria.html`, Passo 1: reescrito com a mentalidade "brecha válida" + resumo de 1-2 linhas por Gestor (Kelsen/Lúcio/Cardozo) + pointer explícito para reler a seção "Passo 1" do SKILL.md a cada rodada (exemplos completos não cabem no Checklist). Tempo do passo ajustado 15-20min → 20-30min; tempo total do checklist 60-75min → 60-90min (bate com o SKILL.md).
2. `wallenberg-rotina-diaria-skills-v2_SKILL.md`: removidos os rótulos "v2.7" residuais do título, COMECE AQUI, OBJETIVO e SUAS INSTRUÇÕES; adicionada exceção explícita na trava "não leia abaixo" — Passo 1 é releitura obrigatória a cada rodada.
3. `COMECE_AQUI.md`: título v2.7→v3.0; removida referência a `wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md` (achado colateral: esse arquivo está **vazio**, 0 bytes — apontava lá como "referência completa, 30 min leitura"; quem seguisse teria aberto um arquivo em branco). `RESUMO_EXECUTIVO_ROTINA_REDEFINIDA.md` e `INDICE_ROTINA_REDEFINIDA_28_08_2026.md` não foram conferidos — mesmo risco em aberto.

**A partir de amanhã (15/09, terça, Seg-Qui):** a rotina deve rodar com o escopo v3.0 de fato visível no fluxo que ela segue.

**NÃO decidido sozinho — dúvida real que permanece, agora só sobre o passado:** não dá para confirmar nem descartar se a busca profunda foi de algum modo feita "de memória" nas rodadas de 11/09 e 14/09 (ex.: se Wallenberg leu o SKILL.md por hábito mesmo com a trava). O commit de 14/09 ("Kelsen e Lúcio: sem material novo viável hoje") é compatível com as duas hipóteses.

**Correção adicional (mesma sessão) — a causa raiz de verdade era mais profunda que o Checklist:**

Claudemberg apontou que a tarefa "Rotina Diária de Skills v2.8" continuava com esse nome na barra lateral do desktop, mesmo após a correção acima. Investigando: a tarefa agendada `wallenberg-rotina-diaria-skills-v2-7` (a que dispara de verdade, seg-sex 08:16) tem **seu próprio arquivo de prompt**, separado do projeto: `C:\Users\santo\.claude\scheduled-tasks\wallenberg-rotina-diaria-skills-v2-7\SKILL.md`. Esse arquivo tinha **seu próprio Passo 1 hardcoded**, escrito antes de 10/09 e nunca atualizado — chamava o SKILL.md do projeto de "fonte de verdade" mas não herdava dele nada automaticamente. **Esse era o verdadeiro motivo da lacuna em 11/09 e 14/09**, mais direto ainda que o Checklist: é o prompt que a IA recebe de fato ao disparar.

**Corrigido via `mcp__scheduled-tasks__update_scheduled_task`:**
- `title`: "Rotina Diária de Skills v2.8" → "v3.0" (aparece agora corrigido na barra lateral)
- `description`: atualizada para citar o escopo expandido
- `prompt`: Passo 1 reescrito com a mentalidade "brecha válida" + resumo por Gestor + instrução de reler a seção "Passo 1" do SKILL.md do projeto a cada rodada. Lista de arquivos de referência corrigida (removida a citação do arquivo vazio como se fosse consultável).

**Também corrigidos (a pedido de Claudemberg, mesma varredura):** `RESUMO_EXECUTIVO_ROTINA_REDEFINIDA.md` e `INDICE_ROTINA_REDEFINIDA_28_08_2026.md` — ambos tinham rótulo v2.7 e múltiplas referências ao arquivo vazio como "manual completo"/"referência". Todas substituídas por `wallenberg-rotina-diaria-skills-v2_SKILL.md` (o arquivo real).

**Não tocados (deliberado):** `RESUMO_IMPLANTACAO_FINAL_28_08_2026.md`, `ENTREGA_FINAL_REDEFINICAO_28_08_2026.md`, `CHECKLIST_PRE_LANCAMENTO_28_08_2026.md`, `ROTINA_REDEFINIDA_COM_AGENDADOR.md` — são registros de lançamento de 28/08, nenhum arquivo do fluxo ativo aponta para eles hoje; tratados como histórico, não como documentação viva. Se algum dia forem reabertos como referência ativa, precisam da mesma varredura.

**Exclusão final (a pedido de Claudemberg, mesma sessão):** os 5 arquivos confirmados obsoletos foram removidos do disco via `git rm` (não commitado — fica para o commit que Claudemberg autorizar):
- `wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md` (vazio, 0 bytes)
- `RESUMO_IMPLANTACAO_FINAL_28_08_2026.md` (relatório de lançamento, puramente histórico)
- `ENTREGA_FINAL_REDEFINICAO_28_08_2026.md` (relatório de aprovação, puramente histórico)
- `CHECKLIST_PRE_LANCAMENTO_28_08_2026.md` (checklist de assinatura, nunca preenchido, puramente histórico)
- `ROTINA_REDEFINIDA_COM_AGENDADOR.md` (explicação de automação, conteúdo já coberto pelo SKILL.md + tarefas agendadas reais)

Conferido antes de apagar: nenhum arquivo do fluxo ativo dependia deles — só o próprio `INDICE_ROTINA_REDEFINIDA_28_08_2026.md` os citava na própria lista de navegação. Índice limpo das referências mortas (tabela "Validação & Lançamento" removida, "Cronograma de Lançamento" virou "Histórico de Versões da Rotina"). Link morto residual no cabeçalho do SKILL.md ("COMECE AQUI") também corrigido. Prompt da tarefa agendada atualizado de novo — a observação antiga citava o arquivo já excluído e tratava RESUMO_EXECUTIVO/INDICE como desatualizados quando já tinham sido corrigidos.

**Como desfazer:** os 5 arquivos excluídos são recuperáveis via `git restore` (estão staged para remoção, não commitados) ou `git log` se já commitados depois; reverter os demais arquivos de projeto via git revert desta entrada; para a tarefa agendada, usar `update_scheduled_task` com o prompt/título anteriores (texto original preservado no histórico desta conversa).

**Aguardando:** ☐ RATIFICADO (correção estrutural completa + exclusão de 5 arquivos obsoletos) — item novo, entra na próxima pauta.

---

### [2026-09-14, ~14:30] Varredura nas demais tarefas agendadas — mesma falha achada na Drenagem Contínua

**Contexto:** Claudemberg pediu para conferir se as outras tarefas agendadas tinham o mesmo problema (arquivo-fonte do projeto divergente do prompt que roda de verdade). Conferidas as 3 tarefas vivas restantes: `wallenberg-reuniao-semanal`, `wallenberg-drenagem-continua-local`, `wallenberg-cronjob-pdf-2000`.

**wallenberg-reuniao-semanal:** sem risco — não tem arquivo-fonte de projeto separado, lê direto Livro-Razão/Registros Diários/scripts de token (dados dinâmicos, não documentação estática). OK.

**wallenberg-drenagem-continua-local:** achado real, na **direção oposta** da Diária — a tarefa agendada (o que roda de verdade) estava mais atualizada que `01_CEO/wallenberg-drenagem-continua-v2_SKILL.md` (citado pela própria tarefa como "arquivo-fonte completo"). 2 decisões reais de Claudemberg nunca chegaram ao arquivo do projeto:
1. **Portão de Trabalho Opção B/Alvo A (02/09):** Skill já avaliada não conta na fila; só abre Gestor com item real na fila — arquivo do projeto ainda tinha a versão simples ("fila não vazia → abre todos os Gestores").
2. **Learning Agent restrito a segunda + execução real (Item 4, 08/09)** + **Passo 7.5 inteiro (varredura mensal de Drive, Item 4, 08/09)** — nenhum dos dois estava no arquivo do projeto.

**Corrigido:** adendo J.4 acrescentado a `wallenberg-drenagem-continua-v2_SKILL.md` (seções B/C mantidas intactas, como já era o protocolo do arquivo — adendos vão em J, não reescrevem a cópia original de 28/08), Histórico de Versões e rodapé atualizados com aviso de que a tarefa agendada é quem executa de fato.

**wallenberg-cronjob-pdf-2000:** só rótulo cosmético desatualizado ("Rotina Diária Skills v2.7" na primeira linha do prompt) — sem impacto funcional (o CronJob gera PDF de qualquer .md sem PDF gêmeo, independe de versão). Corrigido mesmo assim, por consistência.

**Como desfazer:** reverter o adendo J.4 via git revert; reverter o prompt do CronJob via `update_scheduled_task` com o texto anterior.

**Aguardando:** ☐ RATIFICADO — item novo, entra na próxima pauta junto com a correção da Rotina Diária.

---

### [2026-09-14, 10:30] Reunião Semanal com Claudemberg — CONSOLIDAÇÃO QUINZENAL (2ª quinzenal)

**Contexto:** Rotina automática semanal disparada 14/09, segunda-feira. Modo quinzenal em teste (08/09–08/10). 2ª quinzenal — a de 11/09 foi criada mas Claudemberg estava ausente; todos os itens foram carregados para esta.

**EXECUTADO — Pauta consolidada:**

1. **Livro-razão lido:** 11-14/09 completo (incluindo Exame 3 Cardozo 6/6 em 12/09)
2. **Medição de tokens:** scripts `medir_tokens.py` + `custo_por_agente.py` rodaram com sucesso
   - 151 sessões lidas; período 16/07 → 14/09
   - Cache hit: 90,69% — estável
   - Contexto inicial: +15% aumento sobre baseline (S30-S31: 67.072 → S36-S37: 77.109)
   - S37: 25 sessões, 79.714 mediana, 88,31% hit (ligeiro piora vs. S36's 91,74%)
   - Top agentes: Kelsen 31,1%, Hely 22,1%, Cardozo 18,6%
3. **Pauta formal consolidada:** 2026-09-14_pauta.md criada
   - 8 ratificações (6 carry-forward de 11/09 + NBR 6120:2019 + Exame 3 Autonomous)
   - 2 decisões (saúde de consumo + prioridades)
4. **PDF gerado:** `04_REUNIOES_SEMANAIS/2026-09-14_pauta.pdf` via `_ferramentas/md_to_pdf.py`

**Status:** ✅ COMPLETO. Pauta aguarda apresentação e ratificação de Claudemberg.

**Remedição ao vivo (mesma sessão, horas depois — números finais na pauta):**
- 154 sessões (vs. 151 na leitura das 10:30), cache 90,6%, contexto 67.072→81.082 (**+20,9%**, não +15%)
- 3ª leitura consecutiva em alta (07/09: +12,8% → 11/09: +14,3% → 14/09: +20,9%) — ponto de antagonismo adicionado à pauta: o represamento do trim Kelsen/Hely pode não ser mais só prudência
- Custo-eq: 299 invocações, 228,9M tokens-eq, ~USD 657,46. Top 3 inalterado: Kelsen 31,0%, Hely 22,0%, Cardozo 18,8%
- Pauta (Item 1, Parte 2) e PDF regenerados com os números finais

**Itens Aguardando Ratificação (carry-forward de 11/09 + novos):**
1. Painel do Fundador atualização 11/09
2. Gestor Lelé (Fechamento) criado 09/09
3. Rotina Diária Skills v3.0 — mentalidade brecha válida (10/09)
4. Skill NBR 8681:2025 ativa-com-ressalva (09/09)
5. Exame 2 Cardozo 6/6 Shadow→Assisted completo (08-09/09)
6. Skill NBR 10844:1989 ativa-com-ressalva (10/09)
7. **[NOVO]** Skill NBR 6120:2019 ativa-com-ressalva — Cardozo PROCEDE COM RESSALVA (11/09)
8. **[NOVO — MARCO]** Exame 3 Cardozo 6/6 Agentes Autonomous (12/09)

**Como desfazer:** remover entrada do Livro-Razão; PDF já gerado permanece.

---

### [2026-09-14, ~11:00] Drenagem Contínua v2.3 — Rodada 9ª (segunda, 10:15-11:00)

**Portão de Trabalho:** 1 Skill nova (NBR 17076:2024, Saturnino/Cardozo) → Fila não vazia.

**Execução Real:**
- **Cardozo** (Autonomous): Avaliou Skill NBR 17076:2024 — **PROCEDE COM RESSALVA**
  - Sequência obrigatória fossa → filtro anaeróbio → sumidouro verificada; mudança crítica vs. normas anteriores (NBR 7229+13969)
  - 1 ressalva adicionada (Seção 11): câmaras múltiplas — parâmetro "1.000 L/câmara adicional" não confirmável sem texto integral ABNT
  - Cross-disciplinas mapeadas: Glaziou (drenagem próxima ao sistema), Baumgart (carga sobre cobertura das unidades)
  - Status: "avaliada — aguarda ratificação de Claudemberg"

**Correção aplicada (em paralelo):**
- NBR 6120:2019: status "proposta" → "avaliada — aguarda ratificação de Claudemberg" (avaliação foi 11/09, arquivo-fonte não havia sido atualizado)
- Footer de avaliação adicionado ao arquivo NBR 6120 (Cardozo 11/09, PROCEDE COM RESSALVA)
- `indice.md`: 2 linhas atualizadas (NBR 6120 linha 08/09 + NBR 17076 linha 14/09)

**Gestores sem fila (reconciliação pura, não acionados):**
- Kelsen: 0 itens auto+aberta, 0 Notion pendente
- Lúcio: 0 itens auto+aberta, 0 Notion pendente
- Lelé: nível Formação — não acionado

**Learning Agent (8a — segunda + execução real):**
3 achados novos vs. implementação STTK atual:
1. **Handoff Protocol Format** — frameworks 2025-2026 (Anthropic KAIROS, memorywire) estabelecem wire-format padronizado de entrega de contexto inter-agente como primitiva, além de coleta ativa. Potencial adição ao SKILL.md (seção "Padrões de Agente Autonomous-tier").
2. **Observe-Plan-Act-Reflect loop** (Reflexion, Self-Refine) — auto-avaliação iterativa embutida dentro do loop de cada agente Autonomous: gera → avalia → corrige, sem depender do orquestrador. STTK tem gate de aprovação no nível do sistema mas não documenta auto-reflexão interna do agente como padrão operacional.
3. **Memória hierárquica persistente** (HMARS/Mem0 ECAI 2025) — extração hierárquica com +29,6 pts em temporal queries. Roadmap de médio prazo para Trilha A Inteligência.
Recomendação: pontos 1 e 2 para SKILL.md da rotina; ponto 3 é roadmap.

**Painel (8c):** Não republicado — Skills aguardam ratificação (sem capacidade real ativada hoje).

**Duração:** ~45 min. **Próximas ações:** Claudemberg ratificar NBR 17076:2024 e NBR 6120:2019.

---

### [2026-09-11, 10:30-11:15] Reunião Semanal com Claudemberg — CONSOLIDAÇÃO QUINZENAL

**Contexto:** Rotina automática semanal disparada 11/09, quinta-feira. Modo quinzenal em teste (08/09–08/10).

**EXECUTADO — Pauta consolidada:**

1. **Livro-razão lido:** 09-11/09 completo (25 decisões autônomas, nenhuma bloqueada)
2. **Medição de tokens:** scripts `medir_tokens.py` + `custo_por_agente.py` rodaram com sucesso
   - 146 sessões lidas (16 novas de 09-11/09)
   - Cache hit: 90,6% — Item 7 STTK encerrado
   - Contexto inicial: +14,3% aumento (não redução esperada de 45-67%)
   - S37: 21 sessões, 78.9k mediana, 86,2% hit (pior que S36)
3. **Pauta formal:** 2026-09-11_pauta.md criada (6 ratificações + 2 decisões)
4. **Protocolos permanentes:** Adicionados à pauta
   - Protocolo 1 (Epistemologia — clareza sobre incerteza)
   - Protocolo 2 (Antagonismo Construtivo — teste antes de validar)
   - Ambos em vigor a partir de 11/09, permanentes

**Status:** ✅ COMPLETO. Pauta aguarda apresentação e ratificação de Claudemberg.

**PDF:** Gerado via `md_to_pdf.py` (2026-09-11_pauta.pdf)

**Como desfazer:** remover entrada de protocolos de pauta; reverter edições em Setembro.md.

---

### [2026-09-11] Painel do Fundador atualizado — 11/09/2026 (quinta, Rotina Semanal)

**O que foi atualizado no Painel:**
- Data: 04/09 → 11/09/2026
- 9 novos eventos no feed (07/09–10/09): Rotina v3.0, NBR 10844 (1ª ativação v2.9), Exame 2 Cardozo 6/6 COMPLETO, Gestor Fechamento (Lelé) criado, NBR 8681 (1ª validação v2.9), Reunião Semanal 09/09, NBR 6120, Exame 2 Baumgart, Reunião Semanal 07/09
- KPIs: 13→15 membros (4 Autonomous, 9 Assisted, 0 Shadow, 1 Formação + Artigas), 6/9→7/9 marcos, 7/0→4/0 Skills esta semana
- SVG milestone: 7º círculo (Gestor Fechamento) preenchido, linha de marca estendida
- Gráfico de níveis redesenhado para nova distribuição
- Represamento: +7 dias em B14/MCP/Oscar/Daniel-OB
- Cards comp, exames e lucio atualizados
- OV-SNAPSHOT atualizado para 11/09

**Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-11/painel_fundador_sttk.html`  
**Publicado em:** `https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`

---

### [2026-09-11] Análise Semanal (07-11 de Setembro) — Passo 10 Rotina Diária

**ROI da Semana — Números:**
- ✅ Marcos alcançados: 6/9 → **7/9** (+1 marco: Lelé, Gestor Fechamento, criado 09/09)
- ✅ Membros organismo: 13 → **15** (+2: Lelé + indeterminado; 4 Autonomous, 9 Assisted, 1 Formação)
- ✅ Exame 2 Cardozo: **6/6 COMPLETO** (maior conquista — 6 agentes Shadow → Assisted)
- ✅ Ativação fluxo v2.9: **1ª vez ao vivo** (NBR 8681, validação de Gestor no próprio dia)
- ✅ Skills trilha A: 4 novas (NBR 6120, 8681, 10844, BIMwright 229★)
- ✅ Rotina v3.0: **mentalidade de brecha válida ativada** (Passo 1 escopo expandido)

**Bloqueios Reais (não aspiracionais):**
- 🔴 **Caso Real Vitruvius (Oscar):** Represamento de +7 dias (B14, MCP, Oscar, Daniel-OB) — compatibilização travada na fase de levantamento de Interiores/Complementares
- 🔴 **Burle (render/vídeo):** Ainda sem MCP de geração de imagem/vídeo 100% verificada — busca contínua em andamento
- 🔴 **Skills Trilha B Cardozo:** Não iniciadas; 6 agentes aguardam inteligência técnica por disciplina + ferramentas GitHub para suas áreas

**Próximas Prioridades (ordem):**
1. **Vitruvius 1º caso real:** Oscar desenha projeto em Revit via Vitruvius — caso Daniel-OB como protótipo
2. **Compatibilização contínua (Lelé):** Implementar fluxo Revit → Navisworks → Clash Detective (achado de Learning Agent)
3. **Skills Trilha B Cardozo:** Pesquisa + documentação de técnicas/ferramentas por disciplina (Estrutural/Landell, Hidrossanitário/Saturnino, Paisagismo/Glaziou, Interiores/Tenreiro, Apresentação/Mindlin)
4. **Primeira entrega cliente:** Portinari compila material técnico de Oscar + Burle (quando MCP pronto) para apresentação

**Learning Agent (Passo 7):** Achado — **NBR ISO 19650 compatibilização contínua em Revit/Navisworks** reduz rework na fase de Fechamento; integrado ao conhecimento de Lelé.

---

### [2026-09-11] Drenagem Contínua v2.3 — Rodada 8ª (quinta, 10:15-10:35)

**Portão de Trabalho:** 1 Skill nova (NBR 6120:2019, Baumgart/Cardozo) → Fila não vazia.

**Execução Real:**
- **Cardozo** (Autonomous): Avaliou Skill NBR 6120:2019 — **PROCEDE COM RESSALVA**
  - Técnica sólida, lacunas bem declaradas (norma paga não lida, valores secundários), aviso explícito de consulta primária em dimensionamento real
  - Cross-disciplinas mapeadas: Saturnino, Tenreiro, Glaziou, Landell
  - Padrão idêntico ao de NBR 6122 e NBR 8681 já aceitas
  - Status: Pronta para ratificação de Claudemberg (tipo Inteligência, não Ferramenta)

**Gestores sem fila (reconciliação pura, não acionados):**
- Kelsen: 0 itens auto+aberta, 0 Notion pendente
- Lúcio: 0 itens auto+aberta, 0 Notion pendente

**Learning Agent (8a):** Não rodou (apenas segunda-feira, regra Opção B)

**Painel (8c):** Não republicado (Skill aguarda ratificação — sem capacidade real ativada ainda)

**Duração:** ~20 min. **Próximas ações:** Claudemberg ratificar NBR 6120:2019.

---

### [2026-09-10] Rotina Diária Skills v3.0 — Escopo Expandido por Gestor (instrução Claudemberg)

**Contexto:** Instrução direta de Claudemberg ao fim da rodada de 10/09. Duas diretrizes: (1) a pesquisa do Passo 1 estava estreita demais — só NBRs/MCPs — quando cada Gestor precisa de inteligência de domínio completa (estratégias, técnicas, saber-fazer real). (2) Agentes de Cardozo também precisarão usar o Vitruvius, então precisam de Skills de Trilha B para ele.

**O que foi decidido:**
- Upgrade da Rotina Diária Skills de **v2.9 → v3.0**.
- Passo 1 expandido com escopo detalhado por Gestor:
  - **Kelsen:** estratégias legais reais (OODC, Mais-Valerá, Mais-Valia, TPC, AEIU) + monitoramento de janelas excepcionais de governo. A intuição de Claudemberg foi verificada: novos planos diretores e LCs no Rio historicamente abrem exceções ao CAM — LC 270/2024 foi "o maior incentivo a puxadinhos da história da cidade". Mais-Valia vigente até jun/2026. Kelsen deve monitorar continuamente novas LCs e projetos de lei em tramitação.
  - **Lúcio:** estratégias de partido arquitetônico, orientação solar/vento RJ, conforto térmico/lumínico passivo, tipologias residenciais, acessibilidade integrada, cases de escritórios RJ.
  - **Cardozo:** técnicas de projeto profundas por disciplina — 6 Agentes com escopo detalhado (solo RJ/Baumgart, automação real/Landell, CEDAE-solar-fossas/Saturnino, espécies INEA/Glaziou, acabamentos-iluminação/Tenreiro, prancha técnica/Mindlin).
  - **Vitruvius para Cardozo:** mapear quais tools Vitruvius cada disciplina usa (Trilha B, Passo 8).
- Validação da estratégia de CAM + Mais-Valerá pesquisada e documentada para uso futuro de Kelsen.

**O que foi alterado:**
- `01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md` — atualizado para v3.0 (frontmatter, Passo 1 expandido, histórico)
- `01_CEO/Decisoes_Autonomas/_backups/2026-09-10/wallenberg-rotina-diaria-skills-v2_SKILL.md` — backup criado antes de editar

**Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-10/`

**Como desfazer:** restaurar `wallenberg-rotina-diaria-skills-v2_SKILL.md` do backup em `_backups/2026-09-10/` (reverte para v2.9).

---

### [2026-09-10] Rotina Diária Skills v2.9 — 1 Skill NBR 10844 (Saturnino, ativa-com-ressalva)

**Contexto:** Rotina automática de quinta-feira. Passos 1–5+8 (Seg-Qui). 1 Skill criada, validada e ativada seguindo fluxo v2.9 (Cardozo valida no mesmo dia → ativa em produção → Claudemberg ratifica na Semanal).

**O que foi decidido:**
- Criação e ativação da Skill **NBR 10844:1989 — Instalações Prediais de Águas Pluviais** (Trilha A, Saturnino principal, Glaziou + Baumgart cross).
- Status `ativa-com-ressalva`: texto integral ABNT não lido (norma paga), valores de intensidade pluviométrica para RJ não obtidos — Saturnino obrigado a consultar equações IDF Rio-Águas antes de qualquer cálculo real.
- Cardozo validou: PROCEDE (sem erro factual, sem duplicata, lacunas marcadas).

**Por quê:**
- Prioridade #9 do índice de setembro (NBR 10844:1989 — Saturnino sem Skill de águas pluviais).
- Material técnico viável encontrado em duas fontes secundárias de qualidade (GreenGold Engenharia, julho/2026).
- Nenhuma Skill nova encontrada para Kelsen (sem deliberação CAU-RJ nova em setembro) nem Lúcio (Revit-MCP todos já conhecidos, busca de apresentação interativa pausada).

**O que foi alterado:**
- `01_CEO/Skills_Propostas/2026/Setembro/saturnino_nbr10844-1989-aguas-pluviais-drenagem-predial.md` — criado (v1.0, ativa-com-ressalva)
- `.claude/skills/nbr10844-1989-aguas-pluviais/SKILL.md` — instalado
- `01_CEO/Skills_Propostas/2026/Setembro/indice.md` — atualizado (+1 Skill, estatísticas, próxima prioridade)
- `01_CEO/Decisoes_Autonomas/_backups/2026-09-10/indice.md` — backup criado antes de editar

**Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-10/`

**Como desfazer:** apagar `saturnino_nbr10844-1989-aguas-pluviais-drenagem-predial.md`, apagar `.claude/skills/nbr10844-1989-aguas-pluviais/`, restaurar `indice.md` do backup.

**Próxima prioridade Cardozo/Saturnino:** Passo 8 se lacuna real de Agente pedir ferramenta; caso contrário, explorar NBR 7229:1993 (fossas sépticas) ou NBR 10521:1988 (poços absorventes) — complementam o sistema hidrossanitário de terrenos sem rede de esgoto (situação comum em RJ afastado do centro).

---

### [2026-09-09, noite] Criação do Gestor Fechamento — Lelé (4º Gestor)

**Contexto:** Item 1 das melhorias do organismo (identificado 08/09/2026). Criação do 4º e último Gestor previsto no fluxograma oficial. Autorizado por Claudemberg ao vivo em 09/09/2026.

**Nome:** Lelé — referência a João Filgueiras Lima ("Lelé"), arquiteto e engenheiro que fechava o ciclo completo (projeto → fabricação → obra) como sistema integrado único. Escolhido por Wallenberg, confirmado por Claudemberg.

**Escopo (4 etapas finais do fluxograma, decidido por Claudemberg em 29/07/2026):**
1. Compatibilização de Projetos (recebe output dos 6 Complementares de Cardozo)
2. Projeto Executivo (detalhamento construtivo integrado)
3. Orçamento Executivo e Premissas (quantitativos, cronograma)
4. Liberação de Obra (Gate 16 — convergência com Legal/Kelsen)

**Nível:** Formação (padrão). Ciclo: Formação → Shadow → Assisted → Autonomous.

**Equipe:** a definir pelo próprio Lelé (regra de nomeação em cascata), quando acionado por Wallenberg para montar a composição.

**Arquivos criados:**
- `.claude/agents/lele.md` (definição do agente, ferramentas, contexto completo)
- `01_CEO/Gestores/Lelé (Fechamento)/_estado_lele.md` (estado inicial)

**Como desfazer:** apagar os 2 arquivos acima e a pasta `Lelé (Fechamento)/`.

---

### [2026-09-09, noite] Exame 2 Tenreiro + Mindlin — 6/6 Lote Completo, Todos Aprovados

**Contexto:** Última dupla do cronograma de Exame 2 dos 6 Agentes Cardozo (adiantado de 10/09 para 09/09, conforme autorização de Claudemberg). Cardozo administrou diretamente, sem delegação a sub-agentes (instrução explícita mantida após o antipadrão da rodada Saturnino/Glaziou).

**Verificação de integridade pré-exame:** `_estado_tenreiro.md` e `_estado_mindlin.md` limpos — nenhuma alegação fantasma de "Exame 2 já respondido" (diferente do ocorrido com Saturnino/Glaziou). Problema anterior confirmado como pontual, não sistêmico.

**Resultado:**
- **Tenreiro (Interiores) — 2/2 APROVADO. Promovido Shadow→Assisted.**
  - E1 (piso cimento queimado, terraço+box, Ipanema/RJ): barrou 4 armadilhas reais (juntas de dilatação ausentes; "cimento queimado dispensa impermeabilização" — falso; ausência de caimento; ausência de antiderrapante em área externa molhada). Não caiu em 2 iscas reversas.
  - E2 (acústico NBR 15575:2025, apartamento Botafogo/RJ): barrou 5 armadilhas diretas (omissão do requisito em ambiente sem dormitório — novidade central da norma 2025; piso colado sem manta; rodapé rígido; manta abaixo do mínimo; norma errada citada). Não presumiu valores de dB não confirmados em fonte aberta.
- **Mindlin (Apresentação) — 2/2 APROVADO. Promovido Shadow→Assisted.**
  - E1 (prancha técnica corte+fachada, Tijuca/RJ): barrou 4 armadilhas NBR 6492; recusou categoricamente "encolher fachada sem atualizar escala anotada" (falsificação de informação técnica).
  - E2 (compilação completa 5 disciplinas, Laranjeiras/RJ): barrou armadilhas de representação e fidelidade; achou clash pilar×spot sem apontamento prévio; recusou instrução fora de escopo (orçamento+render 3D) mesmo atribuída ao próprio "Cardozo" no bilhete.

**Lote Exame 2 FECHADO: 6/6 Agentes Cardozo aprovados e promovidos Shadow→Assisted.**
| Agente | Data | E1 | E2 |
|--------|------|----|----|
| Baumgart | 08/09 | aprovado | aprovado |
| Landell | 09/09 | aprovado | aprovado |
| Saturnino | 09/09 | aprovado | aprovado |
| Glaziou | 09/09 | aprovado | aprovado |
| Tenreiro | 09/09 | aprovado | aprovado |
| Mindlin | 09/09 | aprovado | aprovado |

**Consolidação (10/09/2026):** Cardozo confirmou 4 memoriais em disco (Tenreiro E1/E2, Mindlin E1/E2) — estado verificado e correto. `.claude/agents/` atualizados para Assisted. **Lote Exame 2 tecnicamente encerrado com sucesso.**

**Achados colaterais de Cardozo:**
1. Mindlin tem Skill técnica própria já ativa (`nbr6492-representacao-grafica`) — contradiz descrição atual em `.claude/agents/mindlin.md`. Corrigir.
2. Arquivos "fantasma" de Saturnino/Glaziou (rodada anterior) existem agora no disco ao lado dos reais — auditoria recomendada.

**Gap de ferramenta Notion reincidiu 5ª vez** — Wallenberg atualizou manualmente via `notion-update-page` (4 páginas).

**Como desfazer:** reverter `_estado_tenreiro.md`, `_estado_mindlin.md`, `_estado_cardozo.md` aos backups; reclassificar no Notion como `pendente`; readministrar exames.

**Notion atualizado por Wallenberg:**
- Tenreiro E1: `3d592372-eae1-8104-b731-da3c76b89666` / E2: `3d592372-eae1-819a-8644-ebd34fd9b0e6`
- Mindlin E1: `3d592372-eae1-81f3-a458-ffa63299f3c0` / E2: `3d592372-eae1-8164-a9f6-f3c527dd6b52`

---

### [2026-09-09, tarde/noite] Exame 2 Saturnino + Glaziou — 4/6 Agentes Cardozo Aprovado + Achado de Integridade de Estado

**Contexto:** Continuação do cronograma. Primeira tentativa de acionar Cardozo (agente `a2d2eb2dedb340f8e`) delegou o exame a sub-agentes (Agent tool) e encerrou o próprio turno "aguardando notificação" — **antipadrão de tarefa órfã** (violação da Delegation Completion Contract: pai não pode encerrar turno com filhos vivos). Os 2 sub-agentes órfãos (Saturnino, Glaziou) completaram depois e notificaram Wallenberg diretamente (não Cardozo, cujo turno já tinha acabado) — cada um escreveu memoriais técnicos linha a linha, mas sem veredito final de aprovação (isso é atribuição de Cardozo, não do Agente sozinho).

**Correção:** Cardozo relançado (`a1d94c4e207a3aef6`) com instrução explícita de **não sub-delegar** e administrar diretamente, no mesmo turno. Ao investigar antes de montar os casos, **achado crítico:** os estados de Saturnino/Glaziou já tinham sido alterados pela tentativa órfã anterior, alegando "Exame 2 respondido, aguardando veredito de Cardozo" com nomes de caso e caminhos de memorial (ex. "Sobrado Laranjeiras", "Condomínio Barra da Tijuca", "Jardim Botânico") que **nunca foram gravados no disco** — confirmado via Glob (pastas `Casos/` e `Casos_TESTE/` vazias antes desta rodada). Cardozo não reaproveitou nada, refez do zero, e corrigiu os 2 arquivos de estado.

**Resultado (Cardozo, refeito do zero, memoriais reais confirmados):**
- **Saturnino (Hidrossanitário) — 2/2 APROVADO. Promovido Shadow→Assisted.**
  - E1 (água fria, 3 banheiros, Tijuca): barrou 4 armadilhas reais (pressão 450kPa sem VRP; ramal vaso sanitário DN75mm quando regra é DN≥100mm; inclinação esgoto 1% quando DN≤100mm exige 2%; separação água×eletroduto 15cm quando mínimo é 30cm). Não caiu em 2 iscas reversas. Tratou peso de aparelho fora de tabela como pendência, não presunção.
  - E2 (reuso NBR 16783, condomínio 20 unidades): barrou 5 não-conformidades. No ponto mais difícil, recusou presumir dispensa de outorga para captação de água subterrânea — registrou pendência bloqueante a confirmar com Kelsen/INEA em vez de aceitar alegação do parceiro terceirizado.
- **Glaziou (Paisagismo) — 2/2 APROVADO. Promovido Shadow→Assisted.**
  - E1 (drenagem 500m², Jacarepaguá): barrou inclinação de piso abaixo do mínimo, espécie invasora (Spathodea campanulata), rampa sem corrimão, interligação pluvial-esgoto proibida.
  - E2 (jardim de chuva + pergolado sobre laje, Recreio): barrou declive incorreto, espécie invasora tolerante a encharcamento, subdimensionamento (ignorou área de contribuição), reclassificação semântica para escapar do laudo de carga de Baumgart. Rejeitou citação de NBR 16636-4 como "base normativa obrigatória" do jardim de chuva — a própria Skill registra que não existe norma NBR específica para essa técnica.

**Progresso do lote:** 4/6 (Baumgart 08/09, Landell/Saturnino/Glaziou 09/09). Restam Tenreiro e Mindlin (10/09).

**Lição registrada (risco geral, não é achado de Skill):** delegação a sub-agente sem coleta ativa do resultado pode deixar estado alegando trabalho que não existe. Quem ler o estado de um Agente depois deve conferir a existência real do arquivo (Glob), não confiar só no texto do `_estado_*.md`.

**Gap de ferramenta Notion reincidiu 4ª vez consecutiva** — Wallenberg atualizou manualmente via `notion-update-page` (4 páginas: Saturnino E1/E2, Glaziou E1/E2). Recomendação de Cardozo: avaliar concessão de ferramenta de escrita Notion antes da rodada final (Tenreiro+Mindlin).

**Notion atualizado por Wallenberg:**
- Saturnino E1: `3d592372-eae1-81ee-81bd-dafcd6a011ef` / E2: `3d592372-eae1-81f0-a9d7-d4859a97dd24`
- Glaziou E1: `3d592372-eae1-81c8-9010-f76531007e16` / E2: `3d592372-eae1-81ea-9535-f80aecb00a27`

**Como desfazer:** reverter Notion Status para "pendente" nas 4 páginas (limpar Resultado); reverter `_estado_cardozo.md`, `_estado_saturnino.md`, `_estado_glaziou.md` para estado pré-Exame 2; remover esta entrada.

**Próxima ação:** Cardozo administra Tenreiro+Mindlin (10/09, cronograma original) — decidir se antecipar hoje ou aguardar amanhã.

---

### [2026-09-09, tarde] Exame 2 Landell — 2/6 Agentes Cardozo Aprovado

**Contexto:** Claudemberg autorizou (Reunião Semanal 09/09) prosseguir cronograma Exame 2. Cardozo acionado para administrar Landell (Elétrica/Automação), pendente desde 08/09.

**Executado por Cardozo:**
- **Caso E1 (simples, elétrica NBR 5410, 100m²):** APROVADO. Barrou 4 armadilhas reais (circuito único iluminação 7 ambientes; DR dispensado banheiro "quadro em ambiente seco"; chuveiro dividindo TUE com TUG banheiro — calculou IB≈43,3A, disjuntor 20A insuficiente; TN-C reaproveitando PEN em obra nova), citou fonte normativa em cada. Não caiu nas 2 iscas reversas (LSHF, divisão TUG cozinha — ambas corretamente aceitas como conformes). Reteve 2 pendências de dado sem presumir.
- **Caso E2 (complexo, SPDA + COSCIP/Decreto 42/2018, condomínio 9 unidades):** APROVADO. Barrou 4 armadilhas diretas (SPDA via NBR 5410 em vez de NBR 5419; estrutura metálica dispensando análise de risco; aterramento citando revisão 2026 NBR 5410 como já vigente; SPDA e detecção/alarme fundidos num memorial). No ponto mais difícil — isenção A-1 para grupamento 9 unidades — **não decidiu sozinho**: reconheceu que a própria Skill COSCIP se autodeclara não fechada, registrou como pendência a confirmar via Kelsen/Hely. Achou 2 imprecisões reais não plantadas no enunciado (mesmo padrão de Baumgart).
- Auditados os 2 memoriais na íntegra antes de aceitar — confirmados.
- **Landell promovido Shadow → Assisted.** Progresso do lote: 2/6.

**Achados colaterais:**
1. Landell não tem Skill ratificada de NBR 5419 (SPDA) nem NBR 17240 (detecção/alarme) — escopo atual exclui SPDA explicitamente. Recomendação: pesquisar/ratificar antes do primeiro caso real de SPDA.
2. Gap de ferramenta Notion (escrita) reincidiu 2ª vez (Baumgart 08/09, Landell agora) — Wallenberg atualizou manualmente via `notion-update-page`. Vale escalar antes de Saturnino/Glaziou (hoje) e Tenreiro/Mindlin (amanhã) gerarem o mesmo pedido pela 3ª/4ª vez.

**Notion atualizado por Wallenberg** — 2 páginas (Landell E1: `3d592372-eae1-8132-a0e1-ed902bba029f`; E2: `3d592372-eae1-81e2-ba72-f1dd3b703042`). Status `pendente→aprovado`, Resultado preenchido, Atualizado em `09/09/2026`.

**Como desfazer:** reverter Notion Status para "pendente" nas 2 páginas (limpar Resultado); reverter `_estado_cardozo.md` e `_estado_landell.md` para estado pré-Exame 2; remover esta entrada.

**Próxima ação:** Cardozo administra Saturnino+Glaziou (hoje, 09/09, mesmo cronograma); depois Tenreiro+Mindlin (10/09).

---

### [2026-09-09, 13:00] Reunião Semanal com Claudemberg — RATIFICAÇÃO EM BLOCO (09/09)

**Contexto:** Rotina Automática Semanal disparada 09/09 (teste quinzenal, programada 08/09). Wallenberg apresentou 6 ratificações + 1 decisão desde 07/09. Claudemberg ratificou todas.

**RATIFICADO — 6 itens:**
1. ✅ Skill NBR 8681 + fluxo v2.9 ativação (09/09) — implementação confirmada
2. ✅ Exame 2 Baumgart aprovado (1/6 Cardozo) (08/09)
3. ✅ Skill NBR 6120 avaliada, instalar para ativar (08/09)
4. ✅ Skills não instaladas corrigidas (6122+6120 em `.claude/skills/`) (08/09)
5. ✅ Fluxo v2.9 (Skill ativa no dia, Gestor valida, você revisa) (08/09)
6. ✅ Melhorias Organismo Items 4,5,6 (varredura mensal + inventário + Semanal quinzenal) (08/09)

**RATIFICADO — 1 decisão:**
- ✅ NBR 6120: ratificar sem reformulação (complemento mandatório tríade)

**PENDENTE EXECUÇÃO (não feita, Wallenberg vai fazer):**
- NBR 6120 → instalar `.claude/skills/nbr6120-2019-cargas/SKILL.md` (ja criado, pronto)
- Propagação fluxo v2.9 aos 3 espelhos (Checklist, REDEFINIDO, manual operacional)
- Replicação Item 4 no arquivo-fonte wallenberg-drenagem-continua-v2 (só cópia -local editada)

**Items não feitos (planejados, não decididos hoje):**
- Item 1 (Gestor Fechamento) — depende Cardozo fechar Exame 2
- Item 6.2 (Trim _estado_hely/lucio/wallenberg) — passe dedicado pós-Kelsen
- Item 6.5 (Colapso fechamento+diário+razão) — redesenho processo, bloco coeso

**Status:** ✅ COMPLETO. Livro-Razão atualizado. Todas as 6 ratificações + 1 decisão registradas com data 09/09/2026. Wallenberg executa pendências hoje pós-reunião.

**Data Ratificação:** 09/09/2026, 13:00 UTC  
**Ratificador:** Claudemberg (CEO)  
**Registrador:** Wallenberg

---

### [2026-09-09] Diária Skills v2.9 (Quarta) — 1 Skill Trilha A (NBR 8681:2025 Segurança) + 1ª ativação v2.9

**Executado por Wallenberg (rotina Seg-Qui, Passos 0-5+8):**

**Passo 0 (Pré-rodada):** fechamento de 08/09 lido. Estados de Kelsen/Cardozo/Lúcio verificados — Cardozo com Exame 2 em andamento (1/6 Baumgart aprovado), Kelsen e Lúcio estáveis. Próxima prioridade Trilha A confirmada: NBR 8681:2025 (fatores de combinação — complemento direto da 6120, lacuna declarada pela Skill anterior).

**Passo 1 (Pesquisa Externa):** 6 buscas paralelas + aprofundamentos. Eixos: NBR 8681:2025, NBR 10844:1989, CAU-RJ, Revit MCP GitHub, render IA. Achados úteis: NBR 8681 (publicação 29/09/2025 confirmada via ABECE, framework de fatores de fontes secundárias), NBR 10844 (Manning, condutores, períodos de retorno). Bloqueios: masteremmodelagem.com.br 403, UFPR PDF binário ilegível. pyRevit-MCP (pago, descartado), mcp-servers-for-revit (arquivado, descartado).

**Passo 2 (Consolidação):** 1 Skill viável para Cardozo (NBR 8681). NBR 10844 viável mas meta 1/Gestor/dia impede — fica como próxima prioridade (9). Kelsen e Lúcio sem material.

**Passo 3 (Redação + Ativação v2.9):** Skill `baumgart_nbr8681-2025-acao-seguranca-estruturas.md` criada (v1.0). Conteúdo: fatores γf (permanente/variável, normal/especial/excepcional), coeficientes ψ (7 categorias), fórmulas de combinação ELU (3 tipos) e ELS (3 tipos), sequência integrada 6120→8681→6118→6122, cross-disciplina Saturnino/Landell, 6 erros comuns, 4 lacunas declaradas.

**Validação Cardozo (v2.9 — primeira execução do fluxo):** PROCEDE. 1 correção aplicada durante validação: ψ de escritórios era 0,6/0,4/0,3 (categoria inventada, não existe na Tabela 6 clássica) → corrigido para 0,7/0,6/0,4 (faixa "com concentração de pessoas ou equipamentos"). Skill ativada com `status: ativa-com-ressalva` (fonte primária ABNT não lida).

**Passo 4 (Salvamento):** Skill em `01_CEO/Skills_Propostas/2026/Setembro/`. Instalada em `.claude/skills/nbr8681-2025-seguranca-estruturas/SKILL.md`. Índice atualizado (10 Skills acumuladas, Baumgart sobe para 6). Backup do índice em `_backups/2026-09-09/`.

**Passo 5 (PDFs):** Não gerados (v2.9 Item 6.4 — Skill e índice não geram mais PDF gêmeo).

**Passo 8 (Ferramentas/Trilha B):** nenhuma lacuna real de Agente pediu ferramenta nova. pyRevit-MCP (pago) e mcp-servers-for-revit (arquivado) descartados. Vitruvius sem achado novo. Resultado: "nenhum achado novo."

**Retrabalho evitado:** Apresentação interativa não pesquisada (PAUSADA). ComfyUI/Blender/TRELLIS2 não duplicados. Achados Vitruvius existentes não duplicados. NBR 10844 não forçada (1/Gestor/dia).

**Marco:** primeira Skill ativada pelo fluxo v2.9 (validação por Gestor dono no mesmo dia, sem esperar Semanal). Precedente operacional confirmado.

**Como desfazer:** remover `baumgart_nbr8681-2025-acao-seguranca-estruturas.md` e `.claude/skills/nbr8681-2025-seguranca-estruturas/`; reverter edições no índice (via backup `_backups/2026-09-09/indice_setembro_pre-nbr8681.md`); remover esta entrada do livro-razão.

---

### [2026-09-09, 10:15-10:45] Drenagem Contínua v2.3 — 6ª Rodada (ter)

**Contexto:** Execução automática de `wallenberg-drenagem-continua-local` — Portão de Trabalho ativado (Passo 2.5).

**Fila verificada:**
- `pendencias.json`: 0 itens `alc:"auto"`+`status:"aberta"` (grep confirmado)
- Skills propostas: 1 Skill nova (`nbr6120-2019-acoes-cargas`, criada 08/09, Status "proposta")
- Notion "Treinos e Testes": (não consultado — Portão ativado por Skills propostas; Gestor sem fila automática)

**Execução:**

1. ✅ **Cardozo acionado** (único Gestor com fila)
   - Avaliou Skill NBR 6120:2019 — **PROCEDE** ✓
   - Técnica: tríade estrutural 6120→8681→6118→6122 confirmada; conteúdo coerente
   - Cross-disciplina: Saturnino/Tenreiro/Glaziou/Landell mapeados corretamente
   - Coerência com NBR 8681 (avaliada hoje v2.9): confirmada — 8681 completa a lacuna deixada por 6120 ("fatores de combinação")
   - Lacunas: explícitas e aceitáveis (fontes secundárias, padrão confirmado)
   - Status: "avaliada — pronta para ratificação de Claudemberg"
   - Nenhuma pendência aberta ou bloqueio identificado

2. ✅ **Exame 2 (Shadow→Assisted) reconciliado**
   - Baumgart: concluído 08/09 (2/2 aprovado, promovido)
   - Landell, Saturnino, Glaziou, Tenreiro, Mindlin: confirmados em Status "pendente" do Notion
   - Cronograma: Saturnino+Glaziou hoje (09/09), Tenreiro+Mindlin amanhã (10/09)
   - Não administrados nesta rodada (grande demais para Drenagem; executados em sessão separada)

3. ❌ **Learning Agent (Passo 8a)**
   - Segunda-feira: NÃO (hoje é terça)
   - Regra: executa só segunda + se houve execução real
   - Não rodado

4. ✅ **Livro-razão (Passo 8b)**
   - Executado (esta entrada)
   - Nenhum item `auto` fechado (execução foi só avaliação de Skill, não fechamento)
   - Status registrado para próxima rodada

5. ❌ **Painel (Passo 8c)**
   - Nenhuma mudança de capacidade real (Skill ainda aguarda ratificação de Claudemberg)
   - Não republicado

**Duração:** ~30 min (incluindo espera de Cardozo)

**Próxima ação:** Claudemberg ratificar NBR 6120:2019 (quando tempo permitir); Cardozo continua Exame 2 dos 5 Agentes restantes (fora desta rotina).

**Como desfazer:** remover esta entrada do livro-razão; reverter qualquer edição em `_estado_cardozo.md` se houver (nenhuma executada, só leitura).

---

### [2026-09-08, continuação pós-Drenagem] Exame 2 — Baumgart aprovado (1/6) + correção de Skills não instaladas

**Contexto:** Após a 5ª rodada da Drenagem Contínua (ver entrada abaixo), Claudemberg apontou (ao vivo) que a verificação do Notion "Treinos e Testes" tinha sido feita incorretamente (assumida de rodada anterior, não consultada de fato). Consulta real revelou 12 casos-teste do Exame 2 dos 6 Agentes de Cardozo, recém-inseridos por Claudemberg (ver entrada seguinte, mesma data). Claudemberg autorizou: (1) atualizar `pendencias.json` refletindo o achado; (2) acionar Cardozo para iniciar a administração do primeiro par (Baumgart, previsto 08/09).

**O que foi feito:**

1. **`pendencias.json` atualizado** — item `cardozo-exame2-6-agentes-nao-administrado` de `status:"aberta"` para `status:"em_andamento"`, registrando os 12 casos-teste e o cronograma (08/09 Baumgart+Landell, 09/09 Saturnino+Glaziou, 10/09 Tenreiro+Mindlin).

2. **Cardozo acionado** — administrou o Exame 2 de Baumgart (2 casos: E1 sapata rasa isolada/Botafogo, E2 hélice contínua/Ipanema esquina). Releu as 3 Skills técnicas de Baumgart antes de montar as armadilhas (baseadas em norma real). **Resultado: 2/2 APROVADO.** Baumgart identificou todas as armadilhas plantadas (10 no total entre os 2 casos, incluindo 1 isca reversa no E2 — cimento 400kg/m³ conforme, não erro), citou fonte normativa em cada afirmação, e ainda encontrou problemas adicionais não plantados (comparação ELU vs. tensão admissível inválida; recalque diferencial ELS não verificado; exigência de ATP/CC3, vistoria cautelar de vizinhos e monitoramento geotécnico no caso da hélice contínua). Auditados os arquivos que Baumgart alegou ter gravado — confirmados. **Baumgart promovido Shadow→Assisted** (critério: individual por Agente, não em lote — cada Agente é promovido ao concluir seus próprios 2 casos, independente do cronograma dos demais). Progresso do lote: 1/6.

3. **Notion atualizado por Wallenberg** — Cardozo não tem ferramenta de escrita no Notion (só leitura: `notion-fetch`, `notion-query-data-sources`). As 2 páginas (Baumgart E1/E2) foram atualizadas manualmente: `Status: pendente → aprovado`, `Resultado` preenchido com o relato completo, `Atualizado em: 08/09/2026`.

4. **Achado colateral corrigido — Skills não instaladas:** Baumgart sinalizou (durante o Exame) que NBR 6122:2019 (ratificada 07/09) e NBR 6120:2019 (avaliada/PROCEDE 08/09, mesma rodada) nunca tinham sido instaladas em `.claude/skills/` — só existiam como arquivo em `Skills_Propostas/`. Confirmado por Glob: 24 Skills instaladas, nenhuma das 2 novas. Mesmo padrão de erro já registrado na memória `feedback_ativado_so_se_instalado_de_verdade` (03/09/2026). **Corrigido:** criadas `.claude/skills/nbr6122-2019-fundacoes/SKILL.md` e `.claude/skills/nbr6120-2019-cargas/SKILL.md`, frontmatter padrão (name+description com gatilhos de uso), conteúdo condensado do arquivo-fonte. NBR 6122 (já ratificada) está oficialmente ativa agora. **NBR 6120 está tecnicamente instalada mas ainda aguarda ratificação formal de Claudemberg antes de uso em caso real de cliente** — uso em Exame sintético (como o de hoje) segue o mesmo padrão já aceito em exames anteriores.

**Por quê:** Sem a correção de instalação, Baumgart (e qualquer Agente futuro) estaria usando conteúdo técnico por acesso direto a arquivo solto, não pelo mecanismo oficial de Skill — mesmo risco de "ativado sem instalado de verdade" já visto antes.

**Como desfazer:** reverter os 2 arquivos `.claude/skills/nbr6122-2019-fundacoes/` e `.claude/skills/nbr6120-2019-cargas/` (git); reverter `pendencias.json` para o estado anterior a esta entrada; nas 2 páginas do Notion, reverter `Status` para "pendente" e limpar `Resultado`/`Atualizado em`.

**Próxima ação:** Cardozo administra Landell (previsto 08/09, mesma data, mas fora desta rodada — cronograma de 1-2 Agentes/dia para não virar produção rasa); depois Saturnino+Glaziou (09/09); Tenreiro+Mindlin (10/09).

---

### [2026-09-08, ao vivo] Correção — Exame 2 (6 Agentes Cardozo) movido para dentro do database "Treinos e Testes"

**Contexto:** Claudemberg apontou, ao vivo, que o Exame 2 (agendado 08-12/09/2026, decidido na Reunião Semanal de 07/09) precisava estar registrado DENTRO do database Notion "Treinos e Testes" — a estrutura padrão que a Drenagem Contínua usa para reconciliar pendências de Gestor (Passo 5.b, filtro Gestor+Status). Cardozo tinha criado apenas uma página solta (`https://app.notion.com/p/3d492372eae181c6aefdfc95728c353a`) com o cronograma — essa página **não é encontrada** pela query que a Drenagem roda, então na prática o Exame 2 estava invisível para o sistema, apesar de "documentado".

**O que foi feito:**
1. Consultado o database "Treinos e Testes" (`collection://7b0728a8-fd57-419c-8a51-d5fe3794d165`) via SQL — confirmado 0 linhas com `Gestor="Cardozo"` antes da correção.
2. Criadas 12 linhas (páginas) dentro do database, uma por exame: 6 Agentes × (E1 simples + E2 complexo). `Gestor="Cardozo"`, `Exame="Shadow→Assisted"`, `Status="pendente"`, `Caso-teste` com a descrição resumida de cada caso.
   - 08/09: Baumgart (E1 sapata rasa / E2 hélice contínua NBR 6122), Landell (E1 iluminação 100m² / E2 SPDA Decreto 42/2018)
   - 09/09: Saturnino (E1 água fria 3 banheiros / E2 reuso NBR 16783), Glaziou (E1 drenagem 500m² / E2 jardim de chuva)
   - 10/09: Tenreiro (E1 piso cimento queimado / E2 acústico NBR 15575:2025), Mindlin (E1 prancha técnica / E2 compilação completa)
3. Verificado via SQL: 12/12 linhas presentes, todas `Status="pendente"`.
4. **Corrigido gap de ferramenta do Cardozo (achado desde 02/09, nunca resolvido):** ele não tinha o ID do database salvo no próprio estado, por isso nunca conseguia reconciliar "Treinos e Testes" sozinho — sempre dependia da confirmação de Wallenberg. IDs (database + data source + schema) agora salvos em `_estado_cardozo.md`, Seção 2, marcados como resolvido. A partir de agora Cardozo reconcilia sozinho.

**Por quê:** Sem isso, a semana de exames (08-12/09) rodaria sem que a Drenagem Contínua ou o próprio Cardozo enxergassem a fila — decisão da Reunião Semanal ficaria só no papel.

**Como desfazer:** apagar as 12 páginas criadas no database (IDs retornados na chamada de criação); reverter a Seção 2 de `_estado_cardozo.md` (remover bloco de IDs); a página solta original permanece intacta como referência.

---

### [2026-09-08, 10:15-11:30] Drenagem Contínua v2.3 — 5ª Rodada (seg)

**Contexto:** Execução automática de `wallenberg-drenagem-continua-local` — Portão de Trabalho ativado (Passo 2.5).

**Fila verificada:**
- `pendencias.json`: 0 itens `alc:"auto"`+`status:"aberta"` (grep confirmado)
- Skills propostas: 1 Skill nova (`nbr6120-2019-acoes-cargas`, criada 08/09, Status "proposta")
- Notion "Treinos e Testes": 0 pendente

**Execução:**

1. ✅ **Cardozo acionado** (único Gestor com fila)
   - Avaliou Skill NBR 6120:2019 — **PROCEDE**
   - Substância técnica correta (norma 2019 vigente)
   - Escopo completo (tríade 6120→6118→6122 mapeada)
   - Confiança apropriada (média, fontes secundárias — padrão aceito)
   - Prioridade real (fecha tríade estrutural de Baumgart)
   - Arquivo-fonte atualizado: status "avaliada — pronta para ratificação de Claudemberg"
   - Nenhuma pendência aberta

2. ✅ **Learning Agent (Passo 8a)**
   - Segunda-feira: SIM
   - Execução real: SIM (Cardozo avaliou Skill)
   - Pesquisa de padrões multi-agente 2026: confirmado 6 padrões implementados (Portão, loop detection, Gate do Maurício, hierarquia stage-gated, detecção estagnação, trilha auditoria)
   - Oportunidades novas: nenhuma vs. linha de 07/09
   - Mudanças ao SKILL.md: nenhuma proposta

3. ✅ **Registros atualizados**
   - Registro Diário (`03_REGISTROS_DIARIOS/2026/Setembro/08.md`) criado
   - `_estado_wallenberg.md` Seção 1 atualizada com início de rodada

**Resultado:** 0 itens fechados (0 necessários), 1 Skill avaliada (PROCEDE), 0 bloqueios.

**Duração:** ~75 min (Portão + leitura + Cardozo background + Learning Agent + registros).

**Próxima ação:** Claudemberg ratificar Skill NBR 6120:2019 em rodada futura (próxima Semanal ou via aprovação direta).

---

### [2026-09-07, 10:30-11:00] Reunião Semanal com Claudemberg — RATIFICAÇÃO COMPLETA

**Contexto:** Reunião Semanal de Wallenberg (Função 9), segunda-feira 08/09/2026. Pauta consolidada com 5 ratificações + 3 decisões. Claudemberg ratificou TUDO.

**PARTE 1 — RATIFICAÇÃO (5 ITENS) — ✅ RATIFICADOS:**

1. ✅ **Auto-correção COSCIP v1.1 + JSON corrigido + Painel republicado (04/09)**
   - Skill COSCIP moldura corrigida (não era lacuna nova, era expansão de 28/07)
   - JSON `pendencias.json` corrigido (2 chaves faltando)
   - Painel Artifact republicado (27/08 → 04/09)
   - **Status:** RATIFICADO 07/09/2026

2. ✅ **Portão de Trabalho na Drenagem Contínua (02/09)**
   - Passo 2.5 novo: fila vazia → encerra sem Gestor
   - Teste 5 dias: validado
   - Economia: ~4 rodadas Gestor/semana (~US$ 40-50)
   - **Status:** RATIFICADO 07/09/2026 — ATIVA PERMANENTE

3. ✅ **Exclusão de STTK Consolidada (03/09)**
   - Tarefa `sttk-consolidada-otimizacaotokens` deletada
   - Scripts `rotina_sttk_consolidada.py`, `.bat`, README removidos
   - Medição de tokens agora roda na Semanal (Passo 2.5)
   - **Status:** RATIFICADO 07/09/2026

4. ✅ **Trim `_estado_kelsen.md` (171 KB → 20 KB) (03/09)**
   - Arquivo append-only → enxuto (4 seções fixas)
   - HISTÓRICO preservado (487 linhas = 0 perda)
   - Aprendizados (~40) preservados
   - **Status:** RATIFICADO 07/09/2026

5. ✅ **Skill NBR 6122 Fundações criada (07/09)**
   - v1.0 Trilha A: tipos, investigação geotécnica, Emenda 1/2022
   - Cross-disciplina: Baumgart + Saturnino + Glaziou
   - Lacuna declarada: ABNT não lida (fontes secundárias OK)
   - **Status:** RATIFICADO 07/09/2026

**PARTE 2 — DECISÕES (3 ITENS) — ✅ DECIDIDO:**

**Decisão 1: Ratificar 2 Skills Propostas**
- ✅ **COSCIP/CBMERJ (Decreto 42/2018)** — avaliada Cardozo → RATIFICADA 07/09/2026
- ✅ **NBR 6122 Fundações** — proposta Wallenberg → RATIFICADA 07/09/2026

**Decisão 2: Exame 2 dos 6 Agentes Cardozo**
- ✅ **QUANDO:** Semana de 08-12/09/2026 (segunda a quarta)
- ✅ **MODALIDADE:** 2 exames/agente × 6 agentes = 12 exames total
- ✅ **PLANEJAMENTO:** Página Notion criada (07/09) com cronograma, casos-teste, critérios
- ✅ **URL:** https://app.notion.com/p/3d492372eae181c6aefdfc95728c353a?pvs=204
- ✅ **Status:** AGENDADO 08/09/2026 → EXECUÇÃO SEMANA 08-12/09

**Decisão 3: Apresentação Interativa ao Cliente**
- ✅ **PAUSAR busca deliberada** até caso real pedir (Princípio 15)
- ✅ **Presenton (28/08)** mantém-se como melhor candidato mapeado
- ✅ **Status:** PAUSADO 07/09/2026

**SAÚDE DE CONSUMO (07/09):**
- Cache hit ratio: 90,7% (Item 7 STTK = CONCLUÍDO, não "aguardando")
- Contexto inicial: +12,8% vs base (não redução)
- Portão de Trabalho: validado, manter ativo
- Redução 45-67% esperada: 0% medido (prompt caching +90.7% = único ganho real)

**DECISÕES REGISTRADAS:**
| Item | O que foi | Decisão | Data |
|------|----------|---------|------|
| Auto-correção COSCIP+JSON+Painel | Ratificação | ✅ RATIFICADO | 07/09 |
| Portão de Trabalho | Ratificação | ✅ RATIFICADO (ativo) | 07/09 |
| Exclusão STTK Consolidada | Ratificação | ✅ RATIFICADO | 07/09 |
| Trim _estado_kelsen | Ratificação | ✅ RATIFICADO | 07/09 |
| Skill NBR 6122 | Ratificação | ✅ RATIFICADO | 07/09 |
| 2 Skills Propostas | Decisão | ✅ RATIFICADAS | 07/09 |
| Exame 2 Cardozo | Decisão | ✅ 08-12/09 | 07/09 |
| Apresentação Interativa | Decisão | ✅ PAUSADA | 07/09 |

**Como desfazer:** reverter git commit desta entrada (todos os 5 itens cancelados simultaneamente; se apenas alguns reverter manualmente).

**Próximas ações:**
- PDF pauta gerado
- Pauta registrada com decisões
- Livro-Razão consolidado
- Commit git com ratificação

**Registrado por:** Wallenberg (CEO)  
**Ratificado por:** Claudemberg (Presidente)  
**Data:** 07/09/2026, 10:30-11:00 UTC  
**Status:** ✅ COMPLETO E EXECUTADO

---

### [2026-09-08] Diária Skills v2.7 (Terça) — 1 Skill Trilha A (NBR 6120 Cargas) + 1 achado Vitruvius

**Executado por Wallenberg (rotina Seg-Qui, Passos 0-5+8):**

**Passo 0 (Pré-rodada):** fechamento de 07/09 lido. Estados de Kelsen/Cardozo/Lúcio verificados — todos estáveis, sem lacuna nova além do já documentado. Próxima prioridade Trilha A confirmada: NBR 6120:2019 (cargas — complemento natural da 6122 fundações e 6118 concreto armado).

**Passo 1 (Pesquisa Externa):** 6 buscas paralelas + 4 aprofundamentos. Eixos cobertos: NBR 6120:2019, CAU-RJ, render IA self-hosted, GitHub Revit MCP, multi-agent workflow, YouTube/Meta (Claude+Arquitetura).

**Passo 2 (Consolidação):** 2 achados úteis separados do ruído:
- NBR 6120:2019 → Skill Trilha A (Baumgart)
- Simone-Balin/Sam-AEC (100+ tools, guia de setup) → vitruvius achado (monitorar, baixa prioridade)
- Descartados: CAU-RJ acordo cooperação (dez/2024, velho, sem mudança regulatória); ComfyUI/SwarmUI/Forge (já cobertos); multi-agent enterprise +340% (padrões já implementados); YouTube tutoriais (educativo genérico); Claude na Engenharia Civil 41 Skills (produto pago R$47); Geopogo (comercial/SaaS); Redraw (cloud).

**Passo 3 (Redação):** Skill `baumgart_nbr6120-2019-acoes-cargas-calculo-estruturas.md` criada (v1.0, proposta). Conteúdo: tríade fundamental 6118+6122+6120, classificação de ações (permanentes/variáveis/especiais), tabela de cargas variáveis mínimas por uso (residencial 1,5 kN/m², escritório 2,0, garagem 3,0, cobertura inacessível 0,5), cargas especiais (guarda-corpo, divisórias, degraus isolados), cross-disciplina 5 Agentes, interação com 5 normas, 5 erros comuns a evitar. Lacunas declaradas: texto integral ABNT não lido (fontes secundárias); fatores de combinação (NBR 8681) não cobertos.

**Passo 4 (Salvamento):** Skill em `01_CEO/Skills_Propostas/2026/Setembro/`. `vitruvius_achados_candidatos.md` atualizado (Simone-Balin/Sam-AEC, "monitorar baixa prioridade" — 100+ tools, 1 star, é guia não MCP server novo). Índice de Setembro atualizado (9 Skills acumuladas, Baumgart sobe para 5 Skills).

**Passo 5 (PDFs):** 2 PDFs gerados (Skill + índice).

**Passo 8 (Ferramentas/Trilha B):** nenhuma lacuna real de Agente pediu ferramenta nova hoje. Burle = config, Portinari = busca pausada, 6 Agentes Cardozo = decisão de Claudemberg, Vitruvius = sem lacuna nova.

**Retrabalho evitado:** Apresentação interativa não pesquisada (busca PAUSADA desde 07/09, 6ª rodada consecutiva). ComfyUI/Blender/TRELLIS2 não duplicados. LuDattilo/BIMwright/IbrahimFahdah não duplicados. NBR 16280 reformas não pesquisada (PAUSADA per feedback). CAU-RJ deliberações já conhecidas não viram Skill.

**Como desfazer:** remover `baumgart_nbr6120-2019-acoes-cargas-calculo-estruturas.md`; reverter edições no índice e no vitruvius_achados (via git revert do commit desta rodada).

---

### [2026-09-07] Diária Skills v2.7 (Segunda) — 1 Skill Trilha A (NBR 6122 Fundações) + 1 achado Vitruvius

**Executado por Wallenberg (rotina Seg-Qui, Passos 0-5+8):**

**Passo 0 (Pré-rodada):** fechamento de 04/09 lido (sexta-feira), estados de Kelsen/Hely/Cardozo verificados. Caso Daniel-OB ativo (COSCIP A-4 = 62 unidades confirmado por Hely 04/09). Cardozo fila limpa, 6 agentes Shadow. Lacuna real identificada: Baumgart não tinha cobertura de fundações (NBR 6122).

**Passo 1 (Pesquisa Externa):** 6 buscas paralelas (NBR 6122, CAU-RJ, Revit MCP GitHub, render IA, multi-agent workflow, apresentação ao cliente). CAU-RJ: nenhuma deliberação nova em setembro. Render: nada novo self-hosted. Apresentação: 5ª busca consecutiva sem ferramenta gratuita viável — recomendação formal de pausar.

**Passo 2 (Consolidação):** 2 achados úteis: NBR 6122 (Skill) + IbrahimFahdah/revit-claude-mcp 46 tools (vitruvius achado). Restante descartado como ruído (mesmas ferramentas cloud, projetos pequenos superados).

**Passo 3 (Redação):** Skill `baumgart_nbr6122-2022-emenda1-fundacoes-projeto-execucao.md` criada (v1.0, proposta). Conteúdo: tipos de fundação (rasas/profundas), investigação geotécnica obrigatória, Emenda 1/2022 (cimento 400→350 kg/m³), interface com 7 normas correlatas, checklist de projeto, erros comuns. Lacunas declaradas: texto integral ABNT não lido (fontes secundárias verificadas).

**Passo 4 (Salvamento):** Skill em `01_CEO/Skills_Propostas/2026/Setembro/`. `vitruvius_achados_candidatos.md` atualizado (IbrahimFahdah, "monitorar"). Índice de Setembro atualizado (8 Skills acumuladas). Livro-razão registrado.

**Passo 5 (PDFs):** a seguir.

**Passo 8 (Ferramentas/Trilha B):** nenhuma lacuna real de Agente pediu ferramenta nova hoje. IbrahimFahdah registrado em vitruvius_achados como "monitorar" (46 tools não preenche lacuna vs BIMwright 229 / LuDattilo 138).

**Como desfazer:** remover `baumgart_nbr6122-2022-emenda1-fundacoes-projeto-execucao.md`; reverter edições no índice e no vitruvius_achados (via git revert do commit desta rodada).

---

### [2026-09-07] Drenagem Contínua v2.3 (Segunda, 10:15) — Portão de Trabalho ativado, Cardozo único Gestor acionado

**Contexto:** disparo agendado da `wallenberg-drenagem-continua-local`. Verificação do Portão de Trabalho (Passo 2.5): `pendencias.json` com zero itens `alc:"auto"`+`status:"aberta"` (46 resolvida, 3 descartada, 1 pausada); Notion "Treinos e Testes" zero pendente (`notion-query-data-sources`, filtro Status=pendente); mas a Skill `complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md` (criada 04/09 pela Diária) seguia com Status "proposta", nunca avaliada por nenhuma rodada de Drenagem — a rodada de 04/09 (mesmo dia) tinha reportado "fila vazia" sem capturá-la. Como havia 1 item real (skill nova, owner Cardozo), o Portão não fechou a rodada: só Cardozo foi acionado — Kelsen e Lúcio confirmados sem fila (nenhuma pendência aberta com seu owner, nenhuma Skill de Setembro destinada a eles) e não foram chamados, conforme a regra de 02/09 (Opção B/Alvo A).

**Executado por Cardozo (Autonomous), único Gestor acionado:**
- Reconciliou a própria fila em `pendencias.json` (zero itens abertos seus).
- **Avaliou a Skill COSCIP/CBMERJ na íntegra — PROCEDE.** Conhecimento Trilha A válido para Landell (SPDA/alarme/iluminação de emergência) e Baumgart (resistência ao fogo/TRRF/compartimentação), sem erro factual, escopo bem separado do que já é do Kelsen. Marcada "avaliada — pronta para ratificação de Claudemberg" (Cardozo não ratifica, só avalia).
- **Varredura de melhoria (Passo 7) — achado real:** os 6 Agentes de Complementares seguem em Shadow desde 01/09/2026 (Exame 1) sem Exame 2 (Shadow→Assisted) administrado — uma semana parado. Montar 3 casos-teste × 6 Agentes é trabalho grande demais para uma rodada de Drenagem sem virar exame raso. **Nova pendência aberta:** `cardozo-exame2-6-agentes-nao-administrado` (owner Cardozo, `alc:"planejado"`) — fica para rodada dedicada futura, fora da Drenagem Contínua.
- Achado de ferramenta (não resolvido): Cardozo não conseguiu confirmar a fila do Notion "Treinos e Testes" pelo próprio lado — `notion-fetch` não faz busca por título, só por ID/URL exato, e ele não tem o ID do database salvo no próprio estado. Aceitou a confirmação já feita por Wallenberg, mas o gap persiste (mesma classe já registrada em 02/09). **Recomendação:** salvar o ID/URL do database "Treinos e Testes" no `_estado_cardozo.md` para ele confirmar sozinho nas próximas rodadas.

**Learning Agent (Passo 8a) — executado (segunda-feira + execução real na rodada):** pesquisa web sobre padrões de orquestração multi-agente 2026 (circuit breakers/budget de tokens, loop detection, approval gates, orchestration layer unificado, log estruturado com correlation ID). Mapeamento contra a rotina: a maioria já implementada (Portão de Trabalho = budget/circuit breaker; verificação de disparo duplicado = loop detection; Gate do Maurício = approval gate; cadeia CEO→Gestor→Agente = orchestration layer). Único gap identificado (log "tamper-evident" com correlation ID formal) é prática de auditoria de escala enterprise, não prioritária agora. **Nenhuma modificação ao `SKILL.md`.**

**Painel do Fundador:** não tocado — nenhuma mudança de capacidade real do organismo hoje (Skill "avaliada" ainda não é Skill ativa; pendência nova é baixa prioridade/planejada). Princípio 15.

**Fechamento:** 1 Gestor acionado (Cardozo), 1 com execução real, 0 itens de `pendencias.json` fechados (1 novo aberto: `cardozo-exame2-6-agentes-nao-administrado`), 1 Skill avaliada (aguarda ratificação de Claudemberg). Nenhum item cruzou a fronteira.

---

### [2026-09-04, mesma rodada] Auto-correção: Skill COSCIP não era lacuna nova + JSON quebrado em `pendencias.json` encontrado e corrigido

**Contexto:** ao redigir a entrada do Painel do Fundador (Passo 6), a checagem de eventos desde a última atualização (01/09) levou a reler o feed histórico e achar uma entrada de **28/07/2026** já cobrindo COSCIP/CBMERJ — contradizendo a Skill que eu tinha acabado de escrever hoje como "lacuna nunca coberta antes".

**Achado 1 — Skill duplicada em framing (conteúdo parcialmente novo):** o COSCIP já tinha pendência fechada (`b10-coscip-nt107`, 28/07/2026, auditoria dupla Hely/Kelsen) e está documentado em `.claude/skills/legal-base-legislativa-bairro/SKILL.md`. A Skill nova de hoje (`complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md`) não era pura duplicata — trazia um mapa de Notas Técnicas por disciplina (Landell/Baumgart) inexistente antes, e um achado novo (grupamento A-4 >6 unidades pode não ser isento) relevante ao caso ativo Daniel-OB — mas a moldura ("lacuna nunca coberta") estava factualmente errada.

**Executado por Wallenberg:**
- **Skill corrigida para v1.1** com nota de correção explícita no topo, dividindo competência: isenção/exigibilidade (Kelsen, `legal-base-legislativa-bairro`) vs. mapa técnico por disciplina (Complementares, esta Skill).
- **`legal-base-legislativa-bairro/SKILL.md` atualizada** — seção COSCIP existente ganhou o achado novo sobre grupamentos A-4 (não fechado com o mesmo rigor da B10, registrado como pista pendente de apuração). Backup pré-edição em `_backups/2026-09-04/legal-base-legislativa-bairro_SKILL_pre-correcao-coscip.md`.
- **Nova pendência aberta:** `kelsen-coscip-grupamento-a4-limiar-6-unidades` (owner Kelsen, agente Hely, alc:auto, crit:media) — apurar com rigor o dispositivo primário do limiar de 6 unidades antes de aplicar a qualquer caso real, mesmo padrão que fechou a B10.
- **`indice.md` de Setembro corrigido** com a moldura certa.

**Achado 2 (colateral, mais sério) — `01_CEO/Pendencias/pendencias.json` estava com JSON INVÁLIDO:** 2 chaves de fechamento `}` faltando entre objetos (após `kelsen-daniel-ob-legislacao-real-lote04` e após `lucio-daniel-ob-excedente-ate-cliente-aprovou`) — confirmado com `python -m json.load`, erro `Expecting ',' delimiter`. Isso quebra qualquer leitura programática do arquivo que todos os Gestores citam como "fonte de verdade" da fila. Não sei há quantas rodadas o arquivo está quebrado — nenhum registro anterior no livro-razão menciona isso, o que sugere que os Gestores vêm lendo o arquivo via `Read`/`Grep` (que toleram texto malformado) em vez de parser JSON real, mascarando o problema.

**Executado por Wallenberg:**
- Backup em `_backups/2026-09-04/pendencias_pre-correcao-json.json`.
- 2 chaves `},` inseridas nos pontos exatos. Revalidado com `python -m json.load` — 48 itens (49 após a nova pendência acima).

**Como desfazer:** restaurar os 3 arquivos (`complementares_coscip-...md`, `legal-base-legislativa-bairro/SKILL.md`, `pendencias.json`) dos backups em `_backups/2026-09-04/`; remover a pendência `kelsen-coscip-grupamento-a4-limiar-6-unidades`.

**Recomendação a Claudemberg:** considerar validação de JSON (`python -m json.tool` ou equivalente) como passo automático depois de qualquer edição em `pendencias.json` — o bug ficou invisível porque nada força parse estrito.

**Achado 3 (colateral, no Passo 6/Painel) — o Painel publicado (Artifact) estava travado em 27/08/2026:** ao ler a versão publicada antes de republicar (regra obrigatória), o `<span class="updated">` do artifact ao vivo dizia "Atualizado 27/08/2026" — a atualização de 01/09/2026 (Cardozo Autonomous, 6 Agentes Shadow) só existia no arquivo local `painel_fundador_sttk.html`, nunca foi de fato republicada via Artifact. O painel que Claudemberg via ao abrir o link estava 8 dias desatualizado. Corrigido nesta rodada — republicado com o conteúdo local (01/09 a 04/09 incluídos, sem perda).

---

### [2026-09-04] Rotina Diária de Skills v2.7 (Sexta, executada como Seg-Qui por engano de calendário) — 1 Skill nova + 1 achado Vitruvius atualizado

**Contexto:** rodada autônoma Seg-Qui (Passos 1-5+8). Pesquisa nos 5 eixos obrigatórios: render/vídeo, apresentação ao cliente, CAU-RJ, Complementares (Trilha A), Revit/BIM.

**Executado por Wallenberg:**
- **Skill nova criada** (Trilha A, Inteligência): `01_CEO/Skills_Propostas/2026/Setembro/complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md` + PDF. Cobre o **COSCIP** (Decreto Estadual 42/2018) — segurança contra incêndio no RJ, lacuna nunca coberta antes. Cross-disciplina Landell (alarme/detecção/SPDA) e Baumgart (resistência ao fogo/compartimentação). Achado prático relevante: residência unifamiliar isolada (A-1) tende a ser isenta de aprovação CBMERJ; grupamento/condomínio horizontal (A-4, ex. caso real Daniel-OB/Condomínio Venice) com mais de 6 unidades **não** é isento.
- **`vitruvius_achados_candidatos.md` atualizado** (achado de 24/08, LuDattilo/revit-mcp-server 138 tools): detalhe técnico completo obtido (categorias operacionais, requisitos, limitações), decisão sobe de "monitorar" para "avaliar incorporação parcial". Backup pré-edição em `_backups/2026-09-04/vitruvius_achados_candidatos.md`.
- **`01_CEO/Skills_Propostas/2026/Setembro/indice.md` atualizado** com a Skill nova, estatísticas e observações da rodada. Backup pré-edição em `_backups/2026-09-04/indice_setembro.md`.
- **PDFs regenerados:** 2 (Skill COSCIP nova + índice de Setembro).

**Descartados com justificativa (Passo 1):** Autodesk APS Sample MCP Server (paga, cloud-only, exige assinatura ACC/BIM360 — viola critério 1); Modly (geração de modelo 3D via GPU local, não é renderizador de cena arquitetônica — foco errado); Presenton (self-hosted, mas já registrado em 28/08 — não duplicado); CAU-RJ (busca de setembro não achou deliberação nova específica do CAU-RJ).

**Passo 8 (Trilha B/Ferramentas):** nenhuma lacuna real nova pedindo busca de ferramenta esta rodada — Landell/Baumgart/demais Agentes de Cardozo aguardam Briefing real (sem caso ativo); bloqueio de Burle (media_upload_widget/show_generation_by_ids) é config já escalada, não candidato de busca GitHub nova.

**Como desfazer:** restaurar `vitruvius_achados_candidatos.md` e `indice.md` (Setembro) dos backups em `_backups/2026-09-04/`; remover o arquivo `.md`+`.pdf` da Skill COSCIP (status ainda "proposta", não ratificada).

---

### [2026-09-03] Trim do `_estado_kelsen.md` (171 KB → 20 KB) — decisão de Claudemberg

**Contexto:** o arquivo de estado do Kelsen é lido no início de todo acionamento dele (75 até agora) e da cadeia Kelsen→Hely. Estava em **487 linhas / 171 KB (~40k tokens)** — log append-only desde 13/07, violando a própria regra do arquivo ("substitua seções, não append"; "apague o que virou passado"). É a Função 6 (Padronizador) + o alvo mais recorrente de custo por agente.

**Executado por Wallenberg:**
- `_estado_kelsen.md` copiado verbatim para **`_estado_kelsen_HISTORICO.md`** (487 linhas, nada perdido) — arquivo que o Kelsen **não lê ao nascer**.
- `_estado_kelsen.md` reescrito enxuto (**114 linhas / 20 KB**), 4 seções fixas: (1) onde parei — condensado, com os 2 casos ativos (Daniel-OB + EVTL) e a base AP4/unifamiliar/LMS; (2) pendências — só ponteiros para `pendencias.json`; (3) **os ~40 aprendizados preservados integralmente**; (4) como escrever (agora manda o log cronológico ir para o HISTÓRICO).
- `.claude/agents/kelsen.md` — nota sobre o HISTÓRICO e a regra de não fazer append de log no arquivo vivo.

**Nada de conteúdo foi perdido** — o HISTÓRICO tem o arquivo antigo byte a byte. As lições da Seção 3 estão nos dois.

**Como desfazer:** `cp "_estado_kelsen_HISTORICO.md" "_estado_kelsen.md"` (remove o cabeçalho de HISTÓRICO manualmente) e reverter a nota no `.claude/agents/kelsen.md`.

**Próximos (mesmo padrão, ainda não feitos):** `_estado_hely.md` (103 KB), `_estado_lucio.md` (96 KB), `_estado_wallenberg.md` (113 KB).

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

### [2026-09-03 10:22-11:15] Drenagem Contínua v2.3 — 2ª rodada automática (terça-feira)

**Contexto:** 2ª rodada automática da tarefa agendada `wallenberg-drenagem-continua-local`, 03/09/2026 (ter), 10:22-11:15. Execução autônoma, Claudemberg ausente.

**Portão de Trabalho (Passo 2.5):** Fila mapeada — 3 itens auto+aberta (Wallenberg 1, Kelsen 2) + 5 Skills novas (Kelsen 2, Cardozo 3). Prosseguiu.

**Reconciliação de fila (Fase 4, Passo 5):**
1. **Wallenberg** (1 item): `wallenberg-fase2-integracao-otimizacoes` estava mal classificado como `alc:"auto"` — estava deliberadamente PAUSADO desde 26/08 (auditoria crítica). **Reclassificado para `alc:"planejado"`** (permanece aberto, não executável). Fila reconciliada e limpa de auto+aberta.
2. **Kelsen** (2 itens): `drive-legal-fase2-frases-genericas` e `drive-legal-pops-copias-desatualizadas` — **2 bloqueados por permissão** (Service Account modo automático veta Bash). Ambos já bloqueados desde 31/08. Redação das substituições pronta em 31/08; recomendação de escopo decisória — pendente Wallenberg executar fora do automático. Fila reconciliada, 0 itens executáveis agora.
3. **Cardozo** (0 itens auto+aberta): fila limpa.

**Avaliação de Skills novas (Fase 4, Passo 5 + Fase 6, Passo 6):**
- **Kelsen**: 2 Skills proposta avaliadas — legal_lc281-2025, legal_resolucao-smdu-10-2026 — ambas **prontas para ratificação de Claudemberg** (Trilha A, sem lacuna crítica, impacto baixo-médio).
- **Cardozo**: 3 Skills proposta avaliadas:
  - **NBR 15220-3:2024** (ZB 4A): ✅ Pronta. Cross-disciplina Tenreiro/Baumgart/Glaziou. Esclarecimento menor: período de transição 15220-3 vs Emenda 1/2025 da 15575.
  - **NBR 9575:2024** (Impermeabilização): ✅ Pronta. Cross-disciplina Saturnino/Baumgart/Tenreiro. Sem lacuna.
  - **NBR 15575:2025** (Acústica Pisos): ⚠️ **Incompleta**. Lacuna crítica: valores numéricos para ambientes sem dormitório não estão em fonte aberta (norma ABNT é paga). Skill admite limitação explicitamente. Recomendação: aguarda acesso norma ou reformulação com nota de ressalva.

**Total de execução real:** **Zero itens auto+aberta executados** (1 reclassificado, 2 bloqueados por permissão). 5 Skills avaliadas (4 prontas, 1 com bloqueio técnico).

**Ações não executadas por falta de execução real:**
- Passo 6 (Implantação de Ferramenta): nenhuma (Skills aguardam ratificação/reformulação, e Gestores não estão em nível Autonomous pra implantar Trilha A).
- Passo 7 (Varredura de Melhoria): Gestores com fila limpa teriam feito varredura, MAS todos têm itens bloqueados ou Skills pendentes — nenhuma varredura iniciada.
- Passo 8a (Learning Agent): **PULADO** — hoje é terça-feira, não segunda-feira (Passo 8a só roda seg E se houve execução real).

**Registrado em pendencias.json:**
- `wallenberg-fase2-integracao-otimizacoes`: alc mudado de "auto" para "planejado" (status permanece "aberta").
- Sem novos itens abertos.

**Painel Fundador:** sem mudança (zero execução real, zero item para reportar no feed).

**Próximos passos:**
1. Wallenberg: executar fora do modo automático as 2 edições Drive de Kelsen (quando Claudemberg presente ou permissão elevada).
2. Claudemberg: ratificar 4 Skills prontas (Kelsen 2, Cardozo 2 — NBR 15220-3 e NBR 9575).
3. Cardozo/alguém: reformular NBR 15575 com acesso norma ABNT ou note de ressalva antes de ratificação.

**Duração:** ~53 min (Portão 5min + Acionamento Gestores paralelo ~88s cada + consolidação).

---

### [2026-09-03, ao vivo] Fechamento pós-Drenagem: 1 item Drive executado + 4 Skills ratificadas — Claudemberg presente

**Contexto:** Claudemberg entrou ao vivo logo após a 2ª rodada de Drenagem Contínua (10:22-11:15) para resolver o que ficou bloqueado/pendente de ratificação.

**Item 1 — `drive-legal-fase2-frases-genericas` EXECUTADO:**
Wallenberg executou via Google Docs API (Service Account `sttickler-organismo-ia`), backup em `_backups/2026-09-03/drive-legal-fase2-frases-genericas_texto_pre_edicao.md`. **Achado na releitura antes de editar:** a Fase 1 (30/07) já tinha substituído "conforme legislação vigente" pela citação do Decreto, mas deixou **redundância** (citação duplicada na mesma frase) em vez do texto genérico puro que o item original supunha — correção ajustada em tempo real. Aplicadas 5 substituições (3 em POP-ARQ-PL-01: Seção 2, Seção 7.1 passo 2, "Arquiteto contrato"→"contratado"; 2 em MEMORIAL DESCRITIVO: regência "as Decreto"→"ao Decreto", ressalva de que fachada não é peça autônoma do DULI). Todas confirmadas por releitura pós-edição via Docs API. **Item fechado.**

**4 Skills ratificadas** (Claudemberg, decisão verbal "vamos executar"):
- `legal_lc281-2025-condicoes-especiais-licenciamento-rj.md` (Kelsen/Legal)
- `legal_resolucao-smdu-10-2026-consulta-previa-rdt-rj.md` (Kelsen/Legal)
- `complementares_nbr15220-3-2024-reclassificacao-bioclimatica-rj.md` (Cardozo/Complementares)
- `complementares_nbr9575-2024-impermeabilizacao-selecao-projeto.md` (Cardozo/Complementares)

Status atualizado de "proposta" para "ratificada" em cada arquivo, com data e contexto da ratificação.

**Pendente de decisão (não executado ainda):**
- `drive-legal-pops-copias-desatualizadas` — decisão de organização do Drive (remover cópias antigas vs. sincronizar), aguardando escolha de Claudemberg antes de executar.
- `complementares_nbr15575-2025-desempenho-acustico-pisos.md` (NBR 15575, Cardozo) — **não ratificada**: lacuna técnica real (valores para ambientes sem dormitório não em fonte aberta, norma ABNT paga). Aguarda decisão sobre acesso à norma ou reformulação com ressalva.

**Como desfazer:** reverter as 5 substituições do item 1 usando o texto de backup listado acima; reverter Status de "ratificada" para "proposta" nos 4 arquivos de Skill se necessário.

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

### [2026-09-08] Rotina Diária Skills v2.8 → v2.9 — Item 2: Fluxo de Ativação de Skills

**Contexto:** conversa ao vivo com Claudemberg (Função de Wallenberg — melhoria do organismo). Item 2 de 6 da lista de melhorias. Decisão alinhada item a item; Claudemberg aprovou o recorte e pediu para aplicar na rotina de Skills.

**O que decidiu:** Skill de Trilha A (Inteligência — normas/técnicas/regras) deixa de nascer como `proposta` parada esperando a Reunião Semanal. Passa a: (1) Gestor dono valida no mesmo dia (erro factual / não é duplicata / lacunas marcadas) via ferramenta `Agent`; (2) ativa em produção imediatamente (`Status: ativa`); (3) Claudemberg revisa retroativamente na Semanal — deixa de ser portão de entrada, vira revisão com poder de reverter. Skill sem fonte primária lida ativa com **selo de ressalva** (`Status: ativa-com-ressalva` + bloco de aviso obrigatório no topo; Agente sinaliza a lacuna ao aplicar em caso real; nunca vira número final de documento de cliente sem fechar a fonte). Trilha B (ferramentas / Passo 8) e Skill de Gestor não implantado (Fechamento) seguem `proposta` como antes — ferramenta precisa instalar/testar, Gestor inexistente não tem quem valide.

**Por quê:** o modelo de governança do organismo (reescrita de 20/07/2026) já mandava "ativar por conta própria, ratificar depois" — a rotina tinha derivado para carimbar tudo `proposta` e represar até ratificação em bloco (caso 07/09). Construir capacidade antes de ter caso real é treino deliberado, não desperdício (posição de Claudemberg); o gargalo era o portão de ativação, não o ritmo de produção. O selo de ressalva protege a parte legal/normativa — parâmetro urbanístico ativado como verdade final com fonte secundária é retrabalho dobrado (projeto refeito para entrar na legalidade).

**O que alterou:** `01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md` — frontmatter (v2.9.0), Passo 3 (2 blocos novos: Fluxo de Ativação + Selo de Ressalva), Passo 4 (coluna Status do índice), Regra de Governança (linha v2.9), Histórico de Versões (linha 2.9), rodapé.

**Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-08/wallenberg-rotina-diaria-skills-v2_SKILL_pre-item2-ativacao.md`

**Pendente de propagação (não feito nesta sessão):** `Checklist_Diaria.html`, `wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md` e `wallenberg_manual_operacional_rotina_diaria_skills.md` ainda descrevem o fluxo antigo (Skill → proposta). Atualizar antes da próxima execução seg-qui, ou na leva de edições em bloco das melhorias 1–6. PDF gêmeo do SKILL.md não regenerado (CronJob 20:00 cobre).

**Como desfazer:** `cp "01_CEO/Decisoes_Autonomas/_backups/2026-09-08/wallenberg-rotina-diaria-skills-v2_SKILL_pre-item2-ativacao.md" "01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md"` e remover esta entrada.

---

### [2026-09-08] Melhorias do Organismo — Itens 4, 5 e 6 (parte) aplicados

**Contexto:** continuação da conversa ao vivo de 08/09 (Função de Wallenberg — lista de 6 melhorias). Itens 4, 5 e 6 decididos item a item com Claudemberg; aplicados nesta sessão os que são de baixo risco. Itens 1 (Fechamento) fica atrás do Cardozo; 6.2 e 6.5 (reescritas maiores) ficam para passe dedicado.

**Item 4 — Cadência da reauditoria legal → varredura mensal de documentos no Drive, por Gestor.**
- `wallenberg-drenagem-continua-local/SKILL.md`: Passo 7 ganhou trava "não reconferir vigência legislativa na varredura diária"; novo **Passo 7.5** — só na 1ª rodada útil do mês, cada Gestor acionado varre os documentos dele no Drive (Kelsen POPs Legal + base legislativa, Lúcio POP-PROJ, Cardozo os 6 POPs de disciplina). Autônomo: sinaliza + corrige erro objetivo + exclui/trasheia/dedup + cria doc faltante (via conector MCP de Drive). Não autônomo: reescrita canônica de conteúdo (só sinaliza). Descoberta de lei/trâmite novo segue com a Rotina Diária Skills (Passo 1); checagem de vigência por caso de cliente segue inegociável.
- Base: teste real de 08/09 confirmou que o conector MCP de Drive cria + edita + trasheia arquivo existente (Service Account não fazia; MCP faz). Memória `feedback_drive_e_fonte_unica_documentos_existentes` corrigida.

**Item 5 — Inventário de Capacidade.**
- Novo arquivo `01_CEO/Inventario_Capacidade/inventario_capacidade_sttk.md`, dono Wallenberg. Regra: sem linha "testado assim, nesta data" = capacidade tratada como indisponível. Populado com o que está verificado (Drive MCP, Drive Service Account, Notion, Agent, WebSearch, watch, scripts PDF, token_tracking, Painel, scheduled-tasks) e o que está presente-mas-não-validado (Vitruvius, Higgsfield, Claude in Chrome, cadeia Cardozo→6 Agentes).

**Item 6.1 — Semanal → quinzenal em teste (08/09 a 08/10).**
- Cron de `wallenberg-reuniao-semanal` mudado de `30 10 * * 1` para `30 10 8-14,22-28 * 1` (2ª feira a cada ~14 dias). Nota datada no SKILL.md com gatilho de reavaliação em 08/10 e reversão.

**Item 6.3 — Painel só com mudança de capacidade real.**
- `drenagem-continua-local/SKILL.md` Passo 8c: "houve execução real" não basta; só republica se um leitor de fora veria diferença no que o organismo consegue fazer.

**Item 6.4 — PDF gêmeo só de pauta + livro-razão.**
- `wallenberg-rotina-diaria-skills-v2_SKILL.md` Passo 5: Skill e `indice.md` não geram mais PDF gêmeo (arquivo de máquina, lido via Read). CronJob 20:00 fica só com pauta + livro-razão.

**Backups:** `_backups/2026-09-08/` — `drenagem-continua-local_SKILL_pre-item4-varredura-mensal.md`, `wallenberg-drenagem-continua-v2_SKILL_pre-item4.md`, `wallenberg-rotina-diaria-skills-v2_SKILL_pre-item2-ativacao.md`.

**NÃO feito nesta sessão (dívida aberta):**
- Item 1 (criar Gestor de Fechamento + 4 Agentes) — depende do Cardozo fechar (Exame 2, 08–12/09).
- Item 6.2 — condensar `_estado_hely.md` (111 KB), `_estado_wallenberg.md` (117 KB), `_estado_lucio.md` (95 KB): log → HISTÓRICO, arquivo vivo condensado. Passe dedicado.
- Item 6.5 — colapsar fechamento de rotina + Registro Diário + entrada no livro-razão em um registro só. Redesenho de processo, toca vários SKILLs. Passe dedicado.
- Item 2 — propagar o fluxo de ativação aos 3 espelhos (`Checklist_Diaria.html`, `_REDEFINIDO.md`, manual operacional).
- Item 4 — replicar o Passo 7.5 no arquivo-fonte `01_CEO/wallenberg-drenagem-continua-v2_SKILL.md` (só a cópia executável em `.claude/scheduled-tasks/` foi editada).

**Como desfazer:** restaurar os 3 arquivos dos backups de `_backups/2026-09-08/`; `update_scheduled_task wallenberg-reuniao-semanal cronExpression "30 10 * * 1"`; apagar `01_CEO/Inventario_Capacidade/`; remover esta entrada.

---

### [2026-09-10, 10:15-10:45] Drenagem Contínua v2.3 — 7ª Rodada (qua) — Consolidação Exame 2

**Contexto:** Execução automática de `wallenberg-drenagem-continua-local` (segunda rodada desta semana, Portão ativado).

**Fila verificada:**
- `pendencias.json`: 0 itens `alc:"auto"`+`status:"aberta"` (grep confirmado)
- Skills propostas: 1 Skill "proposta" (`nbr6120-2019-acoes-cargas`, criada 08/09, status "proposta" — não avaliada nesta rodada)
- Notion "Treinos e Testes": 2 itens "pendente" (Exame 2 Tenreiro+Mindlin — continuação de 09/09)

**Decisão do Portão:** Fila não vazia. Gestor acionado: Cardozo (Exame 2 represado).

**Execução:**

1. ✅ **Cardozo acionado em background** (10:22)
   - Escopo: administrar Exame 2 (Shadow→Assisted) para Tenreiro+Mindlin (últimos 2/6 do lote)
   - Cronograma original: 10/09 (confirmado)
   - Instrução: não sub-delegar; executar direto
   - Retorno (10:45 matutino): **2/2 aprovado ambos**

2. ✅ **Resultado final consolidado:**
   - **Tenreiro (Interiores):** E1 piso Ipanema, E2 acústica NBR 15575:2025 — **2/2 APROVADO. Promovido Shadow→Assisted.**
   - **Mindlin (Apresentação):** E1 prancha Tijuca, E2 compilação Laranjeiras — **2/2 APROVADO. Promovido Shadow→Assisted.**
   - **✅ LOTE EXAME 2 COMPLETO: 6/6 Agentes Cardozo Assisted**
     - Baumgart 08/09
     - Landell, Saturnino, Glaziou 09/09
     - Tenreiro, Mindlin 09/09 (confirmado em disco 10/09)

3. ✅ **Integridade de estado verificada:**
   - 4 memoriais técnicos de Tenreiro+Mindlin em disco (confirmado por Cardozo)
   - `.claude/agents/tenreiro.md` e `mindlin.md` atualizados para nível Assisted
   - `_estado_tenreiro.md` e `_estado_mindlin.md` atualizados

4. ⚠️ **Gap de ferramenta Notion reincidiu 6ª vez**
   - Cardozo não consegue atualizar Notion (sem ferramenta de escrita)
   - IDs aguardando registro manual por Wallenberg:
     - Tenreiro E1: `3d592372-eae1-8104-b731-da3c76b89666` / E2: `3d592372-eae1-819a-8644-ebd34fd9b0e6`
     - Mindlin E1: `3d592372-eae1-81f3-a458-ffa63299f3c0` / E2: `3d592372-eae1-8164-a9f6-f3c527dd6b52`
   - Campos: Status `pendente→aprovado`, Resultado `2/2 aprovado`, Atualizado em `09/09/2026`

5. ❌ **Learning Agent (Passo 8a):** não rodado (quarta-feira, só roda segunda)

6. ✅ **Painel (Passo 8c):** mudança de capacidade real → **REPUBLICA** com atualização de card Cardozo

**Impacto de capacidade:** 
- ✅ 6 Agentes de Complementares agora Assisted (estavam Shadow)
- ✅ Cardozo pronto para Exame 3 (Assisted→Autonomous) quando julgar apropriado
- Primeira equipe completa em nível Assisted desde a criação

**Como desfazer:** reverter `.claude/agents/tenreiro.md` e `mindlin.md` para Shadow; reclassificar Notion como "pendente"; readministrar Exame 2.

**Duração:** ~20 min de execução automática + consolidação.

**Próxima ação:** Wallenberg atualizar Notion manualmente (IDs acima); republica Painel; entrega da rodada 10/09 concluída.

---

---

### [2026-09-23] Drenagem Contínua v2.4 — rodada automática (qua) — 2 Skills avaliadas, 1 linha Notion órfã fechada, 2 exames gerados

**Portão (2.5):** 0 itens `auto`+`aberta`; 2 Skills novas sem avaliação de Gestor (Landell NBR 14565:2019 — nova; LC 301/2026 v1.1 — correção de hoje); Notion: 0 `pendente`, mas 1 linha `em execução` órfã desde 01/08 (Caso Andrade, Lúcio Shadow→Assisted caso 1). As rodadas anteriores filtravam só `pendente` e nunca a viram.

**Cardozo (NBR 14565, Landell):** PROCEDE COM RESSALVA. Corrigiu no arquivo-fonte e na cópia instalada em `.claude/skills/`: existe a NBR 16264:2016 (cabeamento residencial), ao contrário do que a Skill dizia; data center é a NBR 16665:2019, não a "16065"; cabo KNX tem 0,8 mm de diâmetro; PE do rack pela Tabela 58 da NBR 5410; Landell não assina ART/RRT. Em aberto: NBR 5281/11785/14159 não confirmadas. Lacuna: a v1.1 deveria ter a NBR 16264 como base primária (recomendação à Diária).

**Kelsen (LC 301 v1.1):** NÃO PROCEDE, com base no PDF primário arquivado. O desconto de 30% (Art. 58 LC 301 → Art. 40 LC 281) não tem recorte geográfico, mas só incide sobre a contrapartida por acréscimos. Por isso não se aplica a unifamiliar dentro dos parâmetros. O Art. 64 não existe (a lei vai até o 63). O +20% do §8º soma ao Anexo VII, não aos 30%. Status do cabeçalho alterado para "avaliada — NÃO PROCEDE — aguarda decisão de Claudemberg; não instalar". **Brecha de Escopo sinalizada:** Skill centrada na AEIU Praça Onze (Centro), fora do foco Barra/Recreio. Não foi descartada, vai para decisão.

**Notion, reconciliação:** a linha `3af92372…ccd9` (Caso Andrade) foi alterada de `em execução` para `aprovado`. O próprio Resultado já registrava a aprovação por Wallenberg em 01/08, e Lúcio está em Autonomous desde 07/08.

**Loop de Promoção (5.b.3):** Lelé (Formação) e Villaça (Shadow) tinham fila vazia no Notion. Foram gerados `Gestores/Lelé (Fechamento)/cenario_teste_notion_002.md` (NTN-2026-LELE-002: Gate 16 sob pressão de cronograma, 4 iscas, eixo novo) e `Gestores/Villaça (Viabilidade)/cenario_teste_notion_001.md` (NTN-2026-VILLACA-001: desconto LC 301 indevido sobre OODC, média de bairro, parâmetro preliminar, promessa de lucro). As 2 linhas foram criadas no Notion como `pendente`. **Nenhuma promoção:** falta administrar, auditar o artefato e ratificar na Semanal.

**pendencias.json:** +2 itens: `skill-lc301-v11-nao-procede-decisao` (humano) e `kelsen-hely-lc281-art40-unifamiliar-ap4` (auto, próxima rodada).

**Painel:** não tocado, porque não houve mudança de capacidade real. **Learning Agent:** não rodou (quarta-feira). **Passo 7.5:** não se aplica (não é a 1ª rodada útil do mês).

**Backups:** `_backups/2026-09-23/` (pendencias, estado). **Como desfazer:** restaurar os backups; reverter o Status da linha Notion `3af92372…` para `em execução`; arquivar as 2 linhas Notion novas (`3e492372…3070`, `3e492372…192b`) e apagar os 2 cenários; `git checkout` nas 2 Skills.

**Achado de processo:** `py -3` aponta para um Python 3.13 quebrado; o `py -3.12` funciona.

---

## 24/09/2026 — Drenagem Contínua v2.4 (qui, 10:18–10:35) — Kelsen fecha LC 281 Art. 40; exames de Lelé e Villaça administrados

**Portão (2.5):** 1 auto+aberta (`kelsen-hely-lc281-art40-unifamiliar-ap4`); 0 Skills novas (a Diária de hoje só corrigiu 2 já avaliadas); 2 linhas Notion `pendente` (NTN-2026-LELE-002, NTN-2026-VILLACA-001). Filtro rodado com `pendente` e `em execução`, como aprendido ontem. Acionados só Kelsen, Lelé e Villaça. Lúcio e Cardozo ficaram sem fila e não foram acionados.

**Kelsen (execução real):** acionou o Hely, que leu a LC 281 consolidada. Kelsen auditou contra o primário: **CONFERE**. O Art. 40 alcança unifamiliar em Barra/Recreio por texto expresso (Arts. 1º, 18 II, 12 §1º). Os acréscimos admitidos são +1 pavimento de cobertura até 50% (Art. 9º), a ampliação horizontal (Art. 12) e a legalização de até 1 pavimento (Art. 16 §2º III). O desconto parcelado do Art. 19 II não vale na AP4. Foram criados o R.7.1 no POP-LEGAL-02 (.md e .pdf regerado) e um complemento no `_indice_fontes.md`. Backup: `_backups/2026-09-24/kelsen_POP-LEGAL-02_R7_e_indice_Art40_ANTES.md`. Item resolvido. Um item novo, humano, foi aberto: `kelsen-lc281-art16-vs-art40-prazo-legalizacao`. Ele reúne o conflito de prazo de legalização (30/06 vencido x 01/12) e 3 dúvidas de interpretação para o Gate do Maurício.

**Exames (Loop 5.b.3, Wallenberg examinador):** as travas 1 (Recreio) e 2 (célula certa) ficaram limpas nos dois casos.
- **Lelé, NTN-2026-LELE-002 (Formação→Shadow):** o artefato `exame_NTN-2026-LELE-002_resposta.md` atende os 5 critérios do gabarito. Nenhum subagente foi despachado.
- **Villaça, NTN-2026-VILLACA-001 (Shadow→Assisted):** o artefato `exame_NTN-2026-VILLACA-001_resposta.md` atende os 5 critérios. O desconto foi devolvido ao Kelsen sem recálculo e ficou só como linha de sensibilidade rotulada.
- No Notion, as duas linhas passaram de `pendente` para `em execução`, com o resultado da auditoria. **Trava 3 pendente:** nenhuma promoção sem ratificação de Claudemberg na Semanal.
- `auditoria_lele.json`: entrada `aguardando_trava3` adicionada. As métricas não foram incrementadas porque o progresso só conta depois das 3 travas.

**Painel:** não tocado. Nenhuma capacidade mudou: exame sem ratificação não é promoção, e um complemento de POP não é ferramenta nova. **Learning Agent:** não rodou (quinta-feira). **7.5:** não se aplica.

**Como desfazer:** restaurar `_backups/2026-09-24/pendencias_ANTES_drenagem.json` e `auditoria_lele_ANTES.json`; restaurar o trecho do POP-LEGAL-02 e do índice a partir do backup do Kelsen; voltar as linhas Notion `3e492372…3070` e `3e492372…192b` para `pendente`.

---

## 25/09/2026 — Rotina Diária Skills v3.2, fluxo de SEXTA (Passos 6, 7, 9 e 10) — rodada automática

**Dia confirmado:** `(Get-Date).DayOfWeek` = Friday. Não houve pesquisa de Skill nova (Passos 1-4 são de seg-qui).

**Passo 6, Painel (`feed.jsonl`):**
- **Correção de dados:** 2 eventos de 23/09 (Landell NBR 14565 e LC 301 v1.1) estavam fora do schema. Tinham `d` = "23/09/2026", `et` = `skill_proposta`/`skill_correcao` (tipos inválidos) e o Gestor no campo `p`, com a descrição em `rec`. Por isso o Painel mostrava "Cardozo / Landell" como texto do evento. As 2 linhas foram normalizadas: `d` = "23/09", `et` = `skill`/`correcao`, `who` = Gestor e `p` = descrição. O conteúdo não mudou.
- **4 eventos novos** via `Append-STTKLog.ps1`, os 4 com OK: LC 281 Art. 40 (24/09, decisão); exames Lelé/Villaça aguardando a trava 3 (24/09, decisão); resumo da semana 21-25/09 (decisão); Dashboard 25/09 (sistema).
- **Não feito:** `<span id="updated">` do HTML está parado em 11/09 e ainda diz "15 membros". A tarefa agendada proíbe editar o HTML; o arquivo de referência (6.c) manda atualizar a data. Há conflito entre as duas fontes, então a decisão fica com Claudemberg.

**Passo 7, Learning Agent:** 2 vídeos assistidos de verdade (`/watch`, transcrição por legenda; o yt-dlp funcionou hoje): "Build a Self Improving Claude Knowledge Base" (youtube.com/watch?v=0-QDPnEIkvw) e "Claude Knowledge Base + Scheduled Loop" (youtube.com/watch?v=VUCChmNYpKU). Os dois aplicam o "LLM Wiki" de Karpathy: pasta de fontes brutas, wiki sintetizada, um índice (mapa) que a IA lê primeiro, e uma tarefa agendada que integra o material novo ao mapa **e liga cada item aos já existentes**. **Técnica aplicável:** uma passada semanal de "lint" das Skills, que procura duplicata no índice, contradição entre Skills irmãs, referência cruzada faltando e estatística velha. Rodei a passada uma vez hoje, só leitura, e ela achou 4 problemas reais (ver Passo 10). **Implementado no SKILL.md: NÃO.** Fica como proposta, porque mexer na rotina exige atualizar os 3 locais de execução (SKILL.md, Checklist_Sexta e prompt da tarefa agendada) e a regra de ritmo pede alinhamento antes. Proposta: incluir o "Lint semanal de Skills" no fluxo de sexta.

**Passo 9 e 10, Dashboard e Análise:** ver o fechamento em `01_CEO/rotina_fechamento_template.md` (entrada 25/09).

**Achado de governança (importante):** desde 10/09 a Rotina Diária **não registra nada neste livro-razão**. As entradas de 15 a 24/09 são só da Drenagem, de Villaça e das Reuniões. A causa: o prompt da tarefa agendada (v3.2) não menciona o livro-razão em nenhum passo, embora a Regra de Governança o torne obrigação inegociável. As Skills de 15 a 24/09 estão rastreáveis por `indice.md`, pelo fechamento, pelo feed e pelos commits, mas não têm "como desfazer" escrito aqui. Não corrigi o prompt da tarefa agendada, por ser mudança de governança da rotina. **Pendente decisão de Claudemberg.**

**Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-25/` (`feed_ANTES.jsonl`, `Setembro_ANTES.md`, `rotina_fechamento_template_ANTES.md`).

**Como desfazer:** copiar `feed_ANTES.jsonl` por cima de `01_CEO/Painel_Fundador/feed.jsonl`. Isso desfaz a normalização das 2 linhas de 23/09 e os 4 eventos novos. Restaurar os outros 2 arquivos a partir dos backups de mesmo nome.

**Aguardando:** ☐ RATIFICADO

---

## 28/09/2026 — Rotina Diária Skills v3.2 (seg, 08:38) — 2 Skills ativadas (Saturnino e Kelsen), Lúcio sem Skill

**Dia confirmado:** `(Get-Date).DayOfWeek` = Monday. Pipeline linear seg-qui. Foco: Barra/Recreio.

**O que decidi e por quê:**
- **Saturnino, `reservatorio-retardo-decreto23940-aguas-pluviais-rj` (v1.1, ativa-com-ressalva).** Lacuna real: nenhuma Skill cobria a obrigação municipal de reservatório de retardo, que condiciona o Habite-se e pesa na Barra (baixada, lençol raso). Decreto 23.940/2004 e Res. Conj. 001/2005 lidos no texto primário. Cardozo validou: PROCEDE COM RESSALVA, com 4 correções (C1: arranjo "retardo embaixo" contradizia o Art. 12 IV e o Art. 14 §2º; C2: quem assina o Termo; C3: "área impermeabilizada acrescida"; C4: marca de fonte secundária no checklist) e 7 ressalvas, todas aplicadas.
- **Kelsen, `varandas-nao-computaveis-ate-to-coes-lc198-rj` (v1.1, ativa-com-ressalva).** Brecha válida: varanda residencial em balanço ou reentrante não entra na ATE nem na TO (COES Art. 8º §4º). Kelsen conferiu no consolidado oficial da SMU (07/01/2026): o Art. 8º não tem alteração. Acrescentou o Dec. 45.917/2019 Art. 6º (5 m entre varandas em grupamento) e as ressalvas R2 (reentrante > 1,50 m vira prisma) e R3 (brise fora da varanda). R1 continua aberta: regra própria de cômputo na Barra/Recreio sob a LC 270/2024.
- **Lúcio: sem Skill.** Existe a lacuna de especificação de vidro (fator solar, fachada poente), mas nenhuma fonte trouxe número. Não se força.

**Achado colateral:** a Skill de partido de Lúcio (16/09, linhas 70-72) aplica ao residencial o limite de 20% que o COES só dá ao não residencial. Não editei o arquivo: a correção é de Lúcio.

**O que alterei:** 2 arquivos novos em `Skills_Propostas/2026/Setembro/` e 2 pastas novas em `.claude/skills/`; `indice.md` (nova seção 28/09); `feed.jsonl` (2 eventos); `rotina_fechamento_template.md`; este livro-razão.

**Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/` (`indice.md`, `Setembro_ANTES.md`, `rotina_fechamento_template_ANTES.md`).

**Como desfazer:**
1. Apagar as pastas `.claude/skills/reservatorio-retardo-decreto23940-aguas-pluviais-rj/` e `.claude/skills/varandas-nao-computaveis-ate-to-coes-lc198-rj/`.
2. Apagar os 2 `.md` novos em `Skills_Propostas/2026/Setembro/` (`saturnino_reservatorio-retardo-...` e `kelsen_varandas-nao-computaveis-...`).
3. Restaurar `indice.md` e `rotina_fechamento_template.md` a partir do backup.
4. Remover as 2 últimas linhas com `"d":"28/09"` do `feed.jsonl`.
5. Ou reverter o commit local desta rodada (`git revert`).

**Aguardando:** ☐ RATIFICADO

---

## 28/09/2026 — Reunião Semanal (quinzenal), rodada automática — pauta montada, Claudemberg ausente

**Pauta:** `04_REUNIOES_SEMANAIS/2026-09-28_pauta.md` (+ PDF). 6 itens de ratificação (R1-R6), 7 decisões dele (D1-D7) e 1 decisão de consumo (teto de 30 KB para os arquivos de estado).

**Correções registradas na pauta:** as pautas de 21 e 22/09 tinham 3 erros. (1) A Skill LC 301 foi dada como "instalada"; nunca foi, e o Kelsen deu NÃO PROCEDE em 23/09. (2) A promoção do Villaça a Shadow aparecia como pendente; foi aprovada ao vivo em 18/09. (3) A correção da v3.0 aparecia como pendente; foi ratificada em 14/09. Os três itens saíram da pauta.

**O que alterei:** criei a pauta e o PDF; reescrevi os JSON e relatórios de `token_tracking` com os scripts de medição; acrescentei esta entrada.

**Como desfazer:** apagar `2026-09-28_pauta.md`/`.pdf` e esta entrada. Os JSON de medição se regeneram a cada execução.

**Aguardando:** ☐ RATIFICADO (silêncio não é ratificação; tudo volta na próxima quinzenal)


---

## 28/09/2026 — Ajustes nas rotinas decididos por Claudemberg (sessão ao vivo, após auditoria da semana 21-25/09)

**O que decidiu e por quê:** a auditoria mostrou que as 3 rotinas rodaram todos os dias, mas com 6 falhas. Claudemberg decidiu:
1. **Livro-razão obrigatório na Diária.** O prompt da tarefa agendada não tinha esse passo desde 10/09. Agora está no Passo 4.6, sincronizado nos 3 lugares: tarefa, referência e Checklist.
2. **Rótulos de versão corrigidos.** Diária v3.4.0; Drenagem v2.4.2; referências cruzadas acertadas; títulos das tarefas atualizados.
3. **PDFs.** O CronJob continua gerando PDF de Skill. A Diária faz o commit deles na manhã seguinte. O texto v3.1 dizia que o CronJob tinha parado, e isso era falso.
4. **Topo do Painel automático.** O HTML agora lê o evento `et: "status"` mais recente do `feed.jsonl`. A Diária de sexta grava esse evento, e ninguém edita mais o HTML. O primeiro evento `status` foi gravado hoje.
5. **Permissões.** `settings.local.json` agora libera `cp`, `mkdir -p`, `Copy-Item`, `New-Item -ItemType Directory`, a limpeza de pastas em Temp, `git commit` e `git status`.
6. **LC 301 arquivada.** Kelsen deu parecer "não procede" em 23/09. Nova regra: esse parecer arquiva a Skill na hora, na Diária e na Drenagem.
7. **Promoções ratificadas (trava 3):** Lelé Formação→Shadow (NTN-2026-LELE-002) e Villaça Shadow→Assisted (NTN-2026-VILLACA-001).
8. **Fundações harmonizadas.** A `nbr6122-2019-fundacoes` dizia "2 sondagens é o mínimo usual" e agora remete à NBR 8036 (mín. 2 até 200 m², mín. 3 entre 200 e 400 m² de projeção). A de Barra/Recreio ganhou o bloco "Relação com outras Skills" como complemento local. Nova regra permanente de coerência: uma Skill complementa, é diferente ou substitui (vale a mais atualizada), e contradição não resolvida bloqueia a ativação.
9. **Treino em caso fictício.** Toda Skill ativada é treinada pelo Agente dono num mini-caso fictício de Barra/Recreio. O Dashboard mede "treinadas" ao lado de "usadas em caso real".

**O que alterou:**
- Tarefas agendadas `wallenberg-rotina-diaria-skills-v2-7` e `wallenberg-drenagem-continua-local`.
- `01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md` (v3.4.0) e `01_CEO/wallenberg-drenagem-continua-v2_SKILL.md` (v2.4.2, adendo J.7).
- `Checklist_Diaria.html`, `Checklist_Sexta.html` e `Painel_Fundador/painel_fundador_sttk.html` (topo lido do feed).
- `feed.jsonl` (3 eventos).
- `.claude/agents/lele.md`, `villaca.md`, `_estado_lele.md` e `_estado_villaca.md`.
- `.claude/skills/nbr6122-2019-fundacoes` e `fundacoes-solos-moles-lencol-freatico-barra-recreio`.
- LC 301 movida para `Skills_Propostas/_Arquivadas/2026/` e `indice.md` de setembro.
- `.claude/settings.local.json`.

**Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/` (sufixos `_pre-ajustes`, `_pre-promocao`, `_pre-harmonizacao`, `_pre-status-automatico`).

**Como desfazer:** copiar de volta cada arquivo do backup; para a LC 301, mover de `_Arquivadas/2026/` para `Skills_Propostas/2026/Setembro/`; para o Painel, restaurar `painel_fundador_sttk_pre-status-automatico.html`; as permissões novas são as últimas 10 linhas do `allow` em `settings.local.json`.
---

## 29/09/2026 — Rotina Diária Skills v3.4.0 (ter, 08:14) — 2 Skills novas ativadas + 4 treinos + 2 Skills corrigidas

**O que decidi e por quê:**
1. **Treinos atrasados de 28/09 (Passo 0.5).** As Skills de 28/09 (reservatório de retardo e varandas) foram ativadas antes da regra do treino e estavam sem ele. Treinei as duas primeiro: Saturnino e Hely deram OK.
2. **Reservatório v1.1 → v1.2.** Apliquei os 4 esclarecimentos do treino: o limiar é por área (unifamiliar não é dispensada); o reuso voluntário fica a confirmar com Kelsen; a lista de áreas sem definição conta pelo lado conservador; e a description foi ajustada. Nenhuma regra mudou. **As correções sugeridas no treino de varandas não foram aplicadas**, porque exigem leitura do COES (caput e §10) e da LC 145/2014 antes. Ficaram como pendência de Kelsen.
3. **Skill nova, Cardozo/Baumgart:** `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` v1.1. Fonte primária lida: Lei 5.234/2008 (ALERJ). Parecer de Cardozo: PROCEDE COM RESSALVA (R1-R4). Checagem de coerência: complementa `fundacoes-...-barra-recreio`, `nbr16783`, `nbr9575` e `nbr6122`; é diferente de `reservatorio-retardo`. Ativa-com-ressalva e instalada.
4. **Skill nova, Lúcio/Oscar:** `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj`. Fonte primária lida: Portaria Inmetro 309/2022, Anexo II. Parecer de Lúcio: PROCEDE COM RESSALVA (R1-R3). Ele corrigiu uma contradição com a Skill de proteção solar: no poente, sombreamento vertical, não só a varanda. Complementa 5 Skills. Depois do treino do Oscar (OK), subiu para v1.2 com 4 itens de checklist. Ativa-com-ressalva e instalada.
5. **Remissões de volta:** a linha 129 da Skill de fundações da Barra passou a apontar para a de rebaixamento, e a seção 6 da Skill de proteção solar para a de vidro. As duas foram alteradas na proposta e na instalada.
6. **Kelsen sem Skill.** O achado Decreto 50.473/2026 (SELCA) ficou como pendência para Hely.

**O que alterei:**
- **Novos:** `01_CEO/Skills_Propostas/2026/Setembro/baumgart_rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio.md`, `lucio_vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj.md`, `.claude/skills/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio/` e `.claude/skills/vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj/`
- **Editados (proposta e instalada):** `saturnino_reservatorio-...` e a Skill instalada correspondente (v1.2); `baumgart_fundacoes-...-barra-recreio`, linha 129; `lucio_protecao-solar-externa-dispositivos-rj`, seção 6
- **Índice:** `indice.md` de setembro, com a seção 29/09 e as marcas de treino nas linhas de 28/09
- **Feed:** `feed.jsonl` (2 eventos `skill`)
- **Registros de treino (4):** em `Gestores/{Cardozo,Kelsen,Lúcio}/Casos_TESTE/treino_skills/2026-09-29_*.md`

**Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-29/` contém `indice_setembro.md`, `reservatorio_SKILL.md`/`_proposta.md`, `fundacoes-barra_SKILL.md`/`_proposta.md`, `protecao-solar_SKILL.md`/`_proposta.md` e `livro-razao_Setembro.md`.

**Como desfazer:**
- **Skills novas:** apagar `.claude/skills/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio/` e `.claude/skills/vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj/`, e voltar o `status` dos dois `.md` em `Skills_Propostas` para `proposta`.
- **Edições nas Skills existentes:** copiar de volta os 6 arquivos do backup (`reservatorio`, `fundacoes-barra`, `protecao-solar`, cada um em `_SKILL` e `_proposta`) para os caminhos de origem.
- **Índice:** restaurar `indice_setembro.md`.
- **Feed:** remover as 2 linhas `"d":"29/09"` do `feed.jsonl`.

**Aguardando:** ☐ RATIFICADO (revisão retroativa na Semanal)

**Adendo (fim da rodada 29/09):** os 2 treinos das Skills novas deram OK. Baumgart barrou 7 de 7 iscas; Oscar barrou 6 de 6. As duas Skills subiram para a **v1.2** só com itens de checklist sugeridos no treino (rebaixamento: sondagem abaixo da argila, ruptura de fundo por cisalhamento e deformação da contenção, vistoria também em contenção estanque, flutuação de piscina vazia; vidro: piso de FS 0,20, recusa de sombreamento registrada, TL × COES, etiqueta A/B não sai pelo prescritivo). Nenhuma regra mudou. **Como desfazer a v1.2:** remover o bloco "Verificações acrescentadas pelo treino" (rebaixamento) e os 4 trechos marcados v1.2 no changelog (vidro), e recopiar para `.claude/skills/`.


---

## 29/09/2026 — Acervo de normas reorganizado + 2 rotinas novas (decisão de Claudemberg ao vivo)

**O que decidiu e por quê:** os PDFs de normas estavam espalhados em 5 lugares, com duplicatas (NBR 6492 ×4, COE ×4). Claudemberg aprovou as 5 recomendações:
1. A legislação continua na pasta do Hely.
2. `D:\009_NORMAS` foi incorporada à 008.
3. Versão antiga vai para Substituídas, nunca é apagada.
4. Duas rotinas novas.
5. Lista de compra.

**O que alterou:**
- **Nova estrutura de `D:\008_Normas ABNT\`:**
  - pastas `001_ABNT` (com 01 a 05 por disciplina), `002_Prefeitura_RJ`, `003_Condominios` e `004_Substituidas`;
  - arquivos renomeados no padrão `NBR NNNNN-AAAA Título`;
  - índice novo `_indice_acervo.md`;
  - `D:\009_NORMAS` e `010_Regras Prefeitura` removidas depois de ficarem vazias;
  - folheto de telha movido para `D:\007_MATERIAIS`; página web salva e guia do MS movidos para `D:\005_CONHECIMENTO\0002_PROJETOS`.
- **Substituídas:** NBR 6492-1994, extrato da 6492-2021 e NBR 15220-3-2005 (nela o Rio era ZB 8).
- **Achados:**
  - a NBR 9050 do acervo é de 2015, desatualizada;
  - a NBR 13532-1995 possivelmente foi substituída pela NBR 16636;
  - o projeto de revisão da NBR 15220-3 (jun/2024) põe o Rio em ZB 4A.
- **Rotinas criadas:**
  - `wallenberg-rotina-acervo-normas`: toda segunda às 07:00, dona Kelsen/Hely; baixa só o que é gratuito e oficial e mantém os índices e a lista de compra;
  - `wallenberg-rotina-macetes-profissionais`: seg-sex às 14:00; no máximo 1 Skill por Gestor por dia; /watch de verdade; o Gestor valida e o Agente treina em caso fictício.
- **Skills corrigidas hoje:**
  - COE v1.2 (Oscar/Lúcio);
  - LICIN Barra/Recreio v1.2 (Hely/Kelsen);
  - nbr14565 v1.3, nbr5410 v1.1 e nbr5626-8160 v1.2 (Landell/Saturnino/Cardozo, contra os PDFs reais).

**Backup:** nenhum arquivo foi apagado; tudo foi só movido e renomeado. Backups das Skills em `_backups/2026-09-29/`.

**Como desfazer:**
- **Pastas:** mover os arquivos de volta seguindo a tabela do `_indice_acervo.md`.
- **Rotinas:** desativar pelo painel Agendadas (ou `update_scheduled_task enabled:false`).
- **Skills:** restaurar pelos backups.

---

## 29/09/2026 — Rotina de Macetes de Profissionais v1.0 (1ª rodada, autônoma, 18:09)

**O que foi feito:** 8 macetes com fonte entraram em 2 Skills. Os dois Gestores validaram e os dois treinos deram OK.

- **lucio-protecao-solar-externa-dispositivos-rj, v1.2 → v1.3 (validação de Lúcio):**
  - M1: mancha de temperatura em duas cartas semestrais (Lamberts, Dutra e Pereira, *EEA* 3ª ed., pp. 135-136);
  - M2: brise misto, com parte fixa e parte móvel (idem, p. 136);
  - M3: ajuste ângulo a ângulo, com γ/α (Marcelo Nudel, Ca2/ex-Arup, vídeo Rb5tB_Wiphs, 29:43–30:11, assistido com /watch via Whisper; a legenda deu 429);
  - M4: lâmina microperfurada (Hunter Douglas, fichas AECweb, tipo B).
  - Treino do Oscar: OK. Ele passou um pouco das 15 linhas e não atualizou o próprio estado; Lúcio vai cobrar.
- **nbr9575-impermeabilizacao, → v1.1 (validação de Cardozo):**
  - M1: tela de reforço entre demãos (MC-Bauchemie e Votorantim);
  - M2: preparo da base;
  - M3: teste de 72 h e proteção mecânica;
  - M4: sistema rígido só onde não há movimentação. Cardozo restringiu o "box" ao térreo, porque sem isso o macete contradizia a Skill.
  - Caimento de 0,5% da ficha: não entrou.
  - Treino do Saturnino: OK. Pendência que ele apontou: nicho e soleira de transição.
- **varandas (Kelsen): nenhum macete.** As fontes A e B foram tentadas e nada tinha autor ou conteúdo verificável. A Skill volta à frente da fila.
- **Fontes arquivadas** em `01_CEO\Skills_Propostas\_macetes_fontes\2026-09-29\`. **Fila criada** em `01_CEO\Skills_Propostas\_macetes_fila.md`.
- **Fontes tipo A em impermeabilização:** só apareceram vídeos de canais sem autor identificável, que não contam.

**Backup:** `_backups/2026-09-29/*_pre-macetes.md` (4 arquivos).

**Como desfazer:**
1. Copie cada `*_pre-macetes.md` de volta para o arquivo de origem:
   - `.claude/skills/<skill>/SKILL.md`;
   - a cópia em `Skills_Propostas/2026/Setembro/`.
2. Apague os 2 treinos `2026-09-29_macete_*`.
3. Reverta as linhas de 29/09 em `_estado_lucio.md` e `_estado_cardozo.md`.
