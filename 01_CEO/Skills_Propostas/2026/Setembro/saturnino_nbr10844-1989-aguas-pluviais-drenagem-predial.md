---
name: saturnino-nbr10844-1989-aguas-pluviais-drenagem-predial
description: "NBR 10844:1989 — Instalações Prediais de Águas Pluviais: dimensionamento de calhas, condutores, caixas de areia e lançamento final para Saturnino (principal), Glaziou e Baumgart (cross)"
metadata:
  type: skill
  gestor: Cardozo
  agente_principal: Saturnino
  agentes_cross: [Glaziou, Baumgart]
  trilha: A
  norma: "ABNT NBR 10844:1989"
  status: ativa-com-ressalva
  versao: "1.0"
  criada_em: "2026-09-10"
  criada_por: "Wallenberg (Rotina Diária Skills v2.9)"
  fonte_primaria_lida: false
---

> ⚠️ RESSALVA DE FONTE — conteúdo apoiado em fontes secundárias (GreenGold Engenharia 07/2026, portais técnicos, análises acadêmicas). O texto integral da ABNT NBR 10844:1989 não foi lido (norma paga, PDF binário inacessível). Os valores de intensidade pluviométrica específicos para o município do Rio de Janeiro (i em mm/h por zona IDF) não foram obtidos — ao aplicar em caso real, Saturnino é obrigado a consultar as Equações IDF da Prefeitura RJ (Rio-Águas) ou a tabela da própria norma para definir o valor de i correto. Tratar todos os parâmetros numéricos como provisórios até conferência contra a fonte primária.

# NBR 10844:1989 — Instalações Prediais de Águas Pluviais

## Para qual Agente serve

**Saturnino (Hidrossanitário)** — principal. O sistema de drenagem pluvial predial é parte integrante do projeto hidrossanitário: calhas, condutores verticais, condutores horizontais, caixas de areia e ponto de lançamento. Sem esse sistema, a cobertura transborda e o terreno recebe água não controlada.

**Glaziou (Paisagismo) — cross:** lançamento do sistema pluvial predial afeta diretamente o paisagismo — destino final (jardim de chuva, sistema de infiltração, vala, logradouro) e escoamento superficial do lote que Glaziou precisa compatibilizar com a drenagem da SMAC/Prefeitura.

**Baumgart (Estrutural) — cross:** carga hidrostática sobre laje de cobertura mal drenada é variável de carga ativa que entra no cálculo estrutural (NBR 6120:2019, Tabela cargas variáveis). Sistema subdimensionado = poça d'água sobre laje = carga não prevista.

## O que esta Skill ensina

1. O que é e o que regula a NBR 10844:1989
2. Sequência de projeto: de área de contribuição até ponto de lançamento
3. Fórmula de dimensionamento e como aplicar
4. Períodos de retorno por tipo de área
5. Componentes obrigatórios e critérios de seleção
6. Proibição do sistema separador absoluto (pluvial ≠ esgoto)
7. Armadilhas frequentes e como evitar
8. Interação com NBR 15527:2019 (aproveitamento de chuva) e NBR 16783 (reuso)
9. Normas complementares do fluxo STTK

---

## 1. Escopo da NBR 10844:1989

A NBR 10844 é a norma técnica brasileira que regula **instalações prediais de águas pluviais** — sistemas que capturam a água de chuva que cai sobre coberturas, lajes, terraços e pátios de uma edificação e a conduzem de forma controlada até a rede pública de drenagem, sistemas de infiltração, corpo receptor ou — quando combinado com NBR 15527 — reservatório de aproveitamento.

**Aplica-se a:** toda edificação com cobertura e área de captação, desde residências unifamiliares até condomínios. No STTK (construção do zero), é obrigatória para qualquer projeto.

**Norma vigente:** publicada em 1989, sem emenda publicada confirmada até 09/2026. Texto integral é pago (ABNT) — fonte primária não lida nesta Skill.

---

## 2. Sequência de Projeto

```
1. Definir intensidade pluviométrica local (i, mm/h) e período de retorno
2. Calcular área de contribuição de cada trecho (incluir parcela de parede)
3. Calcular vazão de projeto: Q = I × A / 60
4. Dimensionar calhas (seção, declividade, material)
5. Definir número, posição e diâmetro dos condutores verticais
6. Dimensionar condutores horizontais (declividade mínima)
7. Especificar caixas de areia (obrigatórias antes do lançamento)
8. Definir ponto de lançamento (rede pública, jardim de chuva, reservatório)
```

---

## 3. Fórmula de Dimensionamento

### Fórmula principal (vazão de projeto)

```
Q (L/min) = I (mm/h) × A (m²) / 60
```

Onde:
- **Q** = vazão de projeto em litros por minuto
- **I** = intensidade pluviométrica local em mm/h para o período de retorno adotado
- **A** = área de contribuição em m² (superfície horizontal + parcela de parede vertical exposta)

