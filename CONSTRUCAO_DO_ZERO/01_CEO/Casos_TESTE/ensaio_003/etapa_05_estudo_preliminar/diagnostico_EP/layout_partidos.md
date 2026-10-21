# Layout do zero: partidos (Passos 1 a 4). Ensaio 003, EP

**Oscar (Assisted) | para auditoria de Lúcio | 19/10/2026 | caso 100% fictício | treino das Skills `layout-residencial-zoneamento-fluxos` v1.0 e `posicionamento-escada-residencial` v1.1**
**Natureza:** só texto. **Nenhuma escrita no Revit nesta rodada.** O modelo foi só lido (`get_revit_status`, `get_levels`, `list_elements` Paredes com `location`). Análise preliminar, sem Gate.

**Conclusão primeiro.** Recomendo o **Partido B**: frente toda social (hall, escritório, lavabo), 4 vagas descobertas na faixa lateral direita (fora da projeção), escada em U logo atrás do hall, serviço numa faixa à direita ligada à cozinha, social no fundo. É o único dos três em que eu espero **0 grave** na `conferir_layout`. Ele depende de 3 respostas: Kelsen (vaga no afastamento lateral), cliente (demolir a edícula) e topógrafo (posição das árvores, T11). O A (garagem coberta na frente) não fecha num lote de 9,29 m. O C (pátio central) tem a melhor ventilação, mas é o que mais perde em H1 e deixa a dependência acessada pela lavanderia.

Coordenadas em metros, no referencial do Levantamento v8: origem no vértice frente-esquerda (muro do Lote 16), **x ao longo da testada, y da rua para os fundos** (`etapa_03…/v8/01_…_v8.md` L18–19). Faixas de ambiente pela face externa, ±0,15 m de parede.

---

## Passo 1. Lote e lei

| Item | Valor | Origem (arquivo e linha) |
|---|---|---|
| Área de cálculo | 571,80 m² medida (título 600,00) | parecer_legal_base_003.md L23, L54; enunciado EP L22 |
| Afastamentos | frontal 6,00; laterais 2,50; fundos 5,00 (Regramento, mais restritivo) | parecer L33–35; enunciado EP L18 |
| Envelope H0 | 9,29 × 29,00 = 269,41 m²; **x 2,50–11,79; y 6,00–35,00**; forma: retângulo aproximado (o lote real não tem ângulos levantados, T5) | anexo_contas_003_v8.md L27–28; parecer L80–82; 01_v8 L20, L49 |
| Envelope H1 (APP contingente) | 9,29 × 16,00 = 148,64 m²; **y 6,00–22,00** | anexo_contas v8 L36; 01_v8 L34–35, L53; parecer L92 |
| H0 × H1 | H0 não pode ser prometido: a faixa y 22–40 fica "em suspenso" até SMAC, INEA e SPU | parecer L273; L166 |
| TO | 40% (condomínio) → projeção máxima **228,72 m²**, contando como projeção tudo o que for coberto, garagem inclusive | parecer L29, L68, L264 |
| Teto computável | 2 × 228,72 = **457,44 m²** (C) | parecer L69–70; Briefing v4 02 L37 |
| Gabarito e altura | 2 pavimentos; 8,50 m da soleira ao ponto mais alto → **+11,70** se a soleira for +3,20 | parecer L30–31; anexo_contas v8 L199 |
| Cobertura | só técnica; vedado terraço/lazer sobre a laje | parecer L32 |
| Subsolo/escavação | vedado; escavação ≤ 1,20 m | parecer L37 |
| Frente (rua) | Rua das Garças, em **y = 0**; testada 14,30 m; lote de meio de quadra, só a frente é acesso documentado | 01_v8 L4, L41–43, L104 |
| Divisas | esquerda: muro do Lote 16 (x 0); direita: edícula com face em x ≈ 13,49 (parecer: demolir) | 01_v8 L42, L55; parecer L120 |
| Árvores | ipê + 2 amendoeiras no frontal (y 0–6); x, DAP e copa **não constam (T11)**; parecer: preservar; frontal recebe só o acesso de carro | 01_v8 L58; 02_v8 L87–89; parecer L269 |
| Vaga no frontal | vaga descoberta no afastamento frontal mínimo **não é solução** (Dec. 3.046 XXII) | ERRATA_08-10-2026.md (etapa_01) L15, L22, L26; parecer_legal_etapa_01_ERRATA L23–26; enunciado EP L21 |
| Garagem coberta | Dec. 3.046 XXIII (só em subsolo/pavimento-garagem) aplicável ou não a unifamiliar: **pendente — dono Kelsen** | parecer L291; ERRATA raiz L60 |
| Permeável | ≥ 142,95 m² (25%), porções ≥ 4 m² e 2 m de lado; folga impermeável fora do envelope 159,24 m² | parecer L36, L265; anexo_contas v8 L158 |
| SMD | 57,18 m² (TO 50%) ou 68,62 m² (TO 40%): **dois valores, pendente — dono Kelsen (P-SMD)** | Briefing v4 02 L44 |
| Varandas | não computam, mas sem balanço sobre os 6 m frontais e ≥ 2,50 m das divisas | parecer L38, L268 |
| **Norte** | **norte pendente — dono topógrafo** (matriz item 19). Orientação solar tratada só como hipótese; não aceito "sala para o poente" do corretor | 03_matriz_v8 L34; enunciado EP L27, L88, L126 |
| Ventos, insolação | **pendentes — dono topógrafo/Oscar** | 03_matriz_v8 L34 |
| Cota de soleira | +3,20 **prevista**, referencial do condomínio; desnível rua × soleira **pendente — dono topógrafo (T2–T4)** | parecer L41; 02_v8 L94, L110; enunciado EP L34 |
| Níveis | **Divergência:** a ordem de Lúcio diz 0,30 / 3,45 / 6,60 (piso a piso 3,15). O modelo lido diz **Páv. térreo 0,30 / Páv. Superior 3,30 / Cobertura 6,30** (piso a piso **3,00**). **Pendente — dono Lúcio.** | `get_levels` nesta execução (ids 311, 694, 323714) |
| Altura (conta) | com 3,15: cobertura a 6,30 acima do térreo + telhado/platibanda ≤ 2,20 = ≤ 8,50 ✓, se a soleira for o piso do térreo. Relação nível Revit × referencial do condomínio: pendente — dono Lúcio/topógrafo | parecer L31 |
| Volume atual do modelo | projeção x 2,50–11,79; y 6,00–30,62 (paredes externas 449332–449335, eixo em 2,575/11,715 e 6,075/30,545, 15 cm) = 9,29 × 24,62 = 228,72 m² | `list_elements` Paredes nesta execução |

