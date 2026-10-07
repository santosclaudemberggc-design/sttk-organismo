# Peça 1 (v5) — Levantamento Planialtimétrico Cadastral orientado ao DULI
## Ensaio Sombra 003, Etapa 03. Montenegro Prates (100% FICTÍCIO)

**Oscar (Assisted) | Auditoria: Lúcio | 07/10/2026, v5.** Análise preliminar, sujeita ao Gate do Maurício num caso real. **Lote:** Rua das Garças, Lote 17, Quadra C, Condomínio Reserva das Garças, Recreio (AP4) (caso §3).
**Etiquetas:** (a) dossiê (caso §1–§4; 5.1–5.15); (b) premissa do Legal (Hely, Kelsen, ERRATA 4.1), da Viabilidade ou de Skill; (c) pendente: o que falta e quem fornece. Contas: `anexo_contas_003_v5.md` (C-n).

## 0. Limites

- **Revit:** chamada única, em 06/10/2026, com retorno `Error: No such tool available: mcp__vitruvius__revit_status`. Não há desenho simulado. O croqui é descritivo, com coordenadas.
- **Sem visita:** o POP-PROJ-01 exige conferência presencial. O que não está no dossiê aparece como "não consta" e vai para o §7.
- **O 5.2 não basta para o DULI.** É só perímetro e área, "restrito ao perímetro; espelho d'água não levantado". Faltam RN, curvas, perfil natural, PAA, passeio, PVs, postes e árvores (Skill de levantamento §3, §5).
- **O 5.2 também não basta para a NBR 6492:2021 5.1**, que pede relatórios ambientais (marés e ventos), urbanísticos, alagáveis e fotos (Skill `nbr6492-...` §2-§3). Ver o §7.1.
- **Destino do DULI:** é peça do Projeto Legal, na Etapa 07, e não do Executivo (Etapa 15), como diz o enunciado (caso §6; parecer T8). Este levantamento alimenta o DULI, mas não é o DULI.

## 1. Referencial e croqui

- O = (0;0) no vértice frente-esquerda, na face do **muro do Lote 16**, a partir do qual se medem os afastamentos (parecer §2.1, §5.2) (b).
- x ao longo da testada, da esquerda para a direita. y da rua para os fundos.
- Aproximação retangular de **14,29 × 40,00** (menor largura e menor lateral; parecer §2.3). O lote real tem 14,30 / 14,29 / 40,00 / 40,02, sem ângulos nem vértices (c).
- A área oficial é **571,80 m²**.
- Altimetria: só a soleira **prevista** de +3,20 (referencial do condomínio). Não atribuo z ao terreno.

```
 y (m)
 52,00  ~~~~~~~~ margem do lago (5.5: 12,00 m além da divisa de fundos) ~~~~~~~~
        |         faixa verde comum do condomínio, 12 m (5.5) — fora do lote   |
 40,00  +================= divisa de fundos (14,29 m medidos) ==================+
        |  FAIXA DE FUNDOS 5,00 m  (y 35,00–40,00)                            |
 35,00  |----+----------------------------------------------------+----------|
        | L  |   ENVELOPE H0: x 2,50–11,79 ; y 6,00–35,00          |  L   ed. |  <- edícula: face a
        | A  |   9,29 × 29,00 = 269,41 m²  (zona de implantação   |  A  x≈13,49 0,80 m da divisa
        | T  |   possível; varandas só aqui dentro)               |  T       |     direita (5.2); y e
 22,00  |-E--|- - - - - linha H1 (30 m da margem = y 22,00) - - - -|--D-------|     dimensões: não
        | S  |   ENVELOPE H1: y 6,00–22,00 → 9,29 × 16,00 = 148,64 |  I       |     constam
        | Q  |                                                    |  R       |
  6,00  |----+---- face frontal de qualquer pavimento: y ≥ 6,00 ------+----------|
  5,60  |    .  .  .  só jardineira/ar-condicionado, acima do térreo (XIV)    |
        |  AFASTAMENTO FRONTAL 6,00 m (y 0–6,00): ipê + 2 amendoeiras (caso §3);|
        |  locação e DAP: não constam                                          |
  0,00  O================== alinhamento / testada (14,30 m medidos) ==========+
        x=0 (muro Lote 16)  x=2,50                                x=11,79   x=14,29
                            RUA DAS GARÇAS (passeio, meio-fio, postes, PVs: não constam)
```

