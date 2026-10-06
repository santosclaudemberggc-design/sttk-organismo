---
name: nbr6492-2021-memoriais-por-etapa-projeto
description: O que a NBR 6492:2021 exige como documentos escritos (memoriais, relatórios, planilhas) em cada etapa do projeto arquitetônico — LV, PN, EV, EP, AP, PL, PE e As Built. Distingue o que é opcional do que é obrigatório. Use sempre que Oscar/Lúcio for montar ou entregar o jogo de peças de uma etapa, solicitar aprovação de etapa ao cliente ou ao Gate, ou orientar o arquiteto parceiro externo sobre o que documentar.
version: v1.0
status: proposta
fonte_primaria_lida: "ABNT NBR 6492:2021 — Representação de projetos de arquitetura e urbanismo. D:\\008_Normas ABNT\\001_ABNT\\04_Desenho_Tecnico\\NBR 6492-2021 Representacao de Projetos de Arquitetura.pdf — páginas 1-20 lidas via pypdf em 06/10/2026 (de 40 páginas totais; págs. 21-40 não lidas — R1)."
data: 2026-10-06
validacao: "proposta — aguarda validação de Lúcio."
changelog:
  - "v1.0 (06/10/2026, Wallenberg): proposta baseada na NBR 6492:2021 lida no texto primário (págs. 1-20). Originada do sinal de Claudemberg de que o organismo carecia de formalização de como entregar Memoriais e documentações nas etapas e como estruturar aprovações."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar (Coordenador de Projeto Arquitetônico — todas as etapas LV→AP)
agentes_cross: Hely (PL-ARQ, LICIN 2.0/DULI), Baumgart e demais Complementares (PE-ARQ, coordenação de memoriais), Lelé (PE-ARQ, compatibilização)
---

# Skill: NBR 6492:2021 — Memoriais e Documentação por Etapa de Projeto

> ⚠️ RESSALVA DE FONTE. **R1 — Parcialmente lida.** Das 40 páginas da NBR 6492:2021, as páginas 1-20 foram lidas no texto primário (Seções 1-5.5, cobrindo LV-ARQ até AP-ARQ inclusive). As páginas 21-40 (Seções 5.6 a 5.8 — PL-ARQ, PE-ARQ e As Built, mais os Anexos) **não foram lidas**. O conteúdo das etapas PL, PE e As Built desta Skill vem de conhecimento técnico consolidado e de fontes secundárias confiáveis. Antes de usar em caso real com PE-ARQ ou As Built, Oscar deve verificar diretamente as seções 5.6 a 5.8 da norma.

## 1. POR QUE ESSA SKILL EXISTE

Gestores e Agentes do organismo executavam as etapas de projeto sem um mapa claro de quais documentos escritos (memoriais, relatórios, planilhas) são exigidos pela norma técnica vigente, quando são obrigatórios e quando são opcionais, e o que cada um deve conter.

A NBR 6492:2021 é a norma-mãe de representação de projetos de arquitetura e urbanismo no Brasil. Ela estrutura as **oito etapas** do projeto (LV → As Built) e define, em cada uma, quais documentos gráficos e quais **documentos escritos** o jogo de pranchas deve conter.

O principal achado: a exigência de memorial **cresce com o avanço da etapa**. No Levantamento não existe memorial. No Estudo Preliminar ele é opcional. No Anteprojeto ele é obrigatório e duplo. No Executivo ele é obrigatório e quádruplo. Quem não sabe disso entrega o jogo errado — e o cliente ou o Gate rejeita por falta de documento, não por falha técnica.

## 2. MAPA DE MEMORIAIS POR ETAPA