---

## Passo 2. Programa (Briefing Etapa 04 v4)

Usei a **v4** (`etapa_04_briefing/entrega/v4/02_planilha_ambientes_003_v4.md`). **O Briefing não tem metragem por ambiente** (L7 e L15–29: "a definir", dono Cliente; P-l fecha no EP com o cliente, enunciado EP L31). A coluna "área de estudo" é **hipótese minha para desenhar o Partido B**, não área-alvo do Briefing.

| ID Briefing | Ambiente | Área-alvo (Briefing) | Área de estudo (Oscar, Part. B) | Pav. | Exigência |
|---|---|---|---|---|---|
| A1 | Suíte D. Lourdes | a definir (L15) | quarto 16,4 + banho/closet 11,7 | térreo | programa, não lei (COES Art. 31 V, parecer L281); NBR 9050:2020 **não está no acervo** e a Skill `arquitetura-nbr9050-acessibilidade` **não foi lida nesta execução**: nenhum "atende" declarado. Pendente — dono Oscar (leitura) + Lúcio |
| A2 | 3 suítes | a definir (L16) | 39,0 / 28,1 / 44,2 | superior | toda suíte com banheiro (regra 5) |
| A3 | Home office | a definir (L17) | 16,4 | térreo, na frente | atendimento de clientes e porta própria: **pendente — dono Kelsen** (uso) |
| A4 | Home cinema | a definir (L18) | 24,9 | superior | porta por acústica |
| A5 | Estar/jantar integrado | a definir (L19) | 52,2 + 42,6 | térreo, fundo | pé-direito de 7 m pedido por Rodrigo (enunciado EP L79): **pendente — dono Lúcio/Kelsen** |
| A6/A7 | Cozinha + gourmet | a definir (L20–21) | 13,3 + varanda gourmet externa 40,7 | térreo | regime da gourmet/varanda: **pendente — dono Kelsen** (L21) |
| A8 | Serviço + dependência | a definir (L22) | lavanderia 6,6; dependência 6,2 + banho 3,3; circulação de serviço 8,3 | térreo | entrada de serviço separada (regra 3) |
| A9 | Garagem 4 vagas | n·a, "a" sem valor (L23) | Part. B: 0 m² de projeção (vagas descobertas) | externo | "a" **não fixado**; vaga 2,50 × 5,00 (COES Art. 29 I, via L23) |
| A11–A13 | Piscina, deck, jardim | a definir (L25–27) | fora do volume | externo | piscina fora das premissas até T10 e laudo (02_v8 L18) |
| A14 | Edícula | demolição (L28) | 0 | — | o Partido B **depende** da demolição |
| A15 | Circulações, halls, lavabo | a definir, Oscar na Etapa 05 (L29) | ver partidos | ambos | — |

**Soma e comparação.** Pedido: ~520 m² construídos (Briefing v4 02 L42; enunciado EP L30). Teto: 457,44 m² computáveis (C) em H0 (L37). Déficit: **62,56 m²** (L43), que **não é** item não computável. Fisicamente o envelope × 2 dá 538,82 m², mas a TO limita a projeção a 228,72. Em H1: construída máxima 297,28 m² (enunciado EP L32). **Não cabe. Registro, não corto:** leva ao cliente (P-l). Garagem descoberta (Part. B) libera ~56 m² de projeção em relação a uma garagem coberta de 4 vagas, mas isso não fecha os 62,56.

---

## Passo 3. Zoneamento escrito

- **Social:** hall, lavabo, estar, jantar, varanda gourmet. Térreo; o hall na frente, o estar no fundo (jardim/lago).
- **Serviço:** cozinha, lavanderia, dependência, despensa, vagas. Térreo, faixa direita (lado do acesso de carros e da edícula a demolir, o "lado pior" sem norte conhecido).
- **Íntimo:** suíte D. Lourdes (térreo, porque não pode depender de escada); 3 suítes e cinema no superior.
- **Semipúblico:** escritório com atendimento, na frente, junto ao hall.
- **Circulação:** hall → galeria → escada; no superior, hall de chegada → galeria.
- **Fluxos:** visita: rua → porta social → hall → (lavabo/escritório) → galeria → jantar/estar, sem passar por íntimo nem serviço (regra 2). Morador: carro → porta de serviço → cozinha; ou porta social → hall → escada. Serviço: faixa lateral → lavanderia → circulação de serviço → dependência/cozinha, sem cruzar o social (regra 3).

---

## Passo 4. Partidos

Escada (todos): piso a piso 3,15 → 3,15/0,175 = **18 espelhos**, piso 0,28. Reta não serve (regra 10 da Skill de escada): **U ou L, 9 + 9 espelhos** (≤ 10 por lance). Lance: 8 pisos × 0,28 = 2,24 m; patamar 1,00 × 1,00; lance de 1,00 m. U ≈ 2,10 × 3,24 m; L ≈ 3,24 × 3,24 m. Se valer o piso a piso do modelo (3,00): 17 × 0,176 (9 + 8) ou 18 × 0,167. Muda a conta, não o formato. Área livre: largura do lance (1,00) × 1,20 m, na partida e na chegada (seção 3 da Skill).

### Partido A: garagem coberta na frente (4 vagas, 2 × 2 em fila) + escada U junto ao hall + social no fundo

**Térreo**
| Ambiente | x | y | m² |
|---|---|---|---|
| Garagem 4 vagas coberta (portão na frente) | 6,39–11,79 | 6,00–16,40 | 56,2 |
| Hall social (porta frontal) | 2,50–6,39 | 6,00–9,60 | 14,0 |
| Escada U (partida e chegada na face y 9,60; área livre x 2,65–4,75 × y 8,40–9,60, no hall) | 2,65–4,75 | 9,60–12,84 | 6,8 |
| Galeria (1,64 m de largura, 12,4 m de comprimento) | 4,75–6,39 | 9,60–22,00 | 20,3 |
| Lavabo | 2,50–4,75 | 12,84–15,04 | 5,0 |
| Escritório (2,25 m de largura) | 2,50–4,75 | 15,04–19,00 | 8,9 |
| Suíte Lourdes: quarto / banho | 6,39–11,79 | 16,40–19,80 / 19,80–22,00 | 18,4 / 11,9 |
| Estar/jantar | 2,50–8,39 | 22,00–30,62 | 50,6 |
| Cozinha / lavanderia (porta externa em x 11,79) / dependência | 8,39–11,79 | 22,00–26,00 / 26,00–28,00 / 28,00–30,62 | 13,6 / 6,8 / 8,9 |

