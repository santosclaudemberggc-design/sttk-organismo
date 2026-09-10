# Estado — Glaziou (Paisagismo)

> Arquivo de estado pessoal. Leio ao nascer, escrevo ao morrer.

**Última atualização:** 09/09/2026 — Exame 2 (Shadow → Assisted) administrado por Cardozo, 2/2 aprovado. **PROMOVIDO: Shadow → Assisted.**

## 1. Onde parei / em andamento

**Nível:** Assisted (promovido 09/09/2026 após Exame 2 Shadow → Assisted, administrado por Cardozo).

**CORREÇÃO 09/09/2026 (importante):** a atualização anterior deste arquivo (mesma data) registrava um Exame 2 "respondido, aguardando veredito de Cardozo" com casos fictícios em "Recreio dos Bandeirantes" (drenagem) e "Jardim Botânico" (cobertura verde + jardim de chuva) e memoriais em caminhos que **nunca existiram no disco** — resíduo de uma tentativa anterior que delegou a sub-agentes via ferramenta Agent e encerrou o turno esperando notificação, orfanando o trabalho. Esta rodada corrige o registro: o Exame 2 real foi administrado por Cardozo diretamente, sem delegação, com casos e memoriais que existem de fato (caminhos abaixo). Coincidência de nome: o caso E2 real desta rodada também usa "Recreio dos Bandeirantes" como bairro fictício, mas é um caso novo, com conteúdo e caminho de arquivo diferentes do resíduo anterior — não confundir os dois.

**Exame 2 executado (mede CONSISTÊNCIA, 2 casos, ambos administrados por Cardozo no mesmo turno, sem sub-agente):**
- **Caso E1 (simples) — residência Jacarepaguá/RJ, drenagem superficial de lote 500m²** (Notion `3d592372-eae1-81c8-9010-f76531007e16`): proposta de 6 itens revisada item a item. Barradas 4 não-conformidades reais — inclinação de piso do quintal em 0,3% (mínimo normativo 1% para piso), espécie Spathodea campanulata (espatódea, invasora confirmada IBAMA/INEA-RJ), rampa de acesso em 10% sem corrimão (máximo 8,33% + corrimão bilateral obrigatório, sem exceção por trecho curto), condutor pluvial ligado à mesma tubulação do esgoto (proibido, separador absoluto). Não caí nas 2 iscas reversas — jardim frontal privativo sem rota de circulação obrigatória não exige piso tátil; ipê-amarelo é espécie nativa RJ corretamente especificada. Memorial real em `Agentes/Glaziou/Casos/2026-09_Residencia_Jacarepagua_Drenagem500m2/memorial_verificacao_paisagismo.md`. Caso-teste em `Casos_TESTE/Exame2_Glaziou_Caso1_TESTE/caso.md`. **APROVADO.**
- **Caso E2 (complexo) — lote Recreio dos Bandeirantes/RJ, jardim de chuva + pergolado sobre laje** (Notion `3d592372-eae1-81ea-9535-f80aecb00a27`): proposta de 7 itens revisada. Barradas 4 não-conformidades diretas — fundo da célula do jardim de chuva com declive de 3% (deve ser nivelado ≤1%, declive só nas superfícies de condução), leucena no fundo da célula (invasora, mesmo com boa tolerância hídrica), dimensionamento da célula ignorando a área de contribuição do pátio/calçada (só considerou o telhado), pergolado com treliça vegetal sobre laje aprovado sem laudo de Baumgart por reclassificação semântica ("não é cobertura verde tradicional") — mesma exigência de carga em laje se aplica independente do rótulo. Não caiu nas 2 iscas reversas — extravasor da cisterna direcionado ao jardim de chuva antes da rede pública é combinação recomendada pela própria Skill; pendência levantada com Kelsen sobre taxa de permeabilidade é o comportamento correto (não decidir sozinho). Ponto mais difícil do caso: memorial citando "NBR 16636-4" como base normativa obrigatória do jardim de chuva — rejeitado, pois a própria Skill de jardim de chuva registra explicitamente que não há norma NBR específica identificada para a técnica (é prática de mercado, não exigência regulatória); citar a 16636-4 como respaldo obrigatório para essa técnica específica seria inventar vinculação normativa que a Skill não confirma. Memorial real em `Agentes/Glaziou/Casos/2026-09_Recreio_JardimChuva_CoberturaLeve/memorial_verificacao_jardim_chuva.md`. Caso-teste em `Casos_TESTE/Exame2_Glaziou_Caso2_TESTE/caso.md`. **APROVADO.**

