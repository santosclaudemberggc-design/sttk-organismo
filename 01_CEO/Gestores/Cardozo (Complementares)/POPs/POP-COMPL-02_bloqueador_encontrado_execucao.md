---
titulo: POP-COMPL-02 — Bloqueador Encontrado Durante Execução
dono: Cardozo (Gestor Complementares)
criado_em: 2026-09-02
gatilho_de_criacao: Varredura de melhoria (Passo 7) da rotina wallenberg-drenagem-continua v2.3, 02/09/2026. Padrão recorrente identificado em 2 casos de teste (Exame 2 Caso 3, Exame 3 "teste maldoso", 31/08/2026) — quando um Agente ou Oscar (Coordenador de Arquitetura) identifica incompatibilidade/colisão/lacuna técnica após início de execução, qual é meu protocolo de resposta?
precedente_de_forma: POP-LEGAL-06 (Kelsen, checagem preventiva) e REGRA-ARQ-01 (Lúcio, pressão comercial) — Gestor formaliza POP próprio para padrão recorrente.
status: ativo
autonomia: POP próprio de Gestor (Função 6 ampliada 27/07/2026) — não altera escopo comercial nem hierarquia, apenas operacionaliza a Regra de Ouro da Validação já fixada em 14/08/2026.
---

# POP-COMPL-02 — Bloqueador Encontrado Durante Execução

## 1. Objetivo

Padronizar minha resposta quando um Agente (Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin)
ou Oscar (Coordenador de Arquitetura, parceiro de Lúcio) identifica uma incompatibilidade, colisão,
ou lacuna técnica **durante execução** — não na validação inicial de Briefing.

Exemplos:
- Pilar estrutural (Baumgart) bate com prumada de hidrossanitário (Saturnino).
- Quadro de vidro interior (Tenreiro) não cabe em parede com pass-through (Landell).
- Material de piso (Tenreiro) exige carga estrutural não prevista no Briefing (Baumgart).
- Reuso de água (Saturnino) exige espaço para filtro não planejado em paisagismo (Glaziou).

## 2. Quando aplicar

- Um Agente sinaliza: "Achei incompatibilidade com outra disciplina".
- Oscar sinaliza: "Colisão de elemento estrutural com hidro/elétrico/interior/paisagismo".
- Wallenberg sinaliza: "Aviso de risco/incompatibilidade encontrada em anteprojeto antes de apresentar".
- **Nunca** em validação inicial de Briefing — para isso valer POP-COMPL-01.

## 3. Protocolo de resposta

### 3.1 Recebimento e diagnóstico

1. Quando recebi o aviso (de Agente, Oscar ou Wallenberg), peço esclarecimento **imediato**:
   - Qual é a incompatibilidade exata? (não "não cabe", mas "coluna C4 10×50 bate com tubulação φ50 de hidro a 1,50m de altura").
   - Qual disciplina(s) está(ão) afetada(s)?
   - É incompatibilidade real (projeto A viola projeto B) ou dúvida de escopo (A não sabe se pode fazer X)?

2. Diagnostico se é **Erro de Briefing (lacuna)** ou **Erro de Coordenação (incompatibilidade)**:
   - **Erro de Briefing:** O Briefing não prevenía o conflito porque faltava informação. Ex: "Briefing não especificava largura de passeio → Landell previu laje de sobressalência → bate com pilar".
   - **Erro de Coordenação:** O Briefing prevenía, mas um dos Agentes não respeitou ou Oscar não avisou a tempo. Ex: "Briefing dizia 'pilar C4 a 8m da parede' → Saturnino colocou prumada a 7,8m".

### 3.2 Ação se Erro de Briefing

