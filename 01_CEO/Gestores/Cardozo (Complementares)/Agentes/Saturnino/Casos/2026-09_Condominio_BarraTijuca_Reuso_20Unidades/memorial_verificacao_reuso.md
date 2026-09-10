# Memorial de Verificação — Sistema de Reuso de Água, Condomínio Barra da Tijuca/RJ

**Agente:** Saturnino (Hidrossanitário) | **Caso:** Exame 2 — E2 complexo (Reuso NBR 16783, 20 unidades)
**Data:** 09/09/2026 | **Norma base:** NBR 16783:2019 (Skill `nbr16783-reuso-agua`), complementar à Skill `nbr5626-8160-hidrossanitario`

Revisão item a item da proposta preliminar entregue por parceiro terceirizado, antes de virar memorial oficial.

---

## Revisão item a item

### Item 1 — Água de chuva e água cinza dos banhos misturadas no mesmo reservatório, sem tratamento diferenciado por fonte
**NÃO CONFORME.**
A Skill `nbr16783-reuso-agua` lista, entre as exigências de segurança da norma, **"controle de qualidade por uso pretendido"**. Água de chuva de telhado e água cinza de banho têm cargas de contaminação distintas (a água cinza carrega sabão, gordura corporal, cabelo, biofilme — carga orgânica maior que a água de chuva). Misturar as duas fontes num único reservatório "sem tratamento diferenciado" contraria esse princípio de controle de qualidade por fonte antes do uso final (descarga de bacia e irrigação de área comum, esta última com maior exposição humana). Simplificar a estação de tratamento não é justificativa normativa para dispensar tratamento adequado a cada fonte.
**Pendência bloqueante:** dimensionamento da estação de tratamento (pré-filtragem separada por fonte antes da mistura, ou tratamento único dimensionado para a pior carga das duas fontes) exige engenheiro sanitarista — Saturnino aponta a necessidade, não define o processo de tratamento em detalhe.

### Item 2 — Tubulação de reuso pintada na mesma cor da tubulação de água potável
**NÃO CONFORME.**
A Skill é direta: **"sinalização obrigatória e diferenciada da tubulação não potável (evitar contaminação cruzada)"**. Pintar a rede de reuso na mesma cor da rede potável é o oposto do exigido — elimina a diferenciação visual que existe justamente para evitar conexão indevida ou consumo acidental de água não potável. Padrão estético não é critério que se sobreponha à exigência de segurança da norma.

### Item 3 — Interligação da rede de reuso à rede potável por registro de bloqueio manual, para emergência em estiagem
**NÃO CONFORME.**
A Skill exige **"separação física da rede predial"** entre a rede de reuso e a rede potável. Uma interligação direta entre as duas redes — mesmo com registro manual normalmente fechado — cria risco de contaminação cruzada por retrossifonagem/falha operacional (o mesmo princípio já usado no Exame 1: extravasor de cisterna de reuso não pode se conectar à rede de esgoto sem quebra de carga/air gap; aqui o princípio equivalente é não conectar a rede de reuso à potável sem quebra de carga). A solução tecnicamente correta para complementar o reservatório de reuso em período de estiagem é alimentação complementar por **caixa de separação com quebra de carga (air gap)**, nunca uma interligação direta de redes, mesmo com registro de bloqueio manual.
**Pendência bloqueante:** especificar sistema de reposição em estiagem com quebra de carga (ex.: entrada de água potável no reservatório de reuso via air gap, com boia e sem pressurização cruzada) — a confirmar com engenheiro sanitarista/detalhamento executivo.

### Item 4 — Água de reuso abastecendo também as torneiras de pia de cozinha das 20 unidades
**NÃO CONFORME — duas objeções independentes.**
1. **Fora do escopo do Briefing:** Lúcio definiu o sistema de reuso para "descarga de vasos sanitários e irrigação da área comum ajardinada" — pia de cozinha não consta no Briefing aprovado.
2. **Fora dos usos permitidos pela norma:** a Skill lista os usos permitidos da NBR 16783 — descarga de bacia/mictório, lavagem de pisos/áreas comuns/garagem, lavagem de veículo, irrigação paisagística, uso ornamental, resfriamento. Pia de cozinha envolve contato humano direto e uso alimentar/higiene — não está nessa lista e exige água potável.
**Não presumo alteração de escopo sem instrução de Cardozo/Lúcio** — este item deve ser removido da proposta.

