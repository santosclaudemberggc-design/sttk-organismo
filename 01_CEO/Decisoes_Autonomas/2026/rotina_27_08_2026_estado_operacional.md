---
name: rotina-27-08-2026-estado-operacional
description: "Organização refinada da Rotina Diária de 27/08/2026 — o que foi feito, o que falta, sequência exata de execução, como desfazer"
metadata:
  tipo: rotina_operacional
  data: 2026-08-27
  dono: Wallenberg (CEO)
  status: parcial — 5 de 8 passos completos, 3 blocos pendentes
---

# Rotina Diária Skills v2.0 — 27/08/2026 — Estado Operacional

**Sumário:** Pesquisa + consolidação + 2 Skills criadas. Correção estrutural de 2 políticas (Vitruvius + Cardozo dual-track). 3 passos finais pendentes (PDFs, Painel, Learning Agent). Sem bloqueadores críticos — tudo é sequencial e reversível.

---

## I. CONCLUÍDO (✅ Passos 1-4 + Correção Estrutural)

### Passo 1 — Pesquisa Externa
- **5 buscas paralelas:** Revit MCP estrutural, CAU-RJ resolução, landscape MCP, MEP hidrossanitário, WAN 2.2
- **WebFetches:** 3 repos GitHub (freecad-mcp, shuotao revit, WAN 2.2) + 2 WebSearches adicionais (Tekla, interior design)
- **Achados principais:** freecad-mcp (FEM), shuotao/REVIT_MCP_study (173 tools + 76 SOPs), WAN 2.2 confirmado Apache 2.0
- **Tempo gasto:** ~15-20 min (pesquisa + validação WebFetch)

### Passo 2 — Consolidação
- **Critério aplicado:** 4 critérios Passo 8 (custo zero, sem vazamento, sem malware, funcional)
- **Mapa de achados:**
  - Baumgart (Estrutural): **freecad-mcp ✅** — FEM com CalculiX, MIT, 46 tools, localhost
  - Oscar (Arquitetura): **shuotao REVIT_MCP_study ✅** — 173 tools + 76 SOPs BIM, npm, complementar ao LuDattilo
  - Portinari (Apresentação): sem achado novo
  - Cardozo (6 áreas): sem candidato MCP que passe nos 4 critérios (busca continua)
- **Descartados:** WAN 2.2 (já em Drenagem para Burle), Tekla (software base pago), landscape/MEP (sem candidato gratuito com MCP)

### Passo 3 — Redação de Skills
- **2 Skills criadas em `.md`:**
  1. `baumgart_freecad-mcp-fem-estrutural.md` — 46 tools, FEM/CalculiX, MIT, Python 3.13+, FreeCAD 1.1.1+, localhost
  2. `arquitetura_revit-mcp-study-173tools-shuotao.md` — 173 tools + 76 SOPs, npm, Revit 2023-2026, MIT, 100 stars/108 forks

**Estrutura padrão ambas:**
- Para qual Agente / Status (proposta) / O que faz / Como usa / Requisitos técnicos / Evidência segurança / Limitações / Fonte

### Passo 4 — Salvamento Local
- Ambas as Skills salvas em `01_CEO/Skills_Propostas/2026/Agosto/` (caminho correto)
- Índice (`indice.md`) atualizado com 2 novas linhas (27/08 — freecad-mcp + shuotao revit)

### Correção Estrutural (27/08 — Instrução ao vivo Claudemberg)

#### A. Arquivo de Rastreamento Vitruvius
- **Criado:** `01_CEO/Gestores/Lúcio (Arquitetura)/Agentes/Oscar/vitruvius_achados_candidatos.md`
- **Propósito:** todo achado Revit/BIM (plugin/conector/IA) entra aqui antes de virar Skill isolada — comparado contra Vitruvius (avaliar incorporação / monitorar / descartado + motivo)
- **Populado retroativo:** 4 achados existentes de Revit-MCP (48/138/173 tools + MCP oficial Autodesk) já indexados com decisão
- **Próximo:** novos achados de Oscar/Lúcio referem-se a este arquivo primeiro

#### B. Duas Trilhas de Pesquisa para Cardozo
- **Trilha A (Inteligência):** normas técnicas, técnicas de projetar, regras de projeto — qualquer fonte (ABNT, concessionária, livros, YouTube técnico)
  - Vira Skill de conhecimento técnico para o Agente
  - Passo 1 da rotina diária (pesquisa externa)
  - Para as 6 áreas: Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin

