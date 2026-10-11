---
name: nbr8681-2025-acao-seguranca-estruturas
description: "NBR 8681:2025 — Ação e Segurança nas Estruturas — Procedimento. Fatores de ponderação (γf), coeficientes de combinação (ψ), combinações ELU/ELS. Complemento direto da NBR 6120 (cargas) — sem a 8681, as cargas da 6120 não se traduzem em esforços de cálculo"
version: 1.0
status: "ativa-com-ressalva (validada por Cardozo 09/09/2026 — fluxo v2.9; fonte primária ABNT não lida)"
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_alvo: Baumgart (Estrutural, principal) — cross: Saturnino (ações em reservatórios/coberturas), Landell (ações de equipamentos em salas técnicas)
criado: 2026-09-09
fonte_primaria: "ABNT NBR 8681:2025 — Ação e segurança nas estruturas — Procedimento (publicada 29/09/2025, substitui NBR 8681:2003)"
fonte_secundaria:
  - "https://abece.com.br/ — ABECE confirma publicação e escopo geral da revisão 2025"
  - "Portais de engenharia estrutural — framework geral de combinações e fatores clássicos"
confianca: média-baixa (framework e fatores γf/ψ de referência da versão 2003 — a versão 2025 pode ter ajustado valores específicos; texto integral não lido)
---

> **RESSALVA DE FONTE** — Os fatores de ponderação (γf) e coeficientes de combinação (ψ) apresentados nesta Skill são baseados no framework da NBR 8681:2003 e fontes secundárias. A NBR 8681:2025 (publicada 29/09/2025) atualizou termos, conceitos e compatibilizou com outras normas vigentes — ajustes numéricos específicos não confirmados. Fonte primária (texto integral ABNT) não lida. Ao aplicar em caso real, o Agente é obrigado a sinalizar esta lacuna no seu retorno e tratar os valores como provisórios, não como fechados.

# NBR 8681:2025 — Ação e Segurança nas Estruturas — Procedimento

## O que é

Norma brasileira que fixa os **critérios gerais de segurança** e os **métodos de verificação** dos estados limites das estruturas. Publicada em 29/09/2025, substitui a NBR 8681:2003 — revisão que compatibiliza a norma com as atualizações da NBR 6118:2023 (concreto armado), NBR 6120:2019 (cargas) e normas internacionais.

**Papel na tríade + 1 do cálculo estrutural:**
- **NBR 6120** (cargas) → define **QUANTO** pesa (ações permanentes + variáveis)
- **NBR 8681** (segurança) → define **COMO COMBINAR** as ações e **QUAL MARGEM DE SEGURANÇA** aplicar (γf, ψ, combinações ELU/ELS)
- **NBR 6118** (concreto armado) → dimensiona a **superestrutura** usando os esforços combinados da 8681
- **NBR 6122** (fundações) → dimensiona o que **sustenta** tudo

Sem a 8681, Baumgart tem as cargas (6120) mas não sabe como combiná-las nem que fator de segurança aplicar — é a ponte entre "quanto pesa" e "quanto resiste".

## Escopo da revisão 2025

Segundo a ABECE (Associação Brasileira de Engenharia e Consultoria Estrutural):
- Atualização de termos e conceitos
- Renovação e compatibilização com outras normas atuais (6118, 6120, 6122, 6123)
- Manutenção do framework geral de estados limites e combinações de ações

**NÃO cobre (normas próprias):**
- Valores das ações em si → NBR 6120 (cargas de edificações), NBR 6123 (vento), NBR 7188 (pontes)
- Dimensionamento específico → NBR 6118 (concreto armado), NBR 8800 (aço), NBR 7190 (madeira)
- Ações excepcionais → NBR 15421 (sismo), NBR 15200 (incêndio)

## Classificação das ações (framework geral)

### 1. Ações permanentes (G)
Atuam durante toda a vida da estrutura, com intensidade constante ou pouco variável.
- **Diretas:** peso próprio, empuxo de terra/água, protensão
- **Indiretas:** retração, fluência, recalques de apoio

### 2. Ações variáveis (Q)
Variam significativamente ao longo da vida da estrutura.
- **Diretas:** cargas de uso (NBR 6120), vento (NBR 6123), temperatura
- **Indiretas:** ações dinâmicas, variações de temperatura

### 3. Ações excepcionais (Qexc)
Duração extremamente curta e baixa probabilidade — explosões, choques de veículos, sismos.

## Fatores de ponderação das ações (γf)

Os fatores γf majoram as ações (aumentam o efeito) ou minoram (quando favoráveis), garantindo margem de segurança.

**Valores de referência (framework clássico — confirmar contra texto 2025):**

### ELU — Combinações Normais

