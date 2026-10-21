# Volumetria primeiro: 3 estudos. Ensaio 003, EP

**Oscar (Assisted) | para auditoria de Lúcio | 20/10/2026 | caso 100% fictício | treino da Skill `partido-volumetria-residencial-contemporanea` v1.0 (lida inteira, 78 linhas) + `oscar-revit-projetista-vitruvius` v1.3.0 (§0–§11 lidas, L1–210)**
**Natureza:** análise preliminar, sem Gate. Estudo de massa: sem divisões internas, portas e janelas. **Não escolho. Recomendo, com o motivo, e Claudemberg escolhe.**

**Conclusão primeiro.** Modelei três volumetrias de fato diferentes, cada uma em sua cópia: **A, prisma suspenso** (um bloco superior longo sobre um térreo recuado, com garagem e entrada debaixo do balanço), **B, duas alas e pátio** (ala da frente e ala dos fundos ligadas por uma faixa de serviço, com pátio no meio) e **C, casa-varanda** (uma laje-varanda que cobre o lote edificável e um volume superior com fachada oeste curva). **Recomendo a A como base, com o pátio da B como variante.** A A é a que mais aproveita a TO (218,43 de 228,72 m² sem varandas) e a área computável (≈ 356 m²). Ela cumpre as regras 1, 5, 6, 8 e 9 da Skill e é a que menos perde em H1. Nenhuma das três chega ao teto computável de 457,44 m², e o programa de 520 m² já não cabia nesse teto (Briefing v4). Não há sobra de área para propor ambientes novos. O que cada estudo deixa de fora vai para o cliente (P-l), não é corte meu.

Coordenadas em metros, no referencial do Levantamento v8: origem no vértice frente-esquerda, x ao longo da testada (0 a 14,29), y da rua (0) para os fundos (40).

---

## 1. Passo 0: perfil da família Montenegro Prates

Fontes abertas nesta execução: Briefing v4 `etapa_04_briefing/entrega/v4/01_briefing_corpo_003_v4.md` (L30–118) e `02_planilha_ambientes_003_v4.md` (inteira, 62 linhas), e o enunciado da Etapa 5 `etapa_05_estudo_preliminar/enunciado.md` (inteiro, 142 linhas).

| Traço | Trecho (fonte) | O que pede à forma |
|---|---|---|
| **P1** Três gerações: o casal e a mãe | "suíte acessível no térreo para D. Lourdes" (01 L41; 02 A1) | ala íntima térrea, sem escada, com jardim próprio |
| **P2** A família recebe | "estar/jantar", "cozinha com gourmet", "área gourmet ... convívio, churrasco" (01 L41; 02 A5–A7) | varanda como sala, social térreo voltado ao jardim |
| **P3** Trabalho em casa com atendimento | "Escritório com porta própria e atendimento de clientes em casa (Helena, 09/10)" (01 L116) | entrada de cliente separada da íntima, perto da porta |
| **P4** Quatro carros | "garagem para 4 carros" (01 L41); decisão C1 (01 L67) | garagem que não seja a fachada (regra 9) |
| **P5** Gosto pelo efeito de pé-direito alto | Rodrigo, 13/10: "sala de estar com pé-direito de 7 metros" (enunciado L79) | estar em pé-direito duplo |
| **P6** Natureza: lago, árvores, jardim, piscina | Helena, 09/10, lago e árvores (01 L115); "piscina, deck e jardim" (01 L41) | casa aberta para os fundos, árvores da frente preservadas |
| **P7** Lazer em casa | "cinema" (02 A4) | volume fechado, que pode ser cego, no superior |
| **P8** Vista e sol | corretor: "sala de frente pro poente, com vidro de piso a teto" (enunciado L88) | **não aceito:** norte pendente (enunciado L126); vidro grande só com proteção |

**Não consta nas entradas autorizadas** (pergunta ao cliente, dono Lúcio): idades, filhos e quem ocupa as 3 suítes do superior, pets, hobbies além do cinema, referências de imagem ("projeto de referência" citado por Rodrigo, enunciado L79), gosto de materiais.

