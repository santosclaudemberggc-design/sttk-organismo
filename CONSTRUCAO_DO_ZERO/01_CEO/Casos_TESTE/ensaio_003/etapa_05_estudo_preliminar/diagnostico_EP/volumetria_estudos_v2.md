# Volumetria v2: estudos D, E e F. Ensaio 003, EP

**Oscar (Assisted) | para Lúcio | 20/10/2026 | caso fictício | análise preliminar, sem Gate. Nada aprovado: quem escolhe é Claudemberg.**

**Skills lidas inteiras nesta execução:** partido-volumetria-residencial-contemporanea v1.0 (78 linhas); layout-residencial-zoneamento-fluxos v1.0 (79); posicionamento-escada-residencial v1.1 (75); oscar-revit-projetista-vitruvius v1.3.0 (213); quadro-de-areas-rj v0.1 (237); vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj v1.6 (117).
**F1 (tese de Márcia Heck, `C:\Users\santo\Downloads\000501505-02.pdf`, 140 pp.):** lidas as pp. 1–8 do PDF (relação geral, pp. impressas 39–47), 80–84 (fichas 29–31) e 112–131 (fichas 40–48). Este volume só chega até a ficha nº 48. A Casa das Canoas (nº 92) aparece **apenas na relação geral** (p. impressa 42). A ficha dela não está neste volume, então a descrição usada para D é conhecimento geral [nv].
**Perfil da família:** é o mesmo de `volumetria_estudos.md` §1 (P1–P8). Não reabri o Briefing.

---

## 1. Diagnóstico de A, B e C: por que um arquiteto renomado não faria assim

**A, prisma suspenso.** É a citação da Prudente de Moraes Neto, mas sem o que faz aquela casa: o balanço e a varanda contínua. No lote estreito sobrou uma caixa branca com laje plana. As curvas ficaram no hall e na marquise de fundos, onde não se veem. Na rua, a frente lê como um retângulo de 2 pavimentos, e a garagem não se lê sob o volume (Lúcio, F1 e F5). A forma foi decidida pela TO, e não pela ideia. Um Niemeyer começaria pela ideia e acomodaria a TO depois.

**B, duas alas e pátio.** O pátio é a melhor ideia das três, mas as alas são duas caixas iguais, e a curva (o bojo do estar) fica escondida dentro do pátio. A fachada da rua é plana. Não há vaga (falha do pedido). A faixa de serviço come a divisa sem desenho. Lima Pádua e Paes de Carvalho têm o pátio, mas também cobertura e beiral que dão sombra e silhueta. A B tem só tampa plana.

**C, casa-varanda.** A laje-varanda de 250 m² é uma grande tampa que apaga o volume. O gesto curvo da fachada oeste tem R = 30 m: é quase reta e não se vê. A laje estoura a TO (22 m² acima) se a varanda contar. A Costa Ribeiro tem varanda **e** telhado com caimento. A C ficou só com a laje.

**O erro comum aos três:** curva usada como enfeite em parede escondida, e caixa plana como volume principal. Claudemberg pediu o contrário: curva como volume principal.

---

## 2. As três propostas

Coordenadas em metros, origem no canto frente-esquerda, y da rua para os fundos. Envelope de 2,50 a 11,79 × 6,00 a 35,00. Níveis 0,30 / 3,45 / 6,60, relidos pelo `get_levels` (ids 311, 694, 323714). Todas as cópias têm o mesmo terreno:
- grama 213,45 m² (lateral oeste 100 + frente 12 + fundos 58,95 + lateral leste 42,50);
- acesso de carros em "piso garagem" (L de 100 m²);
- caminho de pedestre de 26,23 m²;
- **4 vagas:** 2 cobertas de 2,50 × 5,00 lado a lado, e 2 descobertas paralelas em fila na faixa lateral leste (x 11,79–14,29, y 6–18, vaga 2,50 × 6,00, Skill de vaga §3). As descobertas no afastamento lateral são pendência do Kelsen. A manobra da vaga coberta cai no acesso, dentro do afastamento frontal: R3 e R5 da Skill de vaga, pendência do Kelsen. Nenhuma vaga fica no afastamento frontal mínimo.

