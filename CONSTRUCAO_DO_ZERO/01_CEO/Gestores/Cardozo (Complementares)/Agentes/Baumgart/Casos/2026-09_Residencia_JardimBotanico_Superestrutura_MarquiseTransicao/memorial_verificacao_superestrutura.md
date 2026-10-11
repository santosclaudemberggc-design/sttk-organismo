# Memorial de Verificação — Superestrutura de Concreto Armado
## Residência Unifamiliar, Jardim Botânico/RJ (pilar de transição + marquise em balanço)

**Elaborado por:** Baumgart (Agente Estrutural, equipe Cardozo)
**Acionado por:** Cardozo — Exame 2, Caso 3 (complementar retroativo, POP-FORMACAO-01), com proposta técnica preliminar de escritório terceirizado para revisão item a item
**Data:** 12/09/2026
**Status:** Memorial de VERIFICAÇÃO da proposta preliminar — **NÃO libera Baumgart para assumir o cálculo definitivo** (ver Seção 5)
**Normas de referência:** NBR 6118:2026 Emenda 1 (concreto/CC), NBR 6120:2019 (cargas), NBR 8681:2025 (ações e segurança)

---

## 1. Dados do caso (conforme recebido)

| Item | Valor |
|---|---|
| Uso | Residência unifamiliar |
| Pavimentos | 3 (térreo, 1º pav., pav. superior) |
| Elemento crítico 1 | Pilar de transição no térreo — pilar do pavimento superior não desce à fundação, recebido por viga de transição, libera vão de 6m (integração sala/jantar) |
| Elemento crítico 2 | Marquise em balanço de 2,20m no 1º pavimento, sobre a garagem, concreto armado, uso declarado como "terraço técnico" |
| Origem do material revisado | Proposta técnica preliminar de escritório terceirizado (já trabalhou antes com a Sttickler) |
| Anteprojeto | Aprovado por Lúcio, repassado por Cardozo |

## 2. Classificação estrutural — questão prévia a todo o resto (Item 1 da proposta)

A proposta classifica **todo o projeto como CC1**, com justificativa de "residência unifamiliar padrão, sem uso público, sem grande ocupação". Isso não se sustenta:

- A Skill NBR 6118 (Emenda 1) lista **marquise** como gatilho objetivo de CC3, independente do número de pavimentos ou do caráter privativo do uso. O projeto tem uma marquise em balanço de 2,20m — gatilho presente e explícito.
- Regra já registrada no meu próprio aprendizado (casos anteriores deste Exame): "na dúvida entre classes, prevalece a mais conservadora, até confirmação." Aqui não há nem dúvida — o gatilho da marquise é direto.
- Além da marquise, o projeto tem uma **estrutura de transição** (pilar que não desce à fundação, recebido por viga de transição). Este tipo de sistema é reconhecidamente mais sensível a colapso progressivo na prática da engenharia — mas a Skill que uso como Trilha A **não lista "estrutura de transição" como gatilho nomeado** de CC3 (ela lista: >5 pavimentos, subsolo, marquise, protensão, reforma com eliminação de pilar). Não vou presumir que este é um segundo gatilho automático sem confirmar contra o texto oficial — mas registro como fator agravante que reforça a classificação conservadora, e como pergunta em aberto para Cardozo levar ao texto integral da norma (ver Seção 6, pendência 1).

**Conclusão do item 1: NÃO CONFORME.** A classificação correta, com os dados disponíveis, é **CC3** (gatilho objetivo: marquise), não CC1. Isso não é uma questão de opinião — é um critério listado explicitamente na própria tabela de classes de consequência.

## 3. Revisão item a item da proposta técnica preliminar

