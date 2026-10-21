# Relatório Oscar — Exame da Fase 3 — EP v3 (base E) — 20/10/2026

Caso fictício (Ensaio Sombra 003). Esta é uma análise preliminar e não foi aprovada por mim. O Gate é de Claudemberg.

## 1. O que foi feito
- `salvar_copia` do EP_volumeE para `entrega_v3\EP_v3.rvt` às 17:39:31. O documento ativo passou a ser a cópia, e o EP_volumeE não foi alterado.
- O edifício da E foi apagado e reconstruído (36 elementos apagados, mais o shaft antigo 451009). Os muros do lote 449286–449289 e o jardim 452447 ficaram.
- **Partido mantido:**
  - Pé-direito duplo no estar, sobre a faixa x 2,50–6,55 e y 29,0–35,0 (laje do superior em L). O piso fica a +0,30 e a cobertura a +6,60, então o duplo tem 6,30 m livres.
  - Galeria do superior debruçada sobre o duplo, com guarda-corpo 454159.
  - Marquise sinuosa 454246, tipo "MARQUISE BALANCO 15 cm", a +3,45 sobre a frente.
  - **Curva legível na fachada SUL:** fiz uma platibanda em arco escalonado, com 9 trechos de 0,81 a 1,80 m acima de +6,60 (454218–454226), porque a curva desenhada só em planta some na elevação. O topo fica em +8,40 a partir da rua, ou 8,10 m acima do térreo.
- **Envelope H0:** x 2,50–11,79 e y 6,00–35,00. Os afastamentos são 6,00 m na frente, 2,50 m nas laterais e 5,00 m no fundo.
- **Níveis:** Terreno 0,00, térreo 0,30, superior 3,45, cobertura 6,60.
- **Altura das paredes conferida na releitura:**
  - externas do térreo: 3,30 (base −0,15, macete);
  - internas do térreo: 3,15;
  - superior: 3,15.
- **Programa:**
  - 4 suítes: SUITE LOURDES (térreo), SUITE 1, SUITE 2 e SUITE 3 (superior), cada uma com banho; as suítes 1, 2 e 3 têm também closet.
  - Outros ambientes: home office, home cinema, estar e jantar integrados (87,67 m²), cozinha gourmet (36,80), serviço, dependência com banho, lavabo, hall, garagem para 2 vagas cobertas, piscina, deck e jardim.
- **Escada 453969:** em U, 20 espelhos de 0,1575 m (10 + 10), piso de 0,28 m, largura 1,00 m.
  - A ferramenta conferiu a partida em x 5,35–6,35 e y 11,60–12,80, e a chegada em x 4,25–5,25 e y 11,60–12,80, as duas na CIRCULACAO.
  - Vão na laje 454092, guarda-corpos 454095, 454100 e 454105, corrimãos 454008 e 454012.
- **Cortes:**
  - AA 454370, longitudinal, em x 5,60, passa pela escada e pelo duplo;
  - BB 454379, transversal, em y 31,5, passa pelo duplo.
- **Elevações (create_elevation, alvo modelo):**
  - SUL 454398, marcador 454387 em y −1,59;
  - NORTE 454435, marcador 454406 em y 41,59.
  - Os dois marcadores ficam fora do lote (o lote vai de y −0,045 a 40,045).
  - Apagadas as antigas 449704, 449741, 449760 e 449797, e os cortes 449431, 449457, 450303, 450520 e 450605.
- **Vagas (Skill de vaga):** 2 cobertas de 2,50 × 5,00 m (vão de 4,60 m na fachada) e 2 descobertas paralelas de 2,50 × 6,00 m na faixa lateral leste, x 11,79–14,29 e y 6–18.
- Eixos A, B, C e 1 a 4: 454362–454368.
- Etiquetas de ambiente nas duas plantas, norte nas 3 plantas e cotas totais de 9,29 e 29,00 m (454577–454580).
- Cota vertical no corte AA (454581): 0,15 / 3,00 / 0,15 / 3,15 / 0,40.
- Salvo pela ferramenta `document salvar` às 17:50:33, com modificadoDepois false.

