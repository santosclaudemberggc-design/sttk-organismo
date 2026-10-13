---
name: reforma-preco-projeto-custo
description: Como calcular o preço do PROJETO de reforma pelo custo de produzi-lo (horas da equipe × custo da hora + despesas + impostos), quando a estratégia comercial é cobrar o projeto barato para fechar a obra. Inclui a conferência de sanidade contra a tabela de honorários do CAU e a regra de não vender abaixo do custo. Use sempre que Severiano (ou o Rino) for dar preço a um projeto de reforma, montar a proposta de honorários ou responder "quanto custa o projeto", mesmo que o pedido só diga "honorários", "valor do projeto", "proposta" ou "cobrar barato para pegar a obra".
---

# Preço do Projeto de Reforma a Custo

## A estratégia (decisão comercial da Sttickler, caso Adriana, 11/10/2026)

Cobra-se pelo projeto **só o custo de produzi-lo**; o ganho está em **fechar a obra**. Então o preço do projeto tem piso: nunca abaixo do custo real. Projeto dado de graça vira prejuízo quando a obra não fecha.

## Modo "valor simbólico" (decisão de Claudemberg, 11/10/2026, caso Adriana)

Para cliente simples, com orçamento apertado, o preço de custo cheio (horas × custo da hora) **não** é cobrado. Neste modo:
- Entrega-se **o projeto completo**, o melhor possível, com tudo o que o cliente precisa para a obra. **Revisões sem limite dentro do programa combinado na visita.** Mudança de programa (ex.: trocar a piscina por uma edícula) é projeto novo, e isso vai escrito no termo de aceite.
- O preço é **simbólico**: cobre só o que sai do bolso durante o projeto, ou seja, alimentação na rua e deslocamento nas visitas, mais a parte de luz e internet do escritório em casa no período. O teto para o caso Adriana é **R$ 5.000**.
- O valor do projeto é **abatido do preço da obra** se o cliente contratar a obra com a Sttickler. O termo de aceite diz **até quando** o abatimento vale e **em qual parcela** da obra ele entra. Esses dois números são decididos por Claudemberg em cada caso.
- Pode haver **presente** de fidelização (Adriana: o 2º pavimento entra sem custo, por fazer a obra com a gente).
- A conta de horas × custo da hora continua sendo feita, **só para uso interno**: Claudemberg sabe quanto está investindo para fechar a obra. **Não se mostra ao cliente** o valor real nem o desconto (decisão de 11/10/2026: o cliente pode se sentir diminuído).

Quem decide se o cliente entra neste modo é Claudemberg.

**Nenhum preço vai ao cliente sem a proposta escrita e o termo de aceite** (Skill `reforma-proposta-termo-aceite`).

## A conta (modo custo, quando não for simbólico)

1. **Lista de entregáveis** do projeto (ex.: levantamento e medição, estudo com imagens, projeto executivo das áreas, iluminação, detalhamento de piscina e gourmet, quantitativo para o orçamento de obra, reuniões).
2. **Horas por entregável e por pessoa** (arquiteto, desenhista, render). Estime com base em projetos parecidos; quando não houver histórico, declare "estimativa sem histórico".
3. **Custo da hora** de cada pessoa: (salário ou retirada + encargos + rateio de custo fixo do escritório) ÷ horas produtivas do mês. **Esses números são da Sttickler e precisam vir de Claudemberg.** Não invente.
   **Fonte atual:** `_financeiro/custo_hora_claudemberg.xlsx` (fora do git, porque são finanças pessoais). Em 11/10/2026, o piso era **R$ 105,67/h**, e um ambiente médio de 5 h custava R$ 528,37. Leia sempre a planilha, porque o valor muda. O projeto é emitido como **pessoa física**, e a obra como CNPJ (Sttickler Empreendimento).
4. **Despesas diretas**: deslocamento até a obra (Irajá), impressão, render terceirizado, taxas.
5. **Impostos**: o projeto é emitido como pessoa física. A reserva de INSS e IR já está dentro do custo da hora da planilha (estimativa, a confirmar com o contador). Não some imposto duas vezes.
6. **Preço** = horas × custo da hora + despesas diretas. O imposto já está no custo da hora. Lucro zero ou mínimo, por estratégia.

## Conferência de sanidade

- Compare com a **tabela de honorários do CAU/BR** (referência de mercado, por percentual do custo da obra ou por área). Se o preço a custo ficar muito abaixo, mostre a diferença ao Rino: ela é o "desconto estratégico" e precisa ser declarada na proposta como tal, para valorizar o projeto aos olhos do cliente. **Confira a versão vigente da tabela antes de citar.**
- Se o cliente fechar a obra, avalie abater o valor do projeto do preço da obra. Isso é decisão de Claudemberg.

## Formato da entrega

Tabela de entregáveis × horas × custo; despesas; impostos; preço; referência CAU com a diferença; premissas e o que precisa de confirmação.
