# Correções do Baumgart (Estrutural) para o Briefing Único v2 (31/10/2026)

- **Quem escreveu:** Baumgart (Estrutural, equipe do Cardozo). Estou como "Autonomous provisório": **esta proposta passa pela auditoria do Cardozo antes de o Oscar usar.**
- **Origem:** relatório `briefing_revisao_final_8_agentes_31-10.md`, ALTO 13 e "Decisões de Claudemberg (31/10/2026)", linha "Estrutural". Mais o item "Usado por" da lista de MÉDIOS e BAIXOS.
- **Arquivo corrigido:** `briefing_modelo_v2_proposta.md`. **Não editei o Briefing.** O Oscar junta tudo.
- **Não toquei** no Ensaio 003 nem no Drive. Não fiz commit.

## Escolha dos códigos (ler antes de colar)

- **Pergunta nova: `TER-01`** (Terreno e estrutura). Não usei `EST-06`. No Briefing, "EST" quer dizer Aparência (EST-01 a EST-05, Seção 4). Uma pergunta de estrutura com esse prefixo ficaria na seção errada e confundiria. Se o Oscar preferir `EST-06`, é só trocar o código: o conteúdo não muda.
- **Tarefas internas novas: `TI-EST-01` e `TI-EST-02`**, no mesmo padrão das `TI-PAI-xx` do Glaziou. Hoje, outros agentes (Landell, Saturnino, Kelsen) também estão criando tarefas internas. Se todos usassem `TI-14`, `TI-15`..., os códigos poderiam se repetir. Com um prefixo por disciplina, isso não acontece. Conferi: nenhum `TI-14`, `TER-` ou `C-13` existe hoje na pasta do Oscar.
- **Regra nova: `C-13`** (disparos estruturais). Hoje o Briefing vai até a C-12.

---

## Correção 1 — Sondagem: preliminar no Levantamento + complemento depois do EP

### 1a. Linha TI-01 (Parte B)

**Texto atual:**
> | TI-01 | Situação do terreno, topografia, sondagem | Estrutural (3) | Oscar (Levantamento); leitura da sondagem por Baumgart | Levantamento |

