---
name: arquitetura-hypar-design-generativo-text-to-bim
description: "Plataforma web real (Hypar, fundada 2018, ex-Autodesk) que gera modelo BIM paramétrico a partir de descrição em linguagem natural (\"text-to-BIM\") — ângulo novo para o Lúcio: design generativo/paramétrico no Estudo Preliminar, distinto de render/vídeo (saída), 2D→BIM de planta existente (entrada/WiseBIM) e documentação executiva (SWAPP)."
metadata:
  type: skill_proposta
  gestor_alvo: "Lúcio (Arquitetura) — equipe de Oscar (Coordenador de Projeto Arquitetônico), etapa de Estudo Preliminar"
  data: 2026-08-10
  fonte_principal: "aecmag.com/ai/hypar-text-to-bim-and-beyond, datadrivenaec.com/tools/hypar, github.com/hypar-io"
  status: proposta_arquivada
---

# Hypar — design generativo/paramétrico com geração de BIM a partir de texto

## Para quem serve
Equipe do Gestor Lúcio (Arquitetura), especificamente a etapa de **Estudo Preliminar** — hoje conduzida por Oscar (Coordenador de Projeto Arquitetônico) com o arquiteto parceiro, desenhando no Revit via Vitruvius (MCP comunitário já ativo no organismo). Ângulo **novo**: nenhuma Skill anterior deste mês cobria geração generativa/paramétrica de massa/layout a partir de descrição textual — as 8 Skills anteriores de Agosto mapeiam render/vídeo (saída, 3 Skills), conversão de planta existente em BIM (entrada, WiseBIM), documentação executiva DD/CD (SWAPP), orçamento/takeoff (Togal.AI), biblioteca de produtos (Collection) e acesso de 1ª parte ao modelo (MCP Autodesk).

## O que é — verificado em fontes independentes que não se citam entre si
Hypar é uma plataforma **web/cloud**, fundada em 2018 por Anthony Hauck e Ian Keough (ambos ex-Autodesk), que converte requisitos de programa de necessidades em modelo 3D/BIM parametrizado:
- **Mecanismo ("text-to-BIM"):** usuário descreve o programa (ex. "edifício de varejo com 2 andares e 14 de residencial em formato L") e o sistema mapeia a entrada em **funções paramétricas** próprias (biblioteca/marketplace de lógica reutilizável — posicionamento de núcleo, otimização de fachada, análise de luz natural etc.), gerando estrutura, fachadas e layout em segundos.
- **Motor:** executa código em **Python e C#** (arquitetura de microsserviços); usuários avançados podem escrever suas próprias funções.
- **Integrações confirmadas:** Revit (importação/exportação "rica"), Grasshopper (scripts convertem-se em funções Hypar diretamente), IFC (exportação), e segundo fonte de fev/2026 também Rhino, AutoCAD, Excel/CSV e formatos gráficos (PDF/DXF/DWG/PNG/JPG).
- **Etapa de projeto:** cobre de **Pré-Design/Schematic Design** (equivalente a Estudo Preliminar) até detalhamento de fabricação — não é ferramenta de um único estágio.
- **Preço:** divergência entre fontes por data — AEC Magazine (matéria de 2023) registra US$79/mês/usuário; DataDrivenAEC (verificado 01/02/2026) registra plano Free, Pro US$25/mês e Enterprise sob consulta. Checar valor ao vivo no site oficial antes de qualquer uso real — não tratar nenhum dos dois como preço atual garantido.
- **Financiamento/tração:** Series A de US$5,5M, base de usuários na casa dos milhares, incluindo escritórios nomeados (S/L/A/M, Adrianse) — segundo DataDrivenAEC.

Confirmado em 2 fontes independentes que não se citam entre si (AEC Magazine — publicação técnica AEC estabelecida — e DataDrivenAEC), mais existência confirmada em fonte primária própria (github.com/hypar-io, organização ativa).

## O que NÃO é / ressalva de confiança
- **Sem MCP confirmado.** Nenhuma das fontes consultadas menciona Model Context Protocol. Hypar expõe **API própria** (a plataforma é descrita como "cloud-based platform and API" que executa código do usuário) — mas não é um servidor MCP plugável diretamente num Agente Claude hoje, mesmo status da maioria dos achados deste mês (WiseBIM, Collection, SWAPP, Togal.AI).
- **Não confundir com o Vitruvius já ativo no organismo:** Vitruvius é MCP que manipula diretamente o modelo Revit (criar parede, porta, nível, cômodo etc.) sob comando do Oscar; Hypar é geração paramétrica/generativa de massa e layout a partir de descrição de programa — mecanismo diferente, um não substitui o outro. Comparação vale quando (e se) o organismo avaliar ferramenta de apoio à geração de alternativas no Estudo Preliminar.
- **Preço divergente entre fontes** (US$79/mês vs. Free/US$25/mês Pro) — sinal de que o modelo de preço mudou entre 2023 e 2026, não erro de leitura; ambos os valores registrados com a data da fonte, nenhum tratado como atual sem checagem ao vivo.
- Nenhuma fonte confirma uso por escritório brasileiro nem conformidade com legislação/parâmetro urbanístico local (LICIN 2.0) — geração é genérica de programa arquitetônico, não substitui a checagem de zoneamento que já é responsabilidade do Kelsen desde o Levantamento.

## Por que é achado relevante para o organismo
Hoje o Estudo Preliminar depende inteiramente do arquiteto parceiro (com apoio do Oscar/Vitruvius) para gerar as primeiras alternativas de massa/layout. Uma plataforma que gera múltiplas alternativas paramétricas a partir de descrição textual do programa — mesmo sem conexão automática por Agente — é candidato de mercado a acelerar a fase de geração de alternativas antes da modelagem definitiva no Revit. Vale revisitar quando o organismo tiver capacidade de avaliar integração real (API própria, não MCP) e comparar contra o fluxo Oscar+Vitruvius já em produção.

## Estado da busca contínua de render/vídeo/tour 360 nesta rodada (10/08/2026)
Sem achado novo de conector MCP nos 5 softwares já rastreados (Twinmotion, Magnific, Blender, Matterport, D5 Render/Enscape/Lumion). Achado colateral, não fechado como Skill por redundância: Chaos AI Enhancer, Chaos AI Material Generator e Chaos AI Upscaler (blog oficial Chaos, "Top 20 AI Tools for Architects 2026") são recursos/plugins internos do Enscape/Chaos Cloud — mesma categoria já registrada para a Veras AI em 05/08 (recurso nativo do software de render, não conector de Agente externo). Envision AI Assistant (beta no Enscape, ajuste de iluminação/materiais por linguagem natural) é novo nome, mesma conclusão: sem MCP, não acionável por fora. Gap de geração de apresentação por Agente a partir do modelo BIM continua aberto.
