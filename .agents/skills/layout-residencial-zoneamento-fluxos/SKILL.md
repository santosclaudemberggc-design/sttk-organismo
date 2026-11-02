---
name: layout-residencial-zoneamento-fluxos
description: Método de arquiteto para montar o layout de casa unifamiliar (sobrado ou térrea) — zoneamento social/serviço/íntimo, fluxos de visita, morador e serviço sem atravessar cômodo, entrada social pela frente, áreas molhadas empilhadas, orientação por sol e vento com ventilação cruzada, integração como padrão, casos de uso de partido (pátio em lote estreito, faixa fixa de escada e banheiros, suíte no térreo para idoso, cômodo térreo que vira suíte, social em cima, lote em declive, entrada de serviço), perguntas do Briefing que decidem o partido, e o passo obrigatório de 2 ou 3 partidos com imagem e prós/contras antes de modelar. Use SEMPRE que o Oscar (ou Lúcio, ou qualquer Agente) for montar, revisar, corrigir ou conferir a planta de uma casa no Estudo Preliminar ou Anteprojeto, distribuir o programa do Briefing nos pavimentos, ou rodar conferir_layout — mesmo que o pedido só diga "layout", "planta", "distribuir os ambientes", "partido", "sobrado" ou "refazer o térreo".
version: v1.3
status: proposta-em-treino
data: 2026-10-19
revisao_v1_3: "30/10/2026, sabatina Wallenberg × Claudemberg (rodadas 3-4): casos de uso de partido C1-C9 (seção 4-ter), bloco 'perguntas que decidem o partido' no Passo 2, medidas passam para a Skill layout-mobiliario-dimensoes-residencial. Vale depois do treino em caso fictício (Bardi) e do sim de Claudemberg."
revisao_v1_2: "27/10/2026, treino em caso fictício (Casa do Ipê, nota 7,83, parecer_bardi_treino.md): largura de corredor em unifamiliar (regra 7), ventilação cruzada lei × desejo (regra 9), folga da cozinha (13-14), conferência de área (Passo 2), boneca da porta (4-bis.2), mobília, frações do COES e planta com cotas (5-bis). Aprovado por Claudemberg na sabatina de 27/10; vale depois do 2º treino."
revisao_v1_1: "27/10/2026, sabatina Wallenberg × Claudemberg (rodadas 1-2): regras 13-14 (cozinha e mesa), seção 4-bis (portas), seção 5-bis (ordem de modelagem: paredes → vãos → esquadrias), fontes F7-F8. Vale só depois do treino em caso fictício e do sim de Claudemberg."
origem: "Sabatina Wallenberg × Claudemberg, 19/10/2026: o layout do EP_diagnostico_19-10.rvt foi feito em faixas retangulares sem método (sem entrada social, garagem e serviço sem porta, suíte idosa acessada pela cozinha, nenhum banheiro, suítes acessadas por dentro de outro cômodo, sem ventilação cruzada). Roteiro de 5 passos de Claudemberg + pesquisa de Wallenberg (fontes na seção 8)."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar
agentes_cross: Kelsen/Hely (parâmetros do lote), Saturnino (prumadas), Tenreiro (mobiliário), Villaça (programa × área)
skills_relacionadas: layout-mobiliario-dimensoes-residencial, posicionamento-escada-residencial, coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj, arquitetura-nbr9050-acessibilidade, vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj, legal-base-legislativa-bairro
validacao: pendente — 3 casos fictícios do Bardi com gabarito (lote estreito encostado; 3 pavimentos para casal idoso; declive com vista nos fundos), nota mínima 8,00, avaliação visual e aprovação de Claudemberg. Não usa arquivos do Ensaio 003.
---

# Skill: Layout residencial — zoneamento e fluxos

> **RESSALVA:** método de projeto reunido do roteiro de Claudemberg e de fontes de ensino de arquitetura (seção 8). **Lei vem antes:** pé-direito, iluminação e ventilação pelo COES (Skill `coe-lc198-…`); acessibilidade pela NBR 9050 (Skill `arquitetura-nbr9050-…`); afastamentos, TO e gabarito pelo parecer Legal (Kelsen/Hely). Esta Skill não repete essas regras: ela diz **como organizar** a casa dentro delas.

## 1. Por que existe