**Texto novo (colar):**
> | TI-01 | Situação do terreno e topografia (desnível, cotas, sinais de aterro) + **sondagem preliminar**: sondagem SPT (NBR 6484:2020) com **poucos furos**, só para saber cedo se o solo é mole e onde está a água do terreno (nível d'água, com data da medição). **Mínimo de 2 furos**, na área onde a casa provavelmente vai ficar. Se o terreno tiver desnível, um furo fica na parte mais baixa. **O Baumgart define quantos furos, onde e até que profundidade antes de a sondagem ser contratada.** Na Barra, no Recreio e em Jacarepaguá, os furos descem até a camada firme, e não só até onde a norma deixa parar. Os furos ficam marcados na planta do lote, para servirem depois como parte do total. Sondagem antiga ou feita antes de uma obra vizinha que mexeu com a água do terreno não vale: o Baumgart diz se ela serve | Estrutural (3) | Oscar (Levantamento: topografia e contratação, via Cardozo); quantidade, posição e profundidade dos furos e leitura do laudo: Baumgart | Levantamento |

**Motivo:**
- Claudemberg decidiu assim em 31/10: preliminar no Levantamento e complemento depois do EP.
- A NBR 8036 conta os furos pela **área de projeção da casa**, e não pela área do lote. Essa área só existe depois do EP. Antes dele, ninguém sabe quantos furos a norma pede. **Acredito** que a regra seja: 1 furo a cada 200 m² de projeção, mínimo de 2 até 200 m² e mínimo de 3 entre 200 e 400 m². Esses números vêm de fonte secundária (Skills `nbr6122-2019-fundacoes` e `fundacoes-solos-moles-lencol-freatico-barra-recreio`, R7). Preciso conferir no texto da NBR 8036 antes de citar em memorial.
- Os 2 furos do Levantamento já respondem às perguntas que mudam o partido: o solo é mole? A água está alta? Dá para ter subsolo e piscina enterrada sem bombear água? (Skill `rebaixamento-lencol-freatico-...`, §4.1: essa decisão é tomada **no EP**, não no executivo.)
- A profundidade dos furos é decidida pelo contratante, e não deixada para o critério de parada da NBR 6484:2020 (Skill Barra/Recreio, §2).
- Sondagem antiga ou anterior a uma obra vizinha que rebaixou a água: esse erro já caiu num exame meu (Alto da Boa Vista, 12/09/2026).

### 1b. Tarefa nova TI-EST-01 (Parte B, logo abaixo da TI-13)

**Texto atual:** não existe.

**Texto novo (colar como linha nova da tabela da Parte B):**
> | TI-EST-01 | **Complemento da sondagem**, se faltar ponto. Com o EP aprovado, o Baumgart compara os furos da TI-01 com a área de projeção da casa: (1) a quantidade de furos é a que a NBR 8036 pede para essa área? (2) os furos estão dentro da casa ou perto dela? (3) eles descem o bastante para o subsolo, a piscina enterrada e a estaca prevista? Se tudo estiver atendido, a TI-01 basta, e o Baumgart registra isso por escrito. Se faltar alguma coisa, ele especifica os furos que faltam. Na Barra, no Recreio e em Jacarepaguá, a recomendação é 1 furo a cada 100 a 150 m² de projeção, acima do mínimo da norma | parecer Baumgart 31/10 (ALTO 13) | Baumgart especifica; contratação via Cardozo (custo informado ao cliente antes) | depois da aprovação do EP, antes do AP |

**Motivo:**
- É a 2ª metade da decisão de Claudemberg.
- A NBR 6122:2019 (com a Emenda 1/2022) não aceita projeto de fundação sem sondagem. A NBR 8036 diz quantos furos são precisos para a área da casa. Não há como saber isso antes do EP.
- A densificação de 1 furo a cada 100 a 150 m² é recomendação da Skill Barra/Recreio, e não exigência da norma. Por isso aparece como "recomendação".

---

## Correção 2 — Pergunta ao cliente: TER-01 (uma pergunta só, em grade)

Escolhi **uma pergunta só, em grade**: cada linha tem resposta "sim / não / ainda não sei". Foi o formato com menos perguntas que não perde informação. Uma lista de "marque o que quiser" (CX) não registra o "ainda não sei", e para mim o "ainda não sei" muda o trabalho (ver a regra C-13). O Forms saiu (decisão K1). Por isso, esconder linhas conforme outra resposta não é mais problema.

**Onde entra:** na Seção 2 (Cômodos e organização da casa), logo depois da SOC-02. É lá que a conversa já trata de "sala embaixo ou em cima". Se o Oscar achar melhor, pode ficar junto do novo "tipo de casa (térrea, sobrado...)" que a Arquitetura vai pôr no início. A linha 6 conversa com esse dado.

**Texto atual:** não existe.

**Texto novo (colar como linha nova da tabela da Seção 2):**
> | TER-01 | Algumas escolhas mudam muito a estrutura e o custo da casa, por isso perguntamos já. Para cada linha, responda sim, não ou ainda não sei. | GR (sim / não / ainda não sei em cada linha): (1) **Garagem ou cômodo abaixo do nível da rua** (subsolo, "andar enterrado"); (2) **Uma parte grande da casa "no ar", sem pilar embaixo** (ex.: varanda grande ou quarto que avança para fora, cobertura grande sobre a garagem sem colunas); (3) **A casa encostada no muro do vizinho**, sem espaço livre entre as duas; (4) **Se o terreno tiver ladeira ou desnível: aproveitar o desnível** (ex.: garagem na parte baixa, casa em meios-níveis), em vez de deixar tudo plano; (5) **Piscina: em cima da casa ou da garagem** (na cobertura ou sobre uma laje) → sim / não, no chão / ainda não sei (esta linha só aparece se o ESC-02 tiver Piscina); (6) **Aumentar a casa no futuro, com mais um andar em cima** | sempre | Oscar, Baumgart, Saturnino | R |

**Tempo:** 2 min na reunião, já com a explicação. A reunião passa de 43 para 45 min de perguntas, sem contar as mudanças dos outros agentes.

**Obrigatória (colar na C-1, depois de "SOC-02,"):** `TER-01,`. Motivo: sem ela não consigo dar a classe de consequência da estrutura (Correção 3). Ninguém fica travado, porque "ainda não sei" é uma resposta aceita.

**Impacto nos números (para o Oscar recalcular junto com as outras correções):** +1 pergunta em todos os pacotes (37→38, 46→47, 52→53, antes das outras mudanças); +1 código ativo (53→54); +2 tarefas internas (TI-EST-01 e TI-EST-02).

**Motivo, linha por linha (como cada resposta dispara o meu trabalho; os detalhes estão na C-13):**
1. **Subsolo:** pela Skill `nbr6118-estrutural-concreto`, é gatilho de **CC3**, e na CC3 a revisão independente (ATP) é obrigatória. Também cava abaixo da água na Barra e no Recreio (outorga do INEA e risco ao vizinho, Skill `rebaixamento-lencol-freatico-...`). O subsolo também pede contenção e cálculo do empuxo da água sobre a laje.
2. **Balanço grande:** marquise ou balanço é gatilho de CC3 (mesma Skill). A Emenda 1 da NBR 6118:2026 exige **armadura inferior de segurança** em balanço e marquise. Num terraço sobre balanço, a vibração do piso também precisa ser verificada (3 Hz).
3. **Encostada no vizinho:** fundação junto da divisa (sapata de divisa com viga de equilíbrio, ou estaca), sem mexer no terreno do vizinho. Pede vistoria cautelar da casa ao lado antes da obra. **Acredito** que seja boa prática, e não exigência escrita numa norma que eu tenha lido. Se o lote for de solo mole, há risco de recalque no vizinho. Se encostar é permitido pela lei é com o Kelsen, via Lúcio.
4. **Declive:** muro de arrimo e contenção, fundação em cotas diferentes e furo de sondagem na parte baixa (TI-01). O cliente responde o desejo dele. O desnível em si quem mede é a topografia (TI-01).
5. **Piscina em cima:** é a maior carga de uma casa. A água tem cerca de 10 kN/m³: uma lâmina de 1,40 m pesa por volta de 14 kN/m² só de água (conta minha, de ordem de grandeza). Isso pede laje e vigas próprias, impermeabilização (NBR 9575) e muda o caminho da carga até a fundação. **Piscina no chão** na Barra e no Recreio: verificar se ela flutua quando estiver vazia e se fica abaixo da água do terreno (Skill de rebaixamento, checklist).
6. **Mais um andar no futuro:** a fundação e os pilares precisam ser calculados **hoje** já com a carga do andar extra. Depois não há reforço barato. Esse dado se perdeu dos formulários antigos (ALTO 13).

---

## Correção 3 — Tarefa interna da CAA e da classe de consequência: TI-EST-02

**Texto atual:** não existe. No Briefing, nenhuma tarefa trata da classe de agressividade nem da classe de consequência.

**Texto novo (colar como linha nova da tabela da Parte B, logo abaixo da TI-EST-01):**
> | TI-EST-02 | **Classe de agressividade (CAA) e classe de consequência (CC) da estrutura.** **(a) CAA, no Levantamento:** o Baumgart propõe a classe com base no lugar: distância do mar, da baía ou da lagoa, se a região é urbana ou de praia, e água e solo agressivos (sal, sulfato), tirados da sondagem da TI-01. Escreve por que escolheu a classe. O Cardozo valida, e o cliente, que é o contratante, confirma por escrito junto com a aprovação do EP. Sem a CAA confirmada, não se define a resistência do concreto (fck) nem o cobrimento das armaduras, e o AP estrutural não começa. **(b) CC, primeiro na leitura do Briefing (TER-01) e depois confirmada no EP:** CC1, CC2 ou CC3, pelos gatilhos: subsolo, marquise ou balanço, laje protendida, mais de 5 pavimentos, reforma que tira pilar. Na dúvida entre duas classes, fica a mais exigente. Se der CC3, a revisão independente (ATP) é obrigatória, com custo e prazo próprios: o Baumgart avisa o Cardozo antes do fim do EP, para o cliente saber. Se der CC2, para e confirma com o Cardozo se a ATP é exigida (divergência aberta na Skill). **(c) Norma:** NBR 6118:2026 (Emenda 1). A janela para usar a edição de 2023 fechou em cerca de 07/09/2026 | parecer Baumgart 31/10 (ALTO 13) | Baumgart propõe; Cardozo valida; cliente confirma a CAA | (a) Levantamento; (b) leitura do Briefing → EP |

**Motivo:**
- Isso é o que vem antes de qualquer cálculo de concreto. Pela Skill `nbr6118-estrutural-concreto` (Emenda 1 da NBR 6118:2026), **a CAA é fornecida pelo contratante, e não decidida pelo projetista**. **Acredito** que a CAA continue na Tabela 6.1 da NBR 6118, mas não li a edição 2026.
- **Interpretação a confirmar no Gate:** o cliente é leigo e não sabe classificar a agressividade. Por isso, proponho que o Baumgart escreva a proposta com justificativa e o cliente confirme. **Acredito** que isso cumpre a intenção da norma, mas não li o texto oficial. É uma decisão do Cardozo e de Claudemberg.
- Na Skill, a classe de consequência é "a primeira pergunta de todo projeto", e ela decide se a ATP é exigida. Os valores e gatilhos da Skill vêm de fonte secundária (blogs técnicos). Antes do dimensionamento definitivo, eles precisam ser conferidos no texto da ABNT.
- A CC depende das respostas da TER-01 e do volume do EP. Por isso tem duas etapas.

---

## Correção 4 — "Usado por": incluir o Baumgart

### 4a. ESC-02

**Texto atual (coluna "Usado por"):**
> | Oscar, Saturnino, Landell, Glaziou |

**Texto novo:**
> | Oscar, Saturnino, Landell, Glaziou, Baumgart |

**Motivo:** três opções da ESC-02 mudam a estrutura:
- **Piscina:** carga muito grande, ou escavação abaixo da água do terreno (TER-01, linha 5).
- **Banheira ou hidromassagem:** carga concentrada na laje quando está cheia. Uso a carga da NBR 6120:2019, com o peso real do modelo escolhido.
- **Adega:** se ficar enterrada, é escavação.

Faz sentido incluir. Conferir: a mesma célula aparece uma vez só, na linha da ESC-02.

### 4b. EST-02

**Texto atual (coluna "Usado por"):**
> | Oscar, Tenreiro, Glaziou |

**Texto novo:**
> | Oscar, Tenreiro, Glaziou, Baumgart |

**Motivo:**
- A opção "Concreto aparente" da EST-02 muda a minha especificação: concreto aparente, sobretudo do lado de fora, pede cuidado maior de durabilidade (cobrimento, fck, cura e fôrma), e isso é ligado à CAA (TI-EST-02). Junto com a EST-05 "estrutura à mostra", define se o pilar e a viga ficam aparentes.
- "Metal" também aparece como opção de material. Se for estrutura metálica aparente, entra outra norma de cálculo, que não é a NBR 6118. Faz sentido incluir.

---

## Correção 5 — Regra nova C-13: disparos estruturais

**Texto atual:** não existe. A última linha da C-2 trata só do partido de arquitetura:
> | Levantamento (TI-01, TI-09): frente até ~10 m ou vizinhos encostados / 3+ pavimentos / declive / luz em dois lados | C1 / C2 / C6 / C7 | conforme a Skill |

**Texto novo (colar depois da C-12):**

> **C-13. Disparos estruturais (Baumgart).** "Ainda não sei" numa linha da TER-01: o Baumgart trata como "sim" no cálculo preliminar (lado seguro), e o Oscar pergunta de novo na apresentação do EP.
>
> | Resposta | Dispara | Força |
> |---|---|---|
> | TER-01 (1) subsolo = sim, ou ROT-01/PRG-01 levando o partido a ter garagem enterrada | CC3 provável (TI-EST-02) e ATP; teste "preciso cavar abaixo da água?" já no EP, comparando com garagem no térreo ou em pilotis (Skill de rebaixamento, §4.1); contenção e empuxo da água na laje; Saturnino avisado (drenagem e bomba) | obrigatória |
> | TER-01 (2) balanço grande = sim | CC3 provável (TI-EST-02); armadura inferior de segurança (NBR 6118:2026, Emenda 1); se for piso de uso, verificar vibração (3 Hz) | obrigatória |
> | TER-01 (3) encostada no vizinho = sim, ou TI-01/TI-09 mostrando construção do vizinho na divisa | fundação de divisa sem invadir o terreno ao lado; vistoria cautelar da casa vizinha antes da obra; se o solo for mole, cuidado com recalque no vizinho; se encostar é permitido pela lei: Lúcio → Kelsen | obrigatória |
> | TER-01 (4) aproveitar desnível = sim, ou TI-01 com desnível | arrimo e contenção; fundação em cotas diferentes; furo de sondagem na parte baixa (TI-01) | padrão |
> | TER-01 (5) piscina em cima = sim | laje e vigas próprias para a carga da água, impermeabilização (NBR 9575) junto com Saturnino; a carga entra na CC e na fundação | obrigatória |
> | TER-01 (5) piscina no chão | na Barra, no Recreio e em Jacarepaguá: verificar flutuação com a piscina vazia e a cota da água do terreno (TI-01) | padrão |
> | TER-01 (6) mais um andar = sim | fundação e pilares calculados já com o andar a mais; a carga fica escrita no memorial; Landell avisado (TI-03, ampliação de carga) | obrigatória |
> | TER-01 (6) = ainda não sei | no EP, mostrar ao cliente as duas opções, com e sem preparação para o andar extra, e a diferença de custo | opção comparada |
> | EST-05 estrutura à mostra + EST-02 concreto aparente | durabilidade do concreto aparente pela CAA (TI-EST-02); se for metálica aparente, avisar o Cardozo (outra norma) | padrão |
> | ESC-02 banheira ou hidromassagem | carga concentrada na laje do banheiro (NBR 6120:2019) | padrão |
> | Elevador ou plataforma no partido (novo item de acessibilidade da Arquitetura) | poço do elevador é escavação: na Barra e no Recreio, fica abaixo da água? (Skill de rebaixamento) | padrão |
> | TI-PAI-06 (jardim sobre laje) | ver a Correção 6 | obrigatória |

**Motivo:**
- O ALTO 13 diz "não há nenhum disparo estrutural (subsolo, balanço, vizinho encostado, declive)".
- A C-2 tem os disparos do partido, e a C-12 os do Paisagismo. Faltava a tabela da Estrutura, no mesmo formato.
- Tratar "ainda não sei" como "sim" segue a regra da Skill da NBR 6118: na dúvida, fica a classe mais exigente.
- Nas linhas de força "obrigatória", a falta da providência muda a classe da estrutura ou a segurança. Por isso não podem ficar como opção.

---

## Correção 6 (MÉDIO) — TI-PAI-06: o que o Baumgart precisa receber para dar a carga

**Texto atual:**
> | TI-PAI-06 | Se houver jardim, jardineira ou cobertura verde sobre laje: a carga admissível vem de Baumgart como dado de entrada, e a impermeabilização com anti-raiz segue a NBR 9575:2024 | Baumgart (carga), Glaziou (especificação) | EP, depois AP |

**Texto novo:**
> | TI-PAI-06 | Se houver jardim, jardineira ou cobertura verde sobre laje: **antes**, a Glaziou informa ao Baumgart a espessura da terra (substrato) e a vegetação prevista (gramado, arbusto ou árvore). O Baumgart calcula a carga com a terra **molhada** (NBR 6120:2019) e devolve a carga admissível como dado de entrada. A impermeabilização com anti-raiz segue a NBR 9575 (edição: ver o achado do Kelsen) | Glaziou (espessura e vegetação), Baumgart (carga), Glaziou (especificação) | EP, depois AP |

**Motivo:**
- Do jeito que está, a carga "vem de Baumgart", mas eu não consigo dar a carga sem saber quanta terra vai e o que vai plantado. A terra molhada pesa muito mais que a seca, e árvore em laje muda tudo. A NBR 6120:2019 é a norma de cargas.
- Sobre o ano da NBR 9575: o relatório já aponta que a edição é de 2010, confirmada em 2024 (lista de MÉDIOS e BAIXOS). Não repito a correção. Só tirei o ano para não colar um dado em disputa. O Kelsen fecha esse ponto.

---

## Correção 7 (MÉDIO) — TI-04: quem decide o sistema estrutural

**Texto atual:**
> | TI-04 | Sistema estrutural | Estrutural (2) | Baumgart (aparência à mostra/escondida vem de EST-05) | EP |

**Texto novo:**
> | TI-04 | Sistema estrutural (concreto, metálica ou misto; tipo de fundação) | Estrutural (2) | Baumgart propõe opções, a partir da TER-01, da sondagem preliminar (TI-01), da EST-05 (à mostra ou escondida) e da EST-02; Cardozo valida; o cliente aprova no EP | EP |

**Motivo:**
- Pelo meu perfil, o Baumgart **não decide o tipo de estrutura sem instrução do Cardozo**. A linha atual põe a decisão só no Baumgart.
- A linha também não ligava o sistema estrutural à sondagem, nem às escolhas do cliente que o mudam.

---

## Correção 8 (BAIXO) — TI-05: acesso de obra também serve à fundação

**Texto atual:**
> | TI-05 | Restrição construtiva/executiva (regras de condomínio, acesso de obra, lei) | Estrutural (1) | Oscar no Levantamento; lei via Lúcio → Kelsen | Levantamento |

**Texto novo:**
> | TI-05 | Restrição construtiva/executiva (regras de condomínio, acesso de obra, lei; **largura do acesso e horário de obra, porque limitam a máquina de estaca e o barulho**) | Estrutural (1) | Oscar no Levantamento; lei via Lúcio → Kelsen; leitura do acesso para a fundação: Baumgart | Levantamento |

**Motivo:** a máquina de estaca hélice contínua, que é a solução padrão na Barra e no Recreio (Skill Barra/Recreio, §3.3), precisa de acesso e de horário. Uma regra de condomínio que proíbe máquina grande ou vibração muda o tipo de fundação. Melhor saber no Levantamento do que no executivo.

---

## Correção 9 (BAIXO) — C-3 Gate: o que precisa estar pronto antes do AP estrutural

**Texto atual (fim da C-3):**
> "Com ressalvas" exige lista do que falta com dono.

**Texto novo (acrescentar uma frase depois):**
> "Com ressalvas" exige lista do que falta com dono. **Antes do AP estrutural:** TI-EST-01 fechada (sondagem suficiente para a casa do EP, ou registro de que a TI-01 basta) e TI-EST-02 fechada (CAA confirmada pelo cliente e CC definida).

**Motivo:**
- A NBR 6122 não aceita fundação sem sondagem suficiente.
- Pela Skill da NBR 6118, sem a CAA não há fck nem cobrimento.
- O Gate de hoje confere só a entrada no EP. Sem esta trava, o AP estrutural pode começar sem esses dois dados, que foi exatamente o erro dos meus 3 casos de exame (CAA ausente ou arbitrada, sondagem insuficiente).

---

## O que não verifiquei (para o Cardozo saber)

- Não li o texto oficial da NBR 6118:2026, da NBR 8036, da NBR 6122 nem da NBR 6120. Tudo vem das Skills do organismo, que se baseiam em fontes secundárias. Os números de furos, os gatilhos de CC3 e a regra "a CAA vem do contratante" precisam ser conferidos na norma antes de entrar em memorial real.
- A ATP na CC2 continua com divergência aberta na Skill `nbr6118-estrutural-concreto`.
- O peso da água da piscina (cerca de 14 kN/m²) é uma conta minha, só de ordem de grandeza. Não é valor de projeto.
