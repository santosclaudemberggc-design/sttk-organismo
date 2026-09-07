---
name: vitruvius-achados-candidatos
description: "Log contínuo de todo achado relacionado ao Vitruvius/Revit-MCP encontrado pela rotina diária — candidatos a agregar ao Vitruvius, nunca descartados por padrão"
metadata:
  type: rastreamento_continuo
  dono: Oscar (equipe de Lúcio) — mantido pela rotina diária do Wallenberg
  criado: 2026-08-27
  instrucao_origem: "Claudemberg, 27/08/2026 — 'nosso Vitruvius tem que ser completo então tudo que tenha relação com ele é bem-vindo para vermos se agrega ou não'"
---

# Achados Candidatos ao Vitruvius

**Regra:** qualquer achado de pesquisa (Passo 1 ou Passo 8 da rotina diária) que toque Revit/BIM via MCP, IA, plugin ou automação — mesmo que pareça "concorrente" do Vitruvius — entra **aqui primeiro**, antes de virar Skill isolada de "alternativa". O Vitruvius é o motor de produção real do Oscar; o objetivo não é substituí-lo, é engordá-lo. Nada aqui é descartado sem registro do motivo.

Para cada achado: **o que é**, **o que o Vitruvius já cobre ou não cobre disso hoje**, **decisão** (avaliar incorporação / monitorar / descartado, com motivo), **fonte**.

---

## Achados

### 27/08/2026 — Revit MCP Study (shuotao) — 173 tools + 76 SOPs BIM

