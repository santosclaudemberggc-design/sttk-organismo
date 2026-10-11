# Pré-Estudo de Viabilidade — Ensaio Sombra 003, Etapa 02 — Lote 17, Qd C, Reserva das Garças

**Gestor:** Villaça (Viabilidade). **Execução:** Mascaró (custo de obra) e Fiker (valor de revenda).
**Para revisão de:** Wallenberg. Estou no nível Assisted, então nada daqui vai ao cliente sem a revisão dele.
**Data de referência:** 02/10/2026.
**Peças integradas, ambas na mesma pasta:**
- `custo_obra_mascaro_003.md` (Mascaró)
- `revenda_fiker_003.md` (Fiker)

**Rótulos de confiança usados em todos os números:**
- **[FP] fonte primária:** documento oficial ou documento do Dossiê, que dentro do ensaio vale como real.
- **[ECF] estimativa com fonte:** conta sobre fonte citada, com a fragilidade declarada.
- **[NC] não calculável:** a seção diz o que faltaria para calcular.

> ENSAIO, 100% FICTÍCIO. Nada sai desta pasta. Ninguém foi contatado.

---

## 0. Resumo em uma página

1. **Não existe cenário CAM neste lote.** Para a subzona, o RIU dá CAB = CAM = 1,0. Onde o CAB é igual ao CAM, não há outorga onerosa (LC 270 Art. 345 §3º; Etapa 01). Por isso a **OODC é R$ 0, porque não se aplica**, e a diferença "CAM − CAB" é **zero**: não há área nem custo a mais. O número que de fato muda o resultado é a **área**, e ela depende de duas coisas: a divisa com o Lote 16 e o lago.
2. Comparei os três cenários de área que o Legal entregou:
   - **S1:** 457,44 m², o adotado;
   - **S2:** 480 m², só se a divisa for regularizada;
   - **S3:** 297,28 m², se a APP for confirmada.
3. **Custo de obra no S1:**
   - **R$ 2,12 a 2,26 milhões** pela via do CUB, somando CUB R-1 Alto, BDI, INCC-M até maio/2027 e a demolição da casa [ECF];
   - **cerca de R$ 3,0 milhões** pela via do preço da construtora 5.12, aplicado à área legal [ECF];
   - nas duas vias, **sem** fundação profunda, piscina, paisagismo, AC, automação, projetos, ligações e sondagem [NC].
   - **Não dá para afirmar que o S1 cabe no teto de R$ 4,2 milhões, nem que não cabe.**
4. **Valor de revenda no S1:**
   - **R$ 5,95 a 6,86 milhões**, a partir de 2 vendas no próprio condomínio, com confiança média-baixa [ECF];
   - o controle de mercado (6 anúncios no Recreio) dá **R$ 3,77 a 4,93 milhões**.
   - A distância de pelo menos 20% entre as duas fontes **não está resolvida**. Não escolho um ponto dentro da faixa.
5. **Recomendação, condicionada ao que ainda está aberto:**
   - projetar sobre o S1 e estudar a variante H1 (lago);
   - **não fechar** com a construtora agora;
   - **não contar** com R$ 5 milhões do banco;
   - tratar a regularização da divisa como uma decisão que vale algo entre R$ 0,19 e 0,24 milhão em revenda líquida [ECF, confiança média-baixa], descontado o custo da regularização, que é [NC].

---

## 1. Premissas recebidas do Legal e como as usei

Fonte: `parecer_legal_base_003.md` (Hely), seção 5.1, e `auditoria_kelsen_003.md`, que libera com ressalva. Aprovadas por Claudemberg em 01/10/2026. **Não reabro nenhuma.**

| Premissa | Valor | Como usei |
|---|---|---|
| CAB / CAM | 1,0 / 1,0 | Não há cenário CAM nem OODC. A coluna "CAM" da matriz aparece só para mostrar que é zero (pedido da enunciado e da Helena). |
| Área de cálculo | 571,80 m² medidos (600 m² na escritura e na matrícula, como hipótese condicionada) | S1 sobre 571,80 m². S2 sobre 600 m², só como hipótese. |
| Limite real | TO de 40% do condomínio x 2 pavimentos: **457,44 m²** computáveis (S1) e 480 m² (S2) | É a área base de custo e de revenda. A ATE de 571,80 m² **não** é atingível. |
| Lago (H1, APP de 30 m) | Envelope de 148,64 m², teto computável de **297,28 m²** (S3) | Cenário de risco, não de projeto. |
| Vedados | subsolo, rooftop, escavação acima de 1,20 m (piscina até 1,60 m), Mais-Valerá/LC 281 para área, edícula mantida | Nenhum valor de revenda ou de custo foi atribuído a esses itens. |
| Edícula e casa | premissa de demolição | Entram no custo como demolição. |

