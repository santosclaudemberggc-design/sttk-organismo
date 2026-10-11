# COSCIP/CBMERJ — Decreto Estadual 42/2018: Segurança Contra Incêndio e Pânico no RJ

## Para qual Gestor / Agente serve
- **Landell** (Automação+Elétrica) — alarme de incêndio, detecção automática, iluminação de emergência, SPDA (para-raios), sinalização de saída
- **Baumgart** (Estrutural) — resistência ao fogo dos elementos estruturais, compartimentação horizontal/vertical, saídas de emergência (dimensionamento)
- **Cross-disciplina geral** — todo projeto de Construção do Zero no Estado do RJ precisa conhecer as fronteiras de aplicação do COSCIP, mesmo quando a edificação é isenta de aprovação pelo CBMERJ

## Status
avaliada — pronta para ratificação de Claudemberg (Cardozo, Drenagem Contínua 07/09/2026). v1.1 (04/09/2026, corrigida) — sem erro factual encontrado, fontes primárias citadas, escopo bem distinguido do Kelsen (isenção/exigibilidade) vs. Complementares (mapa de NTs por disciplina). Procede como conhecimento Trilha A para Landell e Baumgart. Lacunas remanescentes (texto integral das NTs mais relevantes, tabela do Anexo III, fronteira exata A-1/A-4 em lote compartilhado) são do mesmo tipo já aceito em Skills anteriores — o Agente lê a fonte primária antes de dimensionar, não impedem ratificação.

## ⚠️ Correção 04/09/2026 — não é lacuna nova, é expansão de conhecimento já existente

**A versão original desta Skill (v1.0) afirmava incorretamente que o COSCIP era "lacuna nunca coberta antes".** Isso é falso — o COSCIP/CBMERJ já foi identificado, apurado e fechado como pendência (`b10-coscip-nt107`) em **28/07/2026**, com auditoria dupla (Hely apura, Kelsen audita contra o primário) e está documentado na Skill `.claude/skills/legal-base-legislativa-bairro/SKILL.md`, seção "Segurança contra incêndio e pânico (CBMERJ/COSCIP)". O achado de 28/07 é mais rigoroso que esta Skill em um ponto (leu a NT 1-07 primária inteira, não só resumo secundário) e conclui: **edificação unifamiliar isolada (A-1) sem atividade econômica está isenta, sem obrigação residual** — questão fechada.

**O que esta Skill (v1.1) genuinamente adiciona, e por isso continua tendo valor:**
1. Mapa completo das Notas Técnicas do CBMERJ por relevância a cada disciplina de projeto (Landell/elétrica-alarme-SPDA, Baumgart/estrutural-resistência ao fogo) — a Skill de 28/07 não tinha esse detalhe, é conhecimento novo para Complementares.
2. Achado sobre **grupamentos (Divisão A-4)** — condomínios horizontais com mais de 6 unidades **não** seguem a mesma isenção do A-1 isolado. Isso NÃO foi apurado com o mesmo rigor da B10 (só fonte secundária, não leitura de artigo primário) — foi acrescentado como pista não fechada na Skill de Kelsen, pendente de apuração por Hely antes de aplicar a qualquer caso real.
3. **Relevância direta ao caso ativo Daniel-OB** (Condomínio Venice, grupamento A-4) — nunca antes levantada nas apurações de zoneamento desse caso.

**Divisão de competência, sem duplicidade:** a pergunta "esta edificação precisa de aprovação CBMERJ?" (isenção/exigibilidade) é conhecimento do Kelsen, vive em `legal-base-legislativa-bairro`. A pergunta "quando o COSCIP incide, o que cada disciplina de projeto precisa saber?" (mapa de Notas Técnicas por função) é conhecimento de Complementares, vive aqui.

## O que é o COSCIP

O **Código de Segurança Contra Incêndio e Pânico** do Estado do Rio de Janeiro é o regulamento estadual que define normas de segurança contra incêndio aplicáveis a edificações e áreas de risco no estado. O COSCIP vigente foi instituído pelo **Decreto Estadual nº 42, de 17 de dezembro de 2018** (publicado no DOERJ de 26/12/2018), que regulamenta o Decreto-Lei nº 247/1975.

### Estrutura normativa
- **Decreto 42/2018** — corpo principal: definições, classificações, obrigações gerais, fiscalização, penalidades
- **Anexo II** — classificação das edificações por ocupação (Grupos A a J)
- **Anexo III** — tabelas de exigências obrigatórias (medidas de segurança por tipo/porte de edificação)
- **46+ Notas Técnicas (NTs)** — regulamentação detalhada de cada medida, agrupadas em 5 categorias