| Elemento | Coordenadas / medida | Fonte |
|---|---|---|
| Lote (aproximação) | x 0–14,29; y 0–40,00 | 5.2; parecer §2.3 |
| Envelope H0 | x 2,50–11,79; y 6,00–35,00 (269,41 m²) | parecer §2.3; 5.4 Art. 6º |
| Limite das varandas | dentro do envelope | Skill `varandas` §4.1; COES Art. 8º §2º; Peça 2 §3.2 |
| Saliência frontal (XIV) | até y = 5,60, acima do térreo | Skill `decreto3046` §6 |
| Linha H1 | y = 22,00 | parecer §2.4, §5.2 |
| Margem do lago | y ≈ 52,00 | 5.5 |
| Face da edícula | x ≈ 13,49 | 5.2 + conta (C-14) |
| Casa de 1998 | ~180 m²; posição não consta | caso §3 |
| Piscina | não consta | caso §3, §4 |
| Árvores (3) | y 0–6,00; x, DAP e copa não constam | caso §3 |

O EXEMPLO do enunciado (casa no meio, edícula de 20–30 m², piscina de 4 × 8) não é documento e não é usado.

## 2. Dimensões: título × medida

- **Título:** 15 × 40 = **600,00 m²** (5.1; RIU 5.3; escritura 5.11).
- **Medido:** 14,30 / 14,29 / 40,00 / 40,02 = **571,80 m²** (5.2).
- **Diferença:** −28,20 m² (C-1).
- **Motivo:** o muro do Lote 16 "avança sobre a linha do PAL" (5.2). O avanço não foi medido. Atribuir os 28,20 m² ao muro (0,70 × 40 = 28,00) é inferência do Legal (parecer §2.1), e a prova vem de T5.
- **Área adotada: 571,80 m²**, com os afastamentos medidos a partir do muro. É premissa recomendada; o efeito é patrimonial, e quem decide é o cliente com advogado (Kelsen R1). O cenário de 600 só vale com a divisa regularizada.
- **Ao DULI** vão as medidas do título **e** as medidas locais (LICIN Anexo I, III, item 1; Skill §3).

## 3. Altimetria

| Item | Situação |
|---|---|
| Cota de soleira | +3,20 **prevista** (5.2), não atual como diz o enunciado; referencial do condomínio (a) |
| Amarração oficial / Art. 458 | Não confirmada. Se der < 3 m, há avaliação técnica (parecer, linha 19) (c: T3; Kelsen/Hely) |
| Topo | +3,20 + 8,50 = **+11,70**, se a soleira ficar em +3,20 (5.4 Art. 7º) |
| Terreno atual, curvas, aclives, depressões | Não constam. As curvas vêm **a cada 1,00 m** (NBR 6492 5.1.1 b) (c: T1, T4) |
| RN do meio-fio | Não consta (DULI, Planta de situação item 8; Cortes item 4) (c: T2) |
| Perfil natural e aterro | Não constam. O "natural" é decisão do Hely (R2) (c: T4) |
| Aterro até +3,20 | Não calculável |
| NA | **0,90 m** (5.7, não 5.2 como diz o enunciado) |
| Piso térreo da casa nova | Soleira = cota de implantação (Skill §2 III). Piso acima da soleira consome altura. O valor depende de T2, T3, T4 e R2 e é fixado no EP |

## 4. Edificações existentes

| Edificação | Dossiê | Não consta |
|---|---|---|
| Casa de 1998 | Térrea, ~180 m², **existente e a demolir** (caso §3), e não "demolida", como diz o enunciado. Não averbada (5.1). Habite-se de 1999 (5.8). Demolição orçada (Mascaró v8 §6.4) | Posição, dimensões, cota |
| Edícula | Churrasqueira e depósito, a **0,80 m** da divisa direita, com janela para a divisa (5.2). Fora do Habite-se (5.8). O cliente quer mantê-la (caso §4) → Peça 2 §5.1 | Área, dimensões, y, altura, cota |
| Piscina | Existe. O cliente quer mantê-la → Peça 2 §5.2 | Posição, dimensões, profundidade, cota, estado, Habite-se |

**Cores do DULI** (Skill §5; LICIN Anexo I IV.2): amarelo para demolir (casa e edícula), vermelho para novo ou a legalizar, preto para manter. A piscina fica indefinida até ser levantada.

## 5. Vegetação

Há 1 ipê-amarelo e 2 amendoeiras no frontal (caso §3). Locação, DAP, copa, altura e estado não constam. O levantamento precisa trazer:
- posição, espécie e DAP de cada árvore (Skill de levantamento §4-§5; Skill `remocao` §4);
- a arborização do passeio (COE Art. 35 §4º);
- as árvores na planta (NBR 6492 5.1.1 b).

## 6. Acessos, vizinhança e corpo hídrico