**Risco residual que registro (não reabro):** a auditoria de Kelsen manteve "no grau declarado pelo Hely, sem releitura" o LC 270 Arts. 345 a 354, e é dali que sai o CAB = CAM. A Skill `legal-oodc-mais-valera-mais-valia` v1.1 também diz: "leitura do Hely, não conferida por Kelsen". Se essa leitura mudar, a seção 2 muda inteira. A pergunta fica para Kelsen, via Wallenberg (seção 5).

---

## 2. Matriz CAB x CAM e cenários de área

### 2.1 CAB x CAM, como o enunciado pede

| Item | Cenário CAB | Cenário CAM | Diferença CAM − CAB | Rótulo |
|---|---|---|---|---|
| Coeficiente | 1,0 | 1,0 | 0 | [FP] RIU 5.3; LC 270 Art. 345 §§3º e 5º |
| Área computável (S1) | 457,44 m² | 457,44 m² (não há área a comprar) | 0 m² | [FP] Etapa 01 |
| Custo da OODC | não se aplica | **R$ 0, porque não existe outorga onerosa** | R$ 0 | [FP] LC 270 Art. 345 §3º; Skill OODC v1.1, "Brecha válida" item 1 |
| Custo de obra | ver 2.2 | igual ao CAB | 0 | — |
| Revenda | ver 2.2 | igual ao CAB | 0 | — |

**A "outorga de R$ 380 mil" da planilha do corretor (5.13)** foi simulada em outro lote, de outro condomínio, com CAM de 1,5. Ela não se aplica ao Lote 17 e não entra em nenhuma conta.

### 2.2 Matriz real: cenários de área (contas abertas)

Fontes das contas:
- custo: Mascaró, seções 3 e 6;
- revenda: Fiker, seção 4;
- valores em reais correntes; o INCC-M foi aplicado até maio/2027 só onde a linha indica.

| Linha | S1 (457,44 m², adotado) | S2 (480 m², depende da divisa) | S3 (297,28 m², APP confirmada) | Rótulo |
|---|---|---|---|---|
| a. Área computável | 457,44 | 480,00 | 297,28 | [FP] Etapa 01 |
| b. CUB R-1 Alto Set/2026 (R$ 3.691,68/m²) x área | R$ 1.688.722 | R$ 1.772.006 | R$ 1.097.463 | [FP] Sinduscon-Rio Set/2026 + conta |
| c. b + BDI (20,34% a 25,00%, TCU) | R$ 2.032.208 a 2.110.903 | R$ 2.132.432 a 2.215.008 | R$ 1.320.687 a 1.371.829 | [ECF] TCU 2013, obra pública, só ordem de grandeza |
| d. c x INCC-M até mai/2027 (+3,9% a +4,4%) | R$ 2.111.464 a 2.202.938 | R$ 2.215.597 a 2.311.582 | R$ 1.372.194 a 1.431.641 | [ECF] FGV 6,61% em 12 meses, extrapolado |
| e. + demolição da casa (R$ 5.400 a 54.000) | **R$ 2.116.864 a 2.256.938** | R$ 2.220.997 a 2.365.582 | R$ 1.377.594 a 1.485.641 | [ECF] fonte fraca (Cronoshare); edícula, piscina e entulho [NC] |
| f. Via do preço de construtora: R$ 6.300/m² x área x INCC | R$ 2.994.265 a 3.007.522 | R$ 3.141.936 a 3.155.846 | R$ 1.945.889 a 1.954.508 | [ECF] n = 1 proposta, inclui radier provavelmente inválido |
| g. Fora das linhas e e f | fundação profunda, rebaixamento, piscina, paisagismo, AC, automação, projetos e aprovações, ligações, sondagem, impostos e taxas, acabamento acima do CUB, efeito de 2 pavimentos | idem | idem | **[NC]** (Mascaró 4.2) |
| h. Custo da OODC | R$ 0 | R$ 0 | R$ 0 | [FP] |
| i. Terreno (preço pago, 5.11) | R$ 3.300.000 | R$ 3.300.000 | R$ 3.300.000 | [FP] Dossiê 5.11; custo afundado, mostrado só para ler j e k |
| j. Revenda, faixa principal (vendas C1 e C4 no condomínio, R$ 13.000 a 15.000/m²) | **R$ 5.946.720 a 6.861.600** | R$ 6.240.000 a 7.200.000 | **[NC]** sem comparável real (a conta ilustrativa de R$ 3,86 a 4,46 mi não é adotada; o risco é para baixo) | [ECF] confiança média-baixa (S1 e S2) |
| j'. Revenda, controle web (6 anúncios no Recreio, R$ 8.245 a 10.778/m²) | R$ 3.771.593 a 4.930.288 | R$ 3.957.600 a 5.173.440 | 2 anúncios com dispersão de 2 vezes [NC] | [ECF] só anúncios; quase todos triplex em lote menor |
| k. j − i − e ("folga antes dos itens [NC]") | +R$ 389.782 a +R$ 1.444.736 | +R$ 574.418 a +R$ 1.679.003 | [NC] | [ECF]. **Não é margem.** Os itens da linha g ainda saem daqui |
| k'. j' − i − e (controle web) | −R$ 1.785.345 a −R$ 486.576 | −R$ 1.707.982 a −R$ 347.557 | [NC] | [ECF] |

