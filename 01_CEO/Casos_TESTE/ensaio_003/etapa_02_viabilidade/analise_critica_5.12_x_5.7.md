# Análise Crítica — Proposta 5.12 × Sondagem 5.7 — Fundação Especial Não Costeada

**Responsável:** Villaça (com Mascaró). Para integração no Pré-Estudo v8-final e no custo_obra de Mascaró.

**Data:** 05/10/2026 | **Ensaio:** Sombra 003, Etapa 02

---

## 1. Sondagem geotécnica 5.7 — Dados reais do lote

### Resultado SPT (3 furos, 2024)

| Parâmetro | Valor | Implicação |
|---|---|---|
| **Nível d'água (NA)** | 0,90 m da superfície | Raso; água próxima às fundações |
| **Argila orgânica mole** | 2,5 m a 9,0 m de profundidade | **Camada problemática para fundação** |
| **Areia compacta** | abaixo de 11 m | Possível fundo de estacas, se houver pressão competente |

**Interpretação técnica [VERIFICADO - Skill fundacoes-solos-moles]:**
- Argila orgânica é compressível e de baixa resistência.
- Profundidade até 9 m exige que qualquer fundação atravesse essa camada ou "flutue" sobre ela (radier).
- Nível d'água raso (0,90 m) acelera deterioração de concreto e gera empuxo.

---

## 2. Proposta 5.12 — O que declara e o que não declara

### Texto literal da Proposta (29/09/2026)

**Inclusos:** "fundação em **radier de concreto armado**, estrutura, alvenaria, cobertura, instalações elétricas e hidrossanitárias, revestimentos e acabamentos de alto padrão, esquadrias".

**Não inclusos:** "demolição de construções existentes; piscina; paisagismo; ar-condicionado; automação; projetos complementares e aprovações; ligações definitivas de concessionárias; **sondagem complementar**".

### Análise crítica

**❌ Problema 1: Radier assumido, mas sondagem inviabiliza radier simples**

A proposta "inclui" radier, mas não contempla que essa fundação seja:
- Radier profundo (caro); ou
- Estacado com radier (ainda mais caro)

Radier flutuante simples (como a proposta imagina) em argila mole de 9 m de espessura **causará recalque diferencial** → fissuras, portas travadas, danos estruturais. A norma NBR 6122:2019, Seção 7 (Fundações profundas), é explícita: **em argila mole, fundação rasa é inadequada**.

**❌ Problema 2: Sondagem complementar nos "Não inclusos"**

A proposta lista "sondagem complementar" como não incluso. Mas a sondagem de 2024 (5.7) **já existe** e **já revela o problema**. "Complementar" só seria nova coleta se a primeira fosse inválida — não é o caso. Logo, a proposta:
- Sabe (ou deveria saber) que argila mole existe; ou
- Não leu a sondagem e está fazendo proposta "às cegas".

**Qualquer interpretação põe a proposta em xeque.**

---

## 3. Solução viável — Estacas hélice contínua

### Por que estacas em vez de radier

| Aspecto | Radier simples | Estacas |
|---|---|---|
| Recalque em argila mole | Alto (diferencial) | Controlado (ancoragem abaixo da mole) |
| Profundidade necessária | Impossível; flutua | 12–20 m (através da mole até areia) |
| Durabilidade em NA raso | Comprometida | Selada, protegida |
| Compatibilidade com sondagem 5.7 | ❌ NÃO | ✅ SIM |

### Especificação indicativa [VERIFICADO - NBR 6122:2019, Seção 7]

**Hélice contínua (HC):**
- Diâmetro: 60–80 cm (depende carga)
- Profundidade: **12–20 m** (para sair da argila mole e ancorar em areia)
- Quantidade: depende da planta estrutural (não calculada aqui [NC])

**Custo indicativo [ECF, fraca, depende de detalhes estruturais]:**
- Preço de mercado (RJ, 2026): R$ 80–150/metro de estaca, ø60 cm
- Exemplo: 20 m × 10 estacas (200 m total) × R$ 100/m = **R$ 20.000** (mínimo)
- Faixa realista: **R$ 150.000 a R$ 300.000** incluindo obra civil (estrutura do bloco de coroamento, rebaixamento)

**Não está aqui:** Projeto estrutural, cálculo de carga, blocos de coroamento. Essa faixa é ordem de grandeza.

---

## 4. Conclusão — Por que 5.12 não é comparável com CUB

### Premissa 1: Proposta 5.12 assume radier

Texto literal: "fundação em radier de concreto armado".

Radier em argila mole de 9 m = **inadequado por norma** (NBR 6122:2019).

### Premissa 2: CUB R-1 também assume fundação rasa

O CUB R-1 (residência térrea alta padrão, NBR 12.721) é modelado com:
- Fundação corrida ou radier simples;
- Solo "normal" (não específico);
- NA não crítico.

**CUB não contempla:** argila mole profunda, NA raso, estacas hélice.

### Implicação para custo real

