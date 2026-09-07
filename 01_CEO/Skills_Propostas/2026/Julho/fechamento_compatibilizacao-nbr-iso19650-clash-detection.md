---
name: skill-proposta-fechamento-compatibilizacao-nbr
description: "PROPOSTA — compatibilização BIM segundo NBR ISO 19650/NBR 15965, clash avoidance, matriz GUT de priorização, e camada de QA/QC multidisciplinar via leitura direta de PDF 2D (inteligência extraída da Helonic, YC Fall 2025), para o futuro Gestor Fechamento"
metadata:
  type: skill_proposta
  status: ratificada
  ratificada_em: 2026-09-03
  ratificada_por: "Claudemberg, rodada de auditoria com Wallenberg"
  gestor_alvo: "Gestor Fechamento — ainda não implantado"
  agente_alvo: "futuro Agente de Compatibilização (já tem MCP oficial da Autodesk)"
  data: 2026-07-16
  atualizado: 2026-09-03
  historico_correcao: "Criada 16/07/2026 com gestor_alvo errado (Gestor Complementares). Corrigido 29/07/2026 no índice para 'sem Gestor definido' — mas o fluxograma oficial (sttickler_fluxograma_oficial.md) já confirmava, na mesma data 29/07/2026, que Compatibilização é do Gestor Fechamento. Erro de propagação identificado e corrigido por Claudemberg em 03/09/2026. Nesta mesma correção, mesclada a inteligência conceitual da proposta Helonic (item 49 da pauta 31/08/2026, arquivada por falta de MCP) — ver Seção 2."
---

# Skill proposta: Compatibilização de Projetos — normas + inteligência de QA/QC multidisciplinar

## Para quem é
**Gestor Fechamento**, ainda não implantado — proposta fica pronta para quando ele for criado. Serve o futuro **Agente de Compatibilização**, que segundo o `CLAUDE_wallenberg_slice.md` já tem MCP oficial da Autodesk pronto (leitura/análise) — um dos Agentes que "produzem de verdade", não só coordenam. Compatibilização é a etapa que recebe o output das 6 disciplinas de Cardozo/Complementares e antecede Projeto Executivo → Orçamento Executivo → Liberação de Obra (Gate 16), todas do Fechamento (decidido por Claudemberg em 29/07/2026, confirmado em `sttickler_fluxograma_oficial.md`).

## Seção 1 — Base normativa (pesquisa original, 16/07/2026)
Pesquisa de mercado confirma que a compatibilização BIM profissional no Brasil hoje é estruturada por duas normas: **NBR ISO 19650** (série que rege gestão da informação em BIM ao longo do ciclo de vida) e **NBR 15965** (classificação da informação da construção). Fontes técnicas (spbim, WGB Engenharia, Thórus Engenharia) descrevem três práticas que a Skill ensinaria ao Agente de Compatibilização:

1. **Clash detection automatizado**: ferramentas de mercado (Navisworks, Solibri Model Checker, Trimble Connect — via Autodesk Construction Cloud, que já é o ecossistema do MCP existente) localizam interferências entre disciplinas (Estrutural, Elétrico, Hidrossanitário, Automação, Interiores, Paisagismo) antes da obra.
2. **Clash avoidance**: prevenção na origem — projetar cada disciplina já pensando na interação com as outras reduz o volume de conflitos encontrados depois, em vez de só corrigir na convergência.
3. **Priorização por matriz GUT** (Gravidade, Urgência, Tendência) quando há muitas interferências simultâneas — decide por onde começar a resolver, em vez de tratar tudo como igualmente crítico.

Fontes de mercado relatam retorno de R$ 30-40 para cada R$ 1 investido em compatibilização correta, e redução de retrabalho superior a 90% — argumento de peso para justificar tempo dedicado a essa etapa antes do Gate 16.

