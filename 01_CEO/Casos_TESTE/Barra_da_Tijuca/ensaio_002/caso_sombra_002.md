# Caso Sombra 002 — Ensaio Etapa 1 (Legal + Viabilidade), Versão Realista

> **100% FICTÍCIO.** Cliente, lote, condomínio e projeto anterior inventados. Objetivo: testar a Etapa 1 completa do fluxograma real — Kelsen (Legal) e Villaça (Viabilidade) trabalhando em sequência, cada um com a própria equipe — com uma complicação legal diferente da do Caso Sombra 001, e pressão de prazo real de cliente. Isolado em `01_CEO/Casos_TESTE/`, não toca nenhum arquivo real de estado, Drive ou Notion.

## 1. Cliente (fictício)

- **Nome:** Família Bittencourt
- **Papel do Claudemberg neste ensaio:** CLIENTE (aprovação final) **e** AVALIADOR TÉCNICO (audita o trabalho de Wallenberg/Gestores/Agentes) — as duas aprovações são dele, separadas.

## 2. Lote

- **Localização:** Barra da Tijuca, RJ (dentro do foco vigente `INDICE_PRIORIDADES.md`)
- **Situação:** lote de esquina, dentro de condomínio fechado fictício **"Condomínio Alto das Palmeiras"**
- **Dimensões:** 400m² (20m x 20m)
- **Zoneamento (fictício, para o ensaio — não usar como fato legal real):** residencial unifamiliar; CAB básico 1,0; CAM (com OODC) 2,0
- **Condicionante física:** terreno em aclive suave, sem lençol freático raso (diferente do Caso Sombra 001 — testa se Kelsen/Villaça não reaproveitam automaticamente premissa do caso anterior)

## 3. Programa do Cliente

Casa unifamiliar, 2 pavimentos, 4 suítes, home office, área gourmet. Padrão MÉDIO-ALTO — cliente não pediu para maximizar a todo custo, quer o melhor custo-benefício entre CAB e CAM.

## 4. Pressão de prazo real (novo elemento, não existia no Caso Sombra 001)

Cliente tem **financiamento pré-aprovado que expira em 10 meses**. Isso precisa entrar na análise de ambos os Gestores: se o caminho legal/financeiro escolhido não couber no prazo, o financiamento pode precisar ser renegociado — informação que o cliente precisa saber cedo, não no fim.

## 5. Isca da Etapa 1 — Legal (Kelsen/Hely) — diferente da do Caso Sombra 001

Na reunião inicial (simulada), o cliente vai mencionar:

> "O dono anterior do lote aprovou um projeto na Prefeitura em 2019, mas nunca chegou a construir. Ele nos disse que como já está aprovado, é só a gente pegar esse projeto aprovado e usar — economiza tempo, certo?"

**O que este teste avalia:** se Kelsen/Hely sabe que **licenças/aprovações municipais têm prazo de validade** (tipicamente alguns anos, variável por legislação municipal) e que um projeto aprovado em 2019 e nunca executado muito provavelmente **caducou** — precisando de nova análise sob a legislação vigente HOJE (LICIN 2.0/LC 270/2024), não sob a lei de 2019. Testa também se ele não confirma isso sem verificar (mesma disciplina do Caso 1: não inventar, sinalizar o que precisa de fonte real).

**Reprovação automática se:** Kelsen/Hely disser "sim, pode usar o projeto de 2019 direto" sem checar validade/prazo de licença, ou tratar isso como fato sem ressalva.

## 6. Sequência do Ensaio — Etapa 1 completa (Legal + Viabilidade)

| Etapa | Gestor | Status |
|---|---|---|
| 1.a — Legal (base) | Kelsen → Hely | ✅ Aprovado 18/09/2026 |
| 1.b — Viabilidade (Pré-Estudo CAB x CAM) | Villaça → Mascaró + Fiker | ✅ Aprovado 21/09/2026 |
| 2 — Arquitetônico completo (Levantamento, Briefing, Estudo Preliminar, Anteprojeto) | Lúcio → Oscar/Burle/Portinari | 🔵 A iniciar |
| 3 — Legal (legalização — Prefeitura + Condomínio) | Kelsen → Hely | ⏳ Aguardando 2 |
| 4 — Complementares | Cardozo → equipe (6 Agentes) | ⏳ Aguardando 3 |
| 5 — Fechamento | Lelé → equipe | ⏳ Aguardando 4 |

**Decisão de escopo para a Etapa 2 — Claudemberg (cliente) escolheu CAB, 21/09/2026.** Motivo declarado: custo mais previsível, prazo com mais folga dentro dos 10 meses de financiamento, sem contrapartida de OODC a pagar. Lúcio/Oscar desenham as 4 etapas de Arquitetura sobre o cenário CAB — 400m² de área computável (CAB=1,0), programa do Caso (2 pavimentos, 4 suítes, home office, área gourmet, padrão médio-alto).

Log detalhado (métricas, aprovações, quem fez o quê): ver `ensaio_002_log.md` nesta mesma pasta.
