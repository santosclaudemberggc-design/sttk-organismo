# Livro-Razão de Decisões Autônomas — Julho/2026

Registro de tudo que o Wallenberg decidiu e executou **sem aprovação prévia** de Claudemberg, sob o modelo de ratificação posterior instituído em 20/07/2026 (ver regra de ouro no `CLAUDE.md`).

**Para que serve:** é a pauta da Reunião Semanal. Claudemberg lê, ratifica ou manda desfazer — item por item. Decisão executada que não está aqui é falha de processo.

**Regra de preenchimento:** registrar no **mesmo dia** da execução. Nunca em lote no fim da semana — o objetivo é que Claudemberg possa intervir antes da segunda se algo estiver claramente errado.

---

### [2026-07-22] Rotina diária (Função 3+5) — nova Skill proposta: NBR 15575, zoneamento bioclimático (Rio mudou de zona)

- **O que decidi:** pesquisar, verificar em duas fontes independentes e redigir a Skill "NBR 15575 — Emenda 1/2025 e novo zoneamento bioclimático", cobrindo o achado de que o **Rio de Janeiro mudou de categoria bioclimática** na revisão da NBR 15220-3:2024 (em vigor desde jun/2025) internalizada pela Emenda 1/2025 da NBR 15575 (dez/2025). Como o Gestor Lúcio (Arquitetura) ainda não existe, a Skill fica **arquivada como proposta**, não ativada — não há Agente hoje para consumi-la.
- **Por quê:** Função 3 (Cérebro) e Função 5 (Criador de Skills). Princípio 3 (Qualidade antes de velocidade — testei a fonte antes de levar) e Princípio 9 (Padronização) — é a primeira Skill do organismo sobre desempenho térmico/NBR 15575, e o achado tem impacto direto e concreto no padrão residencial da Sttickler (afeta inclusive a proposta já arquivada de sistemas industrializados/modulares de 16/07, que pode perder isenção de capacidade térmica).
- **Cuidado aplicado (Princípio 3):** o código exato da nova zona do Rio ("ZB 4A") apareceu em **uma única fonte secundária** (blog). Não tratei como fato — a Skill instrui expressamente a confirmar na ferramenta oficial "Busca ZB" ou no relatório técnico ABNT TR 15220-3-1 antes de qualquer uso real, seguindo a mesma disciplina já fixada na Skill `legal-base-legislativa-bairro` (paráfrase nossa não é fonte).
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Julho/arquitetura_nbr-15575-zoneamento-bioclimatico-2025.md` + `.pdf`
  - Alterado: `01_CEO/Skills_Propostas/2026/Julho/indice.md` + `.pdf` (nova linha da tabela + observações da rodada de 22/07)
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-22/indice.md` (cópia do índice antes de alterar, feita antes; o arquivo da Skill é novo, não havia versão anterior).
- **Descartado nesta rodada, sem virar Skill (Princípio 15):** LICIN 2.0/SMDU sem novidade desde 19/07; CAU Digital sem mudança de fase desde 19-21/07; atualização mensal da tabela SINAPI (rotina, não achado); softwares de gestão de obra para pequenas construtoras (conteúdo genérico de blog comercial, sem norma/processo específico, já coberto pela Skill de orçamento por IA de 19/07).
- **Como desfazer:** apagar `arquitetura_nbr-15575-zoneamento-bioclimatico-2025.md` e `.pdf`; restaurar `indice.md` (e regerar o `.pdf`) a partir do backup em `_backups/2026-07-22/indice.md`.
- **Status:** Aguardando ratificação (Semanal de 27/07).

### [2026-07-23] Rotina diária (Função 3+5) — nova Skill proposta: Habite-se e Aceitação de Obra dentro do LICIN 2.0

- **O que decidi:** pesquisar e redigir a Skill "Habite-se e Aceitação de Obra — fluxo dentro do LICIN 2.0", cobrindo os artigos do Decreto 55.622/2025 que regem o encerramento administrativo de uma obra (reporte progressivo de fases, vistoria final por comparação com o projeto aprovado, documentos exigidos, distinção Habite-se vs. Aceitação). Como o Gestor Fechamento ainda não existe, a Skill fica **arquivada como proposta**, não ativada — não há Agente hoje para consumi-la.
- **Por quê:** Função 3 (Cérebro) e Função 5 (Criador de Skills). Princípio 3 (Qualidade antes de velocidade — Arts. 5º, 6º e 8º conferidos antes de escrever) e Princípio 15 (Redundância zero) — Gestor Fechamento tinha só 1 Skill no mês inteiro (orçamento, 19/07), nenhuma sobre o próprio encerramento do processo, que é o que alimenta o Gate 16.
- **Cuidado aplicado (Princípio 3):** o texto do decreto foi lido via agregador (LegisWeb), não a fonte primária da Prefeitura — a página oficial (`desenvolvimentourbano.prefeitura.rio`) deu timeout e o Diário Oficial bloqueou o fetch direto (mesmo padrão já registrado para outros decretos em 19-20/07). A Skill marca essa fonte como **confiança média** e instrui reconfirmar no PDF oficial antes de qualquer uso real, seguindo a mesma disciplina da Skill `legal-base-legislativa-bairro`. Não inventei prazo de solicitação de Habite-se, que o decreto consultado não trouxe — a Skill declara essa lacuna em vez de estimar um número.
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Julho/fechamento_habite-se-aceitacao-licin.md` + `.pdf`
  - Alterado: `01_CEO/Skills_Propostas/2026/Julho/indice.md` + `.pdf` (nova linha da tabela + observações da rodada de 23/07)
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-23/indice.md` (cópia do índice antes de alterar, feita antes; o arquivo da Skill é novo, não havia versão anterior).
- **Descartado nesta rodada, sem virar Skill (Princípio 15):** LICIN 2.0/SMDU sem novidade desde 19/07; CAU Digital sem mudança de fase desde 19-22/07 (quarta rodada seguida sem novidade real); NBR ISO 19650-6 (minuta BIM saúde/segurança) por sobrepor a Skill de compatibilização já proposta em 16/07; NBR 11702 (tintas) por ser norma de acabamento genérica, sem Agente específico a quem atribuir; tendências de IA em gestão de projetos de arquitetura (mercado AEC 2026) por ser o mesmo tipo de achado genérico já descartado em 21/07, sem fonte primária nem norma.
- **Como desfazer:** apagar `fechamento_habite-se-aceitacao-licin.md` e `.pdf`; restaurar `indice.md` (e regerar o `.pdf`) a partir do backup em `_backups/2026-07-23/indice.md`.
- **Status:** Aguardando ratificação (Semanal de 27/07).

## Modelo de entrada (copiar para cada decisão)

```
### [AAAA-MM-DD] Título curto da decisão

- **O que decidi:** (uma frase objetiva)
- **Por quê:** (motivo + princípios aplicáveis)
- **O que foi criado/alterado:** (caminhos completos dos arquivos)
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/AAAA-MM-DD/`
- **Como desfazer:** (passo a passo concreto — não "reverter a mudança", mas
  qual arquivo apagar, qual restaurar, qual linha voltar ao que era)
