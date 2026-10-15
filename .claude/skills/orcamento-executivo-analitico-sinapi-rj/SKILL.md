---
name: orcamento-executivo-analitico-sinapi-rj
description: Ensina a montar o orçamento executivo analítico de casa unifamiliar no Rio (etapa 16) — quantitativo por serviço, composição SINAPI-RJ ou TCPO com código e data-base, encargos, BDI com composição escrita, premissas explícitas e comparação com a estimativa de viabilidade do Villaça. Use SEMPRE que o Limmer (ou outro agente) for orçar o executivo, montar planilha de custo, aplicar BDI, escolher desonerado ou não desonerado, comparar orçado com estimado, ou responder "quanto custa a obra" a partir do projeto executivo, mesmo que o pedido só diga "orçamento", "planilha", "preço", "BDI" ou "SINAPI".
version: v1.0
status: ativa-com-ressalva
dona: Lelé
validacao: "Ratificada por Claudemberg em 15/10/2026 como ativa-com-ressalva, após os 3 casos de evals.json aprovados com o Limmer. Ressalva: Acórdão TCU 2.622/2013 e exclusões da NBR 12721 não lidos no texto oficial."
data: 2026-10-15
fontes: "_ferramentas/sinapi_consulta.py e _referencias_precos/SINAPI/2026-09_baixado-2026-10-11/ (SINAPI 09/2026, lido por Wallenberg em 15/10/2026); Gestores/Lelé (Fechamento)/proposta_equipe_fechamento_10-10-2026.md, seção 4; skill viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj; Acórdão TCU 2.622/2013 (faixas de BDI) — NÃO lido no texto oficial nesta versão."
---

# Orçamento executivo analítico — casa unifamiliar, RJ

## Regra mãe

Nenhum número entra no orçamento sem **fonte, código e data-base**, e nenhuma conta fica escondida. Um orçamento sem fonte não pode ser conferido, e um número que não pode ser conferido não serve para fechar contrato.

## Gate de entrada

Antes de começar, confirme e cole a prova de cada item:

| # | Condição | Prova |
|---|---|---|
| G1 | O projeto executivo está na revisão final (Gate de compatibilização sem RFI aberto que mude quantidade) | Revisão e data de cada prancha usada |
| G2 | Você tem o extrato SINAPI-RJ do mês de referência | Nome do arquivo de extrato e o mês (ex.: SINAPI 09/2026) |
| G3 | Você sabe o regime: desonerado ou não desonerado | Frase de quem decidiu (Lelé ou cliente) e o motivo |
| G4 | Você tem a estimativa de viabilidade do Villaça (linha de base) | Arquivo, data e valor |

Se faltar um item, **recuse só a parte que depende dele**, diga "não verifiquei" e siga com o resto.

## Passos

| # | Passo | Prova obrigatória |
|---|---|---|
| 1 | Liste os serviços por etapa da obra (serviços preliminares, fundação, estrutura, alvenaria, cobertura, impermeabilização, instalações, esquadrias, revestimentos, pintura, louças e metais, serviços complementares, limpeza). | Lista com a prancha ou o memorial de onde veio cada serviço |
| 2 | Calcule o quantitativo de cada serviço a partir do projeto. Escreva a conta. | Conta com cota e prancha (ex.: 3,20 × 4,00 = 12,80 m², PE-03) |
| 3 | Para cada serviço, escolha a composição: **SINAPI-RJ** primeiro (código e descrição); se não houver, **TCPO** (edição e código); se não houver, **cotação** de 3 fornecedores (nome, data, validade). | Código, descrição, unidade, preço unitário, mês |
| 4 | Use **um regime só** em toda a planilha (desonerado ou não desonerado). Misturar regimes distorce o custo. | O regime escrito no cabeçalho |
| 5 | Calcule o custo direto: quantitativo × preço unitário. | Conta por linha e total |
| 6 | Aplique o BDI **com a composição escrita**: administração central (AC), seguro e garantia (S), risco (R), despesas financeiras (DF), lucro (L) e tributos (I). Fórmula: BDI = [(1+AC+S+R)(1+DF)(1+L)/(1−I)] − 1. | Cada parcela em %, a fonte de cada uma e a conta |
| 7 | Escreva as premissas: data-base, regime, local, o que está e o que não está incluído, validade do preço. | Lista de premissas |
| 8 | Compare o total com a estimativa de viabilidade do Villaça. Antes de comparar, separe o BDI (custo direto = total ÷ (1 + BDI)), porque o CUB não inclui BDI. Separe também os itens que o CUB não cobre, como fundação especial e piscina (conferir a lista de exclusões na NBR 12721 antes de usar com cliente). Se a diferença que sobrar passar de 10%, explique item por item; o que não souber explicar, devolva a Lelé com "não sei". | Valor estimado, valor orçado, BDI separado, itens fora do CUB, diferença em R$ e em %, e a explicação |
| 9 | Entregue no formato de saída abaixo. | O próprio formato |

## Defeitos conhecidos e contorno