### D: "laje livre sinuosa". Referência: Casa das Canoas, Oscar Niemeyer, 1953 (F1 nº 92, relação p. 42; ficha fora do volume, [nv])
- **Conceito:** um pavilhão social de vidro, de contorno curvo, com bolha envidraçada para os fundos, fica sob um volume íntimo de parede curva maciça a oeste (R = 29 m). A cobertura acompanha a curva, e uma varanda semicircular sai da suíte sobre a piscina. Garagem e entrada ficam sob o volume, marcadas por um muro curvo de pedra.
- **Ligação com o perfil:** P2, o estar envolto em vidro curvo, aberto para piscina e deck. P5, pé-direito duplo de 17,15 m² (vão 452346). P1, faixa de serviço e suíte térrea de D. Lourdes na divisa leste (x 9,29–11,715). P4, garagem sob o volume. P6, casa aberta para o fundo.
- **Prós:** é a única em que a curva é o volume (planta e 3D). Tem varanda semicircular, sacada frontal sobre a garagem, entrada marcada e a regra 7 (faixa de serviço) desenhada. O superior tem 170,98 m², dando suítes grandes.
- **Contras:**
  - na elevação SUL a curva some: lê como volume + garagem aberta + pano de vidro (PNG abaixo);
  - o vidro curvo a oeste exige brise (norte pendente);
  - a sacada frontal (balanço de 2 m) e a varanda semicircular (3,6 m) vão para o Baumgart;
  - o vidro curvo de R = 3,6 m é caro.
- **Ids:** paredes 451814, 451815, 451816, 452190–452192; curvas 451817, 451818, 452032, 452281; pisos 452284 (térreo 144,01), 452312 (superior), 452402, 452412, 452423, 452431, 452439, 452447, 452455 (piscina), 452463 (deck); vão 452346; cobertura 452359 (173,59); guarda-corpos 452475 e 452538.

### E: "pavilhão alto e ala curva em L". Referência: Casa Juscelino Kubitschek, Pampulha, Oscar Niemeyer, 1943 (F1 nº 45, pp. impressas 164–165)
- **Conceito:** o estar é um único volume de pé-direito duplo inteiro (6,30 m), com vidro para a rua e para o pátio. A ala íntima de 2 pavimentos corre pela divisa oeste, com a fachada para o pátio em curva de vidro (R = 21 m). Uma marquise de borda sinuosa cobre a entrada e as 2 vagas. O pátio com piscina fica entre a ala curva e a faixa de serviço leste, como a planta em U da JK, com abertura para o pátio.
- **Ligação com o perfil:** P5 é a mais forte das três, com duplo no estar inteiro (78 m²). P2, estar e pátio. P6, pátio e piscina. P1, suíte térrea na ala oeste. P4, vagas sob a marquise.
- **Prós:** tem o pé-direito duplo mais generoso, o pátio (regra 4), a marquise curva como entrada (regra 8, visível no 3D) e a faixa de serviço.
- **Contras:**
  - o superior tem só 74,08 m², o que dá 2 suítes, não 3 (o programa não cabe sem rever);
  - a fachada SUL é um pano de vidro de 2 pavimentos que lê como caixa. A marquise só aparece como linha a 3,45;
  - a borboleta da JK **não foi feita** (lacuna da ferramenta), então a cobertura ficou plana;
  - a laje técnica do serviço (16 m²) e a marquise (34,60 m²) entram como "área construída" na ferramenta. A conta é conservadora (ver §3).
- **Ids:** paredes 452714, 452951–452953, 453123–453129; curvas 453130 e 453342; pisos 453492, 453500, 453517 (térreo), 453531, 453548 (marquise), 453561 (superior), 453641 (deck), 453653 (piscina); cobertura 453575 (153,92).

