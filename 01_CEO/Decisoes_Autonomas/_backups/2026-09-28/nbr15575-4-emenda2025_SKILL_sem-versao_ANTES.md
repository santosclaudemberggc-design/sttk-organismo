<!-- Backup 28/09/2026 (Lúcio) antes da correção pós-treino. Conteúdo idêntico em .claude/skills/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj/SKILL.md e 01_CEO/Skills_Propostas/2026/Setembro/lucio_nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj.md (conferido por leitura integral dos dois). Não tinha campo de versão (tratado como 1.0). -->
---
name: nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj
description: "NBR 15575-4:2021 + Emenda 2025 — desempenho térmico de edificações residenciais para ZB 4A (Rio de Janeiro)"
metadata:
  type: inteligencia
  status: ativa-com-ressalva
  para: Lúcio/Oscar (Arquitetura, principal) — cross: Tenreiro (interiores), Baumgart (envoltória/fachada)
  gestor: Lúcio
  criada: 22/09/2026
  rodada: Diária Skills v3.2
  fontes:
    - seedsolution.com.br/nbr-15575-desempenho-termico-novo-zoneamento-bioclimatico/ (lido 22/09/2026)
    - sienge.com.br/blog/o-que-e-nbr-15575/ (lido 22/09/2026)
    - labeee.ufsc.br/en/NBR15575-2020 (lido 22/09/2026 — parcial)
    - inteligenciaurbana.org/2021/08/norma-desempenho-nbr-15575-termico-acustico-luminico.html (lido 22/09/2026)
  ressalvas:
    - R1 CRÍTICA: valores numéricos específicos (U W/m²K por zona, CT kJ/m²K por nível M/I/S) estão nas Emendas ABNT de 2025 (pagas) — este skill não reproduz a tabela oficial; Oscar deve consultar a norma antes de citar em memorial de projeto
    - R2: a Emenda 2025 de Partes 1/4/5 ainda não foi consolidada em texto único disponível ao público — verificar versão vigente no portal ABNT antes de citar em memorial
    - R3: CT ≥ 130 kJ/(m²·K) para paredes em ZB 4A já consta na Skill NBR 15220-3:2024 (01/09/2026) — valor de referência, confirmar com emenda 2025
    - R4: método simplificado vs simulação computacional: a Emenda 2025 tornou a simulação anual obrigatória para obras novas — verificar se o Decreto 55.622/2025 (LICIN 2.0) já exige isso como condicionante de aprovação no RJ
---

# NBR 15575-4:2021 + Emenda 2025 — Desempenho Térmico de Edificações Residenciais (ZB 4A, RJ)

**Escopo:** requisitos de desempenho térmico de sistemas de vedações verticais (paredes) e coberturas de edificações residenciais no Rio de Janeiro, com foco nas mudanças trazidas pela migração para ZB 4A e pela Emenda de 2025.

**Norma principal:** ABNT NBR 15575-4:2021 (Sistemas de vedações verticais externas e internas) + Emenda publicada ao final de 2025

---

## 1. Mudança de Zoneamento: ZB 8 → ZB 4A (RJ)

A NBR 15220-3:2024 (publicada dez/2024) substituiu o mapa bioclimático de 8 zonas por 12 zonas (1R, 1M, 2R, 2M, 3A, 3B, 4A, 4B, 5A, 5B, 6A, 6B). O Rio de Janeiro **migrou de ZB 8 para ZB 4A** — essa mudança é a base para todas as alterações de parâmetros térmicos em projetos residenciais cariocas.

**Impacto prático:**
- Parâmetros de U (transmitância térmica) e CT (capacidade térmica) associados à ZB 8 **não se aplicam mais** ao RJ
- Soluções construtivas que atendiam ZB 8 podem **não atender** ZB 4A — projeto existente precisa ser reverificado
- A requalificação para ZB 4A é a razão da publicação das Emendas de 2025

---

## 2. O Que Mudou com a Emenda de 2025 (Partes 1, 4 e 5)

Conforme fontes secundárias consultadas (seedsolution.com.br, sienge.com.br):

