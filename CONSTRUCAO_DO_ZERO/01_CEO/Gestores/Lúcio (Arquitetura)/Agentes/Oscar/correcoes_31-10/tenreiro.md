# Correções de Interiores para o Briefing Único v2 (Tenreiro, 31/10/2026)

- **Pedido:** Cardozo, a mando de Claudemberg (decisões de 31/10 em `briefing_revisao_final_8_agentes_31-10.md`: ALTO 16, D1, D2 e K1).
- **Fontes lidas:** `briefing_modelo_v2_proposta.md` (Briefing), `briefing_formularios_drive_transcricao_30-10.md` (transcrição, seção "Opções do Interiores (FORM-INT)", linhas 74 a 83, e seção 4, linhas 30 a 39) e a Skill `layout-mobiliario-dimensoes-residencial` (só a parte das 3 faixas).
- **O que eu não fiz:** não editei o Briefing (o Oscar junta tudo), não mexi no Drive nem no Ensaio 003 e não fiz commit.
- **Contagem:** cada item diz quanto muda de código e de tempo. A recontagem final das tabelas "Números" e "Tempo" fica com o Oscar, porque os outros agentes também mexem nelas.

---

## Parte 1. D2: a INT-02 volta às opções originais

### T-1 · INT-02 (Seção 6, linha 115)

**Texto atual:**
> | INT-02 | Para cada cômodo de INT-01: que sensação ele deve dar? | GR (uma linha por cômodo marcado no INT-01, uma escolha por linha): acolhedor / energizante / calmo / elegante / tanto faz | ESC-01 contém Interiores; só os cômodos do INT-01 | Tenreiro | C |

**Texto novo:**
> | INT-02 | Para cada cômodo que entra nos interiores: que sensação ele deve passar? Escolham uma palavra por cômodo. Se não fizer diferença, deixem em branco. | GR (uma linha por cômodo marcado no INT-01, uma escolha por linha): Aconchegante / Sofisticado / Minimalista / Contemporâneo (opções do FORM-INT) | ESC-01 contém Interiores; só os cômodos do INT-01 | Tenreiro | C |

**Por quê:**
- **D2.** As quatro opções foram copiadas exatamente da transcrição (linha 78: "Aconchegante | Sofisticado | Minimalista | Contemporâneo").
- **Formato mantido.** Continua uma escolha por cômodo, não o ranking de 1 a 4, porque esse corte foi aprovado por Claudemberg em 31/10 para poupar 2,5 min. O tempo fica igual (1,5 min).
- **"tanto faz" saiu.** Não é opção original. Quem não tiver preferência deixa a linha em branco, o que é permitido porque a INT-02 não é obrigatória (C-1). Por isso o texto da pergunta ganhou a frase "deixem em branco".
- **Redação.** Mudou só "INT-01" para "cômodo que entra nos interiores", porque o cliente não vê códigos.

### T-2 · Nota abaixo da Seção 6 (linha 118)

**Texto atual:**
> > INT-02 ficou (não saiu), com sensações de verdade: o estilo da casa já está em EST-01; a sensação por cômodo muda decisões que o estilo não decide (cor da luz, cores e materiais de cada cômodo), e corresponde à pergunta original "sensação ao entrar" do FORM-INT.

**Texto novo:**
> > INT-02 usa as opções originais do FORM-INT (Aconchegante, Sofisticado, Minimalista, Contemporâneo), por decisão de Claudemberg em 31/10/2026 (D2). Fica a escolha de uma palavra por cômodo, corte aprovado em 31/10. Sem preferência, a linha fica em branco. Duas opções (Minimalista e Contemporâneo) também aparecem no estilo da casa (EST-01): a EST-01 vale para a casa toda, e a INT-02 permite que um cômodo fuja dela.

**Por quê:** a nota antiga defende a escolha que D2 desfez. A frase final responde a uma pergunta que vai surgir: "não é a mesma coisa que a EST-01?".

### T-3 · C-8 (linha 211), trecho final

**Texto atual:**
> INT-02 trocou as opções de estilo do FORM-INT por sensações (decisão de Oscar em 31/10, justificativa abaixo da Seção 6; Lúcio confirma) e, na 2ª correção (31/10, aprovada por Claudemberg), o ranking 1–4 virou uma escolha por cômodo com "tanto faz", só nos cômodos do INT-01.

