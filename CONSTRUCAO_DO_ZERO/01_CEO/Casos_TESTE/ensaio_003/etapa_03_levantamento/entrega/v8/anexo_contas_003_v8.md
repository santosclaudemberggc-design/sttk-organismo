# Anexo — Memória de Cálculo e Tabelas de Apoio (v8)
## Ensaio Sombra 003, Etapa 03: Levantamento. Família Montenegro Prates (100% FICTÍCIO)

**Executor:** Oscar | **Auditoria:** Lúcio | **Data:** 08/10/2026 (v8) | Análise preliminar.
**Mudanças da v8 (em relação à v7):** (i) nenhum valor de "a" (m² por vaga) em nenhuma conta, tabela ou cenário; "a" é fórmula simbólica e pendente de verificação primária (R6 reprovada em 08/10/2026); (ii) a soma dos incisos I e II do Art. 29 não é usada como área de garagem; (iii) citações de lei sem abertura do PDF nesta execução marcadas [nv]; (iv) alternativa B reavaliada por comprimento (ver C-9); (v) C-5, C-6 e C-7 refeitos como fórmula e condição. Quadro completo em `tabela_correcoes_oscar_v8.md`.
**Referencial:** O = (0;0) no vértice frente-esquerda, na face do muro do Lote 16. x ao longo da testada, y para os fundos.
**Etiquetas:** (a) dossiê; (b) premissa do Legal ou da Viabilidade aprovada, ou de Skill; (c) pendente. **[nv]** = não aberto no primário nesta execução (citação da v7 ou de Skill).

---

## C-1 Lote: título × medida local

| Lado | Matrícula 5.1 | Levantamento 5.2 | Diferença |
|---|---|---|---|
| Frente | 15,00 | 14,30 | −0,70 |
| Fundos | 15,00 | 14,29 | −0,71 |
| Lateral esquerda (Lote 16) | 40,00 | 40,00 | 0,00 |
| Lateral direita | 40,00 | 40,02 | +0,02 |
| **Área** | **600,00 m² (oficial, documento)** | **571,80 m² (medida, calculada a partir das medidas)** | **−28,20 m²** |

- Retângulo pelas médias: 14,295 × 40,01 = 571,94 m², +0,14 sobre o valor do topógrafo, compatível com polígono não retangular. Prevalece 571,80 como medida (a).
- Perda atribuída ao muro (parecer §2.1): 0,70 × 40,00 = 28,00 m², contra a diferença de 28,20 m² (a). O enunciado traz "~28 m²".
- Área oficial: 600,00 m² (5.1, 5.3, 5.11) (a).

## C-2 Envelope H0 (571,80 m²) e cenário título (600 m²)

- Largura útil: 14,29 − 2 × 2,50 = 9,29 m. Profundidade útil: 40,00 − 6,00 − 5,00 = 29,00 m.
- **Envelope = 9,29 × 29,00 = 269,41 m²** (x 2,50–11,79; y 6,00–35,00).
- **Folga = 269,41 − 228,72 = 40,69 m² por nível** (15,1% do envelope).
- Cenário título: (15,00 − 5,00) × 29,00 = 290,00 m². Projeção: 0,40 × 600,00 = 240,00 m². Folga: 50,00 m².
- Lateral útil livre para vagas em comprimento: 29,00 m (usada em C-9).

## C-3 Cenário H1 (APP de 30 m da margem)

- Faixa no lote: 30,00 − 12,00 = 18,00 m. Profundidade útil: 40,00 − 18,00 − 6,00 = 16,00 m. Linha de H1: y = 22,00.
- **Envelope H1 = 9,29 × 16,00 = 148,64 m²** (y 6,00–22,00). Folga de envelope: zero.
- Contra a projeção: 228,72 − 148,64 = −80,08 m².
- Teto computável: 2 × 148,64 = 297,28 m², contra 457,44 (−160,16 m²).
- Redução do envelope: 269,41 − 148,64 = −120,77 m².
- O "~150 m²" do enunciado não bate com nenhuma das três contas.
- H2 (marinha) e H3 (FMP) não são estimáveis (c).

## C-4 Garagem: mecanismo, fórmulas e "a" pendente (H0)

- Só 1 vaga coberta fica fora da TO (LC 270 Art. 350 III [nv], "nos termos do COES"). Garagem, acesso e manobra ficam fora da ATE (LC 270 Art. 347 II [nv]). O pavimento superior pode ficar sobre a garagem. Cada vaga coberta além da 1ª consome área só do térreo computável.
- **Fonte dimensional (texto citado da Skill de vaga v1.3 §2 e da v7; COES p. 15 [nv]):**
  - Art. 29 I: vaga 2,50 × 5,00 m (ou 2,50 × 6,00 m, paralela ao eixo da circulação).
  - Art. 29 II: área de manobra livre, contígua à menor dimensão demarcada, 2,50 × 5,00 m.
  - Art. 29 III: limiar de dispensa de demarcação. Texto: "exceto quando estiver atendida a proporção mínima de vinte e cinco metros quadrados de área de estacionamento por vaga". **Não é tamanho de garagem, e não fixa a soma de vaga com manobra.**
  - Art. 29 IV: acesso às faixas de circulação, mínimo 2,50 m. Não trata de manobra compartilhada.
  - Divergência com o parecer v6 (que cita o Art. 29 III na p. 19): **em verificação**, não verificada nesta execução.
