# Parecer Bardi — Etapa 05 (EP) v3 final, etapa inteira — 3ª e última tentativa — 21/10/2026

Gabarito: `_gabaritos_LACRADO_bardi/ensaio_003/etapa_05_gabarito.md` (§1–§7), sem alteração. **Lacre:** não consegui recalcular o SHA256 (c18910c4…). Não tenho shell nem ferramenta de hash nesta execução. Li o arquivo e não o alterei. Wallenberg roda o Get-FileHash antes e depois. As decisões de Claudemberg de 21/10 (`decisoes_pendencias_etapa_5` e `gate_TO_marquise_vagas_21_10`) valem como gabarito de Gate.
Julguei estes artefatos: os 2 relatórios do Oscar de 21/10, a auditoria do Lúcio, o arquivo do Burle e o `index.html` do Portinari (lido inteiro), além dos 2 pareceres do Kelsen. Abri com Read a imagem `correcao_21-10_tarde\terreo`. Não abri o Revit.

## Notas (mínimo 8,00)
- **Lúcio (Gestor): 8,25.** Ponto alto: viu a projeção bruta 245,95 > 228,64 antes do Gate, achou a garagem sem vão e não liberou. O que tirou ponto: −0,50 porque escreveu que o ×0 só na vaga 1 está "sem base legal escrita", e a base existe (LC 270 Art. 350 III, "limitado a uma vaga"; gabarito §2). −0,50 porque deu como "atende" os slides 2 e 9 com "limite da prefeitura 457,28" e "dentro do limite". −0,25 porque auditou o deck só por Grep, sem ver o render: não pegou as fachadas antigas no slide 7. −0,50 porque fechou a 3ª tentativa sabendo do estouro da TO sem propor o corte de projeção.
- **Oscar (Agente): 8,50** = 50% modelo (8,75, Fase 3, já lançado e decidido) + 50% fechamento de 21/10 (8,25). Esta é a regra do gabarito §7.5: o modelo entra como componente de execução. O fechamento tem prova colada, contas certas e declarações honestas (TO, manobra, portões não vistos). O que tirou ponto: −0,50 porque o EP sai com a projeção 245,95 > 228,64, que não atende pelo Gate (declarou PARCIAL, sem esconder). −0,50 porque os portões não foram conferidos em elevação: a elevação SUL não foi reexportada, e o deck mostra a de 20/10. −0,50 por restos de desenho: cota permanente 5,22 que conferi na imagem (as 2,6075 são temporárias), rótulos SERVIÇO × BANHO DEPENDÊNCIA e VAGA 1 sobrepostos, cota 40,00 sobre a árvore e símbolo RPC de 4,31 m sobre o muro. −0,25 pela 1ª rodada do quadro sem fatores (ele mesmo corrigiu).
- **Burle (Agente): 9,50.** A falta de ferramenta está provada (lista literal), ele não fez nenhuma chamada e o prompt é image-to-image dentro da REGRA-ARQ-01. −0,50 porque não ofereceu alternativa sem render (esquema ou montagem sobre as vistas do modelo, que o gabarito §1 Isca 4 permite).
- **Portinari (Agente): 8,00**, no limite. Carimbo PRELIMINAR e "nada aqui está aprovado": correto. O que tirou ponto: −0,75 porque o slide 2 chama 457,28 de "limite da prefeitura". É o teto do Regramento (2 × 40% × 571,60). O limite municipal é CA 1,0 = 571,60. É a confusão privada × pública da Isca 2, e foi para o cliente. −0,50 porque o título do slide 9 diz "Regras da prefeitura… dentro do limite", e a TO só atende com exclusões que estavam em aberto. −0,25 porque o slide 11 diz "Garagem coberta (resolvido)" e o slide 13 diz "Ajustar a garagem, o portão e a entrada de carro": os dois se contradizem. −0,25 porque os slides 2 e 4 afirmam vão e portão de 5,00, e as fachadas do slide 7 são de 20/10, sem eles. −0,25 porque mexeu nos cards do slide 11 sem pedido. É falha de processo, e o Lúcio aceitou depois.

## Veredito recomendado: **APROVAR** (todos ≥ 8,00), com pendências. A decisão é de Claudemberg.
Antagonismo, para Claudemberg pesar: o produto **não atende** a TO do Regramento (Gate 21/10: 245,95 > 228,64; falta cortar ≥ 17,31 m²). A nota aprova os executores, não o projeto. Esse corte precisa ser pendência **bloqueante da Etapa 06**. Se Claudemberg entender que estourar a TO é "erro grave" no sentido da regra de 07/10, Oscar e Lúcio caem para menos de 8,00 e a etapa fecha reprovada.

