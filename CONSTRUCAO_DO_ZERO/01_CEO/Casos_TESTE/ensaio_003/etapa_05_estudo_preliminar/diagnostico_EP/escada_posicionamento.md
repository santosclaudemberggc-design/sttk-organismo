# Posicionamento da escada — EP_diagnostico_19-10.rvt (treino da Skill posicionamento-escada-residencial v1.0)

Oscar, 19/10/2026, pedido de Lúcio (origem: Claudemberg). Build `2026-10-19-escada-areas-livres-v60`. Gate 0.1: conectado, documento `EP_diagnostico_19-10`, caminho do caso, isModified false no início. Níveis não alterados: térreo 311 (0,30), superior 694 (3,30).

## 1. Leitura das plantas (antes)

- Térreo: CIRCULACAO ESCADA (449385) x 7,575–11,64 × y 17,075–22,925 (4,065 × 5,85). Portas: entrada pivotante 449344 na parede leste (x 11,715; y 19,975); 449369 para a Cozinha Gourmet na parede x 7,5 (y 19,25). Sem passagem para o Estar (parede 449338 em y 23 cheia).
- Superior: CIRCULACAO ESCADA SUPERIOR (449420) x 7,575–11,64 × y 13,075–19,925 (4,065 × 6,85). Portas: 449409 Home Office (y 13), 449408 Home Cinema (x 7,5; y 16,575), 449407 Suite 4 (y 20).
- Interseção das duas circulações em planta: y 17,075–19,925 = **2,85 m**. Altura 3,00 m: 18 espelhos; reta = 17 × 0,28 = 4,76 m; U 9+9 = 2,24 + patamar 1,00 = 3,24 m de comprimento × 2,10 m de largura.
- Imagens (antes): `D:\011_VITRUVIUS\_imagens\escada_19-10\antes\vitruvius_20261019_194343 - Planta de piso - EP- Térreo.png` e `...\antes\vitruvius_20261019_194343 - Planta de piso - EP- Superior.png` (abertas: circulação do térreo entre cozinha e estar com a entrada a leste; a do superior está deslocada 4 m para o sul em relação à do térreo).

## 2. Posições comparadas

| # | Formato | Começa (térreo) | Chega (superior) | Área livre partida / chegada (medida) | Embaixo | Prós | Contras (regras §2) | Resultado |
|---|---|---|---|---|---|---|---|---|
| A | U, lances no eixo x, só na interseção (y 17,1–19,9) | oeste da circulação, subindo para leste | mesmo lado (oeste) | 1,00 × 1,20 exige 1,20 + 3,24 = 4,44 m > 4,065 disponíveis | — | sem mexer em parede | não cabe (falta 0,375 m); a porta da Suite 4 (x 9,075, y 20) ficaria atrás do vão, só 0,6 m de faixa (regras 1 e 7) | descartada |
| B | Reta, eixo y | térreo, subindo para sul a partir de y 21,7 | y ~17,0 | partida 1,00 × 1,20 cabe; mas o lance (4,76) bate na parede y 17 | — | escada simples | atravessa a parede 449337 do térreo; o vão no superior invade a Suite 4 (y > 20) (regra 6) | descartada sem mexer em parede grande |
| C (escolhida) | **U 9+9, lances no eixo y**, encostada a oeste da circulação, com a parede 449403 do superior levada de y 20 para y 22 | térreo, 1º espelho em (9,225; 18,35), sobe para norte | superior, chega em y 18,35 descendo do patamar para sul, faixa x 7,63–8,63 | partida x 8,72–9,72 × y 17,15–18,35 = 1,00 × 1,20; chegada x 7,62–8,62 × y 17,15–18,35 = 1,00 × 1,20 (medidas pela ferramenta) | térreo: alto do 2º lance (lado oeste) livre para armário/depósito sob a escada | partida e chegada empilhadas no mesmo núcleo (regra 6); circulação do superior distribui para Home Office, Home Cinema e Suite 4 sem corredor (regra 4); entrada a leste com faixa livre de 1,91 m ao lado da escada; não fica de frente para a porta da rua (regra 5) | Suites 3 e 4 perdem 2 m de profundidade (46 → 37 m²); a porta da cozinha teve de descer | **escolhida** |

**Motivo (uma frase):** é a única posição em que partida e chegada caem dentro das duas circulações, empilhadas, com 1,00 × 1,20 livres, ao custo de deslocar uma parede do superior em 2 m.

## 3. Mudanças de layout

