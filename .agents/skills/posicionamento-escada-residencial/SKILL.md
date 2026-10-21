---
name: posicionamento-escada-residencial
description: Onde e como posicionar a escada numa casa de 2 pavimentos para que a circulação funcione — partida e chegada em área de circulação com saída, espaço livre para pisar antes do 1º degrau e depois do último, projeção da escada no superior dentro da circulação, escolha entre reta/L/U pelo formato do espaço, e o passo obrigatório de comparar 2 ou 3 posições com prós e contras antes de desenhar. Use SEMPRE que o Oscar (ou Lúcio, ou qualquer Agente) for propor, desenhar, mover ou conferir uma escada interna, montar o layout do Estudo Preliminar ou do Anteprojeto de casa com mais de um pavimento, ou chamar a ferramenta criar_escada — mesmo que o pedido só diga "escada", "acesso ao superior", "circulação", "hall" ou "layout do térreo".
version: v1.1
status: proposta-em-treino
data: 2026-10-19
origem: "Sabatina Wallenberg × Claudemberg, 19/10/2026: a 1ª escada do Vitruvius (EP_diagnostico_19-10.rvt) começava e terminava de frente para parede (13 cm livres). Pesquisa de Wallenberg em 19/10/2026 (fontes na seção 6)."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar
agentes_cross: Tenreiro (escada personalizada), Burle (vista da escada no render)
validacao: pendente — treino no caso fictício EP_diagnostico_19-10.rvt (Ensaio 003) e aprovação de Claudemberg
---

# Skill: Posicionamento da escada residencial

> **RESSALVA:** prática de projeto reunida de arquitetos e guias de construção (seção 6), não norma brasileira. As medidas de área livre (seção 3) são decisão de Claudemberg (19/10/2026) para o escritório. Regra legal (COES, NBR 9050) prevalece onde existir; o COES LC 198/2019 Art. 21 (2,20 m livre, corrimão dos dois lados, até 16 degraus por lance) trata de **escada de uso comum**, não de escada interna de casa unifamiliar.

## 1. Por que existe

Em 19/10/2026 a 1ª escada criada pela ferramenta `criar_escada` cabia no ambiente, mas não funcionava: na escada em U a partida e a chegada ficam do mesmo lado, e esse lado estava a 13 cm de uma parede. No térreo não havia onde pisar antes de subir; no superior a pessoa chegava de frente para a parede do Home Cinema. **Caber não é funcionar.**

## 2. Regras de posição (o que um arquiteto experiente faz)

1. **Começa e termina em área comum.** A escada nasce num hall, circulação ou estar, e chega numa circulação do superior que distribui para os quartos. Nunca dentro de um cômodo (quarto, cozinha fechada, serviço). (Fonte F1, F3.)
2. **Decida a escada cedo.** A escada principal organiza a planta tanto quanto o estilo; posicione-a junto com a circulação, não no espaço que sobrou. (F3.)
3. **Une, não isola.** A escada deve ligar os ambientes sem dividi-los nem obstruir a passagem entre o social e o serviço. Escada mal posta gera corredor estranho e comprido. (F3.)
4. **Central elimina corredor.** Escada no meio da casa, com os quartos em volta da chegada, dispensa corredor longo no superior. Em lote estreito e comprido (como o Ensaio 003), escada central costuma resolver melhor que escada no fundo. (F1, F4.)
5. **Entrada × privacidade.** Perto da entrada facilita chegar e sair; vista de frente da porta expõe quem desce de pijama. Equilíbrio: perto do hall, mas não de frente para a porta da rua. (F1.)
6. **Mesmo lugar em todos os pavimentos.** Partida e chegada empilhadas no mesmo núcleo de circulação; a projeção da escada (o vão) no superior fica **inteira dentro da circulação**, sem invadir quarto. (F4.)
7. **Nenhuma porta abre sobre degrau** nem dentro das áreas livres de partida e chegada. (F2, exceção do IRC para porta sobre escada.)
8. **Formato pelo espaço disponível:** reta para planta estreita e longa; **L** em canto de parede (libera o espaço embaixo); **U** exige mais largura (patamar dos dois lances) e põe partida e chegada **do mesmo lado** — reserve área livre desse lado nos dois pavimentos. (F5.)
9. **Aproveite o vão de baixo** (lavabo, depósito, adega, armário) e pense na luz natural da escada.
10. **No máximo 10 espelhos seguidos por lance; depois, patamar** (decidido por Claudemberg em 19/10/2026; F6). Com piso a piso de 3,15 m são 18 espelhos: a escada reta não serve, use L ou U. A ferramenta recusa lance com mais de 10. (COES Art. 21 III fala em 16, mas para escada de uso comum.)
11. **A conta é de piso a piso** (o "pé-esquerdo", de laje a laje), nunca pelo pé-direito até o forro (F6). A `criar_escada` já calcula pela diferença entre os níveis.
12. **A escada "morde a laje":** o último degrau é a própria laje de cima, sem sobra de centímetros antes dela; **a partida começa por um espelho** a partir do piso de baixo (F6). Confira as duas coisas na imagem do corte.

