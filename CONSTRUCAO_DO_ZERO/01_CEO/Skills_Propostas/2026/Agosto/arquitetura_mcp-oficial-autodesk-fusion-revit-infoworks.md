---
name: arquitetura-mcp-oficial-autodesk-fusion-revit-infoworks
description: "MCP oficial da Autodesk (Fusion, Revit, InfoWorks) — servidores de 1ª parte anunciados na DevCon 2026, ainda em tech preview, sem confirmação de conector dedicado para Forma"
metadata:
  gestor_alvo: Lúcio (Arquitetura) — não implantado; achado de infraestrutura/plataforma, relevante para a equipe de Coordenador de Projeto Arquitetônico e futuro Agente de Renders/Vídeos
  data: 2026-08-06
  status: ativa (arquivada — Gestor Arquitetura ainda não implantado)
  fonte: aps.autodesk.com (blog oficial "Building for Agentic AI: What's New in Autodesk Platform Services"; página "Forma APIs")
---

# MCP oficial da Autodesk — Fusion, Revit, InfoWorks (tech preview, DevCon 2026)

## Para quem serve
Lúcio (Gestor Arquitetura) e a equipe dele — em especial o Coordenador de Projeto Arquitetônico, que hoje já opera sobre modelo Revit via o conector `mcp__vitruvius__*` (comunitário/terceiro, já ativo neste organismo: cria parede, porta, janela, piso, ambiente, cotas, pranchas etc.). Esta Skill não substitui o Vitruvius — registra que a própria Autodesk lançou, em paralelo, um caminho **oficial de 1ª parte** para o mesmo tipo de acesso, ainda imaturo, que deve ser monitorado antes de qualquer decisão de trocar ou complementar a integração atual.

## O que o achado diz
A Autodesk anunciou na **DevCon 2026 (15/04/2026)** um conjunto de **MCP servers oficiais** sob o guarda-chuva "Building for Agentic AI", permitindo que agentes de IA acessem contexto de projeto e ferramentas Autodesk sem integração customizada. Confirmados no blog oficial (aps.autodesk.com):

- **Fusion MCP** — criar, modificar e inspecionar geometria 3D.
- **Fusion Data MCP** — interagir com propriedades de componentes.
- **Revit MCP** — acessar e inspecionar dados de modelo BIM.
- **InfoWorks MCP** — modelagem hidráulica (fora do escopo de Arquitetura, mais próximo de um futuro Complementares/Hidrossanitário).

A maioria está em **tech preview** — não é lançamento de produção. O documento não especifica preço/licenciamento nem menciona Claude nominalmente (mas o protocolo MCP é agnóstico de cliente; o Claude Code já suporta MCP nativamente, então a conexão é tecnicamente viável assim que o servidor sair de preview).

## O que NÃO foi confirmado (limite do achado, Princípio 3)
- **Forma não tem MCP dedicado confirmado.** A página "Forma APIs" (aps.autodesk.com/developer/overview/forma) lista APIs REST tradicionais (dados de projeto, Data Exchange, Sustainability Data, Parameters, Webhooks, Automation) — nenhuma menção a servidor MCP específico para Forma. O gap de "IA generativa de massing + análise solar/vento via agente" segue sem conector direto, mesmo a Forma sendo a ferramenta mais citada do mercado para isso (ver observações da rodada abaixo).
- Custo/licenciamento do MCP não informado nas fontes.
- Nenhuma menção explícita a integração com Claude — inferência técnica, não fato anunciado pela Autodesk.

## Por que isso importa para o organismo agora
Não é ação imediata — é item de monitoramento. Quando o Gestor Arquitetura for implantado e a equipe de Renders/Vídeos for nomeada, esta Skill deve ser revisitada para decidir: manter o Vitruvius (comunitário, já testado em produção neste organismo) ou migrar/complementar com o MCP oficial da Autodesk quando ele sair de tech preview — trade-off entre maturidade testada (Vitruvius) e suporte de 1ª parte (Autodesk oficial).

## Fontes
- https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services (anúncio DevCon 2026, MCPs Fusion/Revit/InfoWorks)
- https://aps.autodesk.com/developer/overview/forma (APIs da Forma, sem MCP dedicado confirmado)