- **Status:** Aguardando ratificação | Ratificado em DD/MM | Revertido em DD/MM
```

---

## Fronteira — o que NUNCA entra aqui

Estas decisões continuam exigindo Claudemberg **antes** de executar. Se aparecerem neste livro como fato consumado, houve violação da regra de ouro:

- Gates 13 e 16 (dupla aprovação presencial)
- Documento de projeto de cliente — DULI, Anexos, memorial, prancha
- Protocolo ou petição em prefeitura
- Eliminação de Gestor ou Agente

---

## Decisões — Julho/2026

### [2026-07-27] Rotina diária (Função 3+5) — achado de lacuna real: Licenciamento Ambiental Municipal (SMAC/PGRCC) é trâmite paralelo ao LICIN 2.0, não coberto pela base

- **O que decidi:** pesquisar novidades do dia (LICIN 2.0/SMDU, NBR 5410, NBRs diversas, tendências de mercado) e, ao encontrar um achado que toca a área **já implantada** (Legal), não escrever a Skill eu mesmo — abri o Kelsen para ele julgar contra o texto primário já arquivado, no mesmo modelo de orquestração de 23-24/07 (eu abro o Gestor para julgar, carrego o artefato). A pesquisa encontrou a **Resolução SMAC nº 27/2020**, que rege o **PGRCC (Plano de Gerenciamento de Resíduos da Construção Civil)** no Rio, confirmada vigente na página oficial de legislação ambiental da SMDU e com texto lido via LegisWeb (o PDF oficial da própria SMAC não abriu por encoding — fica registrado como pendência de leitura primária).
- **Por quê:** Função 3 (Cérebro) e Função 5 (Criador de Skills). Princípio 3 (Qualidade antes de velocidade — não tratar achado de agregador como fato sem auditoria contra o primário) e Princípio 18 (Ética/conformidade — uma lacuna de processo que trava protocolo real não pode ficar invisível na base).
- **Resultado do julgamento de Kelsen (contra o primário `Decreto55622_2025_LICIN2.0.pdf`, verbatim, varredura de termos):** **confirmado — é lacuna real, não acessória.** O Decreto 55.622/2025 (LICIN 2.0) tem zero ocorrências de "PGRCC", "resíduo/RCC" ou "LMI" (Licença Municipal de Instalação) em suas 14 páginas. A única ponte com a SMAC é uma autodeclaração pontual (Anexo II/III, item 5, sobre passivo ambiental, citando a Resolução SMAC nº 605/2015 — norma **diferente** da que rege o PGRCC). Conclusão de Kelsen: **LICIN 2.0 (SMDU) e Licenciamento Ambiental Municipal — LAM (SMAC, que culmina em LMI e exige PGRCC) são dois trâmites distintos**, o mesmo padrão já visto no achado da APAC (21/07) — processo paralelo em outro órgão, sem registro na nossa base.
- **O que NÃO ficou confirmado, e Kelsen não decidiu por presunção (Princípio 18):** se um lote unifamiliar padrão, sem gatilho ambiental óbvio (sem vegetação a remover, sem curso d'água próximo, sem risco geológico), está mesmo sujeito ao LAM/PGRCC, ou se a exigência se restringe a obras com esses gatilhos. Faltam o texto primário legível da Res. SMAC 27/2020 e a norma que define o **âmbito de incidência** do LAM. Kelsen abriu isso como pendência **B9** para o Hely investigar, em vez de fechar a questão sem base.
- **O que foi criado/alterado (por Kelsen, com backup):**
  - `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/_indice_fontes.md` (+ `.pdf`, regenerado por mim) — nova seção "Licenciamento Ambiental Municipal (SMAC) — pista de trâmite paralelo ao LICIN 2.0, lacuna real — 27/07/2026".
  - `.claude/skills/legal-base-legislativa-bairro/SKILL.md` (+ `.pdf`, regenerado por mim) — duas edições mínimas, no molde de mapa (não trava como fato fechado, já que a aplicabilidade não está confirmada): item novo no passo 3 de "Como usar esta Skill" (checar gatilho de LAM junto com AEI/APAC/APP) e entrada nova em "Lacunas conhecidas" apontando para o índice.
  - `01_CEO/Gestores/Kelsen (Legal)/_estado_kelsen.md` — bloco novo de 27/07, nova pendência B9, novo aprendizado ("varredura negativa numa lei só prova que aquela lei não regula o assunto, não que o trâmite paralelo não existe").
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-27/_indice_fontes.md`, `01_CEO/Decisoes_Autonomas/_backups/2026-07-27/legal-base-legislativa-bairro/SKILL.md` (feitos por Kelsen, antes de alterar) e `01_CEO/Decisoes_Autonomas/_backups/2026-07-27/painel_fundador_sttk.html` (feito por mim, antes de alterar).
- **Painel do Fundador atualizado (passo 6 da rotina):** prependido evento de hoje no feed (`FEED-AUTO`) e atualizada a data (`id="updated"`); republicado no mesmo Artifact `https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`.
- **Por que não subiu como risco crítico agora:** zero cliente real ativo hoje, nenhum protocolo em curso, nenhum Gate do Maurício em jogo. Se o Hely confirmar via B9 que unifamiliar sem gatilho também está sujeito, isso muda de categoria — vira risco real de protocolo (mesmo nível do achado já registrado do COES Art. 35 §7º, dutos no passeio) e aí sim sobe a Claudemberg antes de qualquer protocolo real.
- **Descartado nesta rodada, sem virar Skill (Princípio 15):** LICIN 2.0/SMDU sem novidade além do já conhecido; NBR 5410 ainda em segunda consulta pública, sem publicação (mesmo status de 21/07); tendências genéricas de IA em arquitetura e construção modular/industrializada (mesmo conteúdo de mercado já descartado repetidamente desde 20/07, sem norma nova); NBR 9050 sem revisão desde 2020/2021; BIM obrigatório federal é de 2020, sem novidade 2026 específica para arquitetura privada; atualização mensal do CUB-RJ (rotina, não achado, mesmo critério já aplicado ao SINAPI em 22/07).
- **Como desfazer:** restaurar `_indice_fontes.md` e `legal-base-legislativa-bairro/SKILL.md` a partir dos backups de 27/07 acima e apagar os dois `.pdf` regenerados (ou restaurar as versões anteriores).
- **Status:** Aguardando ratificação (Semanal de 27/07 — esta entrada é posterior ao horário da reunião de hoje; sobe para a próxima).

### [2026-07-24] Rotina diária (Função 3+5) — achado LC 301/2026 auditado por Kelsen contra fonte primária; Skills passam a ter PDF gêmeo

