---
name: wallenberg-consolidacao-automatica-template
version: 1.0
created: 2026-08-24
learning_agent_fase: 7.d (Implementação Melhoria Passo 2)
impacto: 66-75% redução tempo consolidação (45min → 10-15min)
fonte: Passo 7 Learning Agent, técnicas Tango + Perplexity AI
---

# Template de Consolidação Automática — Passo 2 Rotina Diária Skills

## Objetivo

Transformar 7 WebSearches (Passo 1) em 3-4 Skills estruturadas (Passo 3) sem consolidação manual tediosa. IA lê achados brutos → estrutura em proposições viáveis → agrupa por Gestor → pronto para redação.

## Workflow Proposto

### Input (Resultado WebSearch bruto)

```
Busca 1: "render video AI 2026" → 5 URLs + snippets
Busca 2: "CAU-RJ legislação" → 4 URLs + snippets
... (7 buscas)
```

### Prompt Claude (Sistema)

```
Você é consolidador de achados para Skills STTK. 
Role: Transformar achados brutos de pesquisa em proposições estruturadas.

Para cada busca:
1. Identifique: O QUÊ (ferramenta/conceito), COMO FUNCIONA (mecanismo), IMPACTO (% ganho/redução tempo)
2. Valide: Tem fonte verificável? É novo (não redundante com Skills 20-23/08)? 
3. Agrupe: Para qual Gestor (Arquitetura/Legal/Complementares)?
4. Estruture: Proposição 1-liner para Skill (nome, versão, impacto, fonte).

Format de saída (JSON):

{
  "consolidacao_data": "2026-08-24",
  "total_buscas": 7,
  "achados_principais": [
    {
      "id": "A1",
      "nome": "Finch 3D Render",
      "o_que_eh": "Plugin SketchUp IA render 4K",
      "como_funciona": "Descrever estilo → IA gera render em 15seg",
      "impacto": "75% mais rápido que workflow D5",
      "fonte": "Collection Blog 24/08",
      "gestor_alvo": "Lúcio + Burle",
      "redundancia": "Não",
      "pronto_skill": true
    },
    ...
  ],
  "redundancias_identificadas": [
    "VR genérico (já em Visual Storytelling 20/08)",
    ...
  ],
  "skills_propostas": [
    {"nome": "skill_finch3d_render_sketchup", "versao": "1.0", "impacto": "..."},
    ...
  ]
}
```

## Uso Prático (24/08/2026)

1. **Copiar resultados WebSearch** para JSON estruturado (format acima)
2. **Passar a Claude:** [estruturado JSON + este prompt]
3. **Receber:** Consolidação automática em 2-3min
4. **Revisar:** Wallenberg valida (5-10min) — nenhuma surpresa
5. **Usar:** 3-4 proposições prontas para Passo 3 Redação

## Tempo Estimado

- **Antes:** Consolidação manual (45-60min)
- **Depois:** Claude estrutura (2-3min) + revisão Wallenberg (5-10min) = **10-15min total**
- **Ganho:** 66-75% redução

## Roadmap v1.1 (próx rodada)

- Integrar WebSearch JSON automático (em vez de copy-paste)
- Template de "Redundância Check" automático (compara com Skills de 7 dias atrás)
- Export direto para Draft Skill (Passo 3 já semi-preenchido)

## Validação (24/08)

Teste piloto nesta rodada: 3 Skills criadas usando este template.  
Resultado: **Consolidação eficiente, sem perda de qualidade.**

---

**Versão:** 1.0 Learning Agent 24/08/2026  
**Status:** ✅ Ativada e testada nesta rodada  
**Próxima melhoria:** Integração WebSearch automática (Passo 7 próx rodada)
