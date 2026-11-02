# Correções do Landell (Elétrica e Automação) para o Briefing Único v2, 31/10/2026

- **Pedido:** Claudemberg, via Cardozo, depois da revisão final de 31/10 (`briefing_revisao_final_8_agentes_31-10.md`, ALTOS 3 e 14, D3 e seção "Decisões de Claudemberg").
- **Arquivo corrigido:** `briefing_modelo_v2_proposta.md`. **Não editei o Briefing.** Quem junta é o Oscar.
- **Fonte técnica:** Skill `entrada-energia-light-ligacao-nova-padrao-recon-bt-rj` v1.1 (FAQ oficial da Light e vídeo oficial da Light) e Skill `nbr5410-eletrica-automacao`.
- **Códigos novos:** TI-ELE-01, TI-ELE-02 (seguem o padrão TI-PAI-xx do Glaziou) e C-13. Nenhum deles existe hoje no Briefing. **Se outro agente também propuser um C-13, o Oscar renumera o meu.** O conteúdo não muda.

---

## Correção 1: ALTO 14, dados de energia da Light (tarefa interna nova)

**Código:** TI-ELE-01 (Parte B, depois da TI-13; vale também se a linha entrar em tabela própria de Elétrica, como a do Paisagismo).

**Texto atual:** não existe. A revisão diz (ALTO 14): "falta uma tarefa interna com os dados de energia da Light (tensão e tipo de ligação)".

**Texto novo, pronto para colar.** Proponho uma tabela própria, como a do Paisagismo:

> **Tarefas internas de Elétrica (Landell, decisão de Claudemberg em 31/10; só quando ESC-01 contém Elétrico, e portanto também com Automação, C-13). Respondidas pelo Landell logo depois da visita ao local, feita por Claudemberg ou por um estagiário.**
>
> | Cód. | O que a equipe levanta | Dono | Etapa |
> |---|---|---|---|
> | TI-ELE-01 | **Energia da Light no terreno.** O Landell responde: (a) se a rede da Light na frente do lote é aérea (poste e fios) ou subterrânea; (b) a tensão disponível (em geral 220/127 V; a Light confirma); (c) a distância do poste da Light até o muro, para saber se o ramal passa de 30 m; (d) se o terreno já tem padrão de entrada (relógio) e qual; (e) o tipo de ligação (monofásica, bifásica ou trifásica). **O tipo de ligação não se descobre na visita:** o Landell define pela carga calculada na TI-03 e confirma com a Light (consulta de viabilidade) antes de fechar o padrão. **Quem visita registra:** 1) foto da rua mostrando o poste da Light mais próximo e os fios chegando nele, ou a falta de poste (sinal de rede subterrânea); 2) se esse poste fica na mesma calçada do terreno ou do outro lado da rua; 3) a distância aproximada, a passos, do poste até o muro; 4) se houver relógio de luz no terreno: foto do relógio, da caixa e da plaqueta do medidor; 5) foto do número da casa (ou anotar que não há número visível); 6) se houver casa antiga, uma conta de luz recente, pedida ao dono. **Quem visita pergunta ao cliente:** "O terreno já tem ligação de luz? Tem uma conta de luz recente para nos mandar?" | Landell, com fotos e respostas de quem visitou | Levantamento, antes do EP |

**Motivo:** o ALTO 14 apontou a falta. A decisão de Claudemberg transforma isso em tarefa interna respondida depois da visita. Sem esses dados não dá para escolher o padrão de entrada (FAQ Light: mono até 8 kVA, bi até 13 kVA, tri de 13 a 76 kVA de carga demandada). Também não dá para saber se a ligação precisa de estudo da Light (acima de 24 kVA ou com ramal acima de 30 m), nem se a rede é subterrânea, o que muda padrão e prazo. Corrigi o pedido num ponto, para não inventar: em casa nova o **tipo de ligação não é dado de campo**. Ele sai do meu cálculo de carga e é confirmado pela Light. Por isso a tarefa separa o que quem visita registra do que eu defino. O prazo de ligação nova e a posição do poste do padrão no muro (que o Oscar precisa reservar) dependem dessa resposta.

