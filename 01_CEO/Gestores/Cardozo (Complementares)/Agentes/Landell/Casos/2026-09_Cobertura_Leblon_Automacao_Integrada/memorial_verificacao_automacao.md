# Memorial de Verificação — Automação Residencial Integrada — Revisão de Proposta Preliminar

**Projeto:** Cobertura duplex, Leblon/RJ (cliente fictício) — automação completa: iluminação, persianas motorizadas (inclusive varanda externa), climatização, som ambiente e controle de acesso (fechadura eletrônica na porta principal).
**Caso:** Exame 2 (Shadow → Assisted), **Caso 3 — complementar retroativo**, aplicado por instrução de Cardozo em 12/09/2026 para completar o mínimo de 3 casos exigido pelo POP-FORMACAO-01 (apenas 2 haviam sido aplicados na execução original de 08-09/09/2026: Caso 1 elétrica básica, Caso 2 SPDA/COSCIP). Landell já foi promovido a Assisted em 09/09/2026 com base nos 2 casos anteriores — esta promoção não é desfeita por este caso — mas o caso foi respondido com o mesmo rigor de um caso real, sem tratamento simbólico.
**Revisor:** Landell (Automação+Elétrica), equipe Cardozo (Complementares).
**Data:** 12/09/2026.
**Documento revisado:** proposta técnica preliminar elaborada por integrador terceirizado (7 itens), sobre automação residencial integrada à elétrica.

**Bases usadas:**
- NBR 5410:2004 (vigente — única com força normativa hoje) e o princípio geral de segregação de circuitos (cada circuito terminal concebido para que uma falha não afete o restante da instalação), via Skill `nbr5410-eletrica-automacao`.
- Tabela de protocolos de automação (KNX, Zigbee/Z-Wave, Modbus) da mesma Skill — que também define, na seção "Coordenação com outros Agentes", a exigência de IP65 para circuitos/equipamentos de jardim (Glaziou), usada aqui por analogia para equipamento em área externa.
- Skill de mercado `automacao-residencial-tendencias` (centralização, IA local, penetração de mercado) — **conteúdo de referência de mercado/blog especializado, sem exigência regulatória associada** (a própria Skill declara isso; usada só para reforçar o raciocínio de criticidade, nunca como norma).
- Conhecimento técnico geral de engenharia elétrica/automação, aplicado apenas onde a Skill ativa não detalha o ponto (compatibilidade dimmer × driver LED; grau de proteção IP por ambiente de instalação) — sinalizado item a item como tal, nunca apresentado como fonte normativa ratificada.

---

## 1. Dados de partida (caso, conforme recebido)

- Programa: cobertura duplex, Leblon/RJ.
- Automação solicitada pelo cliente (listada por Cardozo, dentro da minha fronteira de "não decido o que automatizar sem instrução"): iluminação, persianas motorizadas (inclusive varanda externa), climatização, som ambiente, controle de acesso (fechadura eletrônica na porta principal).
- Interdisciplinar já fechado por Tenreiro: luminárias de LED com driver dimerizável para a iluminação geral.
- Protocolo de automação (KNX/Zigbee/Z-Wave/Modbus/Wi-Fi): **não definido no Briefing** — a proposta do integrador presume Wi-Fi comum como solução única (item 2).
- Orçamento do cliente para automação: **não informado.** Minha própria atribuição declara que a escolha de protocolo depende do orçamento do cliente — sem esse dado não posso recomendar um protocolo substituto específico, só apontar que a solução proposta (Wi-Fi único, sem malha dedicada) não é adequada para os dispositivos de segurança.
- Potência da central de automação (hub) e lista/potência dos demais equipamentos do circuito de TUG da sala de estar onde ela seria conectada: não informadas.
- Grau de exposição real da varanda (coberta/protegida vs. exposta a chuva direta): não informado.
- Fornecimento da concessionária (mono/bi/trifásico): não informado — não é determinante para nenhum dos 7 itens revisados, mas fica registrado como dado ainda em aberto do Briefing geral.

---

## 2. Revisão item a item da proposta preliminar

### Item 1 — "A central de automação (hub) será conectada em uma tomada comum do circuito de TUG da sala de estar, junto com os demais equipamentos eletrônicos do ambiente — não há necessidade de circuito exclusivo, é um equipamento de baixo consumo."

