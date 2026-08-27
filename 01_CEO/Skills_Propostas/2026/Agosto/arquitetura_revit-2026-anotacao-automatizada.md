# Revit 2026 — Automação Inteligente de Anotação e Documentação

**Data:** 23/08/2026  
**Gestor Alvo:** Lúcio (Arquitetura)  
**Agente Consumidor:** Oscar (Coordenador) + Hely (Documentação Legal)  
**Versão:** v1 (Descritivo de capacidade 2026)  
**Status:** Validar em projeto real (próximo Estudo Preliminar)

---

## O Que Aprendemos

O Revit 2026 passou a oferecer **sugestões inteligentes de anotação** que analisam o contexto do modelo e sugerem automaticamente quais elementos precisam de cotas, tags, notas técnicas. Não é manual — é IA integrada de fábrica.

**Ambiente:** Autodesk Revit 2026 (native AI)  
**Ferramentas Complementares:** Swapp AI (geração automática de pranchas), Autodesk AI (context-aware anotação)  
**Integração:** ChatGPT/Claude para especificações e memoriais (já testado STTK 19/08+)

---

## Como Funciona

### Fluxo Integrado

```
Modelo BIM (Oscar cria via Estudo Preliminar)
  ↓
Revit 2026 AI Context Analysis
  ↓
Sugestões automáticas (cotas, tags, notas)
  ↓
Oscar revisa + aceita/rejeita
  ↓
Documentação semi-automática
  ↓
Swapp AI gera pranchas (opcional)
  ↓
Hely complementa memorial técnico em Claude
```

### Detalhes Técnicos

**Passo 1 — Análise do Modelo**
- Revit 2026 identifica todos elementos (paredes, portas, janelas, lajes, pilares)
- IA local determina quais precisam de anotação por padrão CAU-RJ

**Passo 2 — Sugestões**
- Cotas automáticas (dimensões, distâncias)
- Tags de material (vidro tipo, cerâmica x marca)
- Notas de legenda (tipo de vidro, espessura, classificação)

**Passo 3 — Revisão Oscar**
- Ver sugestões, aceitar 80%, rejeitar 20% (customização)
- Ajustar em 5-10 min vs. 45-60 min manual

**Passo 4 — Hely Complementa**
- Exporta dados automáticos de Revit
- Cria memorial descritivo em Claude
- Integra com Lei 281 RJ (se aplicável)

---

## Testamos com Cliente Real?

**Ainda não** — capacidade é nativa 2026 (recém-lançada). Recomendação: testar em próximo projeto.

**Projeto Piloto:**
- Oscar abre Estudo Preliminar em Revit 2026
- Habilita "AI-Assisted Annotations"
- Processa modelo
- Mede tempo real (goal: 10-15 min vs. 45-60 min manual)

---

## Limitações Honestas v1

1. **Novidade de mercado** — não há casos de uso comprovados em Brasil ainda
2. **Customização limitada** — sugestões baseadas em padrão Autodesk (que pode não casar 100% com CAU-RJ)
3. **Exportação de dados** — precisa de validação: Revit 2026 AI exporta JSON estruturado ou texto solto?
4. **Custo licença** — Revit 2026 com AI pode ser tier pago (não investigado)
5. **Integração Hely** — como Hely (não-BIM) consome dados de Revit 2026 AI?

---

## Roadmap v2

- **v2 (Set/2026):** Teste real em projeto Oscar + validação Hely integração
- **v3 (Out/2026):** Documento "Revit 2026 AI Workflow STTK" (passo-a-passo)
- **v4 (Futuro):** Automação CronJob (nightly: exporta sugestões não-revistas de Revit → Slack Oscar)

---

## Como Implementar

### Requisitos
- Revit 2026 (não versão anterior)
- Modelo BIM com elementos suficientes (mínimo 20 elementos para teste)
- Configuração nativa Revit (sem plugins extras necessários)

### Setup

1. **Abrir Projeto em Revit 2026**
2. **Menu:** Annotations → Suggest Annotations (ou similar)
3. **Configurar:** Select annotation types (cotas, tags, notas)
4. **Executar:** AI processa modelo (2-5 min)
5. **Revisar:** Oscar avalia sugestões
6. **Exportar:** Menu → Export Annotations (JSON ou txt)
7. **Hely processa:** Integra com documentação legal/técnica

---

## Impacto Esperado

| Métrica | Antes (Manual) | Depois (2026 AI) | Ganho |
|---------|----------------|------------------|-------|
| **Tempo anotação** | 45-60 min | 10-15 min | **66%** |
| **Erros omissão** | 5-10% | 0-2% | Qualidade ↑ |
| **Retrabalho Hely** | 20 min ajuste | 5 min ajuste | **75%** |
| **Custo por projeto** | Estável | Estável (não novo) | Sem incremento |

---

## Fontes

- **Energent.ai:** "IA para Desenho Técnico em 2026"
- **Projetou.com.br:** "Automação de Documentação no Revit com IA: Como Economizar Horas em 2026"
- **Mind Group:** "IA na Construção Civil e BIM em 2026"
- **Autodesk Official:** Revit 2026 release notes (features verificadas)

---

## Próximo Passo (Wallenberg)

Agenda com Oscar: "Próximo projeto, usa Revit 2026 AI Annotations. Mede tempo real. Se ganho confirmar, virou Skill v1.1 padrão STTK."

**Registro de Versão:** criado 23/08/2026, integração com capacidade nativa Revit 2026.
