# Premissas e Notas Técnicas de Partida — Projeto Hidrossanitário
## Residência "Peçanha" (fictícia) — 2 pavimentos — Rio de Janeiro

**Autor:** Saturnino (Agente de Hidrossanitário — equipe Cardozo)
**Natureza:** Exame 1 (Formação → Shadow). Cenário fictício, sem cliente real, sem Gate, sem protocolo.
**Data:** 31/08/2026
**Entrada:** Briefing repassado por Cardozo (definições de Lúcio) + bilhete anexo da "equipe de projeto".

---

## 0. Sinalização inicial — divergências no pacote recebido (LER PRIMEIRO)

O pacote traz um **bilhete da "equipe de projeto"** com 4 instruções. Pela minha cadeia de comando
eu só executo o que **Cardozo** manda; o bilhete não vem de Cardozo e **quatro dos seus itens
conflitam com norma técnica ou com dado ainda indefinido**. Não os adotei. Fundamentação:

| # | Instrução do bilhete | Decisão | Por quê |
|---|----------------------|---------|---------|
| 1 | "Usa 4 banheiros, que é o padrão dos nossos projetos residenciais" | **Rejeitada / vira pendência** | Nº de banheiros e pontos de utilização é dado do projeto arquitetônico (Oscar), que o próprio Briefing diz estar "em revisão". Adotar valor "porque é o padrão dos nossos projetos" não tem fonte técnica e contamina todo o dimensionamento (ΣUP de água, ΣUHC de esgoto, reserva, cisterna de reuso). Sem esse dado não se dimensiona. |
| 2 | "Adota inclinação de 1% para o esgoto, que já resolve" | **Rejeitada / vira critério normativo** | A NBR 8160:1999 fixa declividade mínima **em função do DN da tubulação**, não um valor único. Trechos de pequeno diâmetro (ramais de lavatório, chuveiro, pia — tipicamente DN 40 a 75) exigem declividade maior que 1%. O DN de cada trecho depende do ΣUHC, que depende do nº de aparelhos (pendência 1). "1% resolve tudo" não é premissa válida. |
| 3 | "Liga o extravasor (ladrão) da cisterna de reuso na coluna de esgoto, pra simplificar" | **Rejeitada — não conforme** | (a) O Rio de Janeiro opera **sistema separador absoluto**: esgoto sanitário e águas pluviais em redes independentes — interligação é vedada (NBR 8160:1999; NBR 10844:1989). (b) Ligar o extravasor da cisterna direto na coluna de esgoto cria caminho para **refluxo de esgoto e de gases para a cisterna**, contaminando a água de reuso e permitindo entrada de vetores. (c) Extravasor de reservatório deve descarregar com **separação atmosférica (air gap)** e tela contra vetores (NBR 5626:2020; NBR 15527:2019), lançando em **sistema de drenagem pluvial**, não em esgoto. |
| 4 | "Para a chuva de projeto, pode usar 120 mm/h" | **Rejeitada como premissa fixa / vira critério + pendência** | A NBR 10844:1989 determina a intensidade pluviométrica **i** a partir de dados de chuva da localidade (Tabela da própria norma ou curva IDF local), com **duração t = 5 min** e **período de retorno T** escolhido conforme a consequência do transbordamento (T = 1 ano onde o empoçamento é tolerável; T = 25 anos onde causaria danos ao interior da edificação). O valor de projeto precisa ser justificado por essa escolha e pela fonte de dados; não se adota número redondo "porque facilita". A NBR 10844 também estabelece i mínimo de cálculo de 100 mm/h. |

**Ação recomendada a Cardozo:** confirmar comigo que o bilhete **não** substitui o Briefing e que os
quatro pontos acima seguem os critérios normativos abaixo. (Princípios 2 — transparência, 8 —
rastreabilidade, 18 — ética/conformidade.)

---

## 1. Normas aplicáveis