- **"a": pendente de verificação primária.** A soma dos incisos I e II **não** é usada como área de garagem (R6 reprovada em 08/10/2026). Nenhum limite superior ou inferior de "a" é fixado aqui.
- Pendências: (i) R1 da Skill de vaga (dimensão obrigatória na unifamiliar isolada; Gate do Maurício); (ii) se a manobra compartilhada muda a conta (Hely via Kelsen).
- **Fórmulas (n = vagas cobertas):**
  - térreo: T = 228,72 − (n − 1)·a
  - computável: C = 457,44 − (n − 1)·a
  - garagem: G = n·a
  - construída: A = C + G + V = 457,44 + a + V, independente de n (V = varandas não computáveis)
- **Sensibilidade:** ΔC = −(n − 1)·Δa. A exigência de varandas muda 1 m² por 1 m² de "a" (V ≥ 62,56 − a).
- **Uso permitido das dimensões:** só para checar se cabe no lote, por comprimento e largura. Exemplo: 3 vagas perpendiculares em série, cada uma com 5,00 + 5,00 = 10,00 m, somam 30,00 m contra 29,00 m de lateral útil (não cabe sem manobra compartilhada, leitura pendente).

## C-5 Quadro por número de vagas cobertas (H0, fórmulas)

| n | Origem | T (térreo) | C (computável) | G (garagem) |
|---|---|---|---|---|
| 1 | mínimo | 228,72 | 457,44 | a |
| 4 | reunião (caso §4); Briefing (C1) | 228,72 − 3·a | 457,44 − 3·a | 4·a |
| 6 | WhatsApp (5.10); fora do Briefing | 228,72 − 5·a | 457,44 − 5·a | 6·a |

Construída A = 457,44 + a + V para qualquer n. "a" pendente; nenhum valor numérico é atribuído a "a".

## C-6 Garagem em H1 (condição, não valor)

- Em H1, uma vaga dentro do envelope ocupa envelope, mesmo fora da TO. Por isso o conjunto ocupa n·a do envelope de 148,64 m².
- **Condição para caber dentro do envelope H1:** n·a ≤ 148,64 m² (com n = 4, a condição é "a" ≤ 148,64 / 4; valor de "a" pendente).
- Só se a 1ª vaga ficar fora do envelope (alternativa B, C-9) a forma (n − 1)·a passaria a valer.
- Construída máxima em H1: 297,28 m² para qualquer n (teto do envelope). Não depende de "a".

## C-7 Teste do programa de cerca de 520 m²

- Viabilidade: 457,44 computáveis + 42,56 a 62,56 não computáveis = 500 a 520 m² (Mascaró v8 §1; Villaça v9 §2) [nv].
- V necessário para 520: 520 − 457,44 − a = 62,56 − a (qualquer que seja n). Para 500: 42,56 − a.
- Capacidade de V em H0 (regime M-a): térreo livre no envelope (40,69 − a) mais 40,69 no superior = 81,38 − a.

| Regime de medição da TO | 1ª vaga | Varandas | Construída máxima H0 | 520 m² |
|---|---|---|---|---|
| **M-a:** o condomínio mede como a Prefeitura e o Kelsen confirma (LC 270 Art. 350 I e III [nv]; COES Art. 8º §4º [nv]) | fora | fora, dentro do envelope | 457,44 + a + V | **não concluído: depende de a (pendente)** |
| **M-c:** a vaga fica fora, mas as varandas contam | fora | dentro dos 228,72 | depende de a | **não concluído: depende de a (pendente)** |
| **M-b:** conta tudo o que é coberto (premissa vigente, parecer §5.2) | dentro | dentro | **457,44** (teto) | **não cabe: faltam 62,56** |

- Em M-b, a conclusão não depende de "a": tudo o que é coberto, inclusive a garagem, fica no teto de 457,44 m².
- **Nota de verificação para Lúcio (sem número):** as expressões de V necessário (62,56 − a) e de capacidade (81,38 − a) têm o mesmo termo em "a". Isso sugere que M-a pode não depender de "a". Não afirmo essa conclusão nesta versão: ela depende de confirmar a posição da 1ª vaga em M-a e de "a" ser fechado. Fica para refazer quando "a" for verificado.
- H1: faltam 520 − 297,28 = 222,72 m² de construída e 457,44 − 297,28 = 160,16 m² de computável.
- Área de trabalho S3/H1 da Viabilidade: 297,28 + 42,56 a 62,56 = 339,84 a 359,84 m². Não tem espaço físico. Sinalizado a Villaça, via Lúcio.