**Superior:** chegada em y 9,60 na frente-esquerda; galeria de ~12 m até os fundos; 2 suítes sobre a garagem e 1 nos fundos sobre a cozinha; cinema sobre a suíte Lourdes.
**Áreas molhadas:** banhos das suítes da frente caem **sobre a garagem** (sem área molhada embaixo); só o do fundo empilha sobre a cozinha.
**Janelas e ventilação:** frente: hall + portão; escritório e suíte Lourdes têm uma fachada só.
**Vãos livres:** galeria–estar, estar–cozinha. Portas: escritório, lavabo, suíte, banhos (privacidade); garagem (segurança).
**Prós:** 4 vagas cobertas (pedido C1); frente divide garagem e hall (regra 12, no limite: 3,89 m de hall).
**Contras:** regra 7: galeria de 12,4 m (térreo e superior). Regra 3: o serviço entra pela garagem e cai na galeria social; a dependência é acessada pela lavanderia (regra 4). Regra 6: banhos sobre a garagem. Escritório de 2,25 m de largura. A garagem consome 56 m² de projeção, e só 1 vaga sai da TO (parecer L277). Risco legal Dec. 3.046 XXIII (parecer L291).
**Esperado na `conferir_layout`:** **grave** "dependência acessada por dentro de outro cômodo" (lavanderia); **grave/aviso** "área molhada do superior sem área molhada embaixo" (2 banhos). Avisos: sem ventilação cruzada no escritório, na suíte Lourdes e na dependência (uma fachada só).

### Partido B (recomendado): frente social + vagas descobertas na faixa lateral direita + escada U atrás do hall + serviço à direita + social no fundo

**Vagas:** 4 descobertas em fila na faixa lateral direita, **x 11,79–14,29, y 6,00–26,00** (4 × 5,00), entrada pelo frontal só como passagem (02_v8 L89). Fora da projeção. **Pendente — dono Kelsen** (o XXII veda só o frontal: "excetuada aquela do afastamento frontal mínimo", ERRATA etapa_01 L15; a leitura de que a lateral é área livre é minha). Vaga presa em fila e "a": pendente — dono Kelsen/Hely. Pavimento de ~50 m² contra a folga de 159,24 (anexo v8 L158). Ou piso drenante: pendente — dono Glaziou/Kelsen. Depende de demolir a edícula (x ≈ 13,49) e de uma árvore não ficar em x 11,79–14,29 (T11).

**Térreo**
| Ambiente | x | y | m² | Acesso / janela |
|---|---|---|---|---|
| Escritório | 2,50–6,40 | 6,00–10,20 | 16,4 | porta para o hall (acústica, atendimento); janelas frente + esquerda |
| Hall social | 6,40–9,90 | 6,00–10,20 | 14,7 | **porta social na fachada frontal** (y 6,00) |
| Lavabo | 9,90–11,79 | 6,00–8,40 | 4,5 | porta para o hall; janela frente |
| Armário de casacos | 9,90–11,79 | 8,40–10,20 | 3,4 | hall |
| Área livre de partida (é hall) | 8,10–10,20 | 10,20–11,40 | 2,5 | nada abre nela |
| **Escada U** | 8,10–10,20 | 11,40–14,64 | 6,8 | lance 1 x 8,10–9,10 sobe para +y; patamar no fundo; lance 2 x 9,20–10,20 chega em y 11,40 olhando para a frente; armário sob o patamar |
| Galeria | 6,40–8,10 | 10,20–17,40 | 12,2 | liga o hall ao jantar por **vão livre** (y 17,40) |
| Banho acessível + closet Lourdes | 2,50–6,40 | 10,20–13,20 | 11,7 | pelo quarto; janela esquerda |
| Quarto Lourdes | 2,50–6,40 | 13,20–17,40 | 16,4 | porta na galeria (x 6,40, y ≈ 15,5); cabeceira na parede y 17,40 (prumada na y 13,20, oposta) |
| Despensa | 10,20–11,79 | 10,20–14,64 | 7,1 | porta para a lavanderia (y 14,64) |
| Lavanderia = **entrada de serviço** | 9,40–11,79 | 14,64–17,40 | 6,6 | porta externa em x 11,79 (faixa das vagas); janela |
| Circulação de serviço | 8,10–9,40 | 14,64–21,40 | 8,3 | lavanderia → dependência → cozinha |
| Dependência (quarto) | 9,40–11,79 | 17,40–20,00 | 6,2 | porta na circulação de serviço; janela x 11,79 |
| Banho da dependência | 9,40–11,79 | 20,00–21,40 | 3,3 | pelo quarto; janela |
| Cozinha | 8,10–11,79 | 21,40–25,00 | 13,3 | vão livre para o jantar (x 8,10); janela x 11,79 |
| Jantar | 2,50–8,10 | 17,40–25,00 | 42,6 | janela esquerda; integrado |
| Estar | 2,50–11,79 | 25,00–30,62 | 52,2 | janelas fundos + 2 laterais (cruzada) |
| Varanda gourmet (externa, regime pendente — Kelsen) | 2,50–11,79 | 30,62–35,00 | 40,7 | — |
| **Soma do volume** | | | **≈ 228,2** (≈ 228,72 com paredes) | |

**Superior**
| Ambiente | x | y | m² | Observação |
|---|---|---|---|---|
| Suíte 1: quarto / closet / banho | 2,50–8,10 / 8,10–9,90 / 9,90–11,79 | 6,00–10,20 | 23,5 / 7,6 / 7,9 | banho **sobre o lavabo**; porta do quarto no hall (y 10,20); cabeceira na parede x 8,10; janelas frente + esquerda (cruzada) |
| Hall de chegada (área livre x 9,20–10,20 × y 10,20–11,40) | 6,40–10,20 | 10,20–11,40 | 4,6 | vão da escada x 8,10–10,20 × y 11,40–14,64 inteiro na circulação |
| Galeria | 6,40–8,10 | 11,40–22,40 | 18,7 | ~11 m (aviso, regra 7) |
| Suíte 2: banho / quarto | 2,50–6,40 | 10,20–13,20 / 13,20–17,40 | 11,7 / 16,4 | banho **sobre o banho de Lourdes**; cabeceira na parede y 17,40 |
| Cinema (+ sala técnica x 10,20–11,79 × y 10,20–14,64) | 8,10–11,79 | 14,64–21,40 | 24,9 + 7,1 | porta acústica na galeria; janela x 11,79 |
| Área a decidir (sala íntima/estudo) | 2,50–6,40 | 17,40–22,40 | 19,5 | **pendente — dono Cliente (P-l)** |
| Suíte 3: banho / closet / quarto | 8,10–11,79 / 8,10–11,79 / 2,50–8,10 | 21,40–24,20 / 24,20–25,80 / 22,40–27,40 | 10,3 / 5,9 / 28,0 | banho **sobre a cozinha**; porta no fim da galeria (y 22,40); cabeceira na parede y 22,40 |
| Fundo: pé-direito duplo do estar ou varanda superior | 2,50–11,79 | 25,80/27,40–30,62 | ≈ 35,8 | pedido de 7 m (Rodrigo) e "terraço sobre laje": **pendente — dono Lúcio/Kelsen** |

