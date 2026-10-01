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