### Diferença do anterior (Decreto-Lei 247/1975 + Decreto 897/1976)
O antigo COSCIP era um documento estático e monolítico. O novo modelo (Decreto 42/2018) adota o formato de **Notas Técnicas separadas por assunto**, permitindo atualização ágil de cada tema sem reescrever o código inteiro — mesmo modelo já praticado pelo Corpo de Bombeiros de São Paulo (IT-CB/PMSP).

---

## Classificação das Edificações — Grupo A (Residencial)

| Divisão | Descrição | Exemplos |
|---------|-----------|----------|
| A-1 | Habitação unifamiliar | Casas térreas ou sobrados |
| A-2 | Habitação multifamiliar | Edifícios de apartamentos |
| A-3 | Habitação coletiva | Alojamentos, pensões, mosteiros |
| A-4 | Grupamento de edificações | Condomínios horizontais, vilas |

**Escopo STTK (Construção do Zero):** tipicamente A-1 (unifamiliar isolada) ou A-4 (grupamento/condomínio horizontal tipo Venice/Daniel-OB).

---

## Isenções — Quando o CBMERJ NÃO exige aprovação

### Edificação unifamiliar isolada (A-1)
- **Residência unifamiliar privativa**: isenta de regularização junto ao CBMERJ
- **Residência unifamiliar no andar superior de imóvel misto** com até 2 pavimentos, acesso independente ao logradouro e sem interconexão entre ocupações: isenta

### Grupamento de edificações (A-4)
- Cada unidade unifamiliar dentro do grupamento, **quando analisada individualmente**, é isenta das exigências de medidas de segurança contra incêndio
- **Grupamentos de até 6 casas ou lotes**: isentos de Dispositivos Fixos de Prevenção de Incêndio

### O que NÃO é isento (mesmo sendo residencial)
- Modificações arquitetônicas que alterem **altura, área construída ou layout** da edificação
- Regularização de **parcelamentos e grupamentos** (o grupamento como empreendimento, não cada casa isolada)
- Grupamentos com **mais de 6 unidades**: exigem Dispositivos Fixos e potencialmente outras medidas do Anexo III

### Implicação prática para STTK
- **Casa unifamiliar isolada (A-1)** → provavelmente **isenta** de projeto e aprovação CBMERJ
- **Grupamento/condomínio horizontal (A-4) com >6 unidades** (ex.: Condomínio Venice, Daniel-OB) → **NÃO isento** — o empreendimento como um todo precisa de aprovação CBMERJ, mesmo que cada casa individual seja isenta
- **Sempre confirmar com o CBMERJ** a classificação real do empreendimento antes de assumir isenção — a fronteira entre A-1 e A-4 nem sempre é clara em loteamentos com acesso privativo compartilhado

---

## Notas Técnicas do CBMERJ — Mapa por Relevância

### Grupo 1 — Generalidades
| NT | Tema | Relevância STTK |
|----|------|----------------|
| NT 1-01 | Procedimentos administrativos (exigência de profissional CREA/CAU) | **Alta** — define quem pode assinar o projeto de incêndio |
| NT 1-04 | Classificação das edificações e áreas de risco quanto ao risco de incêndio | **Alta** — determina as exigências por tipo |
| NT 1-05 | Adequação de construções antigas (edificações existentes) | Baixa — STTK é construção nova |
| NT 1-06 | Processos administrativos | Média — procedimentos de aprovação junto ao CBMERJ |
| NT 1-07 | Atividades econômicas de baixo risco | Baixa — residencial, não comercial |

### Grupo 2 — Medidas de Segurança (maior impacto em projeto)
| NT | Tema | Agente principal | Relevância |
|----|------|-----------------|-----------|
| NT 2-01 | Saídas de emergência | Baumgart (dimensionamento) | **Alta** para A-4 |
| NT 2-02 | Planos de emergência | — | Média (obrigatório para grupamentos maiores) |
| NT 2-03 | Sistemas de detecção e alarme de incêndio | Landell | **Alta** para A-4 |
| NT 2-04 | Sinalização de emergência | Landell | Média |
| NT 2-05 | Iluminação de emergência | Landell | **Alta** para A-4 |
| NT 2-06 | Extintores de incêndio | — | Média (provisão básica) |
| NT 2-07 | Hidrantes e mangotinhos | — | Média (exigido em A-4 maiores) |
| NT 2-08 | SPDA (Sistema de Proteção contra Descargas Atmosféricas — para-raios) | Landell | **Alta** (NBR 5419) |
| NT 2-09 | Compartimentação horizontal | Baumgart | **Alta** para A-4 |
| NT 2-10 | Compartimentação vertical | Baumgart | Alta (se >2 pavimentos) |
| NT 2-11 a 2-14 | Sprinklers, pressurização, controle de fumaça | — | Baixa (geralmente não exigido para A-1/A-4 de pequeno porte) |
| NT 2-15 | Resistência ao fogo dos elementos de construção | Baumgart | **Alta** — TRRF (Tempo Requerido de Resistência ao Fogo) |
| NT 2-16 | Brigada de incêndio | — | Baixa para residencial |
| NT 2-17 a 2-20 | Gases, caldeiras, fogos de artifício, etc. | — | Não aplicável a residencial |