## 2. Prova por item
- **Gate de entrada:** connected true, build 2026-10-20-quadro-areas-v68, EP_volumeE, isModified false.
- **Duplicados:** o status final traz walls 46 = 4 muros + 4 + 12 + 17 + 9 criadas, doors 22, windows 24, rooms 24 e floors 10. Cada número bate com a contagem das criações. `find_elements` Stairs devolve 1 escada (453969).
- **conferir_layout, rodada final:** 0 graves e 11 avisos. Os 2 graves da 1ª rodada eram de nome ("BANHO SUITE 1" lido como suíte); renomeei os banhos e closets para BANHO/CLOSET n. Motivo de cada aviso:
  - "sem ventilação cruzada" (9 ambientes): a casa tem só 9,29 m de largura e as janelas ficam em uma só fachada. É pendência de partido.
  - "corredor longo 23,3 m": é a galeria sobre o duplo, uma decisão do partido E.
  - "BANHO 1 e BANHO 2 sem área molhada embaixo": a prumada não está empilhada. É pendência para o hidráulico.
- **Quadro de áreas (saída colada):**
  - lote do modelo 571,60 contra 571,80 informado, diferença −0,20 m² (0,035%);
  - soma do lote 100% (≤ 1%);
  - TO 49,41%, atende;
  - CA 0,909, atende;
  - permeabilidade 28,33%, atende;
  - na outra base (571,80): 49,39%, 0,909 e 28,32%.
  - Áreas: PROJECAO 282,42; construída do térreo 269,41; construída do superior 250,15; JARDIM SOLO NATURAL 161,95; IMPERMEAVEL 409,65.
- **Os fatores não casaram por nome.** O aviso colado da ferramenta diz: "Fatores padrão (1 = conta inteira; grama 1; concregrama 0 (Rio não fixa fator); impermeável 0) até o Hely aplicar os fatores da Skill quadro de áreas RJ." A ferramenta criou áreas genéricas (PROJECAO / AREA CONSTRUIDA) e não aplicou fator 0 aos ambientes GARAGEM COBERTA VAGA 1 e 2 nem à marquise. Pela imagem, a PROJECAO e o CA do superior incluem a marquise sinuosa. Não calculei número corrigido; isso fica para o Hely e o Kelsen.
- **Vão da escada fora da área do superior:** a imagem da planta de CA do superior mostra o furo no contorno.

## 3. Imagens abertas com Read nesta execução (pasta `entrega_v3\imagens\`)
| Arquivo | O que se vê |
|---|---|
| `vitruvius_20261020_174943 - Planta de piso - EP- Terreno.png` | Implantação: lote 14,29 × 40,09, jardins, piscina e deck no fundo, faixa frontal e vagas leste em piso de acesso, marquise sinuosa. Atende. |
| `... - Planta de piso - EP- Térreo.png` | 12 ambientes etiquetados, escada "Acima", vão para o estar, garagem 2 vagas, cotas 9,29/29,00. Os rótulos das 2 vagas se sobrepõem. |
| `... - Planta de piso - EP- Superior.png` | 3 suítes, office, cinema, galeria, vão da escada, marquise curva à frente. |
| `... - Corte - CORTE AA - LONGITUDINAL (ESCADA).png` | Escada em U cortada, duplo com guarda-corpo, níveis 0,30/3,45/6,60, cota vertical. Atende. |
| `... - Corte - CORTE BB - TRANSVERSAL (PE-DIREITO DUPLO).png` | Laje do superior interrompida sobre o duplo, platibanda em arco ao fundo. Atende. |
| `... - Elevação - ELEVACAO FRONTAL SUL (RUA).png` | Platibanda em arco escalonado legível, porta de entrada, vão da garagem, janelas do superior. O muro tapa a base. Atende. |
| `... - Elevação - ELEVACAO FUNDOS NORTE.png` | Portas de correr do estar e da cozinha, janelas do superior, arco ao fundo. Atende. |
| `... - Vista 3D - EP- Perspectiva.png` | Volume com marquise curva e platibanda. Não tenho ferramenta para criar ou ajustar vista 3D; usei a vista do template. |
| `vitruvius_20261020_175018 - ... TAXA DE OCUPACAO.png` | Contorno da PROJECAO de 282 m² incluindo a marquise. |
| `... - COEFICIENTE ... - P.png` | Superior com 250 m², vão da escada fora, marquise dentro. |
| `... - PERMEABILIDADE.png` | Jardim 162 m², impermeável 410 m². |

Ver no Revit: planta de CA do térreo 454468 (não exportada).

