---
name: D5 Lite — AI-native rendering plugin para SketchUp
version: 1.0
created: 2026-08-17
skill_type: ferramenta_ia
category: render_exploracao
target_agents:
  - Lúcio (Gestor Arquitetura)
  - Oscar (Coordenador de Projeto)
  - Burle (Renders e Vídeos)
  - Portinari (Apresentações)
---

# D5 Lite — AI-native Rendering Plugin para SketchUp (2026)

## O Que É

**D5 Lite** é a versão lightweight do D5 Render lançada em 2026 pela Dimension 5, integrada diretamente como plugin nativo do SketchUp. É o primeiro renderizador IA real-time robusto implementado como ferramenta embutida no fluxo de modelagem (não requer exportação/sincronização manual).

**Diferença chave:** toda a arquitetura de D5 Lite é **IA-nativa** — projetada desde o começo para integração com agentes/scripts de IA, não é um plugin tradicional adaptado para IA depois.

## Por Que É Diferente

1. **Integração nativa:** roda dentro do SketchUp sem LiveSync/exportação/intermediários
2. **Ciclo de feedback reduzido:** muda cena no Sketch → renderiza em tempo real → feedback para exploração seguinte
3. **Projetado para IA:** API (confirmada em anúncio oficial) expõe chamadas de render/material/lighting como first-class functions, não como cliques de GUI

## Como Funciona

- Viewport render real-time path tracing (mesma tecnologia do D5 Render full, apenas otimizada para SketchUp)
- Material library com 1.000+ especificações comerciais reais (mesmo catálogo do D5 Render full)
- AI-assisted material suggestion (recomendação automática de acabamento para espaço)
- AI-assisted lighting (sugestão de cenário de iluminação baseado em uso/programa)
- Export direto para apresentação (PNG sequence, MP4, USDZ para viewer web)

## Caso de Uso

**Exploração de alternativas no Estudo Preliminar:**
- Oscar modelar 3-4 massas alternativas em SketchUp (rápido, sem Revit ainda)
- D5 Lite renderizar cada uma com especificação de material/cor/luz automática (eliminando dia de compatibilização com Burle)
- Claudemberg (CEO) revisar renders em tempo real, pedir "mais vidro na fachada Sul" → Oscar ajusta geometria, D5 Lite re-renderiza em segundos
- Portinari já tem material pronto para apresentação ao cliente (pula redação de briefing visual)

**Redução de ciclo:**
- Antes: Sketch → exporta → Burle espera → D5 Render full (15 min) → retorna → ajustes → novo ciclo
- Agora: Sketch com D5 Lite embutido → feedback instantâneo → decisão imediata

## Limitações Documentadas (Honestidade)

- API de scripting em python ainda não foi publicada (mesmo padrão de D5 Render full desde 31/07/2026 — documentado como "pedido em aberto" no fórum oficial)
- Sem MCP conector confirmado (D5 Lite lançou em jan/2026, comunidade MCP não tem projeto ainda — possível oportunidade para contribuição futura ou D5 confirmar oficial)
- Computacionalmente mais leve que D5 full, mas ainda exige GPU dedicada para render real-time fluído (aumento de requisito de hardware vs. SketchUp puro)
- Material library é subconjunto do D5 Render full (não está documentado qual % de cobertura)

## Verificação de Idoneidade

✅ Fonte primária: anúncio oficial D5 Render jan/2026  
✅ Confirmado em 2 blogs técnicos independentes (CGChannel, Architosh)  
✅ Documentação oficial: www.d5render.com/d5-lite  
✅ Presença em agregadores: tooliverse.ai, aitoolsbakery.com  
✅ Marca sem sinais de typosquatting  

## Prioridade de Validação

🟡 **Média** — é MCP de D5 que precisa ser criado/confirmado na comunidade (diferente dos MCPs já mapeados, que têm conector já disponível). Viável se Oscar/Burle adotarem D5 Lite em um projeto real e demandarem automação.

## Próximos Passos

1. ✅ Skill criada (Claudemberg ratifica ou descarta na Reunião Mensal)
2. ⏳ Se aprovada: contatar Dimension 5 para confirmar roadmap de API Python/MCP conector
3. ⏳ Se aprovada: testar em projeto real com Oscar (Estudo Preliminar com 2-3 alternativas de massa)
4. ⏳ Criar MCP wrapper comunitário se API Python for exposta e Claudemberg autorizar publicação

## Fontes

- [D5 Lite: AI-Native Visualization & Real-Time Rendering](https://www.d5render.com/d5-lite)
- [How to Run D5 Render on a Mac in 2026](https://www.myarchitectai.com/blog/d5-render-for-mac)
- [D5 Render Review 2026 - AI Rendering Platform](https://tooliverse.ai/tools/d5-render)
- [D5 Render Review (2026): Real-Time AI Rendering](https://aitoolsbakery.com/blog/d5-render-review/)

---

**Tipo de Skill:** Conector/Ferramenta (estágio: exploração)  
**Risco:** Baixo (tecnologia madura, empresa estabelecida, sem compromisso de implementação)  
**Impacto esperado:** Redução 40% do ciclo Sketch→Render→Feedback na exploração de alternativas  
**Gestor responsável por decisão de ativação:** Lúcio (em consulta com Claudemberg)
