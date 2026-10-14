# Treino 14/10/2026: checklist obrigatório aplicado à minha entrega v4 da Etapa 04 (Briefing), Ensaio 003

**Oscar (Assisted) | pedido de Lúcio (origem: Claudemberg via Wallenberg) | 14/10/2026.** Exercício, não entrega. A v4 não foi alterada; nada foi escrito em `entrega\`.
**Checklist usado:** `01_CEO\Gestores\Lúcio (Arquitetura)\Agentes\Oscar\checklist_entrega_oscar.md` (5 partes, a–e).
**Convenção:** caminhos relativos a `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\CONSTRUCAO_DO_ZERO\01_CEO\Casos_TESTE\ensaio_003\`. "L" = linha do arquivo como saiu no Read desta execução. Abreviações: **P01** = `etapa_01_legal_base\entrega\parecer_legal_base_003.md`; **ERR** = `etapa_01_legal_base\ERRATA_08-10-2026.md`; **V9** = `etapa_02_viabilidade\entrega\v9\pre_estudo_viabilidade_003_v9.md`; **LP1/LP2/LP3/LAX** = Etapa 03 v8 Peça 1, Peça 2, Peça 3 e `anexo_contas_003_v8.md`; **v4-01 … v4-06** = arquivos 01 a 06 de `etapa_04_briefing\entrega\v4\`; **v3-01/v3-05** = corpo e contas da v3; **ENU** = `etapa_04_briefing\enunciado.md`.

---

## (a) Herança — tudo o que já foi aprovado antes

**Fato de partida (prova):** v4-06 L51: "Nenhum parecer da Etapa 01 (Hely), nenhum Regramento do condomínio, nenhuma Viabilidade (Villaça v9) e nenhuma errata: o que sei delas vem do Resumo do enunciado". O checklist exige o contrário ("Abra o arquivo aprovado; não copie do enunciado"). Por isso a coluna "origem" abaixo foi aberta agora, nesta execução, e a coluna "v4" mostra o que a v4 fez com cada item.

### (a.1) Etapa 01 — parecer legal base (P01) e errata (ERR)

| # | Parâmetro | Origem aprovada (arquivo + linha) | Valor e regime | Onde está na v4 | Se não está / problema |
|---|---|---|---|---|---|
| 1 | Área de cálculo | P01 L23, L54-56 | 571,80 m² (terreno); título 600,00; afastamentos medidos do muro do Lote 16 | v4-01 L30; v4-05 E-1 (L10-15) | Está a área. **Falta** "afastamentos medidos a partir do muro do Lote 16" (P01 L56, L263; LAX L328). Estava na v3 (v3-01 L42, F4). Regressão |
| 2 | Zona/subzona | P01 L24 | ZPP "A-ENS" | só "ZE-5" no status da alt. A (v4-01 L81) | Sem linha de premissa. Não citada como herança |
| 3 | Uso | P01 L25 | unifamiliar | implícito | Sem linha. Não é falha grave |
| 4-5 | CAB = CAM = 1,0, sem OODC | P01 L26-27 (LC 270 Art. 345 §3º, p. 122) | índice | v4-01 L114; v4-04 L18 | Citado como "Viabilidade (Resumo)", não como Etapa 01 nem com o artigo |
| 6 | **ATE máxima** | P01 L28, L66, L74 | **571,80 m² (CA 1,0 × 571,80)**; sobra de ~114 m² de ATE que não cabe no volume | **não está** | **Falta.** O 520 é testado só contra o teto volumétrico; a v4 não diz que a ATE (571,80) não é o limite que trava. Motivo: Etapa 01 não aberta |
| 7 | TO | P01 L29, L67-68 | Prefeitura (RIU) **50%** = 285,90 m² (P); condomínio **40%** = 228,72 m² (P), prevalece | v4-01 L32 (só 40%); v4-05 E-8 (50% só como "sensibilidade, não é premissa") | **Falta a TO municipal de 50% como herança.** Isso pesa na SMD (item 14) |
| 8 | Gabarito | P01 L30 | 2 pavimentos | v4-01 L34 | ok (fonte: Resumo) |
| 9 | Altura | P01 L31 | 8,50 m da soleira | v4-01 L34 | ok (fonte: Resumo) |
| 10 | Cobertura | P01 L32, L143, L267 | só técnica; terraço vedado; telhado verde admitido (COES Art. 10 p.ú.) | v4-01 L37; v4-04 M-05 L17 | Parcial: telhado verde e Glossário "TELHADO" ausentes |
| 11 | Afastamento frontal | P01 L33 | Prefeitura 5,00; condomínio **6,00** (adotado) | v4-01 L35 | ok (fonte: Resumo). Prefeitura 5,00 ausente |
| 12 | Afastamentos laterais | P01 L34 | COES 1,50; condomínio **2,50** | v4-01 L35; v4-05 E-14 L104 | ok |
| 13 | Fundos | P01 L35 | 5,00 m + faixa APP se confirmada | v4-01 L35 | ok |
| 14 | **Permeabilidade / SMD** | P01 **L36**, L71 | **25% do lote = 142,95 m² (Pe)**, RIU; nota: "Mecanismo geral da LC 270 (SMD = 20% da área livre da TO máx.) **daria 10%**" | v4-01 L17, L36, L126; v4-05 E-6 a E-10 | **Herança mal lida.** (i) v4-05 L62: "A % (25%) não está escrita no Resumo" — está em P01 L36. (ii) O "10%" não é um número solto do enunciado: é a conta do Hely com a TO **municipal** de 50% (0,20 × 0,50 = 10%). A v4 apresenta "Leitura A (enunciado)" e "Leitura B (TO 40%)" como fontes independentes; a origem real (P01 L36) não aparece. Não decido qual TO vale (é Kelsen), mas a pergunta P-SMD tinha de citar P01 L36 e P01 L29 |
| 15 | Subsolo / **escavação** | P01 L37, L266; LAX I-1 L331 | subsolo vedado; **escavação ≤ 1,20 m**; piscina ≤ 1,60 m | v4-01 L37, L102 (subsolo); v4-05 E-18 (1,60) | **Falta "escavação ≤ 1,20 m"** em toda a v4 |
| 16 | Varandas | P01 L38, L268 | não computam (COES Art. 8º §4º; **LC 270 Art. 347 VI, Art. 350 I**); sem balanço sobre os 6 m frontais | v4-01 L93-97 | Parcial: v4-01 §4 L93 cita só COES §4º; LC 270 Art. 347 VI não aparece |
| 17 | Edícula | P01 L39, L128 | conservador: computa ATE e TO (Dec. 3.046 XV) × LC 270 **Art. 347 V** / 350 IV | v4-01 L101; v4-05 E-14 | Parcial: só Art. 350 IV; Art. 347 V ausente |
| 18 | Corpo hídrico | P01 L40, L87-96 | H0/H1/H2/H3 não resolvidos | v4-01 L47-63 | ok |
| 19 | **Cota de soleira** | P01 L41 | +3,20 m (referência do condomínio), **não confirmada**; Art. 458 (cota < 3 m exige avaliação técnica) | **não está** | **Falta.** Estava na v3 (v3-01 L56, P1; v3-05 E-21 topo +11,70). Regressão |
| 20 | APAC | P01 L42 | não | não está | Omissão menor |
| 21 | AEI / áreas protegidas | P01 L43 | não verificado (c) | não está | Omissão |
| 22 | **Aprovação prévia do condomínio** | P01 L44 | obrigatória antes do protocolo; 30 dias; taxa (Art. 9º) | só para a edícula (v4-01 L113) | Parcial: não aparece como premissa geral de prazo |
| 23 | Remoção de árvore | P01 L45 | licença (LC 270 Art. 278 XIV) + condomínio (Art. 12) | v4-01 L115; v4-04 M-11 | ok |
| 24 | **Alteração do Regramento** | P01 L46, L135 | 2/3 = **31 de 46** condôminos, assembleia própria | **não está** | **Falta.** É a resposta direta ao "assembleia de dezembro" (M-04). v3-01 L100 tinha "2/3 (Art. 21)". Regressão |
| 25 | Teto volumétrico | P01 L69-70 | 457,44 m² (C) | v4-01 L33 | ok (fonte: Resumo) |
| 26 | Cenário título | P01 L66-71, L244 | ATE 600; projeção 240; teto **480**; permeável 150; envelope 290 (P01 L83) | v4-05 E-9 (só SMD a 600) | **Falta o cenário 600 inteiro** (teto 480, envelope 290, permeável 150) |
| 27 | Mais-Valerá (P4) | P01 L148-161 | não confere por 4 razões: condomínio; **30% só à vista até 01/12/2026**; **60x com 30% não alcança AP4**; **licença só após pagamento total (LC 281 Art. 20)** | v4-01 L114; v4-04 M-06 L18 ("Não confere (Etapa 03, parecer P4)") | **Razões não escritas.** Rodrigo diz "paga até o fim do ano": a data de 01/12/2026 responde direto. v3-01 L104 e v3-05 E-28 tinham. Regressão |
| 28 | Edícula sem direito adquirido | P01 L120, L124-127 | fora do Habite-se de 1999; Art. 38 da LC 274 revogado; CC 1.301 | v4-04 M-03 (só "parecer de demolição") | Parcial: "fora do Habite-se" estava na v3 (v3-01 L98) e saiu |
| 29 | Subsolo: NA e argila | P01 L135 | NA 0,90; argila mole até 9 m; rebaixamento INEA | v4-04 M-04 L16 (não cita) | Falta |
| 30 | Semienterrado = subsolo | P01 L274 | COES Glossário p. 29 | não está | Falta |
| 31 | Lago | P01 L166-172 | 1 ha; maré; com APP **sai da LMS simplificada** (Dec. 51.503 Art. 27 p.ú.) | v4-01 L115; v4-04 M-10 | Parcial: efeito na LMS ausente |
| 32 | Prazo | P01 L188-190 | licença 30/06/2027 apertada; obra maio/2027 alto risco | v4-04 P-14 L45 | ok |
| 33 | Ordem demolição × obra | P01 L294 | TRAVA POP-LEGAL-03 §5 | v4-01 L141 | ok |
| 34 | Como o condomínio mede a TO (e sobre 600 ou 571,80) | P01 L295 | risco aberto | v4-01 L51 (condição 1) | Parcial: "sobre 600 ou 571,80" ausente |
| 35 | PRPA não definido | P01 L285 | quem assina segue quem produz | não está | Falta (RRT/ART: minha regra manda sinalizar) |
| 36 | Garagem coberta ZPP | P01 L144, L291 | Dec. 3.046 XI e XXIII aplicáveis ou não a unifamiliar | v4-01 L82 (XXIII × XI em aberto) | ok |
| E1 | Errata: XXII | ERR L15 | estacionamento em área livre "excetuada aquela do afastamento frontal mínimo" | v4-01 L81; v4-05 E-22 | ok |
| E2 | Errata: XXIII a | ERR L16 | garagem coberta em subsolo com exclusão do frontal | v4-06 L137 (tabela de cópias) | Não aparece no corpo nem na matriz como herança da errata |
| E3 | Errata: conflito a decidir | ERR L22, L30 | COES **Art. 28 IV** e LC 270 Art. 363 §2º XII × Dec. 3.046 XXII/XXIII a; decide o Gate | v4-01 L81 (só Art. 363 §2º XII) | COES Art. 28 IV ausente |
| E4 | Errata: XXIII b não lido | ERR L31 | limite declarado | não está | Falta registrar |

### (a.2) Etapa 02 — Viabilidade v9 (V9)

| # | Parâmetro | Origem (linha) | Valor e regime | Onde está na v4 | Se não está |
|---|---|---|---|---|---|
| V1 | S1 | V9 L27, L38 | 457,44 C; 500–520 Co de trabalho | v4-01 L33; v4-04 P-01 | ok, mas a faixa **42,56–62,56 de não computável** de S1 (LAX C-7 L81) não aparece; v3-05 E-8 tinha |
| V2 | **S2** | V9 L28, L39 | **480 C; 523–543 Co** (divisa regularizada) | **não está** | **Falta em toda a v4** |
| V3 | S3/H1 | V9 L29, L40 | 297,28 C; 340–360 Co | v4-05 E-13 | ok |
| V4 | Divergência V9 × conta | V9 **L206**: "H1 não cabe 520 m² (falta 160 m²)" | 160 é computável (457,44 − 297,28 = 160,16, LAX L38); 222,72 é construída | não registrada | **Falta.** Dois números para "falta em H1" sem rótulo de regime na fonte |
| V5 | Custo S1 | V9 L14, L58 | R$ 2,49–3,03 mi | não está (só remissão C-16 em v4-04 P-16) | Falta |
| V6 | **Fundação especial** | V9 L16, L98, L139-143 | NA 0,90; argila mole 2,5–9 m; estacas 12–20 m; ~R$ 150–300 mil [NC] | não está | **Falta.** Afeta piscina e prazo |
| V7 | Teto e crédito | V9 L14; LAX C-16 L205 | R$ 4,2 mi = 3,0 crédito + 1,2 próprios; liberação limitada a 60% | v4-04 P-16 L47 | ok (só na matriz) |
| V8 | Divisa vale ~R$ 170–230 mil | V9 L121-124 | — | não está | Omissão (interessa à P-área) |
| V9b | OODC R$ 0 | V9 L26, L126 | — | v4-04 M-06 | ok |

### (a.3) Etapa 03 — Levantamento v8 (LP1, LP2, LP3, LAX)

| # | Parâmetro | Origem (linha) | Valor e regime | Onde está na v4 | Se não está |
|---|---|---|---|---|---|
| L1 | Envelope H0 | LAX C-2 L28-29 | 269,41 P; folga 40,69 | v4-05 E-2, E-5 | ok |
| L2 | Envelope título | LAX C-2 L30; LP3 L16 | 290,00 P; folga 50,00 | não está | Falta |
| L3 | H1 | LAX C-3 L36-38 | 148,64 P; 297,28 C; −80,08; −160,16 | v4-05 E-12 | Parcial: −160,16 (C) não aparece |
| L4 | Fórmulas de garagem | LAX C-4 L54-58 | T, C, G, A | v4-05 E-15 | ok |
| L5 | M-a/M-b/M-c | LAX C-7 L85-92 | quadro de regimes | v4-01 L49-54 | Parcial: M-c não aparece |
| L6 | Alt. A, status verbatim | LAX C-8 L105 | texto obrigatório | v4-01 L81 | ok |
| L7 | Alt. B | LAX C-9 L120-129 | aberta; 2+1 em duas laterais cabe por comprimento | v4-01 L82 | Parcial: a hipótese 2 + 1 (LAX L125) não aparece |
| L8 | Varanda frontal | LAX C-10 L139 | 46,45 m² por pavimento, condicionado | v4-05 E-17 | ok |
| L9 | Folga permeável | LAX C-12 L158 | 159,24 Pe | v4-05 E-10 (159,44, base corrigida) | ok com conta (diferença 0,20 declarada) |
| L10 | **Locação A** | LAX C-12 L162; LP2 L67 | A: 143,95; **folga +1,00** | **não está** | **Falta**; v4-04 P-04 L35 só traz B (+2,05). v3-05 E-17 tinha as duas. Regressão |
| L11 | **Faixa lateral permeável** | LAX C-12 **L165**; LP2 L68 | pavimentar no máximo 0,50 m; **circulação de 1,20 m desqualifica a faixa inteira** | **não está** | **Falta e há contradição:** v4-03 L34 põe o fluxo de serviço numa "lateral útil de 2,50 m (faixa de circulação, COES Art. 29 IV)" sem dizer que isso tira a faixa da conta permeável |
| L12 | H1 permeável | LAX C-13 L180 | 22,79; acesso ≥ 3,80 m esgota | v4-05 E-23 | ok |
| L13 | Edícula | LAX C-14 L187-194 | 1,70; 0,70; CC 1.301; não serve nem como PV | v4-05 E-14 | Parcial: CC 1.301 e PV ausentes |
| L14 | **Altura do topo** | LAX C-15 L199; LP1 L77 | +3,20 + 8,50 = **+11,70** (se soleira +3,20) | não está | **Falta.** Regressão (v3-05 E-21) |
| L15 | Rampa | LAX C-15 L200 | 10% e 0,50 m; NBR 9050 8,33% → 6,00 m | v4-03 L36 (só 10% e 0,50) | Parcial: a conta de 6,00 m (o frontal inteiro) saiu; v3-05 E-26 tinha |
| L16 | NA | LP1 L82 | 0,90 m (5.7) | v4-05 E-18 | ok |
| L17 | **Jardim de chuva** | LP2 L104; LP3 L30 (linha 15) | não recomendado com NA 0,90 | não está | Falta |
| L18 | **Fundações** | LP2 L103; LP3 L31 (linha 16); LAX I-3 | argila mole; blocos de 1,20 podem passar do NA | não está | Falta. v3-01 L68 (P13) tinha. Regressão |
| L19 | Canteiro | LP2 L29; LP3 L33 (linha 17) | sem a faixa verde, tudo entra pela frente | não está | Falta |
| L20 | Casa de 1998 | LP1 L89 | existente, a demolir, não averbada | só P-demolição (v4-01 L141) | Parcial |
| L21 | Ligação lago–canal | LP2 L101; LP3 L23 | LC 270 Art. 216 V se confirmada | não está | Falta (só "maré e manilha") |
| L22 | Matriz linhas com dono Cliente | LP3 L16-39 | 1, 2, 3, 4, 5, 9, 11, 12, 13, 23, 24 | v4-04 §3 L55-65 | ok (11 linhas) |
| L23 | Linhas sem dono Cliente | LP3 L25 (10 soleira), L30 (15), L31 (16), L33 (17), L34 (19) | pendências de terceiros | v4-04 §4 não traz 10, 15, 16, 17, 19 | Falta (v4-01 §6 também não) |
| L24 | **Pedido E-17 da Etapa 03** | LAX E **L264** | 5.15: R$ 6.300/m²; banco 60%; CAB × CAM | **não está**: v4-04 §2 vai até P-16 (L47) | **Falta 1 dos 17 pedidos herdados** |
| L25 | Divergências do enunciado (D) | LAX D L227-242 | ex.: soleira "atual" é prevista; crédito 3,0 ≠ 4,2 | não retomadas | O ENU da Etapa 04 L21 traz "SMD 10% do terreno (Etapa 01, quadro, item 14)": a v4 não conferiu contra P01 L36 |

**Comparação com a minha versão anterior (v3).** Itens que estavam na v3 e sumiram na v4: F8 pé-direito 2,50/2,20 (v3-01 L46, Skill coe-lc198); P1 soleira +3,20 prevista (v3-01 L56); P13 fundação/sondagem (v3-01 L68); P17 moradores, banheiros e lavabos (v3-01 L72); quadro H0 × H1 por item do programa, com "escritório não cabe sem redistribuir", suíte, piscina (v3-01 L78-90); C2 "2/3 em assembleia" (v3-01 L100); C4 Mais-Valerá com AP4, 01/12/2026 e prazo "fim do ano" (v3-01 L104; v3-05 E-28); "fora do Habite-se" (v3-01 L98); E-8 composição do 520 com a faixa 42,56–62,56 da Viabilidade (v3-05 L43-47); E-17 locação A +1,00 (v3-05 L94); E-21 topo +11,70 (v3-05 L118); E-26 rampa 6,00 m (v3-05 L142); C4 cita a Skill `legal-oodc`. **São 12 regressões.**

**Recebi as entregas aprovadas de todas as etapas anteriores?** Na v4: o caminho estava disponível, mas **não abri** P01, ERR e V9 (v4-06 L51). Não é "não recebi": é "não li". Nesta execução abri todos.

---

## (b) Prova — afirmações de conferência da v4

| Afirmação da v4 | Prova (o que o arquivo mostra) | Veredito |
|---|---|---|
| v4-06 L90: "Nenhum 'atende' de regime foi escrito sem cruzar com a E-13" | v4-01 L60: "Construída máxima: **297,28 m²** (teto computável…)"; v4-01 L16: "A construída máxima é de 297,28 m²". E-13 (v4-05 L90) rotula 297,28 como **C**. v4-01 L14: "a construída que cabe… é de 457,44 m² **computáveis**" | **Falsa.** O mesmo número aparece como construída e como computável |
| v4-06 L146: resíduos de "Anexo 03-E" "foram trocados por 'Etapa 03, Anexo E, item N'" | v4-04 L35 "Anexo E-4"; L39 "Anexo E-8"; L40 "E-9"; L41 "E-10"; L42 "E-11"; L43 "E-12"; L44 "E-13"; L45 "E-14"; L47 "Anexo C-16"; L36 "Anexo C-4"; L15 "Anexo C-14". Todos colidem com E-n do arquivo 05 desta entrega (ex.: v4 E-4 = computável máximo) | **Falsa** (11 células) |
| v4-06 L33-35 (itens 11-13): COES pp. 5, 15, 17; LC 270 pp. 124-126, 130; Dec. 3.046 pp. 2-4 "lidas por página" | v4-06 L39 (c): "Nesta execução não abri nenhum desses dois arquivos nem outro da listagem" | **Contraditória** dentro do mesmo arquivo. Não verifiquei qual das duas é verdade (não abri os PDFs) |
| v4-06 L26-29: 4 Skills "lidas nesta execução" | sem linhas, e versão só para a de vaga | Prova insuficiente pelo checklist (d) |
| v4-05 L62: "A % (25%) não está escrita no Resumo" | ENU L20 não traz 25%, correto; mas P01 L36 traz "RIU: 25% do lote" | Verdadeira sobre o Resumo; mostra que a fonte aprovada não foi aberta |
| v4-01 L17 / v4-05 E-6: "SMD 10% do terreno" atribuído ao enunciado | origem real: P01 L36 ("daria 10%"), conta com TO municipal de 50% (P01 L29) | Origem errada; a divergência "A × B" fica mal posta |
| v4-04 L5: "Etapa 03, Anexo E, item N" é a regra de citação | a própria tabela §2 usa "Anexo E-N" | Regra declarada e não aplicada |
| v4-01 L142 (P-saldo): diferença de 0,20 m² | 302,39 − 302,19 = 0,20; 159,44 − 159,24 = 0,20 (v4-05 L63-65; LAX L150-158) | Confere (conta refeita agora) |
| v4-05 E-7: 0,20 × (571,80 − 228,72) = 68,62 | 571,80 − 228,72 = 343,08; × 0,20 = 68,616 | Confere a aritmética; a premissa de TO não é minha para decidir |
| v4-05 E-12: 520 − 297,28 = 222,72 | refeito: confere | Confere |
| v4-04 §3: "linhas 1, 2, 3, 4, 5, 9, 11, 12, 13, 23, 24" com dono Cliente | LP3 L16-39: confere | Confere |
| Contagem de palavras do corpo ≤ 2.500 | não há ferramenta de contagem nesta execução | **Não verifiquei.** Pendente de Wallenberg |
| Citações verbatim dos PDFs (v4-06 L118-137) | não abri COES, LC 270 nem Dec. 3.046 nesta execução | **Não verifiquei** |

---

## (c) Entregável mínimo do enunciado (ENU L72-83), item por item

| Item (linha) | Atende? | Onde | Forma conferida? |
|---|---|---|---|
| L72 Corpo ≤ 2.500 palavras | **não verificado** | v4-01 | Contagem só com ferramenta: pendente de Wallenberg |
| L73 5.2.1 a) organograma funcional com fluxos | **parcial** | v4-03 §1-§3 | **Não.** Só tabelas. A Skill nbr6492 L33 classifica organograma como "documento gráfico"; o checklist diz "'Gráfico' não é tabela nem ASCII" |
| L74 5.2.1 b) esquemas básicos dos ambientes | **não** | v4-03 §4 (tabela); v4-03 L6 adia "gráficos em escala" para a Etapa 05 | **Não.** Esquema básico não é planta: o adiamento não tem base no "não desenhe planta" do ENU L130 |
| L75 5.2.2 planilha com "a definir" com dono e fonte | atende | v4-02 §1 | Sim; "usuários" de A2 = "a definir (moradores)" e A15 = "—" |
| L76 520 separado em computável e não computável, cada não computável com artigo | **parcial** | v4-01 §4; v4-02 §2 | **Não fecha a soma.** Não traz a faixa da Viabilidade (42,56–62,56, LAX L81). Varandas sem LC 270 Art. 347 VI (P01 L38) |
| L77 Garagem: vaga e manobra separadas, com artigo | atende | v4-01 L71-73 | Sim (COES Art. 29 I, II, IV, p. 15) |
| L78 H0 e H1, o que cabe e o que não cabe | **parcial** | v4-01 §2 | Só o total de 520. O "o que cabe" por item (suíte, escritório, piscina), que a v3 tinha em tabela (v3-01 L78-90), saiu |
| L79 "Cabe" com condições; número com unidade e regime | **parcial** | v4-01 §2 | Condições: sim. Regime: **não** (297,28 e 457,44 trocam de rótulo; ver (b)). v4-01 L55 "81,38 − a m²" e L52 "62,56 − a" sem regime no corpo |
| L80 Matriz pedido × resposta × fonte × dono, uma linha por pedido | **parcial** | v4-04 §1-§2 | Falta o pedido 17 da Etapa 03 (LAX L264). Fontes "Anexo E-N" ambíguas |
| L81 Tabela pergunta × onde está respondida | atende | v4-05 T-1 | Sim |
| L82 Declaração de leitura só do aberto | **parcial** | v4-06 §1 | Contradição interna (L33-35 × L39); Skills sem linha |
| L83 Nenhuma premissa legal reinterpretada | **parcial** | v4-05 E-7 | A "Leitura B" aplica a TO do condomínio (40%) a um artigo que remete à TO do Anexo XXI. A v4 não decide, mas o rótulo "Leitura B (Art. 352)" apresenta a conta como leitura da lei. Kelsen decide |
| ENU L57 corpo: "premissas fechadas" | parcial | v4-01 §1 | Fonte "Resumo do enunciado" em 6 de 10 linhas (v4-01 L32-37), não o arquivo aprovado |
| ENU L101 "Diga o que ficou aberto" | atende | v4-04 §5 | Sim |
| ENU L124 "Conclusão primeiro; contas em anexo numerado" | atende | v4-01 §0; v4-05 | Sim |

---

## (d) Skills e primário

Leitura desta execução: cabeçalho de cada Skill (linhas indicadas). Não li nenhuma inteira.

| Skill (ENU L107-116) | Versão (cabeçalho) | Lida agora (linhas) | Na v4 (v4-06 L26-29) | Primário lido agora |
|---|---|---|---|---|
| `nbr6492-2021-memoriais-por-etapa-projeto` | v1.1 (L4) | 1-40 | declarada, sem versão nem linha | não (NBR 6492 não aberta) |
| `arquitetura-nbr9050-acessibilidade` | 1.2, 13/10/2026 (L3) | 1-40 | **não declarada** | não. A Skill (L19) nomeia a Lei 13.146/2015; a v4 diz só "lei federal de acessibilidade" sem nome. **NBR 9050:2020 não está no acervo: "2020 não lida, pendente"** |
| `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj` | 1.2 (L4) | 1-40 | **não declarada** | não. O pé-direito (F8 da v3) saiu |
| `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj` | v1.6, 10/10/2026 (L4, L6) | 1-40 | declarada v1.6 | não. A Skill L38 traz LC 270 Art. 368 §1º I (AP4/ZPP: 1 vaga para cada 4 unidades): a v4 não usa |
| `varandas-nao-computaveis-ate-to-coes-lc198-rj` | v1.2 (L4) | 1-40 | declarada, sem versão | não |
| `legal-oodc-mais-valera-mais-valia` | 1.1 (L3) | 1-30 | **não declarada** | não. A Skill L30 traz "60x com 30% … **não alcança AP4**" e "30% à vista até 01/12/2026": a v4 não usa |
| `legal-base-legislativa-bairro` | **sem versão no cabeçalho** (L1-4) | 1-30 | **não declarada** | não |
| `decreto3046-81-lc270-2024-licin-barra-recreio` | 1.5, 08/10/2026 (L4, L7) | 1-30 | declarada, sem versão | não |
| `remocao-arvores-smac-fpj-autorizacao-compensacao-rj` | v1.0 (L3) | 1-30 | **não declarada** | não |
| `levantamento-topografico-cadastral-orientado-duli-licin-rj` | v1.11, 13/10/2026 (L4, L10) | 1-30 | **não declarada** | não |

**Resultado da v4:** 4 de 10 Skills declaradas, 1 com versão, nenhuma com linhas. 6 Skills listadas no enunciado ficaram fora.

---

## (e) O que NÃO foi feito nesta execução (treino)

- **PDFs primários não abertos** (COES, LC 270, Dec. 3.046, NBR 6492). Não confirmei as citações verbatim da v4-06 L118-137 nem qual lado da contradição de v4-06 L33-35 × L39 é verdadeiro.
- **Skills lidas só no cabeçalho** (linhas indicadas em (d)), não inteiras.
- **Contagem de palavras do corpo v4:** não feita (sem ferramenta). Pendente de Wallenberg.
- **Não abri:** `caso_sombra_003.md`, Regramento do condomínio, auditoria de Kelsen da Etapa 01, v3 arquivos 02-04 e 06, e os arquivos `AUTO_TESTE_R6.md`, `ADENDO_pendencias_08-10-2026.md` e `tabela_correcoes_oscar_v8.md` da pasta v8 (fora da lista).
- **Desvio de método (declarado):** a ordem era "só Read por caminho exato". Usei **Glob duas vezes**, restrito às pastas listadas na ordem (`entrega\v4\`, padrão `0[1-6]*`; `etapa_03_levantamento\entrega\v8\`, padrão `*`), só para obter os nomes exatos. Nenhuma busca em pasta ampla, nenhum Grep. Os nomes da v8 que não estavam na lista não foram abertos.
- **Sem decisão:** qual TO vale para a SMD (Kelsen); se o "10%" do P01 L36 é a SMD a adotar (Kelsen); divergência V9 L206 × 222,72 (Villaça, via Lúcio).

---

## O que a v4 deixou de fora (lista de falhas, com prova)

1. **Não abriu nenhuma etapa aprovada anterior, exceto a Etapa 03.** Prova: v4-06 L51. As premissas legais saíram do Resumo do enunciado (v4-01 L32-37 citam "Resumo"), o que o checklist proíbe.
2. **SMD com origem errada.** O "10%" vem de P01 L36 ("Mecanismo geral… daria 10%"), conta feita com a TO municipal de 50% (P01 L29). A v4 o atribui ao enunciado (v4-01 L17; v4-05 E-6) e não registra que a Etapa 01 já trazia a TO de 50% (só aparece como "sensibilidade, não é premissa", v4-05 E-8). A pergunta P-SMD a Kelsen sai sem a fonte aprovada.
3. **Permeabilidade 25% dada como ausente.** v4-05 L62 diz que o 25% não está escrito; está em P01 L36.
4. **ATE máxima de 571,80 m² não aparece** (P01 L28, L66, L74).
5. **Escavação ≤ 1,20 m não aparece** (P01 L37, L266; LAX L331).
6. **Cota de soleira +3,20 prevista, Art. 458 e topo +11,70 não aparecem** (P01 L41; LP1 L75-77; LAX L199). Regressão da v3 (P1, E-21).
7. **Assembleia: 2/3 = 31 de 46 não aparece** na resposta ao síndico (P01 L46, L135; v4-04 M-04 L16). Regressão da v3.
8. **Mais-Valerá sem as razões** (AP4 fora do 60x com 30%; 30% só à vista até 01/12/2026; licença após pagamento total). Prova: P01 L148-159; Skill `legal-oodc` L30; v4-04 M-06 L18 só remete. Regressão da v3 (C4, E-28).
9. **Cenário título (600 m²) incompleto** e **S2 = 480 (523–543 Co) ausente** (P01 L66-71, L83; V9 L28, L39; v4-05 E-9 só SMD).
10. **Divergência da Viabilidade não registrada:** V9 L206 diz "falta 160 m²" em H1; a v4 diz 222,72 (Co). 160,16 é computável (LAX L38). Sem rótulo, a mesma pergunta tem dois números.
11. **Fundação especial e jardim de chuva fora** (V9 L139-143; LP2 L103-104; LP3 linhas 15-16). Regressão da v3 (P13).
12. **Locação permeável A (+1,00) sumiu**; ficou só B (+2,05) em v4-04 P-04 L35 (LAX L162-163).
13. **Regra da faixa lateral permeável ausente e contradita:** LAX L165 (circulação de 1,20 m desqualifica a faixa) × v4-03 L34 (fluxo de serviço na lateral de 2,50 m, sem efeito na permeabilidade).
14. **Regime trocado:** 297,28 chamado de "construída máxima" e de "teto computável" na mesma linha (v4-01 L60; L16); 457,44 "construída… computáveis" (v4-01 L14). A declaração de v4-06 L90 é falsa.
15. **Remissões colidem e a declaração diz o contrário:** v4-04 L15, L35-47 usam "Anexo E-N"/"Anexo C-N" (11 células) enquanto v4-06 L146 afirma que foram trocadas.
16. **Pedido 17 da Etapa 03 (5.15: R$ 6.300/m², banco 60%, CAB × CAM) ausente** da matriz (LAX L264; v4-04 §2 termina em P-16, L47).
17. **Pendências de terceiros da Etapa 03 sem dono na v4:** linhas 10, 15, 16, 17 e 19 da LP3 (L25, L30, L31, L33, L34).
18. **Organograma e esquemas básicos sem gráfico** (v4-03 L6, §1-§4 só tabelas; Skill nbr6492 L33: documentos gráficos). O adiamento para a Etapa 05 não tem base: esquema básico não é planta.
19. **Skills:** 6 das 10 do enunciado não declaradas (`arquitetura-nbr9050`, `coe-lc198`, `legal-oodc`, `legal-base-legislativa-bairro`, `remocao-arvores`, `levantamento-topografico`); só a de vaga com versão; nenhuma com linha (v4-06 L26-29).
20. **Declaração de leitura contraditória:** v4-06 L33-35 (PDFs lidos por página) × L39 ("Nesta execução não abri nenhum desses dois arquivos nem outro da listagem").
21. **Errata incompleta na v4:** COES Art. 28 IV (ERR L22) e XXIII b não lido (ERR L31) ausentes; XXIII a só na tabela de cópias.
22. **Itens menores de herança ausentes:** afastamentos medidos do muro do Lote 16 (P01 L263); fora do Habite-se (P01 L120); semienterrado = subsolo (P01 L274); APP tira a LMS simplificada (P01 L172); aprovação prévia do condomínio (Art. 9º, 30 dias) como premissa geral (P01 L44); PRPA/RRT não definido (P01 L285); LC 270 Art. 347 V e VI (P01 L38-39); pé-direito (v3-01 L46); M-c (LAX L88); alt. B 2 + 1 (LAX L125); Art. 216 V (LP2 L101).

**Não consegui verificar:** contagem de palavras; texto verbatim dos PDFs citados na v4; qual lado da contradição de leitura de PDFs (falha 20) é verdadeiro; conteúdo inteiro das 10 Skills.

Oscar, 14/10/2026 (treino)