---

## Correção 2: ALTO 14, o que a casa precisa manter quando falta luz (tarefa interna nova)

**Código:** TI-ELE-02 (na mesma tabela da Correção 1).

**Texto atual:** não existe. A revisão diz (ALTO 14): "falta perguntar o que a casa precisa manter quando falta luz (aparelho médico, home office, gerador)".

**Texto novo, pronto para colar:**

> | TI-ELE-02 | **O que não pode parar quando falta luz.** O Landell decide se a casa precisa de circuito separado para emergência, nobreak, gerador ou bateria, e quanto tempo cada item precisa ficar ligado. A proposta vai ao cliente no EP (C-5). **Quem visita pergunta pessoalmente ao morador** (só ele sabe), sem anotar nome nem doença: 1) "Alguém na casa usa aparelho que não pode desligar quando falta luz, por exemplo um aparelho médico ou uma geladeira de remédio? Se sim: qual aparelho, e por quantas horas ele precisa funcionar sem luz?"; 2) "Alguém trabalha em casa e não pode ficar sem internet e computador quando falta luz? Por quanto tempo?"; 3) "O que mais vocês querem que funcione sem luz?" (opções para mostrar: geladeira e freezer · portão da garagem · fechadura, alarme e câmeras · bomba d'água · aquário · nada); 4) "Vocês aceitam um gerador a combustível, que faz barulho e precisa de manutenção, ou preferem bateria ou nobreak, mesmo que durem menos?"; 5) "Vocês sabem se falta luz com frequência nessa região?" **Quem visita registra:** as respostas; e, se houver vizinho ou porteiro por perto, o que ele diz sobre a frequência de falta de luz na rua. | Landell, com as respostas de quem visitou | Levantamento, antes do EP |

E uma linha na C-2 (Disparos), para não esquecer a pergunta na visita:

> | MOR-02 com "outra necessidade especial" ou MOR-03 "alguém trabalhar em casa", com Elétrico contratado | Na visita, as perguntas 1 e 2 da TI-ELE-02 são obrigatórias, não opcionais | obrigatória |

**Motivo:** essa é a decisão de Claudemberg para o ALTO 14. Aparelho médico, home office, portão e fechadura definem se há circuito de emergência e de que tamanho, e isso muda o quadro de distribuição e a carga da TI-03. O cliente não sabe responder "nobreak ou gerador" num formulário. Ele sabe dizer o que não pode parar e por quanto tempo, e a escolha técnica fica comigo. A pergunta 4 existe porque gerador tem barulho e combustível, e isso é escolha do morador. O SUS-01 ("gerar energia com o sol") não cobre o assunto: sistema solar ligado à rede e sem bateria, em geral, desliga junto quando falta luz. Uso as duas respostas juntas.

**Aviso para o Kelsen (não decido sozinho):** a pergunta 1 é dado de saúde (LGPD Art. 11), a mesma natureza da MOR-02 (K2). Por isso o texto pergunta pelo **aparelho** e pelas **horas**, nunca pela pessoa ou pela doença. Mesmo assim, peço ao Kelsen que confirme se o consentimento destacado que ele vai criar antes da MOR-02 precisa dizer que a visita ao local também pode perguntar isso. Se precisar, a frase entra no consentimento, não aqui.

---

## Correção 3: TI-03 passa a usar as tarefas novas e as outras cargas grandes (achado MÉDIO)

**Código:** TI-03 (Parte B).

**Texto atual:** "| TI-03 | Nível de uso elétrico, carga e ampliação futura de carga | Elétrico (2) | Landell, a partir de CLI-01, COZ-01, HID-03, ELE-01 | EP |"

**Texto novo, pronto para colar:**

> | TI-03 | Nível de uso elétrico, carga e ampliação futura de carga (só quando ESC-01 contém Elétrico) | Elétrico (2) | Landell, a partir de CLI-01, COZ-01, HID-03, ELE-01, SUS-01 (energia e água quente pelo sol), ESC-02 (piscina, banheira ou hidromassagem, irrigação), GOU-01, SEG-01, PAI-06, TI-ELE-01 e TI-ELE-02 | EP |

**Motivo:** a lista atual deixa de fora cargas que eu preciso somar. A piscina tem bomba e pode ter aquecimento. A hidromassagem tem motor. A irrigação tem bomba. O portão de SEG-01 tem motor. O PAI-06 traz o circuito externo. O SUS-01 entra porque a geração solar fica limitada à potência disponibilizada pela Light (Skill da entrada Light, seção 2), e a entrada precisa nascer dimensionada para isso. Sem a condição "só com Elétrico", a TI-03 fica sem dono quando a elétrica não é contratada, o mesmo problema do ALTO 2.

---

## Correção 4: D3, Automação leva o Elétrico junto (regra de contratação)

**Código:** C-13 (Parte C, regra nova) e ESC-01 (Seção 0, opção "Automação").

**4a. ESC-01, texto atual da opção:** "CX (vem marcado do Pré-Briefing; o cliente confere): Arquitetura · Interiores · Estrutural · Elétrico · Hidrossanitário · Automação · Paisagismo"

**Texto novo, pronto para colar:**

> CX (vem marcado do Pré-Briefing; o cliente confere): Arquitetura · Interiores · Estrutural · Elétrico · Hidrossanitário · Automação (inclui o Elétrico, C-13) · Paisagismo

**4b. C-13, texto atual:** não existe.

**Texto novo, pronto para colar:**

> **C-13. Automação leva o Elétrico junto (decisão de Claudemberg em 31/10/2026, D3).** Não existe contratação só de Automação. Quando o ESC-01 tem Automação, o Elétrico conta como contratado também: a equipe Comercial já registra os dois no Pré-Briefing (C-9) e, se só a Automação vier marcada, o Elétrico é marcado junto. Para o Briefing, valem as regras de "ESC-01 contém Elétrico" (TI-03, TI-ELE-01, TI-ELE-02, HID-03, ILU-01, ELE-01). A ELE-02 continua sem aparecer, porque a automação já pergunta isso. Elétrica e automação são feitas juntas, pelo Landell (C-5).
>
> **Texto ao cliente** (no Pré-Briefing e ao lado da opção Automação):
> "A automação usa os fios, os quadros e as tomadas do projeto elétrico: a luz que acende pelo celular precisa de um circuito pensado para isso desde o começo. Por isso, quem contrata a Automação recebe também o projeto Elétrico, feito pela mesma pessoa. Assim, um projeto não briga com o outro."

**Motivo:** essa é a decisão de Claudemberg (D3), que eu tinha sugerido na revisão. A razão técnica é que a automação depende da infraestrutura elétrica: circuitos, quadro, caixas e tubulação. Sem o Elétrico do mesmo projetista, a automação ficaria sobre uma elétrica que ninguém dimensionou para ela. A condição da ELE-02 ("Elétrico E não Automação") já funciona com essa regra, não muda. Quem decide como a regra entra no contrato é a equipe Comercial. Aqui só fica escrito o que o Briefing faz.

---

## Correção 5: ALTO 3, HID-03 também aparece com Elétrico sem Hidrossanitário

**Código:** HID-03 (Seção 6), coluna "Condição".

**Texto atual:** "ESC-01 contém Hidrossanitário **E** HID-01 = "Água Fria e Água Quente" **E** TI-13 confirmou que as duas opções são possíveis"

**Texto novo, pronto para colar:**

> ESC-01 contém Hidrossanitário **OU** Elétrico (e, portanto, também com Automação, C-13) **E** HID-01 = "Água Fria e Água Quente" **E** TI-13 confirmou que as duas opções são possíveis. Se a TI-13 disser que gás não é possível, a pergunta não aparece e fica registrado "elétrico" para a TI-03. Se o Hidrossanitário não foi contratado e o cliente marcar "tanto faz", o Landell dimensiona a carga como aquecimento elétrico (o caso de maior carga) e escreve isso no memorial. A TI-13, sem Saturnino contratado, fica com o Oscar no Levantamento (ALTO 2).

**Motivo:** essa é a decisão do ALTO 3. Aquecedor ou chuveiro elétrico costuma ser a maior carga da casa e define o circuito exclusivo, o disjuntor e a faixa do padrão Light. Hoje, quem contrata Elétrico sem Hidrossanitário nunca responde isso. Os dois complementos fecham buracos da nova condição: (1) com gás impossível, a resposta já é conhecida e não se pergunta; (2) com "tanto faz" e sem Saturnino para recomendar, eu fico com o caso de maior carga, para a entrada não sair pequena. A TI-13 depende da solução do ALTO 2. Se o Oscar resolver o ALTO 2 de outro jeito, esta frase acompanha a solução dele.

---

## Correção 6: o Gate confere as tarefas de Elétrica (achado MÉDIO)

**Código:** C-3.

**Texto atual:** "depois de conferir C-1 completa, cada C disparado listado e TI-01, TI-05, TI-09 anexadas."

**Texto novo, pronto para colar:**

> depois de conferir C-1 completa, cada C disparado listado e TI-01, TI-05, TI-09 anexadas; com Elétrico contratado (C-13), também TI-ELE-01 e TI-ELE-02 anexadas.

**Motivo:** Claudemberg mandou responder as duas tarefas logo depois da visita, antes do EP. Se o Gate não confere, nada garante que estejam prontas, e a TI-03 (carga, no EP) depende delas. É o mesmo tipo de falha do ALTO 1: regra que existe, mas que o Gate não confere.

---

## Correção 7: TI-10 sem dono quando o Elétrico não é contratado (achado MÉDIO)

**Código:** TI-10 (Parte B).

**Texto atual:** "| TI-10 | Tipo de luminária (embutida, aparente, trilho, spot) | Elétrico (2) | Landell + Tenreiro propõem; cliente aprova no EP/AP | EP/AP |"

**Texto novo, pronto para colar:**

> | TI-10 | Tipo de luminária (embutida, aparente, trilho, spot) | Elétrico (2) | Landell e Tenreiro propõem, cada um só se a sua disciplina estiver no ESC-01; sem nenhum dos dois, vira nota para quem fizer a elétrica; cliente aprova no EP/AP | EP/AP |

**Motivo:** é o mesmo problema do ALTO 2. A tarefa aponta dono sem conferir se ele foi contratado. A ILU-01 já usa "Elétrico ou Interiores", e a TI-10 passa a seguir a mesma lógica.

---

## Correção 8: ELE-01, opção "outro" sem campo e duas cargas grandes faltando (achado BAIXO)

**Código:** ELE-01 (Seção 6), coluna "Tipo / opções".

**Texto atual:** "CX: forno elétrico · aquecedor de ambiente · carregador de carro elétrico · outro · nenhum"

**Texto novo, pronto para colar:**

> CX: forno elétrico · aquecedor de ambiente · carregador de carro elétrico · sauna · secadora de roupa · outro (qual?) · nenhum

**Motivo:** "outro" sem campo de texto não diz que aparelho é, e sem saber o aparelho eu não acho a potência. Sauna elétrica e secadora são cargas grandes de uso comum que o leigo não pensa em citar. Cada uma pede circuito próprio. Tempo: continua cerca de 1 min.

---

## O que mexe nos números (para o Oscar atualizar)

- **Tarefas internas:** 19 → **21** (mais TI-ELE-01 e TI-ELE-02), se ninguém mais acrescentar tarefas.
- **Perguntas ao cliente:** não mudam. A TI-ELE-02 é feita na visita, não no formulário. A HID-03 já estava contada no máximo dos complementares (12,5 min).
- **Regras:** mais C-13 e uma linha na C-2.

## O que não fiz

- Não toquei no Briefing, no Ensaio 003 nem no Drive. Não fiz commit.
- A redação do consentimento LGPD para a pergunta de aparelho médico é do Kelsen (Correção 2).
- A RECON-BT 2024 da Light continua não lida (ressalva R1 da Skill da entrada Light). Por isso a TI-ELE-01 manda confirmar com a Light, e não com uma tabela minha.
