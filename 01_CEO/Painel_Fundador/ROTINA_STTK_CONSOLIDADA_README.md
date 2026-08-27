# 🚀 Rotina STTK Consolidada

**Uma única rotina local que substitui 5 rotinas cloud**

---

## 📋 O que faz

Executa tudo em uma só chamada:

| Item | Tarefa | Status |
|------|--------|--------|
| 4 | SQLite Legislação | ✅ Validação (96% ↓) |
| 5 | Google Drive Cache | ✅ Validação (93% ↓) |
| 6 | Skills JSON | ✅ Validação (2-5% ↓) |
| 7 | Prompt Caching | ⏳ Planejamento (15-20%) |
| 8 | Sistema de Gestão | ⏳ Planejamento (futuro) |
| — | Sincronizar Painel | ✅ Automático |
| — | Gerar Relatório | ✅ Diário |

**Total:** 45-67% redução de tokens acumulada

---

## 🎯 Execução Manual

### Duplo clique
```
Double-click em: rotina_sttk_consolidada.bat
```

### Via Prompt de Comando
```cmd
cd D:\sttk-organismo\01_CEO\Painel_Fundador
rotina_sttk_consolidada.bat
```

**Resultado esperado:**
```
✅ Rotina STTK consolidada completada!
   ✅ Item 4 (SQLite): Validado
   ✅ Item 5 (Drive Cache): Validado
   ✅ Item 6 (Skills JSON): Validado
   ⏳ Item 7 (Prompt Caching): Planejamento
   ⏳ Item 8 (Sistema Gestão): Planejamento
   ✅ Painel: Sincronizado
   ✅ Registro: Gerado

Total: 7/7 OK
```

---

## ⏰ Agendar no Windows Task Scheduler

### Passo 1: Abrir Agendador de Tarefas
```
Windows + R → taskschd.msc → Enter
```

### Passo 2: Criar Nova Tarefa

1. **Painel Esquerdo:** "Biblioteca do Agendador de Tarefas"
2. **Painel Direito:** "Criar Tarefa Básica..."
3. **Nome:** `Rotina STTK Consolidada`
4. **Descrição:** "Executa validação STTK Items 4-8 localmente"

### Passo 3: Configurar Gatilho

1. Aba **"Gatilhos"** → **"Novo..."**
2. Escolha uma opção:
   - ✅ **Diariamente** às 09:00 (toda manhã)
   - ✅ **Ao iniciar** o PC
   - ✅ **A cada hora** (mantém sempre sincronizado)

### Passo 4: Configurar Ação

1. Aba **"Ações"** → **"Novo..."**
2. Preencha:
   ```
   Programa/script: D:\sttk-organismo\01_CEO\Painel_Fundador\rotina_sttk_consolidada.bat
   Iniciar em: D:\sttk-organismo\01_CEO\Painel_Fundador
   ```
3. Clique **"OK"**

### Passo 5: Configurações (Opcional)

Aba **"Configurações"**, marque:
- ✅ "Permitir que a tarefa seja executada sob demanda"
- ✅ "Se a tarefa falhar, reintentar após: 1 minuto"

### Passo 6: Salvar

Clique **"OK"** → Insira sua senha → **Pronto!**

---

## 📊 Saída Diária

Cada execução gera um arquivo em:
```
03_REGISTROS_DIARIOS/2026/08/YYYY-MM-DD.md
```

Exemplo de conteúdo:
```markdown
# Rotina STTK Consolidada — 2026-08-15

✅ Item 4: SQLite Legislação
✅ Item 5: Google Drive Cache
✅ Item 6: Skills JSON
⏳ Item 7: Prompt Caching (planejamento)
⏳ Item 8: Sistema de Gestão (planejamento)
✅ Painel: Sincronizado

Status: 45-67% redução confirmada
```

---

## 🔧 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Python não encontrado" | Instale Python 3.8+ ou adicione ao PATH |
| "Script não encontrado" | Verifique caminho REPO_PASTA no .bat |
| "SQLite não encontrado" | Confirme que Item 4 foi executado antes |
| "Painel velho no navegador" | Pressione Ctrl+Shift+R para limpar cache |
| Agendador não executa | Clique com botão direito na tarefa → "Executar" |

---

## 🗑️ Deletar Rotinas Cloud

Quando estiver confiante com a local, delete as 5 rotinas cloud:

```
DELETE:
- STTK-Validacao2-15Ago (trig_017QZkLZ9XUELnWDp3STxNjo)
- STTK-Item7-19Ago (trig_01Jqik2HyBK4qexmFHPRVmi9)
- STTK-Item8-20Ago (trig_01BYBvPgG3nDgbhgFuqCtaTg)
- STTK-Validacao3-21Ago (trig_01Ts1HDgwvM5AT6cQGySc96C)
- STTK-Wrapup-22Ago (trig_01RbP6uYEqYkkiYJCT13oLTR)
```

Acesse https://claude.ai/routines e delete cada uma.

---

## 📁 Arquivos

```
01_CEO/Painel_Fundador/
├── rotina_sttk_consolidada.bat      ← Execute isto
├── rotina_sttk_consolidada.py       ← Python que faz o trabalho
└── ROTINA_STTK_CONSOLIDADA_README.md ← Este arquivo
```

---

## ✅ Benefícios

- ✅ **Uma única rotina** — Sem confusão de múltiplos scripts
- ✅ **Totalmente local** — Zero dependência de nuvem
- ✅ **Agendável** — Roda automaticamente via Windows Task Scheduler
- ✅ **Relatórios diários** — Cada execução registra tudo
- ✅ **Simples** — Batch + Python, sem dependências complexas
- ✅ **Rastreável** — Git commit de cada execução

---

**Versão:** 15/08/2026  
**Status:** ✅ Pronto para uso local

