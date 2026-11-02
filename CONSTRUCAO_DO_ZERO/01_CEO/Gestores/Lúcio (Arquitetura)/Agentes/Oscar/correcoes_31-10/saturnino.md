# Correções do Saturnino (Hidrossanitário) ao Briefing Único v2 — 31/10/2026

- **Quem escreve:** Saturnino, equipe do Cardozo. Nível: Autonomous provisório. Por isso, esta proposta passa pela auditoria do Cardozo antes de o Oscar usar.
- **Base:** relatório `briefing_revisao_final_8_agentes_31-10.md` (ALTOS 2, 3 e 15; decisões de Claudemberg de 31/10; MÉDIOS e BAIXOS) e o Briefing `briefing_modelo_v2_proposta.md`. As linhas citadas (L) são as desse arquivo.
- **O que não fiz:** não editei o Briefing, não toquei no Ensaio 003 nem no Drive, e não fiz commit.
- **Códigos novos que proponho:** SUS-02 e HID-04 (perguntas). Uma regra nova, com número provisório **C-13**: se outro agente também propuser uma C-13, o Oscar renumera. Não criei tarefa interna nova: ampliei a TI-02 e a TI-13, que já são minhas.

**Fontes: o que eu li e o que não li (para ninguém tomar como certo o que não está confirmado)**
- **Lidas no texto oficial:** NBR 8160:1999 (PDF no acervo, lido em 29/09). Decreto Municipal 23.940/2004 e Resolução Conjunta SMG/SMO/SMU 001/2005 (lidos por Cardozo em 28/09, Skill `reservatorio-retardo-decreto23940-aguas-pluviais-rj`).
- **Não lidas no texto oficial (não estão no acervo `D:\008_Normas ABNT`):** NBR 16783:2019 (reuso), NBR 15527:2019 (água de chuva), NBR 5626:2020, NBR 10844:1989, NBR 10339 (piscina), NBR 15526 (gás) e Lei Estadual 9.164/2020, esta lida só em matéria de jornal. Onde cito essas normas, cito pela Skill ou pelo nome, sem número de item. Cada uma fica marcada "a confirmar".

---

## Item 1 — Reuso e água de chuva como pergunta de sustentabilidade (ALTO 15, decisão de Claudemberg)

### 1a. SUS-01 (L100): troca do texto e das opções

**Texto atual:**
> | SUS-01 | O que vocês querem ter? | CX: aproveitar água de chuva · aquecer a água com o sol (placas no telhado) · gerar energia com o sol · nenhum | sempre | Oscar, Saturnino, Landell | C |

**Texto novo (pronto para colar):**
> | SUS-01 | Quais destas ideias para economizar água e energia vocês querem na casa? | CX: guardar a água da chuva para usar de novo · reaproveitar a água do chuveiro e da pia do banheiro, depois de limpa por um filtro · aquecer a água com o sol (placas no telhado) · gerar energia com o sol · nenhuma. Ajuda ao cliente: "A água guardada ou reaproveitada não serve para beber, cozinhar nem tomar banho. Ela serve para a descarga, o jardim e a limpeza." | sempre | Oscar, Saturnino, Landell, Glaziou | C |

**Motivo:**
- O formulário antigo F7 tinha "Reuso" e "Captação de chuva" separados (transcrição de 30/10, L64). A junção na SUS-01 (diferenças, L161) deixou só a chuva, e o reuso da água do banho e da pia sumiu.
- A água do banho e da pia é "água cinza" e a água de chuva é outra fonte. Para a NBR 16783:2019 são fontes alternativas diferentes, cada uma com tratamento e controle de qualidade próprios (Skill `nbr16783-reuso-agua`; texto oficial não lido). Por isso viram duas opções.
- A frase de ajuda diz o limite de uso em linguagem simples. A NBR 16783 só admite água não potável em descarga, irrigação, lavagem de piso e de carro e usos ornamentais (Skill `nbr16783-reuso-agua`).
- Sobre a "pia": proponho só a pia do banheiro. A água da pia da cozinha tem gordura e costuma ficar fora do reuso. É prática de projeto que **não confirmei** no texto da NBR 16783. Se a norma admitir, a opção se amplia.
- O Glaziou entra no "Usado por" porque a C-12 (L228) usa a SUS-01. Esse é um achado MÉDIO do relatório.

