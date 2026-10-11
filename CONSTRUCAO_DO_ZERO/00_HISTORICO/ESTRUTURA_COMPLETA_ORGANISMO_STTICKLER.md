# ESTRUTURA COMPLETA DO ORGANISMO STTICKLER
## Referência consolidada para instanciamento de Gestores e Agentes pelo CEO

**Escopo:** Este documento cobre exclusivamente o produto **Construção do Zero**. Documentos e POPs específicos de Reforma, Retrofit ou Home Staging foram deliberadamente excluídos.

**Fonte:** POPs, formulários, planilhas e documentos institucionais reais da Sttickler Empreendimentos, mais o fluxograma oficial de execução de projetos.

---

## 1. FLUXOGRAMA OFICIAL DE EXECUÇÃO

Fonte: *DP - FLUXOGRAMA DE EXECUÇÃO DOS PROJETOS* (Figma)

### 1.1 Legenda do fluxograma

| Cor | Significado |
|---|---|
| Verde | Validação da Coordenação (Gate Interno) |
| Amarelo | Afazeres de Terceiros |
| Azul | Validação do Cliente (Gate Externo) |

### 1.2 Entrada do fluxo

1. Receber aceite formal da proposta (contrato + condições + escopo)
2. Liberar início dos projetos no sistema

### 1.3 Bloco ARQUITETURA (sequencial)

Cada etapa segue o padrão: **Desenvolvimento → [Etapa] Desenvolvido → Validação (SIM/NÃO) → próxima etapa**

1. Desenvolvimento do Levantamento → Levantamento Desenvolvido → SIM/NÃO
2. Desenvolvimento do Briefing → Briefing Desenvolvido → SIM/NÃO
3. Desenvolvimento do Estudo Preliminar → Estudo Preliminar Desenvolvido → SIM/NÃO
4. Desenvolvimento do Anteprojeto → Anteprojeto Desenvolvido → SIM/NÃO

### 1.4 Bifurcação: Projeto Legal + COMPLEMENTARES (paralelos)

Após Anteprojeto aprovado, o fluxo se ramifica em:

**Projeto Legal** (sequência própria):
- Desenvolvimento do Projeto Legal → Projeto Legal Desenvolvido → SIM/NÃO

**COMPLEMENTARES** (6 disciplinas em paralelo, cada uma com o mesmo padrão de validação SIM/NÃO):
- Desenvolvimento do Projeto Estrutural → Projeto Estrutural Desenvolvido
- Desenvolvimento do Projeto Elétrico → Projeto Elétrico Desenvolvido
- Desenvolvimento do Projeto de Automação → Projeto de Automação Desenvolvido
- Desenvolvimento do Projeto de Interiores → Projeto de Interiores Desenvolvido
- Desenvolvimento do Projeto Hidrossanitário → Projeto Hidrossanitário Desenvolvido
- Desenvolvimento do Projeto de Paisagismo → Projeto de Paisagismo Desenvolvido

### 1.5 Convergência final (sequencial)

Após Projeto Legal + todos os Complementares aprovados:

1. Desenvolvimento da Compatibilização → Compatibilização Desenvolvida → SIM/NÃO
2. Desenvolvimento do Projeto Executivo → Projeto Executivo Desenvolvido → SIM/NÃO
3. Orçamento Executivo e Premissas → SIM/NÃO
4. Liberação de Obra → **OBRA PODE COMEÇAR**

---

## 2. MAPEAMENTO POP ↔ ETAPA DO FLUXO ↔ GESTOR RESPONSÁVEL

| # | Etapa do Fluxo | Código POP | Gestor Responsável |
|---|---|---|---|
| 1 | Levantamento | POP-PROJ-01 | Arquitetura |
| 2 | Briefing | POP-PROJ-02 | Arquitetura |
| 3 | Estudo Preliminar | POP-ARQ-EP-01 | Arquitetura |
| 4 | Anteprojeto | POP-ARQ-AP-01 | Arquitetura |
| 5 | Projeto Legal | POP-ARQ-PL-01 | Legal |
| 6 | Projeto Estrutural | POP-EST-01 | Complementares |
| 7 | Projeto Elétrico | POP-ELT-01 | Complementares |
| 8 | Projeto de Automação | (ver seção 3.8) | Complementares |
| 9 | Projeto de Interiores | POP-INT-02 | Complementares |
| 10 | Projeto Hidrossanitário | POP-HID-01 | Complementares |
| 11 | Projeto de Paisagismo | POP-PAI-01 | Complementares |
| 12 | Compatibilização Final | POP-COMP-01 | Fechamento |
| 13 | Projeto Executivo | (ver seção 3.13) | Fechamento |
| 14 | Orçamento Executivo/Premissas | POP-ORC-15 | Fechamento |
| 15 | Liberação de Obra | POP-OBR-16 | Fechamento |