- **Trilha B (Ferramentas):** conector/software pronto no GitHub/MCP
  - Vira Skill de usabilidade de ferramenta
  - Passo 8 da rotina diária (busca dirigida)
  - Mesmas 6 áreas

- **Implementação:** Passo 1 e Passo 8 ambos rodam quando uma área de Cardozo é pesquisada — nunca uma no lugar da outra

#### C. Atualizações Documentais
- **Backup do SKILL.md:** `01_CEO/Decisoes_Autonomas/_backups/2026-08-27/wallenberg-rotina-diaria-skills-v2_SKILL.md`
- **SKILL.md atualizado (v2.4 → v2.5):**
  - Passo 1: adicionada diretriz Vitruvius + Trilha A (Cardozo)
  - Passo 8: rotulado como Trilha B (Ferramentas apenas)
  - Histórico de versões: nova entrada 2.5 (27/08/2026)

#### D. Memórias de Feedback
- **Criadas 2 novas:**
  - `feedback_vitruvius_completude_todos_achados.md` — Vitruvius deve ser "completo", todo achado BIM entra no rastreamento
  - `feedback_cardozo_pesquisa_dupla_inteligencia_ferramentas.md` — duas trilhas separadas, nunca uma no lugar da outra
- **MEMORY.md:** índice atualizado com ambas

#### E. Livro-Razão
- **Entrada em `01_CEO/Decisoes_Autonomas/2026/Agosto.md`:** tudo documentado com "como desfazer" (backup + arquivo reversível)

---

## II. PENDENTE (❌ Passos 5, 6, 7 + Fechamento)

### Passo 5 — Gerar PDFs
**Status:** bloqueado operacional, não técnico
**O quê:** regenerar PDFs de 3 arquivos (2 Skills novas + índice) usando script `md_to_pdf.py`

**Sequência exata:**
```bash
cd D:\000_ESTRUTURA\ DEPARTAMENTO\ DE\ PROJETO\_ferramentas
python md_to_pdf.py "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Skills_Propostas\2026\Agosto\baumgart_freecad-mcp-fem-estrutural.md"
python md_to_pdf.py "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Skills_Propostas\2026\Agosto\arquitetura_revit-mcp-study-173tools-shuotao.md"
python md_to_pdf.py "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Skills_Propostas\2026\Agosto\indice.md"
```

**Output esperado:** 3 PDFs gêmeos (`.pdf` ao lado de cada `.md`)

**Bloqueador histórico:** em 23/08, Edit tool de índice retornou "permission stream closed" — tentativa manual com script evita ferramenta Edit. Se falhar novamente, reporte como bug sistemático (não é falta de arquivo).

**Impacto se não rodar:** Skills documentadas mas sem PDF gêmeo (regra STTK: todo `.md` tem `.pdf` correspondente no mesmo dir). Padrão de referência é manter ambos.

---

### Passo 6 — Atualizar Painel do Fundador
**Status:** bloqueado técnico, não operacional
**O quê:** republicar `01_CEO/Painel_Fundador/painel_fundador_sttk.html` com 2 eventos novos no FEED

**Eventos a adicionar (PREPEND — mais recente no topo):**
```javascript
{d:"27/08",et:"agente",t:"Correção estrutural: Vitruvius rastreamento + Cardozo dual-track",who:"Claudemberg (ao vivo)",p:"2 políticas fixadas: (1) todo achado Revit/BIM passa por vitruvius_achados_candidatos.md antes de virar Skill isolada (Vitruvius deve ser completo); (2) pesquisa para as 6 áreas de Cardozo é dual-track — Trilha A (normas/técnicas, qualquer fonte) + Trilha B (ferramenta GitHub, Passo 8), nunca uma no lugar da outra. Arquivo de rastreamento criado. SKILL.md v2.5 + 2 memórias de feedback."},
{d:"27/08",et:"skill",t:"2 Skills novas — FreeCAD FEM (Baumgart) + Revit MCP 173 tools (Oscar)",who:"Wallenberg (rotina diária)",p:"Passo 8: FreeCAD MCP (46 tools, FEM/CalculiX, MIT, self-hosted) para Estrutural; Revit MCP Study (173 tools + 76 SOPs, npm, Revit 2023-2026) para Oscar — candidato complementar ao LuDattilo 138 tools. Ambas em proposta."},
```