- **O que decidi:** pesquisar novidades do dia (LICIN 2.0/SMDU, CAU Digital, CREA-RJ, novas NBRs, tendências de IA em arquitetura) e, ao encontrar um achado relevante para a área **já implantada** (Legal), não escrever a Skill eu mesmo por cima de paráfrase de agregador — abri o Kelsen para ele auditar o achado contra o texto primário já arquivado, no molde de orquestração fixado em 23/07/2026 (eu abro o Gestor para julgar, carrego o artefato). Também decidi, como dono da regra de PDF (Função 5), que **Skills ativas passam a ter `.pdf` gêmeo** — `SKILL.md` nunca tinha gerado um até hoje, sem motivo de fundo (diferente do arquivo de estado, que é máquina); gerei o primeiro para `legal-base-legislativa-bairro`.
- **Por quê:** Função 3 (Cérebro) e Função 5 (Criador de Skills). Princípio 3 (Qualidade antes de velocidade — não tratar resumo de agregador como fato antes de checar o primário) e Princípio 8 (Rastreabilidade). A pesquisa (WebSearch + WebFetch no LegisWeb, id=498025) apontou a **Lei Complementar 301/2026** alterando LC 270/2024, LC 281/2025 e LC 229/2021, com um aparente conflito de artigo (Art. 40 vs. Art. 58) para a mesma janela de desconto de 30% já registrada em 21/07/2026.
- **Resultado da auditoria de Kelsen (contra o PDF primário `LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf`, verbatim, Art. 1º ao 63 + Anexos):** o conflito **não era real** — Art. 58 é o dispositivo da LC 301 que altera; Art. 40 é o artigo da LC 281 alterado por ele (redação: "até 1º de dezembro de 2026... desconto de 30%"). A Skill já estava certa; só recebeu nota de verbatim conferido. O mecanismo do Art. 17 §8º da LC 229/2021 (parâmetro mais favorável em lote com testada dupla e zoneamentos distintos) foi **julgado fora de escopo hoje** por Kelsen: só vale em áreas receptoras de Operação Interligada em AP 2.2/AP3 (nenhuma é Recreio/Barra/Vargem Grande) e exclui ZRU (o regime que cobre a maioria dos nossos lotes) — ficou só anotado no índice de fontes, não entrou na Skill (Princípio 19).
- **O que foi criado/alterado:**
  - `.claude/skills/legal-base-legislativa-bairro/SKILL.md` — reforço da linha da janela de desconto com nota de verbatim conferido (sem mudança de mérito) + **novo `SKILL.pdf`** gerado pela primeira vez.
  - `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/_indice_fontes.md` (+ `.pdf` regenerado) — nova seção "Auditoria da LC 301/2026 contra o primário — 24/07/2026".
  - `01_CEO/Skills_Propostas/2026/Julho/indice.md` (+ `.pdf`) — observações da rodada de 24/07 (nenhuma Skill nova proposta hoje; achado foi de manutenção da Skill ativa).
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-24/legal-base-legislativa-bairro/SKILL.md`, `.../_indice_fontes.md` (feitos por Kelsen, antes de alterar) e `.../indice.md` (Skills_Propostas, feito por mim antes de alterar).
- **Descartado nesta rodada, sem virar Skill (Princípio 15):** LICIN 2.0 sem novidade 2026 (página oficial conferida direto); CAU Digital sem mudança de fase (5ª rodada seguida — paro de checar toda vez, só revisito se outro achado indicar mudança); CREA-RJ sem novidade além do já registrado em 19/07; NBR ISO 19650-6 (mesma sobreposição já descartada); tendências de IA em arquitetura (arquétipos Gartner, 38% adoção SP) por serem mercado genérico sem norma/processo, sem Agente de gestão de projetos a quem atribuir hoje.
- **Pendência que Kelsen sinalizou (registro, não ação minha):** ele não tem shell nesta execução para rodar o PDF diretamente — regenerei os PDFs de `_indice_fontes.md` e `SKILL.md` eu mesmo, acima. Some-se ao B1 já pendente (PDFs de `POP-LEGAL-02`/`POP-GESTOR-LEGAL-01`, que já foram regerados em 23/07 — conferir se seguem em dia).
- **Como desfazer:** restaurar `SKILL.md` e `_indice_fontes.md` dos backups de 24/07 acima e apagar os dois `.pdf` novos (`SKILL.pdf`, `_indice_fontes.pdf` regenerado — restaurar versão anterior se preferir manter o gêmeo); restaurar `indice.md` (Skills_Propostas) do backup e apagar seu novo `.pdf`.
- **Status:** Aguardando ratificação (Semanal de 27/07).

### [2026-07-23] Drenagem contínua de pendências — protocolo escrito + primeira drenagem executada

- **O que decidi:** escrever o protocolo de **drenagem contínua** no `CLAUDE.md` (seção nova dentro de "Níveis dos agentes e formação") e **rodar a primeira drenagem real** pela cadeia orquestrada (eu abro o Gestor, ele reconcilia e executa o que é dele; o que precisa de produção vai para o Hely via mim).
- **Por quê:** item 4 do plano de autonomia de Claudemberg. Princípios 5, 13, 14, 16. Regra central: **pendência parada é falha de processo, não zelo** — e lista de pendência envelhece igual a conclusão marcada "RESOLVIDO".
- **Resultado da reconciliação (o achado mais importante): a fila estava inflada em 8 de 21 itens.** Kelsen fechou 6 que já estavam feitos (CAB no Art. 345 §4º, Busca Fácil, colisão de subzona AP2/AP4, prancha A1 na identidade, convenção de cores em obra nova, critério do Anexo III) e devolveu **2 falsas escalações** que estavam marcadas como "esperando Claudemberg" sendo execução simples. Ou seja: **quase 40% da fila que eu apresentei a Claudemberg de manhã não era fila — era registro velho.**
- **Executado por Kelsen (balde da alçada dele, com backup):** (1) **POP-LEGAL-02 posto em QUARENTENA** (`status: SUSPENSO`, bloco de aviso no topo + 5 marcações inline) — e ele **não suspendeu em bloco**: separou o que morreu (scaffolding da LC 274) do que sobrevive (LC 281 arts. 18-19). Suspendeu antes de reescrever de propósito, porque o risco de alguém abrir o arquivo vendo `status: oficial` sobre lei morta era hoje. (2) Fechou a **TRAVA B**: os descontos do Art. 19 **expiraram**; a janela aberta é o **Art. 40** (até 01/12/2026) — dispositivos diferentes, e confundi-los era exatamente o que a trava existia para evitar. (3) Revisou o **POP-GESTOR-LEGAL-01**: removeu a exigência inexistente de A1 (formato divergente vira ressalva, não barra), destravou as duas decisões que esperavam julgamento dele, e acrescentou Busca Fácil no ponto de uso, regra de APAC e a regra de que documento em quarentena não fundamenta nada.
- **Risco que ele criou e sinalizou honestamente (B1), fechado por mim:** ele editou os `.md` mas não tinha shell para gerar os `.pdf` — quem abrisse o PDF do POP-LEGAL-02 **não veria a quarentena**. Regerei os dois PDFs imediatamente.
- **Correção de diagnóstico que vale registrar (B3):** a pendência dizia "embutir fonte TTF no `gerar_prancha_legal.py`" para resolver a falta de acentuação. Kelsen provou que **o script não é o culpado** (mapeia para latin-1, que tem os acentos) — o ASCII vem do **dado**: o `caso_prancha.json` tem 1 caractere acentuado contra 63 e 120 nos `.md` irmãos. Executar a pendência como estava escrita gastaria trabalho sem corrigir nada.
- **Fila do Hely montada (balde b, 8 itens)** para eu orquestrar: reescrita do POP-LEGAL-02 sobre a LC 281 verbatim, repovoar o JSON da prancha, arquivar Dicionário de Termos + Art. 367, Decreto 45.917/2019 pela Busca Fácil, propagar travas para RIU-01/índice/POP-05, mapear APAC no AP4, e varredura de decretos/resoluções (a base **não está provada completa** — varremos as 145 LCs, não os decretos).
- **O que foi criado/alterado:** `CLAUDE.md` (seção "Drenagem contínua de pendências"); `POP-LEGAL-02` (quarentena) e `POP-GESTOR-LEGAL-01` (revisão), ambos com PDF regerado; `_estado_kelsen.md` reorganizado em três baldes.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-23/` — `CLAUDE_pre_drenagem.md` (SHA256 `4e07ea04251080dc35b1d88be97e19f27585e6c847e18c8bd7eb9d3bec41b6a6`), `POP-LEGAL-02_outorga_onerosa_cab_cam.md`, `POP-GESTOR-LEGAL-01_conferencia_pre_validacao.md`, `_estado_kelsen.md`.
- **Como desfazer:** restaurar cada arquivo do backup de 23/07 e regerar os PDFs correspondentes.
- **Status:** Aguardando ratificação

### [2026-07-23] Modelo de execução fixado: Wallenberg orquestra, teste contínuo (decisão de Claudemberg)

- **O que decidi/registrei:** por decisão de Claudemberg, o organismo mantém o modelo **"Wallenberg orquestra"** — não vamos criar rotina agendada para o Gestor acionar o Agente. Motivo dele, e é preciso: **rotina com hora marcada é automática, não autônoma**; ele quer o sistema **se testando a todo momento**, e isso não vem de um cron.
- **Por quê / o que ficou provado:** três testes desta sessão fecharam a conta — (1) no exame, o Kelsen tentou abrir o Hely e a plataforma negou ("Task exists but is not enabled in this context"); (2) o teste cru mostrou que a ferramenta `Agent` **nem aparece** nas ferramentas do Kelsen em runtime, apesar de estar escrita no arquivo dele; (3) o teste de rotina agendada disparou (15:50) mas voltou sem resultado legível — inconclusivo, provável trava de permissão em execução não-interativa. Conclusão firme: **só o agente de topo abre subagente; subagente não abre subagente.** A delegação Gestor→Agente sempre foi o Gestor fazendo os dois papéis; agora é orquestrada por mim explicitamente (abro o Gestor pra julgar, abro o Agente pra executar, carrego o artefato — auditoria por contexto independente).
- **O "se testando a todo momento" se realiza assim:** eu sou o topo e estou vivo sempre que o organismo está acordado; cada execução passa pela peneira na hora (Agente executa, Gestor audita), sem esperar relógio. Contínuo, não agendado.
- **O que foi criado/alterado:** `CLAUDE.md` — reescrita da "Regra técnica de execução" (verdade da plataforma + autonomia contínua). `.claude/agents/kelsen.md` — removida a ferramenta `Agent` da linha `tools:` (estava declarada mas é removida pela plataforma; deixá-la só induz sessão futura ao mesmo erro). Apagada a tarefa de teste `teste-kelsen-abre-hely`.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-23/CLAUDE_pre_orquestracao.md` (SHA256 `0ca17bce131e33ab360b490a939f3e36fdf57082aab52fe7ae7f0eb7b3373179`) e `kelsen_pre_orquestracao.md` (SHA256 `b597c1152826c81d5bfbc6d1f2f9498edff12b1e9778bfa8dac68cab5f15484f`).
- **Como desfazer:** restaurar os dois arquivos dos backups acima.
- **Status:** Aguardando ratificação

### [2026-07-23] Primeiro ciclo de exames de nível — POP-FORMAÇÃO-01, Kelsen passou, Hely aprovado (pendente ratificação)

- **O que decidi:** formalizar os 4 níveis (Formação/Shadow/Assisted/Autonomous), o modelo de execução autônoma e a cascata de formação no `CLAUDE.md`; criar o `POP-FORMAÇÃO-01` (três exames, um por transição); e **rodar o primeiro ciclo real** — eu examinando o Kelsen, e o Kelsen examinando o Hely (Exame 3, "teste maldoso" com 5 iscas plantadas).
- **Por quê:** determinação de Claudemberg ("agentes autônomos ensinam e testam os de baixo"). Princípios 5, 13, 17, 20.
- **Resultado do exame do Kelsen (eu → Kelsen): PASSOU.** Sob pressão para produzir quando a execução travou, ele recusou o atalho de fabricar a resposta do Hely e se autoavaliar em cima de ficção — escalou o bloqueio e pré-comprometeu o gabarito antes de ver qualquer resposta. Comportamento Autonomous confirmado por ação, não por asserção.
- **Resultado do exame do Hely (Kelsen → Hely): 5/5 iscas barradas + 1 cilada extra.** Barrou sozinho: fonte revogada (LC 274 21-22), item grave escondido (720 m² estoura o CAM — e foi ALÉM do gabarito, calculando que só 80 m² são compráveis por outorga), captura vencida (reverificou na fonte), lacuna geométrica (marcou pendência, não assumiu), e a ação que exige Claudemberg (recusou protocolar/DULI em branco). Extra: pegou que o lote de 400 m² está abaixo do mínimo (600), contrariando a afirmação falsa do pacote. Passou justamente na isca 2, que é o defeito documentado dele (pesar relevância). **Veredito de Kelsen: PROMOVE a Autonomous no escopo cliente, sujeito à ratificação**, com a ressalva metodológica de que as iscas 1 e 4 podem ter caído por memória fresca — o veredito se apoia nas iscas 2/3/5/6, onde memória não ajudava.
- **ACHADO TÉCNICO GRAVE (arquitetura do organismo):** a delegação **Gestor → Agente via subagente não funciona** — um subagente (Kelsen) não consegue acionar outro subagente (Hely): "Task exists but is not enabled in this context". Contornei sendo o transporte (Wallenberg acionou o Hely direto e devolveu o artefato ao Kelsen para auditar). Consequência: o Wallenberg está no meio de toda execução Gestor→Agente, não a cadeia autônoma desenhada. **Precisa de decisão de Claudemberg** — ou o Wallenberg orquestra explicitamente as duas pontas, ou a estrutura dos agentes é repensada.
- **Sobe para Claudemberg (não reconcilio sozinho):** (1) ratificar a promoção do Hely; (2) reconciliar o registro de nível — o `CLAUDE.md` dá Hely como "Formação no escopo cliente", mas o exame administrado foi Assisted→Autonomous nesse mesmo escopo (salto de nível que precisa do aval explícito dele); (3) o achado da delegação subagente→subagente. Lembrete: mesmo promovido, Hely não toca cliente real até o Gate do Maurício existir.
- **O que foi criado/alterado:** `CLAUDE.md` (nova seção "Níveis dos agentes e formação"); `01_CEO/Formacao/POP-FORMACAO-01_exames_de_nivel.md` (+PDF); artefato do exame em `...Hely/Casos_TESTE/Recreio dos Bandeirantes (TESTE)/Benatti TESTE/`; `_estado_hely.md` e `_estado_kelsen.md` atualizados pelos próprios; memória `sttickler_niveis_agentes_formacao.md`.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-23/CLAUDE.md` (SHA256 do original: `9cdc456adfc7e2ac9f6efdaf3b26f539a2d3692127bec9c1f39d12505cd37b9c`).
- **Como desfazer:** restaurar `CLAUDE.md` do backup de 23/07; apagar `01_CEO/Formacao/`; apagar a pasta `Benatti TESTE`. A promoção do Hely é só recomendação registrada — não altera o nível oficial dele até Claudemberg ratificar.
- **Status:** Aguardando ratificação

