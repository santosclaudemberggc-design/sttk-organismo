---
name: skill-proposta-complementares-verificacao-automatica-conformidade
description: "PROPOSTA — verificação automática de conformidade normativa em modelos BIM (Automated Compliance Checking, metodologia RASE + openBIM IDS), distinta de clash detection, para o futuro Agente de Compatibilização"
metadata:
  type: skill_proposta
  status: proposta_pendente_reuniao_mensal
  gestor_alvo: Gestor Complementares — não implantado
  agente_alvo: futuro Agente de Compatibilização (já tem MCP oficial da Autodesk)
  data: 2026-07-29
---

# Skill proposta: Verificação Automática de Conformidade Normativa em BIM (ACC)

## Para quem é
Gestor **Complementares** — ainda não implantado (proposta fica pronta para quando ele for criado). Mesmo Agente-alvo da Skill de 16/07/2026 (compatibilização/clash detection), mas **mecanismo diferente e complementar, não substituto**: clash detection compara disciplinas entre si (Estrutural x Elétrico x Hidrossanitário); Automated Compliance Checking (ACC) compara o modelo **contra a norma/parâmetro** (afastamento mínimo, dimensão de cômodo, taxa de ocupação, acessibilidade). São duas verificações de natureza distinta — não fundir numa Skill só (Princípio 9 — clareza de escopo).

## O que ensina/entrega — é mapa, não cópia de parâmetro
Regra fixada em 20/07/2026 (ver `legal-base-legislativa-bairro`): esta Skill aponta o método e onde a técnica é discutida, não trava número nem substitui verificação humana.

1. **O que é ACC:** verificação automática de um modelo BIM contra regras pré-definidas (dimensões, distâncias, superfícies, acessibilidade e outros parâmetros de projeto), em vez de conferência manual peça por peça. É uma categoria de ferramenta distinta de clash detection, embora ambas rodem sobre o mesmo modelo BIM.
2. **Metodologia de referência que a literatura técnica aponta como caminho emergente:** marcação semântica **RASE** (Requirement, Applicability, Selection, Exception) combinada com o padrão **openBIM IDS** (Information Delivery Specification) para formalizar regras normativas em formato lido por máquina, permitindo verificação automatizada contra o modelo.
3. **Estado real da técnica em 2026, sem inflar expectativa:** a própria literatura (SIBRAGEC/ANTAC, IEEE, artigos técnicos italianos e revisões recentes) descreve a área como ainda enfrentando fragmentação de fontes normativas, baixa interoperabilidade de dados e dificuldade de traduzir linguagem humana (texto de norma) para formato de máquina. IA está sendo somada para interpretar o *contexto* de aplicação da regra, não só comparar número com limite — mas isso ainda é fronteira de pesquisa, não ferramenta comercial madura e pronta para uso direto pela Sttickler hoje.
4. **Por que interessa ao organismo mesmo sem ferramenta pronta:** é o mesmo problema estrutural que o organismo já enfrentou "na unha" — verificar se um projeto atende parâmetro urbanístico/norma técnica (zona, afastamento, taxa de ocupação) é exatamente o que a equipe de Kelsen/Hely faz manualmente hoje para o Legal, e o que o futuro Agente de Compatibilização precisaria fazer para as demais disciplinas. Vale revisitar esta Skill quando surgir uma ferramenta comercial concreta (ex.: plugin Revit/IDS validator) madura o suficiente para avaliação real — hoje é mapa de direção, não uma ferramenta para adotar.

## O que esta Skill deliberadamente não cobre
- **Nome de produto/plugin específico para comprar ou testar** — a pesquisa de hoje não encontrou ferramenta comercial nomeada madura o bastante para recomendar; não inventar recomendação de compra (Princípio 15 — não gerar Skill por obrigação de preencher).
- **Sobreposição com a Skill de clash detection (16/07/2026)** — deliberadamente não repetida aqui; as duas Skills se complementam mas cobrem fenômenos diferentes.

## Fontes e confiabilidade
- [Verificação automática de conformidade: a busca da síntese nos requisitos — SIBRAGEC/ANTAC](https://eventos.antac.org.br/sibragec/article/view/7804)
- [BIM e automazione normativa: verso il Code Checking intelligente basato su AI — 01building](https://www.01building.it/bim-e-automazione-normativa-verso-il-code-checking-intelligente-basato-su-ai/)
- [A Review on BIM-based automated code compliance checking system — IEEE Xplore](https://ieeexplore.ieee.org/document/8002486/)
- [Automating Geometry-Intensive Compliance Checking in BIM: Graph-Based Semantic Reasoning Framework — arXiv](https://arxiv.org/pdf/2606.12065)
- Pesquisado em 29/07/2026, rotina diária do Wallenberg. Confiança **média-alta** para o conceito e a metodologia RASE/IDS (múltiplas fontes técnicas independentes convergem); confiança **baixa** para maturidade comercial (nenhuma fonte descreve produto pronto e amplamente adotado no Brasil hoje) — tratar como direção de pesquisa, não como capacidade disponível.

## Ação proposta
Quando o Gestor Complementares e o Agente de Compatibilização forem criados: (a) manter esta Skill como referência de metodologia (RASE/IDS), revisitando a cada rodada apenas se aparecer ferramenta comercial madura nova; (b) ao desenhar o Agente, avaliar se vale a pena aplicar a mesma lógica de "regra formalizada e verificável" também ao trabalho do Kelsen/Hely (parâmetro urbanístico), não só às disciplinas de Complementares — mesmo princípio, dois domínios.

## Governança
Proposta pendente — não cria o Gestor Complementares nem qualquer Agente (decisão estrutural, fora do escopo desta rotina). Fica arquivada para quando Claudemberg decidir avançar a construção desse Gestor (Princípio 13).
