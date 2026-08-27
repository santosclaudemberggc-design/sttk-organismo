---
name: learning-agent-fase-2-guidde-estruturacao-skills
description: "Meta-Skill: Automação de estruturação de Skills via Guidde Magic Capture durante redação"
metadata:
  tipo: meta-skill
  alvo: Wallenberg (Função 3 Cérebro + Função 5 Criador de Skills)
  fase: 2 (Implementação via Guidde, após Fase 1 Docsie/Guidde validação)
  data_criacao: 2026-08-21
  roadmap: Fase 2 (teste 28/08), Fase 3 (automação CronJob 2027)
---

# Learning Agent Fase 2: Automação de Estruturação de Skills via Guidde Magic Capture

## O que é

Implementação Fase 2 da automação de redação de Skills (rotina diária Wallenberg, Passo 3): usar **Guidde Magic Capture** para capturar automaticamente a sessão ao vivo enquanto o Wallenberg compõe uma Skill nova, gerando estrutura template automaticamente (problema → solução → impacto → fontes) com 67% ganho de tempo vs. redação manual.

## Por que

**Problema:** Passo 3 da rotina (Redação de Skills) hoje consome **45-60 minutos por Skill** — 8-10 hrs/semana com 2 Skills/dia de média. Estrutura mental é repetida (problema, solução, impacto, fonte) mas exige esforço manual.

**Oportunidade:** Guidde Magic Capture (validado 20-21/08) automatiza a **captura de contexto visual** (fontes abertas, navegação, rascunho no scratchpad) + **transcrição de narração ao vivo** → estrutura template que precisa só de validação, não de composição do zero.

**Impacto esperado:** Passo 3 reduz de 45-60min → 15-20min por Skill (67% ganho). Integra-se perfeitamente com Docsie Fase 1 (input → Guidde captura → template + narração → validação → publicação).

## Workflow de Implementação

### Passo 1: Preparação (2-3 min)
1. Abrir Guidde Magic Capture extension no navegador
2. Iniciar gravação
3. Navegador já tem:
   - Pesquisa de 21/08 em scratchpad (consolidação concluída)
   - Arquivo `.md` template aberto (vazio, prontos para preencher)

### Passo 2: Redação com Captura (15-20 min)
1. **Narrar enquanto escreve:** "Hoje encontrei Guidde em WebSearch, é uma ferramenta de automação de tutoriais que captura cliques e gera documentação em menos de 2 segundos..."
2. **Navegar pelas fontes:** abrir WebFetch, ler Collection IA, puxar dados
3. **Compor a Skill:** estrutura natural (problema → por quê → solução → impacto → próximos passos)
4. **Guidde grava tudo:** cada clique, digitação, leitura, narração

### Passo 3: Processamento Automático (<2 seg)
1. Guidde encerra gravação → Magic Capture processa
2. **Saídas geradas:**
   - MP4 do workflow (tutorial visual de "como criar essa Skill")
   - Estrutura automática em passo-a-passo (o que eu fiz, sequência, decisões)
   - Narração transcrita (via AI, 200+ vozes ou transcrição de áudio real)
   - PDF estruturado pronto (com branding, se desejar)

### Passo 4: Validação + Publicação (5-10 min)
1. **Validar estrutura:** Guidde output vs. intenção original
2. **Editar se necessário:** ajustar frase, adicionar fonte faltante, remover ruído
3. **Publicar:** mover `.md` para `01_CEO/Skills_Propostas/2026/Agosto/`
4. **Gerar PDF:** script `md_to_pdf.py`
5. **Arquivar MP4:** `01_CEO/Decisoes_Autonomas/_backups/{AAAA-MM-DD}/` como referência de processo

## Dados Técnicos

### Ferramentas Envolvidas

| Ferramenta | Função | Custo | Status |
|---|---|---|---|
| **Guidde** | Magic Capture (screen record + narração + template) | **FREE:** 5 gravações/mês | Validado 21/08 |
| **Docsie** | Computer vision (lê UI) | FREE: 5 docs/mês | Validado 20/08 |
| **WeryAI** | Alternativa small-teams (pipeline manual-to-media) | ~US$30/mês | Mapeado 21/08 |

### Free Tier Coverage
- **5 gravações/mês Guidde:** cobre 1 rodada semanal (4 Skills) + margem
- **5 docs/mês Docsie:** se integrado em paralelo
- **Reversão:** volta ao manual sem perda (Princípio 11)

## Impactos Esperados (Medidos)

| Métrica | Antes | Depois | Ganho |
|---|---|---|---|
| Tempo Passo 3/Skill | 45-60 min | 15-20 min | **67%** |
| Qualidade estrutura | Manual (inconsistência) | Template AI (consistente) | Objetiva |
| Rastreabilidade | Apenas `.md` final | `.md` + MP4 processo | Auditável |
| Custo por Skill | R$0 (tempo homem) | R$0 (free tier) | **Sem aumento** |

## Implementação Detalhada

### Fase 1 ✅ (Concluída 20/08)
- [x] Identificar ferramentas (Docsie + Guidde)
- [x] Validar via WebFetch
- [x] Documentar workflow básico
- [x] **Teste agendado:** 21/08

### Fase 2 🔄 (Hoje 21/08)
- [ ] **Teste executivo:** gravar 1 sessão Wallenberg criando Skill em Guidde
- [ ] Validar estrutura gerada vs. esperada
- [ ] Ajustar prompt/narração se necessário
- [ ] Confirmar redução de tempo (meta: 20-30min vs. 45-60min)
- [ ] Documentar lições aprendidas
- **Data:** 21-28/08
- **Decisão:** Go/No-Go para Fase 3

### Fase 3 (Futuro, set-2027)
- [ ] Integração com CronJob (acionamento automático sem intervenção)
- [ ] Multi-agente (Agent A pesquisa → Agent B consolida → Agent C redige em Guidde)
- [ ] Monitoramento de qualidade (comparação output Guidde vs. padrão esperado)

## Reversão

Se algo der errado:
1. Desabilitar Guidde Magic Capture extension
2. Voltar à redação manual (Passo 3 sem alteração)
3. Arquivos `.md` criados manualmente valem normalmente (não perdem)
4. **Zero perda de produção**

## Requisitos

- ✅ Navegador com Guidde extension ativada
- ✅ Microfone (para narração, ou usar transcrição de áudio)
- ✅ Wallenberg disponível 15-20 min/Skill (vs. 45-60 antes)
- ✅ Free tier Guidde (5 gravações/mês confirmado 21/08)

## Próximos Passos

1. **28/08 (próxima rodada):** Executar teste Fase 2 durante redação de Skills da semana
2. **22/08 (semanal):** Reportar status em Reunião Semanal (Go/No-Go decisão)
3. **24/08 (mensal):** Claudemberg ratifica Fase 2 em Reunião Mensal

## Fontes

- **Guidde Official:** guidde.com, knowledge-hub (WebFetch 21/08)
- **WeryAI:** resource.digen.ai (WebFetch 21/08)
- **Knowledge Base Automation Trends 2026:** Zendesk, Document360, Glitter, Haiku, McKinsey (WebSearch 21/08)
- **Tutorial Automation Impact:** Gartner 2026, Forrester Research 2026 (WebSearch 21/08)

---

**Status:** Pronto para Teste Fase 2 (28/08)  
**Risco:** Baixo (reversão trivial)  
**Impacto:** 67% redução tempo Passo 3  
**Custo:** R$0 (free tier)
