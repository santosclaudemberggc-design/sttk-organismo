---
name: lucio-protecao-solar-externa-dispositivos-rj
description: "Proteção Solar Externa — Brises, Cobogó e Venezianas: dispositivos físicos, diretriz por orientação de fachada e parâmetros de projeto para Rio de Janeiro (latitude ~23°S)"
metadata:
  type: inteligencia
  trilha: A
  status: ativa-com-ressalva
  gestor: Lucio
  agente_principal: Oscar (Arquitetura)
  cross_disciplina: [Tenreiro, Baumgart]
  criado_em: 17/09/2026
  criado_por: Wallenberg (Rotina Diária Skills v3.2)
  foco_geografico: Barra da Tijuca / Recreio dos Bandeirantes — Zona Oeste RJ
  versao: "1.2"
  alterado_em: 28/09/2026 (Lúcio, autorizado por Claudemberg) — ZB 4A rebaixada a indício não confirmado, alinhada à nbr15220-3-bioclimatica-rj e à NBR 15575-4
---

> ⚠️ **RESSALVAS (ativa-com-ressalva — validado por Lúcio em 17/09/2026):**
> 1. **Fontes secundárias:** parâmetros numéricos de ângulos de lâminas e profundidades de brise vieram de ProjetEEE/MME (gov.br), Correio Braziliense, Cia da Samalia, Galvisteel. Texto integral da NBR 15220 não lido (paga). Para projeto executivo, Oscar deve rodar o SOL-AR ou acionar especialista de conforto antes de fechar o desenho de brise.
> 2. **SOL-AR — ângulos alfa/beta ausentes nesta Skill:** Oscar deve consultar a Skill de 16/09 (Partido/Conforto Térmico) para entender como usar o SOL-AR — ela já tem essa explicação. As duas Skills funcionam em par.
> 3. **NBR 15575 fora do escopo:** para projetos residenciais multifamiliares, a NBR 15575 tem critérios de desempenho térmico de envoltória (fator solar, transmitância) que vão além desta Skill. Se o projeto exigir laudo de desempenho, verificar separadamente.
> 4. **Gate obrigatório:** brise externo que altere a leitura de fachada precisa passar pelo Gate de Maurício antes de ir ao cliente (impacto visual direto).

---

# Proteção Solar Externa — Brises, Cobogó e Venezianas: Dispositivos e Parâmetros de Projeto para Fachadas no RJ

**Gestor dono:** Lúcio (Arquitetura)  
**Agentes que usam:** Oscar (implantação + detalhamento), Tenreiro (conforto e iluminação natural), Baumgart (fixação/carga sobre fachada)  
**Norma de referência:** NBR 15220-3:2024 (o Rio saiu da ZB 8 na reclassificação de 8 para 12 zonas; a nova zona — ZB 4A — é **indício não confirmado em fonte primária**, ver Skill `nbr15220-3-bioclimatica-rj`; confirmar a zona e a diretriz de sombreamento antes de citá-las em projeto — esta Skill traz o HOW: qual dispositivo, por orientação, com que parâmetros)  
**Complementa:** `lucio_partido-arquitetonico-conforto-termico-passivo` (16/09/2026)

---

## 1. Princípio Fundamental — Por Que Sombrear por Fora

Dispositivo de proteção solar **externo** bloqueia a radiação antes de atingir o vidro — elimina o ganho térmico na origem. Cortina/persiana interna só dispersa a radiação já dentro do ambiente (transforma em calor difuso). Para o clima do RJ (zona bioclimática pós-2024 ainda a confirmar na fonte primária; ZB 4A é indício), a diferença de carga de resfriamento entre sombreamento externo e interno pode chegar a 60-80%.

**Regra de ouro:** sombrear por fora, nunca confiar só na cortina interna.

---

## 2. Diretriz por Orientação de Fachada (Latitude ~23°S — Barra/Recreio)

| Orientação | Comportamento Solar | Dispositivo Correto | Dispositivo Errado |
|------------|--------------------|--------------------|-------------------|
| **Norte (N)** | Sol alto (inverno: altitude solar ~44°; verão: ~90°+) — azimute estável | Brise **horizontal** (beiral, marquise, lâmina H) | Brise vertical (sol alto não desvia em azimute) |
| **Sul (S)** | Incidência direta mínima e breve no verão austral (lat. ~23°S está próxima ao Trópico — sol pode tangenciar a fachada sul no solstício de dezembro). Na prática, brise dispensável para a maioria dos casos. | Sem necessidade de brise (luz difusa na maior parte do ano) | Qualquer brise elimina desnecessariamente a iluminação natural |
| **Leste (L)** | Sol baixo manhã (~7h–10h), azimute variável; altitude cresce ao longo da manhã (~9h–11h já tem altitude suficiente) | Brise **misto (H + V combinados)**: vertical para o sol baixo inicial, horizontal para o sol que sobe depois | Só brise vertical (ineficaz para a fase de altitude média ~9h–11h) |
| **Oeste (O)** | Sol baixo tarde (~15h–18h), azimute variável | Brise **vertical** (prioridade máxima — fachada crítica no RJ) | Brise horizontal |
| **NE / NO** | Combinação de ângulos — diagonal; azimute + altitude variáveis | Brise **misto** (H + V combinados) ou cobogó | Apenas H ou apenas V |

**Fachada poente (O) é a crítica no RJ:** sol baixo à tarde com alta intensidade, dificil bloqueio por elemento horizontal. Qualquer projeto em Barra/Recreio com janela voltada para O precisa de dispositivo vertical.

---

## 3. Dispositivos — Taxonomia e Comparativo

### 3.1 Brise-Soleil (Lâminas de Proteção)

