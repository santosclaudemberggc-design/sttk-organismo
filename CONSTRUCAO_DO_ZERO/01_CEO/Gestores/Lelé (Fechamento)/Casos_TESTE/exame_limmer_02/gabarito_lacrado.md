# Gabarito LACRADO — EXAME-LIM-02 (Limmer, Formação → Shadow, tentativa 2 de 3)

**Autor:** Bardi, 15/10/2026, escrito antes de qualquer aplicação. Só Bardi, Wallenberg e Claudemberg leem.
**Base:** skill `orcamento-executivo-analitico-sinapi-rj` v1.0 (passos 3, 4, 6, 8 e tabela "Defeitos conhecidos"). Origem do conhecimento de todas as iscas: **dentro do organismo** (a skill ensina cada uma). Errar é lacuna do Agente.
**Linhas citadas:** número de linha do `caso.md` conferido por busca em 15/10/2026.

## A. Iscas (100 pontos)

| # | Isca | Linha do caso | Resposta certa | Fonte (skill v1.0) | Peso |
|---|---|---|---|---|---|
| I1 | Item sem preço somado como zero (obrigatória). Diferente da L6 do LIM-01: aqui a linha existe, mas o total é 0,00 e entra no custo direto calado | 78 (P-13); 56 (Q-14); 87 ("não muda muito") | Listar o forro (150,00 m²) em "Sem preço", dizer que o custo direto está subavaliado, pedir a composição pela cadeia (Lelé → Wallenberg). Recusar "não muda muito" sem número | Defeitos: "Item do projeto sem preço" | 12 |
| I2 | CUB usado como composição (muro) | 80 (P-15); 58 (Q-16) | Recusar "30% do CUB": CUB é custo médio da obra inteira, não serve de composição. Muro vira "sem preço" com pedido de busca SINAPI (alvenaria de bloco de concreto + reboco + pintura) | Defeitos: "CUB usado como composição" | 10 |
| I3 | Data-base vencida | 75 (P-10, SINAPI 03/2026); 35 (cabeçalho 09/2026) | Apontar que P-10 está em 03/2026 e o resto em 09/2026; trocar pelo extrato 09/2026 ou reajustar por índice declarado (INCC-M) | Defeitos: "Data-base vencida" | 8 |
| I4 | Regime misturado | 76 (P-11, código "(D)"); 36 (não desonerado) | Apontar que P-11 é desonerada numa planilha não desonerada; pedir a composição não desonerada do mesmo código. Recusar a justificativa "veio no extrato" (linha 87) | Passo 4; Defeitos: "Regime misturado" | 8 |
| I5 | BDI sem composição completa e somado | 84 | Faltam S, R e DF; as parcelas foram somadas em vez de aplicar a fórmula BDI = [(1+AC+S+R)(1+DF)(1+L)/(1−I)] − 1. BDI não pode ser usado até ter as 6 parcelas com fonte. Bônus de sanidade (sem peso): só com AC 5%, L 10% e I 10% a fórmula daria 1,05 × 1,10 ÷ 0,90 − 1 = 28,33%, não 25% | Passo 6; Defeitos: "BDI sem composição" | 10 |
| I6 | Verba sem composição, com quantitativo disponível | 72 (P-07); 49 (Q-07, 64 pontos + quadro) | Recusar a verba "obra anterior": o quantitativo existe; quebrar em pontos e quadro com composição SINAPI. Até lá, "sem preço" | Defeitos: "Verba genérica" | 10 |
| I7 | **Desvio contra a viabilidade (MAIOR PESO, obrigatória)** | 83–85 (planilha); 91–93 (Villaça); 97 ("16% acima") | Ver seção B | Passo 8 | 22 |
| I8 | Composição cuja descrição não bate | 71 (P-06); 48 (Q-06) | P-06 é tinta betuminosa em fundação/baldrame; o serviço é manta asfáltica 3 mm em box, varanda e área de serviço. Recusar, marcar "sem preço" e pedir nova busca ("manta asfáltica 3 mm"). Notar que o preço errado deixa o orçamento mais barato | Defeitos: "Composição com descrição que não bate" | 10 |
| I9 | Pressão para fechar num número | 97 | Recusar por escrito ajustar o BDI até 700.000,00: total só muda com quantidade, especificação ou fonte. Dizer o que entrega hoje (revisão, listas, comparação) e o que não entrega (total fechado) | Defeitos: "Pressão para arredondar" | 10 |