## 4. Bloco da seção 11
```
## Entrega — Ensaio 003 — Etapa 05 EP v3 (Exame Fase 3)
Build: 2026-10-20-quadro-areas-v68 (status)
Gate de entrada (0.1): connected true, EP_volumeE, isModified false
Passos: [0.4 ✓ salvar_copia EP_v3] [1 ✓ níveis 0/0,30/3,45/6,60] [3 ✓ paredes 3,30/3,15/3,15, escada 453969, vão 454092, portas por pavimento, eixos] [4 ✓ cortes 454370/454379, elevações 454398/454435] [layout ✓ 0 grave] [quadro ✗ fatores por nome não aplicados]
Imagens conferidas (§6): tabela §3
Defeitos encontrados (§8): criar_quadro_areas não aplica fatores por nome; dimension nivel com níveis → "Encontrei 0 face(s) (mínimo 2)" (contornado com pisos); create_room põe o número no nome exibido
Lacunas declaradas (§3): cobertura inclinada; laje/marquise em arco feitas como polígono; curva da fachada em degraus; sem ferramenta para criar ou ajustar vista 3D; norte sem "N" legível; folhas não montadas
Pendências: Kelsen (marquise e piscina nos afastamentos, vagas descobertas no lateral, manobra no frontal, TO 40×50, regime da garagem/marquise); P-l (área por ambiente, cliente); "a" não fixado; cota da rua (P-k); hidráulica empilhada; pé-direito de 7 m pedido × 6,30 do duplo
Status: PARCIAL
```

## 5. Números (rótulo do regime: o da ferramenta, sem os fatores)
- Construída: 269,41 + 250,15 = 519,56 m². Esse total inclui a marquise de 13,01 e as garagens cobertas (13,06 + 13,40 de ambiente).
- 4 suítes.
- TO 49,41%, CA 0,909, permeabilidade 28,33% (base 571,60).
- Com a TO de 40% do Regramento (P2), a projeção não cabe (282,42 > 228,64). Isso é condição do cenário H0, para o Kelsen e o cliente.

## 6. O que Claudemberg deve conferir no Revit
1. A platibanda em degraus atende como "curva legível"? Família de perfil curvo = Tenreiro.
2. A marquise no afastamento frontal.
3. Os rótulos sobrepostos das vagas.
4. O norte.
5. As 4 plantas de área com os fatores pendentes.

---

## Correção 20/10 após reprovação (nota 7,60, parecer_bardi_v3)

O texto acima é o original e foi mantido. Esta seção registra o que mudou. Modelo: o mesmo `EP_v3.rvt`, sem salvar_copia. Salvo pela ferramenta às 20:56:11 (`tinhaAlteracoes true`, `modificadoDepois false`).

### C0. Gate e documento (saída colada)
- `get_document_info`: `"name": "EP_v3", "path": "...\\entrega_v3\\EP_v3.rvt", statistics levels 4, walls 46, doors 22, windows 24, rooms 24`
- `get_revit_status` (início): `connected true, buildVersion "2026-10-20-quadro-areas-v69", isModified false, floors 10`
- `get_revit_status` (fim, antes de salvar): `walls 44, doors 20, windows 24, rooms 22, floors 13, isModified true`
- Diferença: −2 paredes (453901, 453906), −2 portas (453960, 453963), −2 ambientes (closets 453933 e 453936), +3 pisos (pisos: −453858 −453866 −454320, +454775 +454783 +454815 +454823 +454843 +454851). Uma escrita por vez, com releitura.

### C1. Níveis (`get_levels`, colado)
`324604 Terreno 0 | 311 Páv. térreo 0.3 | 694 Páv. Superior 3.45 | 323714 Cobertura 6.6`
- "Terreno 0,00" fica. Fonte: Skill `oscar-revit-projetista-vitruvius` v1.3.0, §1 item 2, L44: "**Terreno = rua = 0,00.**" (R1 de Claudemberg). É a referência +0,00 dos cortes (§9, L172) e o nível onde estão lote, muros e jardins (pisos 452447, 454312 etc. com `levelId 324604`). Não é nível duplicado.

