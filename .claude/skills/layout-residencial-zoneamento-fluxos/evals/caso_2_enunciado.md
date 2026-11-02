# Avaliação 2 de 3 — "Casa do Mirante, Santa Teresa"

**Skills testadas:** `layout-residencial-zoneamento-fluxos` v1.3 e `layout-mobiliario-dimensoes-residencial` v1.1 (com `references/medidas_por_comodo.md`).
**Para:** Oscar · **Gestor:** Lúcio · **Montado por:** Bardi, 02/11/2026 · **Frente:** Construção do Zero.
**Tipo:** caso fictício de treino de Skill (`criando-skills-sttk`, seção 4). Não é o Ensaio 003 e não usa nenhum arquivo dele.

Leia também, quando o caso pedir: `arquitetura-nbr9050-acessibilidade`, `posicionamento-escada-residencial`, `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`, `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`, `partido-volumetria-residencial-contemporanea`. **Não use número de cabeça:** toda medida sai de uma Skill, ou fica marcada "interpretação — Gate".

## 1. Terreno (fictício — valores do treino, não confira na lei)

- Bairro: Santa Teresa, Rio de Janeiro. Rua fictícia "Ladeira do Mirante, 40".
- Lote retangular **15,00 m (frente) × 32,00 m (fundo)**. Rua ao **sul**, no alto; o terreno **desce** para os fundos, ao **norte**. Laterais: leste e oeste.
- **Vista da Baía de Guanabara nos fundos**, para o norte, abaixo do nível da rua.
- **Levantamento topográfico (medido), cotas no eixo do lote**, a partir da divisa da frente:

| Distância da frente | 0 (calçada) | 5,00 m | 12,00 m | 20,00 m | 29,00 m | 32,00 m (divisa de fundos) |
|---|---|---|---|---|---|---|
| Cota | 100,00 | 99,40 | 97,90 | 95,50 | 92,20 | 91,00 |

- **Folheto do corretor:** "terreno com desnível de cerca de 6 m, vista eterna".
- **Parâmetros do treino:** afastamento frontal 5,00 m; laterais 1,50 m; fundos 3,00 m; **TO 50%**; até 3 pavimentos. Vaga coberta não pode ficar no afastamento frontal. Rampa e escada descobertas de pedestre podem ficar no afastamento frontal.
- Piso a piso adotado: **3,00 m**.

## 2. Moradores e respostas do Briefing

- **Dona Célia**, 79 anos, usa cadeira de rodas desde um AVC em 2024. Cadeira manual hoje.
- **Mariana**, 52, filha, dentista. Dona do contrato.
- **Pedro**, 16, neto.
- Uma **cuidadora** trabalha das 8h às 18h. Não dorme na casa.

| Pergunta | Resposta escrita da Mariana |
|---|---|
| B1 — Quem mora e idade | Célia 79, Mariana 52, Pedro 16. |
| B2 — Dificuldade de locomoção | "Minha mãe usa cadeira de rodas. Eu tenho artrose no joelho e subo escada devagar." |
| B3 — Rotina em 10 anos | "Daqui a 10 anos quem vai precisar sou eu. Quero a casa toda pronta." |
| B4 — Prioridade do térreo | "A sala e o convívio, com a vista. Minha mãe precisa de um lugar plano no sol, todo dia." |
| B5 — Privacidade | "Quero meu quarto longe do da minha mãe, para ter sossego, mas perto para ouvir se ela chamar de noite." |
| B6 — Carros, compras, entrada suja | "Dois carros: o meu, que é nele que levo minha mãe, e o do Pedro daqui a 2 anos. Compras pela garagem." |
| NIV-01 — Padrão da obra | **Alto padrão.** |
| B8 — Como gosta da casa | "Tanto faz a sala embaixo ou em cima, desde que veja a baía." |

Outras frases:
- Dona Célia: "Não quero banheiro de hospital, cheio de barra."
- Mariana: "O fisioterapeuta disse que corredor de 1,00 m basta para a cadeira."
- Mariana: "Elevador não, que quebra e é caro. Mas, se for o único jeito, me mostra."
- Mariana: "O médico falou em trocar a cadeira da minha mãe por uma motorizada no ano que vem." (Modelo e medidas: não informados.)
- Dona Célia: "Durmo em cama de casal, não abro mão." (Tamanho: não informado.)

## 3. Programa

Garagem para 2 carros; hall de entrada; estar, jantar e cozinha integrados, com a vista; lavabo; lavanderia; suíte da Dona Célia; suíte da Mariana; quarto do Pedro com banheiro; apoio da cuidadora (onde ela guarda as coisas e se troca); lugar externo plano e com sol para a Dona Célia; jardim nos fundos. Área construída: **entre 260 e 320 m²**.

## 4. O que entregar

Pasta de trabalho: `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/treino_layout_mobiliario_v1_3/caso_2/` (arquivo próprio `caso2_mirante.rvt`; cópias de partido `caso2_mirante_partidoA.rvt` etc.). Nunca abra nem altere arquivo do Ensaio 003.

1. **Passo 1 — Lote e lei, escrito:** área, envelope, TO e qual limite vale; desnível adotado e de onde veio; onde estão a vista, o norte e o sol bom. Divergências entre documentos, com dono.
2. **Passo 2 — Programa:** tabela com cada ambiente, área-alvo, faixa de medidas e fonte, nível (cota), e a soma comparada com a área possível. Diga, por escrito, o que as respostas B1, B2 e B3 acionam na Skill e o que muda em cada pavimento.
3. **Zoneamento escrito** por nível, com os fluxos: Dona Célia (do carro até a cama, a cozinha, a sala e o lugar de sol), Mariana, Pedro, visita, cuidadora e compras.
4. **Partidos:** 2 ou 3, com imagem das plantas (aberta com Read), fluxos, `conferir_layout`, prós e contras e casos de uso da seção 4-ter aplicados. Escolha um e modele por inteiro.
5. **Planta do escolhido**, com mobília (camas, armários, sofá, mesa, bancadas, louças), portas com giro, janelas, cotas e etiquetas legíveis. Mostre o círculo de giro da cadeira onde ele for exigido.
6. **Relatório `relatorio_caso2.md`:** por cômodo, a faixa usada e as medidas conferidas (com a fonte da Skill); tabela dos corredores do caminho da Dona Célia (comprimento e largura); a conta da rampa, se houver; a conta de cada janela; cada aviso do `conferir_layout` com resposta; o que ficou "a confirmar" e com quem; o que invalidaria o partido escolhido; ordem de modelagem; e o que você **não** conseguiu fazer.
7. **Uma mensagem curta para a Mariana** (até 10 linhas) explicando a escolha entre os partidos e respondendo às frases do item 2.

Prazo: uma sessão. Dúvida de regra: pergunte ao Lúcio, não ao Bardi.
