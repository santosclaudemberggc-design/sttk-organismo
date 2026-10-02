---
name: rotina-fechamento-historico
description: "Histórico de rodadas antigas do Fechamento de Rotina — movidas do template quando ele passa de 2 rodadas recentes. Nada é apagado, só sai da leitura obrigatória do template."
metadata:
  type: operacional
  escrito_por: wallenberg-cronjob-pdf-2000 (Fechamento do Dia v1.0)
  frequencia: toda vez que o template excede 2 rodadas
---

# Histórico de Rodadas — Fechamento de Rotina

Rodadas completas movidas aqui, sem edição, a partir de `01_CEO/rotina_fechamento_template.md`.
O template mantém só as 2 rodadas mais recentes + a seção consolidada "O QUE NÃO FAZER (acumulado)".
Os itens ❌ de todas as rodadas abaixo já foram incorporados nessa seção consolidada — não precisa reler tudo aqui para saber o que não fazer; venha aqui só para o detalhe completo de uma rodada específica.

**Movido em:** 30/09/2026, pelo Fechamento do Dia v1.0 (primeira execução deste formato). Nova rodada movida em 01/10/2026.

---

## [2026-09-28] — Diária Skills v3.2 (Segunda) — RODADA COMPLETA (2 Skills ativadas)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Monday. Início às 08:38. Pipeline seg-qui.
- [x] **Saturnino, `reservatorio-retardo-decreto23940-aguas-pluviais-rj` v1.1:** ativa-com-ressalva e instalada. Decreto 23.940/2004 e Res. Conj. 001/2005 lidos no texto primário (PDFs extraídos com pypdf porque o WebFetch devolveu binário). Cardozo leu os dois PDFs inteiros: PROCEDE COM RESSALVA, com 4 correções aplicadas.
- [x] **Kelsen, `varandas-nao-computaveis-ate-to-coes-lc198-rj` v1.1:** ativa-com-ressalva e instalada. COES Art. 8º §4º (varanda residencial fora da ATE e da TO). Kelsen conferiu no consolidado da SMU, sem alteração, e acrescentou o Dec. 45.917 Art. 6º (5 m entre varandas em grupamento).
- [x] **Lúcio:** sem Skill. A lacuna de vidro de controle solar é real, mas as fontes não trazem números.
- [x] **Feed:** 2 eventos, 2/2 OK.
- [x] **Livro-razão:** entrada 28/09 em `Setembro.md`, com "como desfazer". Primeira entrada da Diária seg-qui desde 10/09.
- [x] **Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/` (3 arquivos).
- [~] **/watch (v3.3.1):** Lúcio assistiu de verdade "EP14 - Vidros com controlo solar" (youtube.com/shorts/Z0buYmS8fDE), mas as legendas deram 429 e a extração de quadros do script falhou (o ffmpeg novo não aceita `-vsync`). Tirei os quadros com ffmpeg direto e vi 4. É conversa comercial (Portugal) sem parâmetro técnico, então não gerou Skill. Kelsen e Cardozo: a busca de vídeo não achou material relevante (só notícias e texto).
- [ ] **Passo 8 (Trilha B):** não rodou. Nenhum `_estado_` trouxe lacuna de ferramenta nesta rodada.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Lúcio corrige a Skill de partido de 16/09** (linhas 70-72). O limite de 20% da área útil vem do §5º do COES (não residencial). Kelsen recomenda retirar a "projeção máxima 2 m (Dec. 7336/1988)".
- **Kelsen R1:** a Barra/Recreio (LC 270/2024 com o Dec. 3046/81 incorporado) tem regra própria de cômputo de varanda? Hely confirma no RIU/SMDU.
- **Remissão cruzada:** `legal-base-legislativa-bairro`, linha 85, apontar para a Skill de varandas (Kelsen, com backup).
- **Saturnino:** texto da Lei Estadual 9.164/2020 na ALERJ; Decretos 26.168/2006 e 32.119/2010; vigência do rito pós-LICIN 2.0; conflito de uso com a NBR 16783 (descarga sanitária).
- **Bug do /watch:** `scripts/frames.py` usa `-vsync`, que o ffmpeg instalado já não aceita (trocar por `-fps_mode`). É plugin de terceiro, então não editei; decisão de Claudemberg. O 429 nas legendas voltou (o mesmo de 24/09).
- **Orçamento:** foram 7 WebSearch, e não 6. A 7ª localizou o texto primário da LC 198, porque a busca de Kelsen só trouxe a matéria indireta.
- Continuam valendo as pendências de 25/09 (Lint: duplicata no `indice.md`, contradição nbr6122 x fundações Barra, LC 301, span do Painel, livro-razão no prompt agendado).

---

## [2026-09-25] — Diária Skills v3.2 (Sexta) — FLUXO DE SEXTA (Passos 6, 7, 9 e 10)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Friday. Sem pesquisa de Skill nova, que é tarefa de seg-qui.
- [x] **Passo 6, Painel:** 4 eventos novos no `feed.jsonl` via `Append-STTKLog.ps1`, 4/4 OK (LC 281 Art. 40; exames Lelé/Villaça; resumo da semana; Dashboard). 2 eventos de 23/09 **normalizados**: tinham tipo inválido (`skill_proposta`/`skill_correcao`) e o Gestor no lugar da descrição, e o Painel exibia "Cardozo / Landell" como texto.
- [x] **Passo 7, Learning Agent:** 2 vídeos assistidos com `/watch` (o yt-dlp funcionou hoje). Técnica: "LLM Wiki" (Karpathy), com índice/mapa e passada agendada que conecta o conteúdo novo ao antigo. Virou **proposta** de "Lint semanal de Skills" na sexta. Não foi implantada no SKILL.md (exige sincronizar 3 locais e alinhar antes).
- [x] **Passo 9, Dashboard:** setembro tem 28 Skills únicas; semana 21-25/09 teve 6 novas, 6 ativadas com ressalva e **0 testadas em caso real**. Por Gestor: Cardozo 3, Lúcio 2, Kelsen 1. 39 Skills instaladas em `.claude/skills/`.
- [x] **Passo 10, Análise:** abaixo.
- [x] **Livro-razão:** entrada 25/09 em `Setembro.md`.
- [x] **Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-25/` (3 arquivos).

### ANÁLISE SEMANAL (21-25/09)

