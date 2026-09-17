# 📑 Índice Central — Rotina Diária Skills v3.1

**Versão:** 3.1.0 | **Data original:** 28/08/2026 | **Fonte única consolidada:** 16/09/2026 | **Status:** ✅ PRONTO

---

## 📁 Mapa de Arquivos

### Entrada Rápida (Novos Usuários)

| Arquivo | Tempo | Propósito |
|---------|-------|----------|
| **COMECE_AQUI.md** | 2 min | O que mudou, próximos passos |
| **RESUMO_EXECUTIVO_ROTINA_REDEFINIDA.md** | 3 min | Contexto da mudança, ganhos |

### Referência Completa

| Arquivo | Tempo | Propósito |
|---------|-------|----------|
| **wallenberg-rotina-diaria-skills-v2_SKILL.md** | 30 min | Manual completo (Passos 1-10 + Apêndice de bloqueadores/critérios) — inclui o escopo v3.0 por Gestor no Passo 1. **Única fonte de verdade.** |

**[Excluídos 14/09/2026]** `wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md` (estava vazio, 0 bytes), `RESUMO_IMPLANTACAO_FINAL_28_08_2026.md`, `ENTREGA_FINAL_REDEFINICAO_28_08_2026.md`, `CHECKLIST_PRE_LANCAMENTO_28_08_2026.md` e `ROTINA_REDEFINIDA_COM_AGENDADOR.md` — eram registros de lançamento de 28/08 (relatório de entrega, checklist de assinatura em branco, explicação de automação já coberta pelo SKILL.md e pelas tarefas agendadas reais). Nenhum tinha conteúdo vivo além do que já está aqui ou no SKILL.md. Removidos do disco (git rm — recuperáveis via histórico se precisar).

**[Aposentados 16/09/2026, auditoria de dessincronização — Claudemberg]** `wallenberg_manual_operacional_rotina_diaria_skills.md` (v2.9 — preso na versão pré-v3.0 do Passo 1; era citado pelo scheduled task como 2ª fonte de dúvida, causando risco real de reversão de comportamento) e `GUIA_EXECUCAO_ROTINA_SEXTA_28_08_2026.md` (descrevia o Passo 6/Painel como "% de progresso por projeto" — mecanismo que não existe mais; o Painel real usa FEED de eventos). Conteúdo vivo do manual (bloqueadores/critérios por passo) migrado para o Apêndice do SKILL.md. Ambos movidos para `00_HISTORICO/` com aviso de aposentadoria no topo (não excluídos — só a citação ativa foi removida).

### Checklists Interativos

| Arquivo | Dias | Propósito |
|---------|------|----------|
| **Checklist_Diaria.html** | Seg-Qui | Visual + progresso + timer (Passos 1-5) |
| **Checklist_Sexta.html** | Sexta | Visual + progresso + timer (Passos 6-10) |

---

## 🎯 Como Usar Este Índice

### Cenário 1: "Sou novo, nunca li nada"

1. Comece por **COMECE_AQUI.md** (2 min)
2. Depois leia **RESUMO_EXECUTIVO_ROTINA_REDEFINIDA.md** (3 min)
3. Amanhã use **Checklist_Diaria.html** e siga passos
4. Se tiver dúvida em algum passo, consulte **wallenberg-rotina-diaria-skills-v2_SKILL.md**

### Cenário 2: "Quero referência completa"

Leia **wallenberg-rotina-diaria-skills-v2_SKILL.md** (30 min — inclui o Passo 1 v3.0 por Gestor, a explicação de CronJob/Agendador na seção "Automático", e o Apêndice de bloqueadores/critérios de sucesso por passo)

### Cenário 3: "Estou executando agora"

1. Abra **Checklist_Diaria.html** ou **Checklist_Sexta.html**
2. Siga os passos visuais
3. Se ficar preso, consulte **wallenberg-rotina-diaria-skills-v2_SKILL.md** (seção do passo específico)

---

## 📊 Matriz de Seleção

| Tenho... | Quero... | Leia |
|----------|----------|------|
| 2 min | Saber o que mudou | COMECE_AQUI.md |
| 5 min | Entender benefícios | RESUMO_EXECUTIVO_ROTINA_REDEFINIDA.md |
| 15 min | Referência rápida | wallenberg-rotina-diaria-skills-v2_SKILL.md (índice) |
| 30 min | Tudo completo | wallenberg-rotina-diaria-skills-v2_SKILL.md (completo, com Apêndice) |
| Executando | Pronto pra rodar | Checklist_Diaria.html ou Checklist_Sexta.html |
| Sexta | Detalhes sexta | Checklist_Sexta.html + item 6-10 do SKILL.md |

---

## 🚀 Roteiros por Perfil

### Wallenberg (Executor da Rotina)

**Primeira vez:**
1. Leia COMECE_AQUI.md (2 min)
2. Leia wallenberg-rotina-diaria-skills-v2_SKILL.md (30 min)
3. Amanhã 08:00 use Checklist_Diaria.html

**Execução contínua:**
1. Consulte Checklist_Diaria.html ou Checklist_Sexta.html
2. Se dúvida em passo X, vá para wallenberg-rotina-diaria-skills-v2_SKILL.md seção "Passo X" — **no Passo 1, releia a cada rodada (v3.0), não só na primeira vez**
3. Envie relatório ao fim

### Claudemberg (Validação)

**Acompanhamento semanal:**
1. Revise relatórios de execução (seg-qui e sexta)
2. Consulte Dashboard no Painel
3. Leia análise semanal em rotina_fechamento_template.md

---

## 📅 Histórico de Versões da Rotina

| Data | O que mudou |
|------|------|
| 28/08 | Lançamento original (checklists + automação) |
| 08-09/09 | v2.8/v2.9 — escala por Gestor + fluxo de ativação Trilha A |
| 10/09 | v3.0 — Escopo Expandido por Gestor (mentalidade "brecha válida") |
| 14/09 | Rótulos e fluxo de execução corrigidos para refletir a v3.0 de fato (tarefa agendada, Checklist, este índice); 5 arquivos obsoletos de 28/08 excluídos |
| 16/09 | v3.1 — Fonte única consolidada: manual v2.9 e GUIA_EXECUCAO_ROTINA_SEXTA aposentados (movidos para 00_HISTORICO/), conteúdo vivo migrado para o Apêndice do SKILL.md, CronJob PDF corrigido para não gerar mais PDF de Skills individuais |

---

**Próxima leitura:** COMECE_AQUI.md