| Sigla | Etapa | Documentos Escritos Exigidos | Obrigatoriedade |
|-------|-------|------------------------------|-----------------|
| LV-ARQ | Levantamento | Relatórios técnicos: topografia, sondagem (se couber), vizinhança, legislação urbanística | Conforme o escopo contratado |
| PN-ARQ | Programa de Necessidades | Planilha de programa: lista de ambientes com área, quantidade e requisitos funcionais | Obrigatório (é o produto desta etapa) |
| EV-ARQ | Estudo de Viabilidade | Planilha de viabilidade: potencial construtivo, estimativa de área e custo | Obrigatório (é o produto desta etapa) |
| EP-ARQ | Estudo Preliminar | **Memorial Justificativo** | **Opcional** |
| AP-ARQ | Anteprojeto | **1. Memorial Descritivo do projeto arquitetônico** | **Obrigatório** |
| AP-ARQ | Anteprojeto | **2. Memorial Descritivo de elementos, componentes e materiais** | **Obrigatório** |
| AP-ARQ | Anteprojeto | **3. Lista de pranchas e documentos** | **Obrigatório** |
| PL-ARQ | Projeto para Licenciamento | Memorial/declarações conforme o órgão licenciador (no RJ: campos do DULI) | Conforme exigência do órgão |
| PE-ARQ | Projeto Executivo | **1. Memorial Descritivo dos elementos/componentes arquitetônicos** | **Obrigatório** |
| PE-ARQ | Projeto Executivo | **2. Memorial Descritivo de instalações prediais, componentes e materiais** | **Obrigatório** |
| PE-ARQ | Projeto Executivo | **3. Memorial quantitativo** | **Obrigatório** |
| PE-ARQ | Projeto Executivo | **4. Planilhas orçamentárias** | **Obrigatório** |
| PE-ARQ | Projeto Executivo | **5. Lista de pranchas e documentos** | **Obrigatório** |
| As Built | Documentação como construído | Registro de alterações em relação ao projeto aprovado | Conforme contrato / convenção com o cliente |

## 3. O QUE CONTER EM CADA DOCUMENTO ESCRITO

### 3.1 LV-ARQ — Relatórios Técnicos

Não há "memorial" nesta etapa. Os documentos escritos são **relatórios** que documentam os dados coletados:

- **Relatório topográfico:** resultado do levantamento planialtimétrico cadastral (ver Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj`)
- **Relatório de sondagem:** resultado do SPT, se contratado pelo cliente (ver Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio`)
- **Relatório de vizinhança:** gabaritos, recuos e características das edificações confrontantes — serve de prova do contexto urbano
- **Relatório de legislação:** parâmetros urbanísticos confirmados por Kelsen/Hely (TO, ATE, gabarito, afastamentos, zoneamento, OODC)

**Armadilha:** é comum confundir o levantamento topográfico (produto do topógrafo) com o relatório de levantamento (documento que Oscar integra ao jogo). São peças complementares.

### 3.2 PN-ARQ — Planilha de Programa de Necessidades

Lista de **ambientes**, cada um com:
- Nome do ambiente
- Quantidade de unidades iguais
- Área mínima ou área-meta (em m²)
- Requisitos funcionais e de conforto (iluminação natural, ventilação, privacidade, acesso)
- Relações de proximidade com outros ambientes

É um **documento de alinhamento com o cliente**, não um projeto. Deve ser aprovado antes do Estudo Preliminar começar.

### 3.3 EV-ARQ — Planilha de Viabilidade

- Potencial construtivo do lote (TO, CA, ATE, gabarito máx.)
- Área construída estimada por cenário (CAB e CAM quando Villaça atua)
- Estimativa de custo de obra (Mascaró/CUB)
- Estimativa de valor de revenda (Fiker/comparáveis)
- Conclusão: viável, inviável, ou viável com condicionantes

É o produto da equipe Villaça. Oscar recebe este documento como input para o Estudo Preliminar.

### 3.4 EP-ARQ — Memorial Justificativo (opcional)

Quando produzido, descreve:
- O **partido arquitetônico** adotado (a grande ideia organizadora do projeto)
- As decisões de implantação (orientação solar, ventilação, acessos, relação com o lote)
- Justificativa para escolhas de forma, volumetria e programa
- Como o projeto atende ao PN-ARQ e ao contexto do lote (LV-ARQ)

**Por que é opcional:** a NBR o exige apenas quando o cliente ou o órgão licenciador pedir. Na prática, o STTK pode usá-lo como **documento de aprovação de etapa** — apresentar ao cliente junto com os desenhos do EP para registrar o alinhamento antes de avançar para o AP.

**Uso prático no organismo:** Portinari usa o Memorial Justificativo como base para a apresentação ao cliente ao final do EP-ARQ.

### 3.5 AP-ARQ — Memorial Descritivo do Projeto Arquitetônico

