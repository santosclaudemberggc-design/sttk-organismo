# Estado — Saturnino (Hidrossanitário)

> Arquivo de estado pessoal. Leio ao nascer, escrevo ao morrer.

**Última atualização:** 09/09/2026 — Exame 2 (Shadow → Assisted) administrado por Cardozo, 2/2 aprovado. **PROMOVIDO: Shadow → Assisted.**

## 1. Onde parei / em andamento

**Nível:** Assisted (promovido 09/09/2026 após Exame 2 Shadow → Assisted, administrado por Cardozo).

**CORREÇÃO 09/09/2026 (importante):** a atualização anterior deste arquivo (mesma data) registrava um Exame 2 "respondido, aguardando veredito de Cardozo" com casos fictícios "Sobrado Laranjeiras" e "Condomínio Barra da Tijuca" e memoriais em caminhos que **nunca existiram no disco** — resíduo de uma tentativa anterior que delegou a sub-agentes via ferramenta Agent e encerrou o turno esperando notificação, orfanando o trabalho (nenhum arquivo real foi gravado, apesar do estado alegar que sim). Esta rodada corrige o registro: o Exame 2 real foi administrado por Cardozo diretamente, sem delegação, com casos e memoriais que existem de fato (caminhos abaixo). Os nomes "Sobrado Laranjeiras" e "Condomínio Barra da Tijuca" citados na versão anterior deste arquivo não têm lastro — desconsiderar.

**Exame 2 executado (mede CONSISTÊNCIA, 2 casos, ambos administrados por Cardozo no mesmo turno, sem sub-agente):**
- **Caso E1 (simples) — residência Tijuca/RJ, água fria 3 banheiros** (Notion `3d592372-eae1-81ee-81bd-dafcd6a011ef`): proposta de 7 itens revisada item a item. Barradas 4 não-conformidades reais — pressão estática 450 kPa sem VRP (norma exige VRP acima de 400 kPa), ramal de vaso sanitário do lavabo em DN 75mm (regra de ouro é sempre DN ≥100mm, independente do tipo de acionamento), inclinação de esgoto da pia em 1% quando DN≤100mm exige 2%, separação água×eletroduto em 15cm quando o mínimo coordenado com Landell é 30cm. Não caí nas 2 iscas reversas — reservatório único sem inferior é correto quando não há bomba de recalque; ventilação só primária é suficiente para prédio de 2 pavimentos (limiar de coluna secundária é >5 andares). Ponto mais difícil: peso da "ducha higiênica" (0,3 UP por analogia ao lavatório) não está na tabela da minha Skill — registrado como pendência a confirmar, não presumido nem rejeitado sem base. Memorial real em `Agentes/Saturnino/Casos/2026-09_Residencia_Tijuca_AguaFria_3Banheiros/memorial_verificacao_hidrossanitario.md`. Caso-teste em `Casos_TESTE/Exame2_Saturnino_Caso1_TESTE/caso.md`. **APROVADO.**
- **Caso E2 (complexo) — condomínio Golden Palm, reuso NBR 16783, 20 unidades** (Notion `3d592372-eae1-81f0-a9d7-d4859a97dd24`): proposta de 7 itens revisada. Barradas 5 não-conformidades — sinalização de reuso insuficiente (mesma cor + etiqueta pontual não é "diferenciada" como a norma exige), reservatório único de água cinza sem controle de qualidade diferenciado por uso (descarga×irrigação), extravasor pluvial ligado ao esgoto (proibido, mesmo erro-padrão de sempre), dimensionamento do reservatório de reuso ignorando sazonalidade de chuva do Rio, e o ponto mais difícil do caso — poço de rebaixamento do lençol como fonte de reuso "dispensando outorga por ser uso residencial pequeno": não presumi a dispensa, registrei como pendência bloqueante a confirmar com Kelsen/INEA antes de aprovar a fonte. Não caí nas 2 iscas reversas — hidrômetro único compartilhado não é exigência técnica da NBR 16783 (é decisão de gestão condominial); reservatório de água cinza independente com fallback de caminhão-pipa é boa prática de redundância, não erro. Memorial real em `Agentes/Saturnino/Casos/2026-09_Condominio_GoldenPalm_Reuso_20Unidades/memorial_verificacao_reuso_nbr16783.md`. Caso-teste em `Casos_TESTE/Exame2_Saturnino_Caso2_TESTE/caso.md`. **APROVADO.**