**Veredito: NÃO CONFORME.**

O erro da proposta é conflar "baixo consumo" com "não crítico". A necessidade de circuito exclusivo não decorre só da magnitude de corrente (esse é o critério de TUE para chuveiro/ar-condicionado/forno) — decorre também do princípio geral de segregação de circuitos da NBR 5410: cada circuito terminal deve ser concebido para que uma falha (sobrecarga, curto, desarme do disjuntor por carga alheia) não afete o restante da instalação. Já apliquei esse mesmo princípio no Exame 2 Caso 1, item 1, para barrar iluminação de 7 ambientes num único circuito.

Aqui o agravante é maior: pelo próprio Briefing deste caso, a central de automação concentra o controle de iluminação, persianas, climatização, som **e controle de acesso/fechadura eletrônica**. A Skill de mercado `automacao-residencial-tendencias` reforça esse ponto ao descrever a tendência de "Centralização: um único sistema controlando luz, fechadura, câmera, climatização e eletrodomésticos" — o hub deixa de ser "mais um eletrônico da sala" e passa a ser o ponto único de controle de segurança da casa. Colocá-lo no mesmo circuito de TUG "junto com os demais equipamentos eletrônicos do ambiente" significa que uma sobrecarga causada por qualquer outro aparelho da sala (TV, som, carregadores) pode desarmar o disjuntor e tirar do ar simultaneamente iluminação, climatização e o sistema de segurança da casa inteira — exatamente o tipo de falha que a segregação de circuitos existe para conter.

**Recomendação:** circuito exclusivo (dedicado) para a central de automação, dimensionado pela potência real do equipamento (não informada — ver pendências).

### Item 2 — "Optamos por integrar todos os dispositivos (incluindo fechadura eletrônica e sensores de alarme) via Wi-Fi doméstico comum do cliente, dispensando rede dedicada — é a solução mais moderna, sem necessidade de cabeamento ou malha própria."

**Veredito: NÃO CONFORME.**

A Skill `nbr5410-eletrica-automacao` lista três famílias de protocolo de automação a serem definidas no Briefing antes de projetar — KNX (barramento dedicado), Zigbee/Z-Wave (malha sem fio própria, residencial) e Modbus (industrial) — justamente porque protocolos dedicados existem para resolver o que o Wi-Fi doméstico comum não resolve bem: rede única compartilhada com todo o tráfego de dados da casa (streaming, trabalho, celulares), sujeita a congestionamento e interferência, sem malha de redundância própria, e com ponto único de falha no roteador do cliente.

Isso é aceitável para dispositivos de conveniência (ex.: um sensor de luminosidade), mas não para os dois dispositivos citados no próprio item — **fechadura eletrônica e sensores de alarme** — que são dispositivos de segurança. Se o roteador Wi-Fi cair (queda de energia sem UPS no roteador, falha de firmware, sobrecarga de rede), a casa perde simultaneamente controle de acesso e detecção de alarme, sem qualquer caminho alternativo. É exatamente por isso que a prática de mercado em automação residencial usa protocolos com malha dedicada e redundância própria (Zigbee/Z-Wave mesh, ou barramento KNX) para os subsistemas de segurança, mesmo quando o restante da automação (cortina decorativa, cena de iluminação) roda por Wi-Fi/app.

**Recomendação:** protocolo dedicado (KNX ou malha Zigbee/Z-Wave, a definir conforme orçamento do cliente — dado não informado, ver pendências) para fechadura e sensores de alarme; Wi-Fi pode seguir sendo usado para funções não críticas de conveniência.

### Item 3 — "Serão instalados dimmers convencionais de resistência (os mesmos já usados em outros projetos da Sttickler) em todos os pontos de luz, incluindo os pontos com luminária LED especificada por Tenreiro."

**Veredito: NÃO CONFORME.**

Isto é uma incompatibilidade técnica direta, não uma questão de preferência. Dimmer convencional de resistência é tecnologia pensada para carga resistiva pura (lâmpada incandescente) — corta parte da senoide para dissipar potência no próprio filamento. Luminária de LED com **driver dimerizável** exige um dimmer compatível com a curva de resposta do driver (tipicamente corte de fase específico para LED — leading/trailing edge —, ou interface própria 0-10V/DALI, ou o módulo de dimerização do próprio protocolo de automação escolhido no item 2). Usar dimmer de resistência convencional sobre driver LED dimerizável tipicamente resulta em cintilação (flicker), ruído audível no driver, faixa de dimerização reduzida ou não funcional, e pode reduzir a vida útil ou danificar o driver.