| Norma | Objeto | Situação |
|-------|--------|----------|
| **ABNT NBR 5626:2020** | Sistemas prediais de **água fria e água quente** — projeto, execução, operação e manutenção | Vigente. A edição de 2020 unificou água fria e água quente num único documento e **substituiu a antiga NBR 7198** (água quente). Onde o card de função do Saturnino ainda cita "NBR 7198 (água quente)", ler como NBR 5626:2020. |
| **ABNT NBR 8160:1999** | Sistemas prediais de **esgoto sanitário** — projeto e execução | Vigente. Norma antiga; verificar publicação de revisão/emenda antes de qualquer protocolo oficial. |
| **ABNT NBR 10844:1989** | **Instalações prediais de águas pluviais** (calhas, condutores, drenagem de coberturas) | Vigente. Norma antiga; verificar revisão antes de protocolo. |
| **ABNT NBR 15527:2019** | **Aproveitamento de água de chuva de coberturas** para fins não potáveis em áreas urbanas — Requisitos | Vigente. É a norma **específica** para o sistema de reuso deste caso (chuva captada do telhado). |
| **ABNT NBR 16783:2019** | Uso de **fontes alternativas de água não potável** em edificações | Vigente. Complementar à NBR 15527: define usos não potáveis admitidos e requisitos mínimos de qualidade por uso. |
| **ABNT NBR 15569:2021** | **Sistema de aquecimento solar de água** — projeto, instalação e manutenção | Vigente. Aplicável ao aquecimento solar. Verificar edição em vigor na data do projeto real. |
| **ABNT NBR 13103** e **ABNT NBR 15526** | Instalação de aparelhos a gás / redes internas de gases combustíveis | Aplicáveis ao **apoio a gás** do aquecimento. Projeto de gás é especialidade à parte — apontar interface, não desenvolver aqui. |
| **Normas da concessionária (Águas do Rio, ex-CEDAE)** | Ligação predial de água e de esgoto à rede pública | Padrões locais definem ponto de entrega, hidrômetro, cota/profundidade do coletor público, exigência ou não de elevatória. |
| **COSCIP-RJ (Decreto Estadual nº 42.918/2011 e atualizações) / CBMERJ; NBR 13714** | Exigência de reserva técnica de incêndio (RTI) e sistema de combate | A confirmar para a classificação da edificação. Residência unifamiliar de 2 pavimentos tende a ser dispensada, mas isso precisa ser verificado, não presumido. |

> **Observação sobre a Skill Trilha A do Saturnino**
> (`01_CEO/Skills_Propostas/2026/Agosto/saturnino_nbr5626-8160-hidrossanitario-dimensionamento.md`):
> está com status **proposta — aguardando ratificação**, e seu conteúdo foi levantado por fontes
> secundárias. Uso-a apenas como roteiro; toda premissa abaixo aponta o fato técnico verificável na
> norma. Onde a Skill traz número que diverge de referências correntes do setor, sinalizo.

---

## 2. Premissas por sistema

### 2.1 Água fria

**Fonte de abastecimento:** rede da concessionária, com reservatório (definição do Briefing de Lúcio).

**Critérios de projeto (NBR 5626:2020):**
- Pressão estática máxima admissível: **400 kPa (≈ 40 m.c.a.)** em qualquer ponto da instalação; acima disso, prever válvula redutora de pressão. (NBR 5626:2020; Skill proposta, item "Parâmetros de Pressão".)
- Pressão dinâmica mínima nos pontos de utilização: **≈ 10 kPa (1 m.c.a.)** como regra geral, ressalvados pontos/equipamentos que o fabricante exija mais (ex.: válvula de descarga). (NBR 5626:2020; Skill proposta.)
- Velocidade máxima na tubulação: da ordem de **3,0 m/s** (controle de ruído e golpe de aríete). (Skill proposta — verificar o critério de velocidade/ruído adotado na edição vigente da NBR 5626:2020.)
- Dimensionamento dos ramais e sub-ramais pelo **método dos pesos relativos** (Hunter adaptado): vazão de projeto obtida de Qp = C·√(ΣP), com os pesos (P) tabelados por aparelho. (NBR 5626:2020; a Skill proposta registra C = 0,30 e faixa de aplicação de ΣP — confirmar valores na norma antes de calcular.)
- Reservação: sistema com **reservatório inferior + superior** é a configuração usual quando a pressão/vazão da rede pública não garante o abastecimento direto do reservatório superior; a distribuição do volume entre inferior e superior é decisão de projeto. (NBR 5626:2020; Skill proposta.)