Descreve o projeto como um todo, para registro técnico e comunicação:
- Descrição geral da edificação (uso, número de pavimentos, acessos, organização funcional)
- Implantação: posicionamento no lote, afastamentos, orientação
- Organização dos pavimentos: quais ambientes compõem cada nível
- Comunicação vertical: escadas, rampas, elevadores
- Estratégias de conforto térmico e iluminação natural (vinculadas às Skills de partido e proteção solar)
- Confirmação dos índices urbanísticos: TO, ATE, gabarito (confirmados por Kelsen/Hely)

**Armadilha:** não é especificação técnica de materiais (isso vai no segundo memorial). É descrição arquitetônica do partido já definido.

### 3.6 AP-ARQ — Memorial Descritivo de Elementos, Componentes e Materiais

Primeiro nível de especificação técnica:
- Sistema estrutural previsto (concreto armado, metálico, alvenaria estrutural — com referência à Skill de Baumgart)
- Vedações: tipo de alvenaria, espessuras
- Coberturas: tipo de telha, inclinação, estrutura de telhado
- Esquadrias: tipos previstos (madeira, alumínio, PVC) e vidros (vinculado à Skill de vidro)
- Revestimentos de piso e parede por ambiente (nível preliminar)
- Instalações prediais: indicação dos sistemas previstos (vinculado à Skill de Landell, Saturnino)
- Impermeabilizações previstas (vinculado à Skill de NBR 9575)

**Finalidade:** permite ao cliente e aos Complementares (Cardozo) entenderem os sistemas previstos antes de elaborarem os projetos complementares. É o documento que inicia a coordenação de projetos.

### 3.7 AP-ARQ — Lista de Pranchas e Documentos

Índice do jogo completo do AP-ARQ:
- Número e título de cada prancha
- Escala
- Revisão atual e data
- Lista dos documentos escritos incluídos

Serve como checklist de entrega ao cliente e ao Gate.

### 3.8 PL-ARQ — Memorial/Declarações para Licenciamento

No LICIN 2.0 do Rio (Decreto 55.622/2025), **não existe memorial separado**. As informações são declaradas nos campos do próprio DULI (Documento Único de Licenciamento Integrado), sob responsabilidade técnica do PRPA (Profissional Responsável pelo Projeto de Arquitetura).

O DULI é assinado digitalmente pelo arquiteto parceiro (ou por Claudemberg quando o projeto é do próprio STTK) e inclui os parâmetros do Art. 3º declarados pelo PRPA.

**Cuidado:** alguns municípios e órgãos estaduais (CBMERJ para grupamentos, INEA para APA) exigem memorial técnico separado. No LICIN 2.0 padrão para unifamiliar na Barra/Recreio, não exige.