**Texto novo:**
> INT-02 volta às opções do FORM-INT (Aconchegante, Sofisticado, Minimalista, Contemporâneo), por decisão de Claudemberg em 31/10/2026 (D2), que desfez a troca por sensações. Fica o formato da 2ª correção, também aprovado em 31/10: uma escolha por cômodo, só nos cômodos do INT-01. Sem "tanto faz", porque não é opção original: a linha em branco faz esse papel.

**Por quê:** é o registro de onde cada opção veio. O texto atual ficou falso depois da D2.

---

## Parte 2. Ajustes pedidos

### T-4 · C-8 (linha 211), trecho das cores

**Texto atual:**
> Estilo/cores do FORM-INT ("Estilo predominante", "Referências visuais", "Cores preferidas" e "Cores rejeitadas") são texto livre no formulário, sem lista; nada a copiar.

**Texto novo:**
> Estilo e cores do FORM-INT: "Estilo predominante" está na EST-01; "Referências visuais" está na EST-02; "Cores rejeitadas" está na EST-03 ("cor"); "Cores preferidas" virou a EST-06 (texto livre, como no original).

**Por quê:** a frase "nada a copiar" fez a pergunta "cores preferidas" sumir. Era texto livre, mas era uma pergunta.

### T-5 · Nova pergunta EST-06 (Seção 4, logo depois da EST-03)

**Texto novo (linha nova):**
> | EST-06 | Que cores vocês gostam de ver em casa? Pode ser o nome da cor ou um jeito de dizer, como "tons claros", "cores da madeira", "nada muito colorido". | TXT (opcional; "Cores preferidas" do FORM-INT) | sempre | Oscar, Tenreiro | C |

**Por quê:**
- A "cores preferidas" do FORM-INT não virou pergunta (ALTO 16). As "cores rejeitadas" já estão cobertas pela EST-03.
- Ficou na Seção 4, que todos veem, e não na Seção 6, porque a cor também serve à fachada (Oscar) e porque fica ao lado da EST-03, que pergunta o contrário.
- **Custo:** +1 código e +0,5 min em casa (estimativa, a medir) em todos os pacotes. O número EST-06 é sugestão: se o Oscar preferir que a pergunta seja só de Interiores, vira INT-05 na Seção 6, com a condição "ESC-01 contém Interiores".

### T-6 · Nova pergunta ILU-02 (Seção 6, logo depois da ILU-01)

**Texto novo (linha nova):**
> | ILU-02 | Como vocês querem a luz da casa? | ME: Aconchegante (luz mais amarelada e suave) · Neutro (luz branca, parecida com a do dia) · Técnico (luz branca e forte, para trabalhar e enxergar detalhes) (opções do FORM-INT) | ESC-01 contém Interiores ou Elétrico | Tenreiro, Landell | C |

**Por quê:**
- **Recupera as opções perdidas** (transcrição, linha 81: "ambiente mais: Aconchegante | Neutro | Técnico"). Elas definem a cor da luz da casa, coisa que a ILU-01 não decide: a ILU-01 diz o tipo de iluminação (funcional, decorativa, cênica), não a cor da luz.
- **Parênteses.** São um ajuste de redação indispensável, porque o leigo não sabe o que é "luz técnica". Os parênteses são minha leitura das opções e não fazem parte do original. O Gate confirma.
- **Condição igual à da ILU-01.** As duas aparecem juntas, e o Landell também usa o dado.
- **A outra metade da pergunta antiga não vira pergunta nova.** Ela dizia "deseja: Automação | Cenas de iluminação | Destaques decorativos" e já está coberta: "Cenas" é a opção Cênica da ILU-01, "Destaques decorativos" é a opção Decorativa da ILU-01, e "Automação" está na AUT-01/AUT-02, ou no ESC-02 "casa inteligente" quando a Automação não foi contratada. Repetir só aumentaria o tempo.
- **Custo:** +1 código e +0,5 min em casa nos pacotes com Interiores ou Elétrico.

### T-7 · Nova pergunta INT-04 (Seção 6, logo depois da INT-03)

**Texto novo (linha nova):**
> | INT-04 | Vocês querem algum destes itens? Em cada linha, marquem os cômodos onde querem o item, ou "não quero". | GR (uma linha por item; em cada linha, os cômodos do INT-01, podendo marcar vários, + "não quero"): Painel de TV · Estante · Bar · Lareira (opções do FORM-INT) | ESC-01 contém Interiores | Tenreiro, Oscar, Landell, Saturnino | C |

