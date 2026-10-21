---
name: partido-volumetria-residencial-contemporanea
description: Como criar a volumetria e o partido de uma casa brasileira contemporânea com identidade própria, ANTES da planta — perfil da família primeiro, jogo de volumes, curvas, balanços, planos soltos, cheios e vazios, varanda como sala, pátio, pé-direito duplo, sacadas, entrada principal marcada, garagem e área externa pensadas junto, brise/cobogó/beiral para o clima do Rio. Entrega obrigatória de 2 ou 3 estudos de volumetria com imagem 3D e fachadas. Use SEMPRE que o Oscar (ou Lúcio) for iniciar o Estudo Preliminar, propor partido, desenhar fachada, volumetria, cobertura, varanda, pé-direito duplo, entrada ou garagem de uma casa — mesmo que o pedido só diga "partido", "volumetria", "fachada", "forma da casa", "estudo de massa" ou "deixar a casa mais moderna".
version: v1.0
status: proposta-em-treino
data: 2026-10-20
origem: "Sabatina Wallenberg × Claudemberg, 19-20/10/2026: o partido B passou na conferir_layout mas a casa é uma caixa retangular, suítes enormes, sem varanda, sacada ou pé-direito duplo, entrada pouco marcada e distribuição que não é de casa brasileira."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar
agentes_cross: Burle (imagem), Portinari (apresentação), Glaziou (área externa), Baumgart (balanços), Kelsen/Hely (afastamentos, ATE, varanda não computável)
skills_relacionadas: layout-residencial-zoneamento-fluxos (vem DEPOIS desta), posicionamento-escada-residencial, varandas-nao-computaveis-ate-to-coes-lc198-rj, lucio-protecao-solar-externa-dispositivos-rj, vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj, nbr15220-3-bioclimatica-rj
validacao: pendente — treino no Ensaio 003 e aprovação de Claudemberg
---

# Skill: Partido e volumetria residencial contemporânea

> **Ordem do trabalho (decisão de Claudemberg, 19/10/2026):** volumetria primeiro, planta depois. Com a forma certa, a distribuição interna, os fluxos, o conforto e a setorização se encaixam melhor. Lei vem antes de tudo: afastamentos, gabarito, ATE/TO e varanda não computável pelas Skills do Kelsen/Hely.

## 1. Por que existe

O partido B do Ensaio 003 passou na `conferir_layout` com 0 grave, mas Claudemberg reprovou: caixa retangular, suítes fora do normal, sem varanda, sacada ou pé-direito duplo, entrada pouco identificável, garagem e área externa sem desenho, e uma casa que "não funciona como casa brasileira". **Passar na conferência não é ser bom projeto.**

## 2. Passo 0 — A casa com a cara do cliente

Antes de qualquer forma, escreva o **perfil da família** a partir do Briefing (nomes, idades, rotina, trabalho em casa, quem recebe visita, hobbies, carros, pets, quem precisa de acessibilidade, gosto declarado, referências que mandaram). Cada decisão de volumetria e de planta cita o trecho do perfil que ela atende. **Programa:** suítes no tamanho do programa; se sobrar área, proponha ambientes novos (estar íntimo/sala de TV, varanda da suíte, adega, sauna, ateliê) marcados **"sugestão ao cliente"** — nunca como programa aprovado.

## 3. O que faz a casa brasileira (moderna e contemporânea) — regras

1. **Jogo de volumes, não caixa.** A tradição carioca (F1: 145 casas 1930–1965, quase todas classificadas "jogo de volumes") compõe a casa por volumes e planos: alas em L, T ou U, um volume solto sobre outro, prisma suspenso sobre pilotis/base recuada (Casa Prudente de Moraes Neto, Niemeyer, 1943). Contemporâneas fazem o mesmo com balanços, planos desmembrados e empenas (F2: SPBR, Nitsche).
2. **Curva como gesto, reta para o uso.** Curvas na volumetria, em muros, marquises, varandas, escada, jardim e em um ou dois ambientes de estar — não em quarto ou banheiro. Exemplos cariocas: muro de fundo em curva (Casa Ofaire), estúdio limitado por parede semicircular (Prudente de Moraes Neto), canteiros sinuosos (Lima Pádua, jardins de Burle Marx) (F1). Reta, quadrado e retângulo ficam para as divisões internas — e mesmo elas podem ter outra forma onde ajudar o uso.
3. **Varanda é sala.** A varanda/alpendre é onde se vive (F1, Casa Costa Ribeiro, Carlos Leão); liga estar, gourmet, piscina e jardim. Contemporâneo: varanda gourmet integrada à cozinha aberta (F3).
4. **Pátio.** O pátio organiza a casa térrea e ventila a de dois pavimentos (F1: Lima Pádua em U com pátio; Paes de Carvalho com pátio entre alas; F2: pátio de pé-direito duplo em Ilhabela).
5. **Pé-direito duplo no social,** com mezanino ou galeria olhando o estar (F1, Casa Francisco Peixoto: estar em três níveis integrados). Use vão na laje (`criar_abertura_shaft`).
6. **Sacadas e varandas nas suítes,** com balanço que também protege o sol (F1, Prudente de Moraes Neto: varanda contínua suspensa protegendo a fachada).
7. **Faixa de serviço junto à divisa,** paralela ao social, ventilando e iluminando os compartimentos secundários (F1, Lima Pádua; F2: faixa que concentra escada, lavabo e cozinha deixando o estar livre).
8. **Entrada principal marcada:** reentrância no volume, marquise, pergolado, muro baixo de pedra, caminho que conduz (F1: Paes de Carvalho, Prudente de Moraes Neto). Entrada de serviço junto à garagem, separada.
9. **Garagem não é a fachada.** Abrigo sob o volume superior, sob pilotis, lateral ou recuada; portão integrado ao muro/fachada; a frente mostra a entrada e um volume com identidade.
10. **Clima do Rio:** brise móvel em leste/oeste, cobogó e muxarabi para filtrar luz e ventilar, beiral e balanço como sombra, cobertura borboleta/inclinada com calha central ou laje plana com beiral (F1, F2). Conferir pelas Skills de proteção solar e de vidro no poente.
11. **Interior–exterior contínuo:** grandes vãos de correr no social para varanda/jardim; nível único entre dentro e fora quando possível (F3; vídeo Daniel Carvalho, Skill de layout F6).
12. **Planta livre no social:** pilares e poucas paredes, ambientes ligados sem barreira (F4).