- **Acessos:** o lote é de meio de quadra, e só a frente é documentada. Acesso pelos fundos atravessa área comum e não é presumido (c: condomínio). Portão, rebaixo, passeio, postes, PVs, acesso de pedestres e de serviço não constam. O COE Art. 35 §§2º-3º condiciona o acesso (T7).
- **Vizinhança:**
  - Esquerda: Lote 16, com muro avançando. As construções não constam.
  - Direita: confrontante não identificado; o DULI exige o número (Skill §3 item 5).
  - Fundos: faixa verde de 12 m (5.5).
  - Muros e casas vizinhas não constam. Interessam a Baumgart, pelo risco de recalque (Skill `rebaixamento` §6), e à NBR 6492 5.1.1 a/c.
- **Lago:**
  - "~1 ha", com margem a **12,00 m** da divisa de fundos (5.5).
  - O 5.5 diz "sem ligação"; o 5.9 fala em maré 2x/dia e manilha até o canal. Não decido entre as fontes: decidem medição (oscilação ≥ 5 cm, DL 9.760 Art. 2º p.ú.), SPU e SMAC. Se a ligação se confirmar, entra a LC 270 Art. 216 V (Kelsen R2).
  - O espelho d'água não foi levantado, e "~1 ha" não prova < 10.000 m² (LC 270 Art. 215 §2º; Lei 12.651 Art. 4º §4º). M1 e M2 nunca se presumem (Skill `decreto3046` §6).
  - Regime de marés e áreas alagáveis são obrigatórios pela NBR 6492 (T14, T19, T22).
  - APP (SMAC), FMP (INEA) e marinha (SPU) são 3 questões com 3 donos. Nenhuma é resolvida aqui.

## 7. Complementação (encomenda de Oscar via Lúcio; contrata o cliente; assina o responsável de cada item)

- **T1** Planialtimétrico cadastral com curvas a cada 1,00 m; classe pela NBR 13133 (não lida, R1). Responsável: topógrafo. Fonte: NBR 6492 5.1.1 b; DULI item 8.
- **T2** RN do meio-fio, com cota na planta. Responsável: topógrafo. Fonte: DULI, situação item 8 e cortes item 4.
- **T3** Amarração do +3,20 ao referencial oficial. Responsável: topógrafo. Fonte: LC 270 Art. 458.
- **T4** Terreno atual em malha, perfil natural, aterro. Responsável: topógrafo. Fonte: DULI, cortes 3 e 6; M4.
- **T5** Vértices, ângulos, linha do PAL × muro do Lote 16. Responsável: topógrafo. Para provar os 28,20 m².
- **T6** Alinhamento com nº do PAA e largura do passeio. Responsáveis: topógrafo + cliente. Fonte: DULI item 2; R3.
- **T7** Postes (mesma calçada ou oposta), PVs, PVIs, rebaixos, portões, árvores do passeio, drenagem. Responsável: topógrafo. Fonte: DULI item 6; COE Art. 35.
- **T8** Casa: contorno, projeção, cota. Responsável: topógrafo. Para a demolição e o DULI.
- **T9** Edícula: contorno, área, altura, vãos, distância a cada divisa. Responsável: topógrafo. Para a Peça 2 §5.1.
- **T10** Piscina: contorno, profundidade, cotas da borda e do fundo, estado. Responsáveis: topógrafo + laudo de Baumgart/Cardozo. Para a Peça 2 §5.2.
- **T11** Árvores: locação, espécie, DAP, copa, altura; laudo fitossanitário. Responsáveis: topógrafo + Glaziou. Para a Peça 2 §3.3 e §5.3.
- **T12** Confrontantes com número, muros e construções vizinhas. Responsável: topógrafo. Fonte: DULI item 5; vistoria cautelar.
- **T13** Espelho d'água (contorno e área), margem × divisa, manilha. Responsável: topógrafo, com autorização do condomínio. Fonte: Lei 12.651 Art. 4º §4º; LC 270 Art. 215 §2º.
- **T14** Régua ou marégrafo no lago (oscilação ≥ 5 cm). Responsável: topógrafo. Fonte: DL 9.760 Art. 2º p.ú.
- **T15** Norte verdadeiro e calçamento (tipo e estado). Responsáveis: topógrafo + vistoria. Fonte: POP-PROJ-01 Seção 3; NBR 6492 5.1.1 b.
- **T16** DWG/DXF georreferenciado. Responsável: topógrafo. Para entrar no Revit sem redesenho.
- **T17** Sondagem: posição dos 3 furos, data do NA, suficiência dos furos. Responsáveis: Baumgart/Cardozo. Fonte: Skill de fundações §6, R7 (NBR 8036).
- **T18** Clima com fonte: temperatura, chuva, insolação (sombras das vizinhas e das árvores), ventos. Responsável: Oscar, via Lúcio. Fonte: NBR 6492 5.1.2.
- **T19** Regime de marés com fonte; cotas máxima e mínima do lago. Responsáveis: topógrafo + Oscar. Fonte: NBR 6492 5.1.2; 5.9.
- **T20** Poluição do ar, do solo (aterro), da água e sonora, com responsável e método. Responsável: profissional habilitado (Oscar especifica). Fonte: NBR 6492 5.1.2.
- **T21** Entorno, infraestrutura (água, esgoto, drenagem, energia, gás, telecom), tráfego e horário de obra. Responsáveis: Oscar + concessionárias + condomínio. Fonte: NBR 6492 5.1.2.
- **T22** Áreas alagáveis: marcas de cheia, cota máxima do lago, acúmulo, saída da drenagem. Responsáveis: topógrafo + vistoria + condomínio. Fonte: NBR 6492 5.1.1 b.
- **T23** Fotos com pontos de vista locados (testada, árvores, edícula e janela, piscina, muro, divisas, faixa verde, lago, manilha). Responsável: Oscar, na vistoria. Fonte: NBR 6492 5.1.2; critério 1; POP-PROJ-01 (não relido).
- **T24** Plantas cadastrais da vizinhança; cortes e elevações do terreno com as edificações. Responsável: topógrafo. Fonte: NBR 6492 5.1.1 a/c.
- **T25** Divisas de matrícula, áreas de preservação e servidões (com certidão atualizada). Responsáveis: topógrafo + cliente/advogado. Fonte: NBR 6492 5.1.1 b; 5.1.