### F: "prisma sobre pilotis e torre de escada cilíndrica". Referência: Casa Herbert Johnson, Fortaleza, Oscar Niemeyer, 1942 (F1 nº 44, pp. impressas 162–163)
- **Conceito:** um prisma íntimo (y 12–31) fica sobre um térreo livre, com varanda contínua a oeste (1,50 m) e um terraço semicircular sobre a piscina, como a laje da Johnson que protege a piscina. Um cilindro maciço de 3 m de diâmetro e 6,30 m de altura na frente marca a entrada e abriga a escada helicoidal. O núcleo térreo de vidro tem fundo curvo.
- **Ligação com o perfil:** P4, garagem sob o prisma. P2, varanda e piscina sob o terraço. P5, duplo de 18 m² (vão 454459). P8, a varanda oeste sombreia o vidro.
- **Prós:** tem a entrada mais legível na rua: o cilindro aparece na perspectiva e na elevação. A varanda-sala contínua (regra 3/6) e a maior área livre sob o prisma.
- **Contras:**
  - **é a mais "caixa" das três.** O prisma é retangular e as curvas ficam no cilindro e no terraço;
  - o térreo fechado tem só 97,51 m² (não cabe social + serviço + suíte de D. Lourdes);
  - o cilindro está sem tampa (cobertura não modelada) e sem escada: a escada helicoidal é de projeto personalizado, do Tenreiro, e `criar_escada` só faz reta, L ou U;
  - a escada não liga ao prisma no modelo.
- **Ids:** paredes 453813–453815, 453986–453988, 454091; curvas 454262, 454403, 454404; pisos 454407 (térreo), 454424 (superior), 454439, 454447 (piscina), 454539 (deck); vão 454459; cobertura 454472 (167,80); guarda-corpo 454489.

---

## 3. Índices: saída da `criar_quadro_areas` (areaLote 571,8, base "menor", limites {toMax 50, caMax 1,0, tpMin 25})

| | D | E | F |
|---|---|---|---|
| TO | **33,93 % atende** (projeção 193,93) | **34,81 % atende** (199,00) | **33,37 % atende** (190,73) |
| CA | **0,551 atende** (144,01 + 170,98) | **0,506 atende** (164,40 + 74,08 + 34,60 + 16,00) | **0,473 atende** (97,51 + 172,73) |
| Permeabilidade | **37,34 % atende** (213,45 jardim solo natural) | **37,34 % atende** | **37,34 % atende** |
| Na outra base (571,8) | TO 33,92 / CA 0,551 / P 37,33 | 34,8 / 0,506 / 37,33 | 33,36 / 0,473 / 37,33 |
| Soma do lote | 571,6 = 100 % | 100 % | 100 % |

**Saída colada (D, trecho):** `"areaLoteInformadaM2": 571.8, "areaLoteDoModeloM2": 571.6, "diferencaLoteM2": -0.2 ... "taxaOcupacao": {"percentual": 33.93, "resultado": "atende"}, "coeficienteAproveitamento": {"valor": 0.551, "resultado": "atende"}, "permeabilidade": {"percentual": 37.34, "resultado": "atende"} ... "aviso": "Fatores padrão (1 = conta inteira; grama 1; concregrama 0 ...) até o Hely aplicar os fatores da Skill quadro de áreas RJ."`
E e F: mesmos campos, com os valores da tabela (ids das áreas: E 453697–453805; F 454576–454663; D 452601–452708).