**Nota:** os POPs de Projeto de Automação e Projeto Executivo existem na base de conhecimento do Project, mas seu conteúdo detalhado não foi extraído neste documento (não retornados nas buscas realizadas). Recomenda-se confirmar seus códigos oficiais e conteúdo completo antes de codificar os Agentes correspondentes.

---

## 3. RESUMO DE CADA POP (por etapa)

### 3.1 POP – Levantamento Arquitetônico (POP-PROJ-01)
- **Disciplina:** Arquitetura
- **Responsável:** Arquiteto / Técnico de Levantamento
- **Objetivo:** Coleta rigorosa de dados físicos, técnicos e documentais do terreno — base fidedigna para todas as etapas seguintes ("padrão Erro Zero").
- **Entradas obrigatórias:** Escritura/RGI atualizado, Levantamento Topográfico (se houver), EVL inicial.
- **Ferramentas:** Trena laser, câmera 360°, drone (opcional), Ficha de Levantamento de Campo.
- **Aprovação final:** Diretor de Engenharia (Claudemberg).

### 3.2 POP – Gerenciamento do Briefing Arquitetônico (POP-PROJ-02)
- **Disciplina:** Arquitetura
- **Responsável:** Arquiteto Coordenador
- **Objetivo:** Transformar expectativas do cliente em requisitos técnicos objetivos, fundamentando o Estudo Preliminar.
- **Entradas obrigatórias:** POP-PROJ-01 validado, EVL/EVT concluídos, contrato assinado.
- **Ferramentas:** Questionário de Briefing Sttickler, Painel de Referências (Moodboard), Caderno de Briefing.
- **Aprovação final:** Diretor de Engenharia (Claudemberg).

### 3.3 POP – Estudo Preliminar (POP-ARQ-EP-01)
- **Disciplina:** Arquitetura
- **Objetivo:** Desenvolver e validar a solução arquitetônica inicial (conceito, implantação, volumetria, layout) antes do detalhamento técnico.
- **Entradas obrigatórias:** Briefing aprovado, levantamento completo, EVL/diretrizes legais.
- **Gate externo:** Apresentação ao cliente + Formulário do Estudo Preliminar.
- **Gate interno:** Validação da Coordenação (Aprovado / Aprovado com ressalvas / Reprovado).
- **Critério de conclusão:** Aprovado → libera Anteprojeto.

### 3.4 POP – Anteprojeto (POP-ARQ-AP-01)
- **Disciplina:** Arquitetura
- **Objetivo:** Consolidar a solução do Estudo Preliminar em nível técnico suficiente para validação espacial, volumétrica e legal preliminar.
- **Entradas obrigatórias:** Estudo Preliminar aprovado, Briefing validado, levantamentos completos, diretrizes legais básicas.
- **Entregas técnicas:** Plantas de todos os pavimentos, implantação, cobertura, cortes, fachadas preliminares, quadro de áreas, layout humanizado.
- **Critério de conclusão:** Aprovado → libera Projeto Legal e/ou Projeto Executivo.

### 3.5 POP – Projeto Legal (POP-ARQ-PL-01)
- **Disciplina:** Arquitetura (execução terceirizada para legalização)
- **Objetivo:** Garantir que o projeto atenda à legislação vigente e esteja apto para aprovação em órgãos competentes.
- **Entradas obrigatórias:** Anteprojeto aprovado, Briefing validado, levantamentos, legislação urbana vigente.
- **Inclui:** ART/RRT, protocolo junto ao órgão licenciador, acompanhamento de exigências.
- **Critério de conclusão:** Aprovado → libera Projeto Executivo.

### 3.6 POP – Projeto Estrutural (POP-EST-01)
- **Disciplina:** Estrutural
- **Responsável:** Engenheiro Estrutural
- **Objetivo:** Escolha da tipologia estrutural e desenvolvimento garantindo segurança, estabilidade, desempenho e compatibilidade.
- **Entradas obrigatórias:** Briefing Arquitetônico + Briefing Estrutural validados, projeto arquitetônico base, sondagem/topografia.
- **Entregas técnicas:** Fundação, lajes, vigas, pilares, cortes estruturais, detalhamento de armaduras, memorial de cálculo.
- **Compatibiliza com:** Arquitetura, Elétrico, Hidrossanitário.
- **Critério de conclusão:** Aprovado → libera Compatibilização Final / Obra.

