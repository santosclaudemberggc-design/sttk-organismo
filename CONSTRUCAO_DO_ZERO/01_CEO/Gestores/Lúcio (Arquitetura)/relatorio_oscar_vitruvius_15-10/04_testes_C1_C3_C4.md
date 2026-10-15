# Testes C1, C3, C4 — só leitura (Oscar, 15/10/2026, 2ª execução)

Ordem: Lúcio, a mando de Wallenberg, com autorização de Claudemberg (15/10, SOMENTE LEITURA). Ferramentas usadas: `get_revit_status`, `get_document_info`, `get_levels`, `list_elements` (Cotas, Paredes, Pisos), `get_element` (410239, 449542, 323714). Nenhuma escrita, nenhum abrir/salvar.

A 1ª execução (mesmo dia) parou em `Error: Plugin não está conectado`; foi substituída por esta.

## Passo (b) — documento aberto

| Chamada | Saída colada (trecho) |
|---|---|
| `get_revit_status` | `"connected": true, "buildVersion": "2026-10-14-bloco1-correcao-v8", "documentTitle": "EP_Montenegro_003_v2_r1", "documentPath": "...\\etapa_05_estudo_preliminar\\entrega\\v2\\EP_Montenegro_003_v2_r1.rvt", "isModified": false`, levels 4, walls 20, doors 3, windows 6, rooms 19, floors 5 |
| `get_document_info` | `"name": "EP_Montenegro_003_v2_r1"`, mesmo caminho, `"version": "Autodesk Revit 2026"` |

Documento certo, plugin conectado. isModified no início: false. Só leituras depois disso; isModified no fim não foi relido (sem prova do fim, mas nenhuma ferramenta de escrita foi chamada).

## C1 — cor da cota

Prova:
- `list_elements` Cotas: 8 cotas (449542, 449543, 449545–449550), todas `"typeName": "cotas externas 2,0mm", "typeId": "410239"`.
- `get_element 410239` (DimensionType, "Estilo de cota linear"): `{"name": "Cor", "value": 255, "type": "Integer"}`. No inteiro de cor do Revit (R + G×256 + B×65536), 255 = R 255, G 0, B 0 = **vermelho**.
- `get_element 449542` (instância): nenhum parâmetro de cor; só `Família e tipo 410239`. A cor vem do tipo.
- Origem do tipo: o id 410239 é menor que todos os elementos do desenho de 14/10 (paredes a partir de 449352, cotas 4495xx). Isso indica que o tipo já existia no arquivo antes do desenho, ou seja, veio do template/arquivo-base. **Não há prova** de qual chamada escolheu esse tipo para as cotas (a escolha pela escala é da ferramenta `dimension`/facade, P13).

Conclusão: cor vermelha = **T** (parâmetro "Cor" do tipo do template, 255). A escolha de um tipo vermelho para cota de entrega é da ferramenta (sem filtro de cor) — já coberta por P13. Não é A.

## C3 — níveis, alturas, offsets × memorial do EP v2

Prova do modelo:
- `get_levels`: Terreno 0 (324604); Páv. térreo 0.3 (311); Páv. Superior 3.3 (694); Cobertura 6.3 (323714).
- Paredes da casa (16): `"Deslocamento da base": 0`, `"Deslocamento superior": 0`, térreo `Restrição da base "311"` → `Restrição superior "694"`; superior `"694"` → `"323714"`. Altura efetiva 3,00 (piso a piso). Muros 449393–449396: base 324604, topo 311 + `"Deslocamento superior": 0.7` (= 1,00 m).
- Pisos: 449437 e 449445 "LAJE 10 cm" com `"Espessura": 0.15`, topo 0.3 e 3.3; grama 449453/449467/449477 `"Espessura": 0.3`, topo 0.

Texto do memorial (`etapa_05_estudo_preliminar/entrega/v2/06_revit_prova_005_v2.md`, L44–L55): "Níveis do template (não alterados)" (L44); "Cobertura 6,30 (id 323714)" (L48); "O piso a piso de 3,00 m do template é hipótese esquemática" (L49); "o tipo 'LAJE 10 cm' aparece com 0,15 m de espessura" (L54).

Comparação: **modelo e memorial batem** em todos os números (0,30 / 3,30 / 6,30; paredes 3,00; laje 0,15; pé-direito livre 2,85; muros com +0,70). Não há divergência texto × modelo neste arquivo.

Conclusão: alturas = **escolha minha (A)** de aceitar os níveis do template sem justificar pé-direito (falta de justificativa, como já decidido). **Não é efeito de P5/P7**: os níveis deste arquivo estão nos valores do template (3,30 e 6,30); P5 e P7 aconteceram no arquivo de teste do Bloco 1, não aqui. Achado à parte: o nome "LAJE 10 cm" com espessura 0,15 é do tipo do template (T), já registrado em L54.

## C4 — Cobertura 6,30 → 6,20

Prova:
- `get_levels`: `{"id": "323714", "name": "Cobertura", "elevation": 6.3}`.
- `get_element 323714`: `{"name": "Elevação", "value": 20.669291338582926}` (pés; × 0,3048 = 6,30 m).

Conclusão: **no EP_Montenegro_003_v2_r1 a Cobertura está em 6,30; não houve mudança para 6,20 neste arquivo.** O 6,20 é do arquivo de teste do Bloco 1 (`D:\011_VITRUVIUS\_testes_bloco1\TESTE_BLOCO1_14-10_v2.rvt`; meu estado registra "R1 (níveis 3,25/6,20)" e P7 descreve a mudança sem chamada). Qual ferramenta mudou 6,30 → 6,20 naquele arquivo: **sem prova** (o arquivo não está aberto; abrir está fora da autorização de hoje). Reclassificação: C4 deixa de ser assunto da entrega do Ensaio 003 (não há defeito no v2_r1); fica só como defeito de ferramenta P7, a reproduzir no arquivo do Bloco 1.

## Resultado por item

| Item | Classificação | Prova |
|---|---|---|
| C1 cota vermelha | **T** (Cor 255 no tipo 410239 do template); escolha do tipo pela ferramenta = P13 | `get_element 410239` "Cor": 255; ids |
| C3 alturas | **A** (níveis do template aceitos sem justificativa); modelo = memorial; não é P5/P7 | `get_levels`, `list_elements` Paredes/Pisos, memorial L44–L55 |
| C4 Cobertura | **Não ocorre no v2_r1** (6,30); 6,20 é do arquivo do Bloco 1 → P7; ferramenta causadora sem prova | `get_levels`, `get_element 323714` |

## Pedidos de ferramenta

P31 em `D:\011_VITRUVIUS\PEDIDOS_OSCAR\10_pedidos_relatorio_conjunto_15-10.md`: `get_element` devolve valores em pés e cor como inteiro cru, divergindo de `list_elements` (metros).