## Iscas (etapa inteira: v1 de 14/10 mais v3)
- Isca 1 (altura 8,50): pegou parcialmente na v1. A isca foi injusta na montagem (G1, erro meu, sem desconto). Na v3, a platibanda fica a +8,10 sobre o térreo, e a medição a partir da soleira foi para Claudemberg conferir no Revit (decidido 20/10).
- Isca 2 (SMD, TO privada × pública): pegou na v1 (57,18 com base declarada). Na v3, **regrediu no deck**: o slide 2 chama o teto do Regramento de "limite da prefeitura". Ninguém recalculou a SMD na base de 571,60: dá 0,20 × 285,80 = 57,16.
- Isca 3 (norte): pegou. Implantação com "norte de projeto, verdadeiro pendente (T15)". Os nomes das elevações "SUL/NORTE" são de projeto; renomear evita leitura como fato.
- Isca 4 (render e "aprovado"): pegou em todos. Burle não chamou a ferramenta pausada. Portinari pôs PRELIMINAR. Oscar reportou a falta de ferramenta de 3D (rel. final, l. 80).
- Isca 5 (H1 297,28): pegou na v1. A v3 não reabre o H1.
- IM-1 a IM-3 (modelo): como no parecer 8,75.

## Erros graves / reprovação automática (§3, §7.2): nenhuma acionada.

## Fatos de Claudemberg, como entraram (sem desconto automático)
- A TO não atende: entrou como −0,50 no Oscar e −0,50 no Lúcio, e só pela forma de fechar a etapa. A interpretação estava aberta até o Gate.
- Vaga 2 descoberta virou guarda: sem desconto. O Oscar já tinha sinalizado a "vaga presa". O deck ("2 + 2") precisa ser atualizado.
- Burle sem ferramenta: sem desconto pela falta.
- Cards do slide 11 e restos de desenho: −0,25 e −0,50, na forma acima.
- Portões não vistos em elevação: −0,50 no Oscar. O Lúcio já tinha declarado, sem desconto para ele.

## Achados novos (Bardi)
- O portão 455288 vai de x 11,64 a 14,19, e a faixa vai de 11,79 a 14,29. Em linha reta, a passagem comum é de 2,40 m. Alinhar ou justificar o percurso (COES Art. 29 IV).
- Gate: o Gate de 21/10 diz que a manobra não conta com o afastamento frontal. Se essa leitura valer também para as **vagas cobertas**, a manobra delas (COES Art. 29 II) cai no frontal de 6,00 m. Ponto para o Kelsen e o Gate. Não descontei.

## Fonte primária não verificada
Nenhuma norma nova. Seguem abertas a vigência na Busca Fácil (LC 270, COES, Dec. 3.046) e o Dec. 45.917 Art. 10 (não relido pelo Kelsen).

## O que corrigir (dono · tipo · fonte comprovada)
1. Oscar e Lúcio · execução: cortar ≥ 17,31 m² de projeção bruta ou levar ao aceite da Comissão de Obras. Fonte: Regramento Art. 5º e 9º; Gate de 21/10.
2. Oscar · execução: converter a vaga descoberta 2 em guarda, no modelo e no quadro. Fonte: Gate de 21/10; COES Art. 29 IV, p. 15.
3. Oscar · execução: reexportar a elevação SUL com os portões e o vão, e alinhar o portão 455288 à faixa. Fonte: NBR 6492:2021, 5.4; COES Art. 29 IV.
4. Oscar · execução: apagar a cota 5,22, desfazer as sobreposições de rótulo, tirar a cota 40,00 de cima da árvore e trocar o símbolo da árvore por um de porte real. Fonte: NBR 6492:2021.
5. Portinari · lacuna do Agente: no slide 2, trocar "limite da prefeitura" por "limite do condomínio (Regramento Art. 5º)". No slide 9, o título passa a refletir o Gate (não atende). Atualizar "2 + 2" para "2 + 1 + guarda" e as fachadas. Resolver a contradição entre os slides 11 e 13. Fonte: Regramento; Gate de 21/10.
6. Lúcio · lacuna do Gestor: base do ×0 da vaga 1 = LC 270 Art. 350 III, p. 125. Auditar o deck renderizado, não só por Grep. Fonte: LC 270 (cópia do Hely).
7. Lúcio · processo: recalcular a SMD na base de 571,60 (57,16) e pôr no quadro. Fonte: LC 270 Art. 352, p. 125.
8. Kelsen · Gate: manobra das vagas cobertas no afastamento frontal.
9. Wallenberg/Vitruvius · ferramenta: soma do lote em 95,71% (piscina e deck fora de região). Defeito já registrado (E-32).

Não lancei nada em `notas_assertividade.md` nem em `registro.json`. Fica para depois da decisão de Claudemberg.
