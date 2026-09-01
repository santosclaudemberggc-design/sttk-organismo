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

### 24/08/2026 — Revit MCP 138 Tools (LuDattilo)

- **O que é:** conector MCP para Revit 2026, 138 tools, natural language em português.
- **O que o Vitruvius não cobre hoje:** não auditado ponto a ponto ainda contra as 23 tools atuais do Vitruvius — pendência.
- **Decisão:** **monitorar** — candidato mais próximo em maturidade ao Vitruvius (mesma geração 2026), mas nunca comparado tool-a-tool. Decisão pendente de Wallenberg/Cardozo desde 26/08 (ver livro-razão 26/08, "sobreposição Revit MCP 138 tools vs. Vitruvius").
- **Fonte:** `01_CEO/Skills_Propostas/2026/Agosto/skill_revit_mcp_138tools.md`

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
- **O que o Vitruvius não cobre hoje:** o Vitruvius (23 tools produção) expõe um subconjunto curado da API Revit. O RevitMCPBridge2026 expõe a API inteira sem curadoria — abordagem oposta (amplitude vs. curadoria). A base de 113 arquivos de conhecimento arquitetônico é ativo sem equivalente no Vitruvius.
- **Comparação rápida contra achados anteriores:** mais endpoints que shuotao (173 tools), LuDattilo (138 tools), Demolinator (48 tools). Porém "endpoint" ≠ "tool MCP curado" — muitos endpoints podem ser raw API calls sem prompt engineering.
- **Decisão:** **avaliar incorporação parcial** — NÃO é redundância. O RevitMCPBridge2026 expõe a **API inteira** (705+ endpoints em 25+ categorias, 146 arquivos C#) enquanto o Vitruvius é curado (~23 tools). Abordagem oposta: amplitude vs. curadoria. Risco: amplitude sem curadoria gera inconsistência (AI confusa com 705 opções). PORÉM: (a) os 113 arquivos de knowledge base (boas práticas BIM, SOPs) agregam **independente do conector** — devem virar Skill para Oscar; (b) named pipes (mecanismo do RevitMCPBridge) vs. Vitruvius: **PRECISA TESTAR COMPATIBILIDADE** antes de considerar coexistência no mesmo Revit — se não há conflito, o RevitMCPBridge é candidato a "extensão de amplitude" do Vitruvius (coexistem: 23 tools curados Vitruvius + 705 endpoints brutos RevitMCPBridge para casos que não se encaixam nos 23).
- **Próximo passo:** Lúcio/Oscar: (1) Extrair e redigir os 113 arquivos como Skill de knowledge de BIM; (2) Testar se named pipes + Vitruvius rodam no mesmo Revit sem conflito; (3) Se testes OK, propor ao mantenedor do Vitruvius: "posso manter esse conector como fallback para amplitude além dos 23 tools curados?".
- **Fonte:** https://github.com/WeberG619/RevitMCPBridge2026 — verificado 01/09/2026

---

## Como usar este arquivo

- **Rotina diária (Passo 1/Passo 8):** antes de criar uma Skill nova sobre qualquer conector/plugin/IA que toque Revit ou BIM, adicione a entrada aqui primeiro. Se decidir "avaliar incorporação" ou "monitorar", a Skill de usabilidade correspondente ainda é criada normalmente em `Skills_Propostas` — este arquivo é o índice que amarra todos os achados de Revit/BIM entre si, para que a pergunta "isso ajuda o Vitruvius?" seja sempre feita, não só quando o achado parecer óbvio.
- **Lúcio/Oscar:** revisar este arquivo periodicamente (proposto: a cada Reunião Semanal em que Arquitetura estiver na pauta) para decidir se algum "avaliar incorporação" vira ação real.
- **Nunca descartar por omissão:** todo achado aqui tem decisão explícita e motivo — "não vi relação" não é decisão válida, precisa dizer o que foi comparado e por quê não serve.