**Programa e área.** O Briefing não tem metragem por ambiente (02 L7). Suítes "no tamanho do programa" = **a definir pelo cliente (P-l)**. Pedido: ~520 m² construídos. Teto computável: 457,44 m² (02 L37). Os três estudos ficam **abaixo** do teto (§4), então **não há sobra** e nenhuma "sugestão ao cliente" de ambiente novo é proposta. Se o cliente reduzir o programa e sobrar área, entram como **sugestão ao cliente:** varanda da suíte (já existe em A e C), estar íntimo no superior e adega.

## 2. Lote e lei (de `layout_partidos.md` Passo 1, L14–38)

Envelope H0: x 2,50–11,79 × y 6,00–35,00 (9,29 × 29,00 = 269,41 m²). Afastamentos 6,00 frontal / 2,50 laterais / 5,00 fundos. TO 40% = 228,72 m² de projeção. 2 pavimentos. Altura máxima de 8,50 m da soleira. Cobertura só técnica. Níveis do modelo, relidos pelo status: Terreno 0, Páv. térreo 0,30, Páv. Superior 3,45, Cobertura 6,60 (ids 324604, 311, 694, 323714). H1: y ≤ 22,00. Norte pendente.

**Altura (os três estudos):** laje de cobertura "Genérico - 400 mm" com base a 6,60 e topo a 7,00. Da soleira (0,30): 7,00 − 0,30 = **6,70 ≤ 8,50** (folga de 1,80). A relação com a soleira +3,20 do condomínio está pendente (dono topógrafo/Lúcio). **Pé-direito duplo:** 6,60 − 0,30 = 6,30 m de piso a laje (≈ 6,20 livres), abaixo dos 7 m pedidos (P5). Os 7 m exigiriam subir a cobertura acima do nível 6,60: pendente, dono Lúcio/Kelsen.

---

## 3. Os estudos lado a lado

| | **A: prisma suspenso** | **B: duas alas e pátio** | **C: casa-varanda** |
|---|---|---|---|
| Arquivo | `diagnostico_EP\EP_volumeA.rvt` | `diagnostico_EP\EP_volumeB.rvt` | `diagnostico_EP\EP_volumeC.rvt` |
| **Conceito (1 frase)** | Um prisma longo de suítes paira sobre um térreo recuado e envidraçado. Debaixo do balanço ficam a garagem e uma entrada com parede curva. | A casa se divide em duas alas ligadas por uma faixa de serviço junto à divisa, com um pátio no meio para onde o estar avança em curva. | Uma grande laje faz de varanda e cobre todo o térreo. Sobre ela pousa um volume com fachada oeste curva, e a entrada é conduzida por um muro baixo curvo. |
| Referência (Skill F1/F2) | Prudente de Moraes Neto (prisma sobre base recuada, varanda contínua) | Lima Pádua / Paes de Carvalho (pátio entre alas, faixa de serviço) | Costa Ribeiro (varanda-sala) e Ofaire (curva) |
| Ligação com o perfil | P4 (carros sob o volume), P2 (térreo inteiro social sob a marquise curva), P5 (duplo no estar), P1 (térreo amplo) | P1 (ala da frente com suíte térrea e escritório perto da entrada, P3), P6 (pátio, jardim), P5 (duplo na ala dos fundos) | P2 (varanda é a sala, ~95 m² de varanda térrea), P6 (estar envidraçado nos 4 lados), P5 |
| PNG 3D | `D:\011_VITRUVIUS\_imagens\volumetria_20-10\A\vitruvius_20261020_093901 - Vista 3D - EP- Perspectiva.png` | `...\B\vitruvius_20261020_094034 - Vista 3D - EP- Perspectiva.png` | `...\C\vitruvius_20261020_094147 - Vista 3D - EP- Perspectiva.png` |
| PNG frontal SUL (sem/com muro) | `...\A\vitruvius_20261020_093901 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png` / `- COM MURO.png` | `...\B\vitruvius_20261020_094034 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png` / `- COM MURO.png` | `...\C\vitruvius_20261020_094147 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png` / `- COM MURO.png` |
| PNG fundos NORTE (sem/com muro) | `...\A\... - ELEVACAO FUNDOS NORTE - SEM MURO.png` / `- COM MURO.png` | `...\B\... - ELEVACAO FUNDOS NORTE - SEM MURO.png` / `- COM MURO.png` | `...\C\... - ELEVACAO FUNDOS NORTE - SEM MURO.png` / `- COM MURO.png` |