## C-8 Alternativa A: vaga descoberta no afastamento frontal

**Origem:** decisão de Claudemberg, 08/10/2026. Entra como alternativa com geometria e status. **Não é tratada como viável.**

**Geometria (só por comprimento).** Vaga 5,00 m + manobra 5,00 m = 10,00 m de profundidade, contra 6,00 m de afastamento frontal (Regramento 5.4; o RIU 5.3 dá 5,00 m; usado o mais restritivo). Não cabe sem usar a via pública, que não se presume (Skill de vaga R5 [nv]).

**Área e permeabilidade:** não calculadas nesta versão. Dependem de "a" (pendente).

**Status (texto obrigatório):**
"Vaga descoberta no afastamento frontal mínimo é vedada na ZE-5 pelo Dec. 3.046 XXII (p. 4), salvo exceção específica da subzona não verificada; a LC 270 Art. 363 §2º XII é divergente e está em Gate."

**Base (citada, [nv]).**
- Dec. 3.046, Disp. Gerais XXII (p. 4 [nv]): permite área livre para estacionamento, excetuada a do afastamento frontal mínimo, com 1 árvore por vaga. Redação de permissão com exclusão.
- Dec. 3.046, XXIII a (p. 4 [nv]): garagem coberta em subsolo, com exclusão do afastamento frontal mínimo.
- LC 270 Art. 363 §2º XII (p. 130 [nv]): estacionamento no afastamento frontal apenas em uni e bifamiliares, nos termos do COES.
- Nota de redação: a palavra "vedada" no status é leitura da Skill decreto (R12) e da Skill de vaga (R3), não texto literal do XXII.

**Pendências (não resolvidas aqui).**
- Kelsen: se o XXII incide sobre a subzona do lote. O dossiê (5.3) indica "ZPP, subzona A-ENS", designação do caso, **não verificada**.
- Gate do Maurício: conflito COES Art. 28 IV e LC 270 Art. 363 §2º XII × Dec. 3.046 XXII e XXIII a; regra de prevalência.
- Errata de 08/10/2026, Kelsen (`etapa_01_legal_base/ERRATA_08-10-2026.md`): a errata está no processo e não é pendência.

## C-9 Alternativa B: abrigo lateral (Dec. 3.046 XI). Aberta, não inviável

**Condições (paráfrase do XI, Dec. 3.046, p. 3 [nv]):** (i) uso residencial unifamiliar; (ii) afastamento frontal menor que 10,00 m; (iii) só afastamentos laterais, no térreo; (iv) abrigos abertos e cobertos por telha-vã; (v) fora da ATE e da TO. O XI não trata de fundos nem de balanço no frontal (C-10).

**Comprimento (lateral útil de 29,00 m, C-2; faixa de 2,50 m):**
- 2 vagas em série (2 × 10,00 m = 20,00 m): cabem em uma lateral.
- 3 vagas em série (30,00 m): não cabem em uma lateral só, sem manobra compartilhada (leitura pendente).
- 2 em uma lateral + 1 na outra: cabe por comprimento em cada lateral. Sem folga lateral (2,50 m exatos).

**Permeabilidade:** pavimentar a faixa lateral para vaga consome a folga permeável (C-12, folga H0 de 159,24 m²). A conta depende de "a" e não está concluída.

**Conclusão desta versão:** alternativa **aberta**. Depende de condomínio, de Kelsen (conflito XXIII × XI em aberto) e da conta de permeabilidade com "a" fechado. A v7 a dava como inviável por supor que as vagas extras ficavam todas numa lateral; essa premissa não é necessária para o XI.

## C-10 Varandas e saliência frontal

- Dec. 3.046 VII (p. 2 [nv]): varandas não são computadas na ATE e na TO, mas devem atender ao afastamento frontal mínimo, sobre o qual não se projetam balanços; para unifamiliar, remete ao XI.
- Dec. 3.046 XI (p. 3 [nv]): trata só de afastamentos laterais no térreo (C-9). **Não trata de balanço sobre o afastamento frontal de unifamiliar.** Logo, o frontal de unifamiliar não tem regra expressa no Dec. 3.046 (lacuna L2 do parecer v6).
- COES Art. 8º §1º (p. 5 [nv]): sobre o afastamento frontal, varandas e sacadas podem ocupar toda a fachada, recuadas no mínimo 1,00 m da testada.
- COES Art. 8º §2º (p. 5 [nv]): laterais e fundos, 2,50 m das divisas.
- COES Art. 8º §4º (p. 5 [nv]): varandas de unidades residenciais, em balanço ou reentrantes, não são computadas na ATE e na TO.
- Dec. 3.046 XIV (p. 3 [nv]): saliências para jardineira e ar-condicionado, acima do térreo, até 0,40 m, fora da ATE e da TO: 6,00 − 0,40 = y 5,60.
- **Conta condicionada (se o balanço frontal for admitido):** faixa de 1,00 a 6,00 m, dentro das laterais do envelope: 9,29 × 5,00 = 46,45 m² por pavimento superior. Condicionada a que o COES §1º prevaleça sobre o Dec. VII para unifamiliar (Kelsen; Gate) e ao condomínio.
- **Premissa adotada até decisão:** nenhum balanço em y 0–6,00. É premissa conservadora, não exigência legal (Peça 2 §3.3).