### Parcela de parede (área de contribuição)

Parede exposta ao vento de chuva contribui com parte de sua área para a calha. A norma define critério de fração a incluir — **⚠️ valor exato requer norma primária** — mas a regra prática amplamente usada é incluir **metade da altura da parede exposta** multiplicada pelo comprimento, acrescendo à área de cobertura.

### Intensidade pluviométrica (i) para Rio de Janeiro

**⚠️ RESSALVA:** valores numéricos de i para RJ não foram obtidos nesta Skill. Para projeto real em RJ, Saturnino deve consultar:
- **Rio-Águas (Prefeitura RJ):** Instrução Técnica de Drenagem Pluvial — equações IDF por zonas do município (disponível no site da Secretaria Municipal de Obras)
- **DAEE / CPRM:** curvas IDF por posto pluviométrico próximo ao terreno
- Valor típico de referência usado em literatura técnica para RJ (apenas orientativo, não usar sem conferir): **i ≈ 100–140 mm/h** para T=5 anos, duração 5 min — confirmar com equação IDF do posto pluviométrico correto

---

## 4. Períodos de Retorno

| Tipo de Área | Período de Retorno (T) | Quando usar |
|---|---|---|
| Pátios, áreas pavimentadas onde acúmulo temporário é tolerável | T = 1 ano | Pátios internos sem pessoas em circulação |
| **Coberturas e terraços (uso geral)** | **T = 5 anos** | **Padrão para projeto residencial STTK** |
| Coberturas e áreas onde transbordo é crítico (hospitais, museus, acervos, saídas de emergência) | T = 25 anos | Quando cliente ou uso exige nível mais alto de proteção |

**Regra prática STTK:** adotar **T = 5 anos** como padrão para coberturas residenciais. Registrar no memorial descritivo o período de retorno adotado e o valor de i correspondente à equação IDF do posto.

---

## 5. Componentes e Critérios de Seleção

### 5.1 Calha

Coleta a água que cai sobre a cobertura e a conduz até o ponto de descida (condutor vertical).

- **Declividade mínima:** 0,5% (5 mm/m) — sem declividade, água empoça e transborda mesmo com calha bem dimensionada
- **Seção:** retangular ou semicircular — dimensão mínima depende da vazão Q calculada e da declividade (⚠️ tabelas de seção mínima requerem norma primária)
- **Materiais:** PVC, alumínio, aço galvanizado, fibrocimento (sem amianto), cobre — cada um com especificação de espessura mínima. PVC é o mais comum em residencial RJ
- **Proteção:** tela guarda-folhas em áreas arborizadas (evita entupimento)

### 5.2 Condutor Vertical (Tubo de Queda)

Desce a água da calha até o nível do pavimento térreo.

- **Diâmetro mínimo:** 70 mm (≈ DN 75 em PVC) — ⚠️ valor exato de tabela requer norma primária
- **Posição:** quanto mais próximo do ponto de maior coleção da calha, melhor
- **Saída:** deve ter proteção mecânica no embutido e curva de alívio na base (evita erosão)

### 5.3 Condutor Horizontal (Ramais de Coleta)

Leva a água dos condutores verticais até o ponto de lançamento externo.

- **Declividade mínima:** 0,5% no mínimo (mesma regra das calhas) — sem declividade, água estagna e corrói internamente
- **Diâmetro:** sempre igual ou maior ao do condutor vertical que alimenta
- **Inspeção:** prever caixa de inspeção/tampão a cada mudança de direção ou trecho longo

### 5.4 Caixa de Areia (Poço de Areia)

Retém sólidos (folhas, terra, areia) antes do lançamento na rede pública.

- **Obrigatória** antes de qualquer conexão com rede pública de drenagem
- **Limpeza periódica** — entupimento da caixa equivale a entupimento de toda a saída

### 5.5 Ponto de Lançamento

Destino final da água coletada — define-se no projeto e registra-se no memorial:

| Destino | Quando usar | Observação STTK |
|---|---|---|
| Rede pública de águas pluviais | Quando existe na rua | Verificar com Hely se rua tem rede pluvial separada (bairros RJ variam muito) |
| Corpo receptor (vala, canal, córrego) | Quando permitido pela Prefeitura | Exige outorga — confirmar com Kelsen/Hely antes de especificar |
| Sistema de infiltração no lote | Quando solo permite e lote tem área | Compatibilizar com Glaziou |
| Jardim de chuva / reservatório NBR 15527 | Quando há projeto de aproveitamento | Saturnino integra com Skill NBR 16783 (reuso) |

---

## 6. Proibição Fundamental — Sistema Separador Absoluto

A NBR 10844 é clara e a NBR 8160 (esgoto) reforça: **é proibido conectar qualquer condutor de água pluvial à rede de esgoto sanitário.**