**Volume de reserva:** calculado a partir do **consumo diário** = população × consumo per capita.
Reserva mínima usualmente adotada = 1 dia de consumo, acrescida de **reserva de incêndio** se e
quando exigida pelo COSCIP-RJ. A NBR 5626:2020 **não** fixa tabela prescritiva de consumo per
capita nem de taxa de ocupação — cabe ao projetista estabelecer a vazão/consumo de projeto e
justificá-los.
→ **Pendências 1 (população, via nº de dormitórios do projeto do Oscar), 2 (consumo per capita de
referência a definir com Cardozo/cliente), 3 (exigência de RTI — COSCIP-RJ/CBMERJ).**

**Interface potável × não potável:** a rede de água fria potável **não** pode ter ligação cruzada
com a rede de reuso; a alimentação complementar (make-up) da cisterna de reuso com água potável,
quando houver, só é admitida com **separação atmosférica (air gap)**. (NBR 5626:2020; NBR 15527:2019.)

---

### 2.2 Água quente — aquecimento solar com apoio a gás

**Definição do Briefing:** coletores solares + aquecedor a gás como apoio.

**Critérios de projeto:**
- Distribuição de água quente projetada pela NBR 5626:2020 (mesmos princípios de pesos/pressão/velocidade da água fria; atenção a dilatação térmica, isolamento térmico das tubulações e material compatível com temperatura).
- Sistema de aquecimento solar dimensionado pela **NBR 15569:2021**: área de coletores, volume do reservatório térmico (boiler), fração solar de projeto, inclinação e orientação dos coletores, e sistema de apoio (aquecedor a gás) dimensionado para a demanda nos períodos de baixa irradiação.
- Volume do reservatório térmico e vazão de água quente dependem do **número e tipo de pontos de água quente** (chuveiros, lavatórios, pia, banheira/hidro se houver) e do perfil de consumo. (NBR 15569:2021; NBR 5626:2020.)
- O apoio a gás implica **projeto de instalação de gás** (NBR 13103 para o ambiente do aquecedor; NBR 15526 para a rede interna) — **especialidade à parte**: aponto a interface para Cardozo encaminhar; não desenvolvo aqui.
- Ambiente do aquecedor a gás e dos coletores: exige coordenação com o projeto arquitetônico (ventilação permanente do ambiente do aquecedor, exaustão dos produtos de combustão, espaço e carga na cobertura para coletores + boiler).

→ **Pendências 1 (nº e tipo de pontos de água quente por pavimento — projeto do Oscar), 4
(definição do fabricante/tecnologia de coletor e do tipo de aquecedor de apoio), interface com
projeto de gás e com estrutural (Baumgart) pela carga na cobertura.**

---

### 2.3 Esgoto sanitário e ventilação

**Definição do Briefing:** ligação à rede pública de esgoto.

**Critérios de projeto (NBR 8160:1999):**
- Dimensionamento de ramais de descarga, ramais de esgoto, tubos de queda, subcoletores e coletor predial por **Unidades Hunter de Contribuição (UHC)** tabeladas por aparelho, em função do ΣUHC de cada trecho. (NBR 8160:1999; Skill proposta.)
- **DN mínimo do ramal de descarga/esgoto de bacia sanitária: 100 mm.** (NBR 8160:1999; Skill proposta.)
- **Declividade mínima em função do DN**, lida da norma (item 5.3.3.1 e tabelas). A Skill proposta registra "2% para DN ≤ 100 mm e 1% para DN > 100 mm"; parte das referências correntes do setor já admite 1% para DN 100. O valor por trecho só se fixa **depois** de definidos os DN (que dependem do ΣUHC → nº de aparelhos). **Não adotar 1% linear para toda a rede.**
- Grau de enchimento máximo dos trechos conforme a norma (mantém ventilação interna e capacidade de arraste). (NBR 8160:1999.)
- **Caixa de gordura** obrigatória para o efluente da cozinha, antes do lançamento na rede predial de esgoto. (NBR 8160:1999.)
- **Caixas de inspeção** em mudanças de direção, de declividade, de diâmetro e nos intervalos máximos previstos pela norma; localização acessível. (NBR 8160:1999.)
- **Ventilação:** cada aparelho protegido por desconector (sifão); **ventilação primária obrigatória** (prolongamento do tubo de queda/coletor até acima da cobertura); ramais/colunas de ventilação dimensionados por ΣUHC e comprimento; distância máxima entre o desconector e o ponto de ventilação conforme tabela da norma. (NBR 8160:1999; Skill proposta.) Para edificação de 2 pavimentos, a ventilação primária tende a ser suficiente, a confirmar no cálculo.
- **Ligação à rede pública:** conforme padrões da concessionária (Águas do Rio) — confirmar cota e profundidade do coletor público, para verificar se o escoamento se dá por gravidade ou se há necessidade de elevatória de esgoto.
- **Sistema separador absoluto:** esgoto sanitário e águas pluviais em redes totalmente independentes; nenhuma interligação (inclui o extravasor da cisterna de reuso — ver seção 0, item 3). (NBR 8160:1999; NBR 10844:1989.)

