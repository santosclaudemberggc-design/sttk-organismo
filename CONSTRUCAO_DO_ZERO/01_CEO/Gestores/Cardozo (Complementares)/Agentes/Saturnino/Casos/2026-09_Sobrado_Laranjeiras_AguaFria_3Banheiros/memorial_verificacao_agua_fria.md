# Memorial de Verificação — Água Fria, Sobrado Laranjeiras/RJ

**Agente:** Saturnino (Hidrossanitário) | **Caso:** Exame 2 — E1 simples (Água Fria, 3 Banheiros)
**Data:** 09/09/2026 | **Norma base:** NBR 5626:2020 (Skill `nbr5626-8160-hidrossanitario`)

Revisão item a item da proposta preliminar entregue por parceiro terceirizado, antes de virar memorial oficial.

---

## Revisão item a item

### Item 1 — Reservatório: 100 L/hab/dia, 400 L total, sem reserva adicional
**NÃO CONFORME.**
A Skill `nbr5626-8160-hidrossanitario` fixa reservatório com volume mínimo de **1 dia de consumo, à razão de 200 L/habitante/dia** (salvo código de obras local que fixe valor diferente — não há esse dado no Briefing). Para 4 moradores, o mínimo é **800 L**, não 400 L. O parceiro usou metade do parâmetro de referência sem justificativa normativa ("residência compacta, consumo baixo esperado" não é critério da norma).
**Pendência bloqueante:** confirmar se o código de obras do município do Rio de Janeiro fixa valor per capita diferente de 200 L/hab/dia para este uso — não há esse dado no Briefing nem foi verificado por Saturnino nesta revisão.

### Item 2 — Pressão estática 460 kPa no térreo, sem VRP
**NÃO CONFORME — duas objeções independentes.**
1. **Inconsistência física com o próprio Briefing:** o Briefing informa desnível de ~8 m entre o reservatório superior (cobertura) e o ponto mais baixo (banheiro do térreo), com alimentação por gravidade. Pressão estática de coluna d'água por gravidade é ρ·g·h ⇒ 1000 kg/m³ × 9,81 m/s² × 8 m ≈ **78,5 kPa**, não 460 kPa. O valor apresentado pelo parceiro (460 kPa) é incompatível com o desnível declarado no próprio Briefing e não foi aceito sem confirmação — pode ser erro de cálculo, unidade trocada (ex.: confundir kPa com outra grandeza), ou premissa de pressão de rede pública somada indevidamente à gravidade num sistema que o Briefing descreve como alimentado só por gravidade a partir do reservatório superior.
2. **Mesmo se o valor de 460 kPa estivesse correto:** a Skill fixa pressão estática máxima de **400 kPa** em qualquer ponto — acima disso, **VRP é obrigatória**, não op­cional por "baixa complexidade". A justificativa do parceiro para dispensar a VRP é normativamente inválida.
**Pendência bloqueante:** recalcular/confirmar a pressão estática real no ponto mais baixo antes de decidir sobre VRP. Se confirmado ~78,5 kPa pela gravidade (consistente com o desnível do Briefing), está dentro do limite de 400 kPa e VRP não seria necessária por este critério — mas o número apresentado pelo parceiro (460 kPa) precisa ser corrigido ou justificado antes de qualquer decisão.

### Item 3 — Banheira de hidromassagem dimensionada com peso do chuveiro (0,4 UP)
**NÃO CONFORME.**
A tabela de pesos relativos da Skill não usa peso de chuveiro para banheira — banheira comum já tem peso próprio (1,5 UP). Mais grave: banheira de **hidromassagem** não é aparelho padrão da tabela (tem bombas/jatos com vazão adicional). A própria Skill adverte: *"Se o Briefing especificar aparelho fora da lista (spa, hidromassagem, torneira privativa), esses têm valor próprio — não extrapole por analogia sem confirmar na norma."* Usar 0,4 UP (chuveiro) é dupla extrapolação indevida — nem é o valor de banheira comum, nem hidromassagem tem valor tabelado nesta Skill.
**Pendência bloqueante:** obter peso relativo (UP) específico da banheira de hidromassagem — via especificação do fabricante do equipamento (vazão de enchimento + jatos) e/ou confirmação direta no texto da NBR 5626:2020. Sem esse dado, ΣUP da coluna que atende o 2º pavimento não pode ser fechado.