Trabalho residual dos casos-teste (não é caso real): análise de sítio (Glaziou/Lúcio), laudo de carga Baumgart, IDF-RJ INMET, ensaio de infiltração, definição de cliente sobre clima/sombra/manutenção, checagem de taxa de permeabilidade com Kelsen.

Nenhum caso real acionado ainda.

## 2. Pendências abertas

Nenhuma minha — Exame 2 respondido, 2/2 aprovado, promovido a Assisted. Próximo: à espera de acionamento de Cardozo com Briefing aprovado de Lúcio (produção real), ou Exame 3 (Assisted → Autonomous) quando Cardozo administrar.

## 3. Aprendizados

- Minha função é elaborar e ajustar o projeto de paisagismo exterior (plano de plantio, drenagem sustentável, jardim de chuva, especificação de materiais).
- **Sigo NBR 16636-4:2023 (Fases 1-6: Concepção → Pós-obra)**. Seleção de espécies vem em Fases 1-2, após análise de sítio.
- **Espatódea e leucena são exóticas invasoras RJ** (IBAMA/INEA-RJ) — não especificar, nunca, independente de qualquer vantagem técnica alegada (crescimento rápido, tolerância a encharcamento etc.).
- **Cobertura verde/carga em laje:** carga admissível é **dado de entrada** (de Baumgart), não verificação depois. Vale para qualquer estrutura leve com vegetação sobre laje, mesmo que rotulada como "estrutura de sombreamento" em vez de "cobertura verde" — o critério técnico é a existência de carga, não o nome comercial da solução.
- **Jardim de chuva:** célula é área **rebaixada para acumular e infiltrar**, não escoar. Fundo nivelado (≤1%), declive só nas superfícies de condução. Dimensionamento depende da área de contribuição TOTAL (telhado + pátio + qualquer superfície impermeável que escoe para o ponto), não só do telhado.
- **Jardim de chuva não tem norma NBR específica** — é prática de mercado, não exigência regulatória. Não citar NBR 16636-4 (ou qualquer outra) como base normativa obrigatória da técnica em si; ela é recomendada por mérito técnico/sustentável, não por exigência normativa.
- **Rampas:** inclinação máxima 8,33% (1:12) com corrimão bilateral sempre — "trecho curto" não é hipótese de dispensa.
- **Drenagem:** conexão extravasor/drenos → rede pluvial separativa (nunca esgoto). Combinação cisterna (reuso) + jardim de chuva (drenagem do excedente) é boa prática já prevista na Skill.
- **Impermeabilização laje referenciada NBR 9575** — responsabilidade compartilhada com Baumgart (carga) e Saturnino (drenagem).
- **Taxa de permeabilidade/índice urbanístico** é interface obrigatória com Kelsen — não decido sozinho se a área do jardim de chuva/paisagismo conta no cômputo.
- Não defino paisagismo sem entender partido — recebo Briefing com contexto de Cardozo. Não aciono clientes diretamente.
- **Estado de Agente só registra "respondido"/"aguardando veredito" quando o arquivo real existe no disco.** Confirmado nesta rodada (09/09) que uma tentativa anterior escreveu neste mesmo arquivo alegando exame concluído com memoriais que nunca foram gravados — não repetir esse erro.

## 4. Como escrever neste arquivo

Ao encerrar a conversa, atualize as 3 seções acima. Não vire diário — substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Glaziou precisa pra continuar.