### O que vi nas imagens (todas abertas com Read nesta execução)

- **A, 3D:** a casa aparece inteira, com o muro do lote. O prisma branco e a laje de cobertura ficam por cima, e a fachada oeste é de vidro, com sacada contínua e guarda-corpo. Embaixo dele aparecem a garagem aberta, o hall de entrada com parede curva e os pisos do caminho e do acesso de carros até a rua. A marquise curva dos fundos aparece atrás, em escuro. **SUL sem muro:** prisma de 6,60 a 7,00 sobre a laje de 3,45. No térreo, recuado, aparecem a linha da parede do fundo da garagem (x 6,79) e o guarda-corpo da sacada à esquerda. Sem aberturas, porque é estudo de massa. **SUL com muro:** o muro tapa o térreo até ~1 m e o prisma fica inteiro visível. **NORTE sem/com muro:** vidro nos dois pavimentos, a borda da marquise curva vista em segmentos a 3,45 e o guarda-corpo da sacada à direita. Nas 4 elevações aparecem 2 marcadores de corte antigos (limpeza pendente).
- **B, 3D:** a casa aparece inteira. Na frente fica o bloco alto (x 2,5–6,79) com a entrada recuada embaixo, ao lado da laje do abrigo (laje-jardim, escura), e o superior recuado em y 11. Atrás aparecem o bojo curvo do estar avançando sobre o pátio, a ala dos fundos com vidro para o pátio e o guarda-corpo da sacada dos fundos. **SUL sem/com muro:** **lê como caixa plana.** Dois retângulos lado a lado, porque o recuo do superior (5 m) e o abrigo aberto não aparecem em linha sem sombra. Isso é contra da B na fachada. **NORTE:** pano de vidro nos dois pavimentos, com sacada e guarda-corpo a 3,45 e beiral da laje.
- **C, 3D:** a casa aparece inteira. A grande laje a 3,45 cobre o térreo com guarda-corpo em todo o perímetro, o volume superior tem a laje de cobertura com beiral, o térreo é de vidro e o muro baixo curvo fica junto ao caminho de entrada. **A curva da fachada oeste quase não se lê na perspectiva**, porque fica atrás do guarda-corpo e do ângulo da câmera. **SUL sem/com muro:** laje-varanda com guarda-corpo, o volume superior fechado (empena) e o térreo recuado. **NORTE:** vidro nos dois pavimentos e a laje-varanda saliente entre eles.

### Dimensões principais (cotas de vértice, em m)

**A**
- Térreo (fechado): x 3,70–11,715 × y 11,00–33,00, com a parede curva do hall de (3,70; 11,00) por (5,245; 10,20) a (6,79; 11,00), R = 1,89 (releitura). Altura das paredes 3,15 (0,30 → 3,45).
- Garagem coberta sob o prisma: x 6,79–11,79 × y 6,00–11,00 (2 vagas lado a lado, 5,00 × 5,00). Pórtico de entrada: x 3,70–6,79 × y 6,00–11,00.
- Prisma superior: x 3,70–11,715 × y 6,075–30,00, paredes de 3,15 (3,45 → 6,60). Fachada oeste e fundos em "vitrine pav superior".
- Laje do superior: x 2,50–11,79 × y 6,00–30,00 (sacada contínua x 2,50–3,70). Vazio do pé-direito duplo: x 3,85–6,85 × y 24,00–29,90.
- Marquise dos fundos (nível 3,45): y 30,00–33,50 + arco de (11,79; 33,50) por (7,145; 35,00) a (2,50; 33,50), R = 7,942, 34 segmentos de 0,29 m.
- Cobertura: x 2,50–11,79 × y 6,00–30,60 (beiral de 0,60 nos fundos).

