# Avaliação 3 de 3 — "Casa da Família Rocha, Campo Grande"

**Skills testadas:** `layout-residencial-zoneamento-fluxos` v1.3 e `layout-mobiliario-dimensoes-residencial` v1.1 (com `references/medidas_por_comodo.md`).
**Para:** Oscar · **Gestor:** Lúcio · **Montado por:** Bardi, 02/11/2026 · **Frente:** Construção do Zero.
**Tipo:** caso fictício de treino de Skill (`criando-skills-sttk`, seção 4). Não é o Ensaio 003 e não usa nenhum arquivo dele.

Leia também, quando o caso pedir: `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`, `posicionamento-escada-residencial`, `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`, `arquitetura-nbr9050-acessibilidade`, e o modelo do Briefing Único v2 (`CONSTRUCAO_DO_ZERO/01_CEO/Gestores/Lúcio (Arquitetura)/Agentes/Oscar/briefing_modelo_v2_proposta.md`). **Não use número de cabeça:** toda medida sai de uma Skill, ou fica marcada "interpretação — Gate".

## 1. Terreno (fictício — valores do treino, não confira na lei)

- Bairro: Campo Grande, Rio de Janeiro. Rua fictícia "Rua Projetada 7, lote 14".
- Lote retangular **10,00 m (frente) × 20,00 m (fundo)**, plano. Rua a **leste**; fundos a **oeste**. Laterais: **norte** e **sul**.
- **Parâmetros do treino:** afastamento frontal 5,00 m; fundos 2,00 m; lateral norte 1,50 m; lateral sul 0 (pode encostar na divisa); **TO 60%**; até 2 pavimentos. A vaga descoberta pode ficar no afastamento frontal.
- Vizinho ao sul: casa encostada na divisa. Vizinho ao norte: quintal.
- Piso a piso adotado: **2,90 m**.

## 2. Moradores e respostas do Briefing

Diego (35, motorista de aplicativo) e Jéssica (33, cabeleireira). Filhos: Kauã (8), Lara (6) e Miguel (2). A mãe da Jéssica, **Dona Ivone (71)**, mora com eles de março a agosto e hoje dorme no sofá-cama do escritório.

**Histórico do Briefing:**
- Versão 1, com DEC-01 assinada em 20/10/2026: NIV-01 = **Médio padrão**.
- Versão 2, com DEC-01 assinada em 28/10/2026: NIV-01 = **Econômico**. É a versão vigente das respostas abaixo.

| Pergunta | Resposta (versão 2) |
|---|---|
| B1 — Quem mora e idade | "Diego 35, Jéssica 33, Kauã 8, Lara 6, Miguel 2. Minha mãe, Ivone, 71, fica com a gente de março a agosto." |
| B2 — Dificuldade de locomoção | "Hoje ninguém." |
| B3 — Rotina em 10 anos | "Não sei. Quero gastar pouco agora." |
| B4 — Prioridade do térreo | "Convívio. Uma churrasqueira pequena nos fundos." |
| B5 — Privacidade | "Suíte junto dos quartos das crianças, o Miguel ainda é pequeno." |
| B6 — Carros, compras | "Um carro, que é o meu trabalho. Compras de carro." |
| NIV-01 — Padrão da obra | **Econômico.** |
| B8 — Como gosta da casa | "Social embaixo, cozinha aberta." |

**E-mail recebido em 01/11/2026, assinado pelos dois:**

> Arquiteto, pensamos melhor. O dinheiro só dá para uns 120 m² de casa (o pedreiro disse que sai a R$ 3.000 o m²). Então queremos tudo no mínimo da norma, para caber 4 quartos lá em cima:
> 1. corredor de 70 cm;
> 2. box de 70 × 70 nos banheiros;
> 3. pé-direito de 2,40 m em tudo, que economiza na escada e no reboco;
> 4. banheiro sem janela, e janela pequena nos quartos, que a lei de casa não exige;
> 5. o quarto do Miguel pode ser sem janela, a gente põe um ar-condicionado;
> 6. tira o escritório lá de baixo, não precisamos; minha mãe dorme no quarto do Miguel quando vier.
> Pode fazer, a gente assina o que precisar.

## 3. Programa

No superior: suíte do casal e **3 quartos** de criança, banheiro das crianças. No térreo: estar, jantar e cozinha integrados; lavabo; área de serviço; churrasqueira pequena nos fundos; 1 vaga descoberta. Área construída: **até 120 m²** (limite dado pelo cliente).

## 4. O que entregar

Pasta de trabalho: `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/treino_layout_mobiliario_v1_3/caso_3/` (arquivo próprio `caso3_campogrande.rvt`; cópias de partido `caso3_campogrande_partidoA.rvt` etc.). Nunca abra nem altere arquivo do Ensaio 003.

1. **Passo 1 — Lote e lei, escrito:** área, envelope, TO e qual limite vale; onde pode e onde não pode ter janela.
2. **Faixa de medidas:** qual faixa você usa, de onde ela vem e o que muda com o e-mail.
3. **Tabela dos 6 pedidos do e-mail:** para cada um, o que a Skill diz, se é exigência obrigatória, referência não obrigatória ou ponto sem fonte; o que você faz no projeto; e o que depende de quem (cliente, Lúcio, Claudemberg).
4. **Passo 2 — Programa:** tabela com cada ambiente, área-alvo, faixa e fonte, pavimento, e a soma comparada com os 120 m² e com a área possível.
5. **Partidos:** 2 ou 3, com imagem das plantas (aberta com Read), fluxos, `conferir_layout`, prós e contras e casos de uso da seção 4-ter aplicados. Escolha um e modele por inteiro, com mobília, portas com giro, janelas, cotas e etiquetas legíveis.
6. **Relatório `relatorio_caso3.md`:** por cômodo, a faixa e as medidas conferidas (com a fonte da Skill); a conta de cada janela; cada aviso do `conferir_layout` com resposta; o que ficou "a confirmar" e com quem; o que invalidaria o partido escolhido; ordem de modelagem; e o que você **não** conseguiu fazer.
7. **Resposta ao e-mail** do Diego e da Jéssica (até 15 linhas, português simples), pronta para o Lúcio revisar. Não envie nada a ninguém.

Prazo: uma sessão. Dúvida de regra: pergunte ao Lúcio, não ao Bardi.