## C-11 Faixas fora do envelope (H0)

| Faixa | Coordenadas | Conta | Área |
|---|---|---|---|
| Frontal | x 0–14,29; y 0–6,00 | 14,29 × 6,00 | 85,74 |
| Lateral esquerda | x 0–2,50; y 6,00–35,00 | 2,50 × 29,00 | 72,50 |
| Lateral direita | x 11,79–14,29; y 6,00–35,00 | 2,50 × 29,00 | 72,50 |
| Fundos | x 0–14,29; y 35,00–40,00 | 14,29 × 5,00 | 71,45 |
| **Soma fora do envelope** | | | **302,19** |
| Envelope | | 9,29 × 29,00 | 269,41 |
| **Total da aproximação** | | 14,29 × 40,00 | **571,60** |

Fechamento: 571,60 contra 571,80 dá −0,20 m² (0,035%).

## C-12 Locação permeável H0 (142,95 m² = 25% × 571,80)

- Folga: 302,19 − 142,95 = **159,24 m²** podem ser impermeáveis fora do envelope.

| Locação | Faixas inteiras | Conta | Total | Folga |
|---|---|---|---|---|
| A: piscina fora dos fundos (ou demolida) | fundos + lateral esquerda | 71,45 + 72,50 | **143,95** | +1,00 |
| B: piscina nos fundos | duas laterais | 72,50 + 72,50 | **145,00** | +2,05 |

- Faixa lateral de 2,50 m: só se pode pavimentar no máximo 0,50 m ao longo dela, para manter 2,00 m de lado. Circulação de 1,20 m deixa 1,30 m < 2,00 m, e a faixa inteira é desqualificada.
- Com o frontal inteiro impermeável: 159,24 − 85,74 = 73,50 m² de folga.
- Se a alternativa B for adotada (C-9), a faixa lateral pavimentada para vagas consome essa folga. Conta pendente de "a".

## C-13 Faixas em H1

| Zona | Conta | Área |
|---|---|---|
| Faixa H1 (y 22,00–40,00) | 14,29 × 18,00 | 257,22 |
| Frontal | 14,29 × 6,00 | 85,74 |
| Laterais até y 22,00 | 2 × 2,50 × 16,00 | 80,00 |
| Envelope H1 | 9,29 × 16,00 | 148,64 |
| Soma | | 571,60 |

- Se a APP contar como permeável, 257,22 > 142,95.
- Se não contar: 85,74 + 80,00 = 165,74; folga de 165,74 − 142,95 = **22,79 m²**. Acesso com largura ≥ 22,79 / 6,00 = **3,80 m** esgota a folga.
- Vaga descoberta fora do envelope em H1 não é testada por área nesta versão (depende de "a"). Não se presume a via pública.

## C-14 Edícula

| Regra | Exigido | Existente (5.2) | Falta |
|---|---|---|---|
| Condomínio, 5.4 Art. 6º (prevalece) | 2,50 | 0,80 | **1,70** |
| COES, unifamiliar (parecer, linha 12; Art. 31 p.ú.) [nv] | 1,50 | 0,80 | **0,70** |
| CC Art. 1.301 (janela) [nv] | 1,50 | 0,80, com janela | 0,70 (risco civil, Kelsen R5) |
| Vão de iluminação/ventilação | PV com lado ≥ 1,00; PVI com lado ≥ 3,00 (Skill `coe-lc198` §2 [nv]); 0,80 não é afastamento nem prisma (parecer P2) | 0,80 | não atende nem como PV |

- Dec. 3.046 XV (p. 3 [nv]): edícula de até 2 pavimentos é computada na ATE e na TO.
- Face da edícula: x ≈ 14,29 − 0,80 = **13,49**. Se a profundidade em x passar de 1,70 m, parte da edícula entra no envelope (x < 11,79).
- Térreo com edícula mantida: T = 228,72 − (n − 1)·a − E (E = área da edícula; "a" pendente).

## C-15 Piscina, altura, rampa e térreo