Conferências que fiz nesta auditoria:
- 457,44 x 3.691,68 = 1.688.722,10;
- 1.688.722 x 1,2034 = 2.032.208;
- 2.110.903 x 1,0436 = 2.202.938;
- 457,44 x 13.000 = 5.946.720;
- 457,44 x 8.245 = 3.771.593.

As linhas de S2 e S3 nas linhas c, d, e e f são contas minhas sobre os mesmos fatores de Mascaró.

### 2.3 Diferenças entre os cenários

| Comparação | Revenda | Custo de obra (CUB + BDI) | Líquido | Rótulo |
|---|---|---|---|---|
| **CAM − CAB** | 0 | 0 (OODC = R$ 0) | **0** | [FP] |
| **S2 − S1** (regularizar a divisa) | +22,56 m² x R$ 13.000 a 15.000 = +R$ 293.280 a 338.400 | +R$ 83.284 x 1,2034 a 1,25 = +R$ 100.224 a 104.105 | **+R$ 189.175 a 238.176**, menos o custo da regularização da divisa [NC] | [ECF] média-baixa |
| **S3 − S1** (APP confirmada) | [NC]; risco para baixo (perda de área, restrição visível na diligência de comprador e de banco) | −R$ 591.259 (CUB) a cerca de −R$ 739 mil (com BDI) | [NC] | custo [ECF], revenda [NC] |

**Leitura:**
- O lago é, de longe, o maior fator de variação do caso: tira cerca de 35% da área.
- A divisa vale algo entre R$ 0,19 e 0,24 milhão líquidos, com confiança média-baixa.
- A outorga vale zero.

### 2.4 O ponto não resolvido da revenda

As 2 vendas do Dossiê (C1 e C4) ficam pelo menos 21% acima do anúncio web mais caro da mesma faixa de metragem. Há duas hipóteses, que nem Fiker nem eu conseguimos separar com o que temos:
- (a) o condomínio tem um prêmio real (lote de 600 m², lago);
- (b) as escrituras C1 e C4 precisam ser conferidas (área total ou computável; preço).

**Por isso a linha k não é margem nem promessa.** A pergunta que resolve isso está na seção 5.

### 2.5 Custo de tempo (da família, fora do teto de obra)

- Aluguel de R$ 18.000 por mês (Dossiê, seção 2).
- Obra de maio/2027 a dezembro/2028 = 20 meses x R$ 18.000 = **R$ 360.000** [FP + conta].
- **Cada mês de atraso custa R$ 18.000.** Isso pesa a favor de não perder a janela da licença de 30/06/2027.

---

## 3. Triagem dos documentos 5.11 a 5.14