### 1b. SUS-02 (código novo): para que vai servir a água

**Texto novo (linha nova, logo abaixo da SUS-01):**
> | SUS-02 | Para que vocês querem usar essa água guardada ou reaproveitada? | CX: descarga dos vasos sanitários · regar o jardim · lavar quintal, garagem e carro · não sei, quero a recomendação da equipe | SUS-01 contém "guardar a água da chuva" ou "reaproveitar a água do chuveiro e da pia do banheiro" | Saturnino, Oscar, Glaziou | C |

**Motivo:**
- ALTO 15: "ninguém pergunta para que serve a água de chuva". O uso muda o projeto. A descarga exige uma segunda rede de canos dentro da casa, só para essa água, e isso precisa ser decidido no EP. O jardim pede um ponto de água lá fora, ligado à irrigação. A lavagem pede torneiras externas próprias.
- A NBR 16783 pede controle de qualidade diferente para cada uso (Skill `nbr16783-reuso-agua`; aprendizado do Exame 2, caso Golden Palm).
- Tempo estimado: 0,5 min em casa, a medir.

### 1c. O que cada resposta dispara: regra nova C-13 (número provisório)

**Texto novo (pronto para colar, depois da C-12):**

> **C-13. Disparos de Hidrossanitário (Saturnino).** Valem quando o ESC-01 contém Hidrossanitário. Sem ele, cada linha vira nota "a cargo de quem fizer o hidrossanitário", e o Oscar só reserva o espaço no EP.
>
> | Resposta | Dispara | Força |
> |---|---|---|
> | SUS-01 com "guardar a água da chuva" | Cisterna que recebe **só água do telhado**, com filtro de folhas. Rede de água não potável separada da potável, com cor e placa próprias, sem nenhuma ligação entre as duas (NBR 16783). O extravasor vai para a rede de chuva ou para o jardim de chuva (C-12), **nunca para o esgoto**, porque no Rio as duas redes são separadas (NBR 8160 e NBR 10844). O volume depende da chuva do bairro: a série de chuva do Rio ainda não tem fonte confirmada e fica como pendência, sem número presumido. Cisterna enterrada com lençol alto: Baumgart confere a flutuação (empuxo). O espaço da cisterna entra no EP (Oscar) | obrigatória |
> | SUS-01 com "reaproveitar a água do chuveiro e da pia do banheiro" | Esgoto do chuveiro e da pia do banheiro coletado à parte, separado do vaso e da cozinha. Filtro ou tratamento, reservatório próprio e a mesma rede não potável separada e sinalizada (NBR 16783). A equipe mostra no EP o custo e o espaço (tratamento, reservatório e canos a mais), e o cliente confirma ou desiste | opção comparada |
> | SUS-02 = descarga | Os vasos são abastecidos pela rede não potável, com uma ligação de emergência da água potável que não deixa a água voltar. Shafts e prumadas a mais no EP. **A confirmar com o Kelsen antes de projetar:** a Res. Conj. 001/2005, Art. 6º, só autoriza lavagem e rega quando o reuso é exigido pela Prefeitura. A Skill `reservatorio-retardo-decreto23940-aguas-pluviais-rj` registra essa dúvida (R1) | obrigatória |
> | SUS-02 = regar o jardim | Ponto de água não potável no jardim, ligado à irrigação (ESC-02) e à C-12 quando houver Paisagismo | padrão |
> | SUS-02 = lavar | Torneiras externas de água não potável em nicho fechado, com a placa "ÁGUA IMPRÓPRIA PARA CONSUMO HUMANO" (Res. Conj. 001/2005, Art. 9º, aplicada como lado conservador até o Kelsen confirmar que vale para a casa que não é obrigada) | padrão |
> | SUS-01 com "aquecer a água com o sol" | Área de telhado voltada para o norte, reservada no EP (Oscar), com a carga das placas e do reservatório de água quente passada ao Baumgart. A HID-03 continua decidindo o apoio para dias nublados (elétrico ou a gás) | padrão |
> | Reservatório exigido por lei (TI-02) | É feito **com qualquer resposta da SUS-01**. A resposta só decide se a água guardada volta para uso ou só é soltada aos poucos na rede | obrigatória |