### 3.7 POP – Projeto Elétrico (POP-ELT-01)
- **Disciplina:** Instalações Elétricas
- **Objetivo:** Segurança, desempenho, conformidade normativa (NBR 5410), compatibilidade com demais sistemas.
- **Entradas obrigatórias:** Briefing Arquitetônico + Estrutural + Elétrico validados, projeto arquitetônico base (Anteprojeto), diretrizes de automação (se aplicável).
- **Entregas técnicas:** Iluminação, tomadas, força, diagrama unifilar, quadro de cargas, aterramento/SPDA.
- **Compatibiliza com:** Arquitetura, Estrutural, Hidrossanitário, Automação.
- **Critério de conclusão:** Aprovado → libera Compatibilização Final / Obra.

### 3.8 POP – Projeto de Automação
- **Status:** Documento existe na base de conhecimento, mas conteúdo detalhado não foi recuperado nesta consolidação.
- **Contexto conhecido (via menções em outros POPs):** compatibiliza com Elétrico e Interiores; no fluxo de Reforma, aparece nas atividades de "instalações" junto com lógica, som e CFTV.
- **Ação recomendada:** buscar o documento diretamente na base de conhecimento antes de codificar o Agente de Automação.

### 3.9 POP – Projeto de Interiores (POP-INT-02)
- **Disciplina:** Arquitetura de Interiores
- **Objetivo:** Funcionalidade dos ambientes, coerência estética, definição de materiais/mobiliários, base executiva.
- **Aplica-se a:** Construção do Zero, Reforma, Retrofit, Home Staging (POP compartilhado entre produtos).
- **Entregas técnicas:** Conceito, layout decorativo, marcenaria executiva, marmoraria, iluminação decorativa, 3D humanizadas.
- **Compatibiliza com:** Arquitetura, Elétrico, Hidrossanitário, Ar-condicionado, Automação.
- **Critério de conclusão:** Validado por Cliente + Coordenação → libera Compatibilização Final / Executivo.

### 3.10 POP – Projeto Hidrossanitário (POP-HID-01)
- **Disciplina:** Instalações Hidrossanitárias
- **Objetivo:** Abastecimento de água fria/quente, escoamento de esgoto, drenagem pluvial, conformidade normativa (NBR 5626, NBR 8160).
- **Entradas obrigatórias:** Briefings de Arquitetura + Estrutural + Elétrico + Hidrossanitário validados, projeto arquitetônico base.
- **Entregas técnicas:** Água fria, água quente, esgoto sanitário, águas pluviais, memorial descritivo hidrossanitário.
- **Compatibiliza com:** Arquitetura (níveis/shafts), Estrutural (passagens), Elétrico.
- **Critério de conclusão:** Aprovado → libera Compatibilização Final / Obra.

### 3.11 POP – Projeto de Paisagismo (POP-PAI-01)
- **Disciplina:** Paisagismo
- **Objetivo:** Integração entre áreas externas e arquitetura, funcionalidade, adequação climática/ambiental.
- **Aplica-se a:** Construção do Zero, Reforma, Retrofit, Home Staging (POP compartilhado entre produtos).
- **Entregas técnicas:** Conceito paisagístico, áreas verdes, circulação externa, paginação de pisos, espécies vegetais, drenagem superficial, iluminação externa.
- **Compatibiliza com:** Arquitetura, Elétrico (iluminação externa), drenagem/hidráulica externa.
- **Critério de conclusão:** Aprovado → libera Compatibilização Final / Execução Externa.

### 3.12 POP – Compatibilização Final de Projetos (POP-COMP-01)
- **Etapa do fluxo:** Após aprovação de todos os projetos técnicos, antes da liberação para obra.
- **Objetivo:** Garantir que todos os projetos estejam alinhados, sem interferências construtivas, coerentes em níveis/eixos/dimensionamentos.
- **Escopo:** Arquitetônico, Estrutural, Elétrico, Hidrossanitário, Automação, Climatização, outros complementares.
- **Interferências verificadas:** Estrutura×Arquitetura, Estrutura×Hidrossanitário, Estrutura×Elétrico, Hidrossanitário×Elétrico, Forros×instalações, Shafts/prumadas, Pé-direito útil, Passagens em vigas/lajes, Níveis/cotas.
- **Regra crítica:** obra não pode iniciar com interferência pendente. Após aprovação, projeto é "congelado" para execução.
- **Este é o Gate 13 do sistema — corresponde ao bloqueador crítico já implementado em `validar_gate()` no CEO.**
- **Critério de conclusão:** Aprovado (Coordenação + Cliente) → libera Obra.

