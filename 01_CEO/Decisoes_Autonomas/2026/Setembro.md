# Livro-Razão de Decisões Autônomas — Setembro/2026

Registro de tudo que o Wallenberg decidiu e executou **sem aprovação prévia** de Claudemberg, sob o modelo de ratificação posterior instituído em 20/07/2026 (ver regra de ouro no `CLAUDE.md`). Continuação de [Agosto/2026](Agosto.md).

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