| # | Item da proposta | Conformidade | Fonte normativa citada |
|---|---|---|---|
| 1 | Classe de consequência CC1 para todo o projeto | 🔴 **NÃO CONFORME** | NBR 6118:2026 Em.1 — critérios de CC1/CC2/CC3 (marquise = gatilho de CC3) |
| 2 | ATP dispensada "em qualquer hipótese" por ser CC1 | 🔴 **NÃO CONFORME** | Consequência direta do item 1 — reclassificado como CC3, ATP é obrigatória com revisor independente, sem dispensa |
| 3 | Armadura da marquise = flexão padrão (carga permanente + sobrecarga NBR 6120), sem acréscimo | 🔴 **NÃO CONFORME** | NBR 6118:2026 Em.1 — armadura inferior de segurança obrigatória em lajes em balanço/marquises, não opcional |
| 4 | Verificação de flecha ELS = L/250 = 8,8mm | 🟡 **PENDÊNCIA BLOQUEANTE** | NBR 6118 (critério de aceitabilidade sensorial) + NBR 8681 (combinação ELS) — faltam dados para confirmar |
| 5 | Emenda de armadura Ø40mm por traspasse simples | 🔴 **NÃO CONFORME** | NBR 6118:2026 Em.1 — traspasse proibido acima de Ø32mm; exige luva mecânica |
| 6 | Cálculo pela NBR 6118:2023 alegando janela de transição (memorial datado 15/09/2026) | 🔴 **NÃO CONFORME** | Janela de transição (180 dias após 11/03/2026) encerrada em ~07/09/2026 — memorial cai fora da janela |
| 7 | fck 30MPa, cobrimento 3cm, CAA-II autoclassificada ("Jardim Botânico não é orla") | 🔴 **NÃO CONFORME / PENDÊNCIA BLOQUEANTE** | NBR 6118:2026 Em.1 — CAA é insumo obrigatório do contratante, não é arbitrada pelo projetista |
| 8 | fck dos pilares de transição = fck da laje, "por padronização de traço" | 🔴 **NÃO CONFORME / PENDÊNCIA BLOQUEANTE** | NBR 8681:2025 — dimensionamento decorre de esforços solicitantes de cálculo, não de conveniência de obra |

## 4. Detalhamento item a item

### 4.1 Item 1 — Classe de consequência (NÃO CONFORME)

Ver Seção 2. Reclassificação para **CC3** é o ponto de partida obrigatório antes de qualquer outro item — os itens 2 e 3 desta proposta dependem diretamente dele, e ambos foram calculados/dispensados sobre a premissa errada de CC1.

### 4.2 Item 2 — ATP dispensada (NÃO CONFORME)

A proposta dispensa a ATP citando exclusivamente a classificação CC1 ("como o projeto é CC1, ATP não é exigível em nenhuma hipótese"). Com a reclassificação para CC3 (Seção 2), essa dispensa perde o fundamento: pela própria Skill NBR 6118, **CC3 exige ATP com revisor independente, sem exceção** — diferente da divergência não resolvida que existe para CC2 (não é o caso aqui, então não há zona cinzenta a invocar). Não há "dispensa em qualquer hipótese" para CC3.

### 4.3 Item 3 — Armadura da marquise (NÃO CONFORME)

Dois problemas, um bloqueante e um de dado ausente:

1. **Bloqueante:** a Emenda 1:2026 introduziu exigência de **armadura inferior de segurança** em lajes em balanço e marquises — um mecanismo residual contra colapso total, dimensionado para resistir às ações permanentes, independente do dimensionamento convencional à flexão (que cobre a armadura superior de tração). A proposta descreve apenas o dimensionamento padrão à flexão ("o dimensionamento padrão de flexão já cobre a segurança") e não menciona a armadura inferior — que a própria Skill classifica como **não opcional**. Isso é agravado pelo fato de a marquise ser um elemento de terraço acessível (carga de pessoas, não só manutenção eventual).
2. **Dado ausente (pendência):** a proposta não informa o valor numérico da sobrecarga adotada (kN/m²), nem se considerou carga de guarda-corpo/parapeito (a marquise é "terraço técnico" com acesso — presumivelmente tem proteção de borda, que impõe carga horizontal na laje em balanço, NBR 6120: guarda-corpo horizontal 0,8 kN/m). Sem o valor numérico e sem confirmação da inclusão do guarda-corpo, não é possível verificar se "sobrecarga de terraço conforme NBR 6120" foi de fato aplicada corretamente (varanda residencial de acesso restrito = 2,0 kN/m² vs. terraço/cobertura acessível ao público = 3,0 kN/m² — a Skill não resolve sozinha qual dos dois se aplica a um "terraço técnico" privativo; a proposta também não esclarece).