Em 19/10/2026 o layout do caso de treino tinha a frente toda de garagem, entrada pela lateral, garagem e serviço sem porta, a suíte da idosa acessada pela cozinha, nenhum banheiro em 4 "suítes", duas suítes acessadas por dentro de outro cômodo, o Estar de 66 m² sem janela e nenhuma ventilação cruzada. **Desenhar cômodos não é projetar casa.**

> **[20/10/2026, decidido por Claudemberg] Esta Skill vem DEPOIS da `partido-volumetria-residencial-contemporanea`:** o layout é feito dentro da volumetria escolhida por Claudemberg, a partir do perfil da família escrito lá.

## 2. Passo 1 — Lote e lei (antes de qualquer traço)

Leia o parecer Legal e o Levantamento aprovados: afastamentos, envelope (área e forma), TO, CAB/CAM, gabarito, altura, cota de soleira, **onde fica a rua (frente)**, **norte verdadeiro**, ventos dominantes, topografia, árvores, divisas. Se o norte estiver pendente, escreva "norte pendente" e trate a orientação como hipótese com dono — não invente.

## 3. Passo 2 — Programa (Briefing)

Liste cada ambiente pedido com área-alvo, pavimento sugerido e exigência especial (ex.: suíte térrea para idosa → NBR 9050; home office com acesso independente?). Some e compare com a área possível (envelope × pavimentos). Não cabe? Registre e leve ao cliente — não corte por conta própria.

**Conferência de área [v1.3]:** cada área-alvo vem do briefing. Se o briefing não disser, use a faixa **conforto** da Skill `layout-mobiliario-dimensoes-residencial` (medidas com fonte: NBR 15575 Anexo F, Panero, Pronk, Neufert) e escreva a faixa usada. Em casa no Rio não há área mínima legal de cômodo (COES Art. 31); confira iluminação e ventilação pela Skill `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`.

### 3-bis. Perguntas que decidem o partido [v1.3]

O Briefing tem de responder, por escrito, antes do Passo 3. Pergunta sem resposta = volta ao cliente, não se adivinha. Cada pergunta diz que caso de uso da seção 4-ter ela aciona.

| # | Pergunta ao cliente | Aciona |
|---|---|---|
| B1 | Quem vai morar na casa e qual a idade de cada um? | C5, C8 |
| B2 | Alguém tem hoje dificuldade de locomoção, problema nas articulações ou orientação médica para evitar esforço? | C5 (obrigatória se sim), faixa acessível da Skill de medidas |
| B3 | Como imagina a rotina da família daqui a 10 anos? Quer a casa pronta para ficar acessível? | C8 |
| B4 | O que é prioridade no térreo: lazer (piscina, deck) ou a sala e o convívio? | C4 |
| B5 | Quanto de privacidade o casal quer: andar só para a suíte, ou suítes juntas? | C3 |
| B6 | Quantos carros? Como chegam as compras? Há pet ou entrada "suja" (praia, esporte)? | C9 |
| B7 | Que faixa de medidas: conforto (padrão) ou alto padrão? | Skill de medidas |
| B8 | Como gosta que a casa seja disposta (social embaixo ou em cima; integrada ou com portas)? | C4, regra 8 |

Lote estreito (C1), número de pavimentos (C2), declive e vista (C6) e luz em dois lados (C7) vêm do Levantamento e do parecer Legal, não do cliente.

## 4. Passo 3 — Zoneamento (escrito, antes de desenhar)

**Setores** (F2, F3): **social** (hall, estar, jantar, lavabo, varanda/gourmet), **serviço** (cozinha, lavanderia, despensa, dependência, garagem, depósito), **íntimo** (quartos, suítes, banheiros, closet, home office privado) e **circulação** (hall, escada, corredor).