- Piscina: 1,60 − 0,90 = **0,70 m** de fundo abaixo do NA, se as duas medidas partirem da mesma superfície.
- Altura: +3,20 + 8,50 = **+11,70 m** (referencial do condomínio), se a soleira ficar em +3,20.
- Rampa de veículo no frontal: até 10% e até 0,50 m de altura, sem prejudicar a acessibilidade (LC 270 Art. 363 §3º [nv]). Rampa NBR 9050 (≤ 8,33%, 0,80 m, 9,60 m por segmento): fonte secundária da Skill [nv]. Exemplo: 0,50 / 0,0833 = 6,00 m, o frontal inteiro.
- Térreo para a suíte de D. Lourdes: T = 228,72 − (n − 1)·a, "a" pendente. Sem número nesta versão.

## C-16 Crédito (5.14) [dossiê, nv]

Crédito de R$ 3,0 mi + recursos próprios de R$ 1,2 mi = teto de R$ 4,2 mi. Cada liberação limitada a 60% do valor do imóvel (terreno + obra executada), por laudo do banco. Condição: licença emitida até 30/06/2027. Custo para registro: CUB puro de R$ 1,88–2,04 mi (Mascaró v8 §4.1) [nv]; custo total S1 de R$ 2,49–3,03 mi (Mascaró v8 §5.2; Villaça v9) [nv]; fundação especial de ~R$ 150–300 mil [NC].

## C-17 Recontagem das contas (v8)

- Envelope: 14,29 − 5,00 = 9,29; 40,00 − 11,00 = 29,00; 9,29 × 29,00 = 269,41; 269,41 − 228,72 = 40,69. H1: 9,29 × 16,00 = 148,64; 2 × 148,64 = 297,28; −120,77 / −80,08 / −160,16.
- Faixas: 85,74 + 72,50 + 72,50 + 71,45 = 302,19; + 269,41 = 571,60; 302,19 − 142,95 = 159,24. H1: 85,74 + 80,00 = 165,74; − 142,95 = 22,79; 22,79 / 6,00 = 3,80.
- Garagem H0 (fórmulas): T = 228,72 − (n − 1)·a; C = 457,44 − (n − 1)·a; G = n·a; A = 457,44 + a + V. Sem valor de "a".
- Garagem H1: condição n·a ≤ 148,64. Teto construído 297,28.
- Programa: 520 − 457,44 = 62,56 (M-b, não cabe); V = 62,56 − a (formula); capacidade = 81,38 − a (formula); H1: 520 − 297,28 = 222,72.
- Alternativa A: geometria 10,00 m contra 6,00 m. Sem área.
- Alternativa B: lateral útil 29,00 m; 2 vagas (20,00 m) cabem; 3 em uma lateral (30,00 m) não cabem. Sem área.
- COES §1º: 9,29 × 5,00 = 46,45 (condicionado). XIV: 6,00 − 0,40 = 5,60.
- Edícula 1,70 / 0,70. Piscina 0,70. Altura 11,70. Lote 28,20 / 28,00. Crédito 3,0 + 1,2 = 4,2.
- Permeável: folga 159,24 (H0); 22,79 (H1 sem APP); locações A +1,00 e B +2,05.
- **Contagem de palavras:** não feita (sem ferramenta de contagem nesta execução); a ser feita por Wallenberg com ferramenta.

---

## D. Divergências do enunciado em relação às fontes (v8)

| Enunciado diz | Fonte diz | Como tratei |
|---|---|---|
| "Casa demolida (térrea 180 m²)" | A casa existe e está a demolir (caso §3; 5.8; Mascaró v8 §6.4) | Casa existente, a demolir |
| "A Lei permite até 1,60 m" | Quem fixa o limite é o Regramento, Art. 8º (5.4). Pela lei, a piscina descoberta não depende de licença (LC 270 Art. 278 §1º II) [nv] | Limite atribuído ao condomínio |
| "Valor mínimo de lote (Art. 353 III)" | O Art. 353 III trata das porções de ≥ 4 m² com 2 m de lado [nv] | Usei a regra das porções |
| "Cota de soleira atual +3,20" | É **prevista**, no referencial do condomínio (5.2); Art. 458 [nv] | Tratada como prevista e pendente |
| NA de 0,90 m no "5.2" | Está no 5.7 | Citei o 5.7 |
| "Custo ~R$ 1,8–2,1 mi + estrutura" | É o CUB puro; o total S1 é de 2,49–3,03 mi + fundação [NC] (C-16) | Não uso custo; registro para Villaça |
| "Crédito R$ 4,2 mi" | O crédito é de 3,0; o teto de 4,2 = crédito + próprios (5.14) | Corrigido |
| "H1 reduz ~150 m² de envelope" | −120,77 / −80,08 / −160,16 (C-3) | Os três números exatos |
| "Afastamento lateral esquerdo menor" | Continua 2,50 m a partir do muro; o que diminui é a largura do lote | Corrigido |
| "DULI anexado ao Executivo (Etapa 15)" | O DULI é do Projeto Legal, Etapa 07 (caso §6; parecer T8) | O levantamento alimenta o DULI |
| 5.5 "sem ligação" | 5.9: maré e manilha; Kelsen R2: Art. 216 V [nv] | Não decidi; o risco foi mantido |
| "Meça visualmente a edícula" | Não há visita; o 5.2 só dá 0,80 m | Usei só os 0,80; o resto foi para T9 |
| EXEMPLO (casa no meio, edícula de 20–30, piscina de 4 × 8) | Não é documento | Não usado |
| "Árvores sadias raramente saem" | Regra prática de fonte secundária (Skill `remocao` §6 [nv]); parecer P6 (c) | Citada com etiqueta (c) |
| "~0,70 × 40 = 28 m²" | 28,20 real; a atribuição ao muro é inferência | T5 |
| Art. 29 III interpretado como tamanho de garagem (versões anteriores, leitura reprovada) | O Art. 29 III é limiar de dispensa de demarcação [nv] | "a" pendente; nenhum número de garagem |

