# Livro-razão de Decisões Autônomas — Outubro/2026

## 01/10/2026 — Rotina Diária Skills v3.5.0 (qui, 09:07) — 2 Skills novas ativadas com ressalva

**1. Skill `selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj` (Kelsen/Hely), v1.1, ativa-com-ressalva.**
- **O que decidiu:** criar e ativar a Skill do novo SELCA (Decreto Estadual 50.473/2026). A versão é a v1.1, já corrigida por Kelsen.
- **Por quê:** fecha a pendência aberta em 29/09 ("SELCA: o que muda para obra residencial perto de lagoa", dono Hely). Kelsen estava sem Skill nova desde 25/09. O texto integral do DOERJ foi extraído com pypdf e lido. Kelsen conferiu artigo por artigo, fez 6 correções factuais e deu PROCEDE COM RESSALVA. Ressalvas: R1, competência SMAC × INEA (LC 140) não lida; R2, prazos antigos só da nota Mayer Brown; R3, a seção 8 é tese e só entra em caso real depois do Gate do Maurício; R4, a lei de outorga não foi lida; R5, as normas operacionais do INEA não foram lidas. Wallenberg retirou a R6 (treino em caso fictício), porque o treino foi extinto na v3.5.0.
- **O que alterou:** `01_CEO/Skills_Propostas/2026/Outubro/kelsen_selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj.md` (novo); `.claude/skills/selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj/SKILL.md` (novo); remissões de volta em `.claude/skills/legal-base-legislativa-bairro/SKILL.md` (1 linha nova no fim da seção LMS) e em `.claude/skills/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio/SKILL.md` (ressalva 6, linha da tabela e linha de fonte: o SELCA agora consta como conferido no texto primário). Sem mudança de regra nas duas.
- **Backup:** `_backups/2026-10-01/legal-base-legislativa-bairro__SKILL.md` e `_backups/2026-10-01/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio__SKILL.md`.
- **Como desfazer:**
  1. Apague a pasta `.claude/skills/selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj/`.
  2. Restaure os 2 backups sobre os `SKILL.md` originais.
  3. Volte o `Status` do `.md` em `Skills_Propostas` para `proposta` ou mova-o para `_Arquivadas/2026/`.
  4. Ajuste o `indice.md` de Outubro.

**2. Skill `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj` (Lúcio/Oscar), v1.1, ativa-com-ressalva.**
- **O que decidiu:** criar e ativar a Skill de desempenho térmico da cobertura: Ucob × absortância, fator FT do ático ventilado, emitância de telha metálica e o aviso do IPT.
- **Por quê:** preenche o "U cobertura ≤ x — confirmar" da Skill `nbr15575-4-emenda2025-...`. Textos lidos: o Projeto de Emenda NBR 15575-5 (mar/2021, sem valor normativo) e o artigo do IPT (2017), ambos extraídos com pypdf. Lúcio deu PROCEDE COM RESSALVA e corrigiu o §4: a cobertura sem isolante do IPT já não passava no simplificado. Também limitou a brecha do FT a 0,4 < α ≤ 0,6 e retirou 2 macetes sem fonte lida. Ressalvas: R1, projeto de emenda; R2, o envelope das 2 colunas é premissa; R3, Emenda 2025 e simulação; R4, os números do IPT são tendência; R5, o isolante é premissa, não exigência.
- **O que alterou:** `01_CEO/Skills_Propostas/2026/Outubro/lucio_cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj.md` (novo); `.claude/skills/cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj/SKILL.md` (novo); remissões de volta (1 citação cada, sem mudança de regra) em:
  - `.claude/skills/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj/SKILL.md` (após a tabela de Coberturas);
  - `.claude/skills/nbr15220-3-bioclimatica-rj/SKILL.md` (linha 30);
  - `.claude/skills/nbr9575-impermeabilizacao/SKILL.md` (linha 29).