Este item, além de tecnicamente incorreto, **contraria uma decisão interdisciplinar já fechada** (a especificação de luminária LED com driver dimerizável de Tenreiro) — reforça a necessidade de o integrador revisar a proposta em conjunto com a especificação elétrica/de interiores já definida, não em paralelo a ela.

**Observação de dependência:** a escolha do dimmer correto (dimmer dedicado a LED autônomo vs. módulo de dimerização do protocolo de automação) também depende da resolução do item 2 (protocolo) — mais um motivo para não fechar este item isoladamente.

### Item 4 — "O atuador motorizado da persiana da varanda será o modelo padrão indoor já usado nos ambientes internos, IP20, para manter padronização de fornecedor."

**Veredito: NÃO CONFORME.**

IP20 é grau de proteção para uso interno (protegido apenas contra objetos sólidos maiores que 12,5mm; **nenhuma proteção contra líquidos**). Varanda é, por definição, área externa exposta a intempéries (chuva, umidade, variação de temperatura). Instalar um atuador com grau de proteção interno num ambiente externo expõe o equipamento a infiltração de água, curto-circuito e falha prematura — não é uma questão de padronização de fornecedor, é incompatibilidade de grau de proteção com o ambiente de instalação.

A própria Skill `nbr5410-eletrica-automacao`, na seção de coordenação entre Agentes de Cardozo, já registra esse mesmo princípio para outro caso análogo: *"Glaziou (circuito TUE separado + IP65 para jardim)"* — ou seja, equipamento elétrico em área externa/jardim já exige IP65 nesta casa por prática estabelecida. O mesmo raciocínio (ambiente externo exige grau de proteção compatível com exposição a água) se aplica à persiana da varanda.

**Não decido o grau de IP exato exigido (IP44 vs. IP65)** sem saber o nível de exposição real da varanda (coberta e protegida do vento chuva vs. totalmente aberta) — esse dado não foi informado (ver pendências). Mas o modelo proposto (IP20 indoor) é insuficiente em qualquer cenário de área externa, então o item já é não conforme independentemente dessa definição fina.

### Item 5 — "Por ser um equipamento eletrônico sensível a variações, o circuito dedicado à central de automação (quando houver) deve dispensar o DR de 30mA, para evitar desarmes falsos que interrompam o sistema de segurança da casa."

**Veredito: NÃO CONFORME.**

Este é o mesmo tipo de armadilha já barrada no Exame 2 Caso 1 (item 2: tentativa de dispensar DR por raciocínio de conveniência, não de norma). Lá a proposta tentava dispensar o DR do banheiro alegando que o quadro ficava em ambiente seco; aqui a proposta tenta dispensar o DR do circuito do hub alegando que o equipamento é "sensível" e o desarme seria "falso". Em nenhum dos dois casos a lógica é válida: a proteção DR de 30mA é uma exigência de segurança contra choque elétrico (contato direto/indireto), não um recurso opcional a ser removido por conveniência operacional do equipamento que ele protege.

Se o equipamento realmente sofre desarmes por fuga de corrente inerente ao seu próprio funcionamento (comum em fontes chaveadas de baixa qualidade), a solução tecnicamente correta é **outra**: usar DR de tipo adequado à natureza da fuga (ex.: Tipo A, mais tolerante a correntes residuais com componente contínua, comuns em eletrônica), isolar o equipamento em circuito próprio (o que aliás reforça a correção já apontada no item 1) para não acumular fuga de outros aparelhos no mesmo DR, ou trocar o equipamento por um com fuga de corrente dentro do padrão — nunca remover a proteção.

Agravante adicional: o próprio item reconhece que este circuito, se existir isolado, atenderia justamente o sistema que controla a segurança da casa (fechadura, alarme, conforme item 1) — ou seja, a proposta quer remover proteção contra choque exatamente do circuito mais crítico da automação, com a justificativa invertida de "proteger a segurança do sistema" removendo a proteção de segurança das pessoas.

