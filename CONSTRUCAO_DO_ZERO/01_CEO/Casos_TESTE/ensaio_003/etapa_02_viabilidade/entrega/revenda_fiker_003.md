# Ensaio 003, Etapa 02: Valor de revenda (Fiker)

**Para:** Villaça (Gestor de Viabilidade). Integração e auditoria são dele.
**De:** Fiker (Agente de Valor de Mercado / Comparáveis)
**Data de referência:** 02/10/2026. Pesquisa web e acessos feitos em 02/10/2026.
**Imóvel:** Lote 17, Quadra C, Condomínio Reserva das Garças (fictício), Recreio dos Bandeirantes. Casa unifamiliar de alto padrão, 2 pavimentos, 4 suítes, piscina, fundos para a faixa verde e o lago.
**Premissas do Legal (não reabertas):** CAB = CAM = 1,0, então não existe cenário com outorga. Rooftop e subsolo são vedados (Regramento, Art. 7 e Art. 8). Cenários de área computável: S1 = 457,44 m², S2 = 480,00 m², S3 = 297,28 m².

**Rótulos usados em cada número:**
- **[FP] fonte primária:** documento do dossiê ou anúncio aberto individualmente.
- **[EF] estimativa com fonte:** conta minha feita sobre números [FP].
- **[NC] não calculável:** não há base para o número.

---

## 0. Resumo para Villaça

| Cenário | Área computável | Faixa principal: vendas no próprio condomínio (C1, C4) | Valor de revenda (faixa principal) | Controle: anúncios web de outros condomínios | Amostra | Confiança |
|---|---|---|---|---|---|---|
| S1 | 457,44 m² | R$ 13.000 a 15.000/m² [FP] | **R$ 5,95 mi a R$ 6,86 mi** [EF] | R$ 8.245 a 10.778/m² → R$ 3,77 mi a R$ 4,93 mi [EF] | dossiê: 2 vendas + 1 anúncio; web: 6 anúncios | **Média-baixa** |
| S2 | 480,00 m² | R$ 13.000 a 15.000/m² [FP] | **R$ 6,24 mi a R$ 7,20 mi** [EF] | R$ 8.245 a 10.778/m² → R$ 3,96 mi a R$ 5,17 mi [EF] | igual ao S1 | **Média-baixa** (e depende da regularização da divisa) |
| S3 | 297,28 m² | nenhum comparável do condomínio nessa metragem | **[NC] com comparável real.** Interpolação declarada, com ressalva forte: R$ 3,86 mi a R$ 4,46 mi | 2 anúncios na faixa, de R$ 6.774 a 13.492/m² (dispersão de 2 vezes, inútil como faixa) | 0 vendas; 2 anúncios | **Baixa / não confiável** |

**Os três achados que mais pesam:**
1. **A média do corretor (R$ 12.833/m², arredondada para R$ 13.000) não vale como método.** Ela mistura venda com anúncio, área de terreno com área construída, outro condomínio com atributos vedados aqui, e um dado de 2021. Dos 6 comparáveis, sobram 2 vendas válidas (C1, C4) e 1 anúncio aproveitável como teto (C2). O R$ 7,67 mi do rodapé ainda multiplica por 590 m², área que o Legal já mostrou ser inviável. O R$ 8,8 mi "com rooftop" atribui valor a algo vedado.
2. **As vendas do condomínio no dossiê estão pelo menos 20% acima de qualquer anúncio web que abri no Recreio.** A maior venda-base, C1 a R$ 13.000/m², fica cerca de 21% acima do maior anúncio web da faixa de 430 a 520 m² (R$ 10.778/m²). Como o anúncio costuma ficar acima do preço fechado, a distância entre fechamentos deve ser maior ainda. Ou o Reserva das Garças tem um prêmio real (lote de 600 m², lago), ou as escrituras C1 e C4 precisam ser conferidas. Não consigo separar as duas hipóteses. Isso pesa para o banco (5.14): o laudo dele usa comparáveis próprios e pode cair mais perto da faixa web.
3. **S3 não tem comparável real.** Além disso, o risco de APP elimina o argumento "fundos para o lago" que sustenta o topo da faixa (C4). O risco de S3 é para baixo.

---

## 1. Tratamento da planilha do corretor (5.13), linha por linha