Regras:
1. **Sobrado:** térreo = social + serviço (e o quarto de quem não pode usar escada); superior = íntimo (F2, F5, roteiro de Claudemberg).
2. **Gradiente do público ao privado:** quanto mais fundo/alto, mais privado. A visita chega ao social **sem passar pelo íntimo nem pelo serviço** (F1).
3. **Entrada social pela frente**, com hall; **entrada de serviço separada** (pela garagem ou lateral), ligada a lavanderia → cozinha.
4. **Nenhum cômodo de permanência prolongada é acessado por dentro de outro.** Exceção: banheiro e closet de suíte, varanda de quarto.
5. **Toda suíte tem banheiro;** térreo tem **lavabo** para visita.
6. **Áreas molhadas empilhadas e agrupadas:** banheiros do superior sobre banheiro/lavabo/cozinha/lavanderia do térreo; cozinha junto da lavanderia. Menos prumada, menos vazamento (roteiro; F6). Prumada de esgoto **nunca** atrás da cabeceira da cama (F6). Em 2+ pavimentos, ver C2 (faixa fixa com a escada).
7. **Circulação mínima:** corredor longo e "perdido" é área perdida; prefira hall distribuidor curto e circulação pela borda dos grupos de uso, não pelo meio (F1, F4). **Largura mínima [v1.2]:** em casa unifamiliar ou bifamiliar a NBR 9050 **não é obrigatória** — o COES (LC 198/2019) Art. 31 V dispensa (Skill `arquitetura-nbr9050-acessibilidade`). **[v1.3] Meta de projeto** pela NBR 9050:2020 (larguras mínimas de corredores, lida no acervo): **0,90 m** até 4,00 m de extensão; **1,20 m** até 10,00 m; **1,50 m** acima de 10,00 m. Abaixo disso, escreva no relatório "abaixo da NBR 9050, permitido pelo COES Art. 31 V" — nunca abaixo da faixa mínima da Skill `layout-mobiliario-dimensoes-residencial`. Se o Briefing (B1/B2) tiver morador com mobilidade reduzida, essas larguras passam a ser obrigatórias. Áreas comuns de condomínio de casas: Kelsen.
8. **Integrar é o padrão** (Skill de escada, seção 2-bis): estar, jantar e cozinha integrados ou ligados por vão livre; porta só com motivo escrito.
9. **Sol e vento:** no RJ, norte é o sol bom do inverno e oeste é o calor da tarde. Estar e quartos para o norte/leste quando possível; serviço, garagem e escada podem ir para o lado pior. **Ventilação cruzada:** janelas em paredes opostas ou adjacentes nos ambientes de permanência prolongada, principalmente no superior (roteiro). **[v1.2] Lei e desejo separados:** o que a lei exige é a janela com a área do COES (regra 10); a ventilação cruzada é **desejável, não exigência legal**. O aviso de ventilação cruzada do `conferir_layout` só conta janelas, não portas: quando o ar cruza por porta (ex.: porta de correr para a varanda), escreva "ventilação cruzada pela porta X" e marque "interpretação — Gate". Aviso sem resposta escrita é falha de entrega.
10. **Toda permanência prolongada tem janela** com a área do COES; banheiro sem janela só com exaustão (Skill COES).
11. **Escada:** siga `posicionamento-escada-residencial` (coração da casa, partida e chegada em circulação, sem cortar a luz dos cômodos principais, vão de baixo aproveitado).
12. **Fachada de frente não é só garagem:** a garagem divide a frente com o hall/entrada social e uma janela de ambiente.
13. **Cozinha que não cansa [v1.1]:** geladeira, pia e fogão próximos, com a pia entre o fogão e a bancada de preparo; a porta e a passagem ficam **fora** dessa área de trabalho — quem entra não cruza quem cozinha (F7, reel DeemZnYIt8H).
14. **Mesa de jantar fora do caminho [v1.1]:** a mesa não fica na linha de passagem cozinha ↔ estar ↔ varanda; ela vai para o lado e a passagem fica livre (F7, reel DdrL_ZhoyrP). **[v1.3] Folga (regras 13 e 14):** use a Skill `layout-mobiliario-dimensoes-residencial` — conforto: bancada até obstáculo 1,20 m (Pronk; Panero 1,22 m), livre a partir da borda da mesa 0,80 a 1,10 m (Neufert). Escreva a faixa usada. A ilha nunca encosta na mesa.
15. **Casa × quintal × piscina × garagem:** decididos na Skill de partido (regra 16); aqui só se confere que a piscina abre para varanda/estar e que a garagem tem porta para a entrada de serviço.

## 4-bis. Portas [v1.1, 27/10/2026]