| Doc | Aceito | Devolvo / não uso | Por quê |
|---|---|---|---|
| **5.11 Escritura** (R$ 3,3 mi, "600 m² e benfeitorias") | O preço pago, como custo do terreno (linha i) | Os 600 m² como área de cálculo. Os R$ 5.500/m² como "valor de mercado do terreno" | A área medida é 571,80 m² (Etapa 01). O preço inclui casa, edícula e piscina que serão demolidas e é uma transação só. Fiker achou um anúncio de lote a R$ 3.371/m², mas 1 dado não permite dizer que houve sobrepreço. |
| **5.12 Proposta Alicerce Prime** | R$ 6.300/m² como **um ponto** de preço de construtora (data-base 29/09/2026). A lista de não inclusos como checklist. A cláusula de INCC-M | A área de 590 m² (inviável pela lei). O total de R$ 3.717.000. "Chave na mão" como "tudo incluso". O radier como premissa. A validade de 30 dias como prazo de decisão | São 8 itens excluídos por escrito. A sondagem 5.7 mostra NA a 0,90 m e argila mole de 2,5 a 9 m, e a Skill de fundações v1.3 diz que o radier "é inviável na maioria dos casos": risco de aditivo [NC]. A proposta vence por volta de 29/10/2026, antes de existir projeto. Não declara BDI. Mascaró, seção 7. |
| **5.13 Planilha do corretor** | **C1** (venda 03/2026). **C4** (venda 06/2026, com ressalva sobre APP e pavimentos). **C2** só como teto (é anúncio) | **C3**: os 1.200 m² são terreno de 2 lotes. **C5**: subsolo e rooftop vedados aqui, outro condomínio, 680 m², anúncio. **C6**: de 2021, área ambígua, sem índice para atualizar. A média de R$ 12.833. O R$ 7,67 mi (sobre 590 m²). O R$ 8,8 mi (rooftop vedado). A "outorga de R$ 380 mil" (outro lote, CAM 1,5) | A média mistura venda com anúncio, terreno com área construída, atributos vedados e dado velho. Fiker, seção 1. |
| **5.14 Carta do banco** | Teto de crédito de **R$ 3,0 mi**. Liberação por medição. Limite de **60% de (terreno + obra executada), pelo laudo do próprio banco**. Condição: licença até 30/06/2027 | Qualquer leitura de que os 60% ampliam o crédito, ou de que incidem sobre o valor futuro da casa pronta | O valor do laudo do banco é [NC]. Fiker alerta que o laudo usa comparáveis próprios e pode ficar mais perto da faixa web (j'). A ressalva R3 de Kelsen continua: a licença do LICIN Art. 4º §2º vale 3 meses, e é preciso confirmar se ela atende à condição do banco. |

---

## 4. Respostas às mensagens 5.15 (texto para revisão de Wallenberg; não é enviado)

### Rodrigo: "A construtora fecha em R$ 6.300 o m², tudo incluso. 520 m² dá R$ 3,28 milhões, sobra quase R$ 1 milhão do teto. Já dá pra fechar com eles?"

**Resposta:** Rodrigo, ainda não dá para fechar. A conta está certa como multiplicação, mas parte de três premissas que não se confirmam.
- **Área:** a regra do condomínio permite cerca de 457 m² de área "contável". Os 520 m² só existem se uns 63 m² vierem de varandas e vagas, e isso o arquiteto ainda vai ver.
- **"Tudo incluso":** a própria proposta deixa de fora demolição, piscina, paisagismo, ar-condicionado, automação, projetos e aprovações, ligações e sondagem. O R$ 1 milhão que "sobra" tem de pagar tudo isso.
- **Fundação:** a proposta prevê uma fundação simples (radier). A sondagem mostra água a 90 cm e argila mole até 9 m. Se o engenheiro de estrutura pedir estacas, o que é provável, vem um custo extra que hoje ninguém consegue calcular.

Além disso, o preço sobe com o índice da construção até a obra começar (algo como 4% até maio/2027), e a proposta vence no fim de outubro, antes de existir projeto. O caminho é pedir de novo o preço quando houver anteprojeto e projeto de fundação, e comparar com pelo menos mais uma construtora.

**Fundamento:**
- Mascaró, seções 7 e 7.1: 520 x 6.300 = R$ 3.276.000; com INCC, R$ 3,40 a 3,42 mi [ECF]. A proposta lista 8 itens não inclusos [FP 5.12].
- Teto computável: 457,44 m² (Etapa 01).
- Solo: Dossiê 5.7; Skill fundações v1.3, §3.1.
- INCC-M: FGV, Set/2026, 6,61% em 12 meses (conferido por mim no portal da FGV em 02/10/2026).

### Rodrigo: "A casa pronta vale R$ 7,7 milhões, e com o rooftop R$ 8,8. O banco libera 60% do valor do imóvel, então dá pra pedir uns R$ 5 milhões em vez de 3. Pode usar esse número?"

**Resposta:** Não, Rodrigo. Esse número não existe, por três razões.
- **O crédito aprovado é de até R$ 3 milhões.** Os 60% não aumentam esse teto. Eles limitam cada liberação.
- **Os 60% incidem sobre o terreno mais a parte da obra já executada**, e não sobre o valor da casa pronta. E quem avalia é o banco, com laudo próprio, e não o corretor.
- **Os R$ 7,7 e 8,8 milhões não se sustentam.** O primeiro usa 590 m², que não cabem no lote. O segundo põe preço num rooftop que o condomínio proíbe. Pelas vendas que houve no próprio condomínio, uma casa com a área possível ficaria entre R$ 5,9 e 6,9 milhões. Mesmo esse número depende de conferir as escrituras: os anúncios do resto do Recreio apontam valores bem menores.

Para planejar, o número é o que já temos: R$ 4,2 milhões (R$ 3 milhões do banco e R$ 1,2 milhão de recursos próprios).

**Fundamento:**
- Carta do banco, 5.14 [FP]. 60% x 8,8 mi = R$ 5,28 mi, que é a conta implícita no pedido do Rodrigo.
- Só como ilustração, **não como valor**: se o laudo do banco desse ao terreno o preço pago (R$ 3,3 mi), o limite antes de qualquer obra executada seria 60% x 3,3 mi = R$ 1,98 mi. O valor real do laudo é [NC].
- Revenda: seção 2.2, linhas j e j'; Fiker, seções 1 e 4.

### Helena: "Pagamos R$ 3,3 milhões num terreno que a escritura diz ter 600 m² e que, pelo que entendi, mede menos. Quero saber quanto isso pesa em dinheiro. E queremos o comparativo CAB x CAM com o valor da outorga."

**Resposta:** Helena, são duas medidas, e nenhuma delas é "o prejuízo".
- **Rateio pelo preço pago:** faltam 28,20 m² dos 600 m². Pelo preço que vocês pagaram, isso equivale a cerca de **R$ 155 mil**. É uma conta de proporção. Terreno não vale proporcionalmente à área, então ela não mede perda de valor.
- **Efeito no que dá para construir e vender:** com 571,80 m², a casa pode ter cerca de 457 m² "contáveis"; com 600 m², 480 m². Pelas vendas no condomínio, essa diferença vale entre **R$ 190 e 240 mil líquidos** em valor de revenda, já descontado o custo de construir os 22,56 m² a mais. É uma estimativa com amostra pequena.
- **Pela medição, a diferença parece ser o muro do vizinho (Lote 16) avançando sobre o lote de vocês, e não um erro da venda.** Isso muda contra quem e como se reclama. Esse ponto é jurídico, e já pedi a análise ao nosso Legal. Há um prazo legal que pode estar correndo desde o registro da compra (julho/2026), então vale tratar disso logo, com advogado.
- **Comparativo CAB x CAM:** no lote de vocês, os dois coeficientes são iguais (1,0). Não existe outorga para comprar, e **o valor da outorga é zero**. A simulação de R$ 380 mil que o corretor mandou foi feita em outro condomínio, com outra regra, e não vale aqui. O comparativo que de fato importa para vocês é outro: lote com ou sem a faixa de proteção do lago. Se a faixa for confirmada, a área cai de cerca de 457 m² para cerca de 297 m².

**Fundamento:**
- 3.300.000 x 28,20 / 600 = R$ 155.100 [ECF] (Fiker, seção 7).
- S2 − S1 líquido: seção 2.3 [ECF, média-baixa].
- Causa provável (muro do Lote 16): parecer da Etapa 01, seção 2.1.
- Código Civil, Art. 500 §1º: "Presume-se que a referência às dimensões foi simplesmente enunciativa, quando a diferença encontrada não exceder de 1/20 (um vigésimo) da área total enunciada, ressalvado ao comprador o direito de provar que, em tais circunstâncias, não teria realizado o negócio." Texto lido em fonte secundária (jus.com.br, artigo 21633, acesso em 02/10/2026); o Planalto não abriu (ECONNRESET). Aqui, 28,20 / 600 = **4,70%**, abaixo de 1/20 (5%).
- Art. 501 (prazo decadencial de 1 ano a partir do registro do título): visto só em resumo de busca, **não lido no texto**.
- **Não concluo nada jurídico.** Pergunta para Kelsen (seção 5).
- CAB = CAM: LC 270 Art. 345 §3º (Etapa 01).

---

## 5. Recomendação e encaminhamentos

### Recomendação (condicional ao que está aberto)

1. **Não há decisão CAB x CAM a tomar.** A base de projeto é o **S1 (457,44 m² computáveis)**, com uma variante H1 (297,28 m²) até SPU, INEA e SMAC responderem.
2. **O lago é a incerteza que mais vale.** Ele mexe em cerca de 35% da área, no custo e na revenda (S3 sem comparável). As consultas do Legal (Etapa 01, seção 4.2) continuam sendo o caminho crítico também da viabilidade.
3. **A divisa:** regularizar vale cerca de R$ 0,19 a 0,24 mi líquidos em revenda [ECF, média-baixa], menos o custo e o tempo da regularização [NC]. A decisão é da família, com advogado. Do lado financeiro, recomendo **não** apostar o projeto na regularização.
4. **Construtora:** não fechar agora. Recotar com anteprojeto e projeto de fundação, com pelo menos duas propostas e com BDI aberto.
5. **Teto:** planejar com R$ 4,2 mi. A parcela calculável do S1 ocupa:
   - de 50% a 54% do teto pela via do CUB;
   - de 71% a 72% pela via da proposta.

   O resto paga itens ainda sem número, e o maior deles é a fundação em solo mole. **Não afirmo que cabe.**
6. **Revenda:** não usar nenhum número de revenda com a família como valor esperado antes de conferir C1 e C4. Para o banco, considerar que o laudo pode cair perto da faixa web.

### Para Lúcio (Arquitetura), via Wallenberg

- Projetar sobre o S1. A variante H1 fica sem promessa de H0.
- **Cada m² a mais custa cerca de R$ 3.692 só de CUB, mais BDI.** A área não computável (varandas, vagas) aumenta o custo, mas **não** aumenta a revenda pelo mesmo R$/m² (Fiker, seção 4). Os 520 m² do programa dependem de cerca de 63 m² não computáveis: avaliar se valem o custo.
- Definir a dimensão da piscina nova (item [NC] do custo).
- Informar a área total e a área computável em separado, para recalcular custo e revenda **sobre a mesma base dos comparáveis**.

### Para Kelsen (Legal), via Wallenberg

1. **CC Arts. 500 e 501:** a diferença é de 4,70%, abaixo de 1/20, e o registro é de 07/2026. Há direito contra o vendedor, ou o caminho é contra o vizinho do Lote 16 (o muro)? O prazo de 1 ano do Art. 501 está correndo? Li o §1º só em fonte secundária, e o Art. 501 nem isso: precisa ler no primário.
2. **Regramento Art. 8º (escavação até 1,20 m)** x blocos de coroamento, baldrames e estacas: a vedação alcança a fundação? Isso decide a viabilidade da fundação. Pergunta levantada por Mascaró, seção 7(c).
3. **CAB = CAM (LC 270 Art. 345 §§3º e 5º):** a auditoria ficou "no grau declarado pelo Hely". Se mudar, este Pré-Estudo muda inteiro. Peço só a confirmação, sem reabrir.

### Para Wallenberg

1. **Cardozo/Baumgart (entre Gestores, decide Wallenberg):** o radier da proposta x o perfil SPT 5.7. O quantitativo preliminar de fundação é o que destrava o maior [NC] do custo. A sondagem de 2024 chegou à ponta da estaca? E o aterro até a soleira +3,20 m (atrito negativo, Skill M4)?
2. **Banco:** a licença do Art. 4º §2º, com validade de 3 meses, atende à condição (R3 de Kelsen)? Que comparáveis o laudo do banco usa?
3. **Num caso real, eu perguntaria (não feito; é ensaio):**
   - ao corretor: as escrituras de C1 e C4, se a área é total ou computável, e o padrão dessas casas;
   - à construtora: a composição do preço e o BDI;
   - à Comissão de Obras: o valor da taxa.

   As listas completas estão em Mascaró, seção 9, e Fiker, seção 6.
4. **Nada vai ao cliente sem a sua revisão.** As respostas da seção 4 são rascunho.

---

## 6. Auditoria de Villaça sobre Mascaró e Fiker, item por item

**Método:** li os dois artefatos inteiros. Refiz as contas. Conferi duas fontes primárias de Mascaró por conta própria, em 02/10/2026:
- portal da FGV: INCC-M de setembro em +0,25%, agosto em +0,85%, **6,61% em 12 meses**, divulgado em 25/09/2026. **Confere.**
- página de índice do CUB no Sinduscon-Rio: setembro/2026 é o mês mais recente, os três PDFs citados por Mascaró existem, e o R8-N de R$ 2.476,31 bate com o que ele relata.

Os valores de R-1 Alto e R-1 Normal estão dentro do PDF binário, que não reli. Ficam no grau declarado por Mascaró (primário lido por ele com Read).

### 6.1 Mascaró (`custo_obra_mascaro_003.md`)

| Item | Decisão | O que mudou |
|---|---|---|
| CUB Set/2026 (R-1 Alto R$ 3.691,68; Normal R$ 2.990,86) e a ressalva "R-1 é térrea" | **Integrado** | Nada. A ressalva entra na linha g. |
| Contas da seção 3 (por cenário) | **Integrado**, contas refeitas e conferidas | Estendi os fatores de BDI, INCC e demolição a S2 e S3 (linhas c a f). |
| Lista do que o CUB não cobre (texto do PDF) e os itens [NC] | **Integrado** | Nada. |
| BDI do TCU (20,34% a 25%) | **Integrado como [ECF], só ordem de grandeza** | Mantive a ressalva de que é obra pública de 2013 e que o CUB já contém administração. |
| Demolição R$ 5.400 a 54.000 | **Integrado com ressalva** | Anoto que o mínimo usa demolição manual, que é improvável numa casa de 180 m². O piso real tende a ser o da faixa mecanizada (R$ 25.200). Não recalculei a faixa, porque a fonte é a mesma e é fraca. |
| Fundação [NC] e descarte de ORSE e SINAPI | **Integrado**. Achei correta a recusa de usar preço unitário sem quantitativo | Nada. |
| INCC-M e projeção de +3,9% a +4,4% | **Integrado** (dado conferido na FGV) | Nada. |
| Proposta 5.12, itens (a) a (f), e a conta do Rodrigo | **Integrado** | Usei na seção 3 e na resposta ao Rodrigo. |
| Pergunta "blocos x escavação de 1,20 m" | **Redirecionada** | É leitura do Regramento: vai para Kelsen (seção 5), não fica com Cardozo. |
| **Devolvido a Mascaró** (registro; não espero o retorno) | (1) Obter a composição SINAPI de hélice contínua com preço do RJ (caderno técnico já localizado). (2) Ler a Tabela de Honorários do CAU/BR no documento oficial. (3) Rever o piso da demolição pela faixa mecanizada e incluir a destinação de entulho. | — |

### 6.2 Fiker (`revenda_fiker_003.md`)

**Arquivo completo, não truncado:** tem as seções 0 a 8 e a declaração de ensaio. Os 13 comparáveis web têm imóvel, área, preço, data, situação, link e data de acesso; W6 e W7 estão sem data de publicação, o que o próprio Fiker sinaliza. A 5.13 está tratada linha por linha (C1 a C6), mais a média e o rodapé.

| Item | Decisão | O que mudou |
|---|---|---|
| 5.13 linha por linha (C1 aceita; C4 com ressalva; C2 só teto; C3, C5 e C6 rejeitadas) e a crítica da média e do rodapé | **Integrado inteiro** | Nada. Concordo com cada linha. |
| Contas (S1 R$ 5.946.720 a 6.861.600; S2; web; mediana R$ 8.928) | **Conferidas, fecham** | — |
| Faixa principal de S1 e S2 | **Integrada com mudança de apresentação** | A faixa web (j') aparece **sempre ao lado** da faixa do condomínio, inclusive na resposta ao Rodrigo. Não deixo a faixa do condomínio aparecer sozinha enquanto a distância de 20% estiver aberta. |
| S3 | **Integrado como [NC]** | Não uso a conta ilustrativa de R$ 3,86 a 4,46 mi nem como estimativa. O próprio Fiker diz que ela não se sustenta. |
| Desconto anúncio x venda (não aplicado) | **Integrado** | Divergência menor: ele usou o Raio-X FipeZAP do 2º trimestre de 2026 (Portas, 18/08/2026: 9% em todas, 14% com desconto); eu achei o do 1º trimestre (Portas, 19/05/2026: 9% e 13%, 67% das transações). Os dois são consistentes. Nenhum foi lido no PDF primário. |
| Efeito lago / APP sobre C4 | **Integrado** | Usei na recomendação: a APP pode tirar a âncora do topo da faixa até no S1. |
| Terreno (R$ 5.500 a 5.771/m²) e Helena (R$ 155.100) | **Integrado** | Acrescentei o efeito no potencial (S2 − S1 líquido) e a pergunta jurídica sobre os Arts. 500 e 501 para Kelsen. |
| **Devolvido a Fiker** (registro; não espero o retorno) | (1) Ler o PDF primário do Raio-X FipeZAP. (2) Buscar comparáveis web de 2 pavimentos em lote de cerca de 600 m² (hoje só W3 se parece no lote, e é triplex). (3) Quando Lúcio definir área total e computável, recalcular sobre a mesma base dos comparáveis. | — |

### 6.3 Processo (falha minha, registrada)

Deleguei os dois em segundo plano. O harness exigiu meu retorno antes de eles devolverem, e entreguei um relatório parcial a Wallenberg. Corrigido nesta rodada: coletei, auditei e integrei. Lição no meu `_estado`: quando a integração depende do retorno, a delegação é bloqueante.

---

## 7. Fontes e Skills usadas

| Fonte | Data-base | Acesso | Uso |
|---|---|---|---|
| Sinduscon-Rio, CUB/m² Set/2026 (NBR 12.721), emitido em 29/09/2026 | set/2026 | 02/10/2026 (Mascaró, PDF; Villaça, página de índice) | linha b |
| Sinduscon-Rio, Relatório 14 (R8-N) e Relatório 1 (preços medianos), Set/2026 | set/2026 | 02/10/2026 | tendência; descarte do ORSE |
| FGV IBRE, INCC-M Set/2026, divulgado em 25/09/2026 | set/2026 | 02/10/2026 (Mascaró e Villaça) | linha d |
| TCU, Acórdão 2622/2013-Plenário (BDI) | 2013 | 02/10/2026 | linha c [ECF] |
| Cronoshare, custo de demolição | 02/01/2026 | 02/10/2026 | linha e, fonte fraca |
| Dossiê 5.1 a 5.15 (fictício, vale no ensaio) | — | — | áreas, preços, comparáveis C1 a C6 |
| Attria e Consultoria VM, anúncios W1 a W13 (links em Fiker, seção 2) | 05 a 09/2026 | 02/10/2026 | linha j' |
| Raio-X FipeZAP 1T e 2T 2026, via Portas (secundária) | 1T e 2T/2026 | 02/10/2026 | só para dizer que anúncio é teto |
| Código Civil, Art. 500 §1º, via jus.com.br (secundária; o Planalto deu ECONNRESET) | — | 02/10/2026 | pergunta a Kelsen |
| Etapa 01: parecer de Hely e auditoria de Kelsen | 01/10/2026 | — | premissas (seção 1) |

**Skills:**
- `legal-oodc-mais-valera-mais-valia` v1.1: se CAB = CAM, a OODC não existe. Não diverge do primário que a Etapa 01 leu. A ressalva "leitura do Hely não conferida por Kelsen" está registrada na seção 1.
- `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3: risco do radier. A Skill é secundária por natureza (R1 da própria Skill). Não há fonte primária minha contra ela.

**Divergências:**
- Skill x fonte primária: **nenhuma encontrada** nesta etapa.
- Divergência menor entre fontes secundárias (FipeZAP 1T x 2T): seção 6.2.

**Bloqueios de ferramenta:**
- Planalto (ECONNRESET);
- Sinduscon `/cub` (erro do WordPress), contornado pela página de índice;
- PDFs binários sem extração pelo WebFetch, lidos por Mascaró com Read;
- Loft (410), ImóvelWeb e CasaMineira (403), Folha Vitória (403).

Nenhum número veio dessas páginas bloqueadas.

---

## 8. Declaração de ensaio

Este Pré-Estudo foi produzido no **Ensaio Sombra 003, Etapa 02**. Cliente, lote, condomínio, documentos e números do Dossiê são **100% fictícios**. Índices, normas e dados de mercado da web são reais, com fonte e data de acesso.

- Nada foi enviado a cliente, corretor, construtora, banco, condomínio, cartório ou órgão, e ninguém foi contatado.
- Não abri, listei nem citei nada em `_gabaritos_LACRADO/` nem qualquer `parecer_bardi.md`.
- Nenhum número aqui é valor de venda prometido nem custo fechado.
- As respostas ao cliente são rascunho para revisão de Wallenberg.

— Villaça, Gestor Viabilidade, 02/10/2026