- **Backup:** `_backups/2026-10-01/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj__SKILL.md`, `_backups/2026-10-01/nbr15220-3-bioclimatica-rj__SKILL.md` e `_backups/2026-10-01/nbr9575-impermeabilizacao__SKILL.md`.
- **Como desfazer:**
  1. Apague a pasta `.claude/skills/cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj/`.
  2. Restaure os 3 backups.
  3. Volte o `Status` do `.md` em `Skills_Propostas` para `proposta` ou arquive-o.
  4. Ajuste o `indice.md` de Outubro.

**3. Cardozo sem Skill.** A busca sobre contenção de escavação em argila mole (NBR 9061, estaca-prancha) não achou fonte primária. Parte do tema já está na Skill de rebaixamento de 29/09. Não forcei.

**Painel:** 2 eventos `skill` gravados no `feed.jsonl` via `Append-STTKLog.ps1`, 2/2 OK.

**Fonte de verdade para rever:** `01_CEO/rotina_fechamento_template.md`, rodada de 01/10/2026.

---

## 01/10/2026 — Drenagem Contínua v2.5.0 (qui, 11:04) — Ensaio 003 etapa 1 executada e corrigida

**1. Ensaio Sombra 003, etapa 1 (Legal base) — Kelsen/Hely executaram, Bardi corrigiu.**
- **O que decidiu:** executar a etapa liberada (`proxima_acao: executar`). Lacre do gabarito conferido antes e depois (SHA256 48867C3C…C9F9 = histórico). Ninguém abriu `_gabaritos_LACRADO/` além do Bardi.
- **Resultado:** entrega em `01_CEO/Casos_TESTE/ensaio_003/etapa_01_legal_base/entrega/` (`parecer_legal_base_003.md` do Hely, `auditoria_kelsen_003.md` do Kelsen — LIBERA COM RESSALVA). Parecer do Bardi: `etapa_01_legal_base/parecer_bardi.md` — **recomendação APROVAR** (8/8 itens, 4/4 iscas, contas refeitas e corretas; 6 correções não bloqueantes: Skill OODC × LC 301 Art. 58; leitura do Dec. 3.046 inciso XI; 520 m² × teto 457,44 m² computáveis; lençol 0,90 m × piscina/escavação; divergência POP-GESTOR-LEGAL-01 §4.3 × POP-LEGAL-02; Hely sem WebFetch). Bardi registrou erro do próprio gabarito ("computáveis") sem alterá-lo.
- **O que alterou:** `_estado_ensaio_003.json` → `aguardando_aprovacao` / `aguardar_claudemberg`, histórico `executada_e_corrigida`. Evento `marco` no `feed.jsonl` (1/1 OK).
- **Como desfazer:** voltar o JSON a `aguardando_execucao`/`executar`, remover a última linha do histórico e apagar `entrega/` + `parecer_bardi.md`.
- **Sobe a Claudemberg:** aprovar/reprovar a etapa 1 (só ele). Kelsen sinalizou: PRPA não definido; propostas de correção em 4 Skills (OODC, Dec. 3046, varandas, habite-se) — não aplicadas nesta rodada (Kelsen as trata como dono; Bardi alerta que a de varandas precisa reler o fim do inciso VII).

**2. Passo 7.5 — varredura mensal de Drive (Kelsen).** 3 correções objetivas (POP-ARQ-PL-01 seção 7.1 e versão; Memorial com caractere corrompido). **Não aplicadas:** `update_file` do MCP só altera título/pasta; a via Service Account é vetada no automático. Registrado item `kelsen-drive-varredura-mensal-01-10-correcoes` (humano) em `pendencias.json` com texto literal antes/depois. Lúcio e Cardozo não foram acionados nesta rodada (sem fila) — a varredura mensal deles fica para a próxima rodada em que forem acionados no mês.

## 01/10/2026 — Kelsen (Legal): correções pós-Ensaio 003, etapa 1 (ordem direta de Claudemberg, via Wallenberg)