**Ressalva de escopo:** a Skill ativa `nbr5410-eletrica-automacao` lista DR 30mA como obrigatório explicitamente para banheiro, área de serviço e cozinha — não estende esse texto literalmente a todo circuito de TUG interno seco (como a sala de estar, onde o hub estaria hoje). Não presumo, a partir de conhecimento fora da Skill ratificada, que o texto integral da NBR 5410:2004 exija DR também nesse circuito específico da sala — isso fica como pendência de leitura da norma primária (ver seção 4). Isso não muda o veredito do item: independentemente de o DR ser ou não hoje mandatório nesse circuito específico pela norma, a **justificativa proposta** ("dispensar proteção para evitar desarme falso") é, por si, uma prática não conforme e não deve ser adotada como princípio de projeto — inclusive porque abre precedente perigoso para dispensar DR em outros circuitos por conveniência.

### Item 6 — "A fechadura eletrônica da porta principal terá um nobreak (UPS) dedicado, garantindo abertura mesmo em queda de energia da concessionária."

**Veredito: CONFORME, com observação de integração (não bloqueante para o item em si, mas gera pendência cruzada com os itens 1 e 2).**

Backup de energia dedicado para dispositivo de controle de acesso é prática correta e recomendável — evita que uma queda de energia da concessionária deixe o morador trancado do lado de fora ou impossibilitado de destrancar a porta principal, além de ser relevante para emergências (ex.: necessidade de evacuação). Não há nada na Skill ativa ou em princípio de engenharia que contrarie esse item; é o único dos 7 itens que corresponde a boa prática de proteção sem ressalva sobre o mérito da ideia em si.

**Observação de integração (registrada, não decidida sozinho):** o item garante energia para a fechadura em si, mas o controle de acesso remoto (item 7) depende do protocolo do item 2 — se esse protocolo continuar sendo Wi-Fi doméstico comum, a abertura remota via app também depende do roteador/hub estarem energizados durante a queda de energia. Um nobreak apenas na fechadura garante abertura **local** (ex.: teclado/cartão na própria fechadura), mas não necessariamente abertura **remota**, a menos que o roteador e o hub (item 1) também tenham energia de reserva. Isso não invalida o item 6, mas deixa uma lacuna de especificação a fechar junto com os itens 1 e 2.

### Item 7 — "Configuraremos o sistema com o protocolo já definido no item 2."

**Veredito: NÃO CONFORME — decorrência direta da reprovação do item 2.**

Este item não introduz um problema novo: ele herda integralmente o protocolo do item 2 (Wi-Fi doméstico comum, sem rede dedicada) para o controle de acesso remoto — que é justamente o uso mais crítico de segurança de toda a proposta (abrir/fechar a porta principal remotamente). Como o item 2 foi considerado não conforme por depender de Wi-Fi comum para dispositivos de segurança, o item 7 não pode ser aprovado como está, pois aplica a mesma solução reprovada especificamente ao controle de acesso. Este item só pode ser reavaliado depois que o item 2 for corrigido (protocolo dedicado definido conforme orçamento do cliente).

---

## 3. Resumo da revisão item a item

| Item | Veredito |
|---|---|
| 1 — Hub de automação em circuito comum de TUG da sala, sem circuito exclusivo | Não conforme |
| 2 — Todos os dispositivos (incl. fechadura e sensores de alarme) via Wi-Fi doméstico comum | Não conforme |
| 3 — Dimmer convencional de resistência em ponto com driver LED dimerizável | Não conforme |
| 4 — Atuador de persiana da varanda externa com grau IP20 (indoor) | Não conforme |
| 5 — DR dispensado no circuito do hub para evitar desarme falso | Não conforme |
| 6 — Nobreak dedicado para a fechadura eletrônica | Conforme (com observação de integração) |
| 7 — Controle de acesso remoto usa o protocolo do item 2 | Não conforme (decorrência do item 2) |

---

## 4. Pendências bloqueantes (dado não informado ou impreciso — não presumido por Landell)