| Defeito | Por que é erro | Contorno |
|---|---|---|
| "Verba" genérica no lugar de serviço | Não dá para conferir nem medir | Quebrar em serviços com quantitativo e composição. Se for mesmo verba, dizer o que cobre e a fonte do valor |
| CUB usado como composição de serviço | CUB é custo médio por m² de obra inteira (NBR 12721), serve para estimativa, não para orçamento analítico | Usar CUB só na comparação do passo 8 |
| Data-base vencida | Preço de outro mês distorce o total | Usar o SINAPI do mês mais recente disponível; se usar outro, reajustar pelo índice e dizer qual (INCC-M ou o do contrato) |
| Regime misturado | Desonerado e não desonerado têm encargos diferentes | Um regime só na planilha toda (passo 4) |
| BDI sem composição | Um BDI "de mercado" não pode ser conferido | Abrir as 6 parcelas (passo 6) |
| Item do projeto sem preço | Orçamento incompleto parece mais barato | Listar o item como "sem preço" e cobrar o insumo pela cadeia; nunca omitir |
| Desvio grande sem explicação | Ou o orçamento ou a viabilidade estão errados | Explicar item por item (passo 8); se não souber, dizer "não sei" e devolver a Lelé |
| Pressão para arredondar ou "fechar num número" | Ajustar o número sem mudar o escopo é inventar | Recusar por escrito. Só muda o total se mudar quantidade, especificação ou fonte |
| Composição com descrição que não bate com o serviço (ex.: busca "pintura acrílica" devolve textura de fachada de prédio; busca "contrapiso" devolve só a argamassa por m³) | O preço de outro serviço, ou só do insumo, distorce o custo e quase sempre deixa o orçamento mais barato | Ler a descrição inteira e a unidade antes de usar. Se não bater, marcar "sem preço" e pedir nova busca com termos mais precisos |
| Duas composições válidas e o projeto não diz qual (ex.: bloco com furos na horizontal ou na vertical) | Escolher sozinho é decidir especificação de outra disciplina | Usar a de menor risco como provisória, mostrar a alternativa com a diferença em R$ e pedir a confirmação ao dono pela cadeia |
| Consulta ao SINAPI exige terminal | O Limmer não tem terminal | Pedir o extrato a Lelé, que pede ao Wallenberg: `python -I _ferramentas/sinapi_consulta.py "<termos>" --uf RJ [--desonerado]`. Ler o extrato salvo |
| Faixa de BDI de referência | O Acórdão TCU 2.622/2013 tem faixas para obra pública; não foi lido no texto oficial nesta versão | Usar só como referência de sanidade, citando que não foi conferido. Nunca como valor do BDI |

## Formato de saída

```
## Orçamento executivo — <obra>, <revisão do executivo>
Data-base: <SINAPI mês/ano, RJ> | Regime: <desonerado ou não desonerado> | Gate: G1 <ok/falta> G2 <…> G3 <…> G4 <…>

| Etapa | Serviço | Prancha | Qtd. | Un. | Fonte e código | Preço unit. | Total |
|---|---|---|---|---|---|---|---|

Custo direto: R$ <…>
BDI: AC <%> + S <%> + R <%> + DF <%> + L <%> + I <%> = <%> (conta escrita)
Total com BDI: R$ <…>

Premissas: <lista>
Não incluído: <lista>
Sem preço (insumo faltando): <lista, com dono e cadeia>
Comparação com a viabilidade: estimado R$ <…> (Villaça, <data>) × orçado R$ <…> = <diferença R$ e %>. Explicação: <…>
Não verifiquei: <lista>
```

## Checklist final

- [ ] Toda linha tem fonte, código e data-base
- [ ] Um regime só, declarado
- [ ] BDI com as 6 parcelas e a conta
- [ ] Toda conta de quantitativo escrita, com prancha
- [ ] Itens sem preço listados, não omitidos
- [ ] Comparação com a viabilidade explicada
- [ ] "Não verifiquei" onde faltou dado

## Relação com outras skills

- **Complementa** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` (Villaça): a viabilidade estima pelo CUB antes do projeto; esta skill orça pelo projeto executivo e compara com aquela estimativa.
- **Difere de** `reforma-orcamento-obra-rj` (frente Reforma): mesma ferramenta SINAPI, mas para obra nova e etapa 16.
- **Não substitui** `ia-orcamento-executivo-obra`, que é panorama de ferramentas de mercado.

## Changelog

- v0.1 (15/10/2026, Wallenberg, Função 5): criada como rascunho para destravar o exame do Limmer. Pendente: ler o Acórdão TCU 2.622/2013 no texto oficial.
- v0.2 (15/10/2026, Wallenberg): teste E1 feito com o Limmer (passou nas 4 asserções). Duas linhas novas na tabela de defeitos, sugeridas por ele: composição com descrição que não bate com o serviço, e duas composições válidas sem definição no projeto. E2 e E3 ainda não testados.
- v0.3 (15/10/2026, Wallenberg): testes E2 e E3 feitos com o Limmer, os dois aprovados. Passo 8 ganha a separação do BDI e dos itens fora do CUB antes da comparação (sugestão do Limmer no E3). Pendências: ler o Acórdão TCU 2.622/2013 e as exclusões da NBR 12721 no texto oficial; o extrato SINAPI sai com acentos corrompidos (códigos e preços legíveis).
- v1.0 (15/10/2026): ratificada por Claudemberg como ativa-com-ressalva.