**Por quê:**
- **Recupera "Necessidades específicas do ambiente"** (transcrição, linha 79: "Painel TV | Estante | Bar | Lareira | Automação"), pedida no ALTO 16.
- **Vale para cada cômodo.** O formulário antigo perguntava isso dentro de cada ambiente; aqui são os cômodos do INT-01.
- **"Automação" ficou de fora.** Já é perguntada na AUT-02 (o que automatizar e onde) ou no ESC-02 ("casa inteligente"). Se Claudemberg quiser a cópia completa, basta acrescentar uma linha "Automação" com a condição "só se Automação não estiver no ESC-01".
- **Outros agentes usam o dado:**
  - painel de TV: ponto de TV e tomadas (Landell);
  - bar: pode pedir ponto de água e esgoto (Saturnino) e tomada para geladeira ou cervejeira (Landell);
  - lareira: muda a arquitetura (saída de fumaça, Oscar). Se for a gás, depende da TI-13 (Saturnino). O tipo de lareira é escolha da equipe, não do cliente.
- **Disparo para a C-2** (texto pronto para colar):
  > | INT-04 com bar ou lareira | bar: ponto de água e esgoto (Saturnino) e tomada (Landell); lareira: saída de fumaça no partido (Oscar) e tipo escolhido pela equipe (a gás só se a TI-13 confirmar). Disciplina não contratada vira nota para quem fizer aquela parte | padrão |
- **Custo:** +1 código e +1 min em casa (estimativa, a medir) nos pacotes com Interiores.
- **Disparo do bar.** A ideia de que o bar pode pedir ponto de água é minha, de prática de projeto, não de norma. O Saturnino confirma.

---

## Parte 3. Conferência da lista de cômodos (INT-01)

### O que a INT-01 mostra hoje

"CX (cômodos de PRG-01)". A PRG-01 tem estas opções: sala de estar · sala de jantar · sala de TV separada · cozinha · lavabo · varanda · suíte do casal (closet?) · outras suítes · quartos · quarto de hóspedes · escritório · academia · cinema · biblioteca · lavanderia · despensa · quarto e banheiro de funcionário · jardim · playground · outros.

### Comparação com o FORM-INT

A lista do FORM-INT está na transcrição, linha 76: Sala de Estar · Sala de Jantar · Cozinha · Área Gourmet · Lavabo · Suíte Master · Closet · Quartos · Banheiros · Home Office · Brinquedoteca · Academia · Cinema/TV · Lavanderia · Rouparia · Depósito.

**O que FALTA na INT-01, porque não está na PRG-01:**

| Falta | Situação na PRG-01 | Peso para Interiores |
|---|---|---|
| **Banheiros** | Não existe a opção. Só se deduz o banheiro das suítes e do funcionário. O banheiro social (de quarto não suíte) não tem onde ser marcado. | Alto: revestimento, bancada, box, marcenaria (ALTO 16) |
| **Área gourmet** | Não está na PRG-01; está no ESC-02 ("Área gourmet/churrasqueira"). Por isso não aparece na INT-01. | Alto: bancada, revestimento, mobiliário externo (ALTO 16) |
| **Closet** | Só como "(closet?)" dentro da suíte do casal. Não há closet nas outras suítes. | Médio: é marcenaria pura |
| **Brinquedoteca** | Não existe | Baixo a médio |
| **Rouparia** | Não existe | Baixo: marcenaria |
| **Depósito** | Não existe. "Despensa" é guardar comida; "depósito" é guardar coisas. Não são a mesma coisa. | Baixo |

**O que SOBRA na INT-01 (vem da PRG-01, mas não é Interiores):**
- **Jardim e playground:** são área externa (Paisagismo, Glaziou). Devem sair da lista da INT-01.

**O que a PRG-01 tem e o FORM-INT não tinha, mas deve FICAR na INT-01:** varanda, quarto de hóspedes, biblioteca, despensa, quarto e banheiro de funcionário, outras suítes, outros. Todos podem receber mobiliário e acabamento.

