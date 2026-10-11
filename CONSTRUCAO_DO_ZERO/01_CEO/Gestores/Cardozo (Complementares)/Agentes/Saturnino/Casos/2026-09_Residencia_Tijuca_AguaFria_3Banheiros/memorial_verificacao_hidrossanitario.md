# Memorial de Verificação — Residência Tijuca/RJ, Água Fria 3 Banheiros (Exame 2, Caso E1)

**Agente:** Saturnino (Hidrossanitário). **Caso-teste:** Exame 2 (Shadow → Assisted), Notion `3d592372-eae1-81ee-81bd-dafcd6a011ef`.

Revisão item a item da proposta preliminar do parceiro terceirizado.

---

### Item 1 — Pressão estática 450 kPa aceita sem dispositivo adicional
**NÃO CONFORME.** NBR 5626:2020 fixa pressão estática máxima de **400 kPa (40 mca) em qualquer ponto da instalação**. 450 kPa excede o limite normativo. Não é "aceitável por estar na faixa usual" — é **obrigatória a instalação de válvula redutora de pressão (VRP)** no ramal ou na entrada do trecho afetado. Fonte: Skill `nbr5626-8160-hidrossanitario`, seção 1 ("Parâmetros Obrigatórios de Pressão" e "O que NÃO pode: Pressão estática > 400 kPa — obrigatório válvula redutora de pressão").

### Item 2 — Ramal do vaso sanitário do lavabo em DN 75 mm
**NÃO CONFORME.** A Skill fixa regra de ouro sem exceção por tipo de acionamento: "ramal de esgoto de vaso sanitário nunca abaixo de DN 100 mm" — vale tanto para caixa acoplada (UHE 4) quanto para válvula de descarga (UHE 6). O peso menor da caixa acoplada influencia o dimensionamento do tubo de queda/coletor a jusante, não o DN mínimo do ramal individual do aparelho. DN 75 mm viola a norma. Fonte: mesma Skill, seção 2, tabela UHE + "Regra de ouro".

### Item 3 — Reservatório único de 400 L, sem reservatório inferior
**CONFORME.** A Skill distingue função de cada reservatório: "Reservatório inferior: para sucção da bomba elevatória." Este projeto não tem bomba de recalque — a alimentação é por gravidade direta a partir do reservatório superior. Sem bombeamento, não há exigência técnica de reservatório inferior; ele só é necessário quando existe elevatória para recalcar a água até o superior. O volume de 400 L (200 L/hab × 2 moradores) atende ao mínimo de 1 dia de consumo. **Este item está correto** — sinalizo que não é erro, apesar de a alternativa (reservatório único) poder parecer, à primeira vista, uma simplificação indevida.

### Item 4 — Ramal de esgoto da pia de cozinha (DN 50 mm) em 1%
**NÃO CONFORME.** A Skill fixa: "Inclinação mínima: 2% (1 cm por metro) para tubulações DN ≤ 100 mm; Inclinação mínima: 1% para tubulações DN > 100 mm." DN 50 mm é ≤ 100 mm, logo a inclinação mínima exigida é 2%, não 1%. 1% está listado explicitamente nos "Erros comuns que Saturnino deve evitar": "Inclinação de esgoto insuficiente (<2%) — provoca entupimento recorrente." Reduzir para 1% "para o caimento não aparecer no forro" é justamente esse erro.

### Item 5 — Tubulação de água fria a 15 cm dos eletrodutos
**NÃO CONFORME.** Coordenação obrigatória com Landell (Skill, seção 5): "separação física de 30 cm entre tubulações de água e eletrodutos (NBR 5410 exige)." 15 cm está abaixo da distância mínima. Preciso escalar a Cardozo para confirmar com Landell antes de fechar o layout do shaft — reduzir a distância para "economizar espaço" não é decisão que Saturnino tome sozinho, pois compromete o projeto elétrico também.

### Item 6 — Ventilação apenas primária, prédio de 2 pavimentos
**CONFORME.** A Skill diz: "Coluna de ventilação obrigatória em tubos de queda que atendem mais de 5 andares" e "Ventilação primária (prolongamento do tubo de queda acima da cobertura) — o mínimo." Um prédio de 2 pavimentos está muito abaixo do limiar de 5 andares que exigiria coluna de ventilação secundária. Ventilação primária isolada é suficiente e está corretamente especificada aqui.

### Item 7 — Peso da ducha higiênica igual ao do lavatório (0,3 UP), sem fonte
**PENDÊNCIA — não posso confirmar nem rejeitar sozinho.** A tabela de pesos da minha Skill (UP/UHE) não lista "ducha higiênica"/bidê como aparelho — cobre lavatório, vaso sanitário, chuveiro, banheira, pia de cozinha, máquina de lavar louça/roupa. A própria Skill reconhece essa lacuna em "Limitações honestas": "verificar se o Briefing especifica aparelhos fora da lista (spa, hidromassagem, torneira privativa) que têm valores específicos." Adotar 0,3 UP "por proximidade de uso" é uma aproximação razoável de engenharia, mas **não é dado normativo verificado** — não posso assinar como se fosse tabela oficial sem confirmar o valor correto (fabricante do registro/ducha higiênica, ou tabela complementar da NBR 5626 não coberta nesta Skill). Registro como pendência a confirmar antes de fechar o memorial final, não como erro do parceiro nem como aprovação automática.

---

## Notas técnicas de partida do projeto (Saturnino)
- Reservatório: 400 L (mín. 1 dia, 200 L/hab), único elevado — válido sem bomba de recalque.
- VRP obrigatória no trecho com pressão estática 450 kPa (item 1) — bloqueante até ajuste de projeto.
- Todos os ramais de vaso sanitário em DN ≥ 100 mm, independente do tipo de acionamento.
- Inclinações de esgoto: DN ≤ 100 mm → mín. 2%; DN > 100 mm → mín. 1%.
- Separação mínima de 30 cm entre tubulação de água e eletrodutos — a confirmar layout final com Landell.
- Ventilação de esgoto: primária suficiente para 2 pavimentos (não exige coluna secundária).
- Peso da ducha higiênica do lavabo: pendência técnica a confirmar (fonte normativa/fabricante) antes do dimensionamento final do ramal.

## Pendências bloqueantes
1. Pressão 450 kPa exige VRP — sem isso, projeto não pode ser fechado como está.
2. Layout de shaft com 15 cm de água×eletroduto precisa de revisão conjunta com Landell (30 cm mínimo).
3. Peso normativo da ducha higiênica não confirmado — não presumo 0,3 UP como definitivo.

Não assino ART — aponto a necessidade de engenheiro civil/sanitarista licenciado para o memorial final; Cardozo registra o encaminhamento.