**Fraquezas primeiro:**
1. **Uso real = 0%.** Em setembro foram 28 Skills e nenhuma foi usada em caso real. A produção está alta, mas ninguém confirma se as Skills servem. O gargalo é aplicar, não produzir.
2. **Livro-razão sem registro da Diária desde 10/09.** O prompt agendado v3.2 não cita o livro-razão, embora a Regra de Governança o torne obrigatório. As Skills de 15 a 24/09 não têm "como desfazer" registrado. **Decisão de Claudemberg.**
3. **O Lint (1ª passada, só leitura) achou 4 problemas:**
   - `indice.md` de Setembro: as linhas de 18/09 (Tenreiro 8995-1 e Glaziou FPJ/SMAC) aparecem 2 vezes (30 linhas para 28 Skills). O bloco "Estatísticas" está velho: diz "acumulado 15" e dá Glaziou/Tenreiro com 2.
   - **Contradição entre Skills instaladas:** `nbr6122-2019-fundacoes` diz "unifamiliar STTK 2 sondagens é o mínimo usual", mas `fundacoes-solos-moles-lencol-freatico-barra-recreio` R7 (NBR 8036) pede mín. 3 entre 200 e 400 m² de projeção. Cardozo/Baumgart harmonizam.
   - A referência cruzada é só de ida: `iluminacao-interiores-nbr-iso-8995-1-residencial` cita a Skill de 31/08, mas `nbr15575-4-nbr8995-1-interiores` não cita a de 18/09 (pendência aberta desde 18/09).
   - A Skill LC 301 v1.1 está com NÃO PROCEDE desde 23/09 e continua em `Skills_Propostas/` à espera de decisão.
4. **Painel com a data parada em 11/09** (`<span id="updated">`, ainda diz "15 membros"). O prompt agendado proíbe editar o HTML; a referência 6.c manda atualizar. As duas instruções se contradizem.

**Pontos fortes:** foco geográfico Barra/Recreio cumprido nas 6 Skills; Kelsen fechou a LC 281 Art. 40 contra o texto primário; exames de Lelé e Villaça aplicados sem atalho; `/watch` funcionou em 3 dos 4 dias em que foi tentado.

**Próximas prioridades (28/09 em diante):**
- (1) Claudemberg decide: livro-razão no prompt da Diária, LC 301, travas 3 de Lelé/Villaça, span do Painel e a proposta de Lint semanal.
- (2) Cardozo harmoniza a regra de furos entre nbr6122 e fundações Barra.
- (3) Limpar a duplicata e recalcular as estatísticas do `indice.md`, com backup.
- (4) Pôr pelo menos 1 Skill da semana à prova no Ensaio Sombra 002, para testar uso real.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- Os 4 achados do Lint acima, mais os pendentes de 24/09 (NBR 8036 sem leitura primária; Art. 106 LC 270/2024 em aberto; LC 281 Art. 16 x Art. 40, prazo de legalização, com o Gate do Maurício).
- yt-dlp: funcionou hoje (25/09) só com legendas. O 403/429 de 24/09 pode voltar, então não trate como resolvido.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Não assistir de novo** os vídeos 0-QDPnEIkvw e VUCChmNYpKU: técnica já extraída (LLM Wiki / Lint).
- ❌ **Não editar `painel_fundador_sttk.html`** até Claudemberg resolver o conflito do span.
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos.

---

## [2026-09-24] — Diária Skills v3.2 (Quinta) — RODADA COMPLETA (0 Skill nova, 2 correções)

### RODADA ATUAL (O que foi entregue)

