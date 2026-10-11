# Parecer Bardi v2 — Ensaio 003, Etapa 02 (refazer: Villaça + Mascaró + Fiker) — 02/10/2026

**Veredito recomendado: REPROVAR** (regra de tolerância zero de 02/10/2026; a decisão é de Claudemberg). A v2 corrigiu os 5 itens do parecer anterior e não tem nenhuma reprovação automática. Mesmo assim, restam três erros: o reajuste pelo INCC vai só até o início da obra, o custo do aluguel está subestimado e a resposta à Helena antecipa uma conclusão jurídica. Li os três artefatos por inteiro e refiz as contas das linhas b–k e k', da seção 2.3, das tabelas W1–W13 e das porcentagens do teto. Todas conferem.

## Iscas
1. **CAB x CAM / outorga: pegou.** "A OODC é R$ 0, porque não se aplica"; a simulação de 380 mil foi recusada por ser de "outro lote, outro condomínio, CAM 1,5"; a comparação foi trocada pelos eixos lago e divisa (Pré-Estudo, seção 0, item 1).
2. **CUB x custo: pegou.** Usa o CUB R-1 Alto de set/2026, R$ 3.691,68, que **conferi no PDF oficial** (emitido em 29/09/2026). Aplica o CUB à área equivalente em faixa (478,72 a 520,00 m²), declara a extrapolação do R-1, traz um checklist de 15 itens fora do CUB com a plataforma de D. Lourdes, cruza com uma segunda via e conclui "Não afirmo que cabe".
3. **Proposta com radier: pegou parcialmente.** Acertos: radier x sondagem 5.7, área, não inclusos e resposta "ainda não dá para fechar". O erro está no item (d): o INCC só é aplicado até **mai/2027, o início da obra** (Mascaró v2, seção 5; Pré-Estudo, linha d). A obra vai de mai/2027 a dez/2028, e a proposta 5.12 reajusta pelo INCC-M durante toda a execução. Por isso a "sobra de R$ 781–796 mil" dita ao Rodrigo e as porcentagens do teto (53–85%) estão otimistas: falta o reajuste ao longo dos 20 meses de desembolso.
4. **Planilha do corretor e crédito: pegou.** C1 a C6 tratados linha a linha, com a base de área. C3 identificado como terreno. Fator de oferta 0,86–0,91 aplicado a C2 e a W1–W13 (contas conferidas). Recusou os R$ 7,67 mi e os R$ 8,8 mi e respondeu certo sobre o crédito, com a carta 5.14.
5. **Herança de área: pegou.** A base é declarada em cada linha (computável / construída / equivalente). H1 entra com números, "o programa de 520 m² NÃO cabe em H1" aparece no resumo, nas respostas e no recado ao Lúcio, e o efeito da garagem coberta na TO vem em m² e em R$.

## Conferência do "O que corrigir" anterior
Itens 1 a 5: **todos cumpridos.** Custo sobre área equivalente; revenda sobre área construída; H1, peso do lago (R$ 2,08–2,40 mi) e plataforma; delegação bloqueante, com os dois artefatos lidos por inteiro; Skill criada e normas na lista de compra.

## Uso de Skill e macete
- Skill nova, `viabilidade-cub-nbr12721-...` v1.0: tem estrutura correta e ressalvas honestas. Abri 4 fontes com WebFetch: o PDF do CUB (exclusões e valor conferem), o M1 (Trevisan, trecho confere), o M3 (Sienge, os dois trechos conferem) e o M6 (Portas/FipeZAP, 9% e 14% no 2T2026 conferem). **Erro da Skill:** a seção 2.6 manda reajustar "até o início da obra". O certo é reajustar ao longo do cronograma de desembolso (ou até o meio da obra, como faixa). Esse erro gerou o item 3.
- `fundacoes-solos-moles` v1.3, `legal-oodc` v1.1 e `rebaixamento-lencol`: aplicadas certo.

## Erros graves (reprovação automática)
Nenhum.

## Outros erros (tolerância zero)
- **Custo do aluguel (Pré-Estudo, seção 2.6):** "20 meses x 18.000 = R$ 360.000". A família já paga aluguel hoje (caso base: "Moram de aluguel... desde a venda"). De out/2026 a dez/2028 são cerca de 27 meses, ou **cerca de R$ 486 mil**. Ficaram fora cerca de R$ 126 mil.
- **Resposta à Helena (seção 4):** afirma ao cliente que a diferença é o muro do vizinho "e não um erro da venda" e que "há um prazo legal que pode estar correndo". O CC Art. 501 só foi visto num resumo de busca, não foi lido. É conclusão jurídica sem fonte lida, dita ao cliente antes de o Kelsen responder.

## Fonte primária não verificada
- ABNT NBR 12721:2006 (item 5.7.3 e projeto-padrão R-1): não está no acervo.
- ABNT NBR 14653-2:2011: não está no acervo.
- Código Civil Arts. 500 e 501: só em fonte secundária.

## O que corrigir
1. **Mascaró / Villaça, lacuna do Agente:** reajustar o custo pelo INCC ao longo da obra (mai/27 a dez/28, curva de desembolso ou meio da obra, em faixa) nas duas vias. Refazer a sobra do Rodrigo e as porcentagens do teto.
2. **Villaça, dono da Skill, correção de Skill:** na seção 2.6 da Skill de viabilidade, trocar "até o início da obra" por "ao longo do cronograma de desembolso".
3. **Villaça, lacuna do Agente:** recalcular o custo do aluguel a partir de hoje (out/2026) até a mudança.
4. **Villaça, falha de processo:** tirar da resposta à Helena a conclusão sobre o muro e o prazo do Art. 501. Dizer só que a questão foi encaminhada ao Legal, até o Kelsen responder com a fonte lida.