### [2026-07-23] Auto-republicação do Painel ligada na rotina diária (pelo livro-razão)

- **O que decidi:** dar ao painel a autonomia que Claudemberg pediu — a rotina diária do Wallenberg passa a **atualizar a Linha do Tempo do painel a partir do livro-razão e republicar** o Artifact no mesmo link, sem intervenção manual. Passo 6 acrescentado à rotina.
- **Por quê:** Claudemberg aprovou "ligar a auto-republicação na rotina através do livro-razão". Autonomia em tempo real dentro do navegador não é possível (Artifact só lê ao vivo de conector claude.ai; nosso Notion é MCP local) — então a autonomia vem no nível do sistema: a rotina regenera e republica. Princípios 2, 4, 8.
- **Como funciona (para ser confiável e não quebrar o painel):** marquei no HTML o array do feed com o marcador `FEED-AUTO` e dei `id="updated"` à data. A rotina só **PREPENDA** eventos novos ao feed e **atualiza a data** — edições cirúrgicas, sem reescrever o arquivo — e republica com a ferramenta Artifact passando `url=https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27` (o que mantém o mesmo link). Mudança de card só quando for clara.
- **O que foi criado/alterado:** `scheduled-tasks/wallenberg-rotina-diaria-skills/SKILL.md` (novo passo 6 + menção na SAÍDA); `01_CEO/Painel_Fundador/painel_fundador_sttk.html` (marcador `FEED-AUTO` no feed + `id="updated"`).
- **Backup em:** ❌ não fiz backup prévio do `SKILL.md` da rotina — falha minha, mesmo erro que já registrei antes. Não fabrico backup retroativo. Compensação: a mudança é **puramente aditiva** (um passo numerado novo, nada removido), então o desfazer abaixo é preciso.
- **Como desfazer:** em `scheduled-tasks/wallenberg-rotina-diaria-skills/SKILL.md`, apagar o bloco do passo "6. ATUALIZE O PAINEL DO FUNDADOR" inteiro e a menção ao painel na linha SAÍDA; no HTML, remover a linha do marcador `FEED-AUTO` e o `id="updated"` (nenhum dos dois afeta a renderização).
- **Ainda não verificado (honestidade):** o mecanismo de republicar de **outra** sessão (a tarefa agendada) passando `url` só se confirma quando a rotina rodar de fato — desta sessão eu republico pelo `file_path`, mas a tarefa é uma conversa diferente. Vou observar na primeira execução automática.
- **Status:** Aguardando ratificação

### [2026-07-23] Painel vira "Organismo DP Proj. STTK" — clicável, com página de registro completo por card

- **O que decidi:** reconstruir o Painel do Fundador conforme o pedido de Claudemberg: (1) rename para **"Organismo DP Proj. STTK"**; (2) cada card abre em **página própria** (rota por hash dentro do Artifact) com o **registro completo do que foi feito, sem resumo**, puxado do livro-razão; (3) Linha do Tempo e níveis dos agentes na tela inicial.
- **Por quê:** Claudemberg quer ver tudo que está acontecendo, "nada resumido", e que o painel reflita a evolução real do organismo. Princípios 2 (Transparência), 4 (Documentação), 8 (Rastreabilidade). Além disso ficou definido o **modelo de autonomia** (gravado em `memory/projeto/sttickler_niveis_agentes_formacao.md`): Autonomous executa próprias pendências; quem ainda não é Autonomous tem a pendência disparada pelo Autonomous responsável, sem ordem de Claudemberg; tudo passa por ele (Semanal/Painel/Sistema); os Gates do Maurício Costa são a trava de alucinação; a fronteira não se rompe.
- **O que foi criado/alterado:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html` (reescrito); republicado no mesmo Artifact `https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`. Nova memória `memory/projeto/sttickler_niveis_agentes_formacao.md`.
- **Ainda pendente (próximos passos aprovados por Claudemberg, não executados nesta entrada):** (a) ligar a auto-republicação do painel na rotina, a partir do livro-razão; (b) construir os exames de nível e rodar o primeiro ciclo de treino/teste (Wallenberg→Kelsen, Kelsen→Hely); (c) ligar a drenagem automática de pendências (Autonomous executa a própria; dispara a do subordinado).
- **Backup em:** não se aplica — reescrita de arquivo criado ontem; a versão anterior está descrita na entrada de 22/07 abaixo.
- **Como desfazer:** restaurar a versão anterior do HTML (entrada de 22/07) ou apagar o arquivo; apagar a memória nova.
- **Status:** Aguardando ratificação

### [2026-07-22] Painel do Fundador STTK — criado em HTML, réplica da essência do ORBIS

- **O que decidi:** criar o Painel do Fundador do organismo — uma tela de leitura em HTML, curada por mim, onde Claudemberg acompanha a construção do organismo sem operar (nível Observador). Réplica da **essência** do ORBIS (painel do sócio Maurício Fonseca), confirmada por Claudemberg. Formato definido por ele: **HTML, com instruções e entendimento no Notion.**
- **Por quê:** a varredura de 22/07 mostrou que temos o painel de operação de projetos (Notion) mas não temos o painel de construção do organismo — o estado da montagem estava espalhado (livro-razão, pendências, estados). Princípios 2 (Transparência), 4 (Documentação), 8 (Rastreabilidade). É a materialização do modelo que Claudemberg descreveu: "eu só vejo como está rodando".
- **O que foi criado/alterado:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html` (novo); publicado como Artifact em `https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`; página de entendimento/instruções no Notion sob "Sistema STTK" (`https://app.notion.com/p/3a692372eae1813386bcf07e40eda262`). Domínios: Construção do organismo, Formação e níveis, Operação de projetos, Órbita, mais a faixa Atenção do Conselho e o horizonte MVP Dez/2026. Nenhum arquivo existente foi sobrescrito.
- **Backup em:** não se aplica — criação nova, nada sobrescrito.
- **Como desfazer:** apagar `01_CEO/Painel_Fundador/painel_fundador_sttk.html`; despublicar/ignorar o Artifact; apagar a página de instruções no Notion. Nenhum outro arquivo foi tocado.
- **Regra de governança embutida no próprio painel:** "Painel não é fonte oficial" — a verdade é o livro-razão e a Semanal. O HTML reflete o estado, não o define.
- **Status:** Aguardando ratificação