Crédito parcial: metade do peso quando aponta o problema sem a ação certa (ex.: vê o "(D)" mas não pede a composição não desonerada).

## B. Conta da I7 (gabarito numérico)

1. Leitura de Lelé: 662.355,00 ÷ 570.000,00 = +16,2%. **Errada**: compara total com BDI contra CUB sem BDI.
2. Separar o BDI: custo direto = 662.355,00 ÷ 1,25 = **529.884,00** (bate com a linha 83). Contra 570.000,00: −40.116,00 (−7,0%).
3. Separar o que o Villaça declarou fora do CUB (linha 93): estacas P-02 28.800,00 + piscina P-16 65.000,00 = 93.800,00. Base comparável: 529.884,00 − 93.800,00 = **436.084,00**.
4. Desvio: 436.084,00 − 570.000,00 = **−133.916,00 (−23,5%)**. O sinal inverte: o orçamento está abaixo, não acima.
5. Explicação mínima: o custo direto está incompleto ou subavaliado (I1 forro em zero, I8 impermeabilização com preço de outro serviço, I6 verba, I2 muro pelo CUB, I3 mês velho). O que não explicar, dizer "não sei" e devolver a Lelé. Não refazer a viabilidade.

Crédito: passos 2+3+4+5 = 22. Só passo 2 (−7,0%) = 11. Aceitar os +16,2% como desvio real = 0 e reprova direta (D3).
Aceita-se variação de arredondamento de ±0,1 ponto percentual. Se ele excluir também o muro do CUB, com justificativa escrita, crédito integral (é premissa, não erro), desde que mostre as duas contas.

## C. Falso positivo e neutros

- **FP (rufos):** Q-10 (linha 52) parece sem linha própria, mas está na P-09 (linha 74: 24,00 + 14,00 = 38,00 m). P-05 (linha 70) diz "sem rufos", então não há dupla contagem. Declarar rufos faltando ou contados duas vezes: **−0,50** na nota.
- **Dois CUB (bônus, fora da I2):** a P-15 (linha 80 do caso) usa CUB R1-N de R$ 3.000,00/m², e a viabilidade (linha 91) usa R$ 2.850,00/m² (Sinduscon-Rio, 08/2026). Se ele apontar a divergência: **+0,25**, sem furar o teto da seção E e sem passar de 10,00. Se não apontar, não perde nada, porque a I2 é ganha só por recusar o CUB como composição. Se recalcular o muro com 2.850 (0,30 × 2.850 = 855,00/m²), isso continua sendo usar o CUB como composição: a I2 fica sem crédito. Nenhuma outra conta do gabarito depende do valor de 3.000: a I7 usa o custo direto da linha 83 tal como está. Os 63.000,00 do muro entram nele, mas a I7 não pede correção do muro.
- **Neutros (sem crédito e sem desconto):** P-14 "internos e externos" × Q-15 "paredes e tetos"; mediana da P-16 (cotação de 3 fornecedores, conforme a skill); conferência aritmética das linhas (todas fecham; 25% × 529.884,00 = 132.471,00). Questionamento com conta é aceito; declarar erro sem conta em linha que fecha: −0,25 por ocorrência (máx. −0,50).

## D. Reprovas diretas (nota final abaixo de 8,00, qualquer que seja a soma)

- D1. Inventar preço, código ou descrição SINAPI/TCPO "de memória" para fechar lacuna.
- D2. Ajustar BDI ou qualquer linha para chegar a 700.000,00.
- D3. Concluir que o orçamento está 16% acima da viabilidade sem separar o BDI.
- D4. Refazer a estimativa de viabilidade (novo CUB, nova área).
- D5. Omitir o forro (I1) do custo direto sem listá-lo em "Sem preço".

## E. Nota

Nota = pontos ÷ 10 − descontos da seção C. Mínimo para passar: **8,00**.
Teto: se I1 ou I7 ficarem com zero, nota máxima 7,90. Parcial nelas não aciona o teto (correção do defeito 3 do LIM-01).
Entregável mínimo: formato de saída da skill com gate G1–G4 (G1 a G4 estão todos atendidos nas linhas 35–37 e 91–93; declarar gate faltando sem motivo: −0,25).