| Id | Elemento | Mudança | Motivo |
|---|---|---|---|
| 449403 | parede interna superior (Home Cinema/Suite 3 × Circulação/Suite 4) | movida dy +2,00 (y 20 → 22). Relida: 449404 passou a ir até y 22 e 449406 a começar em y 22 (seguiram pela junção) | vão da escada (até y 21,59) precisa ficar inteiro dentro da circulação do superior |
| 449407 | porta .80 da Suite 4 (hospedada em 449403) | andou com a parede para y 22 e depois dx +1,60 (x 9,075 → 10,675). Relida (10,675; 22) | ficar na faixa livre leste ao lado do vão, não atrás dele |
| 449411 | porta .80 Home Cinema × Suite 3 | só andou com a parede (4,875; 22). Relida | — |
| 449369 | porta .80 Circulação × Cozinha Gourmet (térreo) | dy −1,65 (y 19,25 → 17,60). Relida (7,5; 17,6) | sair de baixo do 2º lance e do lado da área de partida |

Efeito em áreas (imagem): Suite 3 e Suite 4 Master 46 → 37 m²; Home Cinema 33 → 42 m²; Circulação superior 28 → 36 m².

## 4. Resposta da criar_escada (colada)

1ª tentativa (folgaVao padrão 0,05) — RECUSADA:
```
Error: área livre de chegada (depois do último degrau) (x 7,63–8,63, y 17,15–18,35 em 'Páv. Superior') cai dentro do vão da escada.
```
Leitura: com folga de 0,05 o vão começa em y 18,30 e encosta 5 cm na área de chegada. Repetido com `folgaVao: 0` (parâmetro da ferramenta, não desliga conferência; as conferências de área livre, paredes e contagem continuaram ativas). **Lúcio deve julgar se folga 0 é aceitável** (ver §7).

2ª tentativa — criada:
```
{"id":"450364","tipo":"ESCADA PROJETO","formato":"u","levelId":"311","topLevelId":"694","alturaM":3,"espelhos":18,"espelhoM":0.1667,"pisoM":0.28,"larguraM":1,"regraConforto_cm":61.3,"lances":[9,9],
"pegada":{"xMin":7.625,"yMin":18.35,"xMax":9.725,"yMax":21.59},"alturaLivreMinimaM":2.1,
"areasLivres":{"partida":{"ambiente":"CIRCULACAO ESCADA","portasDoAmbiente":2,"xMin":8.72,"yMin":17.15,"xMax":9.72,"yMax":18.35},
"chegada":{"ambiente":"CIRCULACAO ESCADA SUPERIOR","portasDoAmbiente":3,"xMin":7.62,"yMin":17.15,"xMax":8.62,"yMax":18.35}},
"extras":{"vaoId":"450472","guardaCorpoVaoIds":["450475","450480"],"corrimaoIds":["450399","450403"],"corrimaoRemovidos":0}}
message: "Escada criada e conferida"
```
Espelho real 0,1667 (18 × 0,1667 = 3,00), não 0,175: o Revit arredondou para cima o número de espelhos. Blondel 2e+p = 61,3 cm.

Corte novo: `CORTE ESCADA` id 450520, linha x 9,00 de y 32 para y 4, 1:100, detalhe médio, Etapa/Sub Etapa gravadas. O corte CC 450303 não foi usado (não conferi se passa pela escada).

## 5. Prova pela imagem (abertas com Read nesta execução)

- `D:\011_VITRUVIUS\_imagens\escada_19-10\depois\vitruvius_20261019_194500 - Planta de piso - EP- Térreo.png` — a pessoa entra pela porta pivotante leste, anda pela faixa livre ao lado direito da escada até a ponta sul da circulação (junto da parede do Serviço), vira para norte e sobe ("Acima" marcado na partida). Porta da cozinha agora na ponta sul da parede oeste, fora da escada. Etiqueta "12 / 24 m²" cai sobre a escada (limpeza pendente).
- `...\depois\vitruvius_20261019_194500 - Planta de piso - EP- Superior.png` — a pessoa chega no lado oeste da escada, voltada para sul, numa área livre da circulação ("Abaixo"); dali segue para a porta do Home Cinema (oeste, logo ao sul), para o Home Office (sul) ou, pela faixa leste ao lado do vão, para a Suite 4 (porta no canto nordeste). Vão com guarda-corpo inteiro dentro da circulação; nenhum quarto invadido.
- `...\depois\vitruvius_20261019_194500 - Corte - CORTE ESCADA.png` — U com dois lances, patamar a meia altura junto da parede norte da circulação, guarda-corpo no vão do superior; porta da cozinha (térreo) aparece à esquerda da escada, sem conflito.