1. **Bloco execução** do Agente responsável (aquele que seria afetado pelo esclarecimento faltante).
2. **Escalo a Wallenberg** com item específico: `"Briefing não cobre <item X> — sem isso, <Agente Y> fica sem requisito. Peço a Lúcio esclarecer com cliente."`
3. Os **outros Agentes** seguem normalmente — só a disciplina afetada pela lacuna espera.
4. Registro no meu arquivo de estado qual Briefing teve lacuna identificada, qual disciplina, data.

Precedente: Exame 2 Caso 2 (31/08/2026) — Hidrossanitário pediu se há reuso, Briefing não responde. Despachei 4 Agentes, retive Saturnino até Lúcio esclarecer.

### 3.3 Ação se Erro de Coordenação

1. **Bloco compilação inteira** — nada de sair ao cliente enquanto houver colisão aberta.
2. **Devolvo às duplas responsáveis** (não resolvo aqui — trade-off de projeto é deles):
   - Qual disciplina cede, qual recua, qual passa por dentro?
   - Quem coordena a mudança?
3. **Escalo a Wallenberg** se o trade-off exigir decisão comercial ou impacto de custo:
   - Se é passível de resolve "sem verdade", é escalão dos Agentes.
   - Se é "custa mais" ou "muda prazo" ou "cliente precisa aprovar", vai a Wallenberg.
4. Registro no meu arquivo de estado qual projeto/etapa, qual foi a colisão, quem se responsabilizou pela solução, data de bloqueio e quando foi resolvido.

Precedente: Exame 2 Caso 3 (31/08/2026) — Pilar P12 × prumada × vidro. Bloqueado compilação, devolvi a Oscar + Lúcio com trade-off, escalei a Wallenberg (decisa de qual cede exigia conhecimento de arquitetura + custos de obra).

## 4. Fluxo (resumido)

```
Bloqueador identificado (Agente / Oscar / Wallenberg)
        ↓
Diagnóstico: Briefing ou Coordenação?
        ↓
Se BRIEFING → Bloco Agente afetado, escalo lacuna a Wallenberg (resto segue)
Se COORDENAÇÃO → Bloco compilação, devolvo trade-off às duplas (escalas a Wallenberg se custo/prazo)
        ↓
Registro em _estado_cardozo.md
```

## 5. O que NÃO faço

- **Não resolvo trade-off arquitetônico sozinho.** Coordenação é atribuição de Oscar/Lúcio, não minha.
- **Não deixo passar incompatibilidade "para resolver depois".** Bloqueador é bloqueador — não vai ao cliente enquanto aberto.
- **Não preenchem lacuna de Briefing por suposição.** Se falta info, escala — não invento.
- **Não comunico direto com Agente externo.** Tudo por Wallenberg (que conversa com Lúcio/Oscar).

## 6. Comunicação com Wallenberg (modelo)

**Se é Briefing incompleto:**
> Wallenberg — Bloqueador em <projeto/etapa>. Saturnino identificou: o Briefing não especifica se há reuso de água. Sem essa info não despacho ele. Peço a Lúcio esclarecer com cliente. Baumgart, Landell, Glaziou e Tenreiro seguem normalmente.

**Se é incompatibilidade de coordenação:**
> Wallenberg — Bloqueador em <projeto/etapa>. Oscar reportou: pilar P12 bate com prumada de Saturnino e quadro de vidro de Tenreiro. Erro de coordenação, não de Briefing. Parei compilação. Precisa de trade-off entre estrutura/hidro/interior — quem cede, quem recua, quem passa por dentro? Escalado a Lúcio/Oscar. Aguardo veredito.

Sempre objetivo, nunca "há um problema".

## 7. Fora de escopo deste POP

- Compatibilização automática / clash detection — lacuna estrutural registrada.
- Mérito técnico dentro de uma disciplina (isso é auditoria do Agente por mim, depois).
- Documento de cliente real, Gates, protocolo.

---

**Nota:** Este POP não é substituição de POP-COMPL-01 (validação de Briefing no recebimento). Aquele é **entrada**; este é **execução**. Ambos são obrigatórios, complementares.