**Molhadas empilhadas:** P1 à direita (lavabo → banho S1; cozinha → banho S3; lavanderia e dependência embaixo do cinema, seco sobre molhado). P2 à esquerda (banho Lourdes → banho S2). Duas prumadas: motivo, a suíte de Lourdes precisa de banho junto ao quarto do lado das janelas. Nenhuma prumada atrás de cabeceira.
**Vãos livres:** galeria–jantar, jantar–cozinha, jantar–estar, estar–varanda. **Portas com motivo:** porta social e de serviço (segurança); escritório (acústica, atendimento); lavabo, banhos, quartos (privacidade); cinema (acústica); despensa (guarda).
**Prós:** regra 12 (frente = hall + escritório + lavabo, nenhuma garagem); regra 3 (serviço separado, lavanderia → cozinha); regra 2 (a visita só toca a galeria); regra 4 e 5 (tudo por circulação, toda suíte com banho, lavabo no térreo); regra 6 (3 banhos superiores sobre molhado); Skill de escada regras 1, 5, 6 e 7 (partida e chegada em hall, perto mas não de frente para a porta da rua; vão inteiro em circulação; nenhuma porta na área livre); Skill de escada regra 9 (armário e despensa embaixo); garagem fora da projeção (+56 m² de programa em relação ao A).
**Contras:** regra 7 e Skill de escada regra 4: escada perto da frente, galeria superior de ~11 m. Regra 9: quarto Lourdes, S2, cinema e dependência com uma fachada só (lote de 9,29 m). Vagas em fila e descobertas. Três dependências externas (Kelsen, edícula, T11). Em H1 (y ≤ 22) perde-se cozinha, jantar, estar e S3: precisa de outro partido (o programa não cabe em H1 de qualquer forma, 297,28 m²).
**Esperado na `conferir_layout`:** **0 grave.** Avisos esperados: "sem ventilação cruzada" no quarto Lourdes, na S2, no cinema, na dependência e, talvez, no jantar. Motivo: uma fachada só no lote estreito. O jantar ventila pelo estar e pela cozinha integrados. Mitigação a estudar: bandeira ventilada nas portas + janela alta/zenital na galeria (pendente — dono Oscar/Lúcio). Possível aviso na sala técnica do cinema (sem janela, não é permanência).

### Partido C: pátio central + vagas descobertas na lateral + escada U no volume da frente + cozinha voltada ao pátio

Dois volumes ligados por galeria envidraçada. Volume da frente y 6,00–18,00 (111,5); galeria x 6,40–8,10 × y 18,00–22,00 (6,8); pátios descobertos x 2,50–6,40 e 8,10–11,79 × y 18,00–22,00 (≈ 30,4); volume do fundo y 22,00–33,89 (110,4). Projeção ≈ 228,72; fundo ≤ 35,00 ✓.

**Térreo:** frente igual ao B (escritório, hall, lavabo, armário em y 6,00–10,20); circulação x 6,40–11,79 × y 10,20–13,00; **escada U** x 8,10–10,20 × y 13,00–16,24 (partida e chegada em y 13,00; área livre y 11,80–13,00 na circulação); suíte Lourdes x 2,50–6,40 (banho y 10,20–13,20, quarto y 13,20–18,00, janelas esquerda + pátio = cruzada); depósito x 10,20–11,79 × y 13,00–18,00. Fundo: jantar x 2,50–7,00 × y 22,00–27,00 (22,5); cozinha x 7,00–11,79 × y 22,00–26,00 (19,2, janelas pátio + direita); lavanderia x 9,40–11,79 × y 26,00–27,80 (porta externa para a faixa); dependência x 9,40–11,79 × y 27,80–31,80 (6,2 + 3,3); estar x 2,50–9,40 × y 27,00–33,89 (≈ 52, fundos + esquerda + pátio).
**Superior:** S1 na frente (banho sobre o lavabo); chegada em y 13,00 (área livre x 9,20–10,20 × y 11,80–13,00); S2 x 2,50–6,40 (banho sobre o de Lourdes, quarto com janelas esquerda + pátio); passarela x 6,40–8,10 sobre a galeria; no fundo, cinema x 2,50–6,40 × y 22,00–27,00 e S3 (banho x 8,10–11,79 × y 22,00–24,40 sobre a cozinha; quarto x 6,40–11,79 × y 24,40–29,00); resto do fundo, área a decidir (pendente — Cliente).
**Prós:** regra 9 (pátio dá duas fachadas aos cômodos do meio: Lourdes, S2, jantar e cozinha com ventilação cruzada); regra 6 (3 banhos sobre molhado); frente social (regra 12); o pátio pode contar como permeável (ajuda a SMD; pendente — Kelsen).
**Contras:** regra 4: dependência acessada pela lavanderia. Regra 3: o serviço só chega à cozinha pelo fundo. Mais fachada e galeria envidraçada (custo; Villaça). O volume do fundo inteiro fica em y > 22: **pior partido em H1** (parecer L273). Usa o envelope até y 33,89.
**Esperado na `conferir_layout`:** **grave** "dependência acessada por dentro de outro cômodo" (corrigível com 1,00 m de circulação de serviço, à custa do estar). Avisos: S3 e cinema com uma fachada só.

### Recomendado: Partido B

**Motivo:** é o único sem grave esperado. Também entrega as regras 2, 3, 4, 5, 6 e 12 ao mesmo tempo e tira as vagas da projeção. O custo é uma galeria superior longa e ventilação cruzada parcial, e os dois ficam registrados como aviso. Do C, o pátio entra como melhoria possível se H0 for confirmado e Kelsen admitir o pátio como permeável. Antes de modelar: resposta de Kelsen (vaga lateral), decisão do cliente (edícula) e T11 (árvores). Sem essas três, o B fica como hipótese.