## 4. Entrega obrigatória — 2 ou 3 estudos de volumetria

Cada estudo, numa cópia do arquivo (`…_volumeA.rvt`): massa dos volumes, cobertura, varandas, balanços, pé-direito duplo, entrada, garagem, área externa (acesso, jardim, piscina, deck) — sem detalhe de planta. Para cada estudo:
- **Imagem 3D** (vista "EP. Perspectiva") e **fachadas** frontal e de fundos (`create_elevation`, marcador fora do lote, com e sem muro), abertas com Read.
- **Ideia em uma frase** (o "conceito") e a ligação com o perfil do cliente.
- **Prós e contras** pelas regras da seção 3 e pela lei (afastamento, gabarito, ATE).
- **O que a ferramenta não fez** (seção 5) e como foi aproximado.

Relatório `.md` com os estudos lado a lado; **Claudemberg escolhe**. Só depois entra a Skill de layout, dentro da volumetria escolhida.

## 5. Limites da ferramenta (Vitruvius, 20/10/2026)

| Quer fazer | Hoje | Como aproximar |
|---|---|---|
| Parede curva | `criar_elemento_linha` categoria `parede_curva` (arco por 3 pontos) | — |
| Laje/varanda com borda curva | `criar_elemento_superficie`/`create_floor` só com vértices retos | polígono com segmentos curtos (≤ 0,30 m); declarar |
| Balanço | laje passando da parede de apoio | declarar para o Baumgart |
| Pé-direito duplo | vão em laje (`criar_abertura_shaft`) + guarda-corpo | — |
| Cobertura inclinada, borboleta ou curva | **não existe** (`create_roof` só plana) | laje plana com platibanda; declarar como lacuna |

Lacunas = proposta de desenvolvimento do Vitruvius (sabatina própria), nunca contorno silencioso.

## 6. Erros já cometidos

| Data | Erro | Regra |
|---|---|---|
| 19/10/2026 | Partido B: caixa retangular, suítes enormes, sem varanda/sacada/pé-direito duplo, entrada fraca, garagem sem desenho | Seções 2–4 |

## 7. Fontes

- **F1** — Márcia Heck, *Casas Modernas Cariocas 1930–1965* (UFRGS/PROPAR, jan. 2005), catálogo de 145 casas com volumetria, cobertura, base e planta (arquivo enviado por Claudemberg, `000501505-02.pdf`; lidas pp. 39–45 e fichas 46–51: Niemeyer — Ofaire, Francisco Peixoto, Prudente de Moraes Neto, Lima Pádua; Carlos Leão — Costa Ribeiro; Lucio Costa — Paes de Carvalho).
- **F2** — Ana Elisia da Costa e Ana Clara Lacerda Menuzzi, "Casas contemporâneas brasileiras: entre gestos de enraizamento e alçamento", *Arquitextos* 232.01, Vitruvius, set. 2019 (SPBR, Casa em Santa Teresa; Nitsche, Casa em Ilhabela): https://vitruvius.com.br/revistas/read/arquitextos/20.232/7519
- **F3** — Archtrends, "Casa contemporânea brasileira" (formas claras, integração, natureza, luz natural, brises): https://blog.archtrends.com/casa-contemporanea-brasileira/
- **F4** — ArchDaily Brasil, "Casas brasileiras: 16 residências com planta livre" (BLOCO, Galeria, Arthur Casas, CR2, Tetro e outros): https://www.archdaily.com/pt/926070/casas-brasileiras-16-residencias-com-planta-livre
- Pendentes (pesquisa contínua da Rotina Diária): demais fichas de F1 (Reidy, Sérgio Bernardes, Bolonha, Vital Brazil); páginas individuais das casas de F4; Studio MK27, Jacobsen, Bernardes, Isay Weinfeld, Gui Mattos; Pinterest de referência enviado por Claudemberg (não lido por ferramenta — pedir imagens).
