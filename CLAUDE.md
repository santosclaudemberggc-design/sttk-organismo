# Sistema Orgânico STTK — CLAUDE.md (Índice de Slices)

**Versão consolidada em 27/07/2026**

Dependendo do seu papel, carregue o slice apropriado:

---

## 📋 Slices Especializados

### Para Wallenberg (CEO)
📄 [`CLAUDE_wallenberg_slice.md`](./CLAUDE_wallenberg_slice.md)  
**Conteúdo:** Regra de Ouro, 21 Princípios, 12 Funções, Reuniões, Drenagem de Fila, Hierarquia, 3 Camadas, 4 Níveis, Arquivo de Estado  
**Tamanho:** ~25 KB | **Redução:** 150 KB → 25 KB

---

### Para Gestores (Legal, Arquitetura, Complementares, Fechamento)
📄 [`CLAUDE_gestor_slice.md`](./CLAUDE_gestor_slice.md)  
**Conteúdo:** Autonomia, 4 Níveis, Contratação de Agentes, Drenagem de Fila, Cascata de Formação, Obrigações, Reuniões  
**Tamanho:** ~15 KB | **Redução:** 150 KB → 15 KB

---

### Para Agentes (Execução)
📄 [`CLAUDE_agente_slice.md`](./CLAUDE_agente_slice.md)  
**Conteúdo:** Arquivo de Estado (obrigatório), Cadeia de Comando, Execução, Obediência & Sinalização, 21 Princípios, 3 Camadas, 4 Níveis, Fronteiras  
**Tamanho:** ~20 KB | **Redução:** 150 KB → 20 KB

---

## ⚙️ AULA CLAUDE — regras operacionais (TODOS os papéis, sem exceção)

📄 Aula completa: [`D:\CONSELHO\AULA-CLAUDE.md`](../CONSELHO/AULA-CLAUDE.md) — **dono: `guia-claude`**

Abaixo, o espelho resumido das regras que mais custam token quando ignoradas. **Não edite aqui**
— é cópia; o original é a aula. Travou, ou vai fazer algo fora da sua rotina? Leia a aula antes
de tentar, não depois de falhar três vezes.

1. `PowerShell` (5.1) para Windows/cmdlet/`.exe`; `Bash` (Git Bash/POSIX) para `git` e pipe de texto. Não misture — errar o shell disfarça o erro real.
2. PowerShell 5.1 **não tem** `&&`, `||`, `?:`, `??`, `?.` nem `-AsHashtable`. Condicional: `A; if ($?) { B }`.
3. Caminho com espaço **sempre** entre aspas (esta pasta tem espaços no nome).
4. Arquivo: `Read`, `Grep`, `Glob`, `Edit`, `Write` — nunca `cat`, `type`, `findstr`, `Get-Content`, `Select-String`, `Get-ChildItem -Recurse`.
5. `Read` antes de `Edit`, e antes de `Write` em arquivo existente — senão falha.
6. Depois de editar, **não releia** para conferir: se falhasse, teria dado erro.
7. `Edit`: `old_string` literal, indentação inclusa, único no arquivo. Ao copiar do `Read`, tire o número de linha e o tab.
8. Ferramenta fora do seu `tools` **não existe para você**: reporte a limitação, não procure atalho.
9. Permissão negada é decisão de Claudemberg, não bug: mude a abordagem.
10. Chamadas independentes vão no **mesmo bloco**, em paralelo.
11. `InputValidationError` numa ferramenta MCP = schema não carregado → `ToolSearch` com `select:a,b,c`, **tudo numa chamada só**.
12. Nome de ferramenta MCP tem UUID: leia do `settings.json` ou do seu frontmatter — nunca de memória.

---

## 📊 Impacto de Tokens

| Métrica | Antes | Depois | Redução |
|---------|-------|--------|---------|
| Arquivo carregado | 150 KB (sempre) | 15-25 KB (por role) | **80-90% ↓** |
| Overhead de contexto | Completo em toda conversa | Apenas o necessário | ~8-12% economia |

---

## 📚 Documentação Consolidada

Para detalhes **ainda mais** compactados:

- [`consolidated_essencia.md`](./memory/projeto/consolidated_essencia.md) — Wallenberg + 12 Funções + Princípios + Níveis + 3 Camadas
- [`consolidated_estrutura.md`](./memory/projeto/consolidated_estrutura.md) — Gestores + Agentes + Fluxo + Reuniões + Modelo Leilão
- [`consolidated_referencia.md`](./memory/referencia/consolidated_referencia.md) — Integrações + Legislação + Capacidade Real

---

## 🔐 Arquivo Completo (Referência Histórica)

Se você precisar do arquivo **CLAUDE.md completo** (original, não slices):

📄 [`00_HISTORICO/CLAUDE_full_20260727.md`](./00_HISTORICO/CLAUDE_full_20260727.md)  
**Conteúdo:** Tudo (150 KB) | **Uso:** Referência apenas, não carregue em execução

---

## 🎯 Como Usar

1. **Identifique seu papel:**
   - CEO? → Carregue `CLAUDE_wallenberg_slice.md`
   - Gestor? → Carregue `CLAUDE_gestor_slice.md`
   - Agente? → Carregue `CLAUDE_agente_slice.md`

2. **Carregue APENAS o slice do seu role**
   - Reduz overhead de contexto
   - Mantém informação essencial
   - Aponta pra consolidated_* pra detalhes

3. **Para referência completa:**
   - Consulte `consolidated_essencia.md`, `consolidated_estrutura.md`, `consolidated_referencia.md`
   - Ou `00_HISTORICO/CLAUDE_full_20260727.md` (histórico)

---

## ✅ Status

- ✅ 3 slices criados (27/07/2026)
- ✅ Backup do original em 00_HISTORICO
- ✅ Sincronia com pasta organismo (local)
- ✅ Impacto esperado: 8-12% redução tokens/conversa
- ✅ `.claude/agents/*.md` (kelsen, lucio, hely, artigas) referenciam o slice do próprio papel (30/07/2026)

**Próximo:** Validação Items 1 & 2 (zero perda confirmada) — agendada para 31/07/2026.

---

**Última atualização:** 30/07/2026  
**Consolidação:** Semana 1, Item 2 de Otimização de Tokens STTK — CONCLUÍDO