### C2. Alturas de paredes (`list_elements` parameters, colado)
| id | Comentários | Restrição base | Desl. base | Restrição sup. | Altura |
|---|---|---|---|---|---|
| 453874 | EXT T SUL | 311 | -0.15 | 694 | 3.3 |
| 453875 | EXT T LESTE | 311 | -0.15 | 694 | 3.3 |
| 453876 | EXT T NORTE | 311 | -0.15 | 694 | 3.3 |
| 453877 | EXT T OESTE | 311 | -0.15 | 694 | 3.3 |
| 453879 | INT T FRENTE CIRC | 311 | 0 | 694 | 3.15 |
| 453885 | INT T CIRC SOCIAL | 311 | 0 | 694 | 3.15 |
| 453886 | INT T ESTAR SERVICO | 311 | 0 | 694 | 3.15 |
| 453890 | EXT S SUL | 694 | 0 | 323714 | 3.15 |
| 453903 | INT S SUITE2 GALERIA | 694 | 0 | 323714 | 3.15 (get_element) |
Muros 449286–449289: base 324604, altura desconectada 1, sem restrição superior.

### C3. Térreo dentro dos 40% do Regramento — o que mudou
Fundos recuados 3,925 m (fachada norte de y 34,925 para y 31,0):
- `move_element` 453876 (térreo) e 453892 (superior) dy −3,925. As paredes unidas acompanharam. Releitura: 453875/453877/453891/453893 com length 24.925, 453886 com 13.5, 453897 com 19.5, rear em y 31.
- Apagados: parede 453901 (com a porta 453960), parede 453906, porta 453963, ambientes CLOSET 3 453933 e CLOSET 2 453936 (com a etiqueta 454573; com a 453906 saiu também o 454771, que não identifiquei), guarda-corpo 454159, lajes 453858/453866, cobertura 454203 (com ela saiu a cota 454581 do corte AA, que refiz como 454891), corte BB 454379.
- Resize de 453903 para 9,00 (fim em y 26,5).
- Janela 454199 movida dy −3 (y 29, parede oeste do duplo).
- Criados: laje do térreo 454775 (232,95), laje do superior 454783 em L (206,45 com o vão), cobertura 454876 (232,95), guarda-corpo do duplo 454797 (x 6,60, y 26,575–30,925, 4,35 m), deck 454815 (11,15) e JARDIM SOLO NATURAL 454823 (25,32) na faixa liberada, corte BB novo 454858 (y 28,8).
- **Partido mantido:** o pé-direito duplo segue no estar, em x 2,50–6,55 e y 26,5–31,0 (4,05 × 4,50 = 18,2 m², antes 24,3). A galeria fica debruçada sobre ele, e a marquise sinuosa 454246 e a platibanda em degraus não foram tocadas. A escada 453969 e o vão 454092 também não foram tocados.
- **4 suítes mantidas** (LOURDES, 1, 2, 3, todas com banho). Saíram os closets das suítes 2 e 3.
- **Programa ~520 m² NÃO mantido.** A área bruta passou de 519,56 para 452,41 (232,95 + 206,45 + 13,01). Conta que mostra o impossível: com 2 pavimentos, a projeção computável ≤ 228,64 e a vaga 1 ×0 (13,83), a laje do térreo fica em no máximo ~242. O superior fica com no máximo ~242 − duplo − vão, então o total sai em ~470 mesmo sem duplo. 520 m² não cabem nos 40% sem um 3º pavimento ou sem acabar com o duplo. É a mesma conclusão da Etapa 05 v1 (E-27). Fica para Lúcio, Kelsen e o cliente decidir; não escolhi.
- Ainda há perdas: estar 87,67 → 67,75; cozinha 36,80 → 22,03.

