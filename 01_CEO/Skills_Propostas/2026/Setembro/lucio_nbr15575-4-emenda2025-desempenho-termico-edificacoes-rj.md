---
name: nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj
description: "NBR 15575-4:2021 + Emenda 2025 — desempenho térmico de edificações residenciais no Rio de Janeiro (RJ — zona bioclimática a confirmar; indício ZB 4A, não confirmado em fonte primária, ver Skill nbr15220-3-bioclimatica-rj)"
version: "1.2"
fonte_primaria_lida: "não — todas as fontes abaixo são secundárias (blogs/sites técnicos); nem a NBR 15575-4 nem a Emenda 2025 nem a NBR 15220-3 foram lidas"
changelog: "1.2 (28/09/2026, Lúcio, autorizado por Claudemberg) — título, Escopo e §§2-5 alinhados: toda ZB 4A usada como premissa marcada como indício não confirmado (aviso por seção, remete ao §1). 1.1 (28/09/2026, Lúcio, aprovado por Claudemberg) — correções do treino em caso fictício: ZB 4A rebaixada a indício não confirmado (alinhada com nbr15220-3-bioclimatica-rj); absortância de cobertura movida para a tabela de Coberturas; fontes declaradas secundárias no cabeçalho. 1.0 = versão de 22/09/2026 sem campo de versão."
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

# NBR 15575-4:2021 + Emenda 2025 — Desempenho Térmico de Edificações Residenciais (RJ — zona bioclimática a confirmar; indício ZB 4A)

**Escopo:** requisitos de desempenho térmico de sistemas de vedações verticais (paredes) e coberturas de edificações residenciais no Rio de Janeiro, com foco nas mudanças trazidas pela saída do RJ da ZB 8 (nova zona a confirmar; indício ZB 4A, ver §1) e pela Emenda de 2025.

**Norma principal:** ABNT NBR 15575-4:2021 (Sistemas de vedações verticais externas e internas) + Emenda publicada ao final de 2025

---

## 1. Mudança de Zoneamento: RJ saiu da ZB 8 (nova zona: provável ZB 4A — indício não confirmado)

A NBR 15220-3:2024 substituiu o mapa bioclimático de 8 zonas por 12 zonas (1R, 1M, 2R, 2M, 3A, 3B, 4A, 4B, 5A, 5B, 6A, 6B). O Rio de Janeiro **mudou de categoria**: não usar mais "ZB 8" como referência. O código da nova zona, **"ZB 4A", é indício não confirmado em fonte primária** — mesma posição da Skill irmã `nbr15220-3-bioclimatica-rj`, que é a dona desse ponto. Antes de usar "ZB 4A" em memorial, simulação ou peça de cliente, confirmar na ferramenta oficial "Busca ZB" (normadedesempenho.com.br/busca-zb) ou no relatório técnico ABNT TR 15220-3-1. Toda menção a "ZB 4A" nesta Skill deve ser lida com essa ressalva.

**Impacto prático:**
- Parâmetros de U (transmitância térmica) e CT (capacidade térmica) associados à ZB 8 **não se aplicam mais** ao RJ
- Soluções construtivas que atendiam ZB 8 podem **não atender** a nova zona — projeto existente precisa ser reverificado
- A reclassificação das zonas é a razão da publicação das Emendas de 2025

---

## 2. O Que Mudou com a Emenda de 2025 (Partes 1, 4 e 5)

> Aviso: "ZB 4A" nesta seção = indício não confirmado (ressalva do §1).

Conforme fontes secundárias consultadas (seedsolution.com.br, sienge.com.br):

| Aspecto | Antes (2021) | Depois (Emenda 2025) |
|---------|-------------|---------------------|
| Zoneamento de referência | ZB 1 a ZB 8 | ZB 1R a ZB 6B (12 zonas) |
| Método de verificação | Simplificado **ou** simulação | Simulação anual obrigatória para obras novas |
| Escopo da simulação | Envoltória | Envoltória + cargas internas (ocupação, iluminação, equipamentos) |
| Parâmetros RJ | Tabela ZB 8 | Tabela ZB 4A — ver Emenda ABNT |
| CT para paredes externas (ZB 4A) | — | ≥ 130 kJ/(m²·K) (referência — confirmar na emenda) |

---

## 3. Parâmetros de Referência para ZB 4A (indício não confirmado — confirmar a zona no §1 e os valores via Emenda ABNT)

> Aviso: todas as tabelas desta seção partem da premissa ZB 4A, que é indício não confirmado (ressalva do §1). Se a zona oficial do lote for outra, os valores não se aplicam.

⚠️ **Atenção (R1):** os valores abaixo são referências de fontes secundárias — **a tabela oficial está na Emenda ABNT de 2025.** Oscar deve consultar a norma antes de citar em memorial de projeto.

### Vedações Verticais Externas (Paredes) — ZB 4A

| Parâmetro | Referência | Nível |
|-----------|-----------|-------|
| CT ≥ 130 kJ/(m²·K) | NBR 15220-3:2024 (skill 01/09/2026) | Mínimo |
| U ≤ x W/(m²·K) | **Confirmar na Emenda ABNT 2025** | M/I/S |

### Coberturas — ZB 4A

| Parâmetro | Referência | Nível |
|-----------|-----------|-------|
| U cobertura ≤ x W/(m²·K) | **Confirmar na Emenda ABNT 2025** | M/I/S |
| Absortância da cobertura ≤ 0,6 | Referência geral Norma Desempenho (fonte secundária — a confirmar) | Mínimo |
| Absortância ≤ 0,4–0,6 | Referência geral (fonte secundária — a confirmar) | M/I/S |

---

## 4. Método de Verificação Obrigatório (Obras Novas — Emenda 2025)

> Aviso: calibrar a simulação para a zona **confirmada** do lote; "ZB 4A" abaixo = indício não confirmado (ressalva do §1).

A Emenda 2025 tornou a **simulação computacional anual** obrigatória para obras novas, substituindo o método simplificado como padrão:

1. **Modelo de simulação:** envoltória + cargas internas (ocupação por ambiente, iluminação artificial, equipamentos)
2. **Software:** qualquer ferramenta calibrada para ZB 4A — EnergyPlus, Design Builder, Domus, SketchUp + OpenStudio
3. **Critério de aceite:** níveis M (mínimo), I (intermediário) ou S (superior) — comparar com tabela da Emenda para ZB 4A
4. **Relatório:** output de simulação é documento de projeto, não só planilha interna

**Método simplificado:** ainda aceito para reformas e para verificação prévia, mas **não substitui a simulação** em licenciamento de obra nova no RJ (verificar se Decreto 55.622/2025/LICIN 2.0 já exige isso como condicionante — R4)

---

## 5. Implicações para o Partido Arquitetônico (Oscar)

> Aviso: "ZB 4A" nesta seção = indício não confirmado (ressalva do §1); as diretrizes valem para o clima quente-úmido do RJ, mas não citar a zona como fato em memorial ou peça de cliente.

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