| Aspecto | Antes (2021) | Depois (Emenda 2025) |
|---------|-------------|---------------------|
| Zoneamento de referência | ZB 1 a ZB 8 | ZB 1R a ZB 6B (12 zonas) |
| Método de verificação | Simplificado **ou** simulação | Simulação anual obrigatória para obras novas |
| Escopo da simulação | Envoltória | Envoltória + cargas internas (ocupação, iluminação, equipamentos) |
| Parâmetros RJ | Tabela ZB 8 | Tabela ZB 4A — ver Emenda ABNT |
| CT para paredes externas (ZB 4A) | — | ≥ 130 kJ/(m²·K) (referência — confirmar na emenda) |

---

## 3. Parâmetros de Referência para ZB 4A (confirmar via Emenda ABNT)

⚠️ **Atenção (R1):** os valores abaixo são referências de fontes secundárias — **a tabela oficial está na Emenda ABNT de 2025.** Oscar deve consultar a norma antes de citar em memorial de projeto.

### Vedações Verticais Externas (Paredes) — ZB 4A

| Parâmetro | Referência | Nível |
|-----------|-----------|-------|
| CT ≥ 130 kJ/(m²·K) | NBR 15220-3:2024 (skill 01/09/2026) | Mínimo |
| U ≤ x W/(m²·K) | **Confirmar na Emenda ABNT 2025** | M/I/S |
| Absortância cobertura ≤ 0,6 | Referência geral Norma Desempenho | Mínimo |

### Coberturas — ZB 4A

| Parâmetro | Referência | Nível |
|-----------|-----------|-------|
| U cobertura ≤ x W/(m²·K) | **Confirmar na Emenda ABNT 2025** | M/I/S |
| Absortância ≤ 0,4–0,6 | Referência geral | M/I/S |

---

## 4. Método de Verificação Obrigatório (Obras Novas — Emenda 2025)

A Emenda 2025 tornou a **simulação computacional anual** obrigatória para obras novas, substituindo o método simplificado como padrão:

1. **Modelo de simulação:** envoltória + cargas internas (ocupação por ambiente, iluminação artificial, equipamentos)
2. **Software:** qualquer ferramenta calibrada para ZB 4A — EnergyPlus, Design Builder, Domus, SketchUp + OpenStudio
3. **Critério de aceite:** níveis M (mínimo), I (intermediário) ou S (superior) — comparar com tabela da Emenda para ZB 4A
4. **Relatório:** output de simulação é documento de projeto, não só planilha interna

**Método simplificado:** ainda aceito para reformas e para verificação prévia, mas **não substitui a simulação** em licenciamento de obra nova no RJ (verificar se Decreto 55.622/2025/LICIN 2.0 já exige isso como condicionante — R4)

---

## 5. Implicações para o Partido Arquitetônico (Oscar)

- **Fachada poente (Oeste) é o caso crítico** em ZB 4A — insolação direta da tarde. Estratégias passivas (brises, cobogó, veneziana — ver Skill `lucio-protecao-solar-externa-dispositivos-rj`) reduzem carga térmica e facilitam atingir nível I/S na simulação
- **Ventilação cruzada** favorece desempenho térmico ZB 4A — a COE LC 198/2019 define os percentuais mínimos de abertura (ver Skill `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`)
- **Cobertura:** é o elemento de maior ganho de calor no clima tropical úmido RJ — absortância da telha/laje importa mais que a parede para cumprir o critério de cobertura
- **Light Steel Frame e estruturas leves:** CT 130 kJ/(m²·K) é difícil de atingir — exige EPS, camada de massa ou bloco cerâmico extra. Verificar com Baumgart

---

## 6. Interface com Outras Skills

- **NBR 15220-3:2024 (01/09/2026):** zoneamento bioclimático de base — confirmar ZB 4A como zona do projeto antes de qualquer simulação
- **Proteção Solar Externa (17/09/2026):** dispositivos que reduzem carga solar nas paredes e coberturas — estratégia passiva complementar
- **COE LC 198/2019 ventilação (21/09/2026):** parâmetros legais de abertura para ventilação natural — contribui para desempenho térmico
- **Partido Arquitetônico/Conforto Térmico (16/09/2026):** orientação solar, tipologias — base do partido que a NBR 15575-4 verificará depois

---

**Lacunas para resolução futura:**
- Tabela oficial U e CT por nível M/I/S para ZB 4A: obter Emenda ABNT 2025 (paga)
- Verificar se LICIN 2.0 (Decreto 55.622/2025) já exige relatório de simulação como condicionante de aprovação (R4)
- Software de simulação recomendado pelo Vitruvius/BIM: verificar integração Revit → EnergyPlus/gbXML
