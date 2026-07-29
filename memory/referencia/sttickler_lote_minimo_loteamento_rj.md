---
name: sttickler_lote_minimo_loteamento_rj
description: Lote abaixo do mínimo em loteamento fechado NÃO aumenta CAB/CAM — como funciona de verdade (RJ)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 24d9ef72-4792-4c6f-9897-f58654189f89
---

Responde a dúvida real do Claudemberg (16/07/2026), levantada pelo caso Vasconcelos TESTE: loteamento fechado de alto padrão que vende lotes de 180 m² onde o lote mínimo da zona é 360 m² — o CAB/CAM são ajustados/aumentados pra dar área construída maior? Pesquisado por Wallenberg contra o Dicionário de Termos oficial da LC 270/2024. Reforça o item "loteamento fechado" da pauta de 20/07 e o limite da TRAVA A em [[sttickler_riu_api_oficial]]. Ver também [[sttickler_outorga_onerosa_rj]].

**Resposta curta: NÃO há ajuste automático de CAB/CAM porque o lote é menor que o mínimo.** O coeficiente não é função do tamanho do lote.

**Por quê (definições oficiais LC 270/2024):**
- **CA = número × área do terreno = m² construíveis (a ATE).** É proporção sobre a área REAL do lote. Lote menor → área construível absoluta menor, mesmo coeficiente.
- **CAB:** regra geral **1,0 para toda a Cidade, sem contrapartida** — MAS "salvo exceções previstas em lei complementar". Na prática o RIU devolve CAB 0,8 em várias subzonas (ex.: ZRM3), ou seja, as exceções por zona existem e são as do Anexo XXI. CAB NÃO sobe por lote pequeno.
- **CAM:** limite máximo por zona/subzona (Anexo XXI), atingido pagando Outorga Onerosa. Também definido por zona, não por tamanho de lote.
- **Lote mínimo** (360 no caso) é regra de **parcelamento** (Anexo XXI/XXIV), não de construção. Diz se você PODE subdividir até aquele tamanho — não mexe no coeficiente de quem constrói.
- Num lote de 180 m² em subzona CAM 1,2: ~180 m² de graça (CAB 1,0) → até 216 m² pagando outorga sobre o excedente. Esse é o teto, e encolher o lote não muda isso.

**Então como um loteamento fechado vende lotes de 180 numa zona de mínimo 360?** Pela aprovação do próprio loteamento — o **PAL (Projeto Aprovado de Loteamento)**, "onde são identificados os lotes, suas dimensões e os logradouros". Dois caminhos:
1. **Direito adquirido do loteamento:** PAL aprovado sob legislação anterior (mínimo menor na época). Legaliza o **parcelamento** (os lotes de 180 são válidos) — mas NÃO sobe o coeficiente de construção.
2. **Parâmetros urbanísticos específicos** no decreto/PAL daquele loteamento: aí os índices podem diferir do genérico da zona — mas é fato que está NO decreto do loteamento, tem que ler caso a caso (GeoPAL + decreto). Não presumir.

**Como se consegue área construída maior num lote pequeno (caminhos reais, nenhum automático):** (a) **remembramento** — juntar dois lotes de 180 → 360 e construir sobre 360; (b) confirmar se o loteamento tem parâmetros específicos que já elevam o índice; (c) instrumento excepcional (AEI, operação urbana). Acima do CAM não há outorga.

**CONDOMÍNIO vs LOTEAMENTO — a distinção que decide o caso Orla Bothânica (real, Daniel-OB, analisado 16/07/2026):**
- **Loteamento:** cria lotes autônomos, matrícula própria cada um; o lote mínimo (360) incide lote a lote e o CA é medido por lote.
- **Condomínio (ex.: Orla Bothânica / "Bothânica Park"):** a gleba continua matrícula única; as unidades são **"áreas privativas" / frações ideais**, NÃO lotes. Logo o lote mínimo de 360 NÃO incide sobre as frações de 180-290, e o **CA é medido sobre a gleba inteira**, com a área construível distribuída entre as unidades. É isso que permite unidade com área construída maior do que a fração dela sozinha comportaria. **Indício prático de condomínio:** o GeoPAL devolve a fração SEM lote cadastral autônomo (CLNP vazio). **Prova definitiva só na matrícula/RGI + ato de aprovação do condomínio** — sem esses documentos, condomínio×loteamento fica tecnicamente em aberto (Kelsen/Hely + Maurício).

**Terreno (gleba) em mais de uma zona — LC 274/2024, Art. 3º (confirmado por lei):** §2º os índices construtivos são calculados por área de cada zona e, **somados, aplicados livremente a todo o terreno**; §3º excedente paga contrapartida (outorga); §4º acréscimo limitado ao **zoneamento mais permissivo** incidente; §5º não vale pra ZCA-1. Para aplicar, precisa da poligonal por zona dentro da gleba. No Orla Bothânica a gleba cruza ZRM1 B (CAB 1,0/CAM 1,2), ZRM2 G (CAB 0,6/CAM 1,0) e ZRM3 D — ZRM1 B é a mais permissiva. **Gleba medida no RIU oficial = 176.447,70 m²** (confirmado por Claudemberg no mapa, 16/07). Escala ilustrativa: só o CAB da gleba (0,6 a 1,0) já dá ~106.000 a 176.000 m² construíveis sem contrapartida — espaço pra centenas de unidades de ~267 m² antes de tocar no CAM/outorga; por isso uma unidade de 267 m² sobre fração de 180 não "estoura" nada SE o CA for medido sobre a gleba (condomínio). O zoneamento da unidade específica do Daniel ficou NÃO confirmado (Claudemberg: a classificação ZRM1 B não tinha fonte) — precisa da implantação georreferenciada.

**Confiança:** alta no conceito (fonte oficial). **Limite:** se ESTE loteamento concreto tem direito adquirido ou parâmetros específicos é leitura do PAL/decreto dele — julgamento do Kelsen/Hely + questão forte pro Maurício, ANTES de qualquer decisão de compra. Wallenberg não dá conselho de investimento; explica o mecanismo.