### 3.13 POP – Projeto Executivo
- **Status:** Documento existe na base de conhecimento, mas conteúdo detalhado não foi recuperado nesta consolidação.
- **Contexto conhecido (via menções em outros POPs):** etapa entre Projeto Legal/Compatibilização e Orçamento Executivo; mencionado como "POP – Projeto Executivo (Arquitetura)" em Documentos Relacionados de outros POPs.
- **Ação recomendada:** buscar o documento diretamente na base de conhecimento antes de codificar o Agente responsável.

### 3.14 POP – Orçamento Executivo e Memorial de Premissas (POP-ORC-15)
- **Disciplina:** Engenharia de Custos / Coordenação de Projetos
- **Responsável:** Orçamentista / Engenheiro de Custos
- **Etapa do fluxo:** Pós-Compatibilização Final (Gate 13)
- **Objetivo:** Elaboração do orçamento executivo final, alinhado ao Projeto Executivo compatibilizado, com separação rigorosa Material × Mão de Obra (padrão PCI Caixa Econômica Federal).
- **Entradas obrigatórias:** Projeto Executivo finalizado/carimbado/compatibilizado (Gate 13), fichas técnicas, laudo de sondagem, logística de canteiro.
- **Ferramentas:** Formulário 15, Planilha PCI Caixa, Memorial de Premissas.
- **Regra:** cotações com mínimo 3 fornecedores homologados para itens de alto valor (marmoraria, esquadrias, marcenaria, automação).
- **Aprovação final:** Diretor de Engenharia (Claudemberg) — auditoria técnica de custos e margens/BDI.

### 3.15 POP – Liberação de Obra (POP-OBR-16)
- **Disciplina:** Engenharia de Obras / Coordenação
- **Responsável:** Coordenador de Engenharia / Engenheiro de Obra
- **Etapa do fluxo:** Após aprovação do Orçamento Executivo (Gate 15) — **este é o Gate 16, o segundo bloqueador crítico do sistema.**
- **Objetivo:** Garantir que condicionantes administrativas, jurídicas, financeiras e técnicas estejam 100% atendidas antes do início físico da obra.
- **Inclui:** Auditoria de licenciamento (Prefeitura + Condomínio), validação financeira do sinal, contratação de seguros, ARTs/RRTs de execução, vistoria técnica inicial, Termo de Entrega de Terreno, mobilização do canteiro.
- **Entradas obrigatórias:** Contrato de obra assinado, Orçamento Executivo aprovado (Gate 15), Alvará de Obras (Prefeitura do Rio de Janeiro), autorização do condomínio.
- **Aprovação final:** Diretor de Engenharia (Claudemberg) — auditoria final do Gate 16, assinatura da Autorização de Início de Obra.

---

## 4. DOCUMENTOS INSTITUCIONAIS TRANSVERSAIS

### 4.1 Livro do Departamento de Projetos (Manual Mestre Institucional)
Documento-mãe, válido para todos os produtos da empresa (Construção do Zero, Reforma, Retrofit, Home Staging).

**Missão do Departamento de Projetos:**
- Estruturar tecnicamente todos os produtos
- Garantir padrão institucional
- Validar qualidade técnica
- Controlar risco e margem
- Liberar projetos para execução

**Estrutura padrão de funcionamento (para todos os produtos):**
1. Entrada formal do projeto
2. Registro interno
3. Fluxo estruturado por etapas
4. Entregáveis definidos
5. Gate de validação
6. Registro em planilha
7. Arquivamento final

**Matriz de Responsabilidade (RACI Global)** — válida para Construção do Zero:

| Função | Diretor | Coordenação | Arquiteto | Complementares |
|---|:---:|:---:|:---:|:---:|
| Estratégia | A | C | I | I |
| Planejamento Técnico | C | R | R | C |
| Desenvolvimento Projeto | I | C | R | R |
| Compatibilização | C | R | C | R |
| Validação Técnica | I | R | C | C |
| Liberação | A | R | C | I |