| Ref | Decisão | Por quê |
|---|---|---|
| **C1**: Lote 04 Qd A, 2 pav., frente para rua interna, **escritura 03/2026**, 450 m² construídos, R$ 5.850.000 | **ACEITA** (a mais forte da amostra) | É venda fechada, recente, no mesmo condomínio, com tipo e gabarito iguais (casa de 2 pavimentos) e metragem dentro da faixa de S1/S2. Conferi a conta: 5.850.000 / 450 = R$ 13.000/m² [FP]. Não tem o efeito do lago (frente para rua interna), então serve como piso da faixa. Ressalvas: não sei se os "450 m² construídos" são área total ou computável, nem se estão averbados; padrão e idade da casa não foram informados. |
| **C2**: Lote 11 Qd B, 2 pav., **anúncio 09/2026**, 480 m² construídos, R$ 7.200.000 | **ACEITA COM AJUSTE**: só como teto, fora do cálculo da faixa | Mesmo condomínio, mesmo tipo e metragem praticamente igual à de S2. Mas é preço pedido, não preço fechado. Conferi: 7.200.000 / 480 = R$ 15.000/m² [FP, anúncio]. Fica como limite superior. Não somo anúncio com escritura numa média só. Desconto: ver seção 3 (não aplico desconto numérico). |
| **C3**: Lotes 22 + 23 Qd C unificados, anúncio 08/2026, "1.200 m²", R$ 9.600.000 | **REJEITA** | 1.200 m² é exatamente 2 lotes de 600 m², ou seja, **área de terreno, não área construída**. O "R$ 8.000/m²" do corretor divide o preço pela área do terreno e não se compara com R$/m² construído. Também é lote duplo (outro produto) e é anúncio. A área construída não foi informada, então o dado não entra no cálculo. |
| **C4**: Lote 09 **Qd C, fundos para o lago**, **escritura 06/2026**, 500 m² construídos, R$ 7.500.000 | **ACEITA COM RESSALVA** | Venda fechada, recente, na mesma quadra e na mesma posição (fundos para o lago) do Lote 17. É o comparável mais parecido com o nosso lote. Conferi: 7.500.000 / 500 = R$ 15.000/m² [FP]. Ressalvas: (a) o número de pavimentos não foi informado (as outras linhas dizem "2 pav."; esta não diz); (b) mesma dúvida de C1 sobre o que entra nos 500 m²; (c) a venda é de 06/2026, antes de qualquer discussão sobre APP do lago. Se a APP de 30 m for confirmada, ela provavelmente atinge também o Lote 09 e os demais lotes de fundos para o lago, e o preço de C4 pode não se repetir (ver seção 5). |
| **C5**: Condomínio Jardim dos Socós (vizinho), 2 pav. + **subsolo + rooftop com piscina**, anúncio 09/2026, 680 m², R$ 11.560.000 | **REJEITA** | São três falhas ao mesmo tempo: (1) os atributos que valorizam a casa (subsolo, rooftop com piscina) são **vedados** no Reserva das Garças (Art. 7 e Art. 8 do Regramento), então nada nela representa o que o cliente pode construir; (2) 680 m² está fora da faixa de qualquer cenário (o maior é 480 m²); (3) é anúncio, em outro condomínio. É a linha que puxa a média do corretor para cima (R$ 17.000/m²). |
| **C6**: Lote 31 Qd B, **escritura 11/2021**, "420 m²", R$ 3.780.000 | **REJEITA** | A data tem quase 5 anos em relação à referência (02/10/2026). Não existe índice de preço próprio para casa em condomínio no Recreio que permita atualizar o valor com fonte: o FipeZAP Venda mede apartamentos, não casas. E a área não diz se é construída ou de terreno. Fica registrado só como histórico, sem número usado. |

**Média do rodapé (R$ 12.833/m²):** a conta está certa: (13.000 + 15.000 + 8.000 + 15.000 + 17.000 + 9.000) / 6 = R$ 12.833/m². **O método é inválido.** A média simples junta:
- 3 vendas e 3 anúncios;
- 1 linha com R$/m² de terreno (C3);
- 1 linha de outro condomínio com atributos vedados aqui (C5);
- 1 linha de 2021 (C6).