**Lacunas desta rodada:** a `conferir_layout` existe no build v63 (status), mas **não está na minha lista de ferramentas**: os resultados acima são previsão, não saída da ferramenta. Não há imagem dos partidos: proibido escrever no Revit nesta rodada, e não tenho outra ferramenta de desenho. Itens (c)/(h) do meu checklist (gráfico): **não cumpridos**. Perspectiva: sem ferramenta para criar ou ajustar vista 3D, e nenhum PNG da "EP. Perspectiva" foi exportado nesta rodada (não pedido).

### Diferença em relação ao layout reprovado (EP_diagnostico_19-10.rvt)
| Erro apontado por Claudemberg | Partido B |
|---|---|
| Frente toda garagem | frente = escritório + hall + lavabo; vagas na lateral |
| Entrada lateral | porta social em y 6,00, com hall |
| Garagem/serviço sem porta | porta de serviço na lavanderia; portas internas listadas |
| Suíte Lourdes pela cozinha | porta na galeria |
| Nenhum banheiro | 4 suítes com banho + lavabo + banho da dependência |
| Suítes por dentro de outro cômodo | todas pela galeria/hall |
| Estar sem janela | estar com 3 fachadas |

### Leitura declarada (nesta execução)
| Fonte | Total | Lido |
|---|---|---|
| Skill `layout-residencial-zoneamento-fluxos` v1.0 | 77 linhas | inteira |
| Skill `posicionamento-escada-residencial` v1.1 | 75 linhas | inteira |
| `etapa_05_estudo_preliminar/enunciado.md` | 142 | inteiro |
| `etapa_01_legal_base/entrega/parecer_legal_base_003.md` | 378 | inteiro |
| `parecer_legal_etapa_01_ERRATA_08_10_2026.md` | 65 | inteiro |
| `etapa_01_legal_base/ERRATA_08-10-2026.md` | 32 | inteiro |
| `etapa_04_briefing/entrega/v4/02_planilha_ambientes_003_v4.md` | 62 | inteiro |
| `etapa_03_levantamento/entrega/v8/01_…_v8.md` | — | [parcial: L16–75] + Grep |
| `…/v8/02_relatorio_…_v8.md`, `03_matriz_…_v8.md`, `anexo_contas_003_v8.md` | — | só Grep (linhas citadas acima) |
| Revit `EP_diagnostico_19-10.rvt` | — | status, níveis, 20 paredes (só leitura) |
Nenhum PDF de lei foi aberto: artigos citados **via parecer [nv]**. Skills `arquitetura-nbr9050-acessibilidade`, `coe-lc198-…` e `vaga-estacionamento-…` não lidas nesta execução: "atende" de acessibilidade, iluminação e vaga **não declarado**.

---

## Partido B — correções G1–G3

**Oscar | 19/10/2026 (noite, 5) | caso fictício | modelado em `EP_layout_partidoB.rvt` (H0).** Nomes do modelo: a suíte de Lourdes passou a ser **SUITE 1 / BANHO S1** (térreo); as superiores são SUITE 2 (frente), SUITE 3 (esquerda), SUITE 4 (fundos). Níveis: **0,30 / 3,45 / 6,60** (decisão de Claudemberg de 19/10/2026; encerra a divergência da L37).

### Layout modelado (H0), face a face aproximada pelos eixos
**Térreo:** ESCRITORIO x 2,50–6,40 × y 6,00–10,20 · HALL x 6,40–11,79 × y 6,00–10,20 (menos o LAVABO x 9,90–11,79 × y 6,00–8,40) · CIRCULACAO (galeria) x 6,40–8,10 × y 10,20–17,40 + nicho da escada x 8,10–11,79 × y 10,20–12,60 · BANHO S1 x 2,50–6,40 × y 10,20–13,20 · SUITE 1 x 2,50–6,40 × y 13,20–17,40 · SERVICO/LAVANDERIA x 8,10–11,79 × y 12,60–15,00 (absorve a despensa) · CIRCULACAO de serviço x 8,10–9,40 × y 15,00–21,40 · DEPENDENCIA x 9,40–11,79 × y 15,00–19,20 · BANHO DEP y 19,20–21,40 · COZINHA x 8,10–11,79 × y 21,40–25,00 · JANTAR x 2,50–8,10 × y 17,40–25,00 · ESTAR x 2,50–11,79 × y 25,00–30,62.
**Superior:** SUITE 2 x 2,50–8,10 × y 6,00–10,20, CLOSET x 8,10–9,90, BANHO S2 x 9,90–11,79 · CIRCULACAO x 6,40–8,10 × y 10,20–22,40 + escada x 8,10–11,79 × y 10,20–12,60 · BANHO S3 x 2,50–6,40 × y 10,20–13,20, SUITE 3 y 13,20–17,40 · cinema x 8,10–11,79 × y 12,60–21,40 (sem ambiente: nome fora da lista) · área a decidir x 2,50–6,40 × y 17,40–22,40 (sem ambiente: nome fora da lista; pendente — Cliente, P-l) · BANHO S4 x 8,10–11,79 × y 21,40–24,20 (sobre a cozinha), CLOSET y 24,20–27,00 · SUITE 4 em L: x 2,50–8,10 × y 22,40–27,00 + x 2,50–11,79 × y 27,00–30,62 (55,25 m²; o fundo é o lugar do pé-direito duplo pedido, pendente — Lúcio/Kelsen).

### G1 — variante H1 (y ≤ 22,00)
Fonte: enunciado L40, L50–51, L68; parecer Legal L273 ("variante H0 e uma H1, mas sem prometer a H0"). Envelope H1: 9,29 × 16,00 = 148,64 m² de projeção (L19). **Não prometo H0:** o modelo é H0 porque foi pedido assim; a H1 é a que se apresenta como base segura.