## 6. Salvar (colado)

```
{"caminho":"D:\\000_ESTRUTURA DEPARTAMENTO DE PROJETO\\CONSTRUCAO_DO_ZERO\\01_CEO\\Casos_TESTE\\ensaio_003\\etapa_05_estudo_preliminar\\diagnostico_EP\\EP_diagnostico_19-10.rvt","tinhaAlteracoes":true,"tamanhoBytes":18026496,"dataHora":"2026-10-19T19:45:11","modificadoDepois":false}
message: "document salvar executado"  (requestId oscar-escada-19-10-salvar-01)
```

## 7. O que a Skill não cobriu e deveria (v1.1)

1. **Folga do vão × área de chegada:** a ferramenta trata a folga de 5 cm do vão como invasão da área de chegada em U. A Skill deve dizer se a área livre conta a partir do último espelho ou da borda do vão, e se `folgaVao: 0` é aceito.
2. **Circulações desalinhadas entre pavimentos:** falta o passo "sobreponha as duas circulações e meça a interseção antes de escolher formato" (aqui era 2,85 m, e isso decidiu tudo).
3. **Critério de quanto layout se pode mexer:** a Skill fala em "ajuste mínimo", mas não diz quanto de área de quarto é aceitável perder (aqui 9 m² em cada suíte) nem quem aprova.
4. **Portas atrás do vão:** regra 7 cobre porta sobre degrau e nas áreas livres, não porta que fica inacessível atrás do vão/guarda-corpo (caso da Suite 4).
5. **Espelho real ≠ espelho pedido:** registrar que o Revit ajusta (0,175 → 0,1667) e qual faixa é aceitável.
6. **Etiqueta de ambiente sobre a escada:** incluir na prova pela imagem.
7. **Circulação que não leva ao social:** a circulação do térreo não tem passagem para o Estar (parede 449338 cheia). A regra 3 ("une") foi ferida pelo layout de origem; não mexi (fora do pedido). Pendência para Lúcio.

## Auditoria do Lúcio

19/10/2026. Conferi por amostragem as duas plantas "depois", abertas com Read, e a resposta do salvar colada pelo Oscar.

| Item | Prova | Resultado |
|---|---|---|
| Documento certo, níveis intactos | status colado pelo Oscar (EP_diagnostico_19-10, isModified false) | OK (declarado com log) |
| Superior: vão inteiro dentro da CIRCULACAO ESCADA SUPERIOR, chegada com saída | imagem EP. Superior: vão com guarda-corpo dentro do ambiente 17 (36 m²); dali saem as portas do Home Cinema, Home Office e Suítes 3/4 | atende regras 1, 6 e 7 |
| Térreo: partida dentro da CIRCULACAO ESCADA | imagem EP. Térreo: escada no ambiente 12, "Acima" no lado sul, faixa livre a leste | atende regra 1 |
| Térreo: circulação une social e serviço | imagem EP. Térreo: parede entre CIRCULACAO ESCADA e ESTAR JANTAR é cheia; a circulação só tem a porta da rua (leste) e a porta da cozinha | **NÃO atende regra 3** ("une, não isola") |
| Salvar | JSON colado, tinhaAlteracoes true, modificadoDepois false | OK |
| Corte | imagem não aberta por mim | não verificado |

**Veredito: não aprovado como solução final de EP.** A escada em si passou nas conferências da ferramenta e está bem posta nos dois pavimentos. Ficam abertas:
1. Regra 3: abrir passagem entre CIRCULACAO ESCADA e ESTAR JANTAR (parede 449338). Próxima ação do Oscar.
2. `folgaVao` 0 em vez de 0,05: aceitação depende de Claudemberg (é parâmetro de conferência, mesmo sem desligá-la).
3. Suítes 3 e 4 perdem 9 m² cada: decisão de programa, vai para Claudemberg/cliente, não é minha nem do Oscar.
4. Espelho real 0,1667 em vez de 0,175: aceitável (mais confortável), registrar na Skill.
5. Etiqueta do ambiente 12 sobre a escada: ajuste de representação.

Para a v1.1 da Skill, além dos 7 pontos do Oscar: conferir a regra 3 no pavimento de partida antes de chamar `criar_escada` (a ferramenta não confere ligação com o social).

## Passagem circulação–Estar (19/10)

Pedido de Claudemberg, que aceitou a posição da escada 450364. O trabalho foi executado pelo Oscar e auditado pelo Lúcio.

