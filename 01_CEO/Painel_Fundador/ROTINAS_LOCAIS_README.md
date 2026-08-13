# 🔄 Rotinas Locais — Otimização de Tokens STTK

**Versão:** 15/08/2026  
**Status:** Painel atualizado com Semana 2 validada (45-67% acumulado)

---

## 🎯 Rotinas Disponíveis

Existem **2 rotinas principais** para escolher:

### 1️⃣ **Rotina Rápida** — Sincronizar Painel
- **Arquivo:** `sincronizar_painel.bat`
- **O que faz:** Copia painel atualizado do repositório para seu computador
- **Tempo:** ~2 segundos
- **Use quando:** Painel foi atualizado no repositório e você quer a versão mais recente

### 2️⃣ **Rotina Completa** — Otimização de Tokens (Recomendado)
- **Arquivo:** `rotina_otimizacao_tokens.bat`
- **O que faz:** Valida Items 4-6, sincroniza painel, gera relatório diário
- **Tempo:** ~5-10 segundos
- **Use quando:** Quer executar a validação completa da otimização (diariamente recomendado)

---

## 📋 Opção 1: Rotina Rápida — Sincronizar Painel (Manualmente)

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

## 📋 Opção 2: Rotina Completa — Validação + Sincronização (Manualmente)

### Passo 1: Baixe o script batch

Coloque este arquivo na sua máquina:
```
rotina_otimizacao_tokens.bat
```

### Passo 2: Ajuste os caminhos (se necessário)

Abra `rotina_otimizacao_tokens.bat` em um editor de texto e verifique:

```batch
set REPO_PASTA=D:\sttk-organismo          ← Caminho do seu repositório local
set PYTHON_EXE=python                     ← Caminho do Python (deixar "python" se no PATH)
```

Se os caminhos estiverem diferentes, atualize-os.

### Passo 3: Execute o script

**Opção A - Duplo clique:**
- Clique 2x em `rotina_otimizacao_tokens.bat`
- Aguarde ver `[OK] Rotina completada com sucesso!`

**Opção B - Via Prompt de Comando:**
```cmd
cd C:\caminho\do\script
rotina_otimizacao_tokens.bat
```

### O que a rotina valida?

✅ **Item 4: SQLite Legislação**
- Verifica se banco de dados existe e tem integridade
- Testa se queries executam em <1ms
- Confirma 14+ registros de legislação

✅ **Item 5: Google Drive Cache**
- Valida cache JSON de arquivos recentes
- Confirma sincronia com Drive (timestamp)
- Verifica que diff logic funciona (novos/modificados/inalterados)

✅ **Item 6: Skills JSON**
- Valida SKILL.index.json (metadata do skill)
- Valida Skills_Propostas/indice.json (17 propostas)
- Confirma JSON parsing OK

✅ **Sincronização de Painel**
- Copia painel atualizado para sua pasta local
- Cria backup automático da versão anterior

✅ **Gera Relatório Diário**
- Registra resultado de cada validação
- Arquivo salvo em: `03_REGISTROS_DIARIOS/2026/08/2026-08-15.md`

### Resultado

```
[OK] Rotina completada com sucesso!
     ✅ Item 4 (SQLite): Validado
     ✅ Item 5 (Drive Cache): Validado
     ✅ Item 6 (Skills JSON): Validado
     ✅ Painel: Sincronizado
     ✅ Registro: Gerado
```

---

## ⏰ Agendar Execução Automática (Agendador de Tarefas Windows)

Você pode agendar **qualquer uma das rotinas** para executar automaticamente.

### Passo 1: Abra o Agendador de Tarefas

Windows + R → Digite: `taskschd.msc` → Enter

### Passo 2: Criar Nova Tarefa

1. **Painel Esquerdo:** Clique em "Biblioteca do Agendador de Tarefas"
2. **Painel Direito:** Clique em "Criar Tarefa Básica..."
3. **Nome:** `Rotina Completa STTK` (ou `Sincronizar Painel STTK` se preferir a rápida)
4. **Descrição:** "Executa validação de tokens e sincroniza painel"

### Passo 3: Configurar Gatilho