**B**
- Ala da frente, térreo: x 2,50–11,79 × y 6,00–15,00. Entrada recuada x 2,50–6,79 × y 6,00–8,00. Abrigo aberto x 6,79–11,79 × y 6,00–11,00 com laje-jardim a 3,45.
- Ala da frente, superior (em L): torre x 2,50–6,79 × y 6,00–15,00 + x 6,79–11,79 × y 11,00–15,00.
- Faixa de serviço (só térreo): x 9,29–11,79 × y 15,00–21,00. Pátio: x 2,50–9,29 × y 15,00–21,00.
- Ala dos fundos (2 pav.): x 2,50–11,79 × y 21,00–33,50. Bojo curvo do estar de (2,575; 21,00) por (5,932; 19,80) a (9,29; 21,00), R = 5,30 (releitura); piso do bojo com 25 segmentos de 0,29 m.
- Sacada dos fundos: y 33,50–35,00. Vazio duplo: x 2,65–7,00 × y 27,50–33,40.
- Coberturas: ala da frente (L) até y 15,60 e ala dos fundos y 20,40–35,00.

**C**
- Térreo (vidro nos 4 lados): x 3,70–10,59 × y 11,00–30,00. Grande laje-varanda (nível 3,45): x 2,50–11,79 × y 6,00–33,00. Garagem sob a laje: x 6,79–11,79 × y 6,00–11,00.
- Volume superior: frente y 9,00, leste x 11,715 (empena), fundos y 28,00 (vidro), oeste em arco de (4,50; 28,00) por (3,00; 18,50) a (4,50; 9,00), R = 30,83 (releitura), sempre ≥ 2,50 da divisa (x mín. 3,00).
- Vazio duplo: x 4,80–8,50 × y 22,00–27,90. Cobertura: x 2,90–11,79 × y 8,40–28,60 (beiral de 0,60).
- Muro baixo curvo (1,20 m, nível Terreno) de (4,20; 0,30) por (3,00; 3,20) a (3,60; 6,00), no afastamento frontal (regime de muro: pendente).

## 4. Áreas aproximadas por pavimento (com a conta)

Regime pela premissa vigente M-b (conta tudo o que é coberto, inclusive a garagem; Briefing v4 01 L49). Varanda é não computável **só se** Kelsen confirmar (COES Art. 8º §4º via Briefing v4 01 L93, [nv] nesta execução). Garagem fora da ATE (LC 270 Art. 347 II, via 01 L92 [nv]). Só 1 vaga coberta fica fora da TO (Art. 350 III, via 01 L91 [nv]). Áreas pelos eixos e vértices dados, não pela face. Áreas dos pisos devolvidas pela ferramenta entre parênteses.

**A**
- Térreo fechado: 8,09 × 22,00 = 177,98 + bojo do hall ≈ 2/3 × 3,09 × 0,80 = 1,65 → **179,63 (C)**. Piso total 8,09 × 27,00 = 218,43 (ferramenta 218,43 ✓).
- Garagem: 5,00 × 5,00 = **25,00 (G)**. Pórtico: 3,09 × 5,00 − 1,65 = **13,80** (acesso coberto, regime pendente).
- Superior: 8,09 × 24,00 = 194,16 − vazio 3,00 × 5,90 = 17,70 → **176,46 (C)**. Sacada: 1,20 × 24,00 = **28,80** (varanda, regime pendente).
- Marquise: 9,29 × 3,50 + segmento (R²/2 × (2φ − sen 2φ) = 31,538 × (1,2493 − 0,9488) = 9,48) = **41,99** (ferramenta 41,99 ✓).
- **Computável A = 179,63 + 176,46 = 356,09.** Teto 457,44 → sobra de teto 101,35. Pedido 520 → faltam 163,91.
- **Projeção (TO), sem varandas:** prisma 8,09 × 24,00 = 194,16 + térreo além do prisma 8,09 × 3,00 = 24,27 → **218,43 ≤ 228,72** (folga 10,29; inclui a garagem sob o prisma). **Com sacada e marquise:** 218,43 + 28,80 + 41,99 − 24,27 (marquise sobre o térreo) = 264,95 > 228,72. Depende de Kelsen.