### Item 4 — Coluna de água fria encostada ao tubo de queda de esgoto no mesmo shaft
**NÃO CONFORME.**
A Skill é explícita: **"Proibido: tubulação de água potável em contato com esgoto."** Compartilhar o mesmo shaft vertical pode ser aceitável do ponto de vista de compatibilização de layout (interface com Baumgart/Mindlin), mas as tubulações não podem estar em contato físico direto — precisam de separação/fixação independente dentro do shaft, evitando contato e risco de contaminação cruzada em caso de vazamento.

### Item 5 — Velocidade de escoamento 1,2 m/s na coluna principal
**CONFORME.**
A Skill fixa faixa de velocidade de 0,5 a 3,0 m/s para água fria/quente (NBR 5626:2020). 1,2 m/s está dentro do intervalo.

### Item 6 — Separação física de 30 cm entre coluna de água fria e eletrodutos verticais
**CONFORME.**
A Skill lista exatamente essa exigência na coordenação com Landell: *"separação física 30cm água/eletroduto, exigência NBR 5410"*. O item está alinhado à interface correta.

---

## Notas técnicas de partida — Água Fria (Sobrado Laranjeiras/RJ)

**Norma aplicável:** NBR 5626:2020 (água fria/quente), Skill `nbr5626-8160-hidrossanitario`.

**Configuração do projeto (conforme Briefing):**
- 3 pavimentos, 1 banheiro por pavimento (3 banheiros empilhados na mesma coluna/prumada), cozinha e área de serviço no térreo, banheira de hidromassagem no 2º pavimento (suíte).
- Reservatório superior na cobertura, alimentação por gravidade, desnível ~8 m até o ponto mais baixo.
- 4 moradores.

**Reservatório — dimensionamento preliminar:**
- Volume mínimo: 4 hab × 200 L/hab/dia = **800 L** (não os 400 L propostos), salvo código de obras local que indique outro parâmetro (pendência acima).

**Pressão:**
- Pressão estática máxima admissível em qualquer ponto: 400 kPa (acima disso, VRP obrigatória).
- Pressão dinâmica mínima nos pontos de utilização: 10 kPa (1 mca).
- Valor apresentado pelo parceiro (460 kPa no térreo) inconsistente com o desnível de 8 m informado — pendência bloqueante de recálculo (ver Item 2).
- Pressão de entrada da rede pública: **a confirmar com a concessionária** (já sinalizado como pendência pelo próprio Briefing) — necessária para verificar se o reservatório superior precisa de recalque (bomba) a partir de um reservatório inferior, dado que o Briefing não descreve reservatório inferior nem sistema de recalque.

**Dimensionamento de água fria (método dos pesos relativos, Hunter adaptado):**
- Lavatório (×3, um por banheiro): 0,3 UP cada.
- Vaso sanitário (×3, presumindo caixa de descarga — **não confirmado no Briefing, pendência**): 0,3 UP cada se caixa, 2,4 UP cada se válvula.
- Chuveiro (×3): 0,4 UP cada.
- Banheira de hidromassagem (2º pavimento): peso pendente (Item 3).
- Pia de cozinha (térreo): 0,7 UP.
- Máquina de lavar roupa (área de serviço, térreo — presença não confirmada no Briefing além de "área de serviço"): 1,0 UP se houver ponto de água fria dedicado — **pendência: confirmar com Oscar/Briefing se há ponto de máquina de lavar roupa**.
- Qp (L/s) = 0,3 × √ΣUP — só pode ser fechado após resolver as pendências de tipo de vaso sanitário (caixa/válvula), peso da banheira de hidromassagem, e confirmação de ponto de máquina de lavar roupa.

## Pendências bloqueantes consolidadas
1. Volume de reservatório: confirmar se código de obras local do Rio de Janeiro exige valor per capita diferente de 200 L/hab/dia.
2. Pressão estática no ponto mais baixo: recalcular/corrigir o valor de 460 kPa, incompatível com o desnível de 8 m declarado — só então decidir sobre VRP.
3. Peso relativo (UP) da banheira de hidromassagem: obter do fabricante e/ou confirmar na NBR 5626:2020.
4. Tipo de vaso sanitário (caixa de descarga ou válvula de descarga) em cada banheiro — não informado no Briefing, necessário para ΣUP e ΣUHE.
5. Confirmação de ponto de máquina de lavar roupa na área de serviço.
6. Pressão de entrada da rede pública — a confirmar com a concessionária (Águas Rio), conforme já sinalizado no Briefing.

## Necessidade de ART
Este memorial é nota técnica de partida elaborada pelo Agente Hidrossanitário Saturnino — não substitui projeto executivo assinado. Assinatura de ART exige engenheiro civil/sanitarista licenciado (Cardozo registra).