- [x] **Skill nova:** 0. Material de SPT seria duplicata da Skill de fundações da Barra (21/09), então foi feita correção, conforme o Princípio 15.
- [x] **Correção Baumgart → v1.1** (`fundacoes-solos-moles-lencol-freatico-barra-recreio`): R5 FECHADA, porque a NBR 6484:2020 substitui a 2001. Entrou o critério de paralisação do SPT (10 m/N≥25, 8 m/N≥30, 6 m/N≥35) e a regra "paralisação ≠ rocha → sondagem mista". O nº mínimo de furos foi reatribuído da NBR 6122 para a NBR 8036. Cardozo: PROCEDE COM RESSALVA. Skill reinstalada em `.claude/skills/`.
- [x] **Adendo Kelsen LC 301:** o "Art. 64" existe na **LC 229/2021 com a redação da LC 301** (a LC 301 termina no Art. 63). Ele trata de isenção de Operação Interligada em AP3 + Tijuca/Praça da Bandeira até 31/12/2027. Sem efeito na Barra/Recreio. Confirma o veredito NÃO PROCEDE (23/09). Pendência "Art. 64" ENCERRADA.
- [x] **Feed:** 2 eventos (skill Cardozo + decisão Wallenberg), ambos OK.
- [x] **Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-24/` (4 arquivos)
- [x] **Lúcio:** sem Skill. A busca só trouxe material genérico sobre ventilação/mofo e brise, tema já coberto pelas Skills de 16/09, 17/09 e 22/09.
- [ ] **/watch (v3.3.1):** tentado no vídeo de Cardozo (NBR 6484). **Falhou**: YouTube HTTP 429 nas legendas e 403 no áudio, no mesmo yt-dlp que funcionou em 22/09. Kelsen: busca de vídeo sem resultado relevante (só notícias). Lúcio: só vídeo genérico em tema já coberto.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **yt-dlp voltou a dar 403/429 (24/09)** — aviso de "impersonation target" ausente. Checar `curl_cffi`/atualização do yt-dlp antes da próxima rodada com vídeo.
- **NBR 8036 (valores de nº mínimo de furos):** vêm da memória de Cardozo, sem leitura da norma. Baumgart confere antes de usar em memorial. Considerar harmonizar a Skill `nbr6122-2019-fundacoes` ("mín. 2") com esta regra por faixa de área.
- **LC 301 cadeia de 30% (Art. 40 LC 281) em AP4:** continua aberta para Hely (lacuna registrada por Kelsen em 23/09).
- **Art. 106 LC 270/2024:** continua aberto.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **NBR 6484:2020 / sondagem SPT: não crie Skill separada.** Está coberta pela Skill de fundações Barra/Recreio v1.1.
- ❌ **Art. 64 LC 301: não pesquise de novo.** Resolvido (é LC 229, AP3/Tijuca, fora da AP4).
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos.

---

## [2026-09-23] — Diária Skills v3.2 (Quarta) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skill criada:** 1 (Landell — NBR 14565:2019 Cabeamento Estruturado para Automação Residencial — proposta → ativa-com-ressalva em rodada única)
- [x] **Skill instalada:** `.claude/skills/nbr14565-2019-cabeamento-estruturado-automacao-residencial/SKILL.md`
- [x] **Correção aplicada (Kelsen):** LC 301/2026 → v1.1 — Art. 20, §8º confirmado via legisweb: +20% adicional exclusivo para AEIU Praça Onze por 24 meses (~ago/2028), separado da cadeia de 30%; Art. 64 nova questão (isenção áreas receptoras 31/12/2027)
- [x] **Cardozo validou Landell NBR 14565:** PROCEDE COM RESSALVA — R1: aterramento rack (cabo verde-amarelo 4mm² dedicado); R2: gatilho R$8k/m² é indicativo; R3: NBR 14159 (fibra GPON) não coberta
- [x] **Feed atualizado:** 2 entradas (nova Skill Landell + correção LC 301)
- [x] **Índice Setembro:** 28 Skills acumuladas (Landell sobe de 3 para 4; LC 301 atualizada, não nova)
- [x] **Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-23/` com LC 301 original + indice original
- [x] **Compliance v3.3.1:** vídeo LICIN 2.0 via yt-dlp auto-captions — conteúdo 2021 pré-LICIN 2.0, sem nova Skill
- [x] **Lúcio:** sem Skill nova (ventilação cruzada/fachada poente já coberta por Partido Arquitetônico 16/09 + Proteção Solar 17/09 — Princípio 15)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **LC 301/2026 cadeia de 30% (escopo):** ainda sem confirmação definitiva se vale RJ-amplo ou só AEIU. Hely lê o art. de vigência/disposições gerais antes de usar com cliente fora da área central
- **Art. 64 LC 301:** isenção em "áreas receptoras" até 31/12/2027 — escopo incerto (TDC/OODC vs. desconto de protocolo) — nova questão para Hely
- **Art. 106 LC 270/2024 (isenção OODC):** continua em aberto (texto só até Art. 80 no legisweb)
- **NBR 6484 edição:** Skill Baumgart cita "NBR 6484/2020" — Baumgart confirma edição vigente

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **NBR 14565:2019 cabeamento estruturado não duplique** — Skill Landell 23/09 (ativa-com-ressalva)
- ❌ **LC 301/2026 AEIU não crie nova Skill** — Skill Kelsen 18/09 v1.1 (proposta-com-ressalvas, corrigida 23/09)
- ❌ **Ventilação cruzada/fachada poente Lúcio não duplique** — coberta por Partido Arquitetônico (16/09) + Proteção Solar (17/09)
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-22] — Diária Skills v3.2 (Terça) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 2 (Glaziou espécies nativas Mata Atlântica + Lúcio NBR 15575-4 Emenda 2025 desempenho térmico ZB 4A)
- [x] **Skills ativadas:** 2 (ambas ativa-com-ressalva após validação Cardozo/Glaziou e Lúcio)
- [x] **Skills instaladas:** `.claude/skills/especies-nativas-mata-atlantica-paisagismo-lotes-rj/SKILL.md` + `.claude/skills/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj/SKILL.md`
- [x] **Correção aplicada (Lúcio):** "Hely/Oscar" → "Oscar" na linha 58 (R1 ressalva). Status atualizado para `ativa-com-ressalva` em ambas
- [x] **Feed atualizado:** 2 entradas (Cardozo/Glaziou espécies nativas + Lúcio/Oscar NBR 15575-4)
- [x] **Índice Setembro atualizado:** 27 Skills acumuladas (sobe de 25; Glaziou sobe de 3 para 4; Lúcio/Oscar sobe de 4 para 5)
- [x] **Commit local:** feito ao finalizar esta rodada (25dc41f)
- [x] **Kelsen:** sem Skill nova (pesquisa APA Barra da Tijuca sem dados públicos viáveis — descartada conforme Princípio 3)
- [x] **Vídeos /watch:** 2 buscas video-orientadas completadas (yt-dlp HTTP 403 RESOLVIDO com yt-dlp.conf + deno)
  - Glaziou: Vídeo YouTube [Plantas nativas Mata Atlântica](https://www.youtube.com/watch?v=LdgXA3HDMwQ) (ago/2024) + estudos 2024-2025
  - Lúcio: Seed Solution + LabEEE UFSC NBR 15575-4 Emenda 2025 simulação anual
  - **v3.3.1 cumprido:** 2/2 Gestores com pesquisa video-orientada

### O QUE FICOU PENDENTE (Cuidado: não repita)

- ✅ **yt-dlp desbloqueado:** deno 2.9.7 instalado, yt-dlp.conf configurado com deno path. /watch funcional para próximas rodadas (23/09+)
- **Kelsen APA Barra:** Decreto nº 3046-81 (ZE-5) e LC 270/2024 já cobertos na Skill de 21/09. APA condicionantes específicas por lote — sem fonte pública viável (INEA portal + consultoria não entregaram dados), descartado. Alternativa: Hely consultar INEA direção ao cliente se houver caso real
- **Glaziou Mata Atlântica:** Skill criada com 10+ espécies confirmadas; R5 mandatória = validar Flora e Funga do Brasil (floradobrasil.jbrj.gov.br) antes de especificar

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Espécies Nativas Mata Atlântica não duplique** — Skill Glaziou 22/09 (ativa-com-ressalva)
- ❌ **NBR 15575-4 Emenda 2025 não duplique** — Skill Lúcio 22/09 (ativa-com-ressalva, correção aplicada)
- ❌ **APA Barra Condicionantes não tente novamente** — dados públicos insuficientes (22/09 confirmado)
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-21] — Diária Skills v3.2 (Segunda) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 3 (Lúcio COE LC 198/2019 ventilação/iluminação/pé-direito + Baumgart fundações solos moles Barra/Recreio + Kelsen Decreto 3046/81 + LC 270/2024 LICIN Barra/Recreio)
- [x] **Skills ativadas:** 2 (Lúcio ativa-com-ressalva + Baumgart/Cardozo ativa-com-ressalva)
- [x] **Skills instaladas:** `.claude/skills/coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj/SKILL.md` + `.claude/skills/fundacoes-solos-moles-lencol-freatico-barra-recreio/SKILL.md`
- [x] **Kelsen Decreto 3046/81:** **RATIFICADA por Claudemberg 21/09** — status `ativa-com-ressalva`. Instalada em `.claude/skills/decreto3046-81-lc270-2024-licin-barra-recreio/SKILL.md`. Ressalvas R1/R5/R8 críticas permanecem ativas.
- [x] **Feed atualizado:** 5 entradas (Lúcio proposta + Baumgart proposta + Kelsen proposta + Lúcio ativação + Baumgart ativação)
- [x] **Índice Setembro:** 25 Skills acumuladas (semana 14/09+ = 14; Baumgart 7; Kelsen/Hely 7; Lúcio/Oscar 4)
- [x] **Commit local:** feito ao finalizar esta rodada
- [x] **Foco geográfico:** Barra da Tijuca, Recreio dos Bandeirantes (Zona Oeste RJ) — Lúcio com fonte primária LC 198/2019 lida; Baumgart com fontes secundárias; Kelsen com fonte parcial LC 270/2024 (truncada Art. 80)
- [x] **Vídeos /watch analisados:** 2 (Lúcio COE vãos iluminação + Kelsen LICIN 2.0 processo digital). Achados: vão RJ = 1/8 área (não 1/7); RIU é passo zero LICIN; processos 100% digitais desde jun/2021; orla = restrição sombreamento na faixa de areia/ciclovia/calçadão que "poucos arquitetos sabem".
- [x] **Passo 8 Trilha B executado e filtrado (21/09):** buscas GitHub rodaram para Kelsen, Lúcio e Cardozo (6 Agentes). Filtro Claudemberg aplicado: **todo projeto fica dentro do Revit** — ferramentas standalone (PyNite, CBE Clima, EasyEletric, PyFlo, open-garden-planner etc.) descartadas por não integrar com Revit. Sobrevivem apenas ferramentas de pesquisa pré-Revit de Kelsen (GEOINFO/SMUL + licenciamento-ambiental-automatizado).
- [x] **Regra nova permanente — Trilha B Lúcio/Cardozo:** próximas rodadas buscam **Revit add-ins / plugins GitHub** (`.addin`, Dynamo scripts, Revit API) — não ferramentas standalone Python/web. Kelsen/Hely é exceção (pesquisa legal não passa pelo Revit).

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Art. 106 LC 270/2024 (isenção OODC):** texto disponível só até Art. 80 via legisweb.com.br. Hely deve ler Art. 106 na íntegra via Diário Oficial ou balcão SMU. Bloqueia: Skill TDC/LICIN 2.0 (16/09) atualização final
- **NBR 6484 edição real:** Skill Baumgart cita "NBR 6484/2020" mas edição anterior consolidada era NBR 6484:2001. Baumgart confirma edição vigente antes de qualquer citação em memorial
- **ZPP vs ZRM1-B nomenclatura:** caso Daniel-OB usa "ZRM1-B" do Decreto 3046/81; Skill Kelsen usa "ZPP" da LC 270/2024. Hely confirma via RIU se subzonas foram renomeadas no novo PD
- **Kelsen LC 301/2026 lacunas (pendência 18/09):** desconto 30% AEIU não verificado em fonte primária; texto integral da lei não lido
- **Vídeo compliance (v3.3.1):** apenas Busca 6 (Cardozo) foi vídeo-orientada; Kelsen e Lúcio não — desvio de protocolo no limite das 6 buscas disponíveis, não replicar na próxima rodada

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **COE LC 198/2019 ventilação/iluminação/pé-direito não duplique** — Skill Lúcio 21/09 (ativa-com-ressalva)
- ❌ **Fundações solos moles Barra/Recreio não duplique** — Skill Baumgart 21/09 (ativa-com-ressalva)
- ❌ **Decreto 3046/81 + LC 270/2024 LICIN Barra/Recreio não duplique** — Skill Kelsen 21/09 (ativa-com-ressalva, ratificada)
- ❌ **PyNite / anaStruct / StructPy não proponha** — estrutural Python standalone, não integra Revit (filtro Claudemberg 21/09)
- ❌ **CBE Clima Tool não proponha** — análise climática web standalone, não integra Revit
- ❌ **EasyEletric SaaS não proponha** — elétrico NBR 5410 standalone, não integra Revit
- ❌ **PyFlo / pipedream não proponha** — hidráulica Python standalone, não integra Revit
- ❌ **open-garden-planner não proponha** — paisagismo standalone, não integra Revit
- ❌ **Blueprint3d / AI interior design agent não proponha** — interiores standalone, não integra Revit
- ❌ **Trilha B Lúcio/Cardozo: nunca mais propor ferramenta standalone** — buscar apenas Revit add-ins/plugins/Dynamo scripts GitHub
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-18] — Diária Skills v3.2 (Sexta) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 3 (Tenreiro iluminação NBR ISO/CIE 8995-1 + Glaziou remoção árvores SMAC/FPJ + Kelsen LC 301/2026 AEIU)
- [x] **Skills ativadas:** 2 (Tenreiro + Glaziou — Cardozo PROCEDE COM RESSALVA)
- [x] **Skills instaladas:** `.claude/skills/iluminacao-interiores-nbr-iso-8995-1-residencial/SKILL.md` + `.claude/skills/remocao-arvores-smac-fpj-autorizacao-compensacao-rj/SKILL.md`
- [x] **Kelsen LC 301:** status `proposta-com-ressalvas` — aguarda Hely verificar 4 lacunas (desconto 30% geral vs. AEIU, parâmetros CA por setor, prorrogação definitiva, texto integral)
- [x] **Feed atualizado:** 7 entradas totais (Tenreiro proposta + Glaziou proposta + LC 301 decisão + resumo semanal + dashboard + Tenreiro ativação + Glaziou ativação)
- [x] **Correção factual:** LC 281 → LC 291 em 2 pontos da Skill LC 301 (erro de propagação da Skill OODC de 15/09)
- [x] **Índice Setembro:** 22 Skills acumuladas (semana 14/09+ = 11; Cardozo 18; Kelsen/Hely 6; Lúcio 5)
- [x] **Commit local:** feito ao finalizar esta rodada

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **LC 301/2026 lacunas críticas (Kelsen/Hely):** desconto 30% é geral (todo RJ) ou restrito ao perímetro da AEIU Praça Onze? Texto integral da lei (PDF) não foi lido — WebFetch retornou binário. Hely deve verificar Art. de disposições gerais/transitórias antes de informar desconto a qualquer cliente.
- **LC 281 vs LC 291:** o erro de origem está na Skill OODC/Mais-Valerá de 15/09 (mencionava "LC 281/2025" na tabela de janelas). A Skill LC 301 foi corrigida (18/09), mas verificar se a Skill OODC também foi corrigida.
- **yt-dlp/YouTube:** HTTP 403 + 429 na extração + sem JS runtime (deno/node). yt-dlp precisa de `deno` ou `node` instalado na máquina para extrair YouTube. Tentar /watch em próxima sexta após instalação.
- **Tenreiro NBR 8995-1 coexistência:** Skill de 18/09 coexiste com a Skill `tenreiro_nbr15575-4-emenda1-nbr8995-1-interiores-desempenho.md` (31/08, ainda em propostas) — adicionar referência cruzada entre as duas em próxima rodada.
- **Painel `id="updated"`:** span hardcoded, não é atualizado pelo feed.jsonl. Limitação arquitetural mantida — feed.jsonl está atual.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Iluminação Interiores NBR ISO/CIE 8995-1 não duplique** — Skill Tenreiro 18/09 (ativa-com-ressalva)
- ❌ **Remoção Árvores FPJ/SMAC RJ não duplique** — Skill Glaziou 18/09 (ativa-com-ressalva)
- ❌ **LC 301/2026 AEIU Praça Onze não duplique** — Skill Kelsen 18/09 (proposta-com-ressalvas)
- ❌ **LC 291/2025 não crie Skill separada** — conteúdo já coberto como histórico na Skill LC 301
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-17] — Diária Skills v3.2 (Quinta) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 1 (Proteção Solar Externa — Brises, Cobogó e Venezianas — Lúcio v1.1)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (1 Skill + índice atualizado)
- [x] **Skill ativada:** SIM — Lúcio validou no mesmo dia (PROCEDE COM RESSALVA, 4 ressalvas)
- [x] **Skill instalada:** `.claude/skills/lucio-protecao-solar-externa-dispositivos-rj/SKILL.md` — ativa
- [x] **Feed atualizado:** 3 entradas (proposta inicial + achado LC 301/2026 + ativação)
- [x] **Commit local:** 2 commits (d510eec + d43193b)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **LC 301/2026 (09/07/2026 — Municipal RJ):** identificada nos resultados de busca de Kelsen, conteúdo não investigado. Próxima rodada de Kelsen deve incluir busca específica sobre impacto (LICIN/OODC/parâmetros urbanísticos).
- **Tenreiro:** iluminação de interiores com parâmetros numéricos reais — prioridade #1 confirmada (2 Skills, menor cobertura Cardozo).
- **Glaziou:** espécies nativas RJ + SMAC (supressão de árvore em lote privado) — prioridade #2 confirmada (2 Skills, menor cobertura Cardozo).
- **Isenção OODC 2029:** fonte primária (Art. 106 LC 270/2024) não verificada — pendência aberta da Skill TDC/LICIN 2.0 (16/09).
- **Painel:** desatualizado (11/09/2026) — próxima sexta-feira 19/09.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Proteção Solar Externa Lúcio não duplique** — Skill de 17/09 v1.1 (ativa-com-ressalva)
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-16] — Diária Skills v3.0 (Quarta) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 3 (TDC/LICIN 2.0 v1.0 — Kelsen + Partido/Conforto Térmico/Tipologias v1.0 — Lúcio + Memorial Descritivo/Apresentação Técnica v1.0 — Mindlin)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (3 Skills + índice atualizado)
- [ ] **Skills ativadas:** Não — todas em status proposta, aguardam avaliação Gestor dono
- [ ] **PDFs gerados:** Não (v2.9: Skills não geram PDF — só pauta e livro-razão)
- [ ] **Painel atualizado:** Não (tarefa de Sexta 19/09)
- [ ] **Livro-razão registrado:** Não — registrar na próxima rodada
- [x] **Commit local:** a ser feito ao finalizar esta rodada

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Verificar isenção OODC até 2029:** dado de Instituto Bramante (fonte secundária) na Skill TDC/LICIN 2.0. Hely deve verificar Art. 106 LC 270/2024 na íntegra antes de usar com cliente.
- **TDC fórmula numérica:** coeficiente de equivalência não fixado em lei — depende de regulamentação SMDU por caso.
- **Tenreiro:** ainda com apenas 2 Skills. Menor cobertura dos Agentes Cardozo (com Mindlin agora em 2). Próxima prioridade: iluminação de interiores + acabamentos RJ com parâmetros numéricos reais.
- **Glaziou:** ainda com 2 Skills. Espécies nativas RJ + legislação SMAC (supressão de árvore em lote privado) ainda sem cobertura.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **TDC/LICIN 2.0 não duplique** — Skill de 16/09 v1.0 (proposta)
- ❌ **Partido/Conforto Térmico não duplique** — Skill de 16/09 v1.0 (proposta)
- ❌ **Memorial Descritivo/Apresentação Técnica Mindlin não duplique** — Skill de 16/09 v1.0 (proposta)
- ❌ Todos os itens de "NÃO FAZER" das rodadas anteriores continuam válidos

