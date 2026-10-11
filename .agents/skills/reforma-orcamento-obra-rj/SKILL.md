---
name: reforma-orcamento-obra-rj
description: Orçamento de OBRA de reforma residencial no Rio de Janeiro, em reais e com fonte (SINAPI-RJ, CUB Sinduscon-Rio, cotação de fornecedor), da estimativa paramétrica ao orçamento discriminado. Cobre o que é próprio de reforma (demolição item a item, retirada de entulho, imprevistos de condição existente, obra com morador, proteção do que fica), a reserva de imprevistos separada do lucro, o BDI e as alternativas mais baratas (engenharia de valor) sem mexer em segurança. Use sempre que Severiano (ou qualquer Agente da Reforma) for estimar quanto custa executar uma reforma, comparar opções de material, montar a planilha de obra para o cliente ou revisar um aditivo, mesmo que o pedido só diga "quanto fica a obra", "orçamento", "planilha", "custo do piso", "BDI" ou "entulho".
---

# Orçamento de Obra de Reforma — RJ

Estrutura adaptada de `afrexai-construction-estimator` (MIT, github.com/ndesv21/openclaw-master-skills). O conteúdo é brasileiro: todo número em R$ e com fonte e data.

## Regra zero: sem fonte, não é número

Todo preço vem de uma destas fontes, nesta ordem de preferência, e é citado com **fonte + mês/ano + local**:
1. **Cotação real** de fornecedor ou empreiteiro para esta obra (melhor).
2. **SINAPI** (Caixa/IBGE), estado RJ, mês de referência. Diga se é **desonerado ou não desonerado**. Use a composição (código) quando existir.
3. **CUB/m² Sinduscon-Rio** (NBR 12721), só para estimativa paramétrica de área. O CUB é de obra nova: em reforma, ele serve apenas de ordem de grandeza.
4. Preço de varejo (site de loja) apenas para material de acabamento, com link e data.

Número sem fonte só pode aparecer marcado **"estimativa sem fonte — confirmar"**. Nunca prometa custo fechado.

## As 3 etapas do orçamento (cada uma tem uma precisão)

| Etapa | Quando | Base | Precisão a declarar |
|---|---|---|---|
| 1. Ordem de grandeza | 1º contato, antes da visita | R$/m² por ambiente ou por pacote, com fonte | ±30 a 40% |
| 2. Estimativa por serviço | depois da visita e da medição | quantitativo × preço SINAPI ou cotação | ±15 a 20% |
| 3. Orçamento discriminado | projeto aprovado | planilha completa com cotações | ±5 a 10% |

Sempre escreva no topo qual etapa é e qual a precisão. O cliente leigo lê o total como promessa.

## Levantamento de quantidades (o que medir na visita)

Por ambiente: áreas de piso, parede e teto, perímetros (rodapé, soleira, pingadeira), vãos (portas, janelas, portões), pontos (elétrica, hidráulica, iluminação), volumes (escavação, aterro, concreto, entulho). Anote a **perda** aplicada em cada material (ex.: revestimento com corte diagonal perde mais que reto). Foto de cada ambiente amarrada ao item.

## O que é próprio de reforma (o que a obra nova não tem)

- **Demolição e remoção item a item**: piso, revestimento, reboco, alvenaria, cobertura, esquadria. Cada um com unidade e preço próprio. Nunca um valor global de "demolição".
- **Entulho**: volume empolado (o material solto ocupa mais que no lugar), número de caçambas e a licença de caçamba quando ficar na via.
- **Proteção do que fica**: piso que fica, móveis, vizinho, área com morador.
- **Obra com morador**: produtividade menor, horário restrito, limpeza diária. Declare o acréscimo e de onde ele veio.
- **Condição existente escondida**: fiação velha, tubulação, laje, umidade e infiltração, armadura exposta. Trate como **verba de imprevistos**, nunca embutida no preço unitário.
- **Mexer em estrutura** (abrir vão, piscina, laje nova) pede engenheiro. Sinalize ao Rino; Severiano não dimensiona.

## Reserva de imprevistos separada do lucro

- A reserva de imprevistos é um **custo direto à parte**, com percentual declarado e justificado pela incerteza da etapa. Ela **não é lucro** e não entra misturada no BDI.
- Faixa usada como ponto de partida, **a confirmar com a prática da Sttickler**: 10 a 15% em reforma com condição escondida relevante; menos quando a visita já abriu e inspecionou.
- Mostre ao cliente como uma linha separada: "reserva para o que só aparece quando a obra abre".

## BDI (benefícios e despesas indiretas)

Preço de venda = custo direto × (1 + BDI). O BDI cobre administração central, seguro e garantia, risco, despesa financeira, impostos sobre faturamento e lucro.
- Referência pública: Acórdão TCU 2622/2013, faixas de BDI por tipo de obra. **Confira os valores na fonte antes de citar**: é referência para obra pública e serve como teto de sanidade, não como regra.
- Impostos: use a alíquota efetiva real da empresa (regime tributário), **confirmada com o contador**. Não chute.

## Engenharia de valor (como baratear sem estragar)

Para cada item caro, ofereça até 2 alternativas, com o custo, o que muda no visual e na limpeza, e a durabilidade.
- **Nunca** baratear: segurança elétrica (DR, aterramento), estrutura, impermeabilização, guarda-corpo, piscina (casa de máquinas, ralo de fundo seguro).
- A decisão é do cliente; o orçamento só mostra a troca.
- Preste atenção ao perfil do cliente: no caso da Adriana, "fácil de limpar" é critério, então piso com menos rejunte vale mais do que o preço sugere.

## Formato da entrega (para o Rino e a Lina)

1. Cabeçalho: cliente, etapa (1, 2 ou 3), precisão, data, fontes usadas.
2. Tabela por ambiente → serviço: item | unidade | quantidade | preço unitário | fonte | total.
3. Subtotal de custo direto, reserva de imprevistos (linha separada), BDI e total.
4. O que **não** está incluído: móveis, eletrodomésticos, projeto, taxas, mobiliário de piscina.
5. Alternativas de engenharia de valor.
6. Lista de tudo que precisa ser confirmado na visita ou com cotação.

## Erros comuns

- Usar o CUB inteiro em reforma: ele inclui estrutura e fundação de obra nova.
- Esquecer o entulho e a caçamba.
- Somar a reserva de imprevistos dentro do lucro.
- Preço sem mês de referência.
- Total sem a lista do que não está incluído: vira briga na obra.