| Tipo de ação | Efeito desfavorável | Efeito favorável |
|-------------|---------------------|-----------------|
| Permanente (G) — peso próprio | γg = 1,4 | γg = 1,0 |
| Permanente (G) — empuxo de terra | γg = 1,2 | γg = 0,9 |
| Permanente (G) — empuxo de água | γg = 1,2 | γg = 1,0 |
| Variável (Q) — geral | γq = 1,4 | γq = 0 |
| Variável (Q) — temperatura | γq = 1,2 | γq = 0 |

### ELU — Combinações Especiais ou de Construção

| Tipo de ação | Efeito desfavorável | Efeito favorável |
|-------------|---------------------|-----------------|
| Permanente (G) | γg = 1,2 | γg = 1,0 |
| Variável (Q) | γq = 1,2 | γq = 0 |

### ELU — Combinações Excepcionais

| Tipo de ação | Efeito desfavorável | Efeito favorável |
|-------------|---------------------|-----------------|
| Permanente (G) | γg = 1,2 | γg = 1,0 |
| Variável (Q) — ação excepcional | γq = 1,0 | — |
| Variável (Q) — demais | γq = 1,0 | γq = 0 |

## Coeficientes de combinação (ψ)

Reduzem as ações variáveis quando atuam em combinação com outras, reconhecendo que a probabilidade de todas agirem simultaneamente com valores máximos é baixa.

| Ação variável | ψ0 | ψ1 | ψ2 |
|--------------|-----|-----|-----|
| Locais residenciais | 0,5 | 0,4 | 0,3 |
| Escritórios / salas comerciais (com concentração de pessoas ou equipamentos) | 0,7 | 0,6 | 0,4 |
| Locais com acesso de público (escolas, hospitais, estádios) | 0,7 | 0,6 | 0,4 |
| Garagens e estacionamentos | 0,8 | 0,7 | 0,6 |
| Bibliotecas, arquivos, almoxarifados | 0,8 | 0,7 | 0,6 |
| Vento | 0,6 | 0,3 | 0 |
| Temperatura | 0,6 | 0,5 | 0,3 |

**Significado prático:**
- **ψ0** — fator de combinação: reduz ações variáveis secundárias em combinações ELU normais
- **ψ1** — fator de frequência: valor frequente da ação, usado em combinações ELS frequentes e ELU especiais
- **ψ2** — fator quase-permanente: parcela "de longa duração" da ação variável (fissuração, deformação lenta)

## Combinações de ações — fórmulas

### ELU — Estado Limite Último

**Combinação Normal:**
Fd = Σ γgi × FGi,k + γq × [FQ1,k + Σ ψ0j × FQj,k]

Onde:
- FGi,k = valor característico da i-ésima ação permanente
- FQ1,k = valor característico da ação variável principal
- FQj,k = valor característico das demais ações variáveis
- ψ0j = fator de combinação da j-ésima ação variável

**Combinação Especial ou de Construção:**
Fd = Σ γgi × FGi,k + γq × [FQ1,k + Σ ψ0j × FQj,k]
(mesma estrutura, γ reduzidos conforme tabela acima)

**Combinação Excepcional:**
Fd = Σ γgi × FGi,k + FQexc + Σ ψ2j × FQj,k
(ação excepcional com valor nominal, demais com fator quase-permanente)

### ELS — Estado Limite de Serviço

**Combinação Rara:**
Fd,ser = Σ FGi,k + FQ1,k + Σ ψ1j × FQj,k
(ação variável principal com valor integral, demais com fator de frequência)

**Combinação Frequente:**
Fd,ser = Σ FGi,k + ψ1 × FQ1,k + Σ ψ2j × FQj,k
(todas as ações variáveis com fator de frequência ou quase-permanente)

**Combinação Quase-Permanente:**
Fd,ser = Σ FGi,k + Σ ψ2j × FQj,k
(só parcelas de longa duração)

**Uso de cada tipo ELS:**
- **Rara** → verificação de tensões máximas, fissuração pontual
- **Frequente** → verificação de abertura de fissuras em concreto armado (NBR 6118)
- **Quase-permanente** → verificação de deformações excessivas (flechas), fluência

## Como Baumgart usa esta Skill

**Entrada obrigatória (vem da Skill NBR 6120):**
- Quadro de cargas permanentes (G) por pavimento/cômodo
- Quadro de cargas variáveis (Q) por uso (residencial, garagem, cobertura, etc.)
- Tipo de combinação requerida (normal para operação corrente; especial para fase de construção; excepcional se aplicável)

**Saída (o que Baumgart produz com a 8681):**
- Esforços de cálculo (Fd) majorados para ELU — entrada da NBR 6118 (dimensionamento de seções)
- Esforços de serviço (Fd,ser) para ELS — entrada para verificação de flechas, fissuração, vibração
- Registro de qual combinação governa cada elemento estrutural