---

## [2026-09-15] — Diária Skills v3.0 (Segunda) — RODADA COMPLETA

### RODADA ATUAL (O que foi entregue)

- [x] **Skills criadas:** 3 (OODC/Mais-Valerá/Mais-Valia v1.1 corrigida — Kelsen + NBR 9050:2020 v1.1 enriquecida — Lúcio + NBR 5419:2026 nova — Landell)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (3 Skills + índice atualizado)
- [x] **PDFs gerados:** 3 (1 Skill Kelsen corrigida + 1 Skill Lúcio enriquecida + 1 Skill Landell nova + índice regenerado = 4 PDFs)
- [x] **Enriquecimentos aplicados:** Kelsen (2 janelas LC 274+LC 281); Lúcio (tabela rampas + 6 erros + elevador >5 pav.); Landell (parâmetros numéricos completos SPDA)
- [ ] **Skills ativadas:** Não — todas em status proposta, aguardam avaliação Cardozo/Drenagem
- [ ] **Painel atualizado:** Não (tarefa de Sexta 19/09)
- [ ] **Livro-razão registrado:** Não — registrar na próxima rodada
- [x] **Commit local:** Pendente (será feito agora)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Mindlin:** ainda com apenas 1 Skill (NBR 6492). Menor cobertura dos Agentes Cardozo — próxima prioridade.
- **OODC fórmula:** Anexo XXV da LC 270/2024 não obtido. Consultar SMU diretamente quando caso real exigir.
- **OODC isenção 5 anos:** mencionada em fonte secundária, NÃO confirmada. Não tratar como fato.
- **NBR 17076:2024 Skill:** ainda aguarda validação Cardozo.
- **Kelsen:** sem deliberação CAU-RJ nova em setembro. LICIN 2.0 sem atualização RJ.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **OODC/Mais-Valerá/Mais-Valia não duplique** — Skill de 15/09 v1.1 (proposta, corrigida)
- ❌ **NBR 9050:2020 acessibilidade não duplique** — Skill de 15/09 v1.1 (proposta, enriquecida)
- ❌ **NBR 5419:2026 SPDA não duplique** — Skill de 15/09 v1.0 (proposta, nova)
- ❌ **NBR 5419:2001 não use como base** — versão obsoleta (antes da divisão em 4 partes de 2015/2026)
- ❌ **NBR 7229:1993 criar Skill separada** — substituída pela NBR 17076:2024 (14/09)
- ❌ **NBR 13969:1997 criar Skill** — também substituída pela NBR 17076:2024
- ❌ **NBR 10521:1988 criar Skill de sumidouros** — conteúdo coberto na NBR 17076:2024
- ❌ **Regime de Licenciamento Portugal (outubro 2026)** — é português, não RJ
- ❌ Todos os itens da lista de "NÃO FAZER" da rodada anterior continuam válidos

