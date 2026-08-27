---
name: arquitetura-helonic-qaqc-clash-detection-multidisciplinar
description: "Helonic (YC Fall 2025) — IA que lê pranchas 2D em PDF (sem exigir BIM) e detecta conflitos entre arquitetura, estrutura, MEP, civil e incêndio, gerando RFI automaticamente; ângulo novo — QA/QC de compatibilização multidisciplinar, distinto de tudo já mapeado no mês (render, 2D→BIM, documentação executiva, orçamento, biblioteca, acesso a modelo, design generativo)."
metadata:
  type: skill_proposta
  gestor_alvo: "Lúcio (Arquitetura) — equipe de Oscar (QA/QC de prancha antes da entrega a Portinari/cliente); relevância secundária a Kelsen (checagem de conformidade genérica antes do protocolo, sem substituir a checagem específica de zoneamento do RIU)"
  data: 2026-08-11
  fonte_principal: "helonic.com (site oficial + about), ycombinator.com/companies/helonic, marketscale.com (cobertura independente do lote YC 2026)"
  status: proposta_arquivada
---

# Helonic — QA/QC e detecção de conflitos multidisciplinares em pranchas 2D

## Para quem serve
Equipe do Gestor Lúcio (Arquitetura) — em especial **Oscar**, no momento de revisar a prancha final antes de entregá-la a Portinari (apresentação) ou ao cliente. Ângulo **novo** dentro da busca contínua deste mês: as 9 Skills anteriores de Agosto cobrem render/vídeo (saída visual), conversão de planta em BIM (entrada, WiseBIM), documentação executiva DD/CD (SWAPP), orçamento/takeoff (Togal.AI — revertido em 10/08), biblioteca de produtos (Collection), acesso de 1ª parte ao modelo (MCP Autodesk) e design generativo (Hypar). Nenhuma cobria **revisão de qualidade e compatibilização entre disciplinas** — etapa que hoje, no fluxo deste organismo, depende inteiramente da checagem manual de Oscar/arquiteto parceiro.

## O que é — verificado em fontes que não se citam entre si
**Helonic** (antes chamada Articulate AI, Inc.) é uma startup de São Francisco, participante do lote **Y Combinator Fall 2025** — confirmado na própria listagem oficial da YC (ycombinator.com/companies/helonic), independente do site da empresa, e citado por cobertura de imprensa do setor (marketscale.com, sobre o lote de construção/proptech da YC 2026).

- **Mecanismo:** o usuário sobe pranchas de construção em **PDF 2D** — não exige modelo BIM/3D. A IA lê o conjunto e aponta conflitos entre arquitetura, estrutura, MEP (instalações), civil e proteção contra incêndio.
- **10 categorias de problema detectadas**, cada uma com grau de severidade e coordenada exata na página: conflitos de coordenação, violação de código/norma, informação faltante, questões estruturais, choques de MEP, lacunas de segurança contra incêndio, acessibilidade, construtibilidade, divergência de cotas, e itens de QA/QC em geral.
- **Saída acionável:** gera **RFI (Request for Information)** automaticamente a partir dos problemas encontrados — não só aponta, produz o documento de pedido de esclarecimento pronto.
- **Integrações confirmadas:** conexão de um clique com **Procore** e **Autodesk Construction Cloud** — puxa pranchas direto do projeto, sem upload manual, e devolve os RFIs gerados para dentro dessas plataformas.
- **Produto dedicado a arquitetos:** a própria empresa tem uma linha de produto chamada "Drawing Set QA/QC for Architects" (helonic.com/for/architects/qa-qc), separada da linha para estruturais e para estimadores — não é ferramenta genérica de construtora, tem oferta pensada para o papel que Oscar exerce.
- **Clientes nomeados** (site oficial): Barnhill Contracting, Omni Structural, Lema Construction, Swinerton, Whiting-Turner, Urban Core, Johnson Pace, LS Black Constructors, Archi Group of Builders, LMG Ventures — Swinerton e Whiting-Turner são construtoras de grande porte nos EUA (top-20 ENR), sinal de tração real, não só startup em estágio de ideia.
- **Proposta de valor declarada:** a indústria de construção americana perde **US$31 bilhões/ano com retrabalho** (dado da própria empresa, não verificado por fonte terceira nesta rodada — registrado como alegação da empresa, não fato confirmado) — o produto se posiciona como prevenção (achar o conflito na prancha, não na obra).