- **O que mudou:**
  - **Skill `legal-oodc-mais-valera-mais-valia` v1.1**, instalada e proposta. Janela da LC 281 Art. 40 aberta até 01/12/2026, 30% só à vista (LC 301 Art. 58). Os dois regimes foram separados: OODC pura (LC 270 Art. 111, Fórmula 1 do Anexo XXV) e LC 281 (Art. 18 §1º). Entrou a isenção de 5 anos da **LC 270 Art. 110**, com exceções no §1º, §3º e §8º.
  - **Skill `decreto3046` v1.3.** R1 reescrita (a isenção está no Art. 110, e não no 106), M3 (VII->XI, unifamiliar), M4 (Art. 111 §5º), §7 sobre como checar a vigência do Dec. 3.046. Exemplo sem artigo marcado.
  - **Skill `varandas` v1.2.** Nova §4.1 sobre o regime da ZPP (VII, XI e XIV). A minha proposta "VII mais restritivo" ficou restrita a multifamiliar.
  - **Skill `habite-se`.** Arts. 4º, 6º e 8º conferidos no PDF oficial. O item de documentos estava errado (Art. 6º é requerimento, não Habite-se).
  - **POP-GESTOR-LEGAL-01 §4.3.** Sai "POP-LEGAL-02 SUSPENSO"; entra a regra de ler o `status:` do próprio POP.
  - **POP-LEGAL-02.** Nova R.8 (LC 270 Arts. 106-111).
  - **`hely.md`.** Corpo: checklist de 7 itens e correção da menção a WebSearch/WebFetch. O frontmatter não foi tocado.
  - **`auditoria_kelsen_003.md`.** Errata 4.1.
  - Pelo Hely: `_indice_fontes` (Dec. 3.046 e LC 270 Arts. 106-111), `_estado_hely` (checklist), cópias proposta = instalada (md5 conferido) e 8 PDFs regerados e conferidos visualmente.