**Sequência de cálculo (integrando 6120 → 8681 → 6118/6122):**
1. [6120] Levantar cargas permanentes (G) e variáveis (Q) por cômodo/pavimento
2. [8681] Identificar a ação variável principal (Q1) — maior efeito no elemento analisado
3. [8681] Montar combinação ELU normal: Fd = 1,4×G + 1,4×[Q1 + Σ ψ0j×Qj] (ex.: residencial ψ0=0,5; escritório ψ0=0,7)
4. [8681] Montar combinações ELS (rara, frequente, quase-permanente) conforme verificação requerida
5. [6118] Dimensionar seção de concreto armado para Fd ≤ Rd (resistência de cálculo)
6. [6118] Verificar ELS: flechas ≤ L/250 (quase-permanente), fissuras ≤ 0,3 mm (frequente)
7. [6122] Alimentar fundações com o somatório de Fd por pilar

## Interação com outras normas do Baumgart

| Norma | Relação com a NBR 8681 |
|-------|----------------------|
| NBR 6120:2019 (cargas) | Fornece os valores de G e Q que a 8681 combina e pondera |
| NBR 6118:2026 Em.1 (concreto armado) | Recebe Fd e Fd,ser da 8681 para dimensionamento e verificação |
| NBR 6122:2019 Em.1 (fundações) | Recebe Fd acumulado para dimensionar fundação |
| NBR 6123 (vento) | Fornece Q_vento; 8681 define como combinar com as demais ações |
| NBR 9575:2024 (impermeabilização) | Peso do sistema impermeabilizante → G na combinação |
| COSCIP/CBMERJ Decreto 42/2018 | TRRF pode afetar seções → altera G e exigências de combinação excepcional (incêndio) |

## Cross-disciplina

- **Saturnino (Hidrossanitário):** ação de reservatório cheio vs. vazio em laje de cobertura — a 8681 exige considerar ambas situações (cheio = desfavorável p/ dimensionamento da laje; vazio = desfavorável p/ tombamento/flutuação). Fator γf para empuxo de água (1,2 desf. / 1,0 fav.) aplica-se a caixas d'água e piscinas.
- **Landell (Elétrica/Automação):** equipamentos pesados em salas técnicas (nobreak, transformador) entram como carga concentrada variável — ψ0 depende da classificação do local (almoxarifado/técnico = 0,8; escritório = 0,6).

## Erros comuns a evitar

1. **Usar fatores da versão 2003 sem verificar a 2025.** A revisão pode ter ajustado valores para compatibilização com a NBR 6118:2023 e a NBR 6120:2019. Até confirmar, tratar os valores como provisórios.
2. **Trocar ψ0, ψ1 e ψ2.** ψ0 (combinação ELU) > ψ1 (frequente ELS) > ψ2 (quase-permanente ELS). Errar a ordem inverte a segurança — subestima ELU ou superestima ELS.
3. **Esquecer de verificar ELS.** Muitos projetistas dimensionam só para ELU (colapso). A 8681 exige as 3 combinações ELS — flechas excessivas e fissuras são patologias reais em edificações, mesmo sem risco de colapso.
4. **Classificar ação variável principal errada.** A Q1 muda conforme o elemento: para uma viga de cobertura, Q1 pode ser vento; para uma laje de garagem, Q1 é carga de veículo. Cada elemento pode ter combinação governante diferente.
5. **Ignorar combinação de construção.** Estruturas pré-moldadas ou escoradas durante a obra podem ter esforços maiores na fase de construção do que em serviço — a combinação especial com γ = 1,2 existe para isso.
6. **Aplicar γf = 1,4 para tudo.** Empuxo de terra, empuxo de água e temperatura têm γf próprios (menores). Usar 1,4 é conservador demais (encarece) em alguns casos e errado em outros (a norma não permite).

## Lacunas conhecidas (a fechar antes de uso real)

1. **Texto integral da NBR 8681:2025 não lido.** Fatores γf e ψ apresentados são do framework clássico (versão 2003). A revisão 2025 pode ter ajustado valores. Aquisição do PDF oficial ABNT é responsabilidade de Wallenberg/Claudemberg.
2. **Compatibilização específica com NBR 6118:2023 e NBR 6120:2019.** A ABECE menciona "renovação e compatibilização" mas não detalha quais ajustes foram feitos. Pode haver fatores novos ou tabelas reorganizadas.
3. **Fatores de ponderação para ações de protensão.** Estruturas protendidas (menos comuns em residencial) têm γf específicos não detalhados aqui.
4. **Combinações para projeto em situação de incêndio.** A NBR 8681 referencia a NBR 15200 para combinações excepcionais de incêndio — não detalhadas nesta Skill (escopo do COSCIP/CBMERJ já cobre o framework regulatório).