**B**
- Térreo: ala da frente 9,29 × 9,00 = 83,61 (ferramenta 83,61 ✓) − abrigo 25,00 − entrada 4,29 × 2,00 = 8,58 → 50,03. Faixa 2,50 × 6,00 = 15,00 (✓). Ala dos fundos 9,29 × 12,50 = 116,13 (✓) + bojo (R²/2 × (2φ − sen 2φ) = 14,594 × 0,3813) = 5,56 (ferramenta 5,55 ✓) → 121,69. **Térreo fechado = 186,72 (C)**. Abrigo **25,00 (G)**.
- Superior: L da frente 4,29 × 9,00 + 5,00 × 4,00 = 38,61 + 20,00 = 58,61. Fundos 116,13 − vazio 4,35 × 5,90 = 25,67 → 90,46. **Superior = 149,07 (C)**. Sacada 9,29 × 1,50 = **13,94** (varanda). Laje-jardim do abrigo 25,00 e da faixa 15,00 (não acessíveis: cobertura só técnica).
- **Computável B = 186,72 + 149,07 = 335,79.** Sobra de teto 121,65. Faltam 184,21 para 520.
- **Projeção sem varandas:** 83,61 + 15,00 + 116,13 + 5,56 = **220,30 ≤ 228,72** (folga 8,42). Com sacada: 234,24 > 228,72, depende de Kelsen. Pátio descoberto: 9,29 × 6,00 − 2,50 × 6,00 = 40,74 − 5,56 = **35,18** (candidato a permeável; Kelsen/Glaziou).

**C**
- Térreo fechado: 6,89 × 19,00 = **130,91 (C)**. Garagem **25,00 (G)**. Varanda térrea coberta: 9,29 × 27,00 = 250,83 (ferramenta 250,83 ✓) − 130,91 − 25,00 = **94,92**.
- Superior: 7,29 × 19,00 = 138,51 + segmento do arco (R = 30,833; 2φ = 0,6262 rad; 475,34 × (0,6262 − 0,5862)) = 19,03 → 157,54 − vazio 3,70 × 5,90 = 21,83 → **135,71 (C)**. Varanda superior em volta: 250,83 − 157,54 = **93,29**.
- **Computável C = 130,91 + 135,71 = 266,62.** Sobra de teto 190,82. Faltam 253,38 para 520.
- **Projeção:** a laje-varanda cobre **250,83 > 228,72 (excesso de 22,11)** se varanda coberta contar na TO. Sem varandas, ≈ 157,54 + 13,78 (térreo y 28–30) + 15,00 (garagem fora do superior) + ~2 (cantos do arco) ≈ **188** (aproximado). **Risco legal maior dos três.**

## 5. Prós e contras (regras da seção 3 da Skill e lei)