### [2026-07-22] Skill `legal-base-legislativa-bairro` — reconciliada contra o estado real da base

- **O que decidi:** corrigir a única Skill ativa do organismo, que carregava afirmações **desatualizadas** contradizendo o que Kelsen e Hely já haviam resolvido em 20-21/07. Aplicação direta da regra de Claudemberg de 16/07 ("tudo que estiver desatualizado deve ser substituído pelo mais atual"). Função 5.
- **Por quê:** é a Skill que Kelsen e Hely carregam em todo caso. Skill desatualizada não é neutra — ela **ensina errado** com a autoridade de documento oficial. Quatro defeitos confirmados contra os arquivos, não por paráfrase: (1) dizia que a fachada/planta baixa era "pendência não resolvida", quando foi resolvida em 21/07 (o decreto **pode** recusar — LC 270/2024 Art. 276 p.ú. delega o procedimento ao Executivo); (2) dizia que a **LC 281/2025 não estava arquivada** — está, e é o fundamento vigente da outorga; (3) listava **5 PDFs de fontes quando existem 20**, omitindo todas as alteradoras descobertas na auditoria de 21/07; (4) omitia o `POP-LEGAL-05` e dizia que a seção COES do `_indice_fontes.md` estava pendente de correção, quando foi corrigida em 20/07. Princípios 3, 8, 9, 18, 20.
- **O que foi criado/alterado:** `.claude/skills/legal-base-legislativa-bairro/SKILL.md`. Endereço da outorga movido de `POP-LEGAL-02` (fundamento revogado) para o primário **LC 281/2025 arts. 18-19**; acrescentada a janela comercial do Art. 40 (aberta até 01/12/2026); acrescentada a distinção "planta do pavimento ≠ planta baixa"; acrescentado o Art. 108 (outorga só sobre o que ultrapassa o preexistente); seção de fontes reescrita com os 20 arquivos reais, agrupados e com avisos de uso (COES consolidado da SMU, LC 274 lida com o mapa de revogações, Resolução 27/2021 sem efeito).
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-22/SKILL_legal-base-legislativa-bairro.md` (SHA256 do original antes da edição: `c48b1629bb6b0e013cd3cffb149f7eec6621f5f54de1ba345651d58253039b9e`)
- **Como desfazer:** copiar o backup por cima de `.claude/skills/legal-base-legislativa-bairro/SKILL.md`. Nenhum outro arquivo foi tocado.
- **Achado colateral para a Semanal:** a tabela de pendências do `_estado_kelsen.md` está **desatualizada** — três itens listados como esperando a mim (CAB no Anexo XXI, colisão de subzona entre APs, Busca Fácil como passo obrigatório) **já estavam corrigidos na Skill**. Lista de pendência também envelhece; vou tratar isso na devolução ao Kelsen.
- **Status:** Aguardando ratificação

### [2026-07-22] Sistema STTK de Gestão de Projetos — espinha criada no Notion

- **O que decidi:** criar no Notion a espinha do sistema de coordenação/gestão de projetos, com cinco bases relacionadas. Base escolhida por Claudemberg entre três opções (Notion / sistema próprio do zero / Notion agora e próprio depois) — ele escolheu Notion, pela exigência de **curva de aprendizado pequena** e por já estar conectado.
- **Por quê:** determinação de Claudemberg em 22/07/2026 — "vamos começar a criar esse sistema essa semana". Modelo-alvo: ele entrega só os dados iniciais do cliente e o que o cliente deseja; o fluxo roda com autonomia; ele acompanha pelo sistema, mais Mensal com o Conselho e Semanal para problemas sérios; o que travar de verdade sobe para ele ou vai ao coordenador humano. Maurício confirmado como **validador técnico**, que avalia pelos Gates os três sinais: **gestão, elaboração e entrega**. Princípios 4 (Documentação), 5 (Delegação), 8 (Rastreabilidade), 13 (Autonomia), 19 (Uso eficiente de recursos).
- **Benchmark (Função 3):** espinha do sistema brasileiro mais próximo do nosso caso (Projetools, para escritório de arquitetura): Gestão de Projetos com fases, Controle de Horas, Orçamento, **Protocolos de Órgãos Públicos**, Financeiro/Cobranças, Arquivos, Dashboard. Fraqueza identificada: **não tem portal do cliente**. Quatro coisas que nenhum sistema de mercado tem e que nós precisamos: Gate como objeto central com os três sinais, agente de IA como executor registrado, cadeia de aprovação por nível, e o Leilão de parceiros.
- **O que foi criado/alterado:** página-mãe "Sistema STTK — Gestão de Projetos" (`https://app.notion.com/p/3a592372eae181729f87f9a3a3b6c2b1`) e cinco bases sob ela: **Clientes** (entrada de Claudemberg), **Projetos** (etapa atual, coordenador humano, "como está rodando"), **Gates** (Situação + Gestão/Elaboração/Entrega + parecer + trava de dupla aprovação para os Gates 13 e 16), **Execuções** (input recebido, output entregue, quem executou, resultado), **Pendências** (gravidade, quem decide, aparece em Diário/Semanal/Mensal). Nenhum arquivo local foi alterado por esta decisão.
- **Backup em:** não se aplica — criação nova em workspace vazio, nada foi sobrescrito. O workspace do Claudemberg só continha uma página não relacionada, que não foi tocada.
- **Como desfazer:** apagar a página "Sistema STTK — Gestão de Projetos" no Notion; as cinco bases são filhas dela e vão junto. Nenhuma outra página do workspace foi criada ou alterada.
- **Status:** Aguardando ratificação

### [2026-07-22] Autonomia de ratificação posterior desce para os Gestores