O número coincidir com C1 (R$ 13.000) é acaso: os erros de C3 e C6 (para baixo) compensam o erro de C5 (para cima). Média certa com dado errado não fica certa.

**Conclusão do rodapé, lado de mercado:**
- **"R$ 7,67 mi para 590 m²"** (13.000 × 590 = 7.670.000, conta conferida). Os 590 m² vêm do estudo de massa de 2024, que o Legal já descartou. A área possível é 457,44 m² (S1). Só a troca de área já tira cerca de R$ 1,72 mi desse número, mesmo mantendo os R$ 13.000/m² do corretor (7.670.000 − 5.946.720) [EF]. **Não usar.**
- **"R$ 8,8 mi com rooftop"**: atribui cerca de R$ 1,13 mi (8,8 − 7,67) a um rooftop **vedado** pelo Regramento (Art. 7). Mercado não paga por área que não pode existir. O número não tem nenhum comparável por trás. **Não usar.**
- **"Outorga de R$ 380 mil para 300 m², simulada no Lote 5 do Jardim dos Socós"**: pelo lado do mercado, não há área adicional a vender (CAM = 1,0), então essa simulação não muda o valor de revenda de nenhum cenário. Ela foi feita em outro condomínio, com outra subzona (CAM 1,5), e trata de custo, não de valor. O custo da OODC é com Villaça; registro só que, para mim, esse número é irrelevante.

---

## 2. Comparáveis reais da web

**Fonte usada:** páginas individuais da Attria (attria.com.br) e da Consultoria Imobiliária VM, **todas abertas uma a uma** em 02/10/2026. Todos os números da web são **anúncios** (preço pedido). Não achei nenhuma venda fechada publicada.

**Limitação forte de tipo:** quase todos os anúncios na faixa de metragem são **triplex com terraço**, com lote pequeno (250 a 300 m²). O Reserva das Garças proíbe essa configuração (2 pavimentos, sem terraço na cobertura) e tem lotes de cerca de 600 m². Mantive esses anúncios porque o tipo é o mesmo (casa unifamiliar em condomínio, alto padrão) e marquei a diferença em cada linha. Só W5 é de 2 pavimentos confirmado. Nenhum comparável web é do Reserva das Garças, que é fictício.

### 2.1 Faixa S1/S2 (cerca de 430 a 520 m²): todos no Recreio dos Bandeirantes