| Regra / lei | A | B | C |
|---|---|---|---|
| 1 Jogo de volumes | ✓ prisma sobre base recuada | ✓ duas alas + volume baixo do abrigo | ✓ laje + volume pousado; mais horizontal |
| 2 Curva como gesto | ✓ hall de entrada e marquise dos fundos | ✓ bojo do estar no pátio | ✓ fachada oeste e muro de entrada; **a curva quase não aparece no 3D** |
| 3 Varanda é sala | parcial: marquise dos fundos ~42 m² | fraca: só sacada; o pátio faz o papel | ✓✓ ~95 m² térreos + ~93 superiores |
| 4 Pátio | ✗ | ✓ | ✗ |
| 5 Pé-direito duplo | ✓ 17,70 m² no estar | ✓ 25,67 m² | ✓ 21,83 m² |
| 6 Sacadas nas suítes | ✓ sacada contínua oeste (também protege do sol) | parcial: só a ala dos fundos | ✓ volta toda |
| 7 Faixa de serviço na divisa | possível no térreo leste (não desenhada) | ✓ desenhada (x 9,29–11,79) | possível (não desenhada) |
| 8 Entrada marcada | ✓ pórtico sob o balanço + parede curva | ✓ reentrância sob a torre | ✓ muro curvo que conduz |
| 9 Garagem não é a fachada | ✓ sob o volume, recuada | parcial: o abrigo fica na frente, mas baixo e com laje-jardim | parcial: sob a laje, visível na frente |
| 10 Clima | vidro oeste grande: **exige brise** (norte pendente) | alas com vidro para o pátio, empenas nas divisas | a laje-varanda sombreia o térreo; vidro nos 4 lados |
| 11 Interior–exterior | ✓ fundos | ✓ pátio + fundos | ✓✓ |
| 12 Planta livre | ✓ térreo de 8 m livre | média: o térreo se divide em alas | ✓ |
| Afastamentos | ✓ tudo em x 2,50–11,79 × y 6,00–35,00 | ✓ | ✓ (muro baixo no frontal: regime de muro pendente) |
| Altura | 6,70 ≤ 8,50 ✓ | 6,70 ✓ | 6,70 ✓ |
| TO sem varandas | 218,43 ✓ | 220,30 ✓ | ≈ 188 ✓ |
| TO com varandas | 264,95 ✗ sem Kelsen | 234,24 ✗ sem Kelsen | **250,83 só na laje ✗ sem Kelsen** |
| Computável (teto 457,44) | **356,09** | 335,79 | 266,62 |
| H1 (y ≤ 22) | fica o prisma até y 22 (8,09 × 16 = 129,44 por pav.) com garagem e entrada | perde a ala dos fundos inteira | perde o volume superior quase todo |
| Estrutura | balanço de 5 m sobre a garagem (Baumgart) | sem balanço relevante | laje-varanda de 1,2 a 3 m em balanço (Baumgart) |
| Vagas | 2 cobertas; as outras 2 descobertas, pendente Kelsen | 2 no abrigo; idem | 2 sob a laje; idem |

## 6. O que a ferramenta não fez (seção 5 da Skill) e como aproximei

| Falta | Aproximação |
|---|---|
| Laje com borda curva | polígono por segmentos: A, marquise com 34 segmentos de 0,29 m; B, piso do bojo com 25 segmentos de 0,29 m. Declarado. |
| Cobertura inclinada, borboleta ou curva | não pedida (todas planas); laje plana "Genérico - 400 mm" com beiral, sem platibanda modelada |
| Balanço | laje passando da parede de apoio (A, prisma sobre a garagem; C, laje-varanda). **Para o Baumgart.** Sem pilares modelados. |
| Brise, cobogó | não modelados (sem família de brise usada). Declarado: A exige brise na fachada oeste. |
| Vista 3D | **sem ferramenta para criar ou ajustar vista 3D.** Exportei a "EP. Perspectiva" (id 438334) como está; ela mostra a casa inteira nos três, mas o ângulo esconde a curva oeste da C e a marquise curva da A só aparece ao fundo. |
| Portão e piscina | não modelados. Portão: família padrão pendente (Tenreiro). Piscina: pendente (regime e laudo, Briefing 02 A11). |

**Falhas de ferramenta (§8):** nenhuma recusa ou erro nesta rodada. Três observações, sem código:
- (i) `criar_elemento_superficie` devolve área menor nos pisos do nível Superior: A 215,00 contra 9,29 × 24,00 = 222,96; B 75,65 contra 83,61; C 242,87 contra 250,83. É sempre −7,96 m², sem causa conhecida. No térreo bate. Usei a conta pelos vértices. Proposta: verificar se a ferramenta mede a área depois de algo do template.
- (ii) Os marcadores de corte antigos (AA/BB do diagnóstico) aparecem nas 4 elevações: limpeza (§5 da Skill) não feita.
- (iii) A primeira exclusão listou 450929 como "não encontrado" porque ele já tinha saído junto com a escada 450890. Não é defeito.

## 7. Recomendação (não é escolha)

**Recomendo a A como base, levando para ela o pátio da B como variante.** Motivos:
1. É a que mais aproveita a TO sem depender de varanda (218,43 de 228,72) e a de maior área computável (356,09).
2. Cumpre de uma vez as regras 1, 5, 6, 8 e 9: garagem e entrada debaixo do volume, entrada marcada pela curva e sacada contínua que protege as suítes.
3. É a que menos perde em H1, porque o prisma da frente cabe em y ≤ 22.

