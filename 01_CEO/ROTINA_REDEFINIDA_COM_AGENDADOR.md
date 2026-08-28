# ⚙️ Como Funciona a Automação

---

## PARTE 1: AGENDADOR (08:00 toda manhã)

### O que faz

Dispara a rotina automaticamente **08:00** sem você fazer nada.

### Como funciona

`
08:00 → Agendador ativa → Rotina começa
      → Notificação chega ("Rotina iniciada")
      → Você trabalha seg-qui (Passos 1-5)
      → Você trabalha sexta (Passos 6-10)
      → Você envia relatório ao fim
`

### O que você precisa fazer

- Nada! Agendador dispara automaticamente
- Você apenas **segue os passos** conforme checklists

---

## PARTE 2: CRONJOB PDF (20:00 toda noite)

### O que faz

Gera **PDF** automático de cada Skill criada.

### Como funciona

`
Durante o dia você cria:
  1. arquivo_skill_1.md
  2. arquivo_skill_2.md
  3. arquivo_skill_3.md

20:00 (noite) → CronJob ativa
             → Lê todos os .md criados
             → Gera PDF gêmeo de cada
             → Salva em Skills_Propostas/2026/Agosto/

Resultado:
  1. arquivo_skill_1.md + arquivo_skill_1.pdf
  2. arquivo_skill_2.md + arquivo_skill_2.pdf
  3. arquivo_skill_3.md + arquivo_skill_3.pdf
`

### O que você precisa fazer

- Nada! CronJob funciona automaticamente
- PDFs aparecem sozinhos às 20:00

---

## Fluxo Completo de 24 horas

`
DIA: SEGUNDA-FEIRA

08:00 → ✅ Agendador dispara (você recebe notificação)
08:05 → 📋 Você abre Checklist_Diaria.html
08:10 → 🔍 Passo 1: Pesquisa Externa (15-20 min)
08:35 → 📊 Passo 2: Consolidação (10 min)
08:50 → ✍️  Passo 3: Redação (20 min)
09:10 → 💾 Passo 4: Salvamento (5 min)
09:15 → 🛠️  Passo 8: Ferramentas (10 min)
09:25 → ✅ Execução completa! Você envia relatório.

Durante o dia:
  - Você criou 3 Skills (.md)
  - Salvas em Skills_Propostas/2026/Agosto/

20:00 → 🤖 CronJob ativa automaticamente
      → Lê os 3 .md criados
      → Gera 3 PDFs gêmeos
      → Salva no mesmo lugar
      → Relatório de conclusão do CronJob enviado

RESULTADO FINAL:
  Skills_Propostas/2026/Agosto/ contém:
    1. skill_1.md + skill_1.pdf
    2. skill_2.md + skill_2.pdf
    3. skill_3.md + skill_3.pdf
`

---

## Se Algo Der Errado

### Agendador não dispara

**Causa:** Servidor de agendamento fora do ar  
**Ação:** Você começa rotina manualmente 08:00  
**Impacto:** Sem notificação, mas rotina roda normalmente

### CronJob não gera PDFs

**Causa:** Servidor de automação fora do ar  
**Ação:** PDFs gerados manualmente (comando manual)  
**Impacto:** Atraso de ~24h, mas Skills continuam úteis em .md

---

## Resumo

| Componente | Frequência | Ação do Wallenberg |
|------------|-----------|-------------------|
| **Agendador** | 08:00 toda manhã | Recebe notificação, começa rotina |
| **CronJob PDF** | 20:00 toda noite | Nenhuma — funciona sozinho |

**Filosofia:** Você foca **criatividade + decisão** (Passos 1-10). A máquina cuida de **repetição + formatação** (geração de PDFs).

---

**Próximo:** Leia wallenberg_rotina_diaria_skills_v2_7_REDEFINIDO.md pra detalhes completos.