1. **Orçamento do cliente para automação — não informado.** Minha função declara que a escolha de protocolo (KNX/Z-Wave/Zigbee/Wi-Fi nativo) é feita "conforme orçamento do cliente". Sem esse dado, aponto que Wi-Fi comum isolado não é adequado para fechadura/alarme (item 2), mas não posso recomendar qual protocolo dedicado específico adotar. **A cobrar de:** Cardozo (deve constar no Briefing).
2. **Potência da central de automação (hub) e lista/potência dos demais equipamentos do circuito de TUG da sala de estar — não informadas.** Necessário para dimensionar o circuito exclusivo recomendado no item 1 (IB/In/Iz) e para confirmar se o circuito atual, mesmo sem o hub, já se aproxima do limite de 1.500W de TUG. **A cobrar de:** integrador terceirizado / Cardozo.
3. **Grau de exposição real da varanda (coberta e protegida vs. totalmente aberta) — não informado.** Determina se IP44 é suficiente ou se é necessário IP65 para o atuador da persiana externa. O veredito do item 4 (IP20 é insuficiente) não depende dessa definição, mas a especificação final do modelo correto, sim. **A cobrar de:** Cardozo / projeto de arquitetura (Lúcio, quanto ao desenho da varanda) e Tenreiro (interiores/fechamento do ambiente).
4. **Autonomia e escopo real do nobreak da fechadura (item 6) — não informados.** Não está claro se o nobreak cobre só a fechadura (abertura local) ou também o roteador/hub necessário para abertura remota (item 7, que depende do protocolo do item 2). **A cobrar de:** integrador terceirizado.
5. **Texto integral da NBR 5410:2004 sobre exigência de DR em circuitos de TUG internos secos (fora de banheiro/área de serviço/cozinha) — não lido por Landell.** A Skill ativa não estende explicitamente a exigência de DR ao circuito de TUG da sala de estar. Isso não muda o veredito do item 5 (a justificativa proposta é inválida de qualquer forma), mas fica como lacuna de leitura de norma primária a fechar antes de qualquer memorial de cálculo definitivo. **A cobrar de:** Cardozo (avaliar leitura de fonte primária ABNT, mesmo tratamento já dado a outras lacunas de norma nos casos anteriores).

---

## 5. Conclusão

**A proposta preliminar NÃO pode avançar como está.** Dos 7 itens revisados, 6 são não conformes (itens 1, 2, 3, 4, 5 e 7 — este último por decorrência direta do item 2) e apenas 1 (item 6) é conforme, ainda que com uma observação de integração a resolver junto aos itens 1 e 2. Diferente dos dois casos anteriores do Exame 2, aqui a maior parte das reprovações não vem de uma única norma isolada, mas da integração malfeita entre elétrica e automação — exatamente a "outra metade do escopo" que este caso 3 foi desenhado para testar.

**Correções bloqueantes (impedem virar memorial definitivo):**
- Isolar a central de automação em circuito exclusivo, dimensionado pela potência real do equipamento — item 1.
- Definir protocolo dedicado (KNX ou malha Zigbee/Z-Wave, conforme orçamento do cliente) para fechadura eletrônica e sensores de alarme, em vez de depender só do Wi-Fi doméstico comum — item 2 / pendência 1.
- Substituir os dimmers convencionais de resistência por dimmers/módulos compatíveis com driver LED dimerizável nos pontos especificados por Tenreiro — item 3.
- Substituir o atuador da persiana da varanda por modelo com grau de proteção adequado a área externa (mínimo IP44, possivelmente IP65 — a confirmar pela exposição real) — item 4 / pendência 3.
- Remover a dispensa de DR do circuito do hub; resolver eventual desarme falso por DR adequado (Tipo A) ou isolamento de circuito, nunca por remoção de proteção — item 5.
- Reavaliar o item 7 assim que o protocolo do item 2 for corrigido — item 7.
- Esclarecer se o nobreak da fechadura cobre também o caminho de acesso remoto (roteador/hub) — item 6 / pendência 4.

**Não bloqueante:** item 6 pode seguir como está quanto ao mérito (nobreak dedicado para a fechadura é boa prática), sujeito apenas ao esclarecimento de escopo registrado na pendência 4.

Nenhum item foi decidido por presunção de dado não fornecido — as pendências 1 a 5 ficam explicitamente registradas para cobrança de Cardozo/integrador/demais Agentes antes de este caso (ou um real equivalente) virar memorial definitivo.