Contras que vão junto: o vidro oeste exige brise, sem norte confirmado; o balanço de 5 m vai para o Baumgart; são só 2 vagas cobertas; e o pé-direito duplo fica em 6,30, não nos 7 m pedidos. A **B** é a melhor em ventilação e pátio (regras 4 e 7), mas a fachada da rua fica plana e ela perde a ala inteira em H1. A **C** é a mais "casa-varanda" (regra 3), mas é a de maior risco de TO (laje de 250,83) e a de menor área. **Quem escolhe é Claudemberg.**

## 8. Ids criados (por estudo)

- **Limpeza do miolo do Partido B (feita na cópia A, herdada por B e C):** apagados 22 ambientes, a escada 450890 (com o corrimão 450929), o guarda-corpo 451022, as linhas de separação 450861/450863/450865, 34 paredes (449332–449335, 449394/449396/449398/449400, 450791–450816, com as 18 portas e as 22 janelas hospedadas), os pisos 449292 e 449300 e a cobertura 449441. Ficaram os muros 449286–449289 e a grama 449308/449316/449324.
- **A (EP_volumeA.rvt):** paredes 451584, 451585, 451586, 451725, 451726, 451727, 451728, 451820; curva 452024; pisos 452027, 452039, 452047 (marquise curva), 452088, 452096; shaft 452108; cobertura 452121; guarda-corpos 452138, 452159.
- **B (EP_volumeB.rvt; ids da A apagados nesta cópia):** paredes 452217–452222, 452356–452358, 452475–452480, 452572, 452573, 452655, 452656, 452738; curva 452739; pisos 452742, 452750, 452762, 452770 (bojo), 452802, 452810, 452824, 452832, 452840; shaft 452852; coberturas 452865, 452892; guarda-corpos 452909, 452930.
- **C (EP_volumeC.rvt; ids da B apagados nesta cópia):** paredes 452958, 452959, 453212, 453329, 453570, 453571, 453572; curvas 453661 (fachada oeste) e 453662 (muro); pisos 453665, 453673, 453681, 453689; shaft 453701; cobertura 453714; guarda-corpos 453731, 453752 (este deixa aberta a borda leste em y 6,10–9,00: corrigir).
- **EP_layout_partidoB.rvt:** não recebeu nenhuma escrita depois da cópia (o documento ativo foi conferido pelo status antes de cada série de escritas).

```
## Entrega — Ensaio 003 — EP, volumetria (3 estudos)
Build: 2026-10-19-conferir-layout-v64 (status)
Gate de entrada (0.1): connected true, documentTitle "EP_layout_partidoB", isModified false
Passos: [cópia A ✓ 09:35:00] [miolo apagado ✓ 64 de 65, 1 já removido] [A massa ✓ salvo 09:39:00] [cópia B ✓ 09:39:25] [B ✓ salvo 09:40:34] [cópia C ✓ 09:41:07] [C ✓ salvo 09:41:46] [imagens ✓ 15 PNG abertos] [portas/janelas ✗ estudo de massa] [eixos ✗ não pedidos]
Imagens conferidas (§6): §3 acima, com o que foi visto
Defeitos encontrados (§8): nenhum erro; observação de área do piso do Superior (−7,96 m²)
Lacunas declaradas (§3): sem ferramenta para criar ou ajustar vista 3D; brise não modelado; borda curva por segmentos; marcadores de corte nas elevações
Pendências: Kelsen (varandas fora da TO, vagas descobertas, pé-direito de 7 m, muro no frontal); Baumgart (balanços); norte (topógrafo); P-l (cliente); escolha (Claudemberg)
Status: PARCIAL
```

## Auditoria do Lúcio

**20/10/2026. Veredito: ENTREGA ACEITA COMO TREINO, PARCIAL. Não é material para cliente nem passou pelo Gate (Claudemberg).**

