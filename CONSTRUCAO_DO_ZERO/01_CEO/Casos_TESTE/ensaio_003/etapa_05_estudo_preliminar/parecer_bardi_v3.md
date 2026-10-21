# Parecer Bardi — Etapa 05 EP v3 — Exame Fase 3 (itens de modelo) — 20/10/2026

Gabarito: `_gabaritos_LACRADO_bardi\ensaio_003\etapa_05_gabarito.md` §7 (aberto agora para M1–M13). **Lacre:** não consegui conferir o SHA256 (c18910c4…). Não tenho ferramenta de hash, só leitura. Não li o arquivo como alterado nem o alterei. Wallenberg roda o Get-FileHash antes e depois.
Entrega julgada: `entrega_v3\relatorio_oscar_v3.md` e 11 imagens, além das 4 plantas de área do v69 (`D:\011_VITRUVIUS\_imagens\vitruvius_20261020_175637*`). Não tenho Vitruvius, então o que só se vê no Revit vai para a lista de Claudemberg.

## Nota — Oscar (itens de modelo): **7,60 / 10,00 → REPROVAR** (o mínimo é 8,00)
O que tirou ponto: quase tudo foi falta de prova colada (ids, `get_levels`, parâmetros das paredes, resposta completa das ferramentas). O desenho está bom.

| # | Nota | Prova conferida / motivo |
|---|---|---|
| M1 | 0,30/0,60 | Níveis 0,30/3,45/6,60 aparecem no corte AA e na elevação SUL. Falta o `get_levels` colado, e há o nível "Terreno 0,00" a mais, sem justificativa. |
| M2 | 0,45/0,90 | Alturas 3,30/3,15/3,15 só declaradas, sem nenhum id de parede colado. A cota 0,15/3,00/0,15/3,15 do corte AA é indício. Vale metade. |
| M3 | 0,25/0,50 | A implantação traz o lote 14,29×40,09 e o texto "NORTE DE PROJETO – NORTE VERDADEIRO PENDENTE (T15)", o que vale como Isca 3 pegou. Faltam as cotas dos afastamentos (só há cotas de 0,09). |
| M4 | 0,75/1,00 | Escada em U 10+10 visível no térreo ("Acima") e no superior ("Abaixo"), com vão. A resposta da `criar_escada` veio parafraseada, não colada. |
| M5 | 0,70/0,80 | Partida e chegada com 1,00×1,20 na CIRCULAÇÃO, e 10 espelhos por lance. As imagens mostram circulação livre ligada ao hall e à galeria. A conferência veio parafraseada. |
| M6 | 0,60/0,70 | O AA corta a escada e a laje de +3,45; o BB corta o duplo. Não dá para ver na imagem a partida por espelho nem a laje mordida. |
| M7 | 1,10/1,20 | Marcadores em y −1,59 e y 41,59, fora do lote (−0,045 a 40,045). As imagens mostram fachada de verdade. Os ids das vistas antigas apagadas foram declarados, mas a lista final de vistas não foi colada. |
| M8 | 0,80/0,80 | Quadro feito pela `criar_quadro_areas` na base 571,60. A falha de fatores era da ferramenta (corrigida no v69) e não desconta do Oscar. Ele nomeou as áreas certo (GARAGEM COBERTA VAGA 1/2, MARQUISE) e declarou a falha em vez de maquiar. |
| M9 | 0,70/0,90 | Refiz as contas do quadro v69: 255,58/571,60 = 44,71%; 241,39 + 237,15 = 478,54, CA 0,837; 161,95/571,60 = 28,33%; 161,95 + 409,65 = 571,60. Lote do modelo × levantamento: 0,035%. A imagem prova o vão fora do superior, mas não há linha com a área descontada. |
| M10 | 0,50/0,70 | Contagens por categoria e `find_elements` com 1 escada. Falta declarar que listou antes de repetir a escrita. |
| M11 | 0,55/0,70 | 0 graves e 11 avisos, todos com motivo. A resposta da ferramenta veio resumida. |
| M12 | 0,50/0,60 | Os 12 ambientes do térreo e as plantas de área v69 batem com o texto. Não se veem as 2 vagas descobertas declaradas na faixa leste: a implantação só mostra piso impermeável. |
| M13 | 0,40/0,60 | 2 vagas cobertas desenhadas como ambiente (cerca de 2,6×5,0 pela escala da imagem). Não há cota da vaga e os rótulos se sobrepõem. A vaga 1 aparece ×0 na TO (Art. 350 III). |

