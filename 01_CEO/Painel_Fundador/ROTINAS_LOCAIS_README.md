# 🔄 Rotinas Locais — Sincronizar Painel do Fundador STTK

**Versão:** 15/08/2026  
**Status:** Painel atualizado com Semana 2 validada (45-67% acumulado)

---

## 📋 Opção 1: Executar Manualmente (Mais Rápido)

### Passo 1: Baixe o script batch

Coloque este arquivo na sua máquina:
```
sincronizar_painel.bat
```

### Passo 2: Ajuste os caminhos (se necessário)

Abra `sincronizar_painel.bat` em um editor de texto e verifique:

```batch
set REPO_PASTA=D:\sttk-organismo          ← Caminho do seu repositório local
set LOCAL_PASTA=D:\000_ESTRUTURA...       ← Sua pasta de trabalho
```

Se os caminhos estiverem diferentes, atualize-os.

### Passo 3: Execute o script

**Opção A - Duplo clique:**
- Clique 2x em `sincronizar_painel.bat`
- Aguarde aparecer `[OK] Painel sincronizado`

**Opção B - Via Prompt de Comando:**
```cmd
cd C:\caminho\do\script
sincronizar_painel.bat
```

### Resultado

✅ O arquivo será copiado para:
```
D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
```

Um backup anterior será criado automaticamente.

---

## ⏰ Opção 2: Agendar Execução Automática (Agendador de Tarefas Windows)

### Passo 1: Abra o Agendador de Tarefas

Windows + R → Digite: `taskschd.msc` → Enter

### Passo 2: Criar Nova Tarefa

1. **Painel Esquerdo:** Clique em "Biblioteca do Agendador de Tarefas"
2. **Painel Direito:** Clique em "Criar Tarefa Básica..."
3. **Nome:** `Sincronizar Painel STTK`
4. **Descrição:** "Copia painel atualizado do repositório para pasta local"

### Passo 3: Configurar Gatilho

1. Abra aba **"Gatilhos"**
2. Clique em **"Novo..."**
3. Escolha quando executar:
   - ✅ **Ao iniciar** (executa quando você ligar o PC)
   - ✅ **Diariamente** às 09:00 (executa toda manhã)
   - ✅ **A cada hora** (mantém sempre sincronizado)

### Passo 4: Configurar Ação

1. Abra aba **"Ações"**
2. Clique em **"Novo..."**
3. Preencha:
   - **Programa/script:** `C:\caminho\completo\sincronizar_painel.bat`
   - **Iniciar em:** `C:\caminho\da\pasta`
4. Clique **"OK"**

### Passo 5: Configurações (Opcional)

Na aba **"Configurações"**, marque:
- ✅ "Permitir que a tarefa seja executada sob demanda"
- ✅ "Se a tarefa falhar, reintentar após: 1 minuto"

### Passo 6: Salve

Clique **"OK"** → Insira sua senha → Pronto!

---

## 🧪 Testar a Rotina

### Teste Manual

```bash
# No Prompt de Comando, execute:
cd caminho\para\script
sincronizar_painel.bat
```

Você deve ver:
```
[OK] Painel sincronizado com sucesso!
     Destino: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
```

### Teste Agendado

Se configurou automático:
1. Abra **Agendador de Tarefas**
2. Clique em **"Sincronizar Painel STTK"**
3. Clique em **"Executar"** (botão direito)
4. Verifique se o arquivo foi atualizado

---

## 📂 Estrutura de Pastas Esperada

```
D:\
├── sttk-organismo/                    ← Repositório Git
│   └── 01_CEO/Painel_Fundador/
│       └── painel_fundador_sttk.html  ← Arquivo de origem
│
└── 000_ESTRUTURA DEPARTAMENTO DE PROJETO/  ← Sua pasta de trabalho
    └── 01_CEO/Painel_Fundador/
        ├── painel_fundador_sttk.html  ← Cópia sincronizada
        ├── painel_fundador_sttk_backup_20260815_0900.html
        └── painel_fundador_sttk_backup_20260815_1430.html
```

---

## ✅ O que foi atualizado

**Painel agora inclui:**
- ✅ **Semana 2 Validação & Consolidação** (15/08/2026)
- ✅ Item 4: SQLite Legislação (96% ↓ carregamento, queries <1ms)
- ✅ Item 5: Google Drive Cache (93% ↓ chamadas MCP, 3/3 testes)
- ✅ Item 6: Skills JSON (parsing OK, 17 propostas indexadas)
- ✅ **Acumulado:** 45-67% redução de tokens por conversa
- ✅ **Próximo:** Item 7 (Prompt Caching, 19/08/2026)

**Status do Card:**
- Chip: "Semana 2 validada (45-67%)"
- Progresso: 68%
- Próximo: "Semana 3 (Item 7 — Prompt Caching, 19/08)"

---

## 🔧 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Arquivo não encontrado" | Verifique os caminhos em `sincronizar_painel.bat` |
| "Acesso negado" | Execute como Administrador (botão direito → "Executar como administrador") |
| Painel ainda velho no navegador | Pressione **Ctrl+Shift+R** para limpar cache |
| Agendador não executa | Abra **Agendador de Tarefas** → clique com botão direito na tarefa → "Executar" |

---

## 📞 Próximas Rotinas Planejadas

Quando os itens forem executados, vamos criar rotinas para:
- **Item 7 (19/08):** Atualizar cache de Prompt Caching
- **Item 8 (20/08):** Sincronizar Sistema de Gestão (Notion)
- **Validação Final (21/08):** Gerar relatório de economia real

---

**Criado em:** 15/08/2026  
**Wallenberg (CEO STTK)**