**Motivo:**
- Claudemberg pediu que eu dissesse o que cada resposta dispara. Hoje a SUS-01 só tem a linha de Paisagismo na C-12 (L228) e nenhum disparo hidrossanitário. A opção "aquecer com o sol" também não dispara nada.
- A separação entre esgoto e água de chuva é exigência da NBR 8160:1999 (lida). A separação entre água potável e não potável e a sinalização são da NBR 16783 (Skill; texto não lido).
- O último disparo existe porque a lei pode obrigar o reservatório de chuva mesmo que o cliente marque "nenhuma". Pelo Decreto 23.940/2004, Art. 1º, ele é exigido acima de 500 m² impermeabilizados. Pela Lei Estadual 9.164/2020, seria exigido em casa com telhado acima de 100 m² e menos de 25% do lote permeável, mas essa lei foi lida só em jornal e falta confirmar o texto com Kelsen/Hely. Ver o Item 5b.

---

## Item 2 — Piscina: dono e aquecimento (ALTO 15)

O Baumgart cria a pergunta sobre onde fica a piscina. **Não a repito.** Proponho só o dono e o aquecimento.

### 2a. Dono da piscina (nota nova na Parte B, abaixo da tabela de tarefas internas)

**Texto novo:**
> **Piscina (quando o ESC-02 contém Piscina): quem cuida de quê.** Dono: **Saturnino**, que cuida da água da piscina: filtro, bombas e casa de máquinas, ligação para encher, destino da água quando esvaziar, ralos e aquecimento. **Baumgart:** a estrutura do tanque e o lugar dela (no chão ou na cobertura), mais a flutuação com lençol alto. **Landell:** a elétrica (bombas, aquecedor elétrico ou bomba de calor, luz da piscina). **Glaziou:** o entorno, com plantas longe da borda (C-12). Impermeabilização: Baumgart e Saturnino juntos (NBR 9575). Sem Hidrossanitário contratado, a parte do Saturnino vira nota "a cargo de quem fizer o hidrossanitário", e o Oscar reserva a casa de máquinas no EP.

**Motivo:** a piscina é, antes de tudo, um sistema de água: enche, filtra, recircula, aquece e esvazia. Por isso o dono é o Saturnino. A estrutura fica com o Baumgart, como ele já está tratando. A norma específica de piscina é a NBR 10339 (projeto, execução e manutenção), que **não foi lida** e não está no acervo. O Cardozo precisa conseguir o texto antes do primeiro caso real com piscina. A ficha do Baumgart sobre rebaixamento de lençol já lista a piscina enterrada como caso de flutuação, e por isso ele cuida dessa parte.

### 2b. HID-04 (código novo): aquecimento da piscina

**Texto novo (linha nova na Seção 5, depois da GOU-01):**
> | HID-04 | A piscina vai ser aquecida? | GR: aquecer → não precisa / sim / ainda não sei; como (só se "sim") → com o sol (placas) / bomba de calor (aparelho elétrico que gasta menos que uma resistência) / a gás / tanto faz, quero a recomendação da equipe; quando (só se "sim") → o ano todo / só nos meses frios. **A opção "a gás" só aparece se a TI-13 confirmar gás possível** | ESC-02 contém Piscina | Saturnino, Landell, Oscar | C |