## E. Pedidos do cliente × resposta (v8)

| # | Pedido (fonte) | Resposta | Dono |
|---|---|---|---|
| 1 | ~520 m², 2 pavimentos (caso §4) | Não redimensiono. Em H0, cabe só com as 3 condições (Peça 2 §1); sob M-b faltam 62,56; em H1 não cabe (297,28) | Cliente + condomínio/Kelsen |
| 2 | 4 suítes, uma acessível no térreo (caso §1, §4) | É programa, não lei (COES Art. 31 V [nv]). O térreo encolhe com a garagem (C-15, fórmula) | Cliente; EP |
| 3 | Home office, cinema, estar/jantar, cozinha + gourmet, serviço com dependência | Só registro (Etapa 04 / EP); concorrem com a garagem no térreo | Cliente + Lúcio |
| 4 | Piscina, deck, jardim | Impermeáveis, saem dos 159,24; com a piscina nos fundos, só a locação B fecha (+2,05); em H1 não se presume | Cliente; Kelsen/SMAC (H1) |
| 5 | Garagem para 4 carros | Fórmulas do C-4/C-5, com "a" pendente. Alternativa A com status (C-8); B aberta (C-9); C = decisão do cliente | Cliente; Kelsen; condomínio; Hely |
| 6 | Manter a edícula (caso §4; Etapa 01 P2) | Não se sustenta; parecer de demolição total (Peça 2 §5.1) | Cliente; Kelsen + Comissão de Obras se insistir |
| 7 | Manter a piscina | Só com (i)–(iv), depois de T10 e do laudo (Peça 2 §5.2) | Cliente + Baumgart/Cardozo |
| 8 | Subsolo para 6 carros; "a assembleia vai liberar" (5.10) | Não pode ser desenhado: subsolo não permitido pelo Regramento do condomínio (5.4 Art. 8º); alterar exige 2/3 (Art. 21) [nv]; NA 0,90 e argila mole. Seis na superfície: fórmula de C-5, "a" pendente; nota fora do Briefing | Condomínio; Kelsen |
| 9 | Rooftop gourmet com piscina (5.10) | Não permitido pelo Regramento do condomínio, Art. 7º (5.4); para a Prefeitura, vira 3º pavimento (parecer P3, linha 10) | Condomínio; Kelsen |
| 10 | Rooftop pela Mais-Valerá, 60x com 30% (5.10) | Não confere, por 4 razões (parecer P4); CAB = CAM | Kelsen (respondido) |
| 11 | "O lago não atrapalha" (5.10) | Não se afirma: "~1 ha" não prova dispensa de faixa; maré; H0 × H1 aberto | SMAC/SPU/INEA via Kelsen |
| 12 | Tirar as árvores "pra rampa" (5.10) | O motivo caiu; preservar; garagem no envelope + árvores, com condição | Cliente; SMAC; condomínio (Art. 12) |
| 13 | Estudo anterior, "cabem 590 m²" (5.6) | Não serve: TO de 60%, afastamentos errados, 600 m², RIU de 2023, artigo revogado; 590 > 457,44 (parecer P1) | Kelsen (respondido) |
| 14 | Licença até 30/06/2027; obra em maio/2027 | Apertado; a obra em maio é de alto risco; edícula e assembleia pioram o prazo; T1–T25 têm de começar já | Cliente; Kelsen |
| 15 | Mudar até dez/2028 | Só registro | Cliente |
| 16 | Teto de R$ 4,2 mi | 3,0 + 1,2 (C-16); demolição de edícula e piscina [NC] | Villaça |
| 17 | 5.15: R$ 6.300/m²; banco libera 60%, R$ 5 mi?; CAB × CAM | Já respondidas pela Viabilidade (Villaça v9 §5) | Villaça |