1. Abra aba **"Gatilhos"**
2. Clique em **"Novo..."**
3. Escolha quando executar:
   - ✅ **Ao iniciar** (executa quando você ligar o PC)
   - ✅ **Diariamente** às 09:00 (executa toda manhã)
   - ✅ **A cada hora** (mantém sempre atualizado)

### Passo 4: Configurar Ação

1. Abra aba **"Ações"**
2. Clique em **"Novo..."**
3. Preencha:
   - **Programa/script:** `C:\caminho\completo\rotina_otimizacao_tokens.bat`
   - **Iniciar em:** `C:\caminho\da\pasta`
4. Clique **"OK"**

### Passo 5: Configurações (Opcional)

Na aba **"Configurações"**, marque:
- ✅ "Permitir que a tarefa seja executada sob demanda"
- ✅ "Se a tarefa falhar, reintentar após: 1 minuto"

### Passo 6: Salve

Clique **"OK"** → Insira sua senha → Pronto!

---

## 🧪 Testar as Rotinas

### Teste Manual - Rotina Rápida

```cmd
cd D:\sttk-organismo\01_CEO\Painel_Fundador
sincronizar_painel.bat
```

Você deve ver:
```
[OK] Painel sincronizado com sucesso!
     Destino: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
```

### Teste Manual - Rotina Completa

```cmd
cd D:\sttk-organismo\01_CEO\Painel_Fundador
rotina_otimizacao_tokens.bat
```

Você deve ver:
```
✅ Rotina completada com sucesso!
   ✅ Item 4 (SQLite): Validado
   ✅ Item 5 (Drive Cache): Validado
   ✅ Item 6 (Skills JSON): Validado
   ✅ Painel: Sincronizado
   ✅ Registro: Gerado

Total: 5/5 OK
```

### Teste Agendado

Se configurou automático:
1. Abra **Agendador de Tarefas**
2. Clique em **"Rotina Completa STTK"** (ou a que criou)
3. Clique em **"Executar"** (botão direito)
4. Verifique os registros em `03_REGISTROS_DIARIOS/`

---

## 🔧 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Arquivo não encontrado" | Verifique os caminhos em `.bat` (REPO_PASTA, LOCAL_PASTA, etc) |
| "Acesso negado" | Execute como Administrador (botão direito → "Executar como administrador") |
| "Python não encontrado" | Instale Python 3.8+ ou adicione ao PATH: Painel de Controle → Variáveis de Ambiente → Path |
| "SQLite não encontrado" | Verifique se `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/indice_sqlite/legislacao_index.sqlite3` existe |
| "Cache não encontrado" | Verifique se `01_CEO/_ferramentas/drive_cache/cache_recentes.json` existe |
| Painel ainda velho no navegador | Pressione **Ctrl+Shift+R** para limpar cache do navegador |
| Agendador não executa | Abra **Agendador de Tarefas** → clique com botão direito na tarefa → "Executar" → verifique última execução |
| Rotina não sincroniza painel | Verifique se pasta `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador` existe; crie manualmente se não |

---

## 📞 Próximas Rotinas Planejadas

Quando os itens forem executados, vamos criar rotinas para:
- **Item 7 (19/08):** Atualizar cache de Prompt Caching (rotina_prompt_caching.bat)
- **Item 8 (20/08):** Sincronizar Sistema de Gestão Notion (rotina_notion_sync.bat)
- **Validação Final (21/08):** Gerar relatório de economia real (gerar_relatorio_final.bat)

---

## 📊 Resumo de Arquivos

```
01_CEO/Painel_Fundador/
├── painel_fundador_sttk.html                ← Painel principal (origem)
├── sincronizar_painel.bat                   ← Rotina rápida (painel apenas)
├── sincronizar_painel.py                    ← Versão Python (portável)
├── rotina_otimizacao_tokens.bat             ← Rotina completa (Items 4-6)
├── rotina_otimizacao_tokens.py              ← Implementação Python
└── ROTINAS_LOCAIS_README.md                 ← Este arquivo

03_REGISTROS_DIARIOS/
└── 2026/08/
    └── 2026-08-15.md                        ← Relatório de execução (gerado automaticamente)
```

---

**Criado em:** 15/08/2026  
**Atualizado em:** 15/08/2026  
**Wallenberg (CEO STTK)**
