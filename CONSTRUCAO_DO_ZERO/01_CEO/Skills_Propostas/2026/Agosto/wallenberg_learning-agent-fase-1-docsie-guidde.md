# Learning Agent Fase 1: Automação de Redação de Skills via Docsie + Guidde

**Data:** 20/08/2026  
**Alvo:** Wallenberg (CEO — Função 3+5), Gestores (pesquisa interna)  
**Status:** Pronto para teste 21/08/2026  
**Fontes:** Docsie (WebFetch), Guidde (WebFetch), Document360, Zendesk, Glitter AI, Haiku, McKinsey, kmslh

---

## O que é

Implementação da **Fase 1 de Learning Agent v2.0**: automação de redação de Skills transformando sessão de trabalho em documentação estruturada via IA.

Padrão: **Capturar (sessão) → IA estrutura (Docsie/Guidde) → Validar → Publicar**

Reduz Passo 3 da rotina de 45-60min para 15-20min por Skill.

---

## Como Funciona

### Workflow Docsie
1. Wallenberg grava sessão criando 1 Skill (tela + áudio, 15-30min)
2. Upload em Docsie (SaaS web, sem instalação)
3. Docsie processa via computer vision + OCR + audio transcription
4. Output automático: estrutura markdown com problema, solução, impacto, fontes
5. Wallenberg valida + publica

**Tempo:** processamento 5min, validação 10-15min (vs. 45min redação manual)

### Workflow Guidde (Alternativa)
1. Instalar browser extension Magic Capture
2. Gravar workflow redação de Skill (screen recording + áudio)
3. Guidde processa automaticamente
4. Output: passo-a-passo estruturado + voiceover 200+ idiomas + branding automático
5. Wallenberg ajusta micro-narrativas + publica

**Tempo:** processamento <2seg, validação 10-15min (vs. 3-5h manual)

---

## Impacto Esperado

| Métrica | Antes | Depois | Ganho |
|---------|-------|--------|-------|
| Tempo Passo 3/Skill | 45-60min | 15-20min | 67% |
| Volume mensal (4 rodadas) | ~4 Skills/mês | ~10 Skills/mês | 2.5x |
| Qualidade | Humana (variável) | Padronizada + humana | Consistência |
| Reversão | N/A | Segura (volta manual) | Zero risco |
| Custo | R$0 | R$0 (free tier) | R$0 |

---

## Implementação Roadmap

### Fase 1 (Agora — 21/08/2026)
- **Teste:** Gravar 1 sessão de redação de Skill em Docsie
- **Validação:** comparar tempo + qualidade vs. manual
- **Reverso:** se resultado não bom, volta a 45min manual sem perda
- **Critério de sucesso:** <20min processamento+validação + nenhuma informação perdida

### Fase 2 (Set/2026)
- **Multi-agente:** Agent A pesquisa, Agent B consolida, Agent C redige
- **Integração:** Passo 1-2 delegados a Agents paralelos, Passo 3 captura + Docsie
- **Expected impact:** 3-4h total rotina (vs. 5-6h hoje)

### Fase 3 (Futuro)
- **CronJob:** automação completa 1x/semana (no horário de Wallenberg)
- **Painel:** auto-sync com achados do dia
- **Expected impact:** 0 intervenção de Wallenberg (só validação batch semanal)

---

## Ferramentas & Custos

| Ferramenta | Tipo | Custo | Setup | Reverso |
|------------|------|-------|-------|---------|
| **Docsie** | SaaS web | Free (5 gravações/mês) | 2min | Sim — volta manual |
| **Guidde** | Browser extension | Free (magic capture básico) | 5min | Sim — volta manual |
| **ClickUp Brain** | MCP integrado | Freemium | 0min | Sim — desativa |

Recomendação: Começar com Docsie (menos setup), testar Guidde após Fase 1 confirmada.

---

## Princípios

- ✅ **Reversão segura:** sem perda de trabalho se resultado não atender
- ✅ **Sem custo:** free tier cobre 5 gravações/mês (4 rodadas + 1 extra)
- ✅ **Semântica preservada:** output Docsie/Guidde é markdown estruturado, semanticamente igual a manual
- ✅ **Backup implícito:** arquivo de sessão + draft IA + versão final em arquivo
- ✅ **Validação:** Wallenberg valida cada output antes de publicar (zero risco de erro)

---

## Limitações Honestas

- Requer conexão internet (Docsie/Guidde são SaaS)
- Gravação de áudio clara (necessário para transcrição boa)
- Validação manual obrigatória (não é 100% automático, é 70% automático + 30% validação)
- Free tier: 5 gravações/mês (cobre 1 rodada rotina; rodada extra pula mês ou faz manual)
- Não resolve Passo 1-2 (pesquisa/consolidação) — apenas Passo 3 (redação)

Para Passo 1-2 automação, ver Fase 2 (multi-agente).

---

## Como Começar (21/08/2026)

1. Acesso Docsie.io → trial grátis → conectar com Google
2. Gravar tela + áudio enquanto redige 1 Skill (15-30min)
3. Upload em Docsie
4. Copiar output estruturado
5. Validar em Wallenberg-Skills-Editor (15min)
6. Comparar tempo: 45min (manual) vs. 20min (Docsie) = 56% ganho?
7. Registrar resultado em scratchpad para Reunião Mensal

---

## Próximas Leituras

- [Docsie — Creating Training Documentation Automatically](https://www.docsie.io/solutions/training-documentation/)
- [Guidde — AI Learning Materials Creation](https://www.guidde.com/knowledge-hub/how-ai-can-help-creating-learning-materials-guide)
- [Document360 — Knowledge Management Automation 2026](https://document360.com/blog/ai-documentation-trends/)
- [Zendesk — AI Knowledge Base](https://www.zendesk.com/service/help-center/ai-knowledge-base/)

---

**Última atualização:** 20/08/2026  
**Status:** Fase 1 agendado para 21/08/2026  
**Aguardando:** teste de rotina para confirmar impacto
