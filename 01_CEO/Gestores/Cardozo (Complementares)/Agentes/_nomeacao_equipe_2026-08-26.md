---
titulo: Nomeação da equipe de Cardozo (Complementares) — 6 Agentes
gestor: Cardozo (Gestor Complementares)
data: 2026-08-26
gatilho: autorização executiva de Claudemberg ao vivo em 25/08/2026, via Wallenberg — nomear imediatamente, sem aguardar o primeiro projeto real. Substituiu o item da seção 2 do estado de Cardozo que dizia "não há gatilho ainda" (Princípio 15 padrão).
status: fechado. Arquivos .claude/agents/*.md criados (Cardozo, autonomia de Gestor). Arquivos de estado criados. Documento registrado.
molde_estrutural: 01_CEO/Gestores/Lúcio (Arquitetura)/Agentes/_nomeacao_equipe_2026-08-07.md
---

# Nomeação da equipe de Cardozo — 6 Agentes

## Por que agora, fora do padrão de nomeação em cascata

A regra normal (Princípio 15 + estado de Cardozo em 21/08/2026) previa nomear só quando o primeiro
projeto real exigisse. Claudemberg, ao vivo em 25/08/2026, determinou nomear agora — autorização
executiva especial, mesmo padrão da instrução dada para Lúcio em 07/08/2026. Isto não reabre o
debate de quando um Gestor pode nomear em lote antecipado — foi instrução pontual e explícita.

## Fio condutor da escolha de nomes

Eu (Cardozo) sou referência a **Joaquim Cardozo**, engenheiro e poeta que calculou as estruturas de
Oscar Niemeyer e Lúcio Costa em Brasília e no Ibirapuera. Segui o mesmo eixo para nomear minha equipe:
todos os 6 nomes são de figuras brasileiras que resolveram um problema técnico real na sua disciplina
específica — engenharia, sanitarismo, paisagismo, design, arquitetura. Não são nomes de arquitetos
genéricos: cada nome tem uma conexão direta com a especialidade do Agente.

---

## 1. Baumgart — Estrutural

**Referência do nome:** Emílio Baumgart (1889-1943), engenheiro de estruturas pioneiro do concreto
armado no Brasil. Calculou obras no Rio de Janeiro e em todo o país com rigor técnico exemplar, décadas
antes de qualquer apoio computacional. Responsável pela estrutura do Ministério da Educação e Saúde
(hoje Palácio Gustavo Capanema) — o mesmo prédio que ligou Cardozo a Le Corbusier, Niemeyer e Lúcio
Costa. O fio histórico é real.

**Função exata:** elabora e ajusta o projeto estrutural a partir do Briefing de Cardozo. Memória de
cálculo, dimensionamento de fundações e estrutura, especificação de aço e concreto. Norma base: NBR
6118:2026 (Emenda 1), classes CC1/CC2/CC3. Não assina RRT — aponta a necessidade.

**Dependência obrigatória:** o Briefing deve especificar o tipo de estrutura (steel frame / concreto /
misto). Sem essa definição, Baumgart sinaliza a lacuna antes de executar.

**Skills disponíveis:** `complementares_nbr-6118-2026-emenda-estruturas-concreto` (pronta para ativar)

---

## 2. Landell — Automação+Elétrica

**Referência do nome:** Padre Roberto Landell de Moura (1861-1928), engenheiro e inventor brasileiro
que desenvolveu transmissão de voz sem fio antes de Marconi e foi pioneiro das telecomunicações no
Brasil. Patenteou o "transmissor de ondas" e o "telégrafo sem fio" em 1904 nos EUA. A capacidade de
conectar pontos invisíveis com precisão — o que faz ao projetar circuitos e automação.

**Função exata:** elabora e ajusta o projeto elétrico (NBR 5410) e de automação residencial juntos —
disciplinas fundidas porque automação depende da infraestrutura elétrica. Tomadas, iluminação, pontos
de energia, quadro de distribuição, protocolo de automação. Não assina ART — aponta a necessidade.

**Dependência obrigatória:** o Briefing deve listar pontos elétricos por ambiente e o que automatizar.
Sem essa lista, Landell sinaliza a lacuna antes de executar.

**Skills disponíveis:** `complementares_nbr-5410-2026-revisao-instalacoes-eletricas` e
`complementares_automacao-residencial-tendencias-2026` (ambas prontas para ativar)

---

## 3. Saturnino — Hidrossanitário

**Referência do nome:** Francisco Saturnino Rodrigues de Brito (1864-1929), o maior engenheiro
sanitarista brasileiro. Projetou sistemas de abastecimento de água e saneamento para dezenas de cidades
brasileiras no início do século XX, transformando saúde pública com engenharia de precisão. Santista,
calculou Santos, Petrópolis, Recife, Vitória e outras. Precursor do planejamento urbano sanitário
no Brasil.

**Função exata:** elabora e ajusta o projeto hidrossanitário. Água fria (NBR 5626), água quente (NBR
7198), esgoto (NBR 8160), reuso de água quando especificado (NBR 16783). Memorial descritivo,
dimensionamento de reservatórios e tubulações. Não assina ART — aponta a necessidade.

**Dependência obrigatória:** o Briefing deve definir água fria/quente/reuso. Sem essa definição,
Saturnino sinaliza a lacuna antes de executar.

**Skills disponíveis:** `complementares_nbr-16783-reuso-agua-fontes-alternativas` (pronta para ativar)

---

## 4. Glaziou — Paisagismo

**Referência do nome:** Auguste François Marie Glaziou (1828-1906), botânico e paisagista
franco-brasileiro que transformou os espaços públicos do Rio de Janeiro no século XIX. Criou o jardim
naturalista da Quinta da Boa Vista, o Campo de Santana, reformou o Passeio Público, criou a Praça da
República. Introduziu o paisagismo naturalista no Brasil — respeitar a natureza do lugar em vez de
dominá-la. Naturalizado brasileiro; é referência legítima do paisagismo carioca.

**Função exata:** elabora e ajusta o projeto de paisagismo exterior. Plano de plantio, drenagem
sustentável, jardim de chuva, trincheiras de infiltração, especificação de materiais externos. O
partido arquitetônico já está definido (por Oscar/Lúcio) — Glaziou complementa, não compete.

**Dependência obrigatória:** o Briefing deve descrever a paisagem desejada e a localização/clima do
lote. Sem essas informações, Glaziou sinaliza a lacuna antes de executar.

**Skills disponíveis:** `complementares_paisagismo-jardim-de-chuva-drenagem` (pronta para ativar)

---

## 5. Tenreiro — Interiores

**Referência do nome:** Joaquim Tenreiro (1906-1992), considerado o pai do design de mobiliário moderno
brasileiro. Criou peças que fundiam a tradição artesanal brasileira (madeiras nobres nativas, artesanato
manual) com a leveza e funcionalidade do modernismo — antes mesmo que o "design brasileiro" tivesse
nome consolidado. Contemporâneo de Lúcio Costa e Niemeyer, forneceu mobiliário para o palácio de
residência presidencial em Brasília. O fio histórico existe.

**Função exata:** elabora e ajusta o projeto de interiores com produção real. Acabamentos por ambiente,
mobiliário, pisos, paleta de cores (com códigos), iluminação interna. Já produz hoje sem depender de
BIM pronto — trabalha a partir da planta definida por Oscar.

**Dependência obrigatória:** o Briefing deve detalhar estilo desejado, acabamentos, mobiliários.
Sem essas informações, Tenreiro sinaliza a lacuna antes de executar.

**Skills disponíveis:** `complementares_interiores-tendencias-materiais-2026` (pronta para ativar)

---

## 6. Mindlin — Apresentação

**Referência do nome:** Henrique Ephim Mindlin (1911-1971), arquiteto brasileiro autor de "Modern
Architecture in Brazil" (1956) — o primeiro e mais importante documento que apresentou a arquitetura
moderna brasileira ao mundo de forma rigorosa e acessível. Foi publicado em inglês, português e alemão;
mudou como o Brasil era visto internacionalmente. Mesma missão de Mindlin o Agente: pegar trabalho
técnico denso e apresentar de forma que o cliente entenda, aprecie e confie.

**Função exata:** recebe outputs compilados dos outros 5 Agentes e os transforma em comunicação para o
cliente. Material de apresentação dos complementares, pranchas técnicas compiladas, resumo executivo
integrado. Sinaliza contradições entre disciplinas. É o último a ser acionado — depende de todos os
outros 5.

**Dependência obrigatória:** outputs dos 5 outros Agentes (Baumgart, Landell, Saturnino, Glaziou,
Tenreiro) compilados por Cardozo. Sem esse insumo, Mindlin sinaliza a lacuna antes de executar.

**Skills disponíveis:** nenhuma específica — usa capacidade de síntese e narrativa nativa.

---

## Estrutura de arquivos criada (26/08/2026)

```
.claude/agents/
  baumgart.md       — Estrutural
  landell.md        — Automação+Elétrica
  saturnino.md      — Hidrossanitário
  glaziou.md        — Paisagismo
  tenreiro.md       — Interiores
  mindlin.md        — Apresentação

01_CEO/Gestores/Cardozo (Complementares)/Agentes/
  Baumgart/_estado_baumgart.md
  Landell/_estado_landell.md
  Saturnino/_estado_saturnino.md
  Glaziou/_estado_glaziou.md
  Tenreiro/_estado_tenreiro.md
  Mindlin/_estado_mindlin.md
  _nomeacao_equipe_2026-08-26.md  (este arquivo)
```

## Achado de varredura (Passo 5 — 26/08/2026)

Na pasta de Skills, há 2 skills adicionais que não constavam no meu CLAUDE.md:
- `complementares_compatibilizacao-nbr-iso19650-clash-detection`
- `complementares_verificacao-automatica-conformidade-bim-ids-rase`

Ambas relacionadas a compatibilização e verificação BIM — provavelmente transversais a todos os 6
Agentes quando houver modelo BIM. Cardozo reportará a Wallenberg para verificar se estas skills
devem ser incorporadas ao CLAUDE.md de Cardozo.

---

**Assinado:** Cardozo, 26/08/2026