### Item 5 — Parâmetros seguem "NBR 16783:2026 (revisão recente, publicada este ano)"
**NÃO CONFORME — não presumido, marcado como pendência bloqueante.**
A Skill `nbr16783-reuso-agua` registra a norma como **vigente desde 2019**, pesquisada em 20/07/2026, sem qualquer registro de revisão publicada em 2026. Não há base para afirmar a existência de uma "NBR 16783:2026". Esta é exatamente o tipo de armadilha já identificada no Exame 1 (não presumir revisão de norma sem confirmação) — o memorial não pode citar uma versão de norma não verificada.
**Pendência bloqueante:** confirmar junto à ABNT se há revisão de 2026 antes de citar essa versão em qualquer documento oficial. Até confirmação, usar **NBR 16783:2019** (versão confirmada pela Skill).

### Item 6 — Irrigação da área comum ajardinada alimentada por água de reuso, ponto e hidrômetro dedicados, separados da prumada potável, a coordenar com Glaziou
**CONFORME.**
Irrigação paisagística é uso permitido pela NBR 16783 (Skill). Ponto/hidrômetro dedicado e separado da prumada potável atende à exigência de separação física da rede predial. A indicação de interface com Glaziou (paisagismo) está correta — é exatamente a coordenação que a Skill do Hidrossanitário aponta como necessária.

### Item 7 — Memorial reconhece que o texto oficial da NBR 16783 não foi lido diretamente pela equipe, recomendando confirmação antes de mudança de processo
**CONFORME.**
Alinhado à seção "Limitações honestas" da própria Skill: *"Texto oficial ABNT não foi lido diretamente — confirmar antes de qualquer mudança de processo em caso real."* Boa prática de transparência técnica, mantida neste memorial.

---

## Notas técnicas de partida — Sistema de Reuso (Condomínio Barra da Tijuca/RJ)

**Norma aplicável:** NBR 16783:2019 (Skill `nbr16783-reuso-agua`) — fontes alternativas de água não potável.

**Fontes combinadas (conforme Briefing de Lúcio):**
- Água de chuva captada do telhado.
- Água cinza dos banhos das 20 unidades.
- Tratamento deve ser diferenciado por fonte antes de qualquer mistura (Item 1) — engenheiro sanitarista a definir.

**Usos permitidos e definidos no Briefing:**
- Descarga de vasos sanitários das 20 unidades.
- Irrigação da área comum ajardinada (interface obrigatória com Glaziou).
- Pia de cozinha **não** está no escopo nem nos usos permitidos pela norma (Item 4) — removido da proposta.

**Exigências de segurança (Skill NBR 16783):**
- Sinalização obrigatória e diferenciada da tubulação não potável — cor distinta da rede potável (Item 2 corrigido).
- Separação física da rede predial — sem interligação direta com a rede potável; reposição em estiagem via quebra de carga/air gap, não registro de bloqueio direto (Item 3 corrigido).
- Controle de qualidade por uso pretendido — tratamento adequado a cada fonte antes da mistura (Item 1).

**Reservatório de reuso:** local a definir por Saturnino junto ao subsolo técnico, conforme Briefing. Dimensionamento de volume depende de dados ainda não disponíveis (ver pendências).

**Interfaces:**
- Glaziou (paisagismo) — ponto de irrigação da área comum, tipo de vegetação e demanda hídrica.
- Baumgart (estrutural) — compatibilização do reservatório de reuso e casa de máquinas no subsolo técnico.
- Cardozo — necessidade de engenheiro sanitarista licenciado para dimensionamento da estação de tratamento e assinatura de ART; Saturnino aponta a necessidade, não assina.

## Pendências bloqueantes consolidadas
1. Área de captação exata do telhado — não consta no Briefing ("ver projeto arquitetônico, em revisão", sinalizado por Lúcio). Sem esse dado não é possível dimensionar a vazão de água de chuva captada.
2. Estimativa de geração diária de água cinza das 20 unidades — não consta no Briefing, mesma pendência de Lúcio. Sem esse dado não é possível fechar o balanço hídrico do reservatório de reuso.
3. Volume do reservatório de reuso — depende dos itens 1 e 2, não pode ser calculado nesta fase.
4. Dimensionamento da estação de tratamento por fonte (Item 1) — exige engenheiro sanitarista licenciado.
5. Confirmação da versão vigente da NBR 16783 (Item 5) — não presumir "2026" sem confirmação ABNT.
6. Sistema de reposição em estiagem com quebra de carga a especificar (Item 3), em substituição à interligação direta proposta.

## Necessidade de ART
Este memorial é nota técnica de partida elaborada pelo Agente Hidrossanitário Saturnino — não substitui projeto executivo assinado. Estação de tratamento e balanço hídrico do sistema de reuso exigem engenheiro sanitarista licenciado; Saturnino aponta a necessidade, Cardozo registra.
