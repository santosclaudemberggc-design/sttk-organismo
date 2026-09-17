# 🚀 COMECE AQUI — Rotina Diária Skills v3.3.2

**Data:** 17/09/2026 (varredura de documentos gerais) | **Status:** ✅ PRONTO PARA USAR | **v3.3.2 desde:** 17/09/2026 (endurecimento SRE + sincronização `/watch:watch` + fronteira crítica de cliente restaurada — ver Histórico de Versões em `wallenberg-rotina-diaria-skills-v2_SKILL.md`)

---

## 📌 O Que Mudou?

Antes: Pesquisa + Consolidação + Redação = processo longo e manual  
Depois: **Mesmo processo, checklist visual + automação 20:00 (PDFs)**

---

## ⏱️ Quanto Tempo Leva?

- **Seg-Qui:** 60–75 min (Pesquisa + Consolidação + Redação + Salvamento + Ferramentas)
- **Sexta:** 90–120 min (Painel + Learning + Dashboard + Análise)

---

## 🎯 Próximo Passo

1. **Seg-Qui:** Clique em Checklist_Diaria.html e siga os passos (1, 2, 3, 4, 8). **No Passo 1, releia também a seção "Passo 1" de `wallenberg-rotina-diaria-skills-v2_SKILL.md`** — tem os exemplos concretos por Agente (v3.0) que não cabem no Checklist.
2. **Sexta:** Use Checklist_Sexta.html (Passos 6, 7, 9, 10)

---

## 📁 Arquivos Úteis

| Arquivo | Quando Usar |
|---------|------------|
| wallenberg-rotina-diaria-skills-v2_SKILL.md | **Fonte única de verdade** — Referência completa (v3.3.2, inclui Apêndice de bloqueadores/critérios). **Releia a seção "Passo 1" a cada rodada**, não só na primeira vez |
| Checklist_Diaria.html | Durante a rotina seg-qui (visual + timer) — tem o resumo do Passo 1 v3.0 |
| Checklist_Sexta.html | Durante a rotina sexta (visual + timer) — Painel = FEED de eventos, ver item 6 do SKILL.md |

**Removido desta lista (14/09/2026):** `wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md` estava vazio (0 bytes) mas era apontado aqui como "referência completa, 30 min leitura" — quem seguisse essa instrução perderia tempo abrindo um arquivo em branco.

**Removido desta lista (16/09/2026, auditoria de dessincronização — Claudemberg):** `wallenberg_manual_operacional_rotina_diaria_skills.md` (v2.9, preso na versão pré-v3.0 do Passo 1; conteúdo vivo migrado para o Apêndice do SKILL.md) e `GUIA_EXECUCAO_ROTINA_SEXTA_28_08_2026.md` (descrevia o Painel como "% de progresso por projeto", mecanismo que não existe mais). Ambos movidos para `00_HISTORICO/` com aviso de aposentadoria no topo — não os use como referência ativa.

---

## ⚙️ Automação (você não controla)

- **20:00 toda noite:** CronJob gera PDFs das Skills
- **08:00 toda manhã:** Agendador dispara rotina

---

## ❓ Dúvida?

1. Consulte `wallenberg-rotina-diaria-skills-v2_SKILL.md` (seção "PASSOS DETALHE", tem exemplo completo por Gestor/Agente)
2. Releia o passo específico em Checklist_Diaria.html ou Checklist_Sexta.html
3. Se ainda preso, registre em relatório de execução e envie

---

**Status:** ✅ Rotina pronta — v3.0 ativa desde 10/09/2026, rótulos corrigidos 14/09/2026, v3.3.2 (SRE + `/watch:watch` + fronteira crítica de cliente) desde 17/09/2026