### 4.4 Item 4 — Flecha ELS da marquise (PENDÊNCIA BLOQUEANTE)

A aritmética apresentada está correta (2.200mm / 250 = 8,8mm) — não é isso que está em questão. Três pontos ficam sem informação suficiente para eu confirmar o item:

1. **Vão de referência para balanço:** não está confirmado, nem pela proposta nem pela minha Skill (que não cobre esse nível de detalhe — "consulte a norma na íntegra"), se o limite L/250 para elementos em balanço deve ser calculado sobre o comprimento real do balanço (2,20m, como a proposta fez) ou sobre um vão equivalente maior, prática comum em balanços na norma de concreto armado. Isso muda o valor de referência e preciso confirmar contra o texto oficial antes de aceitar 8,8mm como o limite correto.
2. **Combinação de ações usada:** a proposta não informa qual combinação ELS foi usada para calcular a flecha. Pela Skill NBR 8681, o cálculo de flechas deve usar a combinação **quase-permanente** (ψ2 = 0,3 para uso residencial), não a rara nem a frequente — preciso que o escritório terceirizado declare explicitamente qual combinação usou.
3. **Verificação de frequência natural do piso acessível:** ausente. Marquise/terraço acessível exige verificação de conforto a vibração (frequência natural mínima, referência que já registrei em casos anteriores como ≥3 Hz) — critério de ELS distinto e adicional à flecha estática, não mencionado na proposta.

### 4.5 Item 5 — Emenda de armadura Ø40mm por traspasse simples (NÃO CONFORME)

A Emenda 1:2026 da NBR 6118 **proíbe emenda por traspasse para barras acima de Ø32mm** — exige luva mecânica com resistência mínima 15% superior à resistência de escoamento da barra. A proposta usa Ø40mm nos cantos do pilar de transição (elemento mais crítico do prédio, único caminho de carga do pilar superior até a fundação) e especifica traspasse simples "mesmo procedimento usado nos demais pilares do prédio" — ou seja, aplica a um elemento singular e crítico o mesmo detalhe padrão de pilares comuns, sem considerar nem o diâmetro da barra nem a criticidade do elemento. Isso é uma não conformidade direta e objetiva, sem margem de interpretação.

### 4.6 Item 6 — Vigência normativa (NÃO CONFORME)

Já documentei em caso anterior deste mesmo Exame que a janela de transição da NBR 6118:2023 → 2026 (Emenda 1) é de 180 dias a partir de 11/03/2026, encerrando em **~07/09/2026**. O memorial da proposta está datado de **15/09/2026** — 8 dias depois do fim da janela. Não há mais opção de "calcular pela versão anterior por segurança jurídica": a partir de 07/09/2026, a NBR 6118:2026 (Emenda 1) é a única versão vigente e aplicável, sem exceção facultativa.

Este item não é isolado: se o escritório terceirizado de fato calcular pela NBR 6118:2023, os itens 3 (armadura inferior de segurança de marquise) e 5 (proibição de traspasse acima de Ø32mm) — ambos introduzidos **pela Emenda 1** — não existiriam na versão que pretendem usar. Ou seja, o erro do item 6, se não corrigido, explica e potencialmente encobre os erros dos itens 3 e 5.

### 4.7 Item 7 — CAA autoclassificada (NÃO CONFORME / PENDÊNCIA BLOQUEANTE)