## Seção 2 — Inteligência extraída da Helonic (achado 11/08/2026, item 49 pauta 31/08/2026)
A Skill Helonic original foi proposta para Oscar (QA/QC de prancha antes de Portinari) e **arquivada** por Claudemberg em 03/09/2026 por falta de conector MCP/API pública. A **ferramenta em si não é adotável hoje** — mas o **conceito e a lista de capacidades** que ela materializa é diretamente aplicável ao que o futuro Agente de Compatibilização do Fechamento precisa fazer, e complementa a Seção 1 (que é normativa/processual, não descreve *como* uma IA executaria a checagem):

- **Mecanismo de referência:** ler o conjunto de pranchas em **PDF 2D** — sem exigir modelo BIM pronto — e apontar conflitos entre arquitetura, estrutura, MEP (instalações), civil e proteção contra incêndio. Relevante porque o organismo já produz pranchas reais via Vitruvius (Oscar) e recebe material das 6 disciplinas de Cardozo em formatos variados — nem sempre BIM nativo compatível de imediato.
- **10 categorias de problema como checklist de referência**, cada uma com severidade e localização exata: conflitos de coordenação, violação de código/norma, informação faltante, questões estruturais, choques de MEP, lacunas de segurança contra incêndio, acessibilidade, construtibilidade, divergência de cotas, itens de QA/QC em geral. Útil como **estrutura de categorização** para o Agente de Compatibilização classificar o que encontra, mesmo sem usar a ferramenta Helonic em si.
- **Saída acionável como padrão de entrega:** gerar automaticamente um **RFI (Request for Information)** a partir de cada problema encontrado, não só apontar a interferência — modelo de output que a Skill do Agente de Compatibilização deveria adotar (formato estruturado, coordenada exata, pedido de esclarecimento pronto), em vez de relatório solto.
- **Precedente real de risco que essa camada mitiga:** Exame 2/Caso 1 de Portinari (10/08/2026) já identificou manualmente uma divergência desse tipo — 4 pavimentos na prancha vs. 3 pavimentos no quadro de áreas. Esse é exatamente o tipo de erro que uma checagem automatizada de coordenação/divergência de cotas capturaria antes da entrega.
- **Ressalva que se mantém:** nenhuma ferramenta de mercado consultada (nem Helonic, nem as citadas na Seção 1) cobre checagem de zoneamento específica do RIU/LICIN 2.0 — isso continua sendo responsabilidade exclusiva do Kelsen desde o Levantamento (`legal-base-legislativa-bairro`). A camada de QA/QC de compatibilização é sobre interferência física/técnica entre disciplinas, não conformidade legal.

## O que esta Skill NÃO cobre
- Não substitui a checagem de zoneamento do Kelsen/Hely.
- Não indica ferramenta específica a adotar — Navisworks/Solibri/Trimble Connect (Seção 1) e Helonic (Seção 2) são referências de mercado, não recomendação de compra; quando o Gestor Fechamento for criado, cabe a ele reavaliar o mercado na data (ferramentas e conectores mudam rápido, mesmo tratamento dado a toda Skill sem MCP confirmado).

## Fontes
**Seção 1** (16/07/2026):
- [O que é o Clash Detection (Detecção de Colisão) no BIM? — spbim](https://spbim.com.br/o-que-e-o-clash-detection/)
- [BIM Clash Detection — WGB Arquitetura e Engenharia](https://www.wgbengenharia.com/bim-clash-detection-deteccao-automatica-de-interferencias-3d/)
- [Análise automatizada clash detection através de regras de verificação — Thórus Engenharia](https://thorusengenharia.com.br/clash-detection/)

**Seção 2** (11/08/2026, ver dossiê original arquivado em `arquitetura_helonic-qaqc-clash-detection-multidisciplinar.md`):
- https://helonic.com/ , https://helonic.com/about , https://helonic.com/for/architects/qa-qc
- https://www.ycombinator.com/companies/helonic (confirmação independente, lote Fall 2025)
- https://www.marketscale.com/industries/engineering-and-construction/y-combinators-2026-real-estate-and-construction-cohort-bets-big-on-ai-agents-and-construction-intelligence

## Governança
RATIFICADA em 03/09/2026 por Claudemberg (rodada de auditoria com Wallenberg). **Convertida em Skill real em 03/09/2026:** `.claude/skills/compatibilizacao-projetos/SKILL.md`.
