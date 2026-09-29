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
  versao: "1.3"
  alterado_em: 29/09/2026 (Rotina Macetes v1.0, validado por Lúcio) — nova seção 8 "Macetes de quem faz" (4 macetes aprovados); nota na 3.1 remetendo ao método da mancha de temperatura
  changelog:
    - "1.3 (29/09/2026): seção 8 Macetes de quem faz (M1 a M4); regra de bolso da 3.1 mantida, com remissão ao método rigoroso. Rotina Macetes v1.0, validado por Lúcio."
    - "1.2 (28/09/2026): ZB 4A rebaixada a indício não confirmado, alinhada à nbr15220-3-bioclimatica-rj e à NBR 15575-4 (Lúcio, autorizado por Claudemberg)."
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
  - *Nota 1.3:* essa regra de bolso serve para a primeira conversa de partido. O método rigoroso não parte de uma data fixa: define o período a sombrear pela mancha de temperatura e ajusta α, β e γ na carta. Ver seção 8, macetes M1 e M3.
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

- Cálculo de fator solar (FS) de vidro + dispositivo: depende de especificação de vidro (não desta Skill) — **ver `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj` (29/09/2026, complementa)**
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

---

## 8. Macetes de quem faz

> Validados por Lúcio em 29/09/2026 (Rotina Macetes v1.0). Complementam as seções 2 e 3; não substituem nenhuma regra delas. Tipo A = método de fonte técnica/acadêmica; tipo B = prática de mercado/produto.

### M1. Defina o período a sombrear pela mancha de temperatura, não por uma data fixa (tipo A)
- **O que fazer:** sobreponha à carta solar os horários em que a temperatura do ar passa de 20 °C (mancha de sombreamento). Faça duas cartas, uma para 21/dez a 21/jun e outra para 21/jun a 21/dez, porque as necessidades mudam muito entre os semestres. Com carga térmica interna alta (home office, cozinha gourmet integrada), a sombra passa a ser necessária abaixo de 20 °C (Tabela 4-4: carga nenhuma, sombra acima de 20 °C; carga existente, abaixo de 20 °C; carga muita, muito abaixo). Depois desenhe α, β e γ para bloquear toda a mancha indesejável e o mínimo possível do resto.
- **Por que funciona:** brise dimensionado para uma única data ou sombreia pouco ou rouba o sol de inverno. A regra de bolso da seção 3.1 ("cobre o solstício de verão") continua valendo para a primeira conversa; este é o método para fechar o desenho.
- **Quem disse:** Roberto Lamberts (Prof. Titular UFSC, supervisor do LabEEE), Luciano Dutra e Fernando O. R. Pereira.
- **Onde:** *Eficiência Energética na Arquitetura*, 3ª ed., Eletrobras/Procel, 2014, Cap. 4, §4.10, pp. 135-136. https://labeee.ufsc.br/sites/default/files/apostilas/eficiencia_energetica_na_arquitetura.pdf (páginas arquivadas em `01_CEO/Skills_Propostas/_macetes_fontes/2026-09-29/`).
- **Limite:** o limiar de 20 °C é o critério do Analysis-BIO; o SOL-AR mostra faixas de temperatura e traz a mancha pronta só para 14 cidades (p. 135). Não está confirmado se o Rio é uma delas; se não for, a mancha sai do arquivo climático do Rio. É estudo de partido e não substitui a verificação de desempenho da NBR 15575.

### M2. Brise com parte fixa e parte móvel (tipo A)
- **O que fazer:** a parte fixa sombreia o sol indesejável comum aos dois semestres. A parte móvel sombreia só o do período mais quente e deixa a abóbada celeste livre no período frio.
- **Por que funciona:** o fixo resolve o que nunca muda sem depender do usuário; o móvel devolve o sol e a luz do inverno.
- **Quem disse / onde:** Lamberts, Dutra e Pereira, mesma obra, p. 136.
- **Limite:** a parte móvel custa mais e exige manutenção; na orla da Barra e do Recreio precisa de material marinizado (ver 3.1 e 3.3). Se o cliente não quer manutenção, fique só no fixo, dimensionado pelo M1.

### M3. Ajuste ângulo a ângulo na carta, não "brise maior" (tipo A)
- **O que fazer:** para estender a sombra até um horário mais tardio (ex.: 16h no verão), alongue o brise horizontal lateralmente além da janela (γ menor). Para cobrir o sol de inverno, aprofunde o brise (α menor). Quando o sol cai fora de α ou γ, a sombra é só parcial.
- **Por que funciona:** cada ângulo controla uma parte da mancha; aumentar tudo por igual encarece e escurece sem necessidade.
- **Quem disse:** Marcelo Nudel, arquiteto, sócio-diretor da Ca2 Consultores Ambientais Associados, ex-consultor de sustentabilidade da Arup (Sydney, Madri, São Paulo), professor de pós-graduação no Mackenzie (perfil: https://www.aecweb.com.br/revista/artigos/articulista/marcelo-nudel/180/1).
- **Onde:** vídeo "Carta Solar p/ Brises – A explicação definitiva", https://www.youtube.com/watch?v=Rb5tB_Wiphs, trecho 29:43 a 30:11. No mesmo vídeo, 09:45 a 10:28: "bate sol na fachada sul no verão", o que reforça a ressalva da seção 2 sobre a fachada Sul.
- **Limite:** exige carta solar e transferidor de ângulos da latitude certa (~23°S).

### M4. Lâmina microperfurada quando a vista importa (tipo B)
- **O que fazer:** em fachada com vista (mar ou lagoa na Barra), especifique lâmina de brise microperfurada, com furos de 2,5 a 3 mm e 16 a 20% de abertura. Mesmo fechada, ela deixa ver para fora e passa luz difusa.
- **Por que funciona:** resolve o conflito entre fechar o brise contra o sol e perder a vista, que é o que o cliente de orla mais valoriza.
- **Quem disse / onde:** Hunter Douglas, fichas técnicas dos Brises Aeroscreen Plano (furo 3 mm com 20% de abertura; 2,5 mm com 16%), https://www.aecweb.com.br/produto/brises-aeroscreen-plano/20485, e SL4/SL0/SL5/H2 (microperfurado, furo de 2 mm a cada 5 mm), https://www.aecweb.com.br/produto/brises-sl4-sl0-sl5-e-h2/20480. A técnica vale para qualquer lâmina perfurada equivalente; não é indicação de marca.
- **Limite:** a perfuração deixa passar parte da radiação direta, então sombreia menos que a lâmina cega. Confirme o fator de sombra com o fabricante e com a Skill `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj`.
