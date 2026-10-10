---
name: verificacao-automatica-conformidade-bim
description: Automated Compliance Checking (ACC) — verificação automática de modelo BIM contra norma/parâmetro (afastamento, dimensão de cômodo, taxa de ocupação, acessibilidade), metodologia RASE + openBIM IDS. Distinta de clash detection (que compara disciplinas entre si). Use sempre que o futuro Agente de Compatibilização precisar avaliar se um projeto atende parâmetro normativo automaticamente, ou discutir formalização de regra normativa em formato lido por máquina — mesmo que o pedido só mencione "conformidade", "checagem automática" ou "code checking", sem citar a metodologia pelo nome.
---

# Verificação Automática de Conformidade Normativa em BIM (ACC)

Skill de Inteligência Técnica da área Fechamento (Gestor ainda não implantado). Mesmo Agente-alvo da Skill `compatibilizacao-projetos`, mas **mecanismo diferente e complementar, não substituto**: clash detection compara disciplinas entre si; ACC compara o modelo **contra a norma/parâmetro**. São duas verificações de natureza distinta — não fundir.

## O que é ACC

Verificação automática de um modelo BIM contra regras pré-definidas (dimensões, distâncias, superfícies, acessibilidade e outros parâmetros de projeto), em vez de conferência manual peça por peça.

## Metodologia emergente

Marcação semântica **RASE** (Requirement, Applicability, Selection, Exception) combinada com o padrão **openBIM IDS** (Information Delivery Specification), para formalizar regras normativas em formato lido por máquina, permitindo verificação automatizada contra o modelo.

## ⚠️ Estado real da técnica — não é ferramenta pronta hoje

A literatura técnica (SIBRAGEC/ANTAC, IEEE, artigos técnicos italianos) descreve a área como ainda enfrentando fragmentação de fontes normativas, baixa interoperabilidade de dados e dificuldade de traduzir linguagem humana (texto de norma) para formato de máquina. IA está sendo somada para interpretar o *contexto* de aplicação da regra, não só comparar número com limite — mas isso é fronteira de pesquisa, **não ferramenta comercial madura para uso direto hoje**.

## Por que interessa mesmo sem ferramenta pronta

É o mesmo problema estrutural que o organismo já enfrenta "na unha": verificar se um projeto atende parâmetro urbanístico/norma técnica é exatamente o que Kelsen/Hely fazem manualmente para o Legal, e o que o futuro Agente de Compatibilização precisaria fazer para as demais disciplinas. Vale revisitar quando surgir ferramenta comercial concreta (ex.: plugin Revit/IDS validator) madura o suficiente.

**Ao desenhar o Agente de Compatibilização:** avaliar se vale aplicar a mesma lógica de "regra formalizada e verificável" também ao trabalho do Kelsen/Hely (parâmetro urbanístico), não só às disciplinas de Complementares — mesmo princípio, dois domínios.

## O que esta Skill NÃO indica
Nome de produto/plugin específico para comprar ou testar — a pesquisa não encontrou ferramenta comercial nomeada madura o bastante para recomendar.

## Fontes
- SIBRAGEC/ANTAC — "Verificação automática de conformidade: a busca da síntese nos requisitos"
- 01building — "BIM e automazione normativa"
- IEEE Xplore — "A Review on BIM-based automated code compliance checking system"
- arXiv — "Automating Geometry-Intensive Compliance Checking in BIM"
- Confiança **média-alta** para o conceito/metodologia RASE-IDS (múltiplas fontes convergem); confiança **baixa** para maturidade comercial.

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Wallenberg para formalizar, especialmente antes de o Gestor Fechamento ser criado.
