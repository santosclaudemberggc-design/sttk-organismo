---
name: sttickler-visao-geral
description: "Contexto geral do projeto Sistema Orgânico STTK — empresa, escopo, pasta destino, documentos mestres e status do código legado"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Sistema Orgânico STTK — Visão Geral

**Empresa:** Sttickler Empreendimento. Usuário (Claudemberg) é o tomador de decisão / dono do negócio.

**Escopo atual:** só **Construção do Zero**. Reforma, Retrofit e Home Staging existem como produtos da empresa mas ficam **fora do organismo por enquanto** — material relacionado a eles deve ser excluído de qualquer Skill/conhecimento que o CEO Wallenberg monte (ver [[sttickler_drive_estrutura]] pra regra de filtro).

**Prazo:** MVP até início de Dezembro/2026.

**Pasta de destino da nova estrutura:** `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO` — é aqui que a estrutura de pastas do organismo (CEO/Gestores/Agentes) vive. Contém: `memory\` (cópia organizada em `projeto/`, `referencia/`, `feedback/` — cópia de referência legível sem acesso à memória do Claude Code; a memória oficial passou a ser esta, em `C:\Users\santo\.claude\projects\D--000-ESTRUTURA-DEPARTAMENTO-DE-PROJETO\memory\`, migrada em 10/07/2026), `00_HISTORICO\` (os 2 docs originais), `02_PROPOSTAS\` (modelo de proposta comercial), `03_REGISTROS_DIARIOS\{Ano}\{Mês}\{data}.md` (visibilidade diária, criado 13/07/2026), `.claude\agents\` (subagentes técnicos — um arquivo .md por Gestor e por Agente, obrigatório ficar aí, é como o Claude Code reconhece um subagente), e **`01_CEO\`** (renomeada de `01_ESPECIFICACAO_ATUAL` em 14/07/2026) — casa de tudo criado através do Wallenberg: `01_CEO\wallenberg_especificacao.html` (especificação viva) e `01_CEO\Gestores\` (documentação de cada Gestor, movida da raiz nessa mesma data).

**Padrão da pasta `01_CEO\Gestores\` (definido por Claudemberg em 13/07/2026, reorganizado em 14/07/2026):** um Gestor por subpasta, nome + área entre parênteses (ex: `01_CEO\Gestores\Kelsen (Legal)\`), com os documentos do próprio Gestor (proposta, Skills) direto ali, e uma subpasta `Agentes\{Nome}\` — uma por Agente da equipe — pro material de trabalho específico daquele Agente (ex: `Agentes\Hely\Fontes_Legislacao\`, `Agentes\Hely\Casos_TESTE\`). Só o conteúdo/documentação vive aqui; o arquivo técnico do subagente (`.claude\agents\<nome>.md`) é separado, por exigência do Claude Code. Primeiro caso: `01_CEO\Gestores\Kelsen (Legal)\gestor_legal_proposta.html`.

**Regra a partir de 10/07/2026:** todo documento/artefato novo criado nesta conversa deve ser salvo direto em `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO` (na subpasta certa), não mais em rascunho temporário. Toda atualização de memória deve ser replicada nos dois lugares (oficial + cópia de referência dentro da pasta do organismo).

## Documentos mestres (fonte da definição original, agora parcialmente substituída)
- `C:\Users\santo\Downloads\SISTEMA_ORGANICO_STTK.md` — versão 1.0, mapa geral do organismo, 21 Princípios, 16 Gates.
- `C:\Users\santo\Downloads\ESTRUTURA_COMPLETA_ORGANISMO_STTICKLER.md` — mapeamento POP ↔ etapa ↔ Gestor, resumo de cada POP.
- `C:\Users\santo\Downloads\DP - FLUXOGRAMA DE EXECUÇÃO DOS PROJETOS.pdf` — fluxograma oficial real da empresa (ver [[sttickler_fluxograma_oficial]]).

**Importante:** esses dois .md descrevem uma definição do CEO que já foi **parcialmente substituída** na conversa de 09/07/2026 — o usuário disse explicitamente "vamos esquecer algumas coisas sobre o CEO que já foi feita" porque a definição original veio de uma mistura entre conversas de chat externas e instruções soltas no Claude Code. A definição válida agora é [[sttickler_ceo_wallenberg]]. Os 21 Princípios, os 16 Gates e a estrutura de pastas por projeto (12 seções) dos .md ainda são válidos como referência de fluxo de trabalho — só a definição das responsabilidades do CEO em si foi refeita.

## Conectores disponíveis
Google Drive (conector MCP, prefixo `mcp__014dedc9-41ba-4ccb-9bf4-e296d09b271e__`) e Google Calendar (prefixo `mcp__83726fbc-3324-4407-8031-c86135b737c4__`) já estão conectados à conta `santosclaudembergg@hotmail.com`. Ambos aparecem como ferramentas deferidas — carregar via ToolSearch antes de usar.

## Código legado
`D:\Sharing_Claudemberg\0001_STTICKLER\ceo_sttickler.py` — classe `CEOSttickler` com métodos parcialmente implementados (gerar_id_projeto, validar_gate, criar_novo_projeto, gerar_relatorio_conselho etc.) e testes unitários. Foi construído ANTES da redefinição da essência do CEO (agora Wallenberg) — **não deve ser reaproveitado automaticamente**; precisa ser revisado à luz da nova definição antes de qualquer decisão de manter/descartar trechos.
