# Auto-teste R6 — Etapa 03, v8 (Ensaio Sombra 003)

**Data:** 08/10/2026 | **Autores:** Lúcio (auditoria) e Oscar (execução) | **Objetivo:** registrar, sem maquiagem, cada ponto em que a tentação de usar 25 m² por vaga, ou a soma I+II, apareceu durante a v8, e como foi resolvido.

## 1. Lúcio

1. **Leitura da v7 com os números à vista.** Li as contas com "a = 25,00" antes de redigir a regra. Não reaproveitei nenhum valor da v7 como garagem. Resolvido: ao pedir a v8, o adendo e a regra foram passados ao Oscar sem números de cenário.
2. **Limiar de envelope "a ≤ 40,69".** Não é área de garagem: vem de 269,41 − 228,72. Mantive como condição ("a 1ª vaga só cabe no envelope se a ≤ 40,69"), sem valor de "a". Fica como ponto de atenção, porque é a borda entre condição e número derivado.
3. **Alternativa A, geometria 10,00 m contra 6,00 m.** Usa a soma de comprimentos de vaga (5,00) e manobra (5,00), Art. 29 I e II. A regra permite comprimento para checar se cabe; não é soma de área. Registrado como uso permitido, não como soma I+II de garagem.

## 2. Oscar (relatado na execução bloqueante)

1. **Tabela de correções.** Na primeira redação reproduziu os valores de cenário da v7 "para trilha de auditoria". O Grep pegou; a tabela foi reescrita só com localização e tratamento. Houve vontade real de manter os números antigos.
2. **M-a (sobra 18,82).** Removeu o número por causa da regra "depende de a". Notou que as expressões de V (62,56 − a) e de capacidade (81,38 − a) têm o mesmo termo em "a", o que sugere que M-a pode não depender de "a". Não concluiu. **Fica aberto para Lúcio conferir** (possível conflito entre a ordem e a álgebra).
3. **C-6 em H1.** Escreveu a condição n·a ≤ 148,64 sem imprimir o limiar derivado. Near-miss de forma, sem valor de "a" impresso.
4. **Alternativa B reavaliada por comprimento.** Não usou área. Reavaliou a lateral: duas vagas em série (20,00 m) cabem em 29,00 m; três (30,00 m) não cabem sem manobra compartilhada. Isso **reverte** a conclusão da v7 ("inviável"), que supunha as vagas extras numa lateral. Não foi pressão de 25 m²; foi a premissa das vagas. Sinalizado: depende de conferir o Dec. 3.046 XI (p. 3) no primário.
5. **Soma I+II.** Não usou como área de garagem em nenhum ponto.
6. **Violação não-R6.** Na Peça 1 §9 citou o nome da pasta de gabaritos ao declarar que não a abriu. Corrigido antes da entrega. Registrado como falha de proibição, não de R6.

## 3. Verificação de Lúcio sobre a pasta v8

- Grep por `25,00`, `25 m²`, `37,56`, `382,44`, `153,72`, `75,00`, `125,00`: **zero ocorrências** nos arquivos v8. O termo "LACRADO" aparece só neste registro, como referência ao nome da pasta de gabaritos; nenhuma ocorrência em peça, conta ou tabela.
- Os cinco arquivos existem em `entrega/v8/`.

## 4. Resultado

Há tentações registradas (itens 1.2, 1.3, 2.1 a 2.4). Nenhuma soma de 25 m² por vaga como área de garagem foi usada. A conclusão da alternativa B mudou e precisa de conferência primária. A sobra de M-a precisa de conferência de álgebra.