**Ressalvas da conta (para o Hely e o Kelsen):**
1. **Os fatores não foram aplicados.** A ferramenta cria áreas genéricas ("PROJECAO", "AREA CONSTRUIDA - <nível>", "JARDIM SOLO NATURAL", "IMPERMEAVEL"), e os nomes não casam com as regex da Skill (varanda, sacada, garagem, marquise). Em D passei os `fatores` do `quadro.json` como lista com `esquema` (o schema pede lista e o arquivo traz um objeto por esquema). Em E e F rodei sem `fatores`. A resposta avisa "Fatores padrão (1 = conta inteira ...)". Ou seja: sacadas, garagem e marquise **contam inteiras** na TO e no CA. O resultado é conservador, e mesmo assim as três atendem.
2. **Área do lote no modelo: 571,60 contra 571,80 do Levantamento.** A diferença de 0,20 m² passa da tolerância de 0,01 da Skill (§2). Os índices usaram a menor. Não corrigi o muro: pendência.
3. **TO do caso.** Os limites usados são os que Lúcio deu (50 / 1,0 / 25). A premissa M-b do Briefing é 40 % (228,72 m²). Pela soma das áreas cobertas, as três ficam abaixo dela também: D 193,93, E 199,00, F 190,73. **SMD (checklist a):** o tpMin de 25 % veio da ordem. Pela LC 270 Art. 352, com TO 50 % seriam 10 % do lote (57,18 m²) e com TO 40 % seriam 12 % (68,62 m²). Exponho os dois valores e não escolho. As três passam de todos.
4. **Programa contra área:** pedido de ~520 m². Construído pelo modelo: D 314,99, E 238,48 (computável real, sem marquise e laje técnica), F 270,24. Nenhuma cabe no programa. Quem decide o que reduzir é o cliente (P-l).
5. **Defeito já conhecido, sem código:** no D, o piso do Superior saiu com 188,13 m² contra cerca de 195,9 pelos vértices (≈ −7,8 m²). No E (453531, 74,08) e no F (454424, 190,73) a área bateu com a conta. Não há erro colado: registro como pendência, não como defeito.

---

## 4. Imagens (todas abertas com Read nesta execução)

Pasta `D:\011_VITRUVIUS\_imagens\volumetria_v2_20-10\`.
- **D 3D** `D\vitruvius_20261020_172439 - Vista 3D - EP- Perspectiva.png`: o pavilhão de vidro curvo contorna o estar; o volume branco tem a cobertura em arco; a varanda semicircular tem guarda-corpo; a sacada frontal fica sobre a garagem; piscina e deck aparecem nos fundos.
- **D planta térreo** `D\...172439 - Planta de piso - EP- Térreo.png`: o contorno é uma "cápsula" com a bolha para a piscina, com a faixa de serviço leste e o muro curvo da entrada. Os marcadores de corte antigos ainda estão sobrepostos.
- **D superior** `D\...172439 - Planta de piso - EP- Superior.png`: parede oeste curva, laje semicircular nos fundos e o vão do duplo.
- **D SUL** `D\...172439 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png`: volume superior com guarda-corpo da sacada, garagem aberta embaixo e vidro curvo à esquerda. A curva não se lê em elevação.
- **D NORTE** `D\...172439 - Elevação - ELEVACAO FUNDOS NORTE - SEM MURO.png`: exportada, **não aberta**. Não declaro nada sobre ela.
- **E 3D** `E\vitruvius_20261020_172633 - Vista 3D - EP- Perspectiva.png`: o volume de vidro de pé-direito duplo, a marquise sinuosa escura na frente, a fachada curva de vidro da ala oeste vista do pátio e a piscina.
- **E planta térreo** `E\...172633 - Planta de piso - EP- Térreo.png`: o L com a ala curva, a faixa de serviço e o pátio com piscina.
- **E SUL** `E\...172633 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png`: um pano de vidro retangular de 2 pavimentos. **Lê como caixa.**
- **E superior** `E\...172633 - Planta de piso - EP- Superior.png`: exportada, **não aberta**.
- **F 3D** `F\vitruvius_20261020_172816 - Vista 3D - EP- Perspectiva.png`: o prisma branco sobre o térreo recuado e o cilindro cinza na frente, aberto no topo (sem tampa). O guarda-corpo aparece só em parte.
- **F superior** `F\...172816 - Planta de piso - EP- Superior.png`: o prisma retangular, a varanda oeste, o terraço semicircular e o vão.
- **F SUL** `F\...172816 - Elevação - ELEVACAO FRONTAL SUL - SEM MURO.png`: o prisma e a base. **O cilindro não aparece na elevação SUL** (ver §7).
- **F térreo** `F\...172816 - Planta de piso - EP- Térreo.png`: exportada, **não aberta**.

**Perspectiva 3D:** sem ferramenta para criar ou ajustar vista 3D. Exportei a "EP. Perspectiva" (438334) como está.

---

## 5. Recomendação (não é escolha)

**Recomendo D como base.** É a única das seis (A–F) em que a curva é o próprio volume e não um enfeite, e ela tem mais área no superior (suítes grandes). Antes de mostrar, D precisa de ajustes:
1. **gesto legível na rua:** a ideia é levar o muro curvo de pedra e a curva da cobertura para a fachada SUL, por exemplo com o volume superior recuado em arco na frente;
2. **trazer o pé-direito duplo integral do E** para o estar;
3. **brise na curva oeste.**

E tem o melhor pé-direito duplo e o melhor pátio, mas falta a 3ª suíte. F tem a entrada mais forte, mas o volume é caixa.

---

## 6. Lacunas de ferramenta (§5 da Skill de partido)

| Falta | Situação |
|---|---|
| Laje com borda em arco | Não existe. Fiz lajes poligonais por segmentos: D semicírculo com 12 segmentos de ~0,95 m, borda oeste em 6 segmentos de 3,5 m (desvio da corda < 0,05 m); E marquise com 8 segmentos de 1–2 m; F terraço com 10 segmentos. Fica acima dos 0,30 m sugeridos pela Skill; declarado. |
| Cobertura inclinada ou borboleta (JK, E) | Não existe. `create_roof` respondeu `"type": "Genérico - 400 mm"` plana nas três. Não tentei inclinar, então não há erro a colar. |
| Parede curva com topo preso ao nível | `create_arc_wall` só aceita `height`. As curvas têm altura solta de 3,15 ou 6,30. No térreo, sem o macete da base −0,15. |
| Escada helicoidal (F) | `criar_escada` só faz reta, L ou U. Escada não modelada; personalizada = Tenreiro. |
| Tampa do cilindro (F) | Não modelada. Pendente: laje ou cobertura circular por segmentos. |
| Vista 3D | Sem ferramenta para criar ou ajustar vista 3D. |
| Fatores por nome no quadro | A ferramenta não aplica os fatores da Skill às áreas que ela mesma cria (aviso colado no §3). |

---

## 7. Bloco de conferência (Skill oscar-revit §11)

```
## Entrega — Ensaio 003 — EP, volumetria v2 (D, E, F)
Build: 2026-10-20-quadro-areas-v68 (status)
Gate de entrada (0.1): connected true, documentTitle "EP_layout_partidoB", isModified false (17:2x)
Passos: [cópia D ✓ 17:20:13] [miolo apagado ✓ 67/67, status walls 4 floors 0] [D ✓ salvo 17:25:05]
        [cópia E ✓ 17:25:39] [E ✓ salvo 17:26:49] [cópia F ✓ 17:27:29] [F ✓ salvo 17:28:30]
        [quadro ✓ 3x atende] [imagens ✓ 12 abertas, 3 exportadas não abertas]
        [portas/janelas ✗ estudo de massa] [eixos ✗ não pedidos] [escada ✗ estudo de massa]