**Mesma coisa com nome diferente (sem perda):** Suíte Master = suíte do casal; Home Office = escritório; Cinema/TV = cinema + sala de TV separada. Fico com os nomes da PRG-01, que estão em português e são os que o cliente já viu.

### T-8 · INT-01 (Seção 6, linha 114)

**Texto atual:**
> | INT-01 | Quais cômodos entram no projeto de interiores? | CX (cômodos de PRG-01) | ESC-01 contém Interiores | Tenreiro | C |

**Texto novo:**
> | INT-01 | Quais cômodos entram no projeto de interiores? | CX (vem marcada com os cômodos da PRG-01 e com a área gourmet, se marcada no ESC-02; o cliente desmarca o que não entra): sala de estar · sala de jantar · sala de TV separada · cozinha · área gourmet · lavabo · banheiros · varanda · suíte do casal · closet · outras suítes · quartos · quarto de hóspedes · escritório · brinquedoteca · academia · cinema · biblioteca · lavanderia · rouparia · despensa · depósito · quarto e banheiro de funcionário · outros (quais?) | ESC-01 contém Interiores | Tenreiro | C |

**Por quê:**
- **Entram** banheiros e área gourmet (pedido do ALTO 16), mais closet, brinquedoteca, rouparia e depósito, que estavam no FORM-INT e se perderam.
- **Saem** jardim e playground, que são Paisagismo.
- **Pode ser assim agora.** Sem o Forms (K1), a lista pode vir pré-marcada pela PRG-01 e pelo ESC-02, e o cliente só confere. Fica simples e não repete a pergunta.

### T-9 · Recomendação ao Oscar (PRG-01, linha 62; a PRG-01 é dele, não minha)

A raiz do problema está na PRG-01. Hoje o cliente não tem onde dizer quantos **banheiros** quer além dos das suítes, e isso é dado de Arquitetura, não só de Interiores.

**Sugestão** (o Oscar decide a redação e se entra): acrescentar à PRG-01 as opções:
- "banheiro social (quantos)";
- "closet" como opção separada da suíte;
- "brinquedoteca", "rouparia" e "depósito".

**Por quê:**
- Se a PRG-01 não tiver essas opções, a INT-01 marca um cômodo que a Arquitetura não planejou.
- O mesmo acontece com a área gourmet: hoje ela só está no ESC-02 (desejos). A INT-01 consegue pegá-la de lá (T-8), sem mudar a PRG-01.

---

## Parte 4. D1: a MED-01 sai; a folga vem do NIV-01

**Afeta meu trabalho? Sim, em três pontos.**

1. **Folga da mobília nos interiores.** A circulação em volta dos móveis, da marcenaria do closet, da cozinha e do banheiro segue a faixa da Skill `layout-mobiliario-dimensoes-residencial`. Hoje essa faixa vem da MED-01. Sem ela, passa a vir do NIV-01. A Skill diz no passo 1: "Leia no Briefing a faixa pedida. Sem indicação: conforto". O dono da Skill (Lúcio ou Oscar) deve trocar "faixa pedida" por "faixa que vem do padrão da obra (NIV-01)". Eu não edito a Skill.
2. **A linha da C-2 que cita o meu nome** (linha 196) deixa de fazer sentido. Texto pronto abaixo (T-10).
3. **A opção "aceito o mínimo da norma em algum ponto (qual?)" some com a MED-01.** Hoje é o único lugar onde o cliente pede uma folga menor. Não é escopo meu, mas aviso: o ALTO 9 (Kelsen) pede o registro do "aceito o mínimo" na DEC-01, e a D4 muda a frase ao cliente. O Oscar e o Kelsen precisam decidir onde esse pedido do cliente fica registrado.

### T-10 · C-2, linha do NIV-01 (linha 196)

**Texto atual:**
> | NIV-01 | pré-marca MED-01; Tenreiro usa o mesmo dado (não pergunta de novo) | padrão |

**Texto novo:**
> | NIV-01 | define a faixa de folga da Skill `layout-mobiliario-dimensoes-residencial` para Arquitetura e Interiores: econômico ou médio → conforto (padrão do escritório); alto padrão ou premium → alto padrão. O mínimo só com pedido escrito do cliente e aprovação de Claudemberg. Tenreiro usa o mesmo dado (não pergunta de novo) | padrão |

