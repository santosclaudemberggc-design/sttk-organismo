# Memorial de Verificação — Condomínio Golden Palm, Reuso 20 Unidades NBR 16783 (Exame 2, Caso E2)

**Agente:** Saturnino (Hidrossanitário). **Caso-teste:** Exame 2 (Shadow → Assisted), Notion `3d592372-eae1-81f0-a9d7-d4859a97dd24`.

Revisão item a item da proposta preliminar do parceiro terceirizado.

---

### Item 1 — Tubulação de reuso na mesma cor da água potável, diferenciada só por etiqueta a cada 10 m
**NÃO CONFORME.** A NBR 16783 exige "sinalização obrigatória e diferenciada da tubulação de água não potável (evitar contaminação cruzada com água potável)." Sinalização "diferenciada" não se cumpre com a mesma cor de tubulação e etiquetas espaçadas — o objetivo da norma é que qualquer pessoa (morador, síndico, encanador) identifique a rede de reuso **de forma contínua e inequívoca**, não só em pontos isolados. Prática de mercado equivalente é cor distinta (tipicamente identificada de forma diversa da água fria) ao longo de todo o trecho, não apenas etiqueta pontual. Fonte: Skill `nbr16783-reuso-agua`, item "Exigências de segurança".

### Item 2 — Um único reservatório de água cinza tratada para descarga + irrigação, mesmo nível de tratamento
**NÃO CONFORME / pendência técnica.** A Skill lista "controle de qualidade por uso pretendido" como exigência da norma — ou seja, o nível de tratamento/monitoramento não é único para todos os usos permitidos. Descarga sanitária interna (contato mais próximo do usuário, ambiente fechado) e irrigação externa têm riscos sanitários distintos. Usar reservatório único com tratamento indiferenciado para os dois destinos não atende a essa exigência. Não posso especificar sozinho o nível de tratamento exigido para cada uso (isso depende de parâmetro técnico/sanitário que minha Skill não detalha) — mas posso afirmar que **tratar os dois usos como equivalentes é o erro**, e escalo a exigência de controle de qualidade diferenciado por uso como pendência a resolver com especialista em tratamento antes de fechar o projeto.

### Item 3 — Extravasor do reservatório de água pluvial ligado à rede de esgoto sanitário
**NÃO CONFORME.** Rio de Janeiro opera em sistema separador absoluto — interligar pluvial e esgoto é proibido pelas NBR 8160/10844 (Skill `nbr5626-8160-hidrossanitario`). O extravasor deve descarregar com air gap (sem conexão direta, evitando retorno) na rede pluvial separativa, nunca no esgoto. Mesmo erro-padrão já identificado no meu Exame 1 (caso Peçanha) — não repito aqui.

### Item 4 — Hidrômetro único compartilhado para as 20 unidades na rede de reuso
**CONFORME.** A NBR 16783, pelo que minha Skill cobre, trata de caracterização, dimensionamento, uso, operação, manutenção e sinalização/segurança da rede de água não potável — não impõe hidrometração individualizada por unidade. Individualizar (ou não) a medição do consumo de água de reuso é decisão de gestão condominial/rateio, não uma exigência técnica desta norma. **Não é erro normativo** — é escolha administrativa do condomínio, fora do escopo técnico que audito aqui.

### Item 5 — Poço de rebaixamento do lençol (1,2 m) como fonte de reuso, "dispensa outorga por ser uso residencial de pequeno porte"
**NÃO CONFORME / pendência bloqueante — não decido sozinho.** Minha Skill confirma que "água de rebaixamento de lençol freático" é fonte alternativa coberta pela NBR 16783. Mas a afirmação de que o uso **dispensa outorga de recursos hídricos** é uma presunção que não está na minha Skill nem posso confirmar — captação de água subterrânea no estado do RJ tipicamente está sujeita a outorga do INEA, independentemente do porte, salvo hipóteses específicas de dispensa que preciso verificar, não presumir. Mesmo padrão de erro já cobrado em exames anteriores do organismo (não presumir vigência/dispensa sem checar fonte primária). Registro como pendência bloqueante: confirmar junto ao Kelsen/base legislativa se há dispensa de outorga aplicável a este porte de captação antes de aprovar o poço de rebaixamento como fonte.

### Item 6 — Reservatório dimensionado só pela fração de descarga (200 L/hab × 0,3), sem considerar sazonalidade da chuva
**NÃO CONFORME.** O volume de água de reuso disponível depende da captação de chuva, que no Rio varia entre meses chuvosos e secos — dimensionar o reservatório apenas pela demanda (consumo) sem cruzar com a disponibilidade sazonal de captação é dimensionamento incompleto: nos meses secos o sistema pode não ter chuva suficiente para sustentar a fração de descarga prevista, sem fallback. Preciso de série histórica pluviométrica local (INMET/dados regionais) para dimensionar a reserva de forma realista — não posso aceitar o número fixo da proposta sem essa verificação. Mesmo tipo de erro do meu Exame 1 (chuva de projeto "120 mm/h" tratada como número fixo em vez de dado de série/IDF local).

### Item 7 — Reservatório de água cinza independente, com bombeamento próprio e reabastecimento por caminhão-pipa em emergência
**CONFORME.** É medida de redundância/resiliência tecnicamente válida: segrega a rede de reuso da rede potável (evitando contaminação cruzada), e prevê contingência (caminhão-pipa) para não comprometer a descarga sanitária das unidades em caso de escassez do sistema de reuso. Não fere nenhuma exigência da Skill — é boa prática de engenharia, não erro.

---

## Notas técnicas de partida do projeto (Saturnino)
- Rede de reuso: sinalização contínua e diferenciada obrigatória em toda a extensão da tubulação, não pontual.
- Tratamento de água cinza: exigir controle de qualidade diferenciado por uso (descarga × irrigação) — pendência para especialista de tratamento.
- Extravasor pluvial: sempre para rede pluvial separativa, nunca esgoto — sem exceção.
- Hidrometração individual: decisão de gestão condominial, não requisito técnico da NBR 16783.
- Poço de rebaixamento como fonte de reuso: aceitável tecnicamente, mas **outorga INEA não pode ser presumida como dispensada** — pendência bloqueante.
- Dimensionamento do reservatório de reuso: exige série pluviométrica/sazonalidade, não só demanda fixa.
- Redundância com caminhão-pipa: aprovada como medida de contingência.

## Pendências bloqueantes (não decido sozinho)
1. Nível de tratamento diferenciado por uso (descarga × irrigação) da água cinza — especialista em tratamento.
2. Outorga de uso de recursos hídricos para o poço de rebaixamento — confirmar com Kelsen/INEA antes de aprovar a fonte.
3. Série histórica pluviométrica RJ para dimensionamento realista do reservatório — dado externo (INMET).

Não assino ART — aponto necessidade de engenheiro sanitarista licenciado para o memorial final.
