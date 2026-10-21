# Parecer Bardi — Etapa 05 EP v3 — Recorreção da Fase 3 (itens de modelo) — 20/10/2026

Gabarito usado: o mesmo, `etapa_05_gabarito.md` §7, sem alteração. A conferência do SHA256 fica com Wallenberg.
Julguei o artefato: `relatorio_oscar_v3.md` §C0–§C9, mais as imagens de `correcao_20-10\`. Abri com Read a planta EP-Terreno e a EP-Térreo. As demais imagens conferi pela descrição em §C7.

## Nota — Oscar (itens de modelo): **8,75 / 10,00 → APROVAR** (o mínimo é 8,00)
Nota anterior: 7,60. A nota subiu porque agora há prova colada: `get_levels`, parâmetros das paredes, saída da `criar_quadro_areas` e cotas.
O que ainda tira ponto: a largura das vagas cobertas, o M2 sem amostra completa, o M10 sem declaração e um elemento apagado sem identificação.

| # | Nota | Motivo |
|---|---|---|
| M1 | 0,60/0,60 | `get_levels` colado. O nível "Terreno 0,00" tem fonte (Skill Oscar §1 item 2, "Terreno = rua = 0,00") e não é duplicado. |
| M2 | 0,75/0,90 | Externas e internas do térreo têm amostra completa. No superior vieram só 2 ids (453890 e 453903), quando o mínimo é 3. |
| M3 | 0,50/0,50 | Conferi na imagem: cadeias 0,09/2,50/0,15/8,99 e 6,00/24,78/8,93, e o texto do norte pendente (T15). |
| M4 | 0,75/1,00 | A escada não foi tocada. A resposta da `criar_escada` continua sem colar. |
| M5 | 0,70/0,80 | Mesmo crédito da correção anterior. A conferência da escada segue parafraseada. |
| M6 | 0,65/0,70 | O corte AA morde a laje e o BB foi refeito. A partida por espelho está só descrita, e os rótulos de nível se sobrepõem no AA. |
| M7 | 1,10/1,20 | As elevações não mudaram. A lista final de vistas segue sem colar. |
| M8 | 0,80/0,80 | Saída completa colada, com fatores e ids por linha, na base de 571,60 m². |
| M9 | 0,85/0,90 | Refiz as contas: 219,11/571,60 = 38,33%; (204,93 + 206,45)/571,60 = 0,720; 187,27/571,60 = 32,76%; 9,29×25,075 − 4,05×4,575 = 214,42, e 214,42 − 206,45 = 7,97 (é o vão). A soma das áreas dá 95,71%, defeito da ferramenta, declarado. |
| M10 | 0,50/0,70 | Há contagens por categoria. Falta declarar "listado antes de repetir escrita". O elemento 454771 foi apagado sem ser identificado. |
| M11 | 0,60/0,70 | Resumo da ferramenta e os 11 avisos com motivo. Não veio a resposta completa. |
| M12 | 0,55/0,60 | As imagens batem com o texto, e as vagas descobertas agora aparecem. Ainda há rótulos sobrepostos no AA e na planta de CA. |
| M13 | 0,40/0,60 | As vagas cobertas estão desenhadas e entram certo no quadro. Mas a cota 5,02 é a **largura total das 2 vagas, medida de eixo a eixo**: o vão interno fica abaixo de 5,00, ou seja, menos de 2,50 por vaga. O "~5,275 ≥ 5,00" de §C5 é a profundidade (5,43), não a largura. A vaga não está provada com 2,50 de largura (COES Arts. 28–29). |

## Reprovação automática (§3 e §7.2): nenhuma
O M13 é erro de leitura de cota, não dado inventado: a imagem mostra o que o texto diz, só que o texto interpreta mal a cota.

## Queda de programa (452,41 contra ~520 m²)
Não pesa em nenhum item de M1–M13: o §7 mede o modelo, não o programa. Conferi a conta do Oscar: 228,64 + 13,83 ≈ 242 m² por pavimento, o que dá no máximo ~470 m² em 2 pavimentos. A queda é **consequência do teto de 40% do Regramento (P2)**, e não erro de execução. É decisão de projeto: Claudemberg, com Kelsen (3º pavimento ou gabarito) e o cliente (programa). Na nota da etapa, vira ponto de julgamento do Lúcio (§2): ele precisa levar a escolha ao cliente, e não absorvê-la calado.

## Fonte primária não verificada
Nenhuma norma nova. Seguem pendentes com Kelsen: o artigo do fator 0 da marquise e o da vaga 2 no CA (LC 270 Arts. 347 e 350).

## O que corrigir (pendências; não travam o ensaio)
1. Oscar, lacuna do Agente: cotar a largura das vagas cobertas **face a face** e garantir 2,50 por vaga, alargando a garagem se faltar. Fonte: COES LC 198/2019 Arts. 28–29 e a Skill de vaga.
2. Oscar, lacuna do Agente: colar a resposta da `criar_escada`, a lista final de vistas e o 3º id de parede do superior. Fonte: Skill Oscar, regra de prova.
3. Oscar, falha de processo: identificar o 454771 e declarar "listado antes de repetir". Fonte: Skill Oscar, seção de falhas.
4. Oscar: tirar a sobreposição de rótulos (AA, CA, cota das vagas descobertas) e mover o eixo 4. Fonte: NBR 6492:2021.
5. Vitruvius, defeito de ferramenta: resize com falso sucesso, cota de face interna que devolve eixo, soma 95,71% (piscina e deck fora de região) e colisão de nome na exportação.
6. Lúcio, Kelsen e cliente, decisão de projeto: o programa de 520 m² contra o teto de 40%.

## Para Claudemberg conferir no Revit (§7.4)
1. Largura interna das vagas cobertas 44 e 45, face a face (este é o ponto que mais preocupa).
2. Vagas descobertas 454843 e 454851 no afastamento lateral leste: se são aceitáveis (decide Kelsen).
3. Marcadores de elevação fora do muro, e as vistas mostrando fachada.
4. Escada 453969 com 1,20 m livre nas duas pontas, e o vão 454092.
5. Corte AA 454370 mordendo a laje, e o BB novo 454858 no duplo.
6. Fundos recuados: nenhuma parede ou laje sobrando de y 31 a y 34,925, nem duplicada (44 paredes, 13 pisos).
7. Base das paredes externas do térreo em −0,15, e o nível Terreno 0,00 sem duplicata.
8. Platibanda abaixo de 8,50 m a partir da soleira.