## O que NÃO foi confirmado (limite do achado, Princípio 3)
- **Sem MCP.** A página oficial referencia um arquivo `helonic.com/llms.txt` ("full LLM description") — isso é um arquivo de indexação para crawlers de IA (mesmo padrão do `robots.txt`, mas para LLMs), **não é um servidor MCP nem uma API pública de automação**. Não confundir os dois — nenhuma fonte consultada indica endpoint de API documentado para terceiros.
- **Preço não divulgado publicamente** — página oferece só "Book a Demo" (modelo de venda consultiva/enterprise), sem tabela de preço.
- **Fundadores não identificados nominalmente** nas páginas consultadas (só e-mail de contato `founders@helonic.com`) — não impede o achado (a empresa e o produto estão verificados via YC), mas registrado como lacuna.
- **Nenhuma fonte confirma uso no Brasil** nem compatibilidade com o fluxo de licenciamento LICIN 2.0 — a "violação de código/norma" que a ferramenta detecta é código de construção americano genérico (IBC e afins), não substitui a checagem de zoneamento específica do RIU que já é responsabilidade do Kelsen desde o Levantamento (Skill `legal-base-legislativa-bairro`).
- **Alegação de US$31bi/ano em retrabalho** é número de marketing da própria empresa — não cruzado com fonte setorial independente nesta rodada, registrado com essa ressalva.

## Por que é achado relevante para o organismo
Hoje a compatibilização entre a prancha de Oscar e o quadro de áreas, cortes e fachadas depende de revisão humana (o próprio Exame 2/Caso 1 de Portinari, de 10/08, testou exatamente uma contradição desse tipo — 4 pavimentos na prancha vs. 3 + cobertura técnica no quadro). Uma ferramenta que varre PDF de prancha e aponta esse tipo de divergência automaticamente, com coordenada exata na página, é candidato de mercado a reduzir esse risco antes da entrega a Portinari — mesmo sem conector automatizável por Agente hoje. Fica registrado como proposta, mesmo tratamento dado às Skills anteriores sem MCP confirmado (SWAPP.AI, Togal.AI, Hypar).

## Estado da busca contínua de render/vídeo/tour 360 nesta rodada (11/08/2026)
Sem achado novo de conector MCP nos 5 softwares já rastreados (Twinmotion, Magnific, Blender, Matterport, D5 Render/Enscape/Lumion) — buscas desta rodada retornaram só matérias comparativas de qualidade/preço entre D5, Enscape, Lumion e Twinmotion (illustrarch.com, myarchitectai.com, 256grays.com, nuviraspace.com), nenhuma menciona integração MCP nova. Gap de geração de apresentação por Agente a partir do modelo BIM continua aberto.

## Fontes
- https://helonic.com/ (site oficial — resumo executivo, proposta de valor, clientes nomeados)
- https://helonic.com/about (Y Combinator, Articulate AI Inc.)
- https://helonic.com/for/architects/qa-qc (linha de produto específica para arquitetos)
- https://helonic.com/for/structural-engineers/qa-qc e https://helonic.com/for/estimators/coordination-review (linhas de produto para estrutural/estimador — contexto de amplitude do produto)
- https://www.ycombinator.com/companies/helonic (confirmação independente — lote Fall 2025, descrição "Automatic Construction Drawing Clash Detection")
- https://www.marketscale.com/industries/engineering-and-construction/y-combinators-2026-real-estate-and-construction-cohort-bets-big-on-ai-agents-and-construction-intelligence (cobertura de imprensa independente sobre o lote YC 2026 de construção/proptech)