---

## [2026-09-14] — Diária Skills v2.8 (Segunda)

### RODADA ANTERIOR (O que foi entregue)

- [x] **Skills criadas:** 1 (NBR 17076:2024 — Sistema de Tratamento de Esgoto de Menor Porte, Trilha A, Saturnino principal + cross Glaziou/Baumgart)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (1 novo + índice atualizado)
- [ ] **Skill ativada:** Não — aguarda validação Cardozo (status: proposta)
- [x] **PDF gerado:** Sim — gerado nesta rodada (15/09) junto com os novos
- [ ] **Painel atualizado:** Não (tarefa de Sexta 19/09)
- [ ] **Livro-razão registrado:** Não — registrar na próxima rodada

---

## [2026-09-10] — Diária Skills v2.9 (Quinta)

### RODADA ANTERIOR (O que foi entregue)

- [x] **Skills criadas:** 1 (NBR 10844:1989 — Instalações Prediais de Águas Pluviais, Trilha A, Saturnino principal + cross Glaziou/Baumgart)
- [x] **Skill ativada v2.9:** Sim — Cardozo validou PROCEDE, instalada em `.claude/skills/nbr10844-1989-aguas-pluviais/SKILL.md`
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (1 novo + índice atualizado)
- [x] **Livro-razão registrado:** Sim (Setembro.md, entrada 10/09)
- [ ] **Painel atualizado:** Não (tarefa de Sexta 12/09)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Apresentação interativa ao cliente:** busca PAUSADA. Não buscar mais até caso real forçar decisão.
- **LuDattilo/revit-mcp-server (138 tools):** decisão em "avaliar incorporação parcial" — falta comparação tool-a-tool formal.
- **Cardozo Exame 2:** LOTE COMPLETO (6/6) — nenhuma pendência.
- **NBR 7229:1993 (fossas sépticas) / NBR 10521:1988 (poços absorventes):** próxima prioridade Saturnino — para terrenos sem rede pública de esgoto.
- **Intensidade pluviométrica RJ (i mm/h):** obtida só como referência orientativa na Skill de hoje. Saturnino precisa consultar IDF Rio-Águas em caso real — não fechar esse item aqui, é responsabilidade do Agente ao usar a Skill.
- **Mindlin: `agents/mindlin.md` desatualizado** — ainda pode listar "sem Skill técnica própria" mas ele TEM `nbr6492-representacao-grafica` ativa. Corrigir quando houver janela.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Blender MCP não crie Skill nova** — já coberto em `arquitetura_mcp-gratuitos-render-video-blender-huggingface.md` (01/08/2026)
- ❌ **Architecture MCP (sceneview-tools) não pesquise mais** — retornou 404
- ❌ **NBR 5410 não duplique** — já coberta por Skill de 28/08
- ❌ **NBR 15220-3:2024 não duplique** — Skill de 01/09
- ❌ **NBR 15575:2025 desempenho acústico pisos não duplique** — Skill de 03/09
- ❌ **NBR 9575:2024 impermeabilização não duplique** — Skill de 02/09
- ❌ **Resolução SMDU 10/2026 (RDT) não duplique** — Skill de 03/09
- ❌ **COSCIP/CBMERJ Decreto 42/2018 não duplique** — Skill de 04/09
- ❌ **NBR 6122:2022 fundações não duplique** — Skill de 07/09
- ❌ **RevitCortex 173 tools não duplique** — vitruvius_achados 27/08
- ❌ **BIMwright/rvt-mcp 229 tools não crie Skill isolada** — vitruvius_achados 03/09
- ❌ **UV-Tech/revit-claude-mcp 40 tools não crie Skill isolada** — vitruvius_achados 03/09
- ❌ **LuDattilo/revit-mcp-server 138 tools não crie Skill isolada nova** — vitruvius_achados 24/08, atualizado 04/09
- ❌ **IbrahimFahdah/revit-claude-mcp 46 tools não crie Skill isolada** — vitruvius_achados 07/09
- ❌ **Simone-Balin/Sam-AEC 100+ tools não crie Skill** — vitruvius_achados 08/09, guia de setup (1 star)
- ❌ **NBR 6120:2019 cargas não duplique** — Skill de 08/09
- ❌ **NBR 8681:2025 segurança/fatores não duplique** — Skill de 09/09 (ativa-com-ressalva)
- ❌ **NBR 10844:1989 águas pluviais não duplique** — Skill de 10/09 (ativa-com-ressalva)
- ❌ **pyRevit-MCP não crie Skill** — pago, viola critério 1
- ❌ **mcp-servers-for-revit não crie Skill** — arquivado 2024, inativo
- ❌ **Luw.ai, Remodel AI, Redraw, Leonardo AI** — todos cloud, violam critério 2
- ❌ **Autodesk APS Sample MCP Server** — exige assinatura paga, viola critério 1
- ❌ **Modly** — gerador 3D, não renderizador de cena
- ❌ **Apresentação interativa — PAUSAR BUSCA** até caso real forçar decisão