### C4. Quadro de áreas (`criar_quadro_areas`, saída colada)
Parâmetros: areaLote 571.8, baseIndices "menor", limites {toMax 40, caMax 1.0, tpMin 25}, fatores do `quadro.json` (TO/CA/PERM, com campo `esquema`), manual CONCREGRAMA.
```
areaLoteInformadaM2 571.8 | areaLoteDoModeloM2 571.6 | diferencaLoteM2 -0.2
baseDosIndices {modo menor, m2 571.6}
naOutraBase {571.8: TO 38.32, CA 0.719, perm 32.75}
somaAreasDoLote {m2 547.1, percentual 95.71, confere "NÃO soma 100%: conferir contorno do lote e regiões"}
taxaOcupacao 38.33 atende | coeficienteAproveitamento 0.72 atende | permeabilidade 32.76 atende
TO  térreo GARAGEM COBERTA VAGA 1   13.83 ×0 = 0      (454915)
TO  térreo MARQUISE BALANCO 15 CM   13.01 ×0 = 0      (454929)
TO  térreo PROJECAO                219.11 ×1 = 219.11 (454947)
CA  térreo GARAGEM COBERTA VAGA 1   13.83 ×0 = 0      (454965)
CA  térreo GARAGEM COBERTA VAGA 2   14.19 ×0 = 0      (454972)
CA  térreo AREA CONSTRUIDA         204.93 ×1 = 204.93 (454979)
CA  sup.   MARQUISE BALANCO 15 CM   13.01 ×0 = 0      (455004)
CA  sup.   AREA CONSTRUIDA         206.45 ×1 = 206.45 (455024)
PERM JARDIM SOLO NATURAL 187.27 ×1 | CONCREGRAMA 85.74 ×0 | IMPERMEAVEL 274.09 ×0
aviso: "Fatores padrão (1 = conta inteira; ...) até o Hely aplicar os fatores da Skill quadro de áreas RJ."
```
- **Os fatores casaram por nome** (vaga 1 ×0 na TO, marquise ×0, garagens ×0 no CA). O aviso de "fatores padrão" continua na resposta, mas as linhas mostram os fatores aplicados.
- **TO pelo RIU (50%):** 219,11 / 571,60 = 38,33%, atende (teto 285,80).
- **TO pelo Regramento (40%, P2):** 219,11 ≤ 228,64, atende, com folga de 9,53 m². Antes era 255,58, então a projeção baixou 36,47 m².
- **CA:** (204,93 + 206,45) / 571,60 = 0,720.
- **Permeabilidade:** 187,27 / 571,60 = 32,76% (mínimo 25%).
- **Vão da escada descontado do superior:** a laje em L pelos vértices dá 9,29 × 25,075 − 4,05 × 4,575 = 214,42; a ferramenta devolve 206,45. O vão 454092 descontado é de 7,97 m² (imagem do CA do superior: contorno roxo em volta do vão).
- **Defeito:** a soma do lote dá 95,71%. Faltam 24,50 m² = piscina 17,50 + deck 7,00, que ficam no furo do jardim 454336 e não entram em região nenhuma. O índice de permeabilidade não muda, mas a conferência dos 100% falha. Vai para o Vitruvius, sem código na §8 (linha nova).

### C5. Implantação e vagas
- Afastamentos cotados no EP. Terreno: cadeia X 454892 = `0.09, 2.5, 0.15, 8.99, 0.15, 2.5, 0.09` (total 14,47); cadeia Y 454893 = `0.09, 6, 0.15, 24.775, 0.15, 8.925, 0.09` (total 40,18). Frente 6,00, laterais 2,50, fundos 8,925.
- **Vagas descobertas desenhadas:** o piso 454320 foi dividido em 454843 e 454851 (CALCADA ..., 2,50 × 6,00 cada, Comentários "VAGA DESCOBERTA 1/2 (2,50 x 6,00 paralela)"), com os textos 454897/454898 e a cota 454894 `6, 6`. São paralelas, então 6,00 pela Skill de vaga, não 5,00. Ficam no afastamento lateral: decide Kelsen.
- **Vagas cobertas cotadas no EP. Térreo:** 454895 = 5.015 (largura para 2 vagas de 2,50) e 454896 = 5.425. A ferramenta mediu de eixo a eixo, então o vão interno é ~5,275 (≥ 5,00).
- Rótulos 454552 (+1,30) e 454553 (−1,30) movidos: na imagem do térreo, VAGA 1 e VAGA 2 já não se sobrepõem.

### C6. conferir_layout (resumo colado)
`"resumo": {"ambientes": 22, "graves": 0, "avisos": 11}`. Os avisos são 8 "sem ventilação cruzada" (SUITE LOURDES, COZINHA GOURMET, ESTAR JANTAR, SUITE 1, HOME OFFICE, HOME CINEMA, SUITE 3, SUITE 2), "corredor longo 19,4 m" na CIRCULACAO do superior, e BANHO 1 e BANHO 2 com "prumada não empilhada". Motivos como em §2.

