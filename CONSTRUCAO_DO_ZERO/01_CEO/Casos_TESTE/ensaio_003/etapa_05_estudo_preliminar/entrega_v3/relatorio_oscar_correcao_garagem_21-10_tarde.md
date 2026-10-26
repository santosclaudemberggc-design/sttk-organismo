# Correção da garagem do EP_v3 (21/10/2026, tarde) — Oscar para Lúcio

## Entrega — Ensaio 003 — Etapa 5 (3ª tentativa), correção garagem/vão/portão
Build: 2026-10-20-quadro-areas-v69
Gate de entrada (0.1): connected true, documentTitle "EP_v3", documentPath ...\entrega_v3\EP_v3.rvt, isModified false (uptime 00:09:18).
Status: PARCIAL (ver pendências; a projeção bruta do térreo passa de 228,64)

## (a) Vagas cobertas
Escritas: `move_element 453878 dx -0,20` (parede divisória hall/garagem); `move_element 453908 dx -0,0675` (linha de separação entre as vagas).
Releitura (`list_elements Paredes levelId 311 fields location`):
- 453878: start (6.35, 6.075) end (6.35, 11.5), e 0,15. Antes: x 6.55.
- 453875: start (11.715, 6.075) end (11.715, 31), e 0,15. Não tocada.
- 453882 (x 6.55, y 11.5–15) continua em 6.55. A parede unida não foi arrastada.
- 453908: start (9.033, 6.075) end (9.033, 11.5).

Conta pelas linhas das paredes:
- Face leste da 453878: 6,35 + 0,075 = 6,425. Face oeste da 453875: 11,715 − 0,075 = 11,640. Total interno: 5,215.
- Vaga 1: 9,0325 − 6,425 = **2,6075** (folga 0,1075).
- Vaga 2: 11,640 − 9,0325 = **2,6075** (folga 0,1075).
- Profundidade: (11,5 − 0,075) − (6,075 + 0,075) = 5,275 ≥ 5,00.
- Ambientes relidos: 453914 bbox x 6.425–9.033, área 13,75; 453915 bbox x 9.033–11.64, área 13,75.
- Efeito colateral: HALL ENTRADA 453911 perde 0,20 m de largura (x 2,65–6,275 = 3,625). A porta 453938, hospedada na 453878, foi junto com a parede.

## (b) Vão da garagem na 453874
`criar_abertura_parede` id **455286** (vão livre, sem família; não procurei porta de garagem no template). Centro (9,0325; 6,075), largura 5,00, altura 2,40, base 0. Trecho na parede de 3,958 a 8,958 (parede de 9,14 a partir de x 2,575), ou seja x 6,533–11,533 dentro do interno 6,425–11,640. A porta 453937 (bbox x 3,88–5,12) não conflita e foi mantida.

## (c) Portões no muro 449286 (y −0,045)
- **455287**: x 6,533–11,533, largura **5,00**, altura 2,20, alinhado ao vão 455286 (vagas cobertas).
- **455288**: x 11,640–14,190, largura **2,55**, altura 2,20, para a faixa leste das vagas descobertas (x 11,79–14,29). Não deu para alinhar exatamente a 14,29: a ferramenta recusa vão a menos de 0,10 do encontro com o muro 449287. Ficou um pilar de 0,107 entre os dois portões.
- Ferramenta: `criar_abertura_parede`, vão livre. A família de portão é com o Tenreiro.
- Observação: a área do muro (14,47 m² para 14,38 m) indica cerca de 1,0 m de altura. O vão de 2,20 foi aceito. Conferir pela elevação.