| # | Imóvel / condomínio | Área construída | Terreno | Pav. / terraço | Suítes | Preço pedido | R$/m² [EF] | Publicado em | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Bothanica Nature (cód. CA2947) | 450 m² | n/d | triplex, com terraço | 3 | R$ 4.850.000 | 10.778 | 28/08/2026 | [Attria CA2947](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7810eaef-b251-4404-a57c-fb28d465e929) | boa, mas a listagem dizia "Del Lago" e a página individual diz "Bothanica Nature" (considerei a página individual) |
| W2 | Artlife (cód. CA2948), casa de 2020 | 485 m² | 485 m² | 3 pav., varanda gourmet | 4 | R$ 3.999.000 | 8.245 | 28/08/2026 | [Attria CA2948](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-485m2/5e1e83bc-6979-496c-a913-2b1a88ae8610) | boa |
| W3 | Riviera Del Sol, Estr. Ver. Alceu de Carvalho 665 (cód. CA0159) | 450 m² | **600 m²** | triplex, terraço com hidro | 5 | R$ 4.800.000 | 10.667 | 02/06/2026 | [Attria CA0159](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7a59356d-c5f1-4f0a-9fce-952f5c41fb76) | boa. **É o mais parecido em lote (600 m²) e metragem.** |
| W4 | condomínio não informado, "espelho d'água no entorno" (cód. CA2879) | 450 m² | 275 m² | 3 níveis | 4 | R$ 3.900.000 | 8.667 | 27/05/2026 | [Attria CA2879](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/3f4cd0dd-1fbf-4af4-a6f6-f137107e5556) | média (condomínio não identificado) |
| W6 | Estr. Ver. Alceu de Carvalho 665 (Riviera Del Sol) (cód. 001867) | 500 m² | 800 m² | não informado | página diz "2 suítes" em 5 quartos | R$ 4.450.000 | 8.900 | **sem data** | [VM 001867](https://consultoriaimobiliariavm.com.br/imovel/casa-a-venda-5-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-500m2-id-364) | **fraca**: sem data, pavimentos não informados, dado de suítes incoerente |
| W7 | Riviera Del Sol (cód. 002243) | 469 m² | 263 m² | triplex, terraço | 4 | R$ 4.200.000 | 8.955 | **sem data** | [VM 002243](https://consultoriaimobiliariavm.com.br/imovel/casa-de-condominio-a-venda-4-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-469m2-id-732) | média: sem data |

Faixa web S1/S2 (n = 6 anúncios): R$ 8.245 a 10.778/m²; mediana R$ 8.928/m² [EF]. Sem W6 e W7, que não têm data, a faixa fica igual: R$ 8.245 a 10.778/m².

**Fora da faixa de metragem, só como referência de tendência (não entram no cálculo):**
- **W5:** Parque das Palmeiras (cód. CA0465), 400 m² em terreno de 300 m², **2 pavimentos**, 4 suítes, "Casa Alto Padrão", R$ 4.200.000, ou R$ 10.500/m², publicado em 02/06/2026. [Attria CA0465](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-400m2/f4e2f578-514a-43c5-8375-c65a034f6114). É o único de 2 pavimentos confirmado e fica 30 m² abaixo da faixa.
- **W8:** Del Lago, Av. Guilherme de Almeida 90 (cód. CA0121), 570 m², 5 suítes, pavimentos não informados, R$ 7.000.000, ou R$ 12.281/m², publicado em 01/09/2026. [Attria CA0121](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-ou-aluguel-5-quartos-avenida-guilherme-de-almeida-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-570m2/bb5b5494-0b0d-49a2-b7c2-d112b5680511). É o anúncio web mais caro por m² que achei, e ainda fica abaixo de C1.
- **W9:** 392 m² em terreno de 250 m², 4 suítes, "alto padrão", R$ 2.939.000, ou R$ 7.497/m², publicado em 27/05/2026. [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-392m2/d7db5acb-d6d4-4204-9133-84a1e3aa02b5).

### 2.2 Faixa S3 (cerca de 280 a 330 m²): Recreio dos Bandeirantes

| # | Imóvel / condomínio | Área | Terreno | Pav. | Suítes | Preço pedido | R$/m² [EF] | Publicado em | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|
| W10 | Riviera Del Sol (cód. CA0291), "acabamento de alto padrão" | 315 m² | 286 m² | triplex | 3 | R$ 4.250.000 | 13.492 | 05/08/2026 | [Attria CA0291](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-315m2/8be15c9f-e2bf-4959-9e8d-e22685e5ec48) | boa |
| W11 | condomínio não informado (cód. CA0467) | 310 m² | n/d | triplex | 3 | R$ 2.100.000 | 6.774 | 03/08/2026 | [Attria CA0467](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-310m2/7a22c151-ec29-4686-9a3b-65a53bbcb317) | fraca: o padrão não foi declarado, pode não ser alto padrão |

**Fora da faixa, só como referência:**
- **W12:** Vivendas do Sol (CA, 267 m², aparentemente 2 pavimentos, 2 suítes), R$ 3.000.000, ou R$ 11.236/m², 01/08/2026. [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-267m2/01f107e3-ac64-420c-9dd1-7aed1a173b78)
- **W13:** triplex de 370 m², 4 suítes, alto padrão (CA2932), R$ 3.990.000, ou R$ 10.784/m², 28/07/2026. [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-370m2/0aa2d877-00ad-48ed-92ea-b857288ff261)

### 2.3 Tentativas sem sucesso (registradas; nenhum número delas foi usado)

- **Loft:** os anúncios individuais retornaram **HTTP 410** (`.../casa-rua-jose-mindlin-...-306m2/0lseb2nv`, `.../home/reknix8h`, `.../4-quartos-312m2/x7cakfzc`). Outros dois abriram só o cabeçalho, com preço e sem área (Av. Aldemir Martins, R$ 3,5 mi e R$ 2,9 mi). Também descartei os R$/m² que apareceram só no resumo da busca (por exemplo, 312 m² a R$ 8.012/m² e 283 m² a R$ 10.247/m²), porque não abri o anúncio.
- **ImóvelWeb:** retornou **HTTP 403** (`.../casa-a-venda-recreio-4-quartos-450-m-rio-de-2990080638.html`). O "450 m², R$ 3,65 mi" do resumo da busca não foi usado.
- **CasaMineira:** retornou **HTTP 403** na listagem.
- **Roberto Almeida Imóveis:** a página do Riviera Del Sol de 600 m² deu **404**.
- **Barra da Tijuca / Vargem:** não precisei ampliar o raio para S1/S2, porque havia anúncios no Recreio. Para S3 a busca na Barra e nas Vargens também caiu em Loft e ImóvelWeb (bloqueados), sem anúncio individual aberto.

---

## 3. Diferença entre preço anunciado e preço fechado

**Fonte:** Raio-X FipeZAP, 2º trimestre de 2026, conforme reportagem do Portas publicada em 18/08/2026: [portas.com.br](https://portas.com.br/noticias/desconto-medio-venda-imoveis-fipezap/) (acesso em 02/10/2026).
- Desconto médio de **14%** considerando só as transações que tiveram desconto.
- Desconto médio de **9%** considerando todas as transações.
- **65%** das transações tiveram desconto (12 meses até junho/2026).

Referência anterior: 3º trimestre de 2025, desconto de cerca de 8% em todas as transações e 68% delas com desconto ([InfoMoney, 14/11/2025](https://www.infomoney.com.br/?p=3103082)).

**Ressalva de fonte:** não abri o PDF primário do 2º trimestre de 2026. O caminho que tentei no DataZAP deu 404. O número vem de reportagem (fonte secundária).

**Decisão: não aplico desconto numérico.** A pesquisa é nacional e não separa resultados por cidade, por faixa de preço ou por tipo de imóvel (casa em condomínio versus apartamento). Aplicar 9% num anúncio de casa de R$ 7 mi no Recreio seria trocar um número inventado por outro. Uso a pesquisa só para dizer que **anúncio é teto, não valor**. Por isso C2 e todos os W ficam fora da faixa principal.

Só para Villaça ter a ordem de grandeza: se o desconto médio nacional valesse para C2, ele cairia de R$ 15.000 para cerca de R$ 13.650/m² [EF, sensibilidade, não é estimativa adotada].

---

## 4. Faixas por cenário

**Base de área:** as faixas multiplicam o R$/m² pela **área computável** que o Legal passou. Os comparáveis falam em "área construída", que provavelmente inclui áreas não computáveis. Quando a Arquitetura definir a área total, Villaça precisa recalcular **sobre a mesma base** dos comparáveis, que é desconhecida. Isso precisa ser perguntado (seção 6).

Somar áreas não computáveis, como varanda e garagem, **não** acrescenta valor no mesmo R$/m².

### S1: 457,44 m² (cenário adotado)
- **Faixa principal [EF]:** R$ 13.000 a 15.000/m² (C1 e C4, vendas fechadas no mesmo condomínio), o que dá **R$ 5.946.720 a R$ 6.861.600**.
- **Teto de oferta [FP, anúncio]:** C2 a R$ 15.000/m², coerente com o topo da faixa.
- **Controle de mercado web [EF]:** R$ 8.245 a 10.778/m², o que dá R$ 3.771.593 a R$ 4.930.288 (6 anúncios, outros condomínios, a maioria triplex com lote menor).
- **Amostra válida:** dossiê com 3 dados (2 vendas, 1 anúncio); web com 6 dados (0 vendas, 6 anúncios).
- **Confiança: média-baixa.**
  - A favor: tipo, local (mesmo condomínio), metragem e data batem.
  - Contra: só 2 vendas; as escrituras não foram conferidas; a área dos comparáveis tem base desconhecida; e há uma distância de pelo menos 20% para todo o mercado web.
- Topo ou base da faixa? O Lote 17 tem fundos para o lago, como C4 (R$ 15.000), e isso puxaria para o topo. Mas, enquanto a APP estiver em aberto, um comprador informado desconta esse risco. **Não escolho um ponto dentro da faixa.**

### S2: 480,00 m² (só se a divisa com o Lote 16 for regularizada)
- **Faixa principal [EF]:** R$ 13.000 a 15.000/m², o que dá **R$ 6.240.000 a R$ 7.200.000**.
- **Controle web [EF]:** R$ 3.957.600 a R$ 5.173.440.
- **Amostra e confiança:** iguais às de S1 (**média-baixa**).
- **Diferença S2 − S1:** 22,56 m² × R$ 13.000 a 15.000 = **R$ 293.280 a R$ 338.400** [EF]. Usar o mesmo R$/m² é aceitável aqui porque a diferença de área é de cerca de 5%. Não é a extrapolação de média de bairro que meu método proíbe.
- O topo da faixa (R$ 7,2 mi) é igual ao preço pedido de C2, que tem exatamente 480 m². Isso reforça que o topo é teto, não valor esperado.

### S3: 297,28 m² (se a APP de 30 m for confirmada)
- **Não achei comparável real.** O condomínio não tem nenhuma venda nem anúncio perto de 300 m² (os dados do dossiê vão de 420 a 1.200 m²). Na web há 2 anúncios na faixa (W10 a R$ 13.492/m² e W11 a R$ 6.774/m²), com dispersão de 2 vezes. Um deles nem declara o padrão. **[NC] por comparável real.**
- **Interpolação declarada, com ressalva forte e não adotada como estimativa:** aplicar a faixa do condomínio (R$ 13.000 a 15.000/m²) a 297,28 m² daria R$ 3.864.640 a R$ 4.459.200. **Essa conta não se sustenta**, por três motivos:
  1. **Efeito de tamanho.** O terreno no Reserva das Garças pesa muito no valor (lote de cerca de R$ 3,3 mi; ver seção 7). Uma casa menor no mesmo lote tende a ter R$/m² construído **maior**, não igual. Isso empurraria o valor para cima.
  2. **A APP no próprio lote.** Uma faixa de cerca de 18 m de fundo inutilizável, registrada como restrição ambiental, reduz o valor do terreno, e qualquer comprador vê isso na diligência. Isso empurra para baixo.
  3. **Produto fora do padrão do condomínio.** Uma casa de cerca de 300 m² num condomínio de casas de 450 a 500 m² tende a perder valor por isso. Também empurra para baixo.

  Os dois efeitos para baixo não são quantificáveis com fonte. **Rótulo: estimativa com ressalva forte; o risco é para baixo; confiança baixa.**
- **Amostra válida:** 0 vendas, 2 anúncios (1 fraco).

---

## 5. O efeito "fundos para o lago" e o risco de APP

- **O que os dados mostram:** C4 (fundos para o lago, R$ 15.000/m²) foi vendida R$ 2.000/m² acima de C1 (rua interna, R$ 13.000/m²).
- **Não transformo essa diferença em "prêmio do lago".** São 2 vendas, com datas diferentes (03/2026 e 06/2026), metragens diferentes (450 e 500 m²), e padrão e idade desconhecidos. Uma diferença entre 2 dados não isola nenhuma causa. W4 também cita um espelho d'água e anuncia a R$ 8.667/m², abaixo da mediana web, o que não mostra prêmio.
- **Como a APP pode anular esse prêmio:**
  1. No próprio lote, a faixa do fundo que dá para o lago deixa de ser usável (nada de construção, deck ou piscina nela). Sobra a vista, mas com uma restrição que aparece na diligência de qualquer comprador e de qualquer banco.
  2. Se a APP for confirmada para o Lote 17, ela provavelmente vale também para o **Lote 09 (C4)** e para todos os lotes de fundos para o lago. A venda de C4 em 06/2026 aconteceu antes dessa informação existir. **Preço formado sem conhecer uma restrição não serve para precificar o imóvel depois que ela é conhecida.** Nesse caso, C4 deixa de ancorar o topo da faixa, inclusive em S1.
  3. Se a APP **não** for confirmada, o Lote 17 fica na mesma posição de C4 e o topo da faixa de S1/S2 passa a ser defensável.
- Não atribuo percentual de prêmio nem de perda. **[NC]**

---

## 6. O que eu perguntaria num caso real (não contatei ninguém, é ensaio)

| A quem | O quê | Por quê |
|---|---|---|
| Marcelo (corretor) | Número de matrícula e cópia das escrituras de C1, C4 e C6; se "450/500 m² construídos" é área total ou computável e se está averbada; padrão, idade e número de pavimentos de C1 e C4; quanto tempo C2 está anunciado e se já baixou o preço; a área construída de C3 | As vendas do dossiê estão pelo menos 20% acima de todo o mercado web. É preciso confirmar o dado antes de basear o valor nele. |
| Cartório de RI (certidão de inteiro teor, que é pública) | Preço e área declarados nas escrituras de C1 e C4 | Conferir independentemente da palavra do corretor. |
| Administradora / síndico | Vendas de 2025 e 2026 no condomínio; se algum lote de fundos para o lago já teve exigência de APP ou FMP | Aumentar a amostra e saber se o mercado interno já conhece o risco de APP. |
| Banco (via Villaça e Wallenberg) | Que comparáveis o laudo do banco costuma usar para casa em condomínio no Recreio | O limite de 60% do valor (5.14) depende do laudo do banco, não da faixa do corretor. |

---

## 7. R$/m² de terreno implícito no Reserva das Garças

- **Preço pago (5.11):** R$ 3.300.000 [FP].
  - Sobre os 600,00 m² da escritura: **R$ 5.500/m²** [EF].
  - Sobre os 571,80 m² medidos: **R$ 5.771/m²** [EF].
- **Por que isso não é valor de mercado do terreno:**
  - É **uma transação só**.
  - O preço inclui benfeitorias: casa de 1998 com cerca de 180 m², edícula e piscina. Para quem vai demolir, essas benfeitorias podem valer menos que zero (custo de demolição, que é do Mascaró). Sem esse custo, não dá para separar terreno de benfeitoria, nem dizer se o terreno puro vale mais ou menos que os R$ 5.500 a 5.771/m².
- **Controle web (1 dado, fraco):** lote de 525 m² no Condomínio Jardim de Maria, anúncio de R$ 1.770.000, ou **R$ 3.371/m²**, publicado em 28/08/2026. [Attria TE0307](https://www.attria.com.br/imovel/terreno-em-condominio-a-venda-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-525m2/d53ed614-6a87-42ee-833c-25d11dc09e26). É bifamiliar, com possibilidade de desmembramento e projeto aprovado.
  - O preço pago pelo Lote 17 fica 63% a 71% acima desse anúncio (5.500 / 3.371 = 1,63; 5.771 / 3.371 = 1,71) [EF].
  - Os lotes de 180 a 198 m² na mesma listagem saem por R$ 4.050 a 4.949/m², o efeito de tamanho esperado.
  - Com 1 dado não dá para dizer se o Reserva das Garças tem prêmio ou se o lote foi pago acima do mercado. **Conclusão sobre o terreno: [NC] como valor de mercado.** Só a conta sobre o preço pago é [EF].
- **Para a pergunta de Helena** (decisão e linguagem são de Villaça): os 28,20 m² que faltam (600 − 571,80), rateados pelo preço pago, dão 28,20 × R$ 5.500 = **R$ 155.100** [EF].
  - Isso é **aritmética sobre o preço pago**, não perda de valor de mercado. Valor de terreno não é linear com a área.
  - O efeito real da área menor aparece no potencial construtivo (S1 contra S2, seção 4: R$ 293 mil a R$ 338 mil de valor de revenda).

---

## 8. Ressalvas finais

- Nenhum número deste documento é promessa de valor de venda. São faixas, com a origem de cada número declarada.
- Não usei média de bairro. Todos os comparáveis passaram por filtro de tipo (casa em condomínio), padrão (alto) e metragem. A origem geográfica de cada um está declarada: todos são do Recreio, e nenhum precisou vir da Barra ou das Vargens.
- **Qualidade desigual da amostra.** As 2 vendas do dossiê (C1, C4) valem mais que os 6 anúncios web juntos para dizer o valor *neste* condomínio. Os anúncios web valem mais para mostrar que esse valor está acima do resto do Recreio. W6 e W7 (sem data) e W11 (padrão não declarado) são os dados mais fracos.
- Legal (CAB, CAM, APP, divisa) e custo de obra estão fora do meu escopo e não foram tocados.

*Declaração: ENSAIO 003, caso 100% fictício. Os dados do dossiê (5.11 a 5.15) foram tratados como reais dentro do ensaio. Os dados de mercado da web são reais, com link e acesso em 02/10/2026. Ninguém foi contatado.*