---

## [2026-09-09] — Diária Skills v2.9 (Quarta)

### RODADA ANTERIOR (O que foi entregue)

- [x] **Skills criadas:** 1 (NBR 8681:2025 — Ação e Segurança nas Estruturas, Trilha A, Baumgart principal + cross Saturnino/Landell)
- [x] **Skill ativada v2.9:** Sim — primeira Skill ativada pelo fluxo v2.9 (validada por Cardozo → ativa-com-ressalva, fonte primária ABNT não lida)
- [x] **Skill instalada:** `.claude/skills/nbr8681-2025-seguranca-estruturas/SKILL.md`
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (1 novo + índice atualizado)
- [x] **Livro-razão registrado:** Sim (Setembro.md, entrada 09/09)
- [ ] **Painel atualizado:** Não (tarefa de Sexta 12/09)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Apresentação interativa ao cliente:** busca PAUSADA desde 07/09 (6 buscas consecutivas sem achado). Presenton (28/08) continua o melhor candidato. Não buscar mais até caso real forçar decisão.
- **LuDattilo/revit-mcp-server (138 tools):** decisão em "avaliar incorporação parcial" — falta comparação tool-a-tool formal contra os 35 tools do Vitruvius, e checar coexistência porta 8080.
- **Cardozo Exame 2 (6 agentes):** em andamento semana 08-12/09. Baumgart aprovado (1/6). Saturnino+Glaziou previstos 09/09, Tenreiro+Mindlin previstos 10/09.
- **NBR 10844:1989 (águas pluviais):** próxima prioridade Trilha A para Saturnino. Pesquisa feita 09/09, material viável, mas meta 1/Gestor/dia limitou a esta rodada.
- **NBR 6120:2019:** status "proposta" — aguarda ratificação de Claudemberg (Drenagem avaliou PROCEDE 08/09).

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Blender MCP não crie Skill nova** — já coberto em `arquitetura_mcp-gratuitos-render-video-blender-huggingface.md` (01/08/2026)
- ❌ **Architecture MCP (sceneview-tools) não pesquise mais** — retornou 404
- ❌ **NBR 5410 não duplique** — já coberta por Skill de 28/08
- ❌ **NBR 15220-3:2024 não duplique** — já coberta por Skill de 01/09
- ❌ **NBR 15575:2025 desempenho acústico pisos não duplique** — Skill de 03/09
- ❌ **NBR 9575:2024 impermeabilização não duplique** — Skill de 02/09
- ❌ **Resolução SMDU 10/2026 (RDT) não duplique** — Skill de 03/09
- ❌ **COSCIP/CBMERJ Decreto 42/2018 não duplique** — Skill de 04/09
- ❌ **NBR 6122:2022 fundações não duplique** — Skill de 07/09
- ❌ **RevitCortex 173 tools não duplique** — vitruvius_achados 27/08
- ❌ **BIMwright/rvt-mcp 229 tools não crie Skill isolada** — vitruvius_achados 03/09
- ❌ **UV-Tech/revit-claude-mcp 40 tools não crie Skill isolada** — vitruvius_achados 03/09
- ❌ **LuDattilo/revit-mcp-server 138 tools não crie Skill isolada nova** — vitruvius_achados 24/08, atualizado 04/09
- ❌ **IbrahimFahdah/revit-claude-mcp 46 tools não crie Skill isolada** — vitruvius_achados 07/09 ("monitorar")
- ❌ **Simone-Balin/Sam-AEC 100+ tools não crie Skill isolada** — vitruvius_achados 08/09, é guia de setup (1 star), monitorar baixa prioridade
- ❌ **NBR 6120:2019 cargas não duplique** — Skill de 08/09
- ❌ **NBR 8681:2025 segurança/fatores não duplique** — Skill de 09/09 (ativa-com-ressalva)
- ❌ **pyRevit-MCP não crie Skill** — pago, viola critério 1
- ❌ **mcp-servers-for-revit não crie Skill** — arquivado 2024, inativo
- ❌ **Luw.ai, Remodel AI, Redraw, Leonardo AI** — todos cloud, violam critério 2
- ❌ **Autodesk APS Sample MCP Server** — exige assinatura paga, viola critério 1
- ❌ **Modly** — gerador 3D, não renderizador de cena (foco errado)
- ❌ **Apresentação interativa — PAUSAR BUSCA** até caso real forçar decisão (5 buscas sem novidade)

