# ⚙️ AUTOMAÇÃO — Instruções de Configuração

**Status:** Pronto para Claudemberg configurar  
**Data:** 28/08/2026  
**Responsável:** Claudemberg (Técnico)  

---

## 📌 O Que Precisa Ser Configurado

### 1. AGENDADOR — Dispara rotina 08:00 toda manhã

**Nome:** Wallenberg Rotina Diária Skills v2.7 — Agendador  
**Frequência:** Diária (seg-dom)  
**Hora:** 08:00 (UTC-3)  
**Ação:** Dispara shell script ou MCP que notifica Wallenberg  
**Instrução Enviada Para:** Wallenberg via notificação  

**Ferramenta Sugerida:**
- /schedule skill (se disponível)
- CronCreate MCP (se disponível)
- Manual com crontab -e no servidor

**Comando Sugerido (Linux/Mac):**
\\\ash
0 8 * * * /path/to/script/wallenberg_rotina_disparo.sh
\\\

**Comando Sugerido (Windows Task Scheduler):**
\\\
schtasks /create /tn "Wallenberg Rotina Diária" /tr "C:\\path\\to\\script.bat" /sc DAILY /st 08:00
\\\

**Notificação de Sucesso:**
\\\
✅ AGENDADOR ATIVO — Rotina dispara 08:00
📌 Acorde: Wallenberg (email/webhook/Slack)
\\\

---

### 2. CRONJOB — Gera PDFs 20:00 toda noite

**Nome:** Wallenberg Rotina Diária Skills v2.7 — CronJob PDF  
**Frequência:** Diária (seg-dom)  
**Hora:** 20:00 (UTC-3)  
**Ação:** Lê Skills .md de Skills_Propostas/2026/Agosto/ e gera PDFs gêmeos  
**Saída:** PDF salvo no mesmo local do .md  

**Ferramenta Sugerida:**
- Pandoc ou wkhtmltopdf (CLI)
- Ferramenta MCP de geração de PDF (se existe)

**Script Shell (Exemplo):**
\\\ash
#!/bin/bash
SOURCE_DIR="/path/to/Skills_Propostas/2026/Agosto"
for md_file in ""/*.md; do
    [ -f "" ] || continue
    pdf_file="\.pdf"
    pandoc -f markdown -t pdf "" -o ""
done
\\\

**Comando no Crontab:**
\\\ash
0 20 * * * /path/to/script/wallenberg_rotina_pdf_gerador.sh
\\\

**Notificação de Sucesso:**
\\\
✅ CRONJOB EXECUTADO — 3 PDFs gerados
📌 Arquivos em: Skills_Propostas/2026/Agosto/
\\\

---

## 🔧 Checklist de Configuração (Claudemberg)

### Agendador
- [ ] Ferramenta selecionada (skill /schedule, CronCreate, manual, etc)
- [ ] Comando testado (08:00 dispara sem erros)
- [ ] Notificação funciona (Wallenberg recebe)
- [ ] Timezone correto (UTC-3 São Paulo)

### CronJob
- [ ] Ferramenta selecionada (Pandoc, wkhtmltopdf, etc)
- [ ] Script criado e testado (gera PDFs corretamente)
- [ ] Comando testado (20:00 dispara sem erros)
- [ ] Permissões de arquivo OK (script pode ler/escrever)

---

## 🚀 Teste Prático (Antes de Lançar)

1. **Agendador:**
   - Agende para 08:05 (5 min de teste)
   - Dispare manualmente
   - Confirme notificação

2. **CronJob:**
   - Crie arquivo teste: 	este_skill.md
   - Agende CronJob para 20:05 (5 min)
   - Confirme PDF 	este_skill.pdf foi criado
   - Delete arquivo teste

3. **Integração:**
   - Se ambos passaram, configure para 08:00 e 20:00 reais
   - Primeira rotina seg 29/08 servirá como teste completo

---

## 📋 Pós-Configuração (Claudemberg)

Após configurar ambos, preencha este checklist:

- [ ] Agendador testado e ativo
- [ ] CronJob testado e ativo
- [ ] Wallenberg recebe notificação 08:00
- [ ] Wallenberg recebe PDFs 20:00
- [ ] Timeline: Primeira execução 29/08 08:00

---

## 🎯 Próximo Passo

**Wallenberg (Executor):** Aguarde aprovação automação  
**Claudemberg (Técnico):** Siga checklist acima  
**Resultado:** 29/08 08:00 Agendador dispara primeira rotina

---

**Versão:** 1.0  
**Criado:** 28/08/2026  
**Aprovado por:** (Pendente Claudemberg)