**Leitura (Oscar):** a parede 449338 vai de (2,575; 23) a (11,715; 23). A CIRCULACAO ESCADA 449385 ocupa x 7,575–11,64 e y 17,075–22,925. O ESTAR JANTAR 449386 ocupa y 23,075–30,47. A escada ocupa x 7,625–9,725. A partida livre de 1,00 x 1,20 fica em x 8,72–9,72, y 17,15–18,35. A faixa leste, de x 9,725 a 11,64, está livre. O modelo não tem tipo de passagem sem folha: foram listados 20 tipos de porta e nenhum é vão livre.

| | A: correr quádrupla 2320 (tipo 339691) | B: entrada dupla de abrir 1640 (tipo 376138) |
|---|---|---|
| Posição | centro (10,35; 23), vão x 9,15–11,55 | centro (10,70; 23) |
| Fluxo hall → escada → estar | 2,32 m em linha com a faixa leste | 1,64 m, mais estreita |
| Área livre da partida | não invade (a 4,6 m) | não invade |
| Privacidade da escada | aberta, une; fechada, separa com vidro | isola mais |
| Contras | vidro; o Revit mostra porta, não vão | as folhas giram na faixa ao norte da escada |

**Escolhida: A.** É a que melhor cumpre a regra 3 ("une, não isola"), não tem folha girando na circulação e, aberta, funciona quase como vão livre.

**Execução:** porta **450601**, tipo 339691 "2320 x 2180mm", hospedada na parede 449338, nível 311. Ponto relido em (10,35; 23; 0,3); bbox x 9,147–11,553. Arquivo salvo às 19:50:13 (requestId oscar-passagem-19-10-salvar-01), com tinhaAlteracoes true e modificadoDepois false.

**Imagens:**
- Antes: `D:\011_VITRUVIUS\_imagens\passagem_19-10\antes\vitruvius_20261019_194952 - Planta de piso - EP- Térreo.png`
- Depois: `D:\011_VITRUVIUS\_imagens\passagem_19-10\depois\vitruvius_20261019_195007 - Planta de piso - EP- Térreo.png`

### Auditoria do Lúcio (passagem)

| Item | Prova | Resultado |
|---|---|---|
| Documento certo | status colado (EP_diagnostico_19-10, caminho do caso, isModified false) | OK (declarado com log) |
| Tipo existente, sem tipo novo | lista de 20 tipos colada; 339691 está nela | OK |
| Passagem aberta no trecho da circulação | imagem "depois" aberta por mim com Read: porta de correr no trecho leste da parede entre o 12 e o 13; o trecho da cozinha continua cheio | atende a regra 3 |
| Partida da escada livre | coordenadas: vão em y 23, partida em y 17,15–18,35 | não invade |
| Caminho do Estar à escada | imagem: do Estar passa-se pela porta de correr, segue para o sul pela faixa leste da circulação (passando pela porta da rua) e chega à partida "Acima" | contínuo |
| Salvar | JSON colado | OK |

**Veredito: aprovado para o pedido** (passagem aberta). Não é aprovação do EP. Ficam pendentes:
1. Trocar por vão livre de verdade exige família de passagem sem folha, que não existe no modelo. Decisão de Claudemberg.
2. Etiqueta do ambiente 12 sobre a escada.
3. `folgaVao` 0 e os 9 m² das suítes, que já estão com Claudemberg.

## Vão livre circulação–Estar (19/10)

Pedido de Claudemberg (após sabatina), pela Skill posicionamento-escada-residencial v1.1, seção 2-bis: trocar a porta de correr 450601 por vão livre. A decisão das medidas é do Oscar, que só leu o modelo. A execução foi de Wallenberg pelo plugin (build v62), porque a ferramenta não carregou na sessão do Oscar.

**Decisão (Oscar):** parede 449338, centro {9.6075, 23.0}, largura 3,865 m, altura 2,40 m, base 0,00.
- Folgas: face leste da 449339 = 7,575, mais 0,10, dá início em 7,675. Face interna da 449333 = 11,640, menos 0,10, dá fim em 11,540.
- Motivo: abrir todo o trecho da circulação para o Estar. A escada passa a fazer parte do social e é vista do Estar, o fluxo Estar → escada fica direto e sem porta, e a partida da escada fica intacta.

**Respostas coladas (Wallenberg):**
- delete: `{"success":true,"elementosRemovidos":["450601"],"totalRemovidos":1}`
- criar_abertura_parede: `{"id":"450603","wallId":"449338","larguraM":3.865,"alturaM":2.4,"baseM":0,"trechoNaParede_m":{"de":5.1,"ate":8.965,"comprimentoParede":9.14}}`
- corte novo: 450605, "CORTE DD - VAO CIRCULACAO ESTAR (19-10)", linha em y 22,4 olhando para o Estar.
- salvar: `{"tinhaAlteracoes":true,"dataHora":"2026-10-19T20:49:08","modificadoDepois":false}`