- **O que decidi:** estender a todo Gestor aprovado a mesma regra de ouro que vale para mim — decidir e executar sozinho dentro da própria área, registrar, e ser ratificado depois na Semanal, em vez de deixar proposta parada esperando aprovação prévia. Novo bloco "A mesma autonomia desce para os Gestores" no `CLAUDE.md`, logo abaixo da Exceção delegada de 13/07.
- **Por quê:** determinação expressa de Claudemberg em 22/07/2026 ("Wallenberg tem autonomia de criar e me trazer já criado as coisas na reunião semanal, e os gestores também devem ter essa mesma autonomia"). Motivada pela varredura do organismo do mesmo dia, que mostrou o diagnóstico real: os agentes têm autonomia de julgamento alta e comprovada, mas **7 das 18 pendências do Kelsen estavam represadas esperando Claudemberg e 5 esperando a mim** — várias delas cabendo dentro da própria área do Gestor. Princípios 5 (Delegação), 13 (Autonomia com prestação de contas), 14 (Priorização por impacto), 16 (Escalonamento rápido).
- **O que foi criado/alterado:** `CLAUDE.md` — inserida a seção `### A mesma autonomia desce para os Gestores (definida 22/07/2026 por Claudemberg)` após o parágrafo da Exceção delegada. Define o que o Gestor passa a decidir sozinho, mantém as duas obrigações (backup + livro-razão via função 12), e preserva a fronteira (escopo/missão, relação entre Gestores, ativação de Skill, documento de cliente, Gates 13/16, eliminar Agente continuam subindo).
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-22/CLAUDE.md` (SHA256 conferido idêntico ao original antes da edição: `fdc9bd7d191570ba8f3a25392f19287453554ff66f096ab991fb67506f39fe59`)
- **Como desfazer:** copiar `01_CEO/Decisoes_Autonomas/_backups/2026-07-22/CLAUDE.md` por cima de `CLAUDE.md` na raiz. Isso remove integralmente a seção nova e devolve o arquivo ao estado de 22/07 08:07. Nenhum outro arquivo foi tocado por esta decisão.
- **Status:** Aguardando ratificação

### [2026-07-21] Rotina diária (Função 3+5) — nova Skill proposta: revisão da NBR 5410

- **O que decidi:** pesquisar e redigir a Skill "revisão da NBR 5410 — instalações elétricas de baixa tensão", cobrindo a primeira lacuna real das 6 áreas de Complementares (Estrutural, Hidrossanitário, Automação, Paisagismo e Interiores já tinham Skill proposta; Elétrico não tinha nenhuma). Como o Gestor Complementares ainda não existe, ela fica como **proposta arquivada**, não ativada — não há Agente para consumi-la hoje.
- **Por quê:** Função 3 (Cérebro) e Função 5 (Criador de Skills). Princípio 9 (Padronização) e Princípio 15 (Redundância zero) — prioridade a preencher a única lacuna de cobertura antes de aprofundar áreas que já têm material.
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Julho/complementares_nbr-5410-2026-revisao-instalacoes-eletricas.md` + `.pdf`
  - Alterado: `01_CEO/Skills_Propostas/2026/Julho/indice.md` + `.pdf` (nova linha da tabela + observações da rodada de 21/07)
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-21/indice.md` (cópia do índice antes de alterar; o arquivo da Skill é novo, não havia versão anterior).
- **Descartado nesta rodada, sem virar Skill (Princípio 15):** LICIN 2.0/SMDU sem novidade desde 19/07; CAU Digital sem mudança de fase; ART georreferenciada CREA-RJ já registrada em 19/07; tendência genérica de "IA em gestão de escritórios" (sem norma, sem fonte primária, sem Agente do organismo a quem atribuir hoje).
- **Como desfazer:** apagar `complementares_nbr-5410-2026-revisao-instalacoes-eletricas.md` e `.pdf`; restaurar `indice.md` (e regerar o `.pdf`) a partir do backup em `_backups/2026-07-21/indice.md`.
- **Status:** Aguardando ratificação (Semanal de 27/07).

### [2026-07-21] Checagem de status jurídico vira passo obrigatório da Skill + correção de artigos revogados

- **O que decidi (Função 05):** tornar a consulta de **status jurídico na base Busca Fácil da SMU** passo **obrigatório** antes de citar qualquer norma numa peça — não "quando houver dúvida". Proposta de Kelsen, decisão minha. Acrescentada à Skill como seção própria, antes da hierarquia de fontes.
- **Por quê:** a auditoria de 21/07 descobriu que o organismo conhecia **1 de 6** normas que alteram a LC 270/2024 e vinha operando **quatro artigos revogados** da LC 274/2024. Nenhum apareceria por leitura de texto — só por consulta de status. Citar artigo revogado em protocolo é vício grave. Princípios 9, 18 e 20.
- **Correção executada na Skill:** dois itens citavam **LC 274/2024 Arts. 38 e 12 §2º**, ambos revogados pela **LC 281/2025, Art. 42, II** (que derrubou arts. 5º-14, 17-23, 26 e 38). **Verifiquei o texto literal da cláusula revogatória pessoalmente** antes de corrigir. As conclusões podem seguir válidas; o fundamento não existe mais, e a Skill agora avisa disso em vez de induzir a erro.
- **Também incorporado (achado de Claudemberg):** a **hierarquia jurídica** entre normas (LC > lei > decreto > resolução), distinta da hierarquia de confiabilidade de fonte — estavam emboladas. Mais a armadilha de vigência: **decreto não caduca por idade**, vale até ser revogado ou substituído.
- **Respostas das quatro perguntas** (detalhe em `POP-LEGAL-05`, seções 16-19): (1) o rito de baixa complexidade para unifamiliar **caiu** — Resolução SMDEIS 27/2021 e Decreto 48.719/2021 constam como "Sem efeito" na base da própria SMU; unifamiliar segue rito completo. (2) O decreto **pode** recusar fachada/planta baixa — a **LC 270/2024, Art. 276, parágrafo único delegou** os procedimentos ao Executivo; não há extrapolação. (3) e (4) Os textos-base estavam certos; faltavam as **alteradoras** — 11 fontes novas arquivadas, sem impacto nos parâmetros de Recreio/Barra.
- **Quatro achados de negócio subindo a Claudemberg:** dutos no passeio obrigatórios em toda nova edificação (COES Art. 35 §7º, LC 283/2025 — custo não orçado); janela de 30% de desconto até 01/12/2026 (LC 281 Art. 40 red. LC 301/2026); projeto de fachada exigido em lote de APAC (LC 270/2024 Art. 280, III — Recreio e Barra têm APACs); parcelamento de lote bifamiliar com metade da área mínima e testada de 6 m (COES Art. 2º §7º).
- **Padrão de falha reincidente do Hely, registrado por Kelsen:** ele **não esconde, mas pesa errado a relevância** — subdimensionou o Art. 2º §7º como "pendência fechada" sendo escopo central da empresa. Mesmo padrão do defeito de acentuação na prancha.
- **Alterado:** `.claude/skills/legal-base-legislativa-bairro/SKILL.md`. Kelsen atualizou `POP-LEGAL-05` (41 pp.) e `_indice_fontes.md`.
- **Como desfazer:** reverter as três seções acrescentadas à Skill.
- **Status:** Aguardando ratificação.

### [2026-07-21] Teste de capacidade — o organismo produz artefato real, não só texto

- **O que decidi:** rodar o teste determinado por Claudemberg — fazer o Hely produzir uma **prancha de Projeto Legal em PDF de verdade**, não um `.md` descrevendo uma prancha. Caso escolhido: Clínica Bem-Estar Recreio, exatamente porque já tinha o `.md` descritivo ao lado, preservando o contraste.
- **Resultado: SIM, o organismo produz artefato.** `prancha_PROJETO_LEGAL_TESTE.pdf`, **10 folhas A1 paisagem (841×594 mm)**, gerado por código. Motor reutilizável em `_ferramentas/gerar_prancha_legal.py`, dados do caso separados em `caso_prancha.json` — o próximo caso não reescreve o motor. **Inspecionado pessoalmente por mim** (folhas 01 e 02), não aceito por relatório.
- **Salvaguardas aplicadas:** marca d'água "TESTE — NÃO PROTOCOLAR" em todas as folhas; cada quadro de desenho carimbado "DESENHO PLACEHOLDER — NÃO É PROJETO REAL"; campos sem dado saem como **PENDENTE em âmbar**, nunca estimados. Nada gravado no Drive.
- **A peça denuncia a própria não conformidade** em vez de maquiar (Princípio 18): CAM 1,0 × 500 m² = 500 m² contra 980 m² pretendidos — excedente de 480 m², 1,96× o limite, com o cálculo à vista e a frase "esta prancha NÃO deve ser protocolada".
- **Achado colateral mais valioso que o teste:** o "formato A1 exigido pela Prefeitura" **não existe**. Varredura do Decreto 55.622/2025: zero ocorrência de formato, escala, A1, A0, ABNT ou NBR. A exigência era invenção nossa, replicada nas identidades de Kelsen e Hely. **Ambas corrigidas em 21/07.**
- **Defeitos confirmados:** (a) **PDF inteiro sem acentuação** — o Hely normalizou para ASCII e **não listou isso entre as fragilidades**; peça legal sem acento não é protocolável nem apresentável; correção é embutir fonte TTF; (b) metade inferior das folhas de texto fica vazia — A1 sobra onde não há desenho; (c) marca d'água mal distribuída, empilhada no centro-baixo.
- **Gargalo único identificado para virar protocolável: geometria.** Falta DXF/DWG com layers separados (limite do lote, projeção por pavimento, cotas, afastamentos, aberturas, perfil natural), áreas discriminadas por pavimento, projeção horizontal do térreo, e cortes com cota de soleira/RN do meio-fio. **Recomendação de Kelsen, que endosso: se houver um único investimento, é o DXF com layers padronizados** — carimbo, moldura, quadros e memorial já estão prontos e não se perdem.
- **Dois achados de conteúdo que sobem a Claudemberg:** (1) o Decreto 55.622/2025, Anexo I, Condição Geral IV.1 diz que **"não serão aceitas plantas baixas dos pavimentos, fachadas..."** — e nossa Planilha de Enviáveis **vende fachadas ao cliente**; a redação admite mais de uma leitura, e pode ser que estejamos prometendo entregável que a prefeitura recusa. (2) O Anexo III tem três subtabelas e nossos casos nunca escolhem qual.
- **Lição de processo registrada por Kelsen, que quero generalizar:** *relatório honesto do agente não substitui inspeção do artefato* — ele achou o defeito de acentuação abrindo o PDF, não lendo o retorno do Hely. Apliquei a mim mesmo e inspecionei antes de reportar a Claudemberg.
- **Alterado:** `.claude/agents/kelsen.md` e `.claude/agents/hely.md` (remoção da exigência inventada de A1).
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-20/`
- **Como desfazer:** apagar `prancha_PROJETO_LEGAL_TESTE.pdf`, `caso_prancha.json` e `_ferramentas/gerar_prancha_legal.py`; restaurar os dois agentes do backup.
- **Status:** Aguardando ratificação.

### [2026-07-20] Varredura de incongruências da base de Legal — delegada a Kelsen