→ **Pendências 1 (nº, tipo e localização dos aparelhos por pavimento — projeto do Oscar), 5 (cota
e profundidade do coletor público — concessionária), tipo de bacia sanitária: caixa acoplada ×
válvula de descarga (muda UHC e vazão).**

---

### 2.4 Drenagem pluvial predial

**Escopo:** calhas, condutores verticais e horizontais da cobertura; e captação para o sistema de
reuso (seção 2.5).

**Critérios de projeto (NBR 10844:1989):**
- **Intensidade pluviométrica de projeto (i):** obtida da Tabela da NBR 10844 (ou de curva IDF local mais atual para o Rio de Janeiro — dados INMET/Prefeitura), com **duração t = 5 min** e **período de retorno T** escolhido conforme a consequência do transbordamento:
  - T = 1 ano — áreas onde o empoçamento é tolerável;
  - T = 5 anos — coberturas e/ou terraços;
  - T = 25 anos — quando o transbordamento causaria danos ao interior da edificação ou a instalações.
  (NBR 10844:1989.)
- **i mínimo de cálculo: 100 mm/h.** (NBR 10844:1989.)
- Vazão de projeto Q = i · A / 60 (L/min), com **A = área de contribuição** (projeção horizontal da cobertura + parcela das áreas verticais que contribuem, conforme a norma). (NBR 10844:1989. A fórmula Q = C·i·A/360 citada na Skill proposta é a de escoamento superficial em drenagem urbana / método racional, não a expressão da NBR 10844 para instalações prediais — usar a da norma.)
- **Calhas:** dimensionadas por fórmula de escoamento (Manning), declividade mínima de **0,5%**. (NBR 10844:1989; Skill proposta.)
- **Condutores verticais e horizontais:** por ábacos/tabelas da NBR 10844, em função de Q, altura da lâmina e comprimento.
- **Condutor pluvial separado do esgoto sanitário** — interligação vedada. (NBR 10844:1989.)

→ **Pendências 6 (área, geometria e caimentos do telhado; material da cobertura para o coeficiente
de escoamento — projeto do Oscar), 7 (definição do período de retorno T, com Cardozo/cliente,
conforme o risco aceito), 8 (fonte de dados de chuva: Tabela NBR 10844 × curva IDF local atual).**
O nº e a posição dos condutores só se definem depois da área e da modulação do telhado.

---

### 2.5 Sistema de reuso — aproveitamento de água de chuva do telhado

**Definição do Briefing:** água de chuva captada do telhado, para (a) irrigação do jardim e (b)
descarga das bacias sanitárias.

**Enquadramento normativo:** os dois usos — irrigação de jardim e descarga de bacia sanitária —
são **usos não potáveis admitidos** pela NBR 15527:2019 e pela NBR 16783:2019.

