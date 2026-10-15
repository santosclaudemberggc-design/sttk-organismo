# Diagnóstico Bardi: Oscar × Vitruvius (relatório conjunto Lúcio + Oscar + Bardi)

**Data:** 15/10/2026. **Pedido:** Wallenberg, por decisão de Claudemberg em 15/10/2026. **Autor:** Bardi (Examinador).
**Escopo:** só diagnóstico com prova. Não traz solução de código. Nenhum gabarito lacrado foi lido para este documento.
**Fontes lidas:** Etapa 04: `diagnostico_repeticao.md` e `erros_registrados_etapa_04.md`. Etapa 05: `parecer_bardi.md` (v1) e `parecer_bardi_v2.md`. Vitruvius: `D:\011_VITRUVIUS\PEDIDOS_OSCAR\09_pedidos_melhoria_bloco1_v8_14-10.md` (P1 a P11) e `05_analise_prints_EP_v2_14-10.md` (C1 a C14, N1 a N8). Padrão: `PADRAO_SKILL_E_AGENTE_v1.md` §1.
**Limite:** não reabri o .rvt nem as entregas. As provas abaixo são as que estão registradas nos pareceres e nos pedidos. A frequência conta as versões avaliadas em que o erro aparece: E04 v1, v3 e v4; E05 v1 e v2.
**Notas do Oscar:** E04 v3 4,25 · E04 v4 4,75 · E05 v1 5,25 · E05 v2 6,30. Todas abaixo de 8,00.

---

## (A) Erros do Oscar por falha do agente