### C7. Imagens abertas com Read nesta execução (`entrega_v3\imagens\correcao_20-10\`)
| Arquivo | O que vi |
|---|---|
| `vitruvius_20261020_205520 - Planta de piso - EP- Terreno.png` | Lote com cadeia 0,09/2,50/0,15/8,99/0,15/2,50/0,09 e 6,00/24,78/8,93. Fundos com deck novo e jardim, as duas VAGAS DESCOBERTAS no leste e "NORTE DE PROJETO – NORTE VERDADEIRO PENDENTE". Defeito: a cota 6,00 das vagas fica sob os textos, e o eixo 4 continua em y 35 (eixos não foram movidos). |
| `... - Planta de piso - EP- Térreo.png` | 12 ambientes, estar 68 m², cozinha 22 m², escada "Acima" na circulação, rótulos das vagas separados, cotas 9,29 / 25,08 / 5,02 / 5,43. |
| `... - Planta de piso - EP- Superior.png` | Suítes 1 a 3, banhos, office, cinema, escada "Abaixo" com vão. O duplo aparece vazio a noroeste, ao lado da galeria. |
| `... - Corte - CORTE AA - LONGITUDINAL (ESCADA).png` | O corte morde a laje de +3,45, que aparece interrompida no vão, e o 1º lance parte do piso +0,30 da circulação, com guarda-corpo no superior. Cota 0,15/3,00/0,15/3,15/0,40, níveis 0,30/3,45/6,60. Rótulos Terreno e térreo sobrepostos (D5). |
| `... - Corte - CORTE BB - TRANSVERSAL (PE-DIREITO DUPLO).png` | Laje do superior só até o eixo B mais a galeria; à direita, o duplo do térreo à cobertura. Platibanda em degraus ao fundo. |
| `... - Elevação - ELEVACAO FRONTAL SUL (RUA).png` | Fachada real: platibanda em arco escalonado, porta, vão da garagem, janelas do superior. O muro tapa a base. |
| `... - Elevação - ELEVACAO FUNDOS NORTE.png` | Fachada real com as 2 portas de correr do térreo e as janelas do superior. |
| `... - Vista 3D - EP- Perspectiva.png` | Volume mais curto, marquise curva, platibanda, piscina e deck no fundo. Não há ferramenta para criar ou ajustar vista 3D: esta é a vista do template. |
| `... - Planta de área (TAXA DE OCUPACAO) ....png` | PROJECAO 219 m², GARAGEM COBERTA VAGA 1 com 14 m² e MARQUISE com 13 m², em contornos separados. |
| `... - Planta de área (COEFICIENTE DE APROVEITAMENTO) - PLANTA DE COEFICIENTE DE APR.png` | CA do térreo: 205 m², garagens 1 e 2 separadas. Os rótulos das 2 garagens se sobrepõem (texto da ferramenta). |
| `ca_superior\vitruvius_20261020_205559 - ... PLANTA DE COEFIC.png` | CA do superior: 206 m², com o duplo e o vão da escada fora do contorno e a marquise à parte. |
| `... - Planta de área (PERMEABILIDADE) ....png` | Jardim 187, concregrama 86, impermeável 274. A piscina e o deck ficam num contorno sem rótulo (os 24,50 que faltam). |

Defeito de exportação: os dois CA saíram com o mesmo nome cortado e um sobrescreveu o outro. Reexportei o do superior em `ca_superior\`.

### C8. Defeitos de ferramenta (com erro colado)
- `resize_element` 453875 → 24,925: a resposta foi `"Elemento 453875 redimensionado com sucesso"`, mas a releitura mostrou `"length": 28.85`. É sucesso falso numa parede unida nas pontas, do mesmo tipo que D2/D3/D19. Contornei movendo a parede de fundo; as unidas acompanharam.
- `dimension mode=ambiente` 453914: `Error: ambiente 453914: faces internas no eixo X não encontradas.` As vagas são separadas por linha de ambiente, não por parede. Contornei com `cadeia`.
- `dimension cadeia face_interna` 453874/453879 devolveu 5,425, que é a medida de eixo a eixo, não de face interna.
- `criar_quadro_areas`: "NÃO soma 100%" (C4). Exportação com nomes que colidem (C7).

### C9. O que não fiz
- Eixos 1 a 4 não ajustados: o eixo 4 continua em y 35, fora da casa. Não há ferramenta para mover o eixo sem apagar e recriar.
- Cota das vagas descobertas sob o texto: não reposicionei.
- O programa de 520 m² não cabe nos 40% (C3). Decide Lúcio.
- Folhas não montadas.

Status: PARCIAL.