**Motivo:**
- ALTO 15: ninguém pergunta se a piscina é aquecida.
- A resposta muda três coisas. (1) O espaço: placas solares para piscina precisam de área de telhado ou de chão (Oscar), e a casa de máquinas cresce. (2) A carga elétrica: a bomba de calor é carga grande para o Landell. (3) O gás: depende da TI-13.
- A linha "quando" muda o tamanho do aquecedor. Aquecer o ano todo exige mais do que aquecer só no frio.
- A pergunta fica na Seção 5, que todos veem, pela mesma lógica da GOU-01 (C-6: o ESC-02 abre linhas dentro de seções que todos veem). Mesmo sem Hidrossanitário contratado, ela muda o partido.
- Não cito valor de consumo nem de área de placa porque não tenho fonte.
- Tempo estimado: 1 min em casa, a medir.

---

## Item 3 — Tarefa de disciplina não contratada (ALTO 2): regra para as minhas tarefas

### 3a. TI-13 (L163), coluna "Dono" e texto

**Texto atual:**
> | TI-13 | Existe gás encanado na rua (concessionária) ou só botijão/central de gás? Define se "a gás" aparece em COZ-01 e HID-03. Reservatório de água quente (antigo "boiler") também é decisão da equipe | F2/F7 (aquecimento), parecer Bardi 31/10 | Saturnino, com dado de concessionária do Levantamento (Oscar) | Levantamento, antes do link "em casa" |

**Texto novo:**
> | TI-13 | Existe gás encanado na rua (concessionária) ou só botijão/central de gás? Define se "a gás" aparece em COZ-01, GOU-01, HID-03 e HID-04. Reservatório de água quente (antigo "boiler") também é decisão da equipe. **Sem resposta da TI-13 antes do link "em casa", a opção "a gás" não aparece e fica anotado "SEM DADO — voltar ao cliente se o gás for confirmado depois"** | F2/F7 (aquecimento), parecer Bardi 31/10 | **Com Hidrossanitário contratado:** Saturnino, com o dado da concessionária levantado pelo Oscar. **Sem Hidrossanitário contratado:** Oscar, no Levantamento. Ele registra só o fato: há rede de gás na rua, sim ou não, e de onde veio a informação. O projeto de gás vira nota "a cargo de quem fizer o projeto de gás" | Levantamento, antes do link "em casa" |

### 3b. TI-02 (L152), coluna "Dono"

**Texto atual:**
> | Saturnino, com os dados de concessionária do Levantamento (Oscar) |

