# POP-GESTOR-LEGAL-01 — Conferência do Gestor antes da Validação da Coordenação

**Área:** Legal (Kelsen) · **Criado em:** 20/07/2026 · **Autor:** Wallenberg (Função 5) · **Status:** aguardando ratificação na Semanal de 27/07/2026

---

## 1. O que é, e por que existe

É a **terceira aprovação** do fluxo, decidida por Claudemberg em 20/07/2026. Ela se posiciona **antes** das duas que já existiam:

```
Gestor (Kelsen, IA) confere  →  Maurício Costa valida  →  Cliente aprova  →  fluxo avança
   [este POP]                    [form Validação           [form Aprovação      [automático]
                                  da Coordenação]           do Projeto]
```

**Por que antes e não depois:** uma aprovação que só pode dizer "sim" não é aprovação, é relé. O Gestor entra aqui porque este é o único ponto do fluxo em que a checagem dele ainda **evita** trabalho — barrar material incompleto antes de consumir o tempo do Maurício e antes de mostrar peça furada ao cliente. Depois do aceite do cliente não há o que aprovar: o avanço de etapa é consequência, não decisão.

**O que esta conferência é:** verificação de **completude e conformidade mecânica**. Falta peça? Número bate com número? Parâmetro tem fonte?

**O que ela não é:** julgamento de mérito de projeto. Partido arquitetônico, solução, gosto e adequação ao briefing são do Maurício e do cliente. Kelsen não opina sobre isso e não barra por isso.

## 2. Quem executa

**Kelsen confere; Hely levanta a evidência.** Kelsen não abre arquivo atrás de peça faltante — ele determina a conferência, Hely executa e devolve o resultado item a item, e Kelsen julga o conjunto e decide liberar ou barrar. Regra geral do organismo: Gestor não executa (13/07/2026).

## 3. Checagem A — está no modelo e tem os entregáveis estipulados

Esta é **a razão de ser da conferência**, conforme Claudemberg definiu em 20/07/2026: o Gestor aprova **como a etapa foi entregue** — se está no modelo Sttickler e traz o que a Sttickler estipulou. Não é sobre formulário; é sobre a entrega.

### Fontes que definem o padrão — leia, não recite

Duas fontes oficiais no Drive, e **elas divergem entre si** (ver 3.3):

- `POP – PROJETO LEGAL (ARQUITETURA)`, código POP-ARQ-PL-01, seção 7.1 — Drive, `001_MATERIAL DE CONTROLE INTERNO`
- **Planilha de Controle de Enviáveis Externos** — a lista contratada com o arquiteto parceiro

Vale também o `MEMORIAL DESCRITIVO - Projeto Legal` como modelo do texto do memorial.

### 3.1 Entregáveis segundo o POP-ARQ-PL-01 (seção 7.1)

- [ ] Plantas legais de todos os pavimentos
- [ ] Planta de implantação conforme legislação
- [ ] Planta de situação do lote
- [ ] Quadro de áreas legal
- [ ] Indicação de parâmetros urbanísticos
- [ ] ART/RRT emitida quando aplicável (seção 7.3)
- [ ] Documentação exigida pelo órgão licenciador, organizada (seção 7.3)

### 3.2 Entregáveis adicionais segundo a Planilha de Enviáveis

- [ ] Cortes legais exigidos pela prefeitura (cotados)
- [ ] Fachadas legais
- [ ] Memorial descritivo para protocolo

### 3.3 Divergência conhecida entre as duas fontes — não resolva sozinho

A Planilha de Enviáveis exige **cortes legais, fachadas legais e memorial descritivo**; a seção 7.1 do POP-ARQ-PL-01 **não os lista**. As duas são documentos oficiais da casa.

**Regra até que Claudemberg unifique:** conferir contra a **união das duas listas** — é a leitura conservadora, e faltar peça que o parceiro contratou entregar é problema real. **Sinalize a divergência a Wallenberg** em toda conferência onde ela pesar; não escolha uma fonte e descarte a outra em silêncio.

### 3.4 Está no modelo?

- [ ] Prancha no formato exigido para protocolo (hoje, **A1**)
- [ ] Plantas, cortes e implantação **cotadas**, conforme a Planilha de Enviáveis
- [ ] Memorial segue o `MEMORIAL DESCRITIVO - Projeto Legal`, não texto livre
- [ ] Nomenclatura e organização de arquivo conforme o padrão da pasta do cliente

**Peça ausente ou fora do modelo barra a etapa.** Não existe "segue e resolve depois" — o que sai daqui incompleto volta incompleto, ou pior, chega ao cliente.

## 4. Checagem B — conformidade e coerência