- **Por quê:** parecer do Bardi, seção "O que corrigir", e a minha auditoria. Ao reler o primário, LC 270 pp. 40-41, achei dois erros a mais, um meu e um do Bardi:
  - a isenção de 5 anos existe, no Art. 110;
  - o Anexo XXV é sim a fonte da fórmula da OODC pura.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/kelsen_ANTES_*` (20 arquivos, cópia feita pelo Hely antes de qualquer edição).
- **Como desfazer:** copiar cada `kelsen_ANTES_*` de volta ao caminho original. Nos arquivos `_SKILL_instalada`, o destino é `.claude/skills/<nome>/SKILL.md`. Depois, regerar os PDFs a partir dos .md restaurados (ou restaurar os .pdf do backup).
- **Sobe a Wallenberg:** pedido formal de ferramenta para o Hely (WebFetch + WebSearch), sem edição de frontmatter. As dúvidas de mérito, Art. 110 §8º na AP4 e VII x XI na unifamiliar, vão ao Gate do Maurício.

## 01/10/2026 — Wallenberg: aprovação da etapa 1 do Ensaio 003 e cadeia de pedido de ferramenta

- **Claudemberg aprovou ao vivo a etapa 1** ("Aprovo a etapa 1"). No `_estado_ensaio_003.json`: `etapa_atual` 2, `status_etapa` a_criar, `proxima_acao` criar_caso, e histórico `aprovada_por_claudemberg`. A próxima Rotina Ensaio Sombra (Bardi) monta a etapa 2 (Viabilidade, Villaça).
- **Ordem de Claudemberg (regra durável):** o Gestor corrige os erros que o seu Agente cometeu no ensaio e capacita esse Agente. A ferramenta ou plugin que o Gestor não consegue dar sobe a Wallenberg. O que Wallenberg não tem permissão de fazer sobe a Claudemberg na Reunião Semanal. Kelsen executou a ordem (entrada acima).
- **Pedido de WebFetch + WebSearch para o Hely:** tentei adicionar as duas ao `tools:` do `.claude/agents/hely.md`. O classificador de permissão do modo automático negou a edição (auto-modificação). Não contornei. Foi para a pauta da Semanal como `hely-ferramentas-webfetch-websearch-semanal` em `pendencias.json`. O `hely.md` não foi alterado. Existe um backup preventivo em `_backups/2026-10-01/wallenberg_ANTES_hely_tools.md`, que pode ser descartado.


## 01/10/2026 — Rotina Macetes de Profissionais v1.2: 7 macetes em 2 Skills (quinta, 14:14)

- **Fila do dia** (máx. 1 por Gestor; Villaça não tem Skill e não foi aberto):
  - Kelsen: `varandas-nao-computaveis-ate-to-coes-lc198-rj`. Prioridade 0a: Bardi apontou a leitura do Dec. 3.046 VII/XI. Era a 2ª rodada.
  - Lúcio: `nbr15220-3-bioclimatica-rj`. Prioridade 0b: a etapa 3 do Ensaio é o Levantamento. A Skill é cross; Cardozo ficou registrado como co-dono.
  - Cardozo: `fundacoes-solos-moles-lencol-freatico-barra-recreio`. Prioridade 1.
- **nbr15220-3 v1.1 → v1.2 (Lúcio), 3 macetes tipo A.** Fontes: Lamberts/LabEEE (ENCAC 2025) e o Projeto de Revisão ABNT de jun/2024, pp. 1, 13, 20-23.
  - M1: a zona se confirma no mapa do LabEEE. O Rio é 4A e é a cidade característica da zona (TMYx, estação 837550).
  - M2: a 2024 não tem diretrizes construtivas por zona; a indústria pediu a retirada.
  - M3: o microclima entra como premissa, sem trocar de zona.
  - A ressalva da zona passou de "indício" para "confirmada no texto de Consulta Nacional; texto final não lido". A seção Limbo recebeu a regra dos 180 dias do prefácio, marcada como "só no texto de projeto".
- **fundacoes-solos-moles 1.2 → 1.3 (Cardozo), 4 macetes tipo A.**
  - M1 a M3 vêm de Urbano R. Alonso (Instituto de Engenharia, 2023): teste do trado junto ao furo de sondagem; leitura do perfil de consumo de concreto; erros de execução a proibir na especificação.
  - M4 vem de Danziger/Gerscovich (UERJ, 2017): atrito negativo na argila da Baixada de Jacarepaguá.
- **varandas: sem macete na 2ª rodada → lista "Sem fonte pública".** Tentativas: tipo A (CAU/RJ, arquitetos) e tipo C (Ademi-RJ, Sinduscon-Rio, CAU/RJ, SMU). A única fonte C achada foi a ata do COMPUR de 13/09/2007 (Ademi/AsBEA). Ela traz só opinião sobre fechamento de varanda e nenhuma técnica nova.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/macetes_ANTES_*` (2 arquivos).
- **Como desfazer:**
  - Copiar cada `macetes_ANTES_<skill>_SKILL_instalada.md` para `.claude/skills/<skill>/SKILL.md`.
  - Nas cópias de `Skills_Propostas/2026/Setembro/`, reverter pelo git (`git checkout <commit>~1 -- <arquivo>`).
  - Reverter também `_estado_lucio.md` e `_estado_cardozo.md`.
- **Pendências geradas (não resolvidas aqui; ficam para a Drenagem/Reunião):**
  - (1) Cinco Skills ainda tratam a ZB 4A como "indício": nbr15575-4-emenda2025, lucio-protecao-solar, vidro-fachada-poente, especies-nativas e cobertura-transmitancia. É preciso alinhar com a 15220-3 v1.2 (donos: Lúcio, e Cardozo para especies-nativas).
  - (2) Divergência de anexo na `nbr6122-2019-fundacoes`. A Skill diz Anexo J para hélice; Alonso cita o Anexo N. Cardozo suspeita que o erro está na Skill. É preciso conferir na norma.
