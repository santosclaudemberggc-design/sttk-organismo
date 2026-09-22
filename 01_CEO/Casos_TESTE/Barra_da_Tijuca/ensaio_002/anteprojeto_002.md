# Anteprojeto — Caso Sombra 002 (ENSAIO/TESTE)

**Cliente fictício:** Família Bittencourt
**Lote:** esquina, 20m x 20m = 400m², Barra da Tijuca — "Condomínio Alto das Palmeiras" (fictício)
**Executor:** Oscar (Agente, equipe Lúcio/Arquitetura)
**Data:** 21/09/2026
**Status do caso:** ENSAIO/TESTE — ANÁLISE PRELIMINAR, não entregável final. Sem Gate do Maurício.

---

## 0. Status real da capacidade Vitruvius/Revit nesta sessão — TESTADO, NÃO SIMULADO

Antes de produzir qualquer conteúdo desta etapa, testei a ferramenta obrigatória de verificação:

```
mcp__vitruvius__revit_status
```

**Resultado:** `Error: No such tool available: mcp__vitruvius__revit_status`

A ferramenta não existe/não está carregada nesta sessão — não é timeout, não é resposta vazia, é erro explícito de ferramenta inexistente. Isso vale por extensão para todo o toolkit Vitruvius listado no meu frontmatter (`create_wall`, `create_room`, `create_door`, `create_window`, `dimension_wall`, `create_schedule`, `create_sheet` etc.) — nenhum foi testado individualmente porque o teste de status, que é o pré-requisito, já falhou de forma definitiva.

**Decisão consequente, conforme instrução explícita recebida:** NÃO vou simular desenho no Revit. Não há paredes, ambientes, pisos, aberturas, cotagem oficial, elevações, cortes, folhas ou quadro de áreas oficial produzidos em modelo BIM nesta sessão. Tudo que seria produzido por desenho real permanece como **capacidade não testada em caso real nem de teste** — mesma pendência já registrada no meu arquivo de estado desde 07/08/2026, ainda não encerrada.

O Anteprojeto abaixo é entregue em **formato de documento técnico** (memorial + quadro de áreas + descrição de partido), consolidando e aprofundando o que já está no Estudo Preliminar — não como substituto do desenho BIM real, que continua pendente.

---

## 1. Memorial de Partido (consolidação do Estudo Preliminar)

- **(a)/(b)/(c)/(d)** — mesma disciplina de marcação das etapas anteriores; nenhuma marcação nova é introduzida aqui além das já usadas no `estudo_preliminar_002.md`.
- Implantação: casa de 2 pavimentos em lote de esquina 20x20m, aclive suave, acesso de veículo pela testada de menor fluxo hipotético (Seção 3 do EP), acesso social pela testada principal.
- Programa: térreo social (living/jantar/cozinha/gourmet/home office/lavabo/1 suíte) + 1º pavimento com 3 suítes.
- Envelope: ATE hipotética utilizada ≈291m² dentro do limite confirmado de 400m² (CAB=1,0) — folga de ≈109m² deliberadamente não alocada nesta iteração, sinalizada como decisão em aberto no EP.
- **(d) Repito aqui, para não se perder entre etapas:** TO, gabarito e afastamento exato usados na pegada do EP são hipóteses conservadoras, não parâmetros confirmados. O Anteprojeto **não corrige** essa pendência — ela continua aberta e precisa ser resolvida via Lúcio → Kelsen antes de qualquer avanço para Executivo num caso real.

---

## 2. Quadro de Áreas — Anteprojeto (mesmo do EP, sem alteração; não há modelo BIM para gerar quadro "oficial")

| Pavimento | Ambiente | Área (m²) |
|---|---|---|
| Térreo | Living/jantar/cozinha integrados | 70 |
| Térreo | Área gourmet | 25 |
| Térreo | Home office | 15 |
| Térreo | Lavabo + circulação | 10 |
| Térreo | 1 suíte térrea | 20 |
| Térreo | Garagem (2 vagas) | 40 |
| Térreo | Circulação/hall | 20 |
| **Subtotal Térreo** | | **200** |
| 1º pavimento | 3 suítes | 66 |
| 1º pavimento | Circulação/estar íntimo | 25 |
| 1º pavimento | Varanda/sacada (não-computável a confirmar) | 15 |
| **Subtotal 1º pav.** | | **91 computável + 15 a confirmar** |
| **Total computável** | | **≈291m² (folga de ≈109m² frente ao limite de 400m²)** |

**Nota explícita:** este quadro é o mesmo do Estudo Preliminar, elaborado manualmente (documento, não modelo). Não é "quadro de áreas oficial" no sentido do POP (que pressupõe extração de modelo BIM cotado) — é aproximação de memorial técnico, e deve ser tratado como tal por quem revisar.

---

## 3. O que está faltando para este ser um Anteprojeto real (lista explícita)

1. Modelo BIM real (paredes, pisos, aberturas) — **não produzido**, Vitruvius indisponível nesta sessão.
2. Cotagem oficial extraída de modelo — **não produzida**.
3. Elevações e cortes — **não produzidos**.
4. Folhas compiladas (NBR 6492) — **não produzidas**.
5. Quadro de áreas oficial extraído de modelo (`create_schedule`) — **não produzido**; o quadro da Seção 2 é manual.
6. TO/gabarito/afastamento reais confirmados via Kelsen — ainda pendente desde o Legal.
7. RRT/ART — não decidido; se o partido vier de arquiteto parceiro externo, a assinatura seria dele; se de dentro da estrutura Sttickler, seria de Claudemberg (CAU). Não assumo isso sozinho — sinalizo a Lúcio.
8. Gate do Maurício — não ocorreu (nem seria aplicável a um caso 100% fictício).

---

## 4. Quem fez o quê

**Oscar (eu):** testei a ferramenta `mcp__vitruvius__revit_status` antes de qualquer produção desta etapa, confirmei sua indisponibilidade real (erro de ferramenta inexistente, não timeout), e decidi não simular nenhum desenho BIM. Entreguei o Anteprojeto em formato de documento técnico, deixando explícito, item por item, o que está faltando para ele ser um Anteprojeto real — sem apresentar nada como "desenhado no Revit" que não foi.

---

**Produzido por Oscar (Agente, equipe Lúcio/Arquitetura) — 21/09/2026, ENSAIO/TESTE — ANÁLISE PRELIMINAR, não entregável final. Capacidade Vitruvius/Revit: testada, indisponível nesta sessão, pendência não resolvida.**