| Ambiente do B (H0) | Área H0 (modelo, m²) | Em H1 | Como fica em H1 |
|---|---|---|---|
| Escritório, hall, lavabo | 14,61 / 16,43 / 3,62 | cabe | igual (y 6,00–10,20) |
| Escada + galeria térreo | 19,18 | cabe | igual |
| Suíte 1 + banho (Lourdes) | 14,88 + 10,47 | cabe | igual |
| Serviço/lavanderia, circulação de serviço | 7,89 + 7,36 | cabe, encurtada | circulação até y 21,40 |
| Dependência + banho | 8,77 + 4,44 | cabe | igual (y até 21,40) |
| Jantar | 40,04 | **parcial** | x 2,50–8,10 × y 17,40–22,00 ≈ 25,8 m² (bruto), vira estar/jantar conjugado |
| Cozinha | 12,05 | **sai do lugar** | vai para x 8,10–11,79 × y 21,40–22,00? não cabe (0,60 m): precisa trocar dependência por cozinha (y 15,00–21,40) e a dependência **sai** |
| Estar | 48,50 | **sai** | junta ao jantar (≈ 25,8 m² para estar + jantar) |
| Varanda gourmet | 40,7 (estudo) | **sai** | sem área livre em y > 22 |
| Superior: Suíte 2, closet, banho S2, Suíte 3 + banho | 21,37 + 6,56 + 6,62 + 14,88 + 10,47 | cabe | igual |
| Cinema | ≈ 30 (bruto) | **parcial** | y 12,60–21,40 cabe; vira suíte 4 reduzida ou cinema, não os dois |
| Área a decidir | ≈ 19,5 (bruto) | cabe | vira banho/closet da suíte 4 |
| Suíte 4 + banho S4 + closet | 55,25 + 9,18 + 9,18 | **sai** | substituída como acima |
| **Soma de projeção** | 228,72 | **148,64** | perda de 80,08 m² de projeção por pavimento (≈ 160 m² construídos) |

**Resumo H1:** fica a frente inteira (social, Lourdes, escada); saem estar separado, varanda gourmet, dependência (ou cozinha no lugar dela) e uma suíte superior (3 suítes no total, não 4). Construída máxima H1 297,28 m² (enunciado EP L32). Decisão do que sacrificar: **Cliente (P-l)**, não eu. Não modelada (o pedido era H0).

### G2 — área livre de partida dentro de circulação
Escada nova: pegada **x 8,10–11,62 × y 10,35–12,45** (saída da `criar_escada`). Partida **x 6,90–8,10 × y 10,35–11,35**, ambiente **CIRCULACAO** (galeria, x 6,475–8,025 face a face), que se abre sem parede para o HALL em y 10,20 (linha de separação 450861) e tem porta para a SUITE 1. Chegada no superior **x 6,90–8,10 × y 11,45–12,45**, ambiente CIRCULACAO do superior (4 portas). Nenhuma parede, porta ou vão nas duas áreas (conferido pela ferramenta e pela imagem).

### G3 — quem desce não chega de frente para a porta da rua
Comparação (Skill de escada §4):

| | Posição 1 (Lúcio): U girado, lances em x, partida/chegada na face x 8,10 | Posição 2: U em y no fundo da galeria (x 8,10–10,20 × y 17,40–20,64), partida para o jantar |
|---|---|---|
| Quem desce o último lance olha para | **oeste** (parede da galeria / Suíte 1); a porta social (y 6,00) fica à esquerda, de lado | norte (jantar): longe da porta, mas desce dentro do social |
| Partida/chegada | galeria, a 1,0 m do hall | jantar/galeria: área livre invade o jantar |
| Vão no superior | inteiro no núcleo de circulação | cai sobre o cinema/serviço: obriga a deslocar a galeria |
| Galeria superior | mesma (~11 m, aviso regra 7) | encurta 3 m |
| Custo | despensa absorvida pela lavanderia; lavabo mantido | desmonta a faixa de serviço (dependência perde lugar) |

**Escolhida: Posição 1.** Motivo: resolve a regra 5 sem tirar a escada do núcleo de circulação nem mexer no serviço. Detalhe: virei para a **esquerda** (lance 1 ao sul, y 10,35–11,35; lance 2 ao norte, y 11,45–12,45) para a chegada no superior ficar a 1,25 m da parede y 10,20 e da porta da Suíte 2.

**Desvio de espelhos:** pedido 18 × 0,175. A ferramenta recusou: "o tipo 'ESCADA PROJETO' não aceita: espelho 0,175 m > máximo do tipo 0,170 m". Com 19 × 0,1658 (10 + 9) recusou: "área livre de chegada (x 7,18–8,38, y 11,45–12,45 em 'Páv. Superior') cai dentro do vão da escada" (o lance de 9 termina 0,28 m antes). Ficou **20 × 0,1575, piso 0,28, lances 10 + 10**, conforto 59,5 cm (abaixo da faixa 63–64 usual: pendente — Lúcio decide se troca o tipo ou aceita). Não desliguei conferência; folgaVao 0,05.

### Vãos pedidos (para Wallenberg; não criei nenhum)
| # | wallId | Pav. | Centro {x,y} | Largura | Altura | Base | Motivo |
|---|---|---|---|---|---|---|---|
| V1 | 450797 (y 17,40) | térreo | (7,25; 17,40) | 1,30 | 2,10 | 0,00 do Páv. térreo | galeria → jantar (visita chega ao social); faces 6,475/8,025 → folga 0,125 cada lado |
| V2 | 450795 (x 8,10) | térreo | (8,10; 23,20) | 3,00 | 2,10 | 0,00 | cozinha integrada ao jantar; 21,70–24,70, a 0,225 da face da parede y 25,00; trecho y 15–21,40 fica cheio (serviço separado) |
| V3 | 450804 (y 25,00) | térreo | (5,30; 25,00) | 4,00 | 2,40 | 0,00 | jantar ↔ estar integrados; 3,30–7,30 (faces 2,65 e 8,025) |
| V4 | 450808 (x 6,40) | superior | (6,40; 19,90) | 1,20 | 2,10 | 0,00 do Páv. Superior | circulação → área a decidir (sala íntima integrada); 19,30–20,50, faces 17,475 e 22,325 |
Ligações sem parede (linhas de separação, não vão): HALL–CIRCULACAO (450861), LAVANDERIA–circulação de serviço (450863), circulação de serviço–COZINHA (450865). Nenhum vão cruza porta ou janela.

### Ids criados
- Paredes térreo (internas, base 0, topo Páv. Superior, 3,15): 450791–450804. Superior (topo Cobertura, 3,15): 450805–450816. Externas mantidas: 449332–449335 (térreo, base −0,15, 3,30); 449394, 449396, 449398, 449400 (superior, base corrigida de −0,15 para 0,00). Muros 449286–449289 mantidos.
- Portas (18): 450817 social (1,24, segurança), 450819 escritório (acústica/atendimento), 450820 Suíte 1 (0,915), 450821 banho S1 (0,915), 450822 lavabo, 450824 serviço externa, 450826 dependência, 450827 banho dep, 450828 estar→varanda (correr 3,52, fechamento externo), 450829 Suíte 2, 450830 closet S2, 450831 banho S2, 450832 Suíte 3, 450833 banho S3, 450834 cinema (acústica), 450835 Suíte 4, 450836 closet S4, 450837 banho S4. Motivo das demais: privacidade.
- Janelas (22, tipo 341315, peitoril 1,10; banhos 1,50): 450838–450859. Lavanderia sem janela (só a porta externa): aviso.
- Escada 450890 (vão 451009, corrimão 450929); guarda-corpo 451022 criado por mim na borda x 8,05 × y 10,30–11,40 do superior, porque a ferramenta devolveu `guardaCorpoVaoIds: []` e essa borda (sobre o lance 1) ficava aberta.
- Linhas de separação: 450861, 450863, 450865. Ambientes (22): 450866–450880, 450882–450889.

