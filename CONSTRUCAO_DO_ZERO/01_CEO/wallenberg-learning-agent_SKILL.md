---
name: wallenberg-learning-agent
version: 1.0.0
created: 2026-08-13
author: Wallenberg (CEO)
description: "Sistema de Aprendizado Autônomo — Agent integrado que busca vídeos sobre implementação de rotinas, aprende técnicas concretas e melhora os SKILL.md das rotinas Wallenberg automaticamente"
---

# Wallenberg Learning Agent v1.0

## Propósito

Este agente é **integrado como Passo Final** de cada uma das 2 rotinas automáticas de Wallenberg:
- `wallenberg-drenagem-continua` (Função 1 + 4)
- `wallenberg-rotina-diaria-skills` (Função 3 + 5)

Seu objetivo: **transformar as rotinas em sistemas auto-evolucionários** que melhoram continuamente com base em técnicas reais que pessoas já implementam.

## Como Funciona

### Fluxo de Cada Rodada

```
1. BUSCA (Research Phase)
   ├─ WebSearch/WebFetch por vídeos relevantes
   ├─ Temas: "como melhorar rotinas automáticas", "autonomous agents", "knowledge systems"
   └─ 3-5 vídeos de alta qualidade encontrados

2. ANÁLISE (Learning Phase)
   ├─ /watch:watch em cada vídeo via skill `watch:watch`
   ├─ Extrai implementações concretas
   ├─ Identifica padrões e técnicas aplicáveis
   └─ Documenta insights

3. MAPEAMENTO (Mapping Phase)
   ├─ Compara técnicas aprendidas com SKILL.md atual
   ├─ Identifica: gaps, oportunidades, limitações
   └─ "Esta técnica do vídeo X melhora o passo Y"

4. IMPLEMENTAÇÃO (Improvement Phase)
   ├─ Propõe mudanças concretas ao SKILL.md
   ├─ Modifica com backup automático
   └─ Atualiza livro-razão + Painel

5. VALIDAÇÃO (Verification Phase)
   ├─ Verifica mudança por syntax check
   ├─ Testa efeito teórico (não executa real)
   └─ Confirma que não quebrou nada
```

## Temas de Busca por Rotina

### Para `wallenberg-drenagem-continua`

Busca por vídeos sobre:
- "Autonomous agents workflow optimization"
- "Multi-agent system queue management"
- "Delegated autonomy patterns"
- "How to automate delegation workflows"
- "Real examples: autonomous system running itself"
- "Agent state management and reconciliation"

### Para `wallenberg-rotina-diaria-skills`

Busca por vídeos sobre:
- "Knowledge base automation systems"
- "How companies automate research -> documentation"
- "Building skills/knowledge systems automatically"
- "Real examples: AI creating training materials"
- "Learning systems that improve documentation"
- "Knowledge management for teams at scale"

## O Que Pode Mudar (Escopo)

✅ **PODE MODIFICAR no SKILL.md:**
- Adicionar passo otimizado (se estiver logicamente no mesmo nível)
- Reorganizar passos (se melhorar clareza)
- Adicionar técnica/ferramenta alternativa (com `[NOVO]` tag)
- Atualizar descrição de passo (mantendo intent original)
- Adicionar observação técnica (em seção "Técnicas Validadas")

❌ **NÃO PODE MODIFICAR:**
- Remover passo existente (sempre versiona com `[DEPRECADO]`, não deleta)
- Mudar governança/fronteira (aqueles passos são blindados)
- Alterar autonomia de um Gestor (decisão só de Claudemberg)
- Tocar em `pendencias.json` (essa é gerência de fila, não melhoria de rotina)

## Estrutura de Saída

Cada melhoria proposta segue este modelo:

```markdown
## [NOVO v1.1] — 2026-08-14 Learning Agent

**Técnica Aprendida:** [nome da técnica]  
**Fonte:** [vídeo X que ensinou isso]  
**Onde Aplicar:** Passo Y do SKILL.md  
**Mudança Proposta:** [exatamente o que muda]  
**Impacto Teórico:** [o que fica melhor]  
**Implementado:** SIM/NÃO [reason]

---
```

## Integração na Rotina

### Passo 7 (Final) — Drenagem Contínua

Depois de toda rodada de `wallenberg-drenagem-continua`:

```
6. [Passo original: registrar no livro-razão]
7. [NOVO] Learning Agent:
   ├─ Busca vídeos sobre "melhorar gestão de pendências"
   ├─ Aprende de quem já faz isso
   ├─ Melhora o próprio SKILL.md desta rotina
   └─ Documenta evolução no livro-razão
```

### Passo 7 (Final) — Rotina Diária Skills

Depois de toda rodada de `wallenberg-rotina-diaria-skills`:

```
6. [Passo original: atualizar Painel]
7. [NOVO] Learning Agent:
   ├─ Busca vídeos sobre "systems creating knowledge automatically"
   ├─ Aprende como outras orgs fazem pesquisa -> skill
   ├─ Melhora o próprio SKILL.md desta rotina
   └─ Documenta evolução no livro-razão
```

## Versioning

Cada melhoria gera nova versão menor:

```
v1.0 — versão base (antes de Learning Agent)
v1.1 — 1ª melhoria (2026-08-14)
v1.2 — 2ª melhoria (2026-08-15)
v1.3 — 3ª melhoria (2026-08-16)
...
v2.0 — quando acumular 10+ melhorias
```

## Segurança & Limites

**O Learning Agent NÃO pode:**
- Alterar fronteira (cliente, Gates, protocolo)
- Mudar decisão de Claudemberg já ratificada
- Executar ação real (só propor melhorias)
- Criar Gestor/Agente novo
- Deletar passo existente (sempre versiona)

**O Learning Agent PODE:**
- Ler qualquer SKILL.md (da própria rotina)
- Modificar estrutura/conteúdo (com backup)
- Registrar melhoria no livro-razão
- Republicar Painel com evolução
- Rodar /watch:watch em vídeos

## Feedback Loop

Depois de 5 melhorias acumuladas → notificação a Claudemberg na Reunião Semanal:

```
"Learning Agent: 5 melhorias propostas desde [data]:
- [melhoria 1]: resultado
- [melhoria 2]: resultado
...
Aprova incorporar na próxima versão oficial?"
```

---

## Princípios que Guiam Este Agente

1. **Princípio 3** — Qualidade antes de velocidade (testa mudança antes de fazer)
2. **Princípio 6** — Melhoria contínua (cada rodada = iteração)
3. **Princípio 8** — Rastreabilidade (todo vídeo/insight documentado)
4. **Princípio 13** — Autonomia com prestação de contas (melhora sozinho, relata tudo)
5. **Princípio 17** — Aprendizado compartilhado (o que aprende vira Skill pro Gestor)

---

## Status Atual

- ✅ Arquitetura definida (2026-08-13)
- ⏳ Integração em drenagem-continua v2 (em andamento)
- ⏳ Integração em rotina-diaria-skills v2 (em andamento)
- ⏳ Primeira rodada de Learning (após integração)