O raciocínio geográfico em si não é implausível — Jardim Botânico é bairro de interior, não de orla, e CAA-II é uma classificação razoável à primeira vista. **O problema é processual, não (necessariamente) numérico:** a Classe de Agressividade Ambiental é insumo de entrada obrigatório do **contratante** (cliente), não uma classificação que o projetista ou o escritório terceirizado arbitra por inferência de localização — mesmo protocolo que já apliquei nos dois casos anteriores deste Exame (Ipanema e Botafogo). O escritório terceirizado autoclassificou CAA-II sem apresentar a definição formal do cliente.

**Pendência bloqueante:** falta a CAA formal do contratante, a ser cobrada por Cardozo junto ao cliente (via Lúcio, que já tem contato de Briefing). Até essa confirmação chegar, fck=30MPa e cobrimento nominal de 3cm ficam como valores propostos, não validados — e mesmo com CAA-II confirmada, não tenho na minha Skill a tabela de cobrimento nominal mínimo por classe de agressividade (a Skill diz explicitamente "não estão aqui — consulte a norma na íntegra"), então o valor de 3cm também precisa ser conferido contra o texto oficial antes da liberação do executivo.

### 4.8 Item 8 — fck dos pilares de transição = fck da laje (NÃO CONFORME / PENDÊNCIA BLOQUEANTE)

A justificativa apresentada ("mesmo fck da laje, por padronização de traço em obra") é um critério de conveniência de execução, não um critério de dimensionamento estrutural. O pilar de transição é o elemento de maior criticidade do edifício — recebe, através da viga de transição, toda a carga do pilar superior que não desce à fundação, tipicamente com esforços concentrados (compressão + momento) muito acima dos de uma laje. O fck de um elemento estrutural deve ser resultado do dimensionamento (esforços resistentes ≥ esforços solicitantes de cálculo, combinações ELU/ELS da NBR 8681), não escolhido a priori por padronização de traço.

**Pendência bloqueante:** falta a memória de cálculo dos esforços solicitantes na base do pilar de transição e na viga de transição (NBR 8681, combinação ELU normal) para verificar se fck=30MPa é de fato suficiente — ou se o elemento exige um concreto de resistência superior. Cobrar do escritório terceirizado, não presumir que "30MPa serve" nem que "30MPa não serve" sem o cálculo.

## 5. O que está no caminho certo — não invento problema onde não há

- O escritório terceirizado ao menos apresentou uma verificação de ELS (flecha) para a marquise — incompleta (Seção 4.4), mas é um passo de processo correto que nem toda proposta preliminar traz.
- O raciocínio geográfico para CAA-II (bairro de interior, não de orla) é diretamente plausível e provavelmente estará correto quando formalizado pelo cliente — o problema apontado no item 7 é de rito (quem classifica), não necessariamente de resultado.
- A aritmética do cálculo de flecha apresentado (2.200mm/250 = 8,8mm) está correta.

## 6. Pendências bloqueantes antes de eu assumir o cálculo definitivo