## F. Perguntas do enunciado × onde estão respondidas (v8)

| Item | Onde |
|---|---|
| Dimensões × matrícula; 571,80 (medida); 600 (oficial); muro | Peça 1 §2; C-1; Matriz 1 |
| Altimetria | Peça 1 §3 (T1–T4) |
| Edificações existentes | Peça 1 §1, §4 (T8–T10) |
| Vegetação | Peça 1 §5 (T11) |
| Acessos | Peça 1 §6; Peça 2 §2 |
| Vizinhança | Peça 1 §6 (T12, T24) |
| Corpo hídrico | Peça 1 §6; Peça 2 §7 |
| Edícula a 0,80: factível manter? | Peça 2 §5.1; C-14; Matriz 2 |
| Acessibilidade do lote, canteiro | Peça 2 §2 |
| Envelope de 228,72, folga, zona | Peça 2 §1, §3.1; C-2; croqui da Peça 1 §1 |
| Piscina: cota, profundidade, alagamento | Peça 2 §5.2; C-15 |
| Árvores + garagem | Peça 2 §5.3 |
| APP/FMP, H1 | Peça 2 §3.5, §7; C-3 |
| Permeabilidade, Art. 353 III | Peça 2 §4; C-11 a C-13 |
| Cotas: soleira, piso térreo, piscina | Peça 2 §6; Peça 1 §3 |
| Riscos | Peça 2 §9 (remissão); Anexo I-2; Matriz |
| Matriz com 5+ questões e dono | Peça 3 (24 linhas) |
| Critério 1 (fotos) | Sem visita → T23; croqui descritivo; sem Revit |
| Critério 7 | Premissas herdadas (Peça 2 §0; Anexo I-1); programa só testado; Anexo D |

## G. Coerência entre as peças (mesma afirmação, mesma condição; v8)

**Regra:** a célula só cita a seção que afirma a frase com a mesma condição. Afirmação parcial = "—".

**Conferência desta versão:** cada célula foi conferida contra o texto escrito nas Peças 1, 2 e 3 desta execução, aberto no próprio arquivo (leitura de texto escrito nesta execução).

| # | Afirmação | Peça 1 | Peça 2 | Peça 3 |
|---|---|---|---|---|
| 1 | Envelope H0 = 269,41 m²; folga de 40,69 m² por nível | §1 (tabela, "Envelope H0") | §1, item 1 | linha 1 |
| 2 | 520 em H0 só com as 3 condições; sob M-b faltam 62,56 | — | §1, itens 2 a 3 | quadro acima; linha 24 |
| 3 | Premissa: nenhum balanço em y 0–6,00 | — | §3.3 | linha 20 |
| 4 | Edícula: falta 1,70 m pelo condomínio; parecer de demolição total; decide o cliente | — | §5.1 | linha 2 |
| 5 | Piscina: fundo até 0,70 m abaixo do NA | — | §5.2 | — (linha 3 traz o fato e o dono, não a frase) |
| 6 | Árvores: parecer de preservar; garagem no envelope + árvores, com condição | — | §5.3 | linha 4 |
| 7 | Alternativa A: "vedada na ZE-5 pelo Dec. 3.046 XXII (p. 4)... em Gate" | — | §3.4 | linha 9 |
| 8 | Varanda frontal: COES Art. 8º §1º (p. 5) admite recuo de 1,00 m; regra de unifamiliar no frontal em aberto | §1 (tabela, "Varandas frontais") | §3.3 | linha 20 |
| 9 | Garagem: "a" pendente; térreo = 228,72 − (n − 1)·a | — | §3.2 | linhas 9 e 22 |
| 10 | Curvas a cada 1,00 m (T1) | §3 | — | linha 11 (como requisito) |
| 11 | Soleira +3,20 prevista; depende de T2–T4 e R2 | §3 | §6 | linha 10 |
| 12 | Crédito 3,0 + 1,2; teto 4,2 | — | — | — (o fato vive só no Anexo: C-16) |
| 13 | Alternativa B: aberta; por comprimento não é barrada | — | §3.4 | linha 9 |
| 14a | H1: envelope 148,64 m² | §1 (croqui) | §3.5 | linha 5 |
| 14b | H1: construída máxima 297,28 m² | — | §1, item 4 | linha 5 |

**Afirmações estreitadas nesta versão:** (i) "a" sem valor em nenhuma peça; (ii) a soma dos incisos I e II não é área de garagem; (iii) "vedada" aparece só com zona e fonte (C-8, Peça 2 §3.4, Matriz linha 9); (iv) a varanda frontal não é "vedada": a regra expressa não existe para unifamiliar.

## H. Skills e fontes usadas (v8)