## Projeção e afastamentos
As paredes externas não mudaram (453874/453875/453876/453877 relidas com os mesmos eixos de antes). Contorno externo: x 2,50–11,79; y 6,00–31,075. Lote: x 0–14,29; y 0–40,00.
- Frontal 6,00; lateral oeste 2,50; leste 2,50; fundos 40,00 − 31,075 = 8,925. Na imagem da implantação aparecem 6,00 / 2,50 / 2,50 / 8,93.
- **Projeção bruta do térreo = 245,95 m²** (1ª rodada do quadro, sem fatores, id 455316), acima de 228,64. É igual à da v3 de antes: 219,11 + 13,83 + 13,01 = 245,95. Esta correção não muda a projeção, porque a parede movida é interna.
- Com os fatores da v3, a projeção computada é 218,39 ≤ 228,64. Esses fatores são: GARAGEM COBERTA VAGA 1 ×0 na TO e MARQUISE ×0. A exclusão de vaga e marquise da TO é interpretação; quem decide é Kelsen, não eu.

## Quadro (criar_quadro_areas, 2ª rodada, vale esta)
Parâmetros: areaLote 571.6, baseIndices "informada", limites {toMax 40, caMax 1.0, tpMin 25}, permeaveis "JARDIM|GRAMA", fatorConcregrama 0, fatores [GARAGEM COBERTA VAGA 1 ×0 TO; MARQUISE ×0; GARAGEM COBERTA ×0 CA].
```
TO 38.21 atende | CA 0.718 atende | perm 32.76 atende | soma lote 547.1 = 95.71% "NÃO soma 100%"
TO  GARAGEM COBERTA VAGA 1 14.55 x0 (455417); MARQUISE 13.01 x0 (455431); PROJECAO 218.39 x1 (455449)
CA  VAGA 1 14.55 x0 (455468); VAGA 2 14.55 x0 (455475); TERREO 203.84 (455482); MARQUISE sup 13.01 x0 (455507); SUPERIOR 206.45 (455527)
PERM JARDIM 187.27 x1 (455553); IMPERMEAVEL 359.83 x0 (455560)
```
1ª rodada, sem fatores (errei ao omiti-los, depois refiz): TO 43,03% "NÃO atende" (projeção 245,95), CA 0,791. As plantas foram refeitas pela 2ª rodada.
A soma de 95,71% é o defeito antigo: piscina 17,50 + deck 7,00 ficam fora das regiões.

## Imagens (abertas com Read nesta execução)
- `entrega_v3\imagens\correcao_21-10_tarde\terreo\vitruvius_20261021_142639 - Planta de piso - EP- Térreo.png`: fachada da garagem aberta, sem parede entre os eixos 1/2 do lado das vagas. A linha de separação divide as duas vagas, com cotas temporárias 2,6075 | 2,6075. A cota antiga mostra 5,22 (interno 5,215). O hall ficou mais estreito. A porta de entrada 453937 continua no lugar.
- `entrega_v3\imagens\correcao_21-10_tarde\implantacao\vitruvius_20261021_142644 - Planta de piso - EP- Terreno.png`: afastamentos 6,00 / 2,50 / 2,50 / 8,93. Vagas descobertas 1 e 2 na faixa leste, entre os eixos 1 e 3. Na escala da imagem, os portões no muro frontal aparecem só como pequenas interrupções na linha do muro, sem leitura clara. Não verificado visualmente com segurança: precisa de elevação SUL ou de zoom.

## Salvamento
`document salvar` (requestId oscar-21-10-tarde-garagem-salvar): dataHora 2026-10-21T14:26:56, tinhaAlteracoes true, modificadoDepois false. `get_revit_status` em seguida: isModified false.
requestId: `move_element` e `criar_abertura_parede` não têm esse campo no schema, então só o salvamento levou requestId.

## Pendências
- Kelsen: manobra das vagas descobertas no afastamento frontal (o acesso pelo portão 455288 atravessa o frontal até a vaga 1).
- Kelsen: confirmar se vaga coberta e marquise saem da TO. Sem isso, a projeção é 245,95 > 228,64 e não atende.
- Não conferido em imagem legível: os portões (falta elevação SUL).
- RDMOB-PBA-04 não foi tocado. `_estado_ensaio_003.json` não foi alterado.