> ⚠️ Ver Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` (checklist dos 13 parâmetros do Art. 3º) e Skill `habite-se-aceitacao-licin` (o que o DULI declara que a vistoria confere no Habite-se).

### 3.9 PE-ARQ — Memoriais do Projeto Executivo

**Memorial Descritivo dos elementos e componentes arquitetônicos:**
- Discriminação técnica de cada elemento: paredes (tipo, espessura, revestimento), pisos (tipo, acabamento, impermeabilização), forros (tipo, altura), coberturas (sistema completo: estrutura + telha + calhas + rufos)
- Esquadrias: tipo, material, espessura de vidro, ferragens
- Proteção solar: tipo e dimensões dos dispositivos

**Memorial Descritivo de instalações prediais, componentes e materiais:**
- Coordenado com Baumgart, Landell e Saturnino
- Descreve os sistemas complementares no nível de especificação do PE (não é o memorial de cada projeto complementar — é o registro integrado que Oscar organiza)

**Memorial quantitativo:**
- Quantificação de cada serviço e material por unidade (m², m, m³, un.)
- Estruturado conforme as etapas construtivas
- Usado por Lelé para o orçamento executivo

**Planilhas orçamentárias:**
- Custo estimado por item/serviço, baseado no memorial quantitativo e nos benchmarks CUB/SINAPI (Mascaró)

> ⚠️ As seções 5.7 e 5.8 da NBR 6492:2021 não foram lidas. O conteúdo acima é baseado em conhecimento técnico consolidado e pode divergir da norma em detalhes de denominação ou de exigência de subseções. Oscar deve confirmar contra a norma antes de usar em PE-ARQ real (R1).

### 3.10 As Built

- Cópia do projeto aprovado com **todas as alterações feitas na obra** marcadas (hachura ou cor diferente)
- Memorial de alterações: lista as mudanças e a justificativa de cada uma
- Assinatura do PRPA como responsável técnico pelo registro

---

## 4. COMO USAR NAS APROVAÇÕES DE ETAPA (Gate)

O **Gate do Maurício** (Artigas) aprova cada etapa antes de avançar. O jogo de documentos exigido pela NBR 6492:2021 é exatamente o que Oscar apresenta ao Gate:

| Etapa | Jogo mínimo para o Gate |
|-------|-------------------------|
| EP-ARQ | Plantas + cortes + elevações. Memorial Justificativo se pedido |
| AP-ARQ | Plantas + cortes + elevações + detalhes + **2 memoriais obrigatórios** + lista de pranchas |
| PL-ARQ | DULI completo assinado pelo PRPA |
| PE-ARQ | Jogo completo: gráficos + **5 documentos escritos** + lista de pranchas |

**Regra STTK:** Oscar nunca apresenta uma etapa ao Gate sem o jogo completo. Um jogo incompleto é apontado por Lúcio na auditoria pré-Gate, antes de chegar ao Artigas (REGRA-ARQ-01).

---

## 5. RELAÇÃO COM OUTRAS SKILLS

- `levantamento-topografico-cadastral-orientado-duli-licin-rj` — **Complementa.** Esta Skill diz "produza o relatório do levantamento"; aquela diz "o que o topógrafo deve medir para o DULI". O conteúdo do relatório LV-ARQ depende diretamente daquela Skill.
- `nbr6492-representacao-grafica` — **Diferente.** Aquela trata de como desenhar (escalas, formatos, carimbo, hachuras). Esta trata do que entregar (documentos escritos por etapa). As duas se complementam para o jogo completo.
- `habite-se-aceitacao-licin` e `levantamento-topografico-cadastral-orientado-duli-licin-rj` — **Complementa** na etapa PL-ARQ: o DULI é o memorial técnico do licenciamento no Rio.
- `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` — **Complementa.** A planilha EV-ARQ desta Skill recebe o output de Villaça (Mascaró + Fiker).
- `ia-orcamento-executivo-obra` — **Complementa.** O memorial quantitativo do PE-ARQ (seção 3.9) é a entrada do orçamento que Lelé usa.
- `compatibilizacao-projetos` — **Complementa** na etapa PE-ARQ: o memorial de instalações (seção 3.9) é coordenado com os Complementares antes da compatibilização.

---

## 6. RESSALVAS ABERTAS (dono)

- **R1 (Oscar/Lúcio):** Seções 5.6 a 5.8 da NBR 6492:2021 (PL-ARQ, PE-ARQ, As Built) **não lidas**. Confirmar antes de usar em Projeto Executivo real ou As Built. Norma disponível em `D:\008_Normas ABNT\001_ABNT\04_Desenho_Tecnico\NBR 6492-2021 Representacao de Projetos de Arquitetura.pdf`.
- **R2 (Hely/Kelsen):** A PL-ARQ no Rio (LICIN 2.0) usa o DULI, não um memorial separado. Esta Skill não detalha os campos do DULI. Ver `levantamento-topografico-cadastral-orientado-duli-licin-rj` para os 13 parâmetros que o DULI declara.

---

## FONTES

- **ABNT NBR 6492:2021** — Representação de projetos de arquitetura e urbanismo. `D:\008_Normas ABNT\001_ABNT\04_Desenho_Tecnico\NBR 6492-2021 Representacao de Projetos de Arquitetura.pdf`. Páginas 1-20 lidas via pypdf em 06/10/2026. Seções cobertas: 1 (Escopo), 2 (Referências normativas), 3 (Termos e definições), 4 (Categorias de documentos técnicos), 5.1 a 5.5 (LV-ARQ, PN-ARQ, EV-ARQ, EP-ARQ, AP-ARQ). Seções 5.6 a 5.8 e Anexos não lidas (R1).
