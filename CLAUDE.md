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

**Próximo:** Atualizar `.claude/agents/*.md` para referenciar slices apropriados.

---

**Última atualização:** 27/07/2026  
**Consolidação:** Semana 1, Item 2 de Otimização de Tokens STTK
