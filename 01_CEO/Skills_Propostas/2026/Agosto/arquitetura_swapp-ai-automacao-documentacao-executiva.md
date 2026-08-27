---
name: arquitetura-swapp-ai-automacao-documentacao-executiva
description: "SWAPP.AI — automação de até 80% da documentação executiva (DD/CD) dentro do Revit/ArchiCAD via agente proprietário 'Frank'; sem MCP/API aberta, mas real, maduro e usado por escritórios nomeados (Stantec, Page, HGA)"
metadata:
  gestor_alvo: Lúcio (Arquitetura) — não implantado; equipe de Coordenador de Projeto Arquitetônico (etapa de documentação executiva, distinta de render/vídeo)
  data: 2026-08-07
  status: ativa (arquivada — Gestor Arquitetura ainda não implantado)
  fonte: swapp.ai (site oficial + case studies), aecmag.com, aecplustech.com, calcalistech.com
---

# SWAPP.AI — automação de documentação executiva (DD/CD) em Revit/ArchiCAD

## Para quem serve
Lúcio (Gestor Arquitetura) e a futura equipe — em especial o **Coordenador de Projeto Arquitetônico**. Ângulo novo dentro da busca contínua deste organismo: as rodadas de 01-06/08 mapearam render/vídeo/tour 360 (saída visual) e conversão 2D→BIM (entrada, WiseBIM); esta Skill cobre a etapa intermediária — **produção da documentação executiva em si** (plantas, cortes, fachadas, quadros, compatibilização básica), que é o volume de trabalho mais repetitivo e caro do Anteprojeto/Executivo.

## O que o achado diz
**SWAPP** (fundada em Tel Aviv, escritório em Houston) é uma AECtech madura e bem financiada — Series A de US$11,5 milhões (liderada pela Eurazeo), total de US$18,5 milhões captados, confirmado em 3 fontes independentes que não se citam entre si (calcalistech.com, thesaasnews.com, pulse2.com), além do anúncio oficial em swapp.ai.

**Como funciona:** o escritório sobe um projeto em nível esquemático; o algoritmo proprietário da SWAPP (chamado "Design Decision Language", DDL) aprende os padrões de anotação, QA e biblioteca (famílias, materiais, móveis) do próprio escritório e gera automaticamente o conjunto DD/CD dentro do Revit ou ArchiCAD — folhas, vistas, cotas, tags, compatibilização básica entre disciplinas. O agente tem nome próprio, **"Frank"**, descrito pela empresa como "teammate" que lê e escreve no modelo ao vivo.

**Resultados reportados pela empresa (2 anos de operação):** mais de 35 milhões de pés quadrados de documentação entregue, mais de 104.000 horas de produção economizadas. Casos por escritório nomeado, com link primário de cada case study:
- **Page** — projeto de moradia estudantil de 270.000 pés², do conceito ao estudo preliminar em 3 semanas, com equipe 40% menor.
- **AHA** — pacote de alvará de 550.000 pés² entregue em 1 semana.
- **MYS Architects** — redução de 8x na carga manual de trabalho (case study com nome do escritório, via aecplustech.com).
- **HTA Design** — equipe da etapa de documentação (Stage 4, padrão britânico RIBA) cortada pela metade.
- **SNHA (Woolpert)** — trabalho que levava 2 semanas, reduzido a menos de 48 horas.
- **MOREgroup** — ampliou capacidade de entrega de projetos sem aumentar equipe (case study próprio, swapp.ai/case-studies1/moregroup).
- Cliente adicional citado pela própria empresa: **Stantec, HGA** (escritórios de grande porte, uso confirmado em material institucional).

## O que NÃO foi confirmado (limite do achado, Princípio 3)
- **Não existe MCP nem API pública documentada.** SWAPP opera como plugin/agente proprietário dentro do Revit/ArchiCAD ("Frank"), não como conector externo que um agente como o Coordenador de Projeto Arquitetônico deste organismo possa acionar via ferramenta própria — diferente do Vitruvius (já ativo) ou dos MCPs de render mapeados em rodadas anteriores. É um produto SaaS de operação pelo próprio time humano do escritório dentro do Revit, não um componente que se integra à cadeia de agentes do organismo hoje.
- Preço não divulgado publicamente nas fontes consultadas (modelo enterprise, sob consulta).
- Nenhuma fonte menciona compatibilidade com fluxo brasileiro de licenciamento (LICIN 2.0/DULI) — é ferramenta de produção de documentação técnica, não de conformidade legal; continuaria exigindo a checagem de parâmetro urbanístico já coberta pela Skill `legal-base-legislativa-bairro` do Kelsen.

## Por que isso importa para o organismo agora
Não é ação imediata (Gestor Arquitetura sem equipe nomeada). Fica registrado como candidato de mercado de peso real para quando o Coordenador de Projeto Arquitetônico for nomeado e a etapa de Anteprojeto/Executivo tiver volume que justifique avaliar automação de documentação — categoria distinta de tudo já mapeado (render, conversão 2D→BIM, gerenciamento de tour 360, acesso a modelo via MCP). Diferença central a lembrar na hora de decidir: SWAPP substitui trabalho humano *dentro* do fluxo de um escritório que já usa Revit/ArchiCAD com time próprio — não é uma ferramenta que um Agente de IA deste organismo aciona por fora, como o Vitruvius é hoje.

## Fontes
- https://swapp.ai/ (site oficial, capacidades e DDL)
- https://aecmag.com/ai/swapp-the-algorithmic-assistant/ (arquitetura técnica, DDL, "Frank")
- https://www.aecplustech.com/blog/swapp-the-ai-co-pilot-for-construction-documentation (resultados: 35M pés², 104.000h)
- https://www.aecplustech.com/projects/mys (case study MYS Architects, nomeado)
- https://www.swapp.ai/case-studies1/moregroup (case study MOREgroup, nomeado)
- https://www.calcalistech.com/ctechnews/article/hkruplbs2 (Series A, US$11,5M, Eurazeo)
- https://pulse2.com/swapp-11-5-million-funding/ (confirmação independente do funding)