**Por quê:**
- **De onde vem a regra.** Não criei regra nova: juntei três regras que já estão no Briefing e na Skill.
  - "alto padrão ou premium → alto padrão" vem da própria MED-01: "Vem pré-marcada 'alto padrão' se NIV-01 = alto padrão ou premium".
  - "conforto" para os outros padrões vem da Skill, onde conforto é o "Padrão do escritório".
  - "mínimo só com aprovação" vem da linha da MED-01 na C-2 (linha 198), que sai junto com ela.
- **"Econômico" não leva ao mínimo.** Não há regra escrita que diga isso. Se Claudemberg quiser que o padrão econômico use a faixa mínima, a decisão é dele, não minha.

**As outras linhas que a D1 obriga a mudar são do Oscar, não minhas:**
- linha 79 da MED-01 (sai);
- linha 198 da C-2 (sai);
- na C-1, "MED-01" sai da lista de obrigatórias, a equivalência "B7 = MED-01" vira "B7 = NIV-01" e a frase "Sem resposta na MED-01: conforto" sai;
- no tempo, −2 min na reunião;
- na contagem, −1 código.

---

## Parte 5. Outros achados meus (MÉDIOS e BAIXOS)

### T-11 (MÉDIO) · ESC-02, coluna "Usado por" (linha 44)

**Texto atual:**
> | Oscar, Saturnino, Landell, Glaziou |

**Texto novo:**
> | Oscar, Tenreiro, Saturnino, Landell, Glaziou |

**Por quê:** com a T-8, a INT-01 passa a ler a área gourmet do ESC-02. A adega também é marcenaria e mobiliário. Sem o meu nome, quem montar o sistema não sabe que eu dependo desse dado.

### T-12 (BAIXO) · GOU-01, coluna "Usado por" (linha 101)

**Texto atual:**
> | Oscar, Saturnino, Landell |

**Texto novo:**
> | Oscar, Saturnino, Landell, Tenreiro |

**Por quê:** a cervejeira e a pia externa entram na bancada e na marcenaria da área gourmet, que agora está na INT-01.

### T-13 (BAIXO) · CLI-01, coluna "Usado por" (linha 99)

**Texto atual:**
> | Oscar, Landell |

**Texto novo:**
> | Oscar, Landell, Tenreiro |

**Por quê:** a posição do ar-condicionado muda o forro, a sanca e a marcenaria que esconde o aparelho e o dreno.

### T-14 (BAIXO) · Nome da lavanderia (HID-02, linha 98, e PRG-01, linha 62)

**O que está escrito:** a HID-02 diz "Área de Serviço"; a PRG-01 e o FORM-INT dizem "lavanderia".

**Sugestão** (Oscar e Saturnino decidem): usar o mesmo nome nas duas, por exemplo "lavanderia / área de serviço".

**Por quê:** é o mesmo cômodo com dois nomes. O cliente leigo pode achar que são dois cômodos diferentes, e o sistema não consegue cruzar uma resposta com a outra.

### T-15 (BAIXO, só registro, sem texto novo) · Perguntas do FORM-INT que não precisam voltar

Conferi as perguntas do FORM-INT (transcrição, linhas 30 a 39) que não estão nas Partes 1 a 3. Todas já estão cobertas, e por isso não proponho pergunta nova:
- **"uso" e "capacidade" do ambiente:** PRG-02 e SOC-03;
- **"problemas a evitar":** EST-03 e PRG-02;
- **"Materiais: proibidos":** EST-03;
- **"Investimento: nível esperado":** NIV-01. As opções são as mesmas: Econômico, Médio padrão, Alto padrão, Premium;
- **"o que não pode faltar" e "sensação ao entrar":** OBJ-01 e INT-02;
- **"algo importante não perguntado":** FIM-01.

---

## Resumo do impacto nos números (só a minha parte)

| Item | Código | Tempo (estimativa, a medir) |
|---|---|---|
| EST-06 (cores preferidas) | +1 | +0,5 min em casa, todos os pacotes |
| ILU-02 (luz Aconchegante, Neutro, Técnico) | +1 | +0,5 min em casa, com Interiores ou Elétrico |
| INT-04 (painel de TV, estante, bar, lareira) | +1 | +1 min em casa, com Interiores |
| INT-01 e INT-02 | 0 | 0 |
| D1 (MED-01 sai; é do Oscar, só registro) | −1 | −2 min na reunião |