## 2-bis. Integrar é o padrão — vale para todos os cômodos (decidido por Claudemberg em 19/10/2026)

Projeto contemporâneo trabalha com espaços integrados, grandes vãos e fluxos conectados. **Entre dois ambientes, o padrão é vão livre** (`criar_abertura_parede`), com largura e altura decididas pelo projeto, pelo programa do cliente e pelo partido. **Porta só com motivo escrito:** privacidade (quartos, banheiros, lavabo), acústica (home cinema, escritório), ar-condicionado, segurança, cheiro (cozinha fechada). Porta sem motivo escrito = erro.

## 3. Áreas livres de partida e chegada (decisão de Claudemberg, 19/10/2026)

- **Antes do 1º degrau (pavimento de baixo)** e **depois do último (pavimento de cima):** área livre com **a largura da escada × 1,20 m** de profundidade, no sentido de quem anda. Pode ser maior, nunca menor. (Referência internacional: o IRC dos EUA exige patamar no topo e na base com a largura da escada e 0,914 m de profundidade, F2; o escritório adota 1,20 m.)
- **Nada invade essa área:** parede, guarda-corpo, porta abrindo, o próprio vão da escada.
- **Essa área leva a algum lugar:** fica dentro de um ambiente de circulação (hall, corredor, estar, circulação) que tem porta ou passagem para outros ambientes. Canto fechado sem saída = escada errada.
- A ferramenta `criar_escada` confere tudo isso e recusa (desfaz) se falhar.

## 4. Passo obrigatório antes de desenhar

1. Leia as plantas dos dois pavimentos (`list_elements` de paredes com `location`, de ambientes e de portas).
2. Escreva **2 ou 3 posições possíveis**, cada uma com: formato (reta/L/U), onde começa, onde chega, área livre de partida e de chegada (medida), o que fica embaixo, prós e contras pelas regras da seção 2.
3. Escolha uma e escreva **o motivo** em uma frase.
4. Se nenhuma posição funciona sem mexer no layout, proponha o ajuste mínimo da circulação (mover uma parede ou porta) com o motivo; registre cada mudança.
5. Só então chame `criar_escada`. Recusou? Leia o motivo, volte ao passo 2. **Não contorne** desligando conferência.
6. Prova: imagem da planta dos dois pavimentos e de um corte pela escada; diga, olhando a imagem, por onde a pessoa chega e para onde vai.

## 5. Erros já cometidos

| Data | Erro | Correção |
|---|---|---|
| 19/10/2026 | Escada em U com partida e chegada a 13 cm da parede (Wallenberg, teste da ferramenta) | Seção 3; conferência na ferramenta |
| 19/10/2026 | 1º treino (Oscar, escada 450364): escada passou na ferramenta, mas a circulação do térreo não tem passagem para o Estar (parede 449338 cheia) — fere a regra 3 | Antes de chamar `criar_escada`, conferir a ligação da circulação de partida com o social; a ferramenta não confere isso |
| 19/10/2026 | Ferramenta recusava a chegada por causa da folga de 5 cm do vão (falso positivo); Oscar zerou `folgaVao` | Corrigido no plugin v61: a chegada confere contra a pegada da escada, sem a folga. Não zerar `folgaVao` |

## 6. Fontes

- **F1** — Green Building Advisor, "Where to locate stairs in a new build": https://www.greenbuildingadvisor.com/question/where-to-locate-stairs-in-a-new-build ; Pro Builder, "Staircases step back": https://www.probuilder.com/staircases-step-back
- **F2** — International Residential Code R311.7.6 (landings: topo e base, largura da escada, 36 in = 914 mm), resumo em guias municipais: https://www.placer.ca.gov/DocumentCenter/View/3303/Residential-Stairs-PDF
- **F3** — Fine Homebuilding, "Staircase Design" (Caleb Johnson, Gil Schafer): https://finehomebuilding.com/2018/07/04/staircase-design
- **F4** — BUILD LLC, "the sensibility of circulation volumes": https://blog.buildllc.com/2015/08/the-sensibility-of-circulation-volumes/ ; ArchDaily, STV House (Arstudio): escada no núcleo dividindo quartos dos filhos e suíte do casal.
- **F5** — Olhar Digital, tipos de escada (reta, L, U, helicoidal) e quando usar.
- **F6** — Reel no Instagram, "Parte 01 - Vou te ensinar sobre ESCADAS" (arquiteto treinando a própria equipe, sem citar norma): https://www.instagram.com/reels/Der2YJAJ3c9/ — assistido em 19/10/2026 via /watch (Gemini). Pontos aproveitados: piso a piso, "morde a laje", partida pelo espelho, até 10 degraus por lance. Adotados como regra do escritório por decisão de Claudemberg, não como norma.
- Pendente de aprofundar: Neufert (Arte de Projetar em Arquitetura), capítulo de escadas; Christopher Alexander, *A Pattern Language* (padrão "Staircase as a Stage", número a confirmar no livro).