---

## ESTA RODADA (Preencher ao terminar)

*(Preenchida acima como "RODADA ANTERIOR" — a próxima rotina lê de lá)*

---

## HISTÓRICO DE RODADAS

### [2026-09-04] Diária Skills v2.7 — Sexta (1 Skill + Painel + auto-correção)

- ✅ Entregou: 1 Skill COSCIP/CBMERJ (corrigida v1.1) + 1 achado Vitruvius atualizado (LuDattilo) + Painel republicado + 2 bugs estruturais corrigidos (JSON quebrado, array manual obsoleto)
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho evitado: Presenton não duplicado, LuDattilo não virou Skill isolada, Autodesk APS descartado, Modly descartado
- 🎯 Status: **Completa** — primeiro dia de auto-auditoria preventiva

---

## [LEGADO 2026-09-04] — Diária Skills v2.7 (Sexta)

**⚠️ Correção 04/09/2026:** esta rodada rodou os Passos 1-5+8 (Seg-Qui) por engano — o executor assumiu "Quinta" sem verificar o dia da semana real. **04/09/2026 é SEXTA**, não quinta (03/09 é que foi quinta). O trabalho de pesquisa (Skill COSCIP/CBMERJ) tem valor e foi mantido; os Passos 6/9/10 (Sexta) foram executados em seguida, na mesma rodada, para não perder o dia. Rótulos corrigidos abaixo.

### RODADA ANTERIOR (O que foi entregue)

- [x] **Skills criadas (03/09):** 2 (Resolução SMDU 10/2026 RDT — Legal + NBR 15575:2025 Desempenho Acústico Pisos — Complementares cross-disciplina)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (2 novos + índice atualizado)
- [x] **PDFs regenerados (03/09):** 3 (2 Skills + índice)
- [ ] **Painel atualizado:** Não (tarefa de Sexta 05/09)
- [x] **Livro-razão registrado:** Sim (Setembro.md, entrada 03/09)
- [ ] **Learning Agent propôs melhorias:** N/A (Seg-Qui)

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Apresentação interativa ao cliente:** 4ª busca consecutiva (01-04/09) sem ferramenta gratuita self-hosted viável. Presenton já registrado (28/08) é o melhor candidato até agora, mas ninguém testou de fato. Prioridade rebaixada — considerar parar de buscar até haver caso real que force decisão.
- **COSCIP/CBMERJ:** Skill nova (04/09) tem lacunas reconhecidas — tabela completa do Anexo III e texto integral das NTs 2-03/2-05/2-08/2-15 não lidos na íntegra. Ler antes de qualquer dimensionamento real (ex. caso Daniel-OB, que é grupamento A-4, não isento).
- **LuDattilo/revit-mcp-server (138 tools):** decisão subiu para "avaliar incorporação parcial" — falta comparação tool-a-tool formal contra os 35 tools do Vitruvius, e checar se a porta 8080 fixa colide com outro conector já testado.

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Blender MCP não crie Skill nova** — já coberto em `arquitetura_mcp-gratuitos-render-video-blender-huggingface.md` (01/08/2026)
- ❌ **Architecture MCP (sceneview-tools) não pesquise mais** — retornou 404, projeto possivelmente removido
- ❌ **NBR 5410 não duplique** — já coberta por `landell_nbr5410-2026-eletrica-instalacoes-prediais.md` (28/08)
- ❌ **NBR 15220-3:2024 não duplique** — já coberta por Skill de 01/09
- ❌ **NBR 15575:2025 desempenho acústico pisos não duplique** — coberta por Skill de 03/09
- ❌ **NBR 9575:2024 impermeabilização não duplique** — coberta por Skill de 02/09
- ❌ **Resolução SMDU 10/2026 (RDT) não duplique** — coberta por Skill de 03/09
- ❌ **COSCIP/CBMERJ Decreto 42/2018 não duplique** — coberta por Skill de 04/09
- ❌ **RevitCortex 173 tools não duplique** — já registrado em vitruvius_achados e Skill de 27/08
- ❌ **BIMwright/rvt-mcp 229 tools não crie Skill isolada** — registrado em vitruvius_achados 03/09 (candidato a agregar ao Vitruvius)
- ❌ **UV-Tech/revit-claude-mcp 40 tools não crie Skill isolada** — registrado em vitruvius_achados 03/09 (monitorar)
- ❌ **LuDattilo/revit-mcp-server 138 tools não crie Skill isolada nova** — já existe desde 24/08, só atualizada em detalhe técnico 04/09 (vitruvius_achados)
- ❌ **Luw.ai não crie Skill** — cloud + watermark + sem MCP, viola critério 2 (vazamento de dados)
- ❌ **Remodel AI / Redraw / Leonardo AI** — todos cloud, violam critério 2
- ❌ **Autodesk APS Sample MCP Server não crie Skill** — exige assinatura paga (ACC/BIM360), viola critério 1
- ❌ **Modly não crie Skill de render** — é gerador de modelo 3D via GPU local, não renderizador de cena arquitetônica (foco errado, não critério de segurança)

---

## ESTA RODADA (Preencher ao terminar)

**Nota:** rodada híbrida — começou como Seg-Qui (engano de calendário, corrigido em andamento) e terminou cobrindo os Passos 6/9/10 de Sexta na mesma sessão, já que 04/09 é realmente sexta-feira.

### Entregáveis — Passos 1-5+8 (Seg-Qui, pesquisa)

- [x] **Skills criadas:** 1 (COSCIP/CBMERJ Decreto 42/2018 v1.1 — Segurança Contra Incêndio RJ — Complementares cross-disciplina Landell/Baumgart; corrigida em andamento após auto-verificação, ver abaixo)
- [x] **Skills documentadas:** `01_CEO/Skills_Propostas/2026/Setembro/` (1 novo + índice atualizado)
- [x] **PDFs regenerados:** 2 (1 Skill + índice)
- [x] **Vitruvius achados atualizados:** 1 (LuDattilo 138 tools — detalhe técnico completo, decisão sobe para "avaliar incorporação parcial")
- [ ] **Learning Agent melhorias:** N/A (regra: só segunda e se houve execução real)

### Auto-correção (achada ao preparar o Painel, antes de publicar qualquer coisa errada)