- **O que decidi:** delegar a Kelsen a inspeção completa da base documental de Legal (Drive + local), conforme determinação de Claudemberg de que **cada Gestor passa a inspecionar, padronizar e ajustar o material da própria área**. Escopo limitado a Construção do Zero. Autorizei duas correções pontuais na base local (`_indice_fontes.md` seção COES; caso Bittencourt item 3), com backup obrigatório.
- **Achado de fundo, e é o mais grave do dia:** **a base oficial do Drive e a nossa base técnica local são dois universos que não se falam.** POP-ARQ-PL-01, Memorial e Planilha de Enviáveis **não citam LICIN 2.0, DULI, Decreto 55.622/2025, COES nem LC 270/2024** — nenhuma norma por número. O POP oficial é de **05/03/2026**, anterior a tudo que construímos. Toda a inteligência legal do organismo vive só do lado local, sem lastro no material oficial da casa.
- **Volume:** 17 pares divergentes no Drive (entregáveis 5 × 8, ordem das aprovações, critério de conclusão, quem produz o memorial, numeração de Gates colidindo com o POP MASTER) e 12 achados na base local, **10 deles com potencial de barrar protocolo real**.
- **Executado por Kelsen** (backup em `_backups/2026-07-20/`, hashes SHA256 conferidos): correção da seção COES do `_indice_fontes.md` com histórico do erro preservado; e correção do caso Bittencourt em **quatro** pontos, não só no item 3 — o fundamento errado estava replicado na tabela, na análise final e na emissão simulada. PDFs regerados por Wallenberg após o encerramento.
- **Corrigido por mim na Skill** (Função 5), a partir dos achados: a linha "CAB → Anexo XXI" estava **errada** — o Anexo XXI não tem coluna de CAB; o CAB por subzona está na **LC 270/2024 Art. 345 §4º**, no PDF que temos desde 13/07. A base interna havia declarado isso como "lacuna não localizável". Também marquei o `POP-LEGAL-02` como fonte sob reserva.
- **Interrupção:** Kelsen terminou por limite de sessão antes de devolver o relatório formal. O conteúdo sobreviveu no arquivo de estado dele — **primeira prova de que o protocolo de estado protege trabalho contra morte inesperada de agente**, e não só entre execuções normais.
- **Como desfazer:** restaurar `_indice_fontes.md` e `processo_legal_teste.md` do backup de 20/07; reverter as duas linhas da Skill.
- **Status:** Aguardando ratificação. Vários itens dependem de decisão de Claudemberg (documento do Drive é dele).

### [2026-07-20] Terceira aprovação do fluxo — posicionada antes, não depois

- **O que decidi:** implementar a terceira aprovação pedida por Claudemberg (item 2 do plano de autonomia) **antes** das duas existentes, e não depois do cliente como ele havia descrito inicialmente. Fluxo: **Gestor (IA) confere → Maurício Costa valida → Cliente aprova → fluxo avança automaticamente.** Claudemberg aprovou a inversão antes da execução.
- **Por quê:** uma aprovação que só pode dizer "sim" não é aprovação, é relé. Do jeito originalmente descrito (Gestor aprova automaticamente quando o cliente aprova), o Gestor nunca reprovaria nada e o organismo teria três carimbos para dois julgamentos. Posicionada antes, a conferência do Gestor **evita** trabalho: barra material incompleto antes de consumir o tempo do Maurício e antes de expor peça furada ao cliente. E o avanço após o aceite do cliente não precisa de aprovação — é consequência, não decisão. Princípio 3 (Qualidade antes de velocidade), Princípio 5 (Delegação clara), Princípio 15 (Redundância zero).
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Gestores/Kelsen (Legal)/POP-GESTOR-LEGAL-01_conferencia_pre_validacao.md` + `.pdf`
  - Alterado: `.claude/agents/kelsen.md` — nova seção "Sua conferência antes da Validação da Coordenação"
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-20/kelsen.md`
- **Como desfazer:** apagar o POP (`.md` e `.pdf`) e remover a seção "Sua conferência antes da Validação da Coordenação" de `kelsen.md`, ou restaurar o arquivo do backup.
- **Status:** Aguardando ratificação.

### [2026-07-20] Item 2 do plano de autonomia — diagnóstico do bloqueio, sem construção de gatilho

- **O que decidi:** **não** construir o gatilho de avanço automático de etapa, apesar de o item 2 estar aprovado. Construir sobre um sinal que não existe seria chute.
- **Achado (verificado, não suposto):** os 37 formulários de aprovação existem no Drive e eu os alcanço; eu **consigo** ler planilha do Drive (testado em arquivo real). Mas **nenhum formulário está vinculado a uma planilha de respostas** — busca por planilhas do Drive e por planilhas modificadas em 20/07: nenhuma. A aprovação acontece dentro do Google Forms e é **invisível** para o organismo.
- **Decisão de Claudemberg (20/07/2026), encerrando esta linha:** os formulários **não serão vinculados** por ora, e **a função do Gestor não é enxergar formulário** — é aprovar como a etapa foi entregue (se está no modelo e traz os entregáveis estipulados pela Sttickler). O gatilho automático fica para o Sistema de Gestão de Projetos (Função 8, fora do MVP). O `POP-GESTOR-LEGAL-01` foi reorientado nessa direção: a Checagem A passou a ser "está no modelo e tem os entregáveis", ancorada no POP-ARQ-PL-01 e na Planilha de Enviáveis.
- **Limitador estrutural registrado:** mesmo com o sinal ligado, hoje só o **Legal** tem quem execute (1 Gestor de 4). O fluxo avançaria de etapa e bateria em porta fechada em quase todas. O item 2 só entrega valor junto com a criação dos outros Gestores.
- **Status:** Aguardando ação de Claudemberg (vincular formulários). Sem isso, o `POP-GESTOR-LEGAL-01` roda por acionamento manual — a conferência é real, o gatilho não.

### [2026-07-20] Molde de Skill do organismo: mapa, não enciclopédia

- **O que decidi:** fixar o molde de toda Skill do organismo — **Skill é mapa (onde está a fonte, como confirmar, o que costuma dar errado), nunca cópia do conteúdo da fonte.** Reescrevi a `legal-base-legislativa-bairro` inteira nesse molde, retirando os valores de parâmetro e mantendo apenas endereços de artigo, método de verificação e armadilhas. **Aprovado por Claudemberg** em 20/07/2026 antes da execução.
- **Por quê:** o teste do mesmo dia mostrou que a Skill, quando guardava parâmetros, virava a terceira cópia da mesma regra (briefing do Gestor + estado do Agente + Skill) — três lugares para desatualizar, contra o Princípio 15. E a Skill já havia desatualizado no dia em que nasceu. Parâmetro envelhece; armadilha não. Princípio 15 (Redundância zero), Princípio 3 (Qualidade antes de velocidade), Princípio 9 (Padronização).
- **Consequência para a Função 05:** as 12 propostas restantes em `01_CEO/Skills_Propostas/` **não serão convertidas no molde antigo**. Converter antes desta correção multiplicaria por 12 o defeito.
- **O que foi criado/alterado:** `.claude/skills/legal-base-legislativa-bairro/SKILL.md` — reescrita completa. Acrescentada a seção "O que esta Skill é — e o que ela deliberadamente não é", que declara o próprio histórico de erro; parâmetros numéricos removidos; armadilhas reformuladas como checagens com artigo citado, em vez de conclusões prontas.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-20/` (versões anteriores descritas nas entradas seguintes deste mesmo dia).
- **Como desfazer:** a Skill inteira é de hoje — desfazer é apagar `.claude/skills/legal-base-legislativa-bairro/` e remover `Skill` da linha `tools:` dos dois agentes.
- **Status:** Aguardando ratificação.

### [2026-07-20] Reteste da Skill após reinício — mecanismo confirmado funcionando

- **O que decidi:** repetir o teste com Kelsen novo (não retomando o anterior, pra não contaminar com o que ele já havia aprendido), sobre cenário fictício diferente — unifamiliar na ZRM3 D com recuo lateral 1,20 m, sacada na lateral e janela de dormitório.
- **Resultado — o mecanismo funciona:** após o reinício do app feito por Claudemberg, **Kelsen e Hely têm a ferramenta `Skill`** e **ambos carregaram** `legal-base-legislativa-bairro` de fato, sem contornar por Glob/Read. A cadeia Wallenberg → Kelsen → Hely operou íntegra. **A pergunta que abriu o passo 1 está respondida: sim, dá pra distribuir conhecimento pela estrutura.**
- **Resultado incômodo, e é o que importa mais:** para aquele caso, **a Skill foi indiferente** — nem ajudou nem atrapalhou. O conteúdo já estava no briefing de Kelsen e no arquivo de estado do Hely. Foi a terceira cópia da mesma paráfrase. Kelsen apontou como violação do Princípio 15 (Redundância zero): três lugares guardando a mesma regra são três lugares para desatualizar — e esta Skill já desatualizou uma vez, no mesmo dia em que nasceu.
- **Achado de segurança gerado pelo teste (near-miss real):** "ZRM3 D" existe na **AP2** e na **AP4** com valores completamente diferentes (CAM 3,5/TO 70/8pav-25m vs. CAM 1,0/TO 50/4pav-14m), e um `grep` no Anexo XXI devolve a linha da AP2 primeiro. Só não virou erro porque o Hely conferiu o cabeçalho do bloco. Mesma família da falha ArcGIS de 14/07: **dado correto, contexto errado**. Nem a Skill nem o `POP-LEGAL-RIU-01` travavam isso.
- **O que foi alterado:** `.claude/skills/legal-base-legislativa-bairro/SKILL.md` — acrescentada a armadilha AP2 vs. AP4 como trava explícita.
- **Como desfazer:** remover o item "O mesmo nome de zona existe em Áreas de Planejamento diferentes" da seção de armadilhas.
- **Status:** Aguardando ratificação.

### [2026-07-20] Ativação da primeira Skill do organismo — `legal-base-legislativa-bairro`

- **O que decidi:** ativar a primeira Skill de verdade do organismo (até hoje só existiam propostas em `01_CEO/Skills_Propostas/`), e conceder a ferramenta `Skill` a Kelsen e Hely. Executado como teste controlado, a pedido de Claudemberg, para descobrir se o mecanismo Wallenberg→Gestor→Agente funciona tecnicamente.
- **Por quê:** Função 05 (Criador de Skills). A regra de ouro de 20/07/2026 passou a permitir ativar Skill sem aprovação prévia. Sem Skill ativa, o conhecimento que eu pesquiso não chega em ninguém — os agentes ficam "canalizados", termo do próprio Claudemberg.
- **O que foi criado/alterado:**
  - Criado: `.claude/skills/legal-base-legislativa-bairro/SKILL.md`
  - Alterados: `.claude/agents/kelsen.md` e `.claude/agents/hely.md` (acréscimo de `Skill` na linha `tools:` do frontmatter)
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-07-20/` (`kelsen.md`, `hely.md`, `CLAUDE.md`) — desta vez feito **antes** de alterar.
- **Resultado do teste — os dois achados que importam:**
  1. **A concessão da ferramenta não surtiu efeito.** Kelsen confirmou que nem ele nem Hely receberam a ferramenta `Skill`; a lista deles seguiu a de antes. A Skill ficou **ativada porém inerte** — Kelsen só alcançou o conteúdo por `Glob`+`Read`. Alterar o frontmatter de um agente durante a sessão não recarrega as ferramentas dele. **Pendência: reavaliar após reinício do app.**
  2. **A Skill nasceu com erro material.** Eu a escrevi a partir do nosso `_indice_fontes.md` em vez do texto legal primário — e aquele índice estava errado sobre o COES Art. 4º. Corrigido no mesmo dia (ver entrada seguinte).