**O que conferi eu mesmo (com prova):**
1. **Imagens abertas por mim com Read:** as 3 perspectivas (`D:\011_VITRUVIUS\_imagens\volumetria_20-10\A|B|C\... - Vista 3D - EP- Perspectiva.png`) e a frontal SUL sem muro do A. As 15 existem (Glob). As 3 perspectivas mostram a casa inteira, com muro, jardins e acessos.
   - A: bloco superior envidraçado na lateral oeste com sacada e guarda-corpo, térreo recuado, hall curvo na frente. Lê como "prisma sobre base recuada".
   - B: dois volumes com altura e recuo diferentes, ligados; é o que mais quebra a caixa em perspectiva.
   - C: laje-varanda contínua com guarda-corpo dando a volta; a curva oeste quase não se lê (confere com o Oscar).
   - Frontal SUL do A: um retângulo de 2 pavimentos com cobertura plana, mais marcadores de corte sobrepostos. Em elevação, o balanço e a entrada não se leem.
2. **Aritmética refeita, todas fecham:** A 177,98+1,65=179,63; 194,16−17,70=176,46; soma 356,09; TO 194,16+24,27=218,43. B 83,61−25−8,58=50,03; 50,03+15+116,13+5,56=186,72; 38,61+20+90,46=149,07; soma 335,79. C 6,89×19=130,91; 138,51+19,03−21,83=135,71; soma 266,62; 250,83−228,72=22,11. TO limite 571,80×0,40=228,72. Altura 7,00−0,30=6,70 ≤ 8,50.
3. **Arquivo original:** status colado mostra cópias com `isModified:false` após cada save e nenhuma escrita no partidoB depois da 1ª cópia (declaração do Oscar; não reli o .rvt, não tenho Vitruvius).

**Achados (o que não aceito como "atende"):**
- **F1, a crítica de Claudemberg ainda vale em parte:** os três estudos têm cobertura plana única, e a fachada frontal do A é um retângulo. A regra 8 (entrada marcada) e a regra 1 (não caixa) estão cumpridas na perspectiva, não na fachada da rua. Antes de mostrar, a frente precisa de um gesto legível em elevação (marquise, recuo, cobogó).
- **F2, C não cumpre a TO:** a laje-varanda de 250,83 m² passa 22,11 m² da projeção de 228,72. Só fica de pé se Kelsen confirmar varanda fora da TO (Skill `varandas-nao-computaveis-ate-to-coes-lc198-rj`). Até lá, C é "não atende".
- **F3, pé-direito de 7 m (P5) não atendido em nenhum:** 6,30 m piso a laje. Há folga de 1,80 m na altura máxima; subir a cobertura do social para ~7,30 parece caber, mas a forma de medir os 8,50 (topo de laje, platibanda, soleira do condomínio +3,20) é do Kelsen. Pendência minha com Kelsen.
- **F4, área dos pisos do Superior 7,96 m² menor que pelos vértices nos 3 estudos:** sem causa achada. Uso a conta por vértices, e registro como possível defeito do Vitruvius sem código (sem erro colado = pendência, não defeito).
- **F5, garagem do A "sob o balanço":** na perspectiva, o piso escuro da garagem aparece à frente do hall curvo, não claramente sob o bloco superior. Conferir em planta antes de afirmar.
- **F6:** marcadores de corte antigos nas elevações; guarda-corpo 453752 do C com borda aberta (y 6,10–9,00); brise, pilares, portão e piscina não modelados; norte pendente (fachada oeste = suposição).
- **F7, perfil:** idades, filhos, pets, referências de imagem não constam. O perfil está correto no que existe; o resto vira pergunta ao cliente.

**Recomendação do Lúcio (a escolha é de Claudemberg):** concordo com o Oscar na **A como base**, por ser a que mais aproveita TO e área dentro da lei e a única que já tem sacada, pé-direito duplo e entrada sob balanço no mesmo gesto, **com dois ajustes antes de mostrar:** (1) o pátio e o jogo de alturas do B (que é o mais "casa brasileira" em perspectiva) e (2) uma frente com gesto legível na elevação SUL. C fica como alternativa só se Kelsen liberar varanda fora da TO.

**Lacunas de ferramenta:** sem criar ou ajustar vista 3D (perspectiva exportada como estava); borda curva só por segmentos (34 no A, 25 no B); cobertura só plana (sem borboleta ou inclinada, Skill §5); área de piso divergente (F4).