*R = Responsável · A = Autoridade final · C = Consultado · I = Informado*

**Critério de qualidade — projeto é considerado adequado quando:**
- Cumpre escopo contratado
- Está compatível tecnicamente
- Não possui interferências não resolvidas
- Está documentado corretamente
- Segue o POP da modalidade
- Possui memorial correspondente

**Reprova quando:**
- Falta de coerência técnica
- Falta de compatibilização
- Falta de clareza executiva
- Entregáveis incompletos
- Não cumprimento de POP

### 4.2 Certificação Oficial de Execução de Projetos (Programa de Arquitetos Parceiros)
Estabelece critérios para certificar arquitetos parceiros aptos a executar projetos comercializados pela Sttickler.

**Estrutura da certificação:**
1. Avaliação de Dados Profissionais (CAU, formação, experiência)
2. Avaliação de Capacidade Técnica por Tipo de Projeto
3. Avaliação de Estrutura Operacional
4. Avaliação de Governança e Controle
5. Classificação Interna por Produto e Complexidade

**Governança exigida do parceiro:**
- Seguir o POP Oficial de Execução da Sttickler
- Cumprir checklist de validação por fase
- Aceitar auditoria técnica interna
- Aceitar sistema de avaliação de performance
- Aceitar política de precificação padronizada
- Aceitar registro formal de não conformidades

### 4.3 Guia de Redação e Preenchimento do Memorial de Premissas
Orienta o orçamentista a preencher o Memorial de Premissas evitando ambiguidade (proteção jurídica da Sttickler).

**Passos do redator:**
1. Investigação logística (regulamento de obras do condomínio: horários, restrição de carga)
2. Mapeamento de projetos (esquadrias pesadas, revestimentos de grande formato)
3. Divisão de sistemas especiais (quem compra o quê: cliente vs. Sttickler — climatização, automação)
4. Revisão de exclusões (itens de custo variável/imprevisível)

**Erros fatais a evitar:**
- Usar "a combinar" (anula a função do memorial — usar "Excluído" ou "Verba Limite")
- Omitir número do laudo de sondagem
- Não fazer o cliente rubricar todas as páginas

**Padrão Sttickler para sistemas complexos (climatização, automação):** fornecer apenas infraestrutura seca (eletrodutos e caixas); qualquer serviço além disso é "Inclusão Especial".

---

## 5. GESTÃO DA SIGLA DE BAIRRO E ID DE PROJETO (já implementado no CEO)

Para referência cruzada com o código já funcional:

- Formato do ID por etapa: `{SiglaEtapa}-RJ-{SiglaBairro}-NNN-AAAA`
- Estrutura de pastas no Drive: `000_CLIENTES/{Bairro}/{Nome Cliente}/[12 pastas de etapa]`
- As 12 pastas de etapa e suas siglas já codificadas: CLI, LEV, BRI, ESP, ANT, LEG, EST/ELE/HID/AUT/INT/PAI (dentro de 007_PROJETOS_COMPLEMENTARES), COM, PE, ORC, LIB, VAL.

---

## 6. LACUNAS IDENTIFICADAS (para resolver antes de codificar Gestores/Agentes)

1. **POP – Projeto de Automação:** conteúdo completo não recuperado nesta consolidação. Buscar diretamente.
2. **POP – Projeto Executivo:** conteúdo completo não recuperado nesta consolidação. Buscar diretamente.
3. **Checklists (Entrega de Projeto, Validação do Formulário):** mencionados na estrutura de pastas do Drive, mas conteúdo não verificado nesta consolidação.
4. **Formulários (Aprovação do Cliente, Validação do Coordenador, Briefings):** confirmada a existência de ao menos um exemplo preenchido; estrutura de campos completa não mapeada.
5. **Planilhas de Controle (Externo, Interno):** existência confirmada (pasta), conteúdo não extraído.
6. **Memoriais Descritivos por Gestor** (Arquitetura, Complementares, Fechamento, Legal): apenas o de Orçamento foi confirmado com detalhe; os demais precisam de verificação.

---

*Documento gerado em 08/07/2026, a partir da base de conhecimento do Project "SISTEMA ORGANICO STTK" e do fluxograma oficial fornecido em PDF. Destinado a servir de referência para o CEO Sttickler no processo de criação e instrução dos 4 Gestores e ~15 Agentes especializados.*
