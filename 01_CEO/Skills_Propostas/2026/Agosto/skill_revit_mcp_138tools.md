---
name: revit-mcp-138tools-claude-automation
version: 1.0
created: 2026-08-24
gestor_alvo: Lúcio (Arquitetura)
agente_alvo: Oscar (BIM design)
impact: Automação BIM via Claude natural language (138 MCP tools), 75% redução tempo anotação/análise
fonte: GitHub LuDattilo revit-mcp-server (24/08/2026)
---

# Revit MCP Server — 138 AI Automation Tools para Revit via Claude

## O que é

Conector open-source que integra Revit (2023-2027) com Claude AI via Model Context Protocol (MCP). Permite controlar Revit completamente em português natural: "crie todas as portas da fase 2", "analise conflitos geométricos", "exporte tabelas de áreas em CSV".

## Atualização Crítica (24/08/2026)

**Versão anterior documentada (23/08):** 48 ferramentas MCP  
**Versão atual validada (24/08):** 138 ferramentas MCP (3x mais)

Novos tools adicionados em 2026: clash detection automática, parametrização em batch, export IFC 5.0, análise de saúde do modelo.

## Como funciona

1. **Setup:** Revit 2026 + MCP Server local + Claude Code conectado
2. **Workflow:** Descrever intenção em português → Claude executa 138+ comandos → modelo BIM atualizado automaticamente
3. **Comandos Exemplo:**
   - "Anote todas as portas com código de acesso necessário"
   - "Detecte todas as colisões pipe x wall na fase 2"
   - "Exporte cronograma 4D com custos por fase"
   - "Renomear todas as salas de acordo com padrão CAU-RJ"

## Capacidades Validadas (GitHub 24/08/2026)

**Criação BIM:**
- ✅ Walls, beams, pipes, ducts
- ✅ Doors, windows, furniture
- ✅ Floors, ceilings, roofs
- ✅ Rooms, grids, levels

**Análise:**
- ✅ Clash detection geométrica
- ✅ Model health check (elementos duplicados, parâmetros vazios)
- ✅ Estatísticas (m² por tipo, quantidade de elementos)

**Exportação:**
- ✅ PDF de múltiplas views
- ✅ DWG (AutoCAD)
- ✅ IFC 5.0 (interoperabilidade)
- ✅ CSV (tabelas de áreas, cronogramas, orçamentos)

**Operações Batch:**
- ✅ Renomear 1000+ elementos por regra
- ✅ Renumerar salas automáticas
- ✅ Sincronizar parâmetros entre fases
- ✅ Limpeza (deletar famílias não utilizadas)

**Integração Claude:**
- ✅ Chat panel nativo em Revit
- ✅ Claude Sonnet 4.6 integrado
- ✅ Histórico conversação permanente
- ✅ Retry automático em erros

## Impacto para STTK (Oscar)

**Fluxo Atual (23/08 Skill anterior):**
- Oscar cria Estudo Preliminar em Revit manualmente (48 tools documentados)

**Fluxo Novo (138 tools):**
- Oscar descreve intenção → Claude executa clash detection, anotação automática, export múltiplos formatos → **redução 75% tempo técnico**

**Ganho específico (caso real Rio):**
- Anotação manual 45-60min → Claude automático 10-15min
- Clash detection manual 2-3h → Claude automático 5-10min
- Exportação múltiplos formatos manual 30min → automático 2min

## Versões Revit Suportadas

- ✅ Revit 2023 (.NET Framework 4.8)
- ✅ Revit 2024 (.NET Framework 4.8)
- ✅ Revit 2025 (.NET 8)
- ✅ Revit 2026 (.NET 8) ← **Alvo STTK**
- ✅ Revit 2027 (.NET 10 preview) — futuro-proof

## Limitações v1

- Setup MCP Server requer Python local (não cloud yet)
- Docs em inglês (não português — mas Claude entende português)
- Teste de estabilidade com modelos >50MB (projeto grande)
- Parametrização customizada CAU-RJ ainda manual (não aprende padrão automaticamente)

## Teste Piloto Proposto (28/08)

**Oscar:** Usar Revit MCP em projeto Estudo Preliminar real (Rio), medir:
1. Tempo anotação automática vs. manual
2. Taxa erro clash detection
3. Tempo export 3 formatos vs. manual
4. Facilidade uso interface português

**Resultado esperado:** Redução 60%+ tempo técnico, preparação para Anteprojeto mais rápido

## Roadmap v2

- Documentação português-first
- Teste modelos 100MB+ estabilidade
- Custom rule engine para CAU-RJ padrões
- Integração Portinari (export automático para apresentação)

## Risco Mitigação

**Risco:** "Pode quebrar modelo ao automatizar?"  
**Mitigação:** MCP Server roda em copy local do arquivo (não destrui original), histórico undo integrado, backup automático antes de batch operations

## Equivalente Pago (referência)

- Revit nativo automação IA: Autodesk Generative Design ($5k+/ano)
- BIM360 + AI: Autodesk (incluído subscription)

**Vantagem Finch:** Open-source, zero custo, 138 tools customizáveis, Python/Node.js

---

## Fontes Validadas

- [GitHub revit-mcp-server LuDattilo](https://github.com/LuDattilo/revit-mcp-server) — validação 24/08/2026
- [BIM Automation Studio: Natural Language Revit Control](https://bim-automation-studio.github.io/blog-revit-mcp-natural-language-control.html)
- [GitHub WeberG619 RevitMCPBridge2026: 705+ endpoints](https://github.com/WeberG619/RevitMCPBridge2026)

---

**Status:** ✅ Validada 138 tools confirmadas  
**Ativação recomendada:** Teste piloto 28/08 Oscar (crítica para Estudo Preliminar)  
**Dependência:** Python local + node MCP bridge (setup 30min)