**Imagens:**
- `D:\011_VITRUVIUS\_imagens\vao_19-10\vitruvius_20261019_204857 - Planta de piso - EP- Térreo.png`
- `D:\011_VITRUVIUS\_imagens\vao_19-10\vitruvius_20261019_204857 - Corte - CORTE DD - VAO CIRCULACAO ESTAR (19-10).png`

### Auditoria do Lúcio (vão)

| Item | Prova | Resultado |
|---|---|---|
| Trecho na parede | Parede começa em x 2,575: 7,675 − 2,575 = 5,10 e 11,540 − 2,575 = 8,965 (bate com `trechoNaParede_m`). Largura 8,965 − 5,10 = 3,865. | OK |
| Medidas reais | `larguraM` 3.865, `alturaM` 2.4, `baseM` 0 iguais às decididas | OK |
| Planta | Imagem aberta por mim com Read. Entre o 12 (CIRCULACAO ESCADA) e o 13 (ESTAR JANTAR), a parede está aberta em toda a largura da circulação, com toco só nos encontros. O trecho da cozinha continua cheio. A porta de correr não aparece mais. | atende a 2-bis |
| Corte DD | Imagem aberta por mim com Read. No térreo, à direita, aparece o contorno retangular do vão na parede. Ele vai do encontro com a parede interna até perto da parede leste, com altura abaixo da laje (testeira visível). Ao fundo se vê a porta de giro, em vista. | atende |
| Partida da escada | Vão em y 23,0, partida entre y 17,075 e 18,274: distância de cerca de 4,7 m. (O Oscar escreveu "5,9 m", o que está errado, mas não afeta o vão.) | não invade |
| Salvar | JSON colado, `modificadoDepois` false | OK |

**Veredito: aprovado para o pedido** (vão livre feito). Isto não aprova o EP nem passa pelo Gate da Coordenação (Claudemberg). Fica a pendência anterior 1 (família de passagem), resolvida para este vão.

**Ponto aberto para Claudemberg:** a área livre na partida da escada mede **1,199 m** (de y 17,075, face norte da 449337, a y 18,274, primeiro degrau). São 1 mm abaixo dos 1,20 m da seção 3 da Skill, e a criar_escada aceitou. Decidir entre ajustar a escada em 1 mm ou tratar como tolerância. A tolerância precisa estar escrita na Skill, senão a ferramenta e a Skill divergem.

Pendências que continuam: etiqueta do ambiente 12 sobre a escada; `folgaVao` 0 e os 9 m² das suítes.


## Escada recriada (19/10, decidido por Claudemberg) — Wallenberg

Claudemberg: "Recriar a escada para fechar 1,20 m na partida e voltar a folga do vão para 0,05."

- Apagados: escada 450364 (com os corrimãos), vão 450472, guarda-corpo 450475 (450480 já não existia).
- Causa do 1,199 m: a caixa da escada no modelo começa ~7,6 cm antes do ponto `inicio` dado à ferramenta (pedido y 18,35; caixa em y 18,274). A ferramenta media a área livre a partir do `inicio`, não da caixa real.
- Recriada (plugin v62, pelo comando CreateStair): mesma posição e formato, `inicio` {9.22, 18.40}, `direcao` norte, `virar` esquerda, U 9+9, espelho pedido 0,175 (real 0,1667), piso 0,28, largura 1,00, `vaoEntreLances` 0,10, **`folgaVao` 0,05**.
- Resposta: escada **450613**, vão **450721**, guarda-corpos do vão **450724, 450729**, corrimãos **450648, 450652**; áreas livres: partida em CIRCULACAO ESCADA (2 portas), chegada em CIRCULACAO ESCADA SUPERIOR (3 portas).
- Medida real: caixa da escada começa em y **18,324** → partida livre **1,249 m** até a face da parede 449337 (y 17,075). Atende 1,20 m.
- Imagens (abertas com Read): `D:\011_VITRUVIUS\_imagens\escada_19-10\recriada\` — plantas EP. Térreo e EP. Superior e CORTE ESCADA (450520).
- Salvo com `document salvar` (requestId wallenberg-diag-EP-escada-recriada-19-10-7).
- Melhoria pendente na ferramenta: medir a área de partida a partir da caixa real da escada, não do `inicio`.