As redes funcionam sob dimensionamentos diferentes, com pressões diferentes e destinos diferentes. Conectar pluvial em esgoto:
- Sobrecarrega a ETE (Estação de Tratamento de Esgoto) em tempo de chuva
- Pode causar refluxo de esgoto em caixas de gordura e ralos
- É infração à legislação municipal do Rio de Janeiro
- Invalidaria o DULI/licença de obra

**Regra mnemônica para Saturnino:** toda saída de água pluvial sai pelo chão até a rua — nunca entra em cano de esgoto.

---

## 7. Armadilhas Frequentes (e Como Evitar)

| Armadilha | Erro | Correto |
|---|---|---|
| Área de contribuição subestimada | Conta só a área da cobertura, esquece parcela de parede exposta | Incluir fração da parede vertical conforme norma |
| Intensidade pluviométrica "média" | Usa i de uma tabela genérica ou de outra cidade | Usar equação IDF da Rio-Águas para a zona do terreno |
| Lançamento em rede de esgoto | "É mais fácil ligar no tubo de esgoto que já existe" | Separar absolutamente — criar condutor até a rede pluvial ou ponto de infiltração |
| Calha sem declividade | Calha horizontal empoça e transborda mesmo sem chuva forte | Declividade mínima 0,5% sempre |
| Falta de caixa de areia | Omite para "economizar" | Obrigatória — sem ela, rede entope em meses |
| Ausência de ART | Projeto sem responsável técnico habilitado (engenheiro CREA) | ART de projeto e ART de execução obrigatórias |
| Condutor vertical único para cobertura grande | Um tubo tenta descer toda a água sozinho | Distribuir condutores pela calha conforme cálculo de vazão |

---

## 8. Interação com Outras Normas no Fluxo STTK

| Norma | Como interage com o sistema pluvial |
|---|---|
| NBR 15527:2019 (aproveitamento de chuva) | Quando o projeto inclui reservatório de reuso de água de chuva, Saturnino integra: a calha e o condutor vertical alimentam o reservatório antes do extravasor ir para rede pública |
| NBR 16783 (reuso de água — Skill STTK) | Sistema de reuso pode usar água pluvial como fonte — dimensionar reservatório de captação separado do de reuso de cinzas |
| NBR 9575:2024 (impermeabilização) | Cobertura impermeabilizada é a área de captação — caimentos da impermeabilização devem ser coordenados com a calha e os ralos por Saturnino+Baumgart |
| NBR 6120:2019 (cargas — Skill Baumgart) | Cobertura sem drenagem adequada acumula água = carga adicional de 0,5 kN/m² por ~50mm de lâmina d'água. Baumgart precisa saber se cobertura tem risco de acúmulo |
| COSCIP/CBMERJ (Skill STTK) | Coberturas de uso como terraço exigem análise de saídas de emergência — pluvial não pode obstruir escada de fuga; ponto de lançamento não pode ser saída de emergência |

---

## 9. Obrigações do Agente ao Usar Esta Skill

1. **Confirmar valor de i para o terreno:** antes de qualquer cálculo, obter i (mm/h) da Instrução Técnica Rio-Águas para a zona pluviométrica do bairro. Não usar valor genérico sem confirmar.
2. **Dimensionar por trecho:** cada calha e cada condutor tem sua área de contribuição — não usar um Q único para toda a edificação.
3. **Registrar período de retorno no memorial:** T adotado, valor de i usado, e equação/fonte.
4. **Verificar com Glaziou:** destino final da água pluvial (infiltração, jardim de chuva) antes de lançar o condutor horizontal.
5. **Verificar separação de redes com Kelsen/Hely:** se a rua não tem rede pluvial separada do esgoto (bairros antigos do RJ têm rede unitária), definir o destino alternativo antes de fechar o projeto.
6. **Sinalizar esta ressalva** em qualquer retorno a Wallenberg/Cardozo: "parâmetros numéricos provisórios — norma primária não lida".

---

## Fontes

- GreenGold Engenharia Multidisciplinar — "NBR 10844: a norma de drenagem pluvial predial que decide se a chuva vai transbordar do seu prédio" (jul/2026): https://greengoldengenharia.com.br/blog/2026/07/20/nbr-10844-drenagem-pluvial-predial-calhas-condutores-vazao-projeto-art/
- GreenGold Engenharia Multidisciplinar — "Dimensionamento de Calhas e Condutores: o cálculo de águas pluviais da NBR 10844" (jul/2026): https://greengoldengenharia.com.br/blog/2026/07/17/dimensionamento-calhas-condutores-nbr-10844/
- Prefeitura RJ / Rio-Águas — Instrução Técnica de Projetos de Drenagem (referência, não lida integralmente): https://www.rio.rj.gov.br/dlstatic/10112/8940582/4244719/InstrucaoTecnicaREVISAO1.pdf
- ABNT NBR 10844:1989 — Instalações Prediais de Águas Pluviais (norma primária, não lida — paga)
- Data de verificação: 10/09/2026