**Alterações ao HTML:**
1. Locate `var feed = [` (linha ~540)
2. Prepend os 2 objetos JSON acima (remova um mês de histórico se exceder 50 eventos — regra de limpeza)
3. Update `<span class="updated">` para `Atualizado em: 27/08/2026 ...`
4. Backup já existe: `_backups/2026-08-27/painel_fundador_sttk.html`

**Bloqueador:** tentativa anterior (26/08) de republicar via Artifact retornou erro interno. Opções:
- **(A)** Tentar novamente com `force:true` (recomendado se erro foi transiente)
- **(B)** Reportar à Claudemberg para decisão (revert / retry amanhã / usar versão alternativa do painel)
- **(C)** Deixar localmente pronto, não republicar — Painel fica com último estado de 26/08 (2 dias desatualizado, aceitável se bloqueador persistir)

**Impacto:** Painel fica visível a Claudemberg só se republicado. Se não rodar, dados locais estão certos, só não sincronizados com a versão pública.

---

### Passo 7 — Learning Agent (Auto-Melhoria da Rotina)
**Status:** não iniciado
**O quê:** pesquisar vídeos sobre automação de criação de conhecimento, analisar via `/watch:watch`, mapear melhoria para a rotina, implementar se viável

**Sequência:**
1. WebSearch 3-5 vídeos sobre "como empresas automatizam pesquisa → documentação" (termos em SKILL.md, seção 7.a)
2. Para cada vídeo: `/watch:watch <URL>` → extrair técnicas reais
3. Mapear: qual passo desta rotina seria otimizado? (Consolidação/Redação/PDFs são candidatos)
4. Se encontrar técnica validável: documenta, implementa, registra no SKILL.md com tag `[NOVO v2.6]`
5. Se não: registra "nenhuma técnica nova identificada" (Princípio 15)

**Tempo estimado:** 15-20 min se vídeos são acessíveis, mais se houver timeout

**Impacto se não rodar:** Learning Agent v2.0 "completo" exigiu rodar até hoje. Omissão não é crítica (Passo 7 foi proposto como auto-evolucionário, não obrigatório), mas marca que a rotina não se auto-melhorou nesta rodada. Registrar no fechamento.

---

### Fechamento de Rotina
**Status:** não iniciado
**O quê:** preencher template de fechamento, declarar status final (Completa / Parcial), registrar bloqueadores e próximas ações

**Arquivo:** `01_CEO/rotina_fechamento_template.md` → seção "ESTA RODADA"

**Campos obrigatórios:**
```markdown
### Entregáveis
- Skills criadas: baumgart_freecad-mcp-fem-estrutural, arquitetura_revit-mcp-study-173tools-shuotao
- Skills documentadas: [paths]
- PDFs regenerados: 3 (se Passo 5 rodar)
- Painel atualizado: Sim/Não (depende de resolução do bloqueador Passo 6)
- Livro-razão registrado: Sim (entrada completa em Agosto.md)
- Learning Agent melhorias: 0 (Passo 7 não executado) OU N (se executado)

### Bloqueadores
1. **Passo 5 (PDFs):** bloqueado operacional se script não rodar (história de 23/08 Edit permission)
2. **Passo 6 (Painel):** bloqueado técnico — erro interno de Artifact em 26/08, não retentado
3. **Passo 7 (Learning Agent):** não foi executado nesta rodada

### Retrabalho Evitado
(nenhum — pesquisa de 27/08 foi frescos)

### Status Final
- **Rodada:** ⚠️ Parcial (5 de 8 passos completos, 3 pendentes — nenhum crítico)
- **Taxa de sucesso:** Skills criadas/documentadas + Correção estrutural (100% de impacto). PDFs/Painel/Learning dependem de execução final.
- **Próxima rodada recomendação:** (1) executar Passo 5 + Passo 6 hoje ou amanhã se possível; (2) aplicar Trilha A (Inteligência Cardozo) na próxima pesquisa — começar por Baumgart (normas estrutural) e Saturnino (normas hidrossanitário).
```

---

## III. COMO DESFAZER (Reversibilidade Completa)

**Se algo der errado após a publicação:**