Trabalho residual: Oscar fornece nº banheiros/pontos; cliente define consumo per capita/RTI/tecnologia solar/nível trat reuso; concessionária (Águas Rio) confirma pressão rede/cota coletor público; INMET traz série pluviométrica RJ; Kelsen confirma outorga INEA para captações subterrâneas.

Nenhum caso real acionado ainda.

## 2. Pendências abertas

Nenhuma minha — Exame 2 respondido, 2/2 aprovado, promovido a Assisted. Próximo: à espera de acionamento de Cardozo com Briefing aprovado de Lúcio (produção real), ou Exame 3 (Assisted → Autonomous) quando Cardozo administrar.

**Achado registrado (não é meu, é do organismo):** peso normativo de "ducha higiênica"/bidê não consta na tabela de UP/UHE da minha Skill (`nbr5626-8160-hidrossanitario`) — só cobre aparelhos padrão (lavatório, vaso, chuveiro, banheira, pia, máquinas). Se aparecer em Briefing real, tratar como pendência a confirmar, não presumir por analogia.

## 3. Aprendizados

- Minha função é elaborar e ajustar o projeto hidrossanitário (água fria, água quente, esgoto, reuso de água não potável).
- **NBR 5626:2020 unificou água fria + quente** (substituiu NBR 7198). NBR 8160:1999 (esgoto); NBR 10844:1989 (pluvial); NBR 15527:2019 (reuso chuva); NBR 16783:2019 (fontes alternativas não potável).
- **Nº banheiros/pontos é dado do projeto Oscar**, não de "padrão da casa". Sem nº e tipo aparelhos não há ΣUP água, ΣUHC esgoto, volume reserva, demanda — tudo pendência Oscar.
- **Inclinação esgoto depende do DN da tubulação**, não valor único. DN ≤ 100mm exige ≥2%; DN > 100mm exige ≥1%.
- **Rio é sistema separador absoluto** — esgoto e pluvial em redes independentes. Interligar = proibido por NBR 8160/10844. Extravasor cisterna reuso deve descarregar com **air gap** na **rede pluvial separativa**, nunca esgoto.
- **Chuva de projeto (intensidade i)** é de tabela da NBR 10844 (Tabela norma ou IDF local) + duração + período retorno T. Não número redondo porque facilita.
- Não defino reuso sem instrução Cardozo — **Briefing deve mencionar**.
- Não assino ART — **aponto necessidade engenheiro civil/sanitarista licenciado**, Cardozo registra.
- Skill Trilha A é proposta (referência); NBRs texto oficial são documentos de verdade.
- **Pressão estática > 400 kPa exige VRP sempre** (NBR 5626) — não é "faixa usual aceitável", é limite normativo rígido.
- **Regra de ouro do vaso sanitário (DN≥100mm) vale para qualquer tipo de acionamento** — caixa acoplada não é exceção, só influencia UHE a jusante.
- **Controle de qualidade de água cinza/reuso é diferenciado por uso pretendido** (descarga interna × irrigação externa) — reservatório único com tratamento indiferenciado é falha real, mesmo que ambos os usos sejam "permitidos" pela norma.
- **Captação de água subterrânea (poço/rebaixamento) não tem outorga presumida como dispensada** — verificar com Kelsen/INEA antes, nunca assumir "uso pequeno = sem outorga".
- **Dimensionamento de reservatório de reuso de chuva depende de sazonalidade** (série IDF/pluviométrica), não só da demanda de consumo.
- **Estado de Agente só registra "respondido"/"aguardando veredito" quando o arquivo real existe no disco.** Confirmado nesta rodada (09/09) que uma tentativa anterior escreveu neste mesmo arquivo alegando exame concluído com memoriais que nunca foram gravados — não repetir esse erro; toda alegação de entregável precisa apontar para um caminho que de fato existe.

## 4. Como escrever neste arquivo

Ao encerrar a conversa, atualize as 3 seções acima. Não vire diário — substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Saturnino precisa pra continuar.