### Níveis relidos (`get_levels`)
Terreno 324604 = 0; Páv. térreo 311 = 0,3; Páv. Superior 694 = 3,45; Cobertura 323714 = 6,6.

### Imagens (abertas com Read nesta execução)
- `D:\011_VITRUVIUS\_imagens\partidoB_19-10\vitruvius_20261019_223440 - Planta de piso - EP- Térreo.png` — rua embaixo. **Visita:** porta dupla no meio da fachada da rua → hall → galeria à esquerda da escada → (vão V1 pedido) jantar → estar no fundo. **Morador:** mesmo hall; a escada ("Acima") nasce na galeria, 1 m depois do hall, e sobe para a direita (leste). **Serviço:** porta na fachada direita, entre a escada e a dependência → lavanderia → corredor de serviço → dependência / cozinha, sem tocar a galeria. Portas da Suíte 1 e do banho visíveis à esquerda. As etiquetas de ambiente não aparecem (não criadas).
- `D:\011_VITRUVIUS\_imagens\partidoB_19-10\vitruvius_20261019_223440 - Planta de piso - EP- Superior.png` — "Abaixo" na galeria; quem chega sai olhando para oeste, na galeria que leva à Suíte 2 (frente), Suíte 3 (esquerda), cinema (direita) e Suíte 4 (fundo). Vão da escada fechado por paredes em três lados e pelo guarda-corpo. Galeria superior de ~11 m: aviso (regra 7).
- Corte pela escada: **não feito** nesta rodada (não pedido no passo 8); pendente para a prova da Skill de escada §4.6.

### Defeitos / recusas Vitruvius
- `criar_escada`: recusas acima (são conferência funcionando, não defeito).
- `criar_escada`: `guardaCorpoVaoIds: []` com uma borda do vão livre sobre o lance 1 → possível defeito (sem código na §8; proposta: D23). Contorno: guarda-corpo manual 451022.
- `operar_elementos apagar` 450648/450652: "Elemento com ID '450648' não encontrado" — já removidos junto com a escada 450613 (não é defeito).

```
## Entrega — Ensaio 003 — EP, Partido B (H0)
Build: 2026-10-19-conferir-layout-v63 (status)
Gate de entrada (0.1): connected true, documentTitle "EP_diagnostico_19-10", isModified false
Passos: [0.4 ✓ salvar_copia → EP_layout_partidoB.rvt 22:27:19] [1 ✓ níveis 0,3/3,45/6,6 relidos] [miolo apagado ✓ contagens antes 20/9/6/19, depois 12/0/0/0] [paredes ✓ 26 internas 3,15] [portas ✓ 18] [janelas ✓ 22] [escada ✓ 450890] [ambientes ✓ 22] [vãos ✗ não criados por ordem — tabela V1–V4] [conferir_layout ✗ não rodada por ordem] [salvar ✓ 22:34:56] [eixos ✗ não feitos] [corte ✗ não feito]
Imagens conferidas (§6): os 2 PNG acima, descritos
Defeitos encontrados (§8): guardaCorpoVaoIds vazio (proposta D23)
Lacunas declaradas (§3): sem ferramenta para criar ou ajustar vista 3D (EP. Perspectiva não exportada); cobertura não refeita; cinema e área a decidir sem ambiente (nome fora da lista)
Pendências: vãos V1–V4 (Wallenberg); conferir_layout (Wallenberg); espelho 0,1575/conforto 59,5 (Lúcio); H1 (Cliente); Kelsen (vaga lateral, gourmet, pé-direito 7 m); edícula; T11; NBR 9050 da Suíte 1 não verificada
Status: PARCIAL
```

---

## Auditoria do Lúcio

**Lúcio (Gestor Arquitetura) | 19/10/2026 | conferência contra as 2 Skills e as fontes, por amostragem com prova. Análise preliminar, sem Gate.**

**Veredito: Passos 1 a 3 aprovados. Passo 4 NÃO aprovado para ir ao modelo. Partido B aceito como direção, condicionado aos itens G1 a G3.**

### Ponto de partida (herança)
Oscar recebeu e leu Legal (Etapa 01 + 2 erratas), Levantamento v8 (parcial + Grep) e Briefing v4 (tabela "Leitura declarada", L175–188). Sem falha de herança. O Levantamento v8 lido só em parte fica como ressalva, não como falha.

### Cruzamento enunciado × entrega
| Exigência | Prova na fonte | Na entrega | Situação |
|---|---|---|---|
| Afastamentos, envelope H0 | enunciado L18–25 | Passo 1 L17–18 | OK |
| Envelope H1 148,64 m² | enunciado L25 | Passo 1 L19 | OK no Passo 1 |
| **Cenários H0 e H1 com o que cabe** | enunciado L40, L50–51, L68; parecer L273: "pode estudar uma variante H0 e uma H1, mas sem prometer a H0" | os 3 partidos só ocupam H0; B perde cozinha, jantar, estar e S3 em H1 (L145) e não tem variante H1 | **NÃO ATENDE (G1)** |
| Déficit 62,56 m², não cortar | Briefing v4 02 L42–43 | L61 | OK, registrado sem corte |
| Metragens "a definir" | Briefing v4 02 L7, L15–29 | L45: áreas de estudo declaradas como hipótese | OK |
| Norte pendente | matriz v8 L34 | L34 | OK, sem orientação inventada |
| Vaga no frontal vedada | ERRATA etapa_01 L15 | B usa faixa lateral, pendente Kelsen (L105) | OK como hipótese |