1. **Skills criadas:** delete os 2 `.md` (e `.pdf` se gerados) de `01_CEO/Skills_Propostas/2026/Agosto/`
   - Remova as 2 linhas de 27/08 do `indice.md`
   - Sem impacto em cliente/código (são apenas propostas)

2. **Vitruvius rastreamento:** delete `vitruvius_achados_candidatos.md` (Oscar)
   - Remove apenas o índice; os 4 achados continuam em suas Skills isoladas

3. **SKILL.md atualizado:** restore de `_backups/2026-08-27/wallenberg-rotina-diaria-skills-v2_SKILL.md`
   - Reverte para v2.4 (sem as diretivas de Cardozo dual-track)

4. **Memórias de feedback:** delete `feedback_vitruvius_*.md` e `feedback_cardozo_*.md`
   - Remova as 2 linhas do `MEMORY.md`
   - Sem impacto operacional (são apenas notas futuras)

5. **Livro-razão:** delete ou revert a entrada de 27/08 em `Agosto.md`
   - Se houver conteúdo subsequente, mover para backup antes

**Nada foi alterado em código/Painel/cliente — tudo é reverível sem cicatrizes.**

---

## IV. SEQUÊNCIA DE EXECUÇÃO RECOMENDADA (se retomando)

```
AGORA (ou assim que possível):
  1. Passo 5 (PDFs) — 5 min
     → python md_to_pdf.py × 3
     → verifica 3 PDFs gerados

  2. Passo 6 (Painel) — 10 min
     → decide: retry / report / defer
     → se retry: WebFetch → Edit → republica via Artifact
     → se defer: registra no fechamento

  3. Passo 7 (Learning Agent) — 15-20 min (opcional)
     → WebSearch + /watch:watch
     → registra achado ou "nenhum"

  4. Fechamento de rotina — 5 min
     → preenche template
     → registra status final (Completa / Parcial)
     → copia para histórico se > 48h

TOTAL: 35-45 min para completar tudo
```

---

## V. ESTADO DE CADA PASSOS DA ROTINA (Snapshot)

| Passo | Nome | Status | Tempo | Bloqueador | Próxima Ação |
|---|---|---|---|---|---|
| 1 | Pesquisa Externa | ✅ Completo | ~15 min | Nenhum | Registrado |
| 2 | Consolidação | ✅ Completo | ~5 min | Nenhum | Registrado |
| 3 | Redação Skills | ✅ Completo (2 skills) | ~20 min | Nenhum | Passo 4 →Passo 5 |
| 4 | Salvamento Local | ✅ Completo | ~2 min | Nenhum | Passo 5 |
| 5 | Gerar PDFs | ⏳ Pendente | ~5 min | Operacional (script) | Executar |
| 6 | Atualizar Painel | ⏳ Pendente | ~10 min | Técnico (Artifact error 26/08) | Retry / Report |
| 7 | Learning Agent | ⏳ Pendente | ~20 min | Nenhum (opcional) | Executar se tempo |
| Corr. | Estrutural | ✅ Completo | ~30 min | Nenhum | Registrado + 2 memórias |
| Fech. | Fechamento | ⏳ Pendente | ~5 min | Nenhum | Preencher template |

---

## VI. CHECKSUM FINAL

**O que saiu desta rodada:**
- ✅ 2 Skills novas (Baumgart + Oscar), prontas para teste em produção
- ✅ 2 políticas estruturais codificadas (Vitruvius + Cardozo dual-track)
- ✅ Arquivo de rastreamento Vitruvius criado e populado retroativo
- ✅ SKILL.md v2.5 + 2 memórias de feedback
- ⏳ 3 PDFs gerados (se Passo 5 rodar)
- ⏳ Painel atualizado (se Passo 6 resolvido)
- ⏳ Learning Agent executado (se Passo 7 rodar)

**Risco:** baixo (nada é descartável, tudo tem backup)
**Impacto:** alto (Cardozo ganha estrutura dual, Vitruvius ganha índice de achados)
**Próxima meta:** Trilha A (Inteligência) de Cardozo começando por Estrutural (normas NBR 6118, técnicas de cálculo fundações)

---

**Última atualização:** 27/08/2026 (em progresso)
**Status operacional:** Parcial — 5/8 passos + 1 correção estrutural
**Próxima rodada:** 28/08/2026 (se agendada) ou manual conforme Wallenberg