- [ ] **Zoneamento confirmado por fonte oficial** para o lote real, sob o `POP-LEGAL-RIU-01`, com a trava GeoPAL. Premissa de zona não confirmada invalida todo o resto.
- [ ] **Cada parâmetro usado tem fonte registrada** no arquivo do caso — coordenada literal, parâmetros da requisição, lei e artigo (Princípio 8).
- [ ] **Passou pelas armadilhas** da Skill `legal-base-legislativa-bairro`: cabeçalho da Área de Planejamento conferido; afastamento lateral verificado nos quatro artigos, não em um; preexistente vs. obra nova separados; vigência das normas checada.
- [ ] **Recuos, gabarito e coeficientes** conferidos contra os parâmetros confirmados (Seção 7.2 do POP-ARQ-PL-01).
- [ ] **Coerência entre plantas e quadro de áreas** — os números fecham entre si.
- [ ] **Solução do Anteprojeto preservada integralmente** — a adequação ao padrão legal não alterou o partido arquitetônico.
- [ ] **PRPA identificado** (não decidido por Kelsen nem por Hely — apenas conferido se está definido; se não estiver, é pendência a sinalizar, ver seção 6).

## 5. Resultado — três saídas, não duas

| Resultado | Quando | O que Kelsen faz |
|---|---|---|
| **Libera** | Tudo de A e B atendido | Segue para o formulário de Validação da Coordenação (Maurício). Registra a liberação. |
| **Barra** | Falta entregável, ou há não conformidade objetiva | Devolve ao Hely com a lista exata do que falta. Não sobe. |
| **Libera com ressalva** | Está completo e conforme, mas há risco relevante fora da alçada de Kelsen | Sobe **acompanhado da ressalva por escrito** — nunca em silêncio. Ver seção 6. |

A terceira saída existe porque risco real raramente é binário. Um projeto pode estar 100% conforme e ainda expor o cliente — exemplo confirmado em 20/07/2026: janela a menos de 1,50 m da divisa é conforme para a SMDU e vulnerável pelo Código Civil art. 1.301.

## 6. O que sobe sempre, mesmo liberando

Kelsen sinaliza a Wallenberg, que leva a Claudemberg:

- **Confirmação de PRPA** — nunca decidida pelo Legal (regra de Claudemberg).
- **Risco civil ou de responsabilidade técnica** que o Alvará não cobre, sobretudo quando o PRPA for Claudemberg (COES Art. 39 §1º; Princípio 18).
- **Lacuna de conhecimento** encontrada durante a conferência — vira proposta de Skill via Wallenberg, nunca conhecimento oficial por decisão de Kelsen.
- **Divergência entre fonte oficial e material recebido** do arquiteto parceiro.

## 7. Paradas obrigatórias — a autonomia não passa daqui

Este POP automatiza a conferência, **não** as decisões de Claudemberg. Continuam exigindo ele **antes**, sem exceção:

- **Gate 13** (Compatibilização) e **Gate 16** (Liberação de Obra) — dupla aprovação presencial.
- **Qualquer documento que chegue ao cliente ou à prefeitura** — DULI, Anexos, memorial, prancha.
- **Protocolo ou petição em prefeitura** — ato externo e irreversível.

Fluxo que avança sozinho por cima de um destes pontos é falha grave, não eficiência.

## 8. Registro

Toda conferência entra no **Registro Diário** do dia (`03_REGISTROS_DIARIOS/{Ano}/{Mês}/{data}.md`), com: etapa, resultado (liberou / barrou / liberou com ressalva), o que foi checado, e o que subiu como sinalização. Conferência que não aparece no Registro Diário não aconteceu (Princípio 8).

## 9. Pendências conhecidas deste POP

**9.1 — O avanço automático de etapa não faz parte deste POP.** Claudemberg definiu em 20/07/2026 que os formulários **não** serão vinculados a planilha de respostas por ora, e que a função do Gestor **não é enxergar formulário** — é aprovar como a etapa foi entregue. Este POP roda por acionamento, e isso é o desenho, não uma limitação a contornar. O gatilho automático fica para quando o Sistema de Gestão de Projetos existir (Função 8, fora do MVP).

**9.2 — Não confunda a ordem escrita nos POPs com a ordem real** *(esclarecido por Claudemberg, 20/07/2026)*. Todo POP da casa lista "Apresentação ao Cliente" antes de "Validação da Coordenação" — no `POP-ARQ-PL-01`, seções 7.4 e 7.5. **Isso é convenção de redação, padronizada em todos os POPs, e não descreve a sequência real.** A ordem real é a que consta na seção 1 deste documento: Gestor confere → Maurício valida → cliente aprova. Não trate a numeração do POP como fluxo.

**9.3 — Divergência de entregáveis** entre POP-ARQ-PL-01 seção 7.1 e a Planilha de Enviáveis (ver 3.3). **Confirmada por Claudemberg como incongruência real** — atualização feita num documento e não propagada aos outros. Ele vai ajustar os materiais. Até lá, vale a união das duas listas.

**9.4 — Responsável pelo Projeto Legal segundo o POP:** "Arquiteto contratado para Legalização (Terceirizado)". Se e quando o Hely passar a produzir de fato, o POP oficial precisa ser atualizado — hoje ele não prevê execução interna.