| # | Pendência | Responsável | Bloqueia |
|---|---|---|---|
| 1 | Confirmar contra o texto oficial ABNT se "estrutura de transição" é gatilho nomeado de CC3 (além da marquise, já confirmada) | Cardozo (acesso ao texto integral) | Classificação final e escopo de ATP |
| 2 | Reclassificar formalmente o projeto para CC3 e contratar ATP com revisor independente | Cardozo, junto ao escritório terceirizado | Liberação de qualquer memorial definitivo |
| 3 | Incluir armadura inferior de segurança no dimensionamento da marquise (Emenda 1) | Escritório terceirizado (ou eu, se assumir o cálculo) | Detalhamento da marquise |
| 4 | Informar valor numérico da sobrecarga adotada na marquise e confirmar inclusão de carga de guarda-corpo | Escritório terceirizado | Verificação de flexão e armadura da marquise |
| 5 | Confirmar vão de referência correto para o limite de flecha em balanço (2,20m real ou vão equivalente) contra o texto oficial | Cardozo (texto integral) | Validação do item 4 (ELS) |
| 6 | Declarar a combinação ELS usada no cálculo de flecha (deve ser quase-permanente, NBR 8681) | Escritório terceirizado | Validação do item 4 (ELS) |
| 7 | Verificar frequência natural do piso acessível (marquise/terraço técnico) | Escritório terceirizado (ou eu, se assumir o cálculo) | Conforto/vibração, ELS |
| 8 | Substituir traspasse simples por luva mecânica nas barras Ø40mm do pilar de transição | Escritório terceirizado | Detalhamento do pilar de transição |
| 9 | Refazer o memorial de cálculo integralmente pela NBR 6118:2026 (Emenda 1) — janela de transição encerrada | Escritório terceirizado | Todo o memorial, especialmente itens 3 e 5 |
| 10 | Obter CAA formal do contratante (cliente), via Lúcio | Cliente, via Lúcio/Cardozo | fck, cobrimento nominal, especificação de concreto |
| 11 | Confirmar cobrimento nominal mínimo para a CAA definida, contra tabela oficial da NBR 6118 (não constante na minha Skill) | Cardozo (texto integral) | Especificação de concreto e armadura |
| 12 | Apresentar memória de cálculo dos esforços solicitantes no pilar/viga de transição (combinação ELU, NBR 8681) para validar ou corrigir o fck=30MPa | Escritório terceirizado | fck dos pilares de transição |
| 13 | Engenheiro civil licenciado CREA-RJ para assinar o memorial definitivo (ART) | Cardozo | Emissão formal do projeto executivo |

## 7. Recomendação final

**Não recomendo aceitar esta proposta técnica preliminar como base para eu assumir o cálculo definitivo.** Dos 8 itens revisados, nenhum foi aprovado sem ressalva: 6 são não conformidades diretas contra critérios objetivos da NBR 6118:2026 Emenda 1 (itens 1, 2, 3, 5, 6, 7 e 8 — CAA e fck também carregam pendência bloqueante de dado ausente) e 1 fica como pendência bloqueante por dados insuficientes para confirmar (item 4). O padrão observado — classificação mais branda que a devida (CC1), dispensa de exigência (ATP), omissão de requisito novo da Emenda 1 (armadura inferior de segurança), detalhe inadequado no elemento mais crítico do edifício (traspasse em barra Ø40mm no pilar de transição), uso da norma antiga fora da janela permitida, autoclassificação de CAA e fck justificado por conveniência de obra — é sistemático o suficiente para eu recomendar a Cardozo tratar esta proposta como preliminar em sentido literal, não como material a refinar em pequenos ajustes.

Devolvo a Cardozo para: (a) formalizar as 13 pendências junto ao escritório terceirizado e ao cliente (via Lúcio), (b) decidir se o escritório terceirizado refaz a proposta com as correções ou se o cálculo definitivo passa a ser conduzido por mim desde a base, e (c) confirmar com Claudemberg/texto oficial ABNT o ponto em aberto sobre "estrutura de transição" como gatilho de CC3 (pendência 1), já que isso não está resolvido nem na minha Skill nem em nenhuma fonte que tenho disponível.

## 8. Notas de transparência sobre as fontes usadas

As Skills de NBR 6118 (Emenda 1), NBR 6120 (cargas) e NBR 8681 (ações e segurança) usadas nesta verificação são baseadas em fontes secundárias (blogs técnicos e resumos), não no texto integral pago da ABNT — ressalva já registrada nas três Skills. Usei-as como checklist de processo e como base para identificar não conformidades objetivas e citáveis (ex.: proibição de traspasse acima de Ø32mm, armadura inferior de segurança obrigatória, janela de transição de 180 dias), mas não como fonte de valores numéricos finais para o memorial de cálculo definitivo (ex.: tabela de cobrimento nominal por CAA, vão equivalente de balanço para flecha). Todos os pontos em que a Skill não tinha profundidade suficiente foram registrados como pendência explícita (Seção 6, itens 1, 5, 11), não presumidos.