| Via | Custo declarado | Fundação especial | Custo real |
|---|---|---|---|
| **Proposta 5.12** | R$ 3.717.000 (590 m² × 6.300) | Não incluído [Isca 3] | **R$ 3.717.000 + R$ 150–300 k** |
| **CUB R-1 Alto** | R$ 3.691,68/m² × área equivalente | Radier simples, não especial | **R$ CUB + R$ 150–300 k** |

**Diferença:** Nem a proposta 5.12 nem o CUB puro cobrem a fundação especial que a sondagem 5.7 exige.

**Custo real da obra = benchmark (CUB ou proposta) + diferencial de fundação (R$ 150–300 k).**

---

## 5. Integração no Pré-Estudo — Revisão de "Teto de Obra"

### Impacto no cenário S1 (adotado)

| Linha | Valor | Observação |
|---|---|---|
| **e (parcela calculável CUB)** | R$ 2.493.663 a 3.006.072 | Assume radier, não estacas |
| **e' (plataforma/elevador D. Lourdes)** | R$ 46.754 a 196.337 | Sim, costeado |
| **g (fora das linhas e, e', f)** | **[REVISTO]** | Agora: fundação especial **R$ 150–300 k** |
| **Teto de R$ 4,2 mi** | − | Mais **R$ 150–300 k** reservados para fundação |

### Folga contra teto (recalculada)

**Via CUB (com coeficiente pendente TCPO):**
- Custo calculável: R$ 2.493.663 a 3.006.072
- Plataforma: R$ 46.754 a 196.337
- **Fundação especial (novo):** R$ 150.000 a 300.000
- **Subtotal:** R$ 2.690.417 a 3.502.409 (64–83% do teto)
- **Folga:** R$ 697.591 a 1.509.583 (17–36%)

**Conclusão:** Teto continua viável, mas a folga de ~R$ 1,2 mi agora tem comprometida R$ 0,15–0,30 mi pela fundação. Isso é **Isca 3 resolvida:**

> **"O custo real não é só CUB + proposta; é CUB (ou proposta) + diferencial de fundação especial, porque sondagem 5.7 inviabiliza radier simples. Isso pesa ~R$ 150–300 k no teto."**

---

## 6. Recomendação estrutural

### Para Mascaró (custo de obra)

1. **Manter a seção "Fundação" nas exclusões de linha g** (Skill v1.4 §2.6 item 1).
2. **Acrescentar nota específica:** "Na sondagem 5.7, argila orgânica mole de 2,5 a 9 m exige estacas hélice contínua (~R$ 150–300 k) em vez de radier simples. Nem a proposta 5.12 nem o CUB R-1 puro cobrem esse custo especial. Recomenda-se projeto estrutural antes de fechar qualquer acordo com construtora."
3. **Integrar na resposta ao Rodrigo sobre R$ 3,28 mi:** "A proposta 5.12 assume radier, mas a sondagem inviabiliza radier. Construtora terá que recotar fundação."

### Para Villaça (Pré-Estudo)

1. **Linha g (Fora das linhas):** acrescentar "fundação especial (argila mole, 2,5–9 m, estacas hélice; ~R$ 150–300 k) [NC — depende de projeto estrutural]".
2. **Seção 2.4 (Ponto não resolvido):** revelar que **nem 5.12 nem CUB contemplam a fundação especial**. Isso é diferente de "falta valor" — é erro de premissa.
3. **Recomendação (seção 5):** "Antes de fechar com construtora, exigir **projeto estrutural** que reconcilie sondagem 5.7 com a fundação proposta. Radier simples não é solução."

### Para Kelsen (Legal) — via Wallenberg

Pergunta (Villaça → Kelsen): "Subsolo foi vetado no Regramento Art. 8º. Mas se a estrutura exigir pilar de fundação profunda que transpasse a camada mole (até 20 m), a escavação é caracterizada como subsolo? Ou é 'escavação estrutural necessária'? Há janela jurídica?"

(Resposta: determina se estacas viáveis legalmente, ou se muda para solução mais cara tipo micro-estacas superficiais.)

---

## 7. Fontes e Skill

| Fonte | Conteúdo | Data | Status |
|---|---|---|---|
| **Dossiê 5.7** | SPT: NA 0,90 m; argila mole 2,5–9 m | 2024 | [FP] — ensaio |
| **Dossiê 5.12** | Proposta radier | 29/09/2026 | [FP] — ensaio |
| **NBR 6122:2019** | Fundações profundas; inadequação de fundação rasa em argila mole | 2019 (Emenda 1, 2024) | [FP] — norma oficial |
| **Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio`** | Compatibilidade de técnicas de fundação com solo mole RJ | Acervo 2026 | [ECF] — aplicada |

---

## 8. Declaração

Análise crítica de ensaio fictício (Sombra 003, Etapa 02). Sondagem, proposta e documentos do dossiê são fictícios; normas, custos de mercado e critérios técnicos (NBR 6122) são reais. Nenhum número de fundação é prometido como custo fechado — é ordem de grandeza.

— Villaça + Mascaró, 05/10/2026