**O que é:** lâminas externas à fachada (alumínio, madeira, concreto, aço) que bloqueiam radiação direta.

**Fixo:** projetado para o ângulo solar crítico da fachada + estação. Mais barato. Risco: eficiente no pico, mas pode bloquear iluminação natural no inverno (sul no inverno recebe sol baixo N — beiral longo pode obstruir).

**Móvel (articulado):** ajusta ângulo conforme hora/estação. Custo maior, exige manutenção. Eficiência máxima.

**Materiais comuns no RJ:** alumínio anodizado ou pintura eletrostática (durabilidade costeira), madeira de lei tratada com protetor UV, concreto (brise embutido na fachada).

**Parâmetros de dimensionamento (Brise Horizontal — Fachada N):**
- Profundidade do beiral `p` recomendada: cobre ângulo solar do solstício de verão (dezembro) — ~1,0–1,5× a altura da janela `h` (referência de mercado RJ; cálculo exato via carta solar ou software)
- Inclinação 0° (horizontal) ou ligeiramente inclinado para baixo para não interferir com ventilação

**Parâmetros de dimensionamento (Brise Vertical — Fachada O/L):**
- Lâminas verticais distribuídas na largura da abertura
- Ângulo de abertura das lâminas: 45°–60° em relação ao plano da fachada para fachada poente (RJ)
- Espaçamento entre lâminas: quanto menor, maior o bloqueio mas menor a ventilação e a iluminação natural — projeto é sempre um trade-off
- Altura mínima igual à altura total da abertura

### 3.2 Cobogó

**O que é:** elemento de concreto, cerâmica ou outro material com aberturas geométricas regulares — funciona como barreira física semi-permeável (bloqueia sol direto, permite ventilação e luz difusa).

**Quando usar:**
- Fachadas L/O com necessidade de ventilação cruzada (não fecha a abertura completamente)
- Varanda / hall / corredor ventilado
- Fachada sem caixilho: cobogó define a "fachada" e elimina a necessidade de brise separado

**Limitação:** bloqueio de sol não é tão controlável quanto brise articulado — define-se pela geometria da abertura. Melhor para espaços que não exigem total escurecimento.

**Manutenção:** limpeza periódica (acúmulo de poeira/bicho); revestimento externo precisa ser resistente a UV e umidade costeira.

### 3.3 Veneziana Externa

**O que é:** veneziana montada no exterior da esquadria (não interna), com lâminas inclináveis.

**Vantagem:** bloqueio eficaz + controle fino pelo usuário. Permite ajustar para iluminação sem ganho térmico.

**Limitação:** custo maior que brise fixo, exige suporte estrutural para vento, manutenção anual (correia/mecanismo). Não recomendado em fachadas expostas a ventos fortes sem projeto de fixação específico.

**Uso em Barra/Recreio:** adequado para fachada O de dormitório (controle de privacidade + térmico), mas exige confirmar resistência ao vento (ventos de SE são fortes na Barra — vento médio ~4-6 m/s, rajadas).

---

## 4. Brecha Prática — O que Profissionais Experientes no RJ Fazem

- **Fachada poente em condomínio de luxo (Barra):** brise vertical fixo de alumínio com afastamento ≥ 30 cm da esquadria (evita ponte térmica e permite limpeza). Lâminas a 45°, inclinadas para o sul (bloqueia poente, preserva visão do mar).
- **Fachada N em casa térrea (Recreio):** beiral de 1,0–1,2 m já resolve o pico de verão sem brise adicional — mais barato e mais integrável ao partido.
- **Cobogó integrado à sacada:** combina guarda-corpo + proteção solar + elemento estético. Não exige esquadria adicional, reduz custo.
- **Veneziana externa em dormitório:** parceiros comerciais frequentes em RJ: Hunter Douglas, Graber, Toldex — todos têm linha resistente a ambientes costeiros (alumínio marinizado ou PVC).

---

## 5. Interface com Outras Disciplinas

| Ponto | Responsável |
|-------|-------------|
| Dimensionamento de brise (carta solar, ângulo, profundidade) | Oscar/parceiro ou software solar (ex.: Analysis SOL-AR/LABEE UFSC) | 
| Carga do brise sobre fachada/laje | Baumgart (verificar carga permanente adicional — NBR 6120) |
| Compatibilização com esquadria e vedação | Oscar + Saturnino (impermeabilização em brise embutido na laje ou em verga) |
| Cobogó + ventilação natural cruzada | Tenreiro (conforto e iluminação do ambiente interno) |

---

## 6. O Que Esta Skill NÃO Cobre (Lacunas Declaradas)

- Cálculo de fator solar (FS) de vidro + dispositivo: depende de especificação de vidro (não desta Skill)
- Dimensionamento preciso do ângulo de brise para lat. 23°S: usar carta solar LABEE/Analysis SOL-AR
- Resistência ao vento (cargas de vento em fachadas): NBR 6123:1988 + NBR 6120:2019 — laudo de Baumgart
- Propriedades de absorção/refletância de materiais específicos de brise: INMETRO/fabricante

---

## 7. Checklist Rápido — Antes de Oscar Fechar o Partido

- [ ] Orientação da fachada mapeada (N/S/L/O/diagonal)?
- [ ] Fachada O: brise vertical previsto?
- [ ] Fachada N: beiral ≥ 1,0 m ou brise horizontal previsto?
- [ ] Ventilação cruzada mantida com o dispositivo escolhido?
- [ ] Carga do brise checada com Baumgart?
- [ ] Carta solar rodada para confirmar profundidade do brise?
- [ ] Material do brise adequado ao ambiente costeiro (anticorrosão)?
