---
padrao: PADRAO-DOC-POP-01
titulo: Padrão de POP em Google Docs — vale para todo Gestor/departamento
autor: Wallenberg (CEO) — Função delegada por Claudemberg, 08/08/2026
criado: 2026-08-08
status: RASCUNHO — para discussão na Reunião Semanal de 10/08/2026, ainda não aplicado a nenhum documento real
aplica_a: POPs do Sistema Orgânico STTK que vivem como Google Docs no Drive (distinto dos POPs internos em .md, ex. POP-LEGAL-06, que já seguem molde próprio e não são tocados por este padrão)
principios: 8 (Rastreabilidade), 9 (Padronização), 15 (Redundância zero), 18 (Ética e conformidade)
---

# Padrão de POP (Google Docs) — Sistema Orgânico STTK

## 0. Por que este documento existe
Cada Gestor evoluiu sua documentação de forma orgânica, sem molde comum. O objetivo aqui não é reescrever conteúdo — é fixar **uma estrutura única**, para que um POP do Legal, da Arquitetura, e (no futuro) de Complementares/Fechamento sejam reconhecíveis como a mesma família de documento, mesmo tratando de assuntos diferentes. Mesmo princípio já usado para as Skills (ver `memory/projeto/sttickler_molde_skill_mapa.md`, 20/07/2026): o molde é fixado uma vez, deliberadamente, e depois aplicado — não emerge de cada Gestor decidindo por conta própria.

Este padrão só se aplica depois de aprovado por Claudemberg na Semanal. Até lá, é rascunho de discussão.

## 1. Estrutura obrigatória (nesta ordem)

**Bloco de cabeçalho** (primeiras linhas do documento, antes do título):
```
Departamento/Gestor responsável: [nome]
Versão: [n]
Última atualização: [DD/MM/AAAA] — por [quem]
Status: Vigente | Em revisão | Superado (aponta pro que substituiu)
```

**1. Objetivo** — por que este POP existe, que problema resolve. Se nasceu de um erro/lacuna real, citar o episódio (mesmo estilo do POP-LEGAL-06: "este bug se repetiu três vezes...").

**2. Escopo** — o que o procedimento cobre e o que explicitamente não cobre. Evita que alguém estenda o POP para um caso que não foi pensado.

**3. Procedimento** — passo a passo numerado, imperativo ("Confira X", "Rode Y"), não narrativo. Cada passo que depende de uma fonte externa (lei, sistema oficial, dado do cliente) diz qual é essa fonte.

**4. Fontes / Referências** — lista do que fundamenta o procedimento. Regra de ouro (mesma do molde de Skill): **nunca citar um resumo interno como fonte** — sempre o texto primário (lei, decreto, NBR, sistema oficial) ou, na ausência dele, dizer explicitamente "fonte não confirmada em primário, usar com ressalva".

**5. Responsabilidades** — quem executa (Agente/Gestor), quem audita antes de considerar concluído, se passa pelo Gate do Maurício (Artigas) antes de virar parecer para cliente.

**6. Histórico de revisão** — tabela: `Data | O que mudou | Quem mudou | Motivo`. Nunca apagar linha antiga — POP é auditável, não edição silenciosa.

**7. Lacunas conhecidas** — o que ainda não está resolvido/confirmado. Honestidade sobre o que falta é parte do padrão, não falha dele (Princípio 3 — não fabricar certeza).

## 2. Regras de formatação (valem para todo Gestor, não só Legal)
- **Nenhum caractere unicode decorativo** (setas →←, emojis, símbolos como ✓✗🔴) em nenhum POP — mesma lição do `POP-LEGAL-06` (bug de glifo silenciosamente descartado ao gerar PDF), generalizada para todos os departamentos, não só quem já sofreu o incidente.
- Hierarquia de título padrão do Google Docs (Título 1 = nome do POP, Título 2 = seções acima).
- Não duplicar informação que já vive em outro documento oficial — linkar, não copiar (Princípio 15).

## 3. Quem pode criar/editar
- Cada Gestor decide o conteúdo técnico da própria área.
- Documento que serve **mais de um departamento ao mesmo tempo** (ex.: planilha de entregáveis compartilhada) não é editado unilateralmente por um Gestor — passa por Wallenberg antes (ver `01_CEO/Padroes_Documentos/PROTOCOLO-DADO-CLIENTE-EM-DOCUMENTO-BASE.md`, seção 2).
- Execução técnica da escrita: hoje mediada por Wallenberg (Service Account para editar existente; conector Drive OAuth, confirmado 08/08/2026, para criar novo — ver `pendencias.json`, item `wallenberg-drive-create-file-confirmado`). Avaliar dar a ferramenta direto a cada Gestor depois que este padrão estiver validado.

## 4. Aplicação a documentos já existentes
Não é reescrita automática de tudo de uma vez. Sequência:
1. Wallenberg identifica os documentos candidatos (ver plano de auditoria completa, `01_CEO/Padroes_Documentos/PLANO-AUDITORIA-DOCUMENTOS_2026-08.md`).
2. Cada documento passa pelo checklist do `PROTOCOLO-DADO-CLIENTE-EM-DOCUMENTO-BASE.md` antes de qualquer edição.
3. Gestor dono da área recebe a pendência (via `pendencias.json` + Painel do Fundador + Notion "Pendências de Documentos") e executa a adequação ao padrão.
4. Wallenberg confere antes de fechar (mesmo modelo de auditoria por rasterização já usado nos PDFs).

## 5. Lacunas conhecidas deste próprio padrão
- Ainda não testado em nenhum documento real — é a primeira versão, sujeita a ajuste depois do primeiro caso de aplicação.
- Não cobre POPs internos em `.md` (esses já têm molde funcionando, ver POP-LEGAL-06) — só documentos Google Docs no Drive.
- Não define ainda o padrão equivalente para outros tipos de documento (Memorial, Planilha, Quadro de Áreas) — este é só o de POP; os demais tipos citados por Claudemberg entram em rodadas seguintes, um de cada vez.