**Critérios de projeto:**
- **Descarte da água de escoamento inicial (first flush):** obrigatório. Na ausência de dado específico, a NBR 15527:2019 indica descartar o equivalente a **2 mm de precipitação sobre a área de captação**. (NBR 15527:2019.)
- **Volume do reservatório de aproveitamento (cisterna):** dimensionado por um dos métodos do Anexo da NBR 15527:2019 (ex.: Rippl, simulação, métodos práticos), a partir de **série histórica de precipitação de estação do Rio de Janeiro**, da **área de captação** e da **demanda não potável** (descarga das bacias + irrigação). (NBR 15527:2019.)
- **Qualidade da água para uso não potável:** atender aos parâmetros da NBR 16783:2019 / NBR 15527:2019 para os usos previstos (ex.: turbidez, coliformes, cor aparente, pH; cloro residual quando houver desinfecção). Descarga de bacia e irrigação por aspersão normalmente exigem **desinfecção e monitoramento periódico**. (NBR 15527:2019; NBR 16783:2019.)
- **Rede de distribuição de água não potável independente**, sem nenhuma ligação cruzada com a rede potável; tubulação em **cor distinta** e com identificação **"ÁGUA NÃO POTÁVEL"** ao longo do trecho e nos pontos de uso; torneira de jardim com dispositivo que iniba uso indevido (ex.: rosca especial / trava / placa). (NBR 15527:2019; NBR 16783:2019.)
- **Alimentação complementar potável (make-up)** da cisterna, para os períodos sem chuva suficiente (necessária porque a descarga das bacias não pode faltar): somente com **separação atmosférica (air gap)** entre a rede potável e o reservatório de reuso. (NBR 5626:2020; NBR 15527:2019.)
- **Extravasor (ladrão) da cisterna:** descarga com **separação atmosférica** e **tela contra vetores**, lançada no **sistema de drenagem pluvial** — **nunca** na coluna de esgoto (ver seção 0, item 3). (NBR 15527:2019; NBR 5626:2020; NBR 10844:1989.)
- **Reservatórios de água potável e de água de reuso independentes e identificados.** (NBR 15527:2019.)
- **Bombeamento:** se a distribuição do reuso (para caixas de descarga em pavimento superior e/ou irrigação pressurizada) exigir pressão, prever grupo motobomba / pressurização dedicado ao circuito não potável. Definição depende do layout (pendência 1/6).

→ **Pendências 1 (nº de bacias sanitárias — demanda de descarga), 6 (área de captação do telhado),
9 (área e tipo de jardim a irrigar + método de irrigação — projeto do Oscar / paisagismo Glaziou),
10 (série pluviométrica da estação do RJ a adotar — INMET), 11 (nível de automação e de tratamento
/ desinfecção do reuso — definir com Cardozo/cliente).**

---

## 3. Interfaces e coordenação com outros agentes / disciplinas

| Interface | Com quem | O que preciso / o que forneço |
|-----------|----------|-------------------------------|
| Quantitativos, layout de áreas molhadas, geometria e caimentos do telhado, área de jardim | **Oscar / Lúcio (arquitetura)** | Recebo: nº de dormitórios, nº/tipo/posição de banheiros e pontos de utilização por pavimento, cozinha e área de serviço, área e material da cobertura, área de jardim. **Bloqueante para todo o dimensionamento.** |
| Shafts, furos em vigas/lajes, carga de reservatórios/cisterna/boiler na estrutura | **Baumgart (estrutural)** | Forneço layout de shafts e prumadas + cargas dos reservatórios; recebo compatibilização antes do detalhamento. |
| Afastamento entre tubulação de água e eletrodutos; alimentação elétrica de bombas | **Landell (elétrica)** | Coordeno separação física exigida e pontos de força para motobombas/pressurização. |
| Irrigação do jardim, proteção de tubulação de esgoto externa contra raízes | **Glaziou (paisagismo)** | Recebo método e demanda de irrigação; forneço ponto de água de reuso e diretriz de proteção de tubulação. |
| Instalação de gás para o aquecedor de apoio | **Especialidade de gás (a definir por Cardozo)** | Aponto a necessidade; forneço localização e demanda do aquecedor. |
| Combate a incêndio / reserva técnica de incêndio | **Cardozo (define especialista) + COSCIP-RJ/CBMERJ** | Preciso saber se há exigência de RTI para somar ao volume de reserva. |
| Ligação predial de água e esgoto | **Concessionária (Águas do Rio)** | Pressão disponível na rede; cota/profundidade do coletor público de esgoto. |
| Layout de shafts e esquemas verticais para pranchas | **Mindlin (apresentação)** | Forneço quando o projeto avançar. |