### Grupo 3 — Riscos Específicos
| NT | Tema | Relevância |
|----|------|-----------|
| NT 3-02 | Gás predial (GLP/GN) | **Alta** — instalação de gás é obrigação de projeto |
| NT 3-03 | Geradores de emergência | Baixa para A-1, Média para A-4 |
| NT 3-01, 3-04 a 3-07 | Cozinhas profissionais, subestações, líquidos inflamáveis, heliponto | Não aplicável a residencial |

### Grupo 4 — Estruturas Especiais
| NT | Tema | Relevância |
|----|------|-----------|
| NT 4-06 | Garagens | **Média** — se o projeto inclui garagem coberta (cálculo de ventilação, combate a incêndio) |
| NT 4-10 | Canteiro de obras | **Média** — segurança durante a construção |
| Demais (4-01 a 4-05, 4-07 a 4-09) | Quiosques, patrimônio histórico, explosivos, armazenagem, túneis | Não aplicável |

### Grupo 5 — Eventos
Não aplicável a projetos de construção residencial.

---

## Integração com LICIN 2.0 (LC 270/2024)

- A aprovação do CBMERJ é **trâmite paralelo** ao licenciamento urbanístico (SMDU/LICIN 2.0), não substitutivo
- O Habite-se / Certidão de Conclusão de Obra (CCO) exige a apresentação do **Laudo de Exigências Cumpridas** (antigo "AVCB") emitido pelo CBMERJ
- O projeto de incêndio deve ser **aprovado pelo CBMERJ antes do início da obra** (condição para Licença de Obras)
- Profissional responsável: engenheiro civil ou engenheiro de segurança do trabalho registrado no CREA-RJ (ou arquiteto inscrito no CAU para aspectos de saídas de emergência e compartimentação não-estrutural)

---

## O que esta Skill NÃO cobre (lacunas conhecidas)

1. **Tabela completa do Anexo III** — a tabela de exigências por tipo/porte precisa ser consultada no decreto original, não foi reproduzida aqui (direitos autorais + extensão). Fonte: [COSCIP compilado — CBMERJ](https://www.cbmerj.rj.gov.br/wp-content/uploads/2024/05/DECRETO_42_2018_COSCIP_COMPILADO.pdf)
2. **Texto integral das 46+ NTs** — cada NT é um documento próprio publicado pelo CBMERJ. As mais relevantes (NT 2-03, 2-05, 2-08, 2-15) devem ser lidas por Landell/Baumgart antes de dimensionar
3. **Fronteira exata entre A-1 isento e A-4 não isento** para configurações de lote com acesso privativo compartilhado (ex.: 4 casas com portaria mas lotes individuais) — requer consulta ao CBMERJ caso a caso
4. **Atualizações pós-2024** — NTs são atualizadas periodicamente por Portaria do CBMERJ; confirmar versão vigente antes de aplicar

---

## Fontes

| Fonte | URL | Data verificação |
|-------|-----|-----------------|
| COSCIP compilado (Decreto 42/2018) — PDF oficial CBMERJ | https://www.cbmerj.rj.gov.br/wp-content/uploads/2024/05/DECRETO_42_2018_COSCIP_COMPILADO.pdf | 04/09/2026 |
| Nota sobre Novo Portal do Requerente CBMERJ 2026 | https://www.cbmerj.rj.gov.br/wp-content/uploads/2026/01/NOTA-DGST-001-2026-Novo-Portal-do-Requerente.pdf | 04/09/2026 |
| Artigo CREA-RJ Ângulos sobre o COSCIP | https://angulos.crea-rj.org.br/o-novo-coscip-codigo-de-seguranca-contra-incendio-e-panico-do-cbmerj-e-sua-importancia-para-engenharia-de-seguranca/ | 04/09/2026 |
| NT 1-04 Classificação de edificações | https://www.cbmerj.rj.gov.br/wp-content/uploads/2022/04/NT-1-04-Classificacao-das-edificacoes-e-areas-de-risco-quanto-ao-risco-de-incendio.pdf | 04/09/2026 |
| NT 2-05 Iluminação de emergência (3ª edição 2023) | https://www.cbmerj.rj.gov.br/wp-content/uploads/2024/05/NT2-05_3Edio_2023.pdf | 04/09/2026 |
| LegNet — notas técnicas publicadas CBMERJ | https://legnet.com.br/blog/notas-tecnicas-cbmerj-atualizacoes-e-impactos/ | 04/09/2026 |
| LegisWeb — Decreto 42/2018 | https://www.legisweb.com.br/legislacao/?id=372879 | 04/09/2026 |