### Conferência contra a Skill de layout (seção 4) e de escada, no Partido B
- Regras 2, 3, 4, 5, 6, 12 de layout: conferidas na tabela de coordenadas (L110–139). Visita: porta y 6,00 → hall → galeria → jantar, sem íntimo nem serviço. Toda suíte com banho; lavabo no térreo; 3 banhos superiores sobre lavabo, banho de Lourdes e cozinha (L133, L136, L139). **OK.**
- Escada regra 10 (≤ 10 espelhos): 9 + 9 em U (L78). **OK.**
- Escada seção 3 (área livre 1,00 × 1,20 em circulação): chegada x 9,20–10,20 × y 10,20–11,40 dentro do hall superior (L134), OK. **Partida térreo x 8,10–10,20 × y 10,20–11,40 (L114) fica FORA do hall, que termina em y 10,20 (L111).** Ela só toca a galeria em x 8,10. **G2:** o hall do térreo tem de ser redesenhado até y 11,40, ou a área livre deixa de estar "dentro de circulação".
- Escada regra 5 (não de frente para a porta): o lance 2 desce em −y, ou seja, de frente para a porta social em y 6,00 (L111, L115). **L144 declara a regra 5 cumprida, mas não está.** **G3:** reposicionar ou girar a escada, ou escrever o motivo da exceção.
- Regra 9 (ventilação cruzada): 4 a 5 avisos assumidos com motivo (L146). Aceito como aviso. Ressalva: janelas da lavanderia, dependência e cozinha abrem para a faixa de carros (x 11,79). Registrar ruído e gases como aviso.
- Regra 7: galeria superior de ~11 m (L135). Aviso com motivo, aceito.

### Prova (checagem obrigatória item 2)
- `conferir_layout` **não foi rodada**: "0 grave" é previsão de Oscar (L162). Status: **não verificado**.
- **Não há imagem dos partidos** (Skill de layout §5.2–5.3). A rodada dispensou a escrita no modelo, então isso não é falha do Oscar, mas **nenhum partido está aprovado graficamente**.
- NBR 9050 na suíte de Lourdes, iluminação COES e vaga: Skills não lidas (L188). **Não verificado**, nenhum "atende".

### Divergência de dado (minha)
Níveis: meu pedido trazia 0,30 / 3,45 / 6,60 (piso a piso 3,15). O modelo lido diz 0,30 / 3,30 / 6,30 (piso a piso 3,00) (L37). **A origem do 3,15 não está no enunciado** (Grep em `enunciado.md` sem ocorrência). Pendente: Wallenberg/Claudemberg confirmam qual vale. O formato U não muda (L78).

### Para a próxima rodada (conversa nova, com as ferramentas visíveis)
1. **G1:** variante H1 do Partido B (y ≤ 22,00), com quadro do que cabe e do que não cabe.
2. **G2 e G3:** corrigir a área livre de partida e a visada da escada para a porta.
3. Respostas de Kelsen (vaga lateral, fila, "a", gourmet, pé-direito 7 m), do cliente (edícula) e do T11 (árvores).
4. Ler as Skills de NBR 9050, COES e vaga antes de declarar qualquer "atende".
5. Estudo rápido em cópia `…_partidoB.rvt`, imagens das plantas e `conferir_layout` real colada.

---

## Auditoria do Lúcio — Partido B modelado (19/10/2026, noite)

**Veredito: PARCIAL, não aprovado. G1, G2 e G3 atendidos no texto e no modelo. A escada fica pendente (espelho fora do conforto). Os vãos V1–V4 e a `conferir_layout` estão com Wallenberg.** É análise preliminar, sem Gate.

**Herança:** o Oscar leu as 2 Skills, o relatório anterior e a minha auditoria. Não há falha de entrada.

| Item | Prova | Situação |
|---|---|---|
| Documento certo, cópia | status com "EP_diagnostico_19-10" e isModified false; salvar_copia às 22:27:19, salvar às 22:34:56 (bloco de entrega acima) | OK, declarado pelo Oscar; o log não foi relido por mim |
| Níveis 0,30/3,45/6,60 | get_levels colado: 311 = 0,3; 694 = 3,45; 323714 = 6,6 | OK |
| Miolo apagado | contagens antes 20/9/6/19 e depois 12/0/0/0 (paredes/portas/janelas/ambientes) | OK. Escadas e guarda-corpos não foram relistados depois: **não verificado** |
| G1 (H1) | tabela L200–220. Perde 80,08 m² de projeção, com 148,64 = 9,29 × 16,00 ✓. Não promete H0 | OK no texto. Não foi modelado, e a decisão é do Cliente (P-l) |
| G2 (área livre de partida) | partida x 6,90–8,10 (1,20 ✓) × y 10,35–11,35 (1,00 = largura ✓) na CIRCULACAO. Na imagem do térreo, "Acima" aparece na galeria, logo depois do hall | OK |
| G3 (porta da rua) | lances em x: quem desce chega olhando para oeste. Na imagem, a porta da rua fica na fachada de baixo, de lado em relação à escada. Comparei as 2 posições (L228–234) | OK |
| Escada | 20 × 0,1575 = 3,15 ✓; lances 10 + 10 ✓ (≤ 10). Conforto 2 × 0,1575 + 0,28 = **0,595**, abaixo de 0,63–0,64 | **NÃO aceito como final.** A solução é trocar o tipo para admitir 0,175 (18 × 0,175, com 2 × 0,175 + 0,28 = 0,63). Isso é mudança de tipo da família, então a decisão fica com Claudemberg, via Wallenberg |
| Portas com motivo | 18 portas, cada uma com motivo (L251) | OK |
| Vãos | tabela V1–V4 (L241–246). Conferi a folga de V1: 7,25 ± 0,65 = 6,60–7,90, dentro das faces 6,475 e 8,025 ✓ | OK como pedido; ainda não foram criados |
| Imagens | abri os 2 PNG. As paredes, as portas e a escada ("Acima" no térreo, "Abaixo" no superior) batem com a descrição | OK. **Ressalva:** as plantas estão sem etiqueta de ambiente, então pela imagem não dá para conferir os nomes |
| Guarda-corpo manual 451022 | contorno de `guardaCorpoVaoIds: []` | Aceito. O D23 entra na tabela da Skill depois de reproduzido |
| Externas do superior com base passada para 0,00 | a R5 vale só para o térreo | Aceito. A mudança foi registrada |

**Pendências:**
- **Wallenberg:** criar V1–V4 e rodar a `conferir_layout`.
- **Claudemberg:** decidir o tipo da escada (espelho 0,175).
- **Oscar, na próxima rodada:** corte pela escada (Skill de escada §4.6), etiquetas de ambiente na vista, ambientes do cinema e da área a decidir (nome fora da lista: pedir à conferência que aceite), janela da lavanderia, e reler escadas e guarda-corpos.
- **Vêm de antes:** Kelsen (vaga lateral, gourmet, pé-direito de 7 m), edícula, T11 e NBR 9050 da Suíte 1.

