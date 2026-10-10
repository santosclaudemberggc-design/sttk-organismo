---
name: compatibilizacao-projetos
description: Compatibilização de projetos multidisciplinares — normas NBR ISO 19650/15965, clash detection, matriz GUT de priorização, e inteligência de QA/QC via leitura de PDF 2D (10 categorias de conflito, geração automática de RFI). Use sempre que o futuro Agente de Compatibilização (Gestor Fechamento) precisar checar interferência entre disciplinas (Estrutural x Elétrico x Hidrossanitário x Paisagismo x Interiores), priorizar conflitos encontrados, ou revisar prancha compilada antes da entrega ao cliente — mesmo que o pedido só mencione "clash", "conflito entre disciplinas" ou "compatibilizar", sem citar a norma pelo nome.
---

# Compatibilização de Projetos — Normas + Inteligência de QA/QC Multidisciplinar

Skill de Inteligência Técnica da área Fechamento (Gestor ainda não implantado). Etapa que recebe o output das 6 disciplinas de Cardozo/Complementares e antecede Projeto Executivo → Orçamento Executivo → Liberação de Obra (Gate 16) — todas do Gestor Fechamento (decidido por Claudemberg em 29/07/2026).

## Base normativa

Compatibilização BIM profissional no Brasil é estruturada por duas normas: **NBR ISO 19650** (gestão da informação em BIM ao longo do ciclo de vida) e **NBR 15965** (classificação da informação da construção). Três práticas centrais:

1. **Clash detection automatizado:** ferramentas de mercado (Navisworks, Solibri Model Checker, Trimble Connect — via Autodesk Construction Cloud) localizam interferências entre disciplinas (Estrutural, Elétrico, Hidrossanitário, Automação, Interiores, Paisagismo) antes da obra.
2. **Clash avoidance:** prevenção na origem — projetar cada disciplina já pensando na interação com as outras reduz o volume de conflitos encontrados depois.
3. **Priorização por matriz GUT** (Gravidade, Urgência, Tendência) quando há muitas interferências simultâneas — decide por onde começar a resolver, em vez de tratar tudo como igualmente crítico.

Fontes de mercado relatam retorno de R$30-40 para cada R$1 investido em compatibilização correta, e redução de retrabalho superior a 90%.

## Inteligência de QA/QC (extraída de achado de mercado real — Helonic, YC Fall 2025)

A ferramenta comercial original não é adotável hoje (sem MCP/API pública) — mas o **conceito** que ela materializa é diretamente aplicável:

- **Mecanismo de referência:** ler o conjunto de pranchas em **PDF 2D** — sem exigir modelo BIM pronto — e apontar conflitos entre arquitetura, estrutura, MEP, civil e proteção contra incêndio. O organismo já produz pranchas reais via Vitruvius (Oscar) e recebe material das 6 disciplinas de Cardozo em formatos variados — nem sempre BIM nativo compatível de imediato.
- **10 categorias de problema como checklist de referência**, cada uma com severidade e localização exata: conflitos de coordenação, violação de código/norma, informação faltante, questões estruturais, choques de MEP, lacunas de segurança contra incêndio, acessibilidade, construtibilidade, divergência de cotas, itens de QA/QC em geral.
- **Saída acionável como padrão de entrega:** gerar automaticamente um **RFI (Request for Information)** a partir de cada problema encontrado, não só apontar a interferência — formato estruturado, coordenada exata, pedido de esclarecimento pronto, em vez de relatório solto.
- **Precedente real de risco que essa camada mitiga:** o Exame 2/Caso 1 de Portinari (10/08/2026) já identificou manualmente uma divergência desse tipo — 4 pavimentos na prancha vs. 3 pavimentos no quadro de áreas.

## ⚠️ O que essa camada NÃO cobre

Nenhuma ferramenta de mercado consultada (nem a de referência, nem as normas de compatibilização) cobre checagem de zoneamento específica do RIU/LICIN 2.0 — isso continua sendo responsabilidade exclusiva do Kelsen desde o Levantamento (`legal-base-legislativa-bairro`). A camada de QA/QC de compatibilização é sobre interferência física/técnica entre disciplinas, não conformidade legal.

## O que esta Skill NÃO indica

Não recomenda ferramenta específica para compra — Navisworks/Solibri/Trimble Connect e a ferramenta de referência (Helonic) são referências de mercado, não recomendação; quando o Gestor Fechamento for criado, cabe a ele reavaliar o mercado na data.

## Fontes
- spbim, WGB Engenharia, Thórus Engenharia (base normativa, 16/07/2026)
- Site oficial da ferramenta de referência, YC, cobertura de imprensa independente (achado de mercado, 11/08/2026)

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Wallenberg para formalizar, especialmente antes de o Gestor Fechamento ser criado. Relevante para o Gate 16 (Liberação de Obra).