Toda porta é desenhada com o **giro da folha** e conferida com a mobília no lugar.
1. **A folha abre encostando na parede mais próxima**, não para o meio do cômodo nem contra a circulação. Quem entra vê o cômodo, não a folha (F7, reel Dd9Vnd0IktW).
2. **Distância do canto:** o batente fica com uma "boneca" (trecho de parede) entre ele e a parede do canto, para a folha encostar e o interruptor caber. **[v1.2] A largura da boneca não tem medida em nenhuma fonte lida pelo organismo (27/10/2026):** use sempre a marca fixa "interpretação — Gate", escreva no relatório a medida usada e o motivo, e use a mesma medida em todas as portas do projeto. O vão livre da porta vem da Skill `arquitetura-nbr9050-acessibilidade` (0,80 m livre), lembrando a dispensa do COES Art. 31 V (seção 4, regra 7).
3. **Nada no giro:** cama, armário, bancada, vaso sanitário e outra porta ficam fora do arco de abertura. Porta de suíte não abre contra a cama nem esconde o closet (F7, Dd9Vnd0IktW: errado × certo).
4. **Porta não bate em porta:** duas portas próximas (hall de suítes, banheiro + closet) não podem ter os arcos cruzados; resolva invertendo o sentido, afastando os vãos ou trocando uma por porta de correr.
5. **Porta de correr** quando o arco atrapalha (banheiro pequeno, closet, cozinha) ou para integrar varanda e sala; precisa de parede livre ao lado do vão do tamanho da folha (F8, apartamento EV).
6. **Banheiro:** porta abre para dentro só se o arco não alcançar o vaso; senão, para fora ou de correr. Banheiro acessível: pela NBR 9050.
7. **Cozinha:** a porta não abre sobre a bancada nem sobre a área de trabalho (regra 13).
8. **Porta separando íntimo do social** (corredor dos quartos) quando ajuda o ar-condicionado e a privacidade — sem contrariar a regra 8 da seção 4 (integrar é o padrão no social) (F8).

## 4-ter. Casos de uso de partido [v1.3, aprovados por Claudemberg na sabatina de 30/10/2026]

Força: **obrigatória** (sempre que a condição existir), **padrão** (sempre que o lote permitir; se não der, motivo escrito), **opção comparada** (entra como um dos 2-3 partidos do Passo 4, ao lado da solução comum), **meta** (buscar; se não der, justificar no relatório).

**C1 — Pátio interno em lote estreito.** Força: padrão.
- Quando usar: frente até ~10 m, ou vizinhos encostados nas duas laterais, e o meio da casa não ventila só por frente e fundo.
- Regra: um pátio no meio divide a casa em dois blocos; a ligação entre eles (galeria, corredor) também se ilumina pelo pátio.
- Medida: mínimo legal **1,50 m** (COES, LC 198/2019, Art. 31, parágrafo único); recomendado **2,00 a 3,00 m**, crescendo com a altura das paredes em volta — marcar "interpretação — Gate".
- Atenção: o pátio vira bacia — prever drenagem e captação (Saturnino; Skill `nbr10844-1989-aguas-pluviais`) para não infiltrar na fundação do vizinho; cuidar da privacidade entre os blocos.
- Quando não usar: lote largo, com ventilação lateral possível.

**C2 — Faixa fixa de escada e áreas molhadas.** Força: obrigatória em 3+ pavimentos; padrão em 2.
- Regra: escada, banheiros e shafts numa faixa vertical única, empilhada do térreo ao topo. Amplia a regra 6.
- Quando não usar (2 pavimentos): lote ou programa que não comporte — motivo escrito.

**C3 — Suíte master sozinha no último andar.** Força: opção comparada.
- Quando usar: casal sem dificuldade de locomoção, casa de 3 pavimentos, B5 pedindo privacidade.
- Sempre junto com C8 (cômodo térreo pronto para virar suíte).
- Quando não usar: B1/B2 com idoso ou mobilidade reduzida → C5.

**C4 — Social em cima quando o lazer domina o térreo.** Força: opção comparada.
- Quando usar: B4 diz que o térreo é de piscina e lazer.
- Regra: estar e jantar sobem; banheiros continuam alinhados (C2).
- Conferir: como a visita chega lá em cima (escada de destaque, elevador, perto da entrada); se a sala não devassa vizinho nem a própria área de lazer; se ganha a melhor vista e orientação.
- Sempre comparada com "social embaixo".

**C5 — Suíte principal no térreo para morador idoso.** Força: obrigatória quando B1/B2 indicarem.
- Regra: suíte principal no térreo; o andar de cima fica para filhos e visitas.
- Sub-regra: piso **sem nenhum degrau** entre suíte, cozinha e convívio. Medidas: seção "Térreo acessível" da Skill de medidas (NBR 9050:2020 por escolha de projeto).

**C6 — Lote em declive.** Força: opção comparada; decide-se pela vista.
- Social no nível da rua: entrada de impacto; vista do horizonte na frente; quartos embaixo exigem cuidado com umidade, ventilação e sensação de porão.
- Invertida (íntimo na rua, social descendo): melhor quando a vista está nos fundos, abaixo; social sai direto para quintal, piscina e jardim; quartos na rua pegam melhor sol e ar.
- Sempre os dois partidos, com a posição da vista escrita.