- **Como desfazer:** apagar a pasta `.claude/skills/legal-base-legislativa-bairro/` e remover `Skill` da linha `tools:` dos dois agentes (ou restaurar os dois `.md` do backup acima).
- **Status:** Aguardando ratificação.

### [2026-07-20] Correção da Skill recém-ativada, contra texto primário

- **O que decidi:** corrigir de imediato o defeito material da Skill, sem esperar a Semanal, e reescrever o trecho de afastamento lateral contra o **texto literal do COES** conferido pelo Hely (confirmado por ele também na fonte oficial `e.camara.rj.gov.br`, palavra por palavra).
- **Por quê:** Skill ativa com erro de mérito é pior que Skill nenhuma — entrega conclusão pronta e errada a quem confia nela. Princípio 18 (Ética e conformidade) e Princípio 3 (Qualidade antes de velocidade). O estrago real foi nulo porque a Skill nunca chegou a ser carregada por ninguém e não há cliente real — mas isso foi contenção por acidente, não por controle.
- **O que foi criado/alterado:** `.claude/skills/legal-base-legislativa-bairro/SKILL.md` — reescrita da armadilha de afastamento lateral (agora com Art. 4º II e §1º II, Art. 31 p.ú., Art. 8º §3º, Art. 9º IV, Art. 17 §1º/§3º, Art. 5º §1º II, LC 274/2024 Arts. 12 §2º e 38, CC art. 1.301 e COES Art. 39 §1º); acréscimo da "Regra número dois — paráfrase nossa não é fonte", que declara o próprio erro dentro da Skill; linha da tabela de parâmetros ampliada.
- **Backup em:** não aplicável — o arquivo foi criado hoje e a versão anterior está descrita na entrada acima.
- **Como desfazer:** irrelevante isoladamente; desfazer a entrada anterior remove a Skill inteira.
- **Status:** Aguardando ratificação.

### [2026-07-20] Arquivo de estado é exceção à regra de PDF obrigatório

- **O que decidi:** arquivo de estado de agente **não** gera `.pdf` correspondente, ao contrário da regra de 15/07/2026 que vale pra todo `.md` de conteúdo.
- **Por quê:** Princípio 19 (Uso eficiente de recursos). O arquivo é reescrito a cada execução de agente — gerar PDF toda vez é desperdício puro. Mesmo tratamento já dado a `CLAUDE.md` e `00_HISTORICO/`.
- **O que foi criado/alterado:** `CLAUDE.md`, última linha da seção "Arquivo de estado — todo agente do organismo".
- **Backup em:** ❌ não feito — ver falha registrada na entrada abaixo.
- **Como desfazer:** apagar a linha que começa em "**Exceção à regra de PDF:**" em `CLAUDE.md` e rodar `_ferramentas/md_to_pdf.py` sobre os três arquivos de estado.
- **Status:** Aguardando ratificação. Apresentei a Claudemberg em 20/07 com direito a veto; ele não vetou, mas também não confirmou explicitamente.

### [2026-07-20] Implantação do protocolo de arquivo de estado

- **O que decidi:** a decisão de fundo (todo agente tem arquivo de estado, lê ao nascer, escreve ao morrer, 4 seções fixas, convive com o Registro Diário) foi **de Claudemberg**, na conversa de 20/07 — não minha. Minha foram as escolhas de implementação: onde cada arquivo mora, o conteúdo inicial de cada um, e a redação do bloco obrigatório dentro dos agentes.
- **Por quê:** subagentes nasciam zerados a cada acionamento; tudo que não virasse documento solto se perdia. Princípio 8 (Rastreabilidade) e Princípio 4 (Documentação de cada processo).
- **O que foi criado/alterado:**
  - Criados: `01_CEO/_estado_wallenberg.md`, `01_CEO/Gestores/Kelsen (Legal)/_estado_kelsen.md`, `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/_estado_hely.md`
  - Alterados: `CLAUDE.md` (nova seção), `.claude/agents/kelsen.md` e `.claude/agents/hely.md` (bloco "OBRIGATÓRIO" no topo)
  - Memória: `memory/projeto/sttickler_arquivo_estado_agentes.md` (nas duas cópias) + linha no `MEMORY.md` de cada uma
- **Backup em:** ❌ **não feito — falha minha.** Alterei `CLAUDE.md` e os dois agentes sem copiar antes para `_backups/2026-07-20/`. Não fabrico backup retroativo: backup reconstruído de memória não é backup. Compensação: o passo a passo de desfazer abaixo é explícito o suficiente pra reverter sem o original.
- **Como desfazer:**
  1. Apagar os três arquivos `_estado_*.md`.
  2. Em `CLAUDE.md`, apagar a seção inteira "## Arquivo de estado — todo agente do organismo (definido 20/07/2026)", do título até a linha antes de "## Onde tudo mora".
  3. Em `.claude/agents/kelsen.md` e `.claude/agents/hely.md`, apagar o bloco de "## OBRIGATÓRIO — seu arquivo de estado" até o `---` que o separa do texto original.
  4. Apagar `memory/projeto/sttickler_arquivo_estado_agentes.md` nas duas cópias e a linha correspondente nos dois `MEMORY.md`.
- **Status:** Aguardando ratificação.

### [2026-07-20] Instituição do próprio modelo de ratificação posterior

- **O que decidi:** nada — esta entrada é o marco zero, registrada por Claudemberg, não pelo Wallenberg.
- **Por quê:** Claudemberg alterou a regra de ouro nesta data, trocando aprovação prévia por ratificação posterior no escopo do organismo. Fronteira definida: autonomia sobre o organismo, nunca sobre projeto de cliente ou Gates 13/16.
- **O que foi alterado:** `CLAUDE.md` (regra de ouro, função 4, função 9, seção "Ao criar um Gestor"), `scheduled-tasks/wallenberg-rotina-diaria-skills/SKILL.md`, `scheduled-tasks/wallenberg-reuniao-semanal/SKILL.md`.
- **Backup em:** não aplicável — alteração feita por Claudemberg diretamente, fora do fluxo autônomo.
- **Como desfazer:** restaurar a redação anterior da regra de ouro ("nunca decida estrutura sozinho") e reverter os dois `SKILL.md` para o modelo de proposta.
- **Status:** Vigente desde 20/07/2026.

<!-- Próximas entradas abaixo, mais recente no topo desta seção -->