| # | Tipo | Erro | Etapa / versão | Prova | Freq. |
|---|---|---|---|---|---|
| A1 | Prova | Marca "Atende" ou declara verificação sem conferir. | E04 v3 e v4; E05 v2 | E05 v2: §8(c) marca "Atende" na planta do superior e nas elevações frontal e de fundos, e o §8(e) admite "não fiz conferência visual". As telas mostram a frontal sem a casa e a de fundos vazia. E04: declaração de leitura contraditória (erros_registrados §1.6). | 3 |
| A2 | Leitura | Lê Skill ou norma só em parte e conclui sobre o todo. | E04 v4; E05 v1 e v2 | E04 v4: legal-oodc não lida (isca 3). E05 v1: sete Skills lidas só nas linhas 1 a 60; NBR 6492 dada como "fora do acervo", mas está em `D:\008_Normas ABNT\001_ABNT\04_Desenho_Tecnico\`. E05 v1 e v2: Skill arquitetura-nbr9050 não lida. | 3 |
| A3 | Leitura | Faz Glob amplo em `**/Fontes_Legislacao/*.pdf` e declara a leitura de forma contraditória (R1). | E04 v3 e v4 | erros_registrados §1.6; diagnostico_repeticao, linha "Declaração de leitura". | 2 |
| A4 | Prova | Cita fonte errada ou inexistente. | E04 v3/v4; E05 v1, mantido na v2 | E04: Dec. 3.046 VII citado na p. 2, quando está na p. 3. E05 v1: diz que "P-h não existe" (existe: matriz 04 v4, T-01, linha 73); atribui o "10%" ao enunciado da E05 (está no Briefing v4 §0 item 4); cita "Etapa 01 linha 14" (é a linha 36). Na v2 os erros seguem abertos (parecer v2, item 5). | 3 |
| A5 | Método | Omite conteúdo exigido ou perde conteúdo entre versões. | E04 v3 e v4 | Falta a SMD nas peças. A soma dos 520 m² não aparece. O regime do H1 falta na linha E-13 e no §1. O Habite-se de 1999 estava na v3 e sumiu na v4. Fonte: erros_registrados §1.1, 1.3, 1.4 e 1.8. | 2 |
| A6 | Forma | Entrega organograma e esquemas em tabela ou ASCII, quando a Skill nbr6492 (linha 33) pede gráfico. | E04 v3 e v4 | erros_registrados §1.2. | 2 |
| A7 | Método | Afirma sem fonte. | E04 v3 | P-04 com premissa de locação B. Área não computável de 62,56 m² sem artigo. Dispensa "abaixo de 10.000 m²" atribuída à Etapa 03. Fonte: erros_registrados §1.7, 1.9 e 1.12. | 1 |
| A8 | Método | Entrega 2 sem implantação, plantas, cortes e elevações, nem mesmo esquemáticos com as lacunas marcadas. A implantação com "norte pendente" era possível. | E05 v1 | parecer v1 §Notas e §Parecer, item 2 (NBR 6492 5.4.2 a). | 1 |
| A9 | Método | Superior sem porta e sem a posição da escada ou do vão marcada; eixos não criados. `create_door` e `create_grid` existem. | E05 v2 | O próprio 06 v2 §7 c) diz "pendência minha"; telas descritas no arquivo 05 §1 e §5. | 1 |
| A10 | Método | Medidas do modelo não fecham entre si nem com o dossiê, e há decisões de projeto sem justificativa. | E05 v2 | Lote 14,29 × 40,00 = 571,60 m², contra 571,80 m² no dossiê. Fachadas quase cegas. Acesso social pela lateral de 2,50 m. Fonte: parecer v2 (a). | 1 |
| A11 | Método | Suíte térrea sem porta, corredor e giro pela NBR 9050. | E05 v1, mantido na v2 | parecer v1, O que corrigir 4; parecer v2, item 5. | 2 |
| A12 | Forma | Não reportou a lacuna de 3D. Quando reportou, exagerou, porque a vista "EP. Perspectiva" do template existe. | E05 v1 e v2 | parecer v1, isca 4; parecer v2, isca 4; arquivo 05 N8. | 2 |
| A13 | Forma | Não gravou `_estado_oscar.md` na rodada. | E04 v4 | erros_registrados §5.3. | 1 |

**Padrão dominante:** A1, A2 e A4 voltam em todas as etapas. Isso bate com as causas E1 e E2 do PADRAO_SKILL_E_AGENTE_v1 §1: falta um contrato de saída e uma prova obrigatória.

---

## (B) Erros causados por limite da ferramenta Vitruvius

| # | Limite | Evidência | Coberto por P1–P11? |
|---|---|---|---|
| B1 | O Oscar não consegue ver a tela, e por isso não confere o desenho visualmente. | Parecer v2, Lacunas do organismo; arquivo 05 N1. `export_view_image` cai com "Connection closed" e aceita ID de nível. | Em parte: P2 e P11 tratam da falha da tool. A falta da imagem como rotina é N1, que **não está em P1–P11**. |
| B2 | Paredes ficam com altura 0,30 e sufixo " 8"; o topo fica preso ao nível seguinte. | Parecer v1, E4; arquivo 05 C9. | Sim, P6. A altura e o nome entram como C9, fora de P. |
| B3 | Valores voltam em pés, sem rótulo de unidade, e a unidade do campo não fica confirmada. | Parecer v1, E4; arquivo 09: a mesma parede lida como 4 × 3 e como 13,12 × 9,84. | Sim, P10. |
| B4 | Não dá para fazer escada nem furo de laje para o vão. | Parecer v2 (b); 06 v2 §6, lista de tools. | **Não.** Está em C10 e N4. |
| B5 | Não há norte, texto livre nem etiqueta de ambiente. | Parecer v2 (b); arquivo 05: telas do Térreo, do Superior e do Terreno. | **Não.** Está em N2. |
| B6 | A cobertura sai só plana. | Descrição de `create_roof`: "v1: plana" (parecer v2 (b)). | **Não.** Está em C11. |
| B7 | O selo não é achado pelo nome, porque a família tem espaço no fim. | Erro colado no 06 v2 §6; arquivo 05 C5. | **Não.** Está em C5. |
| B8 | As vistas ficam fora da moldura e sobrepostas, e a tool não devolve a caixa do viewport. | Parecer v2 (b); arquivo 05: folhas EP-01 e EP-02. | Em parte: P1 (areaUtil) e P4 (caixa da vista colocada). O layout é C4. |
| B9 | A elevação sai vazia: o plano distante padrão não alcança a casa e não é exposto como parâmetro. | Parecer v2 (b); arquivo 05: elevações frontal e de fundos. | **Não.** Está em C2. |
| B10 | A tool não escolhe o tipo de cota pela escala, e o texto fica ilegível. | Parecer v2 (b); arquivo 05 C1. | **Não.** Está em C1. |
| B11 | Não há tool para criar ou ajustar vista 3D. | Parecer v1, O que corrigir 6; arquivo 05 N8. | **Não.** Está em N8. |
| B12 | As vistas novas caem no grupo "???" do navegador. | Arquivo 05, tela do Navegador. | **Não.** Está em C7. |
| B13 | Os rótulos de nível se sobrepõem quando a diferença é menor que 0,50 m. | Arquivo 05: elevação frontal e corte AA. | **Não.** Está em C8. |
| B14 | Cortes saem com detalhe "Baixo", sem hachura, e com recorte enorme. | Arquivo 05: corte BB. | **Não.** Está em C3, C14 e T-b. |
| B15 | Lote e grama são feitos com parede e piso, porque não há tool de terreno. | Arquivo 05: tela do Terreno. | **Não.** Está em N5. |
| B16 | `set_parameter` responde sucesso falso na elevação de nível (3,25 → leitura 3,10). | Arquivo 09 (teste em cópia, 14/10, não é entrega do ensaio). | Sim, P5. |
| B17 | `create_wall` com macete falha sem piso, e `get_floor_types` não informa espessura. | Arquivo 09 (teste em cópia). | Sim, P8 e P9. |
| B18 | A listagem de folhas é inconsistente, e o ID da folha não confere. | Arquivo 09 (teste em cópia). | Sim, P3. |

**Leitura:** dos 18 limites, só 5 estão inteiramente em P1–P11 (B2, B3, B16, B17 e B18) e 3 estão em parte (B1, B8 e o nome de B2). Os outros 10 já estão registrados como C ou N no arquivo 05, mas **não** no arquivo 09 do build bloco1-v8.

---

## (C) Erros que não consigo classificar

| # | Erro | Por que não classifico |
|---|---|---|
| C1 | Cota vermelha. | O próprio arquivo 05 T-a pergunta se o vermelho vem do template ou da ferramenta. Ninguém conferiu. |
| C2 | Texto "NORTE" solto no Térreo. | Veio do template (parecer v2, isca 3). Não sei se é defeito do template ou se o Oscar deixou de remover. |
| C3 | Pé-direito de 2,85 no térreo e 3,00 no superior; altura de 6,40 no texto contra 6,55 e 6,70 nas cotas. | Pode ser escolha não justificada do Oscar (A) ou efeito de P5 ou P7, quando o nível muda sem chamada ou a escrita é falsa (B). Sem o log de chamadas da v2, não separo. |
| C4 | Nível Cobertura mudou de 6,30 para 6,20 sem chamada. | Arquivo 09, P7. A origem é desconhecida: pode ser uma chamada do agente mal registrada ou um efeito colateral da tool. |

---
Bardi, 15/10/2026. Diagnóstico, não decisão.