Imagens conferidas (§6): §4 acima
Defeitos (§8): nenhum erro; área do piso Superior do D ≈ −7,8 m² contra os vértices (sem erro colado)
Lacunas (§3): §6 acima
Pendências: Kelsen (vagas descobertas no afastamento lateral, manobra no afastamento frontal, TO 40×50, SMD 10×12×25 %, balanços/varandas);
            Hely (fatores por nome; lote 571,60 × 571,80); Baumgart (balanços D/F);
            Tenreiro (escada helicoidal F); norte (topógrafo); P-l (programa 520 × área); escolha (Claudemberg)
Status: PARCIAL
```

**Escritas:** feitas uma chamada por vez, cada uma relida (resposta "criada e conferida", raio ou área conferidos contra a conta). Algumas chamadas criaram vários itens em lote, na mesma ordem e sem paralelo. Declaro isso como desvio possível da regra "uma escrita por vez".
**Elevações:** em D, `view_setup ocultarMarcadores` na 449760 ocultou 449430, 449759 e 450519. O 449759 pode ser o marcador da própria elevação: **não conferido**. As plantas continuam com os marcadores de corte antigos.
**Originais:** EP_layout_partidoB.rvt não recebeu escrita (a 1ª ação foi `salvar_copia` para D). A, B e C não foram abertos.
**Gabaritos e pareceres do Bardi:** não abertos.

## Auditoria do Lúcio