**C7 — Luz em dois lados.** Força: meta.
- Regra: todo cômodo de permanência prolongada busca abertura em duas faces (ventilação cruzada, regra 9).
- Quando não der (parede cega na divisa): escreva no relatório e no memorial o motivo, ex.: "iluminação unilateral: parede na divisa oeste, onde o Código Civil, Art. 1.301, proíbe janela a menos de 1,50 m do vizinho", e mostre que a face única basta pela regra 10.

**C8 — Cômodo térreo que vira suíte.** Força: obrigatória em toda casa de 2+ pavimentos (bloco "térreo acessível", junto com C5).
- Regra: um cômodo do térreo (escritório, hóspedes) com banheiro ao lado ou anexo, porta de 0,90 m, box sem degrau e caimento pronto, pontos de água, esgoto e elétrica já previstos.
- Por quê: custa pouco na obra e muito para adaptar depois; serve a idoso, a quem se recupera de cirurgia e valoriza a casa.

**C9 — Entrada de serviço.** Força: padrão.
- Regra: garagem → entrada de serviço (banco, cabides) → lavanderia e despensa → cozinha, sem cruzar o social.
- Cuidados: lavanderia não abre direto para preparo de comida nem cola em quarto; porta da máquina não bloqueia passagem.
- Quando não usar: lote sem largura ou zoneamento para o acesso secundário — motivo escrito.

## 5. Passo 4 — Partidos (obrigatório, com imagem)

1. Monte **2 ou 3 partidos** diferentes de verdade (ex.: escada central × escada lateral; garagem na frente × lateral; cozinha aberta para o fundo × para a lateral).
2. Cada partido é um **estudo rápido no Revit numa cópia do arquivo** (`document salvar_copia` → `…_partidoA.rvt`): só paredes, portas, vãos, janelas principais, escada e ambientes nomeados. Sem detalhe.
3. Para cada partido: imagem das plantas dos pavimentos (`export_view_image`, aberta com Read), **fluxos descritos** (visita, morador, serviço), **resultado da `conferir_layout`**, área por setor, prós e contras pelas regras da seção 4 e **quais casos de uso da 4-ter foram aplicados** (e, para os obrigatórios ou padrão não aplicados, o motivo). As opções comparadas (C3, C4, C6) entram aqui como um dos partidos.
4. Relatório `.md` na pasta do caso com tudo acima e, no fim, **o partido escolhido e o motivo**. O escolhido é modelado por inteiro.

## 5-bis. Ordem de modelagem no Revit [v1.1, regra de Claudemberg, 27/10/2026]

1. **Paredes primeiro**, fechando todos os ambientes, com tipo e espessura certos.
2. **Vãos depois:** passagens sem porta (ligação estar–jantar, entrada de closet) com `criar_abertura_parede`, já na posição definitiva.
3. **Esquadrias e vidros por último**: portas (`create_door`, sentido do giro conferido pela seção 4-bis) e janelas (`create_window`). **[v1.2]** A área do vão vem da Skill `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`: estar e quartos 1/8 da área do cômodo; sala-cozinha integrada 1/8 da área total; banheiro 1/10, ou 1/8 por duto. Escreva no relatório a conta de cada janela.
4. **Mobília [v1.2]:** cama, armário, mesa, bancada, ilha e louças, antes de qualquer conferência — o giro das portas (4-bis) só se confere com a mobília no lugar.
5. Só então ambientes (`create_room`) e `conferir_layout`.
6. **Planta de entrega [v1.2]:** cotas dos ambientes e dos vãos e etiquetas sem sobreposição, pela Skill `nbr6492-representacao-grafica`. Abra a imagem exportada e confira antes de entregar.
Inverter a ordem (pôr janela antes de a parede estar certa) obriga a refazer as esquadrias a cada mudança de parede.

## 6. Passo 5 — Conferência

Rode `conferir_layout` no partido escolhido. Ela aponta (sem alterar o modelo): cômodo sem acesso; permanência prolongada acessada por dentro de outro; permanência prolongada sem janela; suíte sem banheiro; área molhada do superior sem área molhada embaixo; ambiente sem ventilação cruzada. Erro grave = volta ao Passo 3. Cada aviso que ficar tem motivo escrito.