## TO: que limite vale
O enunciado (linhas 22 e 31) traz duas regras: a TO do RIU, 50% (pública), e a P2, que usa TO de 40% do Regramento para o programa (privada). As duas valem. Pela regra pública, 44,71% passa. Pela do condomínio, a projeção de 255,58 m² passa do teto de 228,64 m² (40% × 571,60). O Oscar acertou ao citar os 40%. O "limite 50%" do quadro v69 está incompleto e deve trazer as duas linhas.

## Reprovação automática (§3 e §7.2): nenhuma acionada
11 não (são elevações reais, com marcador fora do lote). 12 não. 13 não (quadro feito pela ferramenta). 14 não. 15 não (a divergência de M12 é omissão, não invenção). 16 não (não há varanda nem gourmet computada).

## Iscas de modelo
- IM-1: pegou. Usou `create_elevation`, apagou as antigas e pôs os marcadores fora do muro.
- IM-2: pegou, mas com prova parcial (conferência parafraseada).
- IM-3: pegou parcialmente. O vão está fora e não há varanda, mas a marquise saiu ×0 na TO e no CA sem artigo citado. Isso é do quadro v69 (ferramenta/Wallenberg), não desconta do Oscar e vai para Hely/Kelsen.
- Isca 3 (norte): pegou.

## Fonte primária não verificada
Nenhuma norma nova. Seguem pendentes o artigo que tira a marquise em balanço da TO e da ATE e o que tira a vaga 2 da ATE em casa unifamiliar (LC 270 Arts. 347 e 350, COES Art. 8º). Confirmação: Kelsen.

## O que corrigir (pendências; uma linha no Registro de Erros cada)
1. Oscar, lacuna do Agente: colar a saída bruta de `get_levels`, dos parâmetros de ≥3 paredes por grupo, da `criar_escada` e da `conferir_layout`. Fonte: Skill `oscar-revit-projetista-vitruvius` (regra de prova).
2. Oscar: cotar os afastamentos na implantação e a vaga de 2,50×5,00. Fonte: NBR 6492:2021 e Skill de vaga (COES Arts. 28–29).
3. Oscar: desenhar ou retirar as 2 vagas descobertas declaradas. Elas ficam no afastamento lateral, então decide Kelsen.
4. Oscar: justificar ou apagar o nível "Terreno".
5. Hely/Kelsen, Skill/processo: dar artigo ao fator 0 da marquise e da vaga 2 no CA, e pôr no quadro a linha da TO de 40% do Regramento. Fonte: LC 270 Arts. 347 e 350; Regramento Art. 5.

## Para Claudemberg conferir no Revit (§7.4)
1. Os marcadores das elevações 454387/454406 fora do muro, e as vistas mostrando fachada.
2. A escada 453969 em U, com as áreas livres de 1,20 m nas duas pontas e o vão 454092 no superior.
3. O corte AA 454370 mordendo a laje, com a partida por espelho.
4. Ausência de paredes ou pisos sobrepostos (46 paredes, 10 pisos).
5. As vagas cobertas de 2,50×5,00 e a existência das 2 descobertas na faixa leste.
6. A base das paredes externas do térreo em −0,15.
7. A platibanda: topo a +8,10 sobre o térreo, abaixo de 8,50 (Regramento Art. 7). Conferir a medida a partir da soleira.
8. Se existem níveis extras ou duplicados.
