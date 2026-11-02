# Avaliação 1 de 3 — "Casa Estreita da Tijuca"

**Skills testadas:** `layout-residencial-zoneamento-fluxos` v1.3 e `layout-mobiliario-dimensoes-residencial` v1.1 (com `references/medidas_por_comodo.md`).
**Para:** Oscar · **Gestor:** Lúcio · **Montado por:** Bardi, 02/11/2026 · **Frente:** Construção do Zero.
**Tipo:** caso fictício de treino de Skill (`criando-skills-sttk`, seção 4). Não é o Ensaio 003 e não usa nenhum arquivo dele.

Leia também, quando o caso pedir: `posicionamento-escada-residencial`, `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`, `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`, `partido-volumetria-residencial-contemporanea`. **Não use número de cabeça:** toda medida sai de uma Skill, ou fica marcada "interpretação — Gate".

## 1. Terreno (fictício — valores do treino, não confira na lei)

- Bairro: Tijuca, Rio de Janeiro. Rua fictícia "Rua das Acácias, 118".
- **Levantamento topográfico (medido):** testada (frente) **5,48 m**; fundos **5,52 m**; as duas laterais com **34,00 m**. Terreno plano.
- **Planta do IPTU (documento da prefeitura, que o cliente trouxe):** testada **5,60 m** × 34,00 m.
- Rua a **oeste** (a frente olha para o poente); fundos a **leste**. Divisa **norte** e divisa **sul** com vizinhos encostados.
- Vizinho ao **norte**: sobrado "de uns 3 andares", encostado na divisa em quase todo o comprimento. Altura não medida.
- Vizinho ao **sul**: casa de 2 pavimentos, encostada na divisa.
- **Parâmetros do treino:** afastamento frontal 3,00 m; fundos 3,00 m; laterais 0 (pode encostar nas duas divisas); **TO 70%**; até **3 pavimentos**; altura máxima 11,00 m.
- Cada parede de divisa da casa nova tem **0,20 m** de espessura (paredes próprias, não se apoia no vizinho).
- Piso a piso adotado: **3,00 m** em todos os pavimentos.

## 2. Moradores e respostas do Briefing

Casal: Rafael (41, engenheiro) e Luísa (39, professora de música, dá aula em casa duas tardes por semana). Filhos: Tom (9) e Bia (5). Um cachorro grande. Bicicletas da família inteira.

| Pergunta | Resposta escrita do cliente |
|---|---|
| B1 — Quem mora e idade | Rafael 41, Luísa 39, Tom 9, Bia 5. |
| B2 — Dificuldade de locomoção | "Não, ninguém." |
| B3 — Rotina em 10 anos | "Nunca pensamos. Talvez a mãe do Rafael venha morar com a gente um dia." |
| B4 — Prioridade do térreo | "A sala e o convívio. Não queremos piscina, só um jardinzinho para o cachorro." |
| B5 — Privacidade do casal | "Queremos um andar só nosso, longe da bagunça das crianças." |
| B6 — Carros, compras, entrada suja | "Um carro. Compras chegam de carro. O cachorro volta do passeio sujo de lama e as bicicletas ficam na garagem." |
| NIV-01 — Padrão da obra | **Alto padrão.** |
| B8 — Como gosta da casa | "Social embaixo, tudo integrado, sala clara." |

Outras frases da reunião:
- "Vimos que o vizinho fez um poço de luz de 1,00 m no meio da casa e a prefeitura aprovou. Faz igual, que sobra mais casa."
- "A TV é de 75 polegadas e não abro mão do sofá de 3 lugares com chaise."
- "Mesa de jantar de 8 lugares: a família dela é grande."
- "Cama king no nosso quarto." (Modelo do colchão: não informado.)
- "A Luísa precisa de um lugar para dar aula de piano sem atravessar a casa com o aluno."

## 3. Programa

Garagem para 1 carro (com as bicicletas); hall de entrada; estar, jantar e cozinha integrados; lavabo; lavanderia; sala de aula de música (piano de armário, 2 cadeiras); suíte do casal com closet; 2 quartos de criança; banheiro das crianças; jardim nos fundos. Área construída: **entre 240 e 290 m²** (o cliente aceita o que couber nessa faixa).

## 4. O que entregar

Pasta de trabalho: `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/treino_layout_mobiliario_v1_3/caso_1/` (arquivo próprio `caso1_tijuca.rvt`; cópias de partido `caso1_tijuca_partidoA.rvt` etc.). Nunca abra nem altere arquivo do Ensaio 003.

1. **Passo 1 — Lote e lei, escrito:** dimensões e área do lote que você adotou (e por quê), envelope, TO e qual dos dois limites vale. Divergências entre documentos, com dono.
2. **Passo 2 — Programa:** tabela com cada ambiente, área-alvo, faixa de medidas usada (e de onde ela vem), pavimento, e a soma comparada com a área possível.
3. **Zoneamento escrito** por pavimento, com os fluxos de visita, morador, serviço e aluno de música.
4. **Partidos:** 2 ou 3 partidos de verdade, cada um com imagem das plantas (aberta com Read), fluxos, `conferir_layout`, prós e contras, casos de uso da seção 4-ter aplicados (e o motivo de cada obrigatório ou padrão não aplicado). Escolha um e modele por inteiro.
5. **Planta do escolhido**, com mobília (sofá com chaise, rack da TV, mesa de 8, bancadas, cama king, armários, louças, piano), portas com giro, janelas, cotas e etiquetas legíveis.
6. **Relatório `relatorio_caso1.md`:** por cômodo, a faixa usada e as medidas conferidas (com a fonte da Skill); conta de cada janela; cada aviso do `conferir_layout` com resposta; o que ficou "a confirmar" e com quem; ordem de modelagem; e o que você **não** conseguiu fazer.

Prazo: uma sessão. Dúvida de regra: pergunte ao Lúcio, não ao Bardi.