1. **Skill COSCIP mal enquadrada:** dizia "lacuna nunca coberta antes" — falso, já apurada e fechada (pendência B10, 28/07/2026). Corrigida para v1.1 (é expansão real: mapa de NTs por disciplina + achado novo sobre grupamentos A-4, não descoberta). `legal-base-legislativa-bairro/SKILL.md` também atualizada com o achado do grupamento.
2. **`pendencias.json` estava com JSON inválido** (2 chaves de fechamento faltando) — corrigido e revalidado (49 itens). Tempo que ficou quebrado: indeterminado, nenhum registro anterior menciona.
3. **Painel publicado (Artifact) estava travado em 27/08/2026** — a atualização de 01/09 só existia no arquivo local, nunca foi republicada de fato. Corrigido.
4. **Array manual `pendencias` do Painel tinha 5 de 8 itens obsoletos** (já resolvidos/descartados em `pendencias.json`, ex.: WAN 2.2, Fase 2 tokens, 2 itens Drive Legal, CAU-RJ RRT) — mesma classe de bug já corrigida uma vez em 04/08/2026, reincidiu. Reescrito com os 6 itens reais.
5. **Nova pendência aberta:** `kelsen-coscip-grupamento-a4-limiar-6-unidades` — Hely apura com rigor antes de aplicar ao caso Daniel-OB.

### Entregáveis — Passos 6/9/10 (Sexta, hoje mesmo)

- [x] **Painel atualizado e republicado:** feed com 4 eventos reais desde 01/09 (ratificação em bloco, Compatibilização→Fechamento, Portão de Trabalho, auto-correção de hoje); KPIs de pendências recontados (43/49 fechadas, 6 ativas — antes mostrava números stale "34/43"); gráficos SVG (criticidade, alçada, represamento) recalculados com dados reais.
- [x] **Dashboard:** KPI "Skills criadas esta semana / testadas" adicionado (7 criadas, 0 testadas, Complementares é o Gestor mais ativo com 4). Achado: a seção de Dashboard descrita no manual (`metric-created`, `metric-tested` etc.) nunca foi implementada no arquivo real — documentação e código divergentes. Resolvido pragmaticamente com um KPI simples no padrão já existente, em vez de construir a estrutura nunca implementada nesta rodada.
- [x] **Learning Agent:** pulado (não é segunda-feira).
- [x] **Livro-razão registrado:** Sim (Setembro.md, 3 entradas — pesquisa + auto-correção + Painel)

### Bloqueadores (se houver)

*Sem bloqueadores de execução. 1 falha transitória do md_to_pdf.py ao sobrescrever indice.pdf (resolvida no retry). Custo de token maior que o normal por causa da leitura obrigatória do artifact publicado (630 linhas) antes de poder republicar.*

### Retrabalho Evitado (se houver)

- **Item 1:** Presenton não duplicado (Skill de 28/08 já existe)
- **Item 2:** LuDattilo 138 tools não virou Skill isolada nova — atualização do achado já existente (24/08)
- **Item 3:** Autodesk APS Sample MCP descartado por critério 1 (paga)
- **Item 4:** Modly descartado por foco errado (geração de modelo 3D, não render de cena)
- **Item 5:** CAU-RJ — busca de setembro não achou deliberação nova, não forçou Skill
- **Item 6 (o mais importante):** Skill COSCIP quase publicada com alegação factualmente errada ("lacuna nunca coberta") — pega antes de qualquer ratificação, pela própria checagem do feed histórico ao preparar o Painel.

### Status Final

- **Rodada:** ✅ Completa — Seg-Qui + Sexta na mesma sessão
- **Taxa de Sucesso:** 1 Skill (corrigida) + 1 achado Vitruvius + 1 pendência nova aberta + Painel corrigido e republicado + 2 bugs estruturais achados e corrigidos (JSON quebrado, array manual obsoleto) — 100% do que foi tentado, com qualidade real (não só volume)
- **Marco:** Primeiro dia em que a própria rotina se auto-auditou e pegou um erro antes de publicar — precedente de processo, não só entrega de conteúdo
- **Próxima Rodada Recomendação:** (1) Hely apura o limiar de grupamento A-4/COSCIP (pendência nova, relevante ao caso Daniel-OB); (2) LuDattilo — testar coexistência de porta 8080 antes de decidir incorporação; (3) considerar parar busca de apresentação interativa até caso real forçar decisão (4 buscas sem novidade); (4) verificar se o array manual `pendencias` do Painel pode ser gerado automaticamente a partir de `pendencias.json` em vez de espelho manual — 2ª vez que diverge e vira trabalho de correção

---

## HISTÓRICO DE RODADAS

*Apenas os últimos 2-3 encerramentos para referência rápida*

### [2026-09-03] Diária Skills v2.7 — Seg-Qui (2 Skills)

- ✅ Entregou: **2 Skills Trilha A** (Resolução SMDU 10/2026 RDT — Legal; NBR 15575:2025 Desempenho Acústico Pisos — Complementares cross), 3 PDFs, +2 achados Vitruvius (BIMwright 229 tools + UV-Tech 40 tools)
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho evitado: NBR 9575/15220-3 não duplicadas, render cloud descartado, CAU-RJ fora de escopo não virou Skill
- 🎯 Status: **Completa** — NBR 15575:2025 pisos (prioridade #2) resolvida, Kelsen/Hely sobe para 3 Skills

### [2026-09-02] Diária Skills v2.7 — Seg-Qui (1 Skill)

- ✅ Entregou: **1 Skill Trilha A** (NBR 9575:2024 Impermeabilização cross-Saturnino/Baumgart/Tenreiro), 2 PDFs, índice Setembro atualizado
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho evitado: NBR 15220-3 não duplicada, Luw.ai descartado, RevitCortex não duplicado
- 🎯 Status: **Completa** — NBR 9575 (prioridade #1) resolvida

### [2026-09-01] Diária Skills v2.7 — Seg-Qui (2 Skills + RevitMCPBridge)

- ✅ Entregou: **2 Skills Trilha A** (NBR 15220-3:2024 zona 4A cross-Complementares + LC 281/2025 Legal), 4 PDFs, índice Setembro criado, RevitMCPBridge2026 registrado em vitruvius_achados
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho evitado: Leonardo AI/Runway ML/Midjourney descartados (freemium); Demolinator não duplicado
- 🎯 Status: **Completa** — pendência zoneamento 31/08 resolvida, Setembro inaugurado

---

## INSTRUÇÕES DE USO (histórica, do modelo pré-30/09/2026)

1. **Ao INICIAR rodada:** Leia "RODADA ANTERIOR" + "O QUE FICOU PENDENTE" + "O QUE NÃO FAZER"
2. **AO TERMINAR rodada:** Preencha "ESTA RODADA" (todos os campos)
3. **Ao formatar:** Mova "ESTA RODADA" para "HISTÓRICO" (após 48h de fechamento)
4. **Cada rodada lê isto:** para não repetir trabalho

*Substituída em 30/09/2026 pelo fluxo do Fechamento do Dia v1.0: o template ativo vive em `01_CEO/rotina_fechamento_template.md`, e este arquivo (`rotina_fechamento_historico.md`) recebe as rodadas que saem dele.*