## 7. Erros já cometidos

| Data | Erro | Regra |
|---|---|---|
| 19/10/2026 | Layout em faixas: frente toda garagem, entrada lateral, garagem/serviço sem porta, suíte idosa pela cozinha, 0 banheiros, suítes por dentro de outro cômodo, Estar sem janela | Seções 4 e 6 |

## 8. Fontes

- **Roteiro de Claudemberg (19/10/2026):** legislação e terreno → programa → zoneamento por pavimento (social/serviço no térreo, íntimo no superior, hidráulica centralizada) → escada estratégica → circulação curta, integração e ventilação cruzada.
- **F1** — Guias de planejamento de espaço residencial (zonas pública/privada/serviço, gradiente, teste "chegar ao social sem passar pelo privado", circulação mínima pela borda): https://www.studiomatrx.org/students/interior-design-studio-2/space-planning-fundamentals ; https://learnarchitecture.net/architectural-diagrams/33891-zoning-diagram-guide.html
- **F2** — Apostila de setorização residencial (social, íntimo, serviço, circulação e acessos; térreo social, superior íntimo): https://www2.fag.edu.br/coopex/arquivos/producao/15127539905a2acb46332f3.pdf
- **F3** — Estudo sobre habitações do PAR em Maceió (setor social como distribuidor): https://oasisbr.ibict.br/vufind/Record/UFAL_7c694ce0e9364a96bfa51d68bc77235b
- **F4** — Louis Kahn, espaços servidos e servidores (citado em F1).
- **F5** — Guias de plantas de sobrado em lote estreito (social e lavabo no térreo, quartos com banheiro em cima, escada central para luz): https://www.architecturaldesigns.com/blog/how-multi-story-narrow-house-plans-solve-the-space-problem
- **F6** — Daniel Carvalho Arquitetura, vídeo de fluxo de projeto (norte antes de locar, prumada fora da cabeceira, compatibilização): https://www.youtube.com/watch?v=v0eibn6hlzs
- **F7** — EK Architecture (@architecture.ek), Instagram, out. 2026, diagramas sem fala lidos por quadros: https://www.instagram.com/reel/Dd9Vnd0IktW/ (sentido errado × certo da porta da suíte), https://www.instagram.com/reel/DeemZnYIt8H/ (erro de layout na cozinha), https://www.instagram.com/reel/DdrL_ZhoyrP/ (mesa fora da passagem), https://www.instagram.com/reel/DeHlmQMI4ht/ (ventilação: entrada baixa do lado do vento, saída alta).
- **F8** — Eduarda Granado (Graê Arquitetura), apartamento EV: https://www.instagram.com/p/DchTCHuJPC5/ — porta de correr para integrar a sacada, porta no corredor separando o íntimo, mobília desenhada junto. Transcrição, 27/10/2026. É reforma de apartamento: só a lógica das portas é aproveitada.
- **Ordem paredes → vãos → esquadrias:** regra de Claudemberg (27/10/2026); nenhuma fonte externa lida a ensina diretamente.
- **F9 — Casos de uso C1-C9 [v1.3]:** pesquisa de 15 rodadas e 12 casas em `CONSTRUCAO_DO_ZERO/01_CEO/Gestores/Lúcio (Arquitetura)/pesquisa_externa_layout_mobilia_28-10.md` (C1 pátio: A9-A12; C2 faixa: rodada 3; C3/C5/C8: rodadas 8 e 12, "aging in place"; C7: Alexander, *A Pattern Language*, P159, por resumos; C9: rodada 13) e complementos de Claudemberg na sabatina de 30/10/2026; COES LC 198/2019 Art. 31 lido no acervo.
- **F10 — NBR 9050:2020** (acervo `D:\008_Normas ABNT`): larguras de corredores (regra 7). **Código Civil, Art. 1.301:** janela a menos de 1,50 m da divisa (C7).
- Medidas (Neufert, Panero, Pronk): na Skill `layout-mobiliario-dimensoes-residencial`.
- Pendente de aprofundar (pesquisa contínua da Rotina Diária): Buxton, *Manual do Arquiteto*, caps. 18 (moradia para idosos — C5/C8) e 36 (zonas tropicais — regra 9), no acervo `D:\005_CONHECIMENTO`; Francis Ching, *Arquitetura: Forma, Espaço e Ordem*; Christopher Alexander, *A Pattern Language* (original); plantas de casas publicadas no ArchDaily por escritórios reconhecidos.