### 7.1 NBR 6492:2021 5.1: item exigido × dossiê (Skill `nbr6492-...` §2-§4)

| Item | Dossiê | T |
|---|---|---|
| 5.1.1 a) Cadastro da vizinhança | Só o muro do Lote 16 | T12, T24 |
| 5.1.1 b) Curvas a cada metro | Não | T1 |
| 5.1.1 b) Corpos hídricos | Só o memorial | T13 |
| 5.1.1 b) Alagáveis | Não | T22 |
| 5.1.1 b) Árvores | Existência | T11 |
| 5.1.1 b) Construções | Existência; 0,80 m da edícula | T8–T10 |
| 5.1.1 b) Postes e drenagem | Não | T7 |
| 5.1.1 b) Divisas de matrícula | Medidas; sem vértices nem PAL | T5 |
| 5.1.1 b) Preservação e servidão | H1/H2/H3 abertos; servidão não mencionada | T13, T14, T25 |
| 5.1.1 b) Norte | Não | T15 |
| 5.1.1 c) Cortes e elevações com vizinhas | Não | T24 |
| 5.1.2 Topografia | Parcial (5.2) | T1–T7 |
| 5.1.2 Sondagem | 5.7 (3 furos, NA 0,90, argila mole 2,5–9,0, areia > 11); sem posição nem data | T17 |
| 5.1.2 Vizinhança | Não | T12, T21, T24 |
| 5.1.2 Clima | Não | T18 |
| 5.1.2 Marés com fonte | Só o relato (5.9) | T14, T19 |
| 5.1.2 Poluição | Não | T20 |
| 5.1.2 Urbanísticos | Só "46 lotes" (5.4) | T21 |
| 5.1.2 Legislativos | Etapa 01 (inclui CBMERJ e APAC); falta o PAA | T6 |
| 5.1.2 Fotos | Não (sem visita) | T23 |

**Conclusão:** o Levantamento está **incompleto** pela NBR 6492. Só os dados legislativos e a sondagem, com ressalvas, estão cobertos. Nada foi inventado.

## 8. Skills e fontes

Skill de levantamento §2-§5, R1-R3; `nbr6492-2021-memoriais-...` §2-§4; `varandas-...` §4.1; `decreto3046-...` §4, §6; `remocao-arvores-...` §4; `fundacoes-...` §6, R7, M4; `rebaixamento-...` §6. Etapa 01: Hely §§1, 2.1–2.4, 5.2, 5.4; Kelsen R1, R2, ERRATA 4.1. Etapa 02: 5.11–5.15; Mascaró v8 §1, §6.4, §8; Villaça v9 §5.

## 9. Declaração

Caso fictício. Nada foi protocolado. Não abri nem listei nada em `_gabaritos`. Para esta v5, li só, por caminho exato e por ordem de Lúcio: o `parecer_bardi_v4.md`, o `enunciado.md` e a entrega v4 (Peça 1, Peça 2, Peça 3 e `anexo_contas_003_v4.md`), que ficou intocada, além do meu arquivo de estado. A nota 00 da v4 não foi lida nem copiada. Na v5: só correção de remissões e de rótulos, sem mudança de conteúdo.

— Oscar, 07/10/2026 (v5)