- **O que é:** conector comunitário MCP para Revit 2023-2026 via npm (`@shuotao/revit-mcp-server`), 173 tools cobrindo design/clash detection/documentação/MEP/QTO + 76 arquivos de SOP (Standard Operating Procedures) de BIM profissional (código de edificações, verificações de conformidade).
- **O que o Vitruvius não cobre hoje:** o Vitruvius atual (23 tools em produção, listado no frontmatter do Oscar) não tem clash detection nem QTO (Quantity Take-Off) documentados; as 76 SOPs BIM são um ativo de conhecimento estruturado que o Vitruvius não tem equivalente.
- **Decisão:** **avaliar incorporação parcial** — não trocar o Vitruvius pelo shuotao inteiro (risco de trocar ferramenta já em produção por uma "study"/experimental), mas mapear se (a) as 76 SOPs podem virar Skill de conhecimento para o Oscar independente do conector, e (b) as funções de clash detection/QTO têm equivalente no roadmap do Vitruvius antes de julgar necessário importar de outro conector.
- **Próximo passo:** Lúcio/Oscar avaliam se vale abrir uma issue/pedido ao mantenedor do Vitruvius (se for projeto ativo) pedindo essas 2 funções, em vez de rodar 2 conectores MCP simultâneos no mesmo Revit (risco de conflito de conexão exclusiva, já documentado no Skill correspondente).
- **Fonte:** [github.com/shuotao/REVIT_MCP_study](https://github.com/shuotao/REVIT_MCP_study) — Skill completa em `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_revit-mcp-study-173tools-shuotao.md`

### 24/08/2026 — Revit MCP 138 Tools (LuDattilo) — **atualizado 04/09/2026**

- **O que é:** conector MCP para Revit 2023-2027 (`LuDattilo/revit-mcp-server`), 138 tools MCP (README anuncia "80+"), MIT, 51 stars, 140 commits — desenvolvimento ativo confirmado em 04/09.
- **Detalhe técnico confirmado (04/09):** 6 categorias operacionais — Projeto/Modelo Info (metadados, views, seleção), Análise/Auditoria de Modelo (health score, **clash detection**, consultas espaciais), Materiais/Quantitativos (takeoff), Criação de Elementos (paredes, pisos, salas, grids, arrays), Modificação (parâmetros, tipos, overrides gráficos), Exportação (PDF/DWG/IFC/CSV, schedules). Painel de chat integrado com API Anthropic (extended thinking 10K tokens) dentro do próprio Revit. Windows apenas, Node.js 18+, porta 8080 fixa, documento único ativo, sem agrupamento de undo para lotes de IA.
- **O que o Vitruvius não cobre hoje:** clash detection e health score de modelo, quantitativos (QTO) e exportação IFC/CSV em lote — mesma lacuna já identificada no achado shuotao (173 tools, 27/08).
- **Decisão:** **avaliar incorporação parcial** — dado técnico agora suficiente para decisão (antes "monitorar" por falta de detalhe). Mais maduro que Demolinator (48, descartado) mas ainda sem comparação tool-a-tool formal contra os 35 tools do Vitruvius em produção. Prioridade sobe frente a shuotao/BIMwright por ter integração de chat nativa Anthropic já pronta.
- **Próximo passo:** Lúcio/Oscar decidem se vale testar coexistência (porta 8080 fixa pode colidir com outro conector já testado nesse endereço) antes de qualquer piloto.
- **Fonte:** `01_CEO/Skills_Propostas/2026/Agosto/skill_revit_mcp_138tools.md` | https://github.com/LuDattilo/revit-mcp-server — reverificado 04/09/2026

### 23/08/2026 — Revit MCP 48 Tools (Demolinator)

- **O que é:** primeiro conector MCP mapeado pela rotina, 48 tools, Revit 2024-2027.
- **Decisão:** **descartado como candidato ativo** — superado em tooling pela versão de 138 tools (LuDattilo, mesma família conceitual) encontrada um dia depois. Mantido só como registro histórico.
- **Fonte:** `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_revit-mcp-48-tools-natural-language.md`

### 06/08/2026 — MCP oficial da Autodesk (Fusion/Revit/InfoWorks)

- **O que é:** MCP de 1ª parte da própria Autodesk, anunciado na DevCon 2026, tech preview.
- **O que o Vitruvius não cobre hoje:** é suporte oficial do fabricante vs. o Vitruvius (comunitário) — diferença de sustentabilidade de longo prazo, não de função.
- **Decisão:** **monitorar** — sem preço, sem maturidade de produção ainda. Comparar com o Vitruvius quando sair do tech preview.
- **Fonte:** `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_mcp-oficial-autodesk-fusion-revit-infoworks.md`

### 01/09/2026 — RevitMCPBridge2026 (WeberG619) — 705+ endpoints + 113-file knowledge base

- **O que é:** ponte open source entre IA (MCP client) e Revit 2026 via named pipes. Expõe a Revit API inteira através do MCP com 705+ endpoints (não tools MCP — endpoints da API Revit acessíveis). Inclui base de conhecimento arquitetônico de 113 arquivos. Repositório ativo, alternativa mantida pelo autor.
- **O que o Vitruvius não cobre hoje:** o Vitruvius tem **35 tools MCP curados** em produção (`.claude/agents/oscar.md`, linha 4: change_type, create_door/elevation/floor/grid/level/opening/room/schedule/section/sheet/wall/window, delete_element, dimension_facade/room/wall, find_elements, get_element/model_info, list_categories/element_types/elements/levels/rooms, move_element, place_view_on_sheet, resize_wall, revit_status, set_parameter/set_parameters_batch, tag_rooms). O RevitMCPBridge2026 expõe a API inteira (705+ endpoints) sem curadoria — abordagem oposta (amplitude extrema vs. curadoria extrema). A base de 113 arquivos de conhecimento arquitetônico é ativo sem equivalente no Vitruvius.
- **Comparação rápida contra achados anteriores:** mais endpoints que shuotao (173 tools), LuDattilo (138 tools), Demolinator (48 tools). Porém "endpoint" ≠ "tool MCP curado" — muitos endpoints podem ser raw API calls sem prompt engineering.
- **Decisão:** **avaliar incorporação parcial** — NÃO é redundância. O RevitMCPBridge2026 expõe a **API inteira** (705+ endpoints em 25+ categorias, 146 arquivos C#, 13.000+ linhas) enquanto o Vitruvius tem 35 tools curados. Abordagem **extremamente oposta**: amplitude radical (705+) vs. curadoria radical (35). Risco de coexistência: 705+ opções podem confundir o AI vs. clareza dos 35. Porém, complementares se compatíveis. (a) Os 113 arquivos de knowledge base (boas práticas BIM, SOPs) agregam **independente do conector** — devem virar Skill para Oscar; (b) Named pipes (mecanismo RevitMCPBridge) vs. Vitruvius: **PRECISA TESTAR COMPATIBILIDADE** (ambos usam named pipes? há conflito de conexão exclusiva?) antes de considerar coexistência no mesmo Revit. (c) SE testes OK, o RevitMCPBridge é candidato a **complemento** do Vitruvius (35 curados para padrão + 705 brutos para exceções).
- **Próximo passo:** Lúcio/Oscar: (1) Extrair e redigir os 113 arquivos como Skill de BIM knowledge; (2) **TESTAR: named pipes + Vitruvius no mesmo Revit — há conflito de comunicação?**; (3) Se testes OK, propor a Wallenberg: "manter RevitMCPBridge como fallback paralelo ao Vitruvius para casos fora do escopo dos 35 tools".
- **Fonte:** https://github.com/WeberG619/RevitMCPBridge2026 — verificado 01/09/2026

### 03/09/2026 — BIMwright/rvt-mcp — 229 tools, Revit 2022-2027, Apache-2.0

- **O que é:** ponte local entre MCP client (Claude, Cursor, Codex, etc.) e Revit via TCP (Revit 2022-2024, .NET Framework 4.8) ou Named Pipe (Revit 2025-2027, .NET 8/10). Oferece **229 tools** em modo completo (40 no modo padrão, expansível até 232 com bake adaptativo). Organizado em toolsets temáticos: Query (vistas, seleção, filtros, parâmetros), Create (grids, níveis, salas, elementos geométricos), View (criar vistas, sheets, capturar imagens), Meta (execução em lote, multi-Revit, envio de código C#), e opcionais: MEP, estrutural, anotações, materiais, geometria, links, parâmetros.
- **O que o Vitruvius não cobre hoje:** suporte a multi-Revit (rodar em mais de uma instância do Revit simultaneamente), envio de código C# arbitrário via MCP (o Vitruvius não expõe raw API), toolsets MEP/estrutural dedicados, bake adaptativo (o AI recebe só as tools relevantes ao contexto). 229 tools vs. 35 do Vitruvius — faixa intermediária entre o Vitruvius curado (35) e o RevitMCPBridge bruto (705+).
- **Comparação com achados anteriores:** mais tools que UV-Tech (40), Demolinator (48) e LuDattilo (138, original), menos que RevitMCPBridge2026 (705+). Porém é o mais maduro em CI/manutenção: **166 commits, 18 estrelas, 9 forks** — atividade sustentada. Apache-2.0 (licença mais permissiva que MIT para uso corporativo).
- **Compatibilidade Revit:** 2022-2027 — a mais ampla de todos os achados. Vitruvius suporta quais versões? (pendente de confirmação).
- **Decisão:** **avaliar incorporação parcial** — é o candidato mais equilibrado entre amplitude de tooling e maturidade de projeto. Testar coexistência com Vitruvius (Named Pipe no Revit 2025+ — mesmo mecanismo?). Se compatíveis, os toolsets opcionais (MEP, estrutural) podem ser ativados conforme a disciplina do Agente (Baumgart ativa estrutural, Landell ativa MEP).
- **Próximo passo:** Lúcio/Oscar: (1) confirmar se Vitruvius usa Named Pipe ou outro mecanismo; (2) se Named Pipe, testar se dois servidores MCP podem escutar no mesmo Revit; (3) avaliar bake adaptativo como modelo para curar tools do Vitruvius por contexto.
- **Fonte:** https://github.com/bimwright/rvt-mcp — verificado 03/09/2026

### 03/09/2026 — UV-Tech/revit-claude-mcp — 40 tools, Revit 2026, MIT

- **O que é:** conector MCP para Revit 2026 com 40 ferramentas locais. Claude fala com um servidor Node.js MCP que se comunica com um addin Revit via HTTP local (localhost:6543). Cobre 5 áreas: Read (project info, levels, rooms, elements, families, views, sheets, parameters), Modify (criar paredes, posicionar famílias, definir parâmetros, mover/deletar), Export (PDFs, DWGs, IFCs, cronogramas), Audit (famílias, conteúdo não utilizado, importação de dados), Coordinate (detecção de clashes, exportação de relatórios HTML/CSV).
- **O que o Vitruvius não cobre hoje:** exportação direta de PDF/DWG/IFC via MCP (o Vitruvius exporta?), auditoria de famílias e conteúdo não utilizado, relatórios de clash em HTML/CSV. Mesma faixa de tools que o modo padrão do BIMwright (40).
- **Comparação com achados anteriores:** 40 tools é igual ao modo padrão do BIMwright, porém só Revit 2026 (vs. 2022-2027 do BIMwright) e com atividade muito inferior (5 commits, 2 stars, 0 forks). Arquitetura HTTP local vs. Named Pipe — pode ser mais simples de configurar, mas menos performante.
- **Decisão:** **monitorar** — projeto em estágio muito inicial (5 commits). Funcionalidades de export e audit são interessantes mas o BIMwright cobre as mesmas com mais maturidade. Se o UV-Tech evoluir, reavaliar.
- **Fonte:** https://github.com/UV-Tech/revit-claude-mcp — verificado 03/09/2026

### 07/09/2026 — IbrahimFahdah/revit-claude-mcp — 46 tools, extensivel, .NET 8

- **O que e:** conector MCP entre Claude AI e Revit via HTTP local (127.0.0.1:5578). 46 tools built-in cobrindo query, modificacao, exportacao e visualizacao. Instalavel via `.mcpb` (Claude Desktop extension). .NET 8 SDK, Revit 2026 para build (anuncia compatibilidade com "todas as versoes"). 22 stars, 3 forks, 67 commits — desenvolvimento ativo (curso gratuito publicado no LinkedIn pelo autor).
- **Diferencial:** modelo de extensibilidade via `Packages\` folder — usuarios publicam e compartilham tool packages customizados, adicionando funcoes sem alterar o core. Tres caminhos de contribuicao: melhorar os 46 tools, publicar pacotes custom, ou melhorar o plugin.
- **O que o Vitruvius nao cobre hoje:** o modelo de extensibilidade (pacotes plugaveis) e um conceito que o Vitruvius nao tem — mas as 46 tools em si cobrem funcoes ja presentes nos achados anteriores (LuDattilo 138, BIMwright 229).
- **Comparacao:** 46 tools e comparavel ao UV-Tech (40, monitorar) e ao modo padrao do BIMwright (40 padrao / 229 expandido). Porem o BIMwright cobre Revit 2022-2027 com 166 commits e Apache-2.0 — mais maduro. IbrahimFahdah se destaca pela extensibilidade, nao pela amplitude.
- **Decisao:** **monitorar** — 46 tools nao preenche lacuna nova vs achados existentes (BIMwright 229, LuDattilo 138). Extensibilidade via pacotes custom e interessante como conceito (Vitruvius poderia adotar modelo similar), mas nao justifica piloto agora. Reavaliar se o ecossistema de pacotes crescer.
- **Fonte:** https://github.com/IbrahimFahdah/revit-claude-mcp — verificado 07/09/2026

---

## Como usar este arquivo

- **Rotina diária (Passo 1/Passo 8):** antes de criar uma Skill nova sobre qualquer conector/plugin/IA que toque Revit ou BIM, adicione a entrada aqui primeiro. Se decidir "avaliar incorporação" ou "monitorar", a Skill de usabilidade correspondente ainda é criada normalmente em `Skills_Propostas` — este arquivo é o índice que amarra todos os achados de Revit/BIM entre si, para que a pergunta "isso ajuda o Vitruvius?" seja sempre feita, não só quando o achado parecer óbvio.
- **Lúcio/Oscar:** revisar este arquivo periodicamente (proposto: a cada Reunião Semanal em que Arquitetura estiver na pauta) para decidir se algum "avaliar incorporação" vira ação real.
- **Nunca descartar por omissão:** todo achado aqui tem decisão explícita e motivo — "não vi relação" não é decisão válida, precisa dizer o que foi comparado e por quê não serve.