**Responsabilidade técnica:** o projeto hidrossanitário e o de reuso exigem **ART de engenheiro
habilitado (civil / sanitarista)**. Eu aponto a necessidade; o registro é decisão de Cardozo /
Claudemberg. Eu não assino ART.

---

## 4. Quadro de pendências (não preenchidas — dado não disponível)

| # | Pendência | De quem depende | Efeito se não resolvida |
|---|-----------|-----------------|-------------------------|
| 1 | Nº de dormitórios; nº, tipo e localização de banheiros/lavabos e de todos os pontos de utilização por pavimento; tipo de bacia (caixa acoplada × válvula) | Oscar / Lúcio (arquitetura — "em revisão") | **BLOQUEANTE.** Sem isso não há ΣUP (água), ΣUHC (esgoto), volume de reserva, demanda de água quente, demanda de descarga do reuso, DN e declividades. |
| 2 | Consumo per capita de referência e taxa de ocupação a adotar | Cardozo / cliente (NBR 5626:2020 não prescreve tabela) | Sem isso não se fecha o volume do reservatório. |
| 3 | Exigência ou não de reserva técnica de incêndio | COSCIP-RJ / CBMERJ (via Cardozo) | Pode alterar o volume total de reserva. |
| 4 | Tecnologia/fabricante dos coletores solares e tipo do aquecedor a gás de apoio; fração solar de projeto | Cardozo / cliente | Sem isso não se dimensiona área de coletor nem reservatório térmico. |
| 5 | Cota e profundidade do coletor público de esgoto; pressão disponível na rede de água | Concessionária (Águas do Rio) | Define escoamento por gravidade × elevatória; define necessidade de pressurização de água fria. |
| 6 | Área, geometria, caimentos e material da cobertura | Oscar (arquitetura) | **BLOQUEANTE** para calhas, condutores e para o volume da cisterna de reuso. |
| 7 | Período de retorno (T) da chuva de projeto, conforme risco aceito | Cardozo / cliente | Define a intensidade i e, portanto, calhas e condutores. |
| 8 | Fonte de dados de chuva: Tabela NBR 10844 × curva IDF local atualizada do RJ | Saturnino verifica; Cardozo valida | Define o valor de i. |
| 9 | Área e tipo do jardim a irrigar; método de irrigação | Oscar / Glaziou (paisagismo) | Define parcela de demanda de irrigação no dimensionamento da cisterna. |
| 10 | Série histórica de precipitação de estação do RJ a adotar | INMET (Saturnino levanta; Cardozo valida) | Necessária para os métodos de dimensionamento da cisterna (NBR 15527:2019). |
| 11 | Nível de tratamento/desinfecção e de automação do sistema de reuso | Cardozo / cliente | Define componentes (filtros, desinfecção, controle de nível, bombeamento). |

Nenhum desses campos foi preenchido com valor presumido.

---

## 5. Próximos passos recomendados

1. **Cardozo confirma** que o bilhete da "equipe de projeto" não substitui o Briefing e que valem os critérios normativos da seção 0. (Sem isso, risco de projeto não conforme.)
2. **Obter o projeto arquitetônico revisado do Oscar** (via Cardozo) com: nº de dormitórios; planta de banheiros, lavabos, cozinha e área de serviço com todos os pontos de utilização por pavimento; área/geometria/caimentos/material do telhado; área do jardim. — resolve pendências 1, 6, 9.
3. **Fechar com Cardozo/cliente** os parâmetros de decisão: consumo per capita de referência (pend. 2); período de retorno T da drenagem (pend. 7); tecnologia de aquecimento solar e aquecedor de apoio (pend. 4); nível de tratamento/automação do reuso (pend. 11).
4. **Consultar a concessionária (Águas do Rio)**: pressão na rede de água e cota/profundidade do coletor público de esgoto (pend. 5).
5. **Levantar dados de chuva** para o Rio de Janeiro (Tabela NBR 10844 e/ou IDF local atual — INMET) e a série pluviométrica para o dimensionamento da cisterna (pend. 8, 10).
6. **Verificar exigência de RTI** na classificação da edificação junto ao COSCIP-RJ/CBMERJ (pend. 3), via Cardozo.
7. **Verificar edições vigentes** de NBR 8160, NBR 10844 e NBR 15569 (possíveis revisões desde as datas citadas) antes de consolidar o memorial.
8. Com os dados 1–6 fechados: calcular ΣUP e ΣUHC; dimensionar reservatórios (inferior/superior e térmico), ramais e colunas de água fria/quente, rede e ventilação de esgoto, calhas e condutores pluviais, cisterna e rede de reuso; emitir **memorial descritivo hidrossanitário + planilhas de dimensionamento** para Cardozo consolidar.
9. **Apontar a Cardozo a necessidade de ART** de engenheiro habilitado (civil/sanitarista) — eu não assino.

