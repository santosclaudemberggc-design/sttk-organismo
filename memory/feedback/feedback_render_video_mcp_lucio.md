---
name: feedback-render-video-mcp-lucio
description: "Busca contínua e obrigatória de conectores/IAs via MCP para render, vídeo e tour 360 dentro da equipe do Gestor Lúcio (Arquitetura) — e regra de cadência: só reportar a Claudemberg quando 100% verificado e confirmado prático dentro do organismo"
metadata:
  type: feedback
---

Render, vídeo e apresentação já são entregável **mandatório** de Lúcio (Estudo Preliminar e Anteprojeto, confirmado na Planilha de Enviáveis — ver [[sttickler_planilha_enviaveis_arquitetura]]), mas o organismo não tem hoje nenhuma ferramenta que produza isso. Claudemberg instruiu (31/07/2026): a busca por essa lacuna não é um achado pontual de uma rodada — é **contínua**, e o critério de solução é específico:

**O que buscar:** conectores ou IAs que, via **MCP** (não ferramenta web solta, não plugin manual), a **equipe do Lúcio** (hoje: o bridge Vitruvius/Revit + futuros Agentes coordenadores) já consiga usar para gerar:
- Renders (imagem estática a partir do modelo)
- Vídeos (fly-through, animação)
- Tour 360 (passeio virtual navegável)
- e outros formatos de apresentação equivalentes

**Por quê MCP especificamente:** o organismo funciona por agentes que operam via MCP (mesmo padrão do Vitruvius, que é literalmente um MCP de Revit). Uma ferramenta de render sem conector MCP não é utilizável pela equipe do Lúcio da mesma forma — exigiria operação manual fora do fluxo de agente, quebrando a automação.

**Como aplicar:** Toda rodada de pesquisa (rotina diária ou sob demanda) que tocar em Arquitetura/Lúcio deve checar o registro de conectores MCP (`mcp-registry`, `search_mcp_registry`/`suggest_connectors`) além da busca web solta, e verificar se algum MCP novo de renderização/visualização 3D/tour virtual apareceu — D5 Render, Enscape, Veras, Twinmotion, Lumion, Matterport e equivalentes são candidatos naturais a checar se ganharam conector MCP. Não é achado de uma vez só — é vigilância recorrente até resolver o gap.

**Regra de cadência, acrescentada em 01/08/2026 (Claudemberg, ao vivo):** depois de uma rodada com 3 achados no mesmo dia (Twinmotion, Magnific, stack gratuito Blender MCP/Hugging Face — ver `01_CEO/Skills_Propostas/2026/Agosto/`), Claudemberg pediu para desacelerar o ritmo de reporte, não o de pesquisa. Instrução: continuar estudando/analisando nas rodadas seguintes (rotina diária normal), **mas só levar o achado a Claudemberg quando estiver com 100% de certeza** — não trazer candidato parcialmente verificado ou "acho que resolve". O critério de "100% de certeza" tem duas partes, ambas obrigatórias:
1. **Verificação técnica completa** (Princípio 3) — não só "existe e tem estrelas no GitHub", mas testado ou confirmado por fonte primária que funciona de ponta a ponta para o caso de uso real (render/vídeo/tour a partir do fluxo de trabalho do Lúcio).
2. **Compatibilidade confirmada com o organismo específico** — precisa conectar dentro do Claude Code (não só Claude Desktop/Cursor/outro cliente) de forma **fácil e prática** ("de fácil conexão", nas palavras de Claudemberg), não uma integração frágil ou que exija múltiplos passos manuais fora do fluxo de agente.
Enquanto isso não estiver batido, a pesquisa continua nos bastidores (rotina diária, sem crescer a cadência de report) e nada precisa ser levado à conversa — nem um resumo intermediário. Isso não cancela o registro em Skills_Propostas (continuar arquivando candidatos como proposta, é o registro de trabalho em andamento) — cancela é a expectativa de trazer isso à tona em toda conversa/rotina até estar pronto.