- **Lidas integralmente nesta execução:** Skill `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj` v1.3; Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.8.
- **Citadas da v7 ou de Skill, não relidas nesta execução [nv]:** Skill `decreto3046-81-lc270-2024-licin-barra-recreio` v1.5 (XI, XIV, XV, XXII, XXIII a, VII); Skill `varandas-nao-computaveis-ate-to-coes-lc198-rj`; Skill `nbr6492-2021-memoriais-por-etapa-projeto`; Skill `coe-lc198-2019-...`; Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio`; Skill `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`; Skill `remocao-arvores-smac-fpj-...`; Skill `arquitetura-nbr9050-acessibilidade`.
- **PDFs primários (COES, Dec. 3.046, LC 270) não abertos nesta execução.** Toda página citada é [nv].

## I. Conteúdo transferido do corpo da Peça 2 (v8)

### I-1 Premissas herdadas, sem reinterpretação (Etapa 01: parecer §2.2 e §5.2; Kelsen R1–R5) (b)

- Área de cálculo de 571,80 m² (medida). TO de 40%, com projeção de **228,72 m²**.
- Até o condomínio dizer como mede, conta-se como projeção tudo o que for coberto.
- Afastamentos de 6,00 / 2,50 / 5,00 m, medidos a partir do muro do Lote 16.
- 2 pavimentos e 8,50 m a partir da soleira. Teto computável de **457,44 m²**.
- Área permeável de **142,95 m²**, em porções de ≥ 4 m² com 2 m de lado.
- Sem subsolo nem rooftop. Escavação de até 1,20 m (piscina até 1,60 m).
- A edícula computa na TO e na ATE (Dec. 3.046 XV [nv]).
- Só 1 vaga coberta fica fora da TO, e as vagas não entram na ATE (LC 270 Art. 350 III e Art. 347 II [nv]).
- Vaga: **"a" = pendente de verificação primária**. Fonte dimensional: Art. 29 I e II (COES p. 15 [nv]). Art. 29 III é limiar de demarcação. Pendência R1 da Skill de vaga (Gate).
- Varandas: premissa conservadora de nenhum balanço em y 0–6,00, e a ≥ 2,50 m das divisas (COES Art. 8º §2º [nv]). COES Art. 8º §1º e Dec. 3.046 VII em aberto (C-10).
- O Dec. 3.046 XI entra só como alternativa condicionada da garagem, nunca como premissa (C-9).
- O Dec. 3.046 XXII e XXIII a: status do C-8, com o texto obrigatório. Leitura restritiva até o Gate (Skill de decreto R12).

### I-2 Riscos: o que o Legal deixou aberto (ex-Peça 2 §9)

| # | Aberto | O levantamento ajuda? | Impacto | Matriz |
|---|---|---|---|---|
| 1 | Espelho d'água (APP) | Sim (T13); decide a SMAC | H0 × H1 | 5 |
| 2 | Maré (marinha) | Sim (T14, T19); decide a SPU | Domínio da União | 7 |
| 3 | FMP | Não (INEA) | Não estimável | 6 |
| 4 | Ligação lago–canal | Sim (T13); decidem SMAC/Kelsen | Reforça H1/H2 | 8 |
| 5 | Soleira no referencial oficial (Art. 458 [nv]) | Sim (T3) | Rito e alturas | 10 |
| 6 | Divisa com o Lote 16 | Sim (T5); decide o cliente com advogado | 571,80 × 600 | 1 |
| 7 | Medição da TO pelo condomínio | Não | Decide o "cabe" em H0 | 21 |
| 8 | Edícula: rito e cômputo | Parcial (T9) | Térreo | 2 |
| 9 | Demolição × obra (POP-LEGAL-03 §5) | Não | Cronograma | 12 |
| 10 | O que conta como permeável | Não | Folga; alternativa B e A (C-8, C-9) | 14 |
| 11 | Varanda frontal: COES §1º × Dec. VII | Não | Até 46,45 m² por pavimento superior, se admitido | 20 |
| 12 | Garagem: XXIII × XI | Não | Alternativa B (aberta; depende de "a") | 9 |
| 13 | Dimensão mínima de vaga | Não | Valor de "a" (pendente) | 22 |
| 14 | Alagáveis e marés | Sim (T19, T22) | Piscina e fundos | 3 |

(A coluna "Matriz" é remissão à linha correspondente da Peça 3 v8.)

### I-3 Entradas para Baumgart (fundações) (ex-Peça 2 §7)

Baumgart precisa receber: a cota do terreno e o aterro; a posição dos 3 furos frente à projeção (NBR 8036, pela Skill R7 [nv]: mínimo de 3 furos entre 200 e 400 m²); a data do NA (médio × máximo); e os vizinhos, para vistoria cautelar.

— Oscar, 08/10/2026 (v8)