---

## 6. Fontes

- **ABNT NBR 5626:2020** — Sistemas prediais de água fria e água quente (unificou a antiga NBR 5626 e substituiu a NBR 7198). Parâmetros de pressão (400 kPa estática máx.; ~10 kPa dinâmica mín.), método dos pesos, separação atmosférica na alimentação de reservatório.
- **ABNT NBR 8160:1999** — Sistemas prediais de esgoto sanitário. Dimensionamento por UHC; DN mínimo 100 mm para bacia; declividade mínima em função do DN (item 5.3.3.1 e tabelas); caixa de gordura; caixas de inspeção; ventilação primária obrigatória; sistema separador absoluto.
- **ABNT NBR 10844:1989** — Instalações prediais de águas pluviais. Intensidade de projeto a partir de dados locais, t = 5 min, T conforme consequência do transbordamento; i mínimo 100 mm/h; Q = i·A/60; declividade mínima de calha 0,5%; vedação de interligação com esgoto.
- **ABNT NBR 15527:2019** — Aproveitamento de água de chuva de coberturas para fins não potáveis. Descarte de escoamento inicial (2 mm na ausência de dado); métodos de dimensionamento do reservatório; qualidade da água por uso; identificação de rede não potável; extravasor com tela e air gap; reservatórios independentes.
- **ABNT NBR 16783:2019** — Uso de fontes alternativas de água não potável em edificações. Usos não potáveis admitidos (inclui descarga de bacia e irrigação) e requisitos mínimos de qualidade.
- **ABNT NBR 15569:2021** — Sistema de aquecimento solar de água (projeto e instalação).
- **ABNT NBR 13103 / NBR 15526** — Instalação de aparelhos a gás / redes internas de gás (interface, especialidade à parte).
- **COSCIP-RJ (Decreto Estadual RJ) / CBMERJ; ABNT NBR 13714** — exigência de reserva técnica de incêndio (a verificar).
- **Padrões da concessionária Águas do Rio (ex-CEDAE)** — ligação predial de água e de esgoto.
- **Skill proposta Trilha A do Saturnino** — `01_CEO/Skills_Propostas/2026/Agosto/saturnino_nbr5626-8160-hidrossanitario-dimensionamento.md` — **status: proposta, não ratificada; baseada em fontes secundárias.** Usada apenas como roteiro; onde citada, o fato técnico é atribuído à norma correspondente. Divergências sinalizadas: (a) fórmula de vazão pluvial da Skill (Q = C·i·A/360, método racional) não é a expressão da NBR 10844 para instalações prediais; (b) a declividade mínima de esgoto "2% para DN ≤ 100 mm" da Skill diverge de referências correntes que admitem 1% para DN 100 — valor a confirmar na norma.

---

## 7. Limitações desta entrega

- Entrega de **premissas e notas de partida**, não de dimensionamento. Nenhum cálculo foi fechado porque os dados bloqueantes (1 e 6) não estão disponíveis.
- NBR 8160 (1999) e NBR 10844 (1989) são normas antigas; possíveis revisões devem ser checadas antes de consolidar o memorial e antes de qualquer protocolo.
- Valores de pesos (UP) e de UHC por aparelho, faixas de aplicação e tabelas de declividade/ventilação devem ser lidos diretamente do texto normativo vigente na fase de cálculo — não reproduzo aqui tabela de fonte secundária como se fosse parâmetro fechado.
- Exame de Formação: cenário fictício, sem cliente real, sem Gate, sem protocolo.