**Texto novo:**
> | **Com Hidrossanitário contratado:** Saturnino, com os dados de concessionária do Levantamento (Oscar). **Sem Hidrossanitário contratado:** Oscar registra no Levantamento só os fatos de campo (há rede de água, de esgoto e de chuva na rua; onde fica a caixa d'água ou a cisterna existente). O dimensionamento não é feito e vira nota "a cargo de quem fizer o hidrossanitário". O enquadramento legal do reservatório de chuva (Item 5b) vai ao Kelsen do mesmo jeito, porque trava o Habite-se |

### 3c. TI-PAI-03 (L171): a minha parte

**Texto novo (frase a acrescentar no fim da célula):**
> Sem Hidrossanitário contratado, a rede de chuva vira nota "a cargo de quem fizer o hidrossanitário"; Glaziou dimensiona só a parte com plantas.

**Motivo do Item 3:**
- Hoje a TI-13 trava a COZ-01 quando só a Arquitetura foi contratada, porque não tenho a quem passar o dado. A solução aprovada é o Oscar levantar no Levantamento.
- Separei **fato de campo** (Oscar consegue: perguntar à concessionária, olhar a rua) de **cálculo e especificação** (só quem é contratado para a disciplina faz).
- Deixei uma regra para quando o dado não chega: a opção some e a falta fica escrita. É a mesma lógica da C-1: "pergunta sem resposta não se adivinha".

---

## Item 4 — Opção "gás" da churrasqueira ignora a TI-13 (MÉDIO do relatório)

**Linha:** GOU-01 (L101).

**Texto atual:**
> | GOU-01 | Área gourmet | GR: churrasqueira → gás / carvão; cervejeira → sim / não; pia externa → sim / não | ESC-02 contém área gourmet | Oscar, Saturnino, Landell | C |

**Texto novo:**
> | GOU-01 | Área gourmet | GR: churrasqueira → a gás / carvão / tanto faz, quero a recomendação da equipe (**a opção "a gás" só aparece se a TI-13 confirmar gás possível**, como na COZ-01); cervejeira → sim / não; pia externa → sim / não | ESC-02 contém área gourmet | Oscar, Saturnino, Landell | C |

**Motivo:** a COZ-01 (L96) e a HID-03 (L107) já dependem da TI-13, e a GOU-01 ficou de fora. Sem a trava, o cliente escolhe uma churrasqueira a gás que talvez não possa ter. A TI-13 também passa a citar a GOU-01 (Item 3a). Pus "tanto faz" para que, quando o gás não aparecer, a linha não fique com uma opção só. Não é questão de norma. É coerência interna do Briefing (parecer Bardi 31/10, L59: "gás depende da TI-13").

---

## Item 5 — Outros achados meus, relendo o Briefing

### 5a. ALTO 3: a HID-03 só aparece com Hidrossanitário contratado (achado do Landell e meu)

**Linha:** HID-03 (L107), coluna "Condição".

**Texto atual:**
> ESC-01 contém Hidrossanitário **E** HID-01 = "Água Fria e Água Quente" **E** TI-13 confirmou que as duas opções são possíveis

**Texto novo:**
> ESC-01 contém Hidrossanitário **ou Elétrico** **E** HID-01 = "Água Fria e Água Quente". Se a TI-13 não confirmar gás, a opção "a gás" não aparece e a resposta só pode ser "elétrico" ou "tanto faz"

**Motivo:**
- O aquecedor elétrico de água costuma ser a maior carga da casa, e quem contrata Elétrico sem Hidrossanitário hoje não a informa.
- A condição antiga também escondia a pergunta inteira quando não havia gás. O certo é esconder só a opção "a gás", como na COZ-01.
- Com só Arquitetura contratada, a pergunta não aparece e fica a recomendação da equipe, escrita no estudo, como já é feito com a seção de automação.
- Alternativa, se Claudemberg preferir: levar a HID-03 para a Seção 5, visível a todos, porque o aquecedor a gás precisa de lugar ventilado no partido. Sugiro a mudança menor (o "ou Elétrico"), pela regra de manter o Briefing o menor possível. O Landell pode ter proposto outra forma; o Oscar junta as duas.

### 5b. TI-02 não confere se a lei obriga reservatório de chuva (MÉDIO, trava o Habite-se)

**Linha:** TI-02 (L152), coluna "O que a equipe levanta".

**Texto atual:**
> Abastecimento (rede, poço), reservatório (caixa, cisterna), destinação do esgoto, drenagem pluvial

**Texto novo:**
> Abastecimento (rede, poço), reservatório (caixa, cisterna), destinação do esgoto, drenagem pluvial. **Mais:** (1) se a lei obriga reservatório de chuva no lote: Decreto 23.940/2004 (acima de 500 m² impermeabilizados) e Lei Estadual 9.164/2020 (casa com telhado acima de 100 m², dispensada com 25% ou mais do lote permeável; texto a confirmar por Kelsen/Hely), com o Kelsen acionado via Cardozo e Lúcio; (2) poço ou água do subsolo: nunca se presume dispensa de outorga do INEA, o Kelsen confirma antes; (3) se o ESC-02 tem piscina: casa de máquinas, ligação para encher e destino da água ao esvaziar

**Motivo:**
- O reservatório de retardo condiciona o Habite-se (Decreto 23.940/2004, Art. 2º §4º, lido; Skill `reservatorio-retardo-decreto23940-aguas-pluviais-rj`). Nenhuma tarefa interna confere isso hoje.
- A dispensa por 25% de área permeável se cruza com a TI-PAI-05 (permeabilidade, Kelsen). A data de entrada é o Levantamento, para que a área do reservatório entre no EP.
- Sobre o poço: a Skill `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` e o meu aprendizado do Exame 3 (Grajaú) dizem que captação de água do subsolo nunca tem outorga presumida.

### 5c. Banheira ou hidromassagem sem água quente (MÉDIO)

**Linha:** C-2 (L182 a L199), linha nova na tabela.

**Texto novo (linha a acrescentar):**
> | ESC-02 com "Banheira ou hidromassagem" e HID-01 = "Água Fria" | Aviso ao cliente na revisão do Briefing: "banheira sem água quente — confirmar". Sem resposta, vale o que o cliente marcou, e o aviso fica escrito no estudo | padrão |

**Motivo:** as duas respostas podem se contradizer, e nada avisa. Banheira costuma usar água quente; se o cliente quer mesmo só água fria, ele confirma. Isso segue a C-1: "pergunta sem resposta não se adivinha".

### 5d. HID-02 mostra "Área gourmet" a quem não pediu área gourmet (BAIXO)

**Linha:** HID-02 (L98), coluna "Tipo / opções".

**Texto atual:**
> CX: Cozinha · Banheiros · Área de Serviço · Área gourmet (opções do F2)

**Texto novo:**
> CX: Cozinha · Banheiros · Área de Serviço · Área gourmet (esta opção só aparece se o ESC-02 contém área gourmet) (opções do F2)

**Motivo:** é a mesma lógica da C-6 (o ESC-02 abre linhas). Evita que o cliente marque água quente num lugar que não existe.

### 5e. Ninguém é dono do projeto de gás (MÉDIO, para o Cardozo decidir; não proponho texto ao Briefing)

A TI-13 só confere se existe gás na rua. O projeto de gás em si (rede dentro da casa, abrigo do botijão ou da central, ventilação dos cômodos com aparelho a gás) **não está em nenhuma Skill do organismo**. A minha Skill `nbr5626-8160-hidrossanitario` (L154) diz claramente que não cobre gás predial (NBR 15526). O formulário oferece "a gás" em quatro perguntas (COZ-01, GOU-01, HID-03 e HID-04), mas ninguém projeta o gás.

Não me nomeio dono por conta própria, porque isso seria ampliar escopo sem instrução. Sinalizo ao Cardozo, que decide: me dá o escopo e uma Skill de gás, ou o gás fica como "projeto de terceiro" no ESC-01.

---

## Efeito nos números (para o Oscar recontar com as propostas dos outros agentes)

| O que muda | Antes | Com as minhas propostas |
|---|---|---|
| Códigos ativos | 53 | +2 (SUS-02, HID-04) |
| Só Arquitetura, perguntas visíveis | até 37 | até 39 (SUS-02 e HID-04 são condicionais, na Seção 5) |
| Tempo em casa | 31,5 min | +1,5 min (SUS-02 0,5 e HID-04 1), estimado, a medir |
| Tarefas internas | 19 | 19 (só ampliei a TI-02 e a TI-13) |
| Regras | C-1 a C-12 | +C-13 (número provisório) e +1 linha na C-2 |

## Pendências que deixo abertas (não presumo)

- NBR 16783, NBR 15527, NBR 10339 e NBR 15526 sem texto oficial no acervo. Peço ao Cardozo que as consiga antes do primeiro caso real com reuso, piscina ou gás.
- A NBR 16783 admite a água da pia da cozinha no reuso? Confirmar no texto (Item 1a).
- Descarga com água de reuso numa casa que não é obrigada pela Prefeitura: confirmar com o Kelsen (Item 1c, linha SUS-02 = descarga).
- Lei Estadual 9.164/2020: texto da ALERJ e vigência a confirmar com Kelsen/Hely (Item 5b).
- Dono do projeto de gás: decisão do Cardozo (Item 5e).
