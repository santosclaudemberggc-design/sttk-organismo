---
name: coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj
description: "Parâmetros de ventilação natural, iluminação natural e pé-direito mínimo para edificações residenciais no RJ — COE (LC 198/2019), prismas, dutos e vãos."
version: "1.0"
status: ativa-com-ressalva
created: 2026-09-21
author: Rotina Diária Skills v3.2
gestor_validador: lucio
agente_principal: oscar
cross_disciplina:
  - tenreiro
  - baumgart
  - landell
fonte_primaria_lida: "sim — LC 198/2019 Art. 5º, 12º, 14º, 17º e 18º lidos via câmara.rj.gov.br"
metadata:
  tipo: Inteligência (Trilha A)
  norma_base: "LC 198/2019 — COE do Rio de Janeiro (Código de Obras e Edificações)"
  zona_geografica: "Rio de Janeiro (aplicável em toda cidade, incluindo Barra da Tijuca e Recreio)"
  tags:
    - ventilacao-natural
    - iluminacao-natural
    - pe-direito
    - prisma-ventilacao
    - coe-rj
    - oscar-revit
---

# COE RJ — Ventilação Natural, Iluminação e Pé-Direito em Edificações Residenciais
## LC 198/2019 — Parâmetros para Projeto

---

## POR QUE ESTA SKILL

Toda aprovação LICIN 2.0 no Rio de Janeiro precisa atender ao COE (LC 198/2019). Os erros mais frequentes em projeto residencial envolvem poços/prismas de ventilação subdimensionados, vãos de iluminação abaixo do mínimo e pé-direito fora do exigido — três fontes comuns de exigência da prefeitura na análise. Esta Skill reúne os parâmetros verificados direto no texto da lei.

---

## 1. PÉ-DIREITO MÍNIMO (Art. 12º e 14º)

### Residencial (Art. 12º)

| Tipo de Compartimento | Pé-Direito Mínimo |
|---|---|
| Permanência prolongada (salas, quartos, escritórios) | **2,50 m** |
| Permanência transitória (banheiros, circulações, depósitos) | **2,20 m** |

### Não residencial (Art. 14º — referência cruzada para uso misto)

| Uso | Pé-Direito Mínimo |
|---|---|
| Salas e quartos hoteleiros | **2,60 m** |
| Lojas | **3,00 m** |
| Banheiros e circulações | **2,20 m** |

**Atenção:** pé-direito medido da laje ao piso acabado (não estrutura bruta). Em projetos BIM (Revit/Vitruvius): parametrizar com folga mínima de 5 cm para embutidos de forro.

---

## 2. PRISMAS DE VENTILAÇÃO E ILUMINAÇÃO — PVI e PV (Art. 5º)

### PVI — Prisma de Ventilação e Iluminação (serve luz + ar para compartimento de permanência prolongada)

**Regra dimensional:**
- Seção horizontal **constante** ao longo de toda a altura
- Ângulos internos ≥ 90° (seção retangular ou poligonal convexa, nunca aguda)
- **Nenhum dos lados ≤ H/4** (onde H = altura do prisma = número de pavimentos × pé-direito)
- **Mínimo absoluto de qualquer lado: 3,00 m**

**Exemplo prático:**
- Edifício de 4 pavimentos (H ≈ 10 m) → cada lado ≥ H/4 = 2,5 m → prevalece o mínimo absoluto: **lado ≥ 3,0 m**
- Edifício de 20 pavimentos (H ≈ 50 m) → cada lado ≥ 50/4 = 12,5 m

**Erro comum:** projetar prisma com lado < 3 m em edifícios baixos, achando que a relação H/4 não seria acionada. O mínimo de 3 m é incondicional.

### PV — Prisma de Ventilação apenas (serve ar para compartimento de permanência transitória: banheiro, lavabo, DML)

**Regra dimensional:**
- **Nenhum dos lados ≤ H/20**
- **Mínimo absoluto de qualquer lado: 1,00 m**

**Exemplo prático:**
- Edifício de 4 pavimentos (H ≈ 10 m) → lado ≥ H/20 = 0,5 m → prevalece o mínimo: **lado ≥ 1,0 m**
- Edifício de 25 pavimentos (H ≈ 62 m) → lado ≥ 62/20 = 3,1 m

---

## 3. DUTOS DE VENTILAÇÃO NATURAL (Art. 17º, § 1º)

- Dutos de ventilação natural **podem passar sobre outros compartimentos**
- **Comprimento horizontal máximo: 6 m** (além disso, exige ventilação mecânica)
- Uso típico: ventilação de banheiros internos em apartamentos compactos

**Implicação de projeto:** banheiro distante mais de 6 m da fachada ou de um PV não pode usar duto natural — requer exaustão mecânica. Planejamento de plant deve prever isso antes do lançamento estrutural.

---

## 4. VÃOS MÍNIMOS PARA ILUMINAÇÃO NATURAL (Art. 18º)

| Tipo de Compartimento | Proporção Mínima de Vão (área do vão / área do compartimento) |
|---|---|
| Salas de estar, quartos, dormitórios | **1/8 (12,5%)** |
| Cozinha, copa, refeitório | **1/10 (10%)** |
| Conjunto sala-cozinha integrada | **1/8 da área total integrada** |
| Banheiros com ventilação natural | **1/10** |
| Banheiros com ventilação por duto | **1/8** |

**Exemplo:** quarto de 12 m² → vão mínimo = 12/8 = **1,5 m²** de janela.

**Barra da Tijuca — aplicação:** apartamentos com planta aberta e cozinha integrada à sala seguem a regra de 1/8 da área total combinada. Relevante para os layouts típicos de condomínios horizontais da região.

---

## 5. VENTILAÇÃO NATURAL — MODOS ACEITOS PELO COE

O COE aceita as seguintes formas de ventilação natural:

1. **Vãos abertos diretos** para o exterior (fachada, cobertura)
2. **Via varandas ou terraços cobertos** que abrem para o exterior, afastamentos ou prismas
3. **Dutos** (comprimento horizontal ≤ 6 m — ver § 3 acima)
4. **Ventilação mecânica** — permitida como alternativa apenas para compartimentos de permanência transitória e alguns usos não residenciais

**Não é permitido:** ventilação de compartimento de permanência prolongada (quarto, sala) exclusivamente por duto ou por compartimento intermediário sem vão para o exterior.

---

## 6. BARRA DA TIJUCA E RECREIO — CONTEXTO

- Tipologia dominante: condomínios horizontais (casas e sobrados) e edifícios multifamiliares até 2 pavimentos em Subzona A (Decreto 3046/81)
- Lotes maiores: menor pressão sobre prismas, mas a regra H/4 ainda se aplica quando houver edifício com mais de 1 pavimento e fechamento lateral
- Bairros com restrições de gabarito (Decreto 3046/81): reduz H → reduz exigência de prisma, mas o mínimo de 3 m (PVI) e 1 m (PV) é sempre o piso

---

## RESSALVAS

**R1 — Versão do COE:** LC 198/2019 pode ter sido emendada após janeiro de 2019. Verificar se houve atualização antes de qualquer consulta de aprovação.

**R2 — Prevalência entre leis:** o Decreto 3046/81 (Barra/Recreio) e a LC 270/2024 podem estabelecer parâmetros adicionais ou exigências especiais para a ZE-5. COE é o mínimo; a legislação urbanística de zona pode ser mais restritiva.

**R3 — Uso misto:** projetos com uso misto (residencial + comercial) podem precisar atender ao maior pé-direito (ex.: 3,00 m de loja no térreo).

**R4 — Hely valida LICIN:** na hora da montagem do processo LICIN 2.0, Hely verifica se a análise municipal exige cálculo e inserção do PVI no memorial descritivo ou apenas na planta.

**R5 — Denominador H/4 do PVI não verificado por memória para edifícios altos (Lúcio, 21/09):** o COE anterior (Decreto-Lei 322/76) usava denominadores menores (H/5 ou H/6). Se LC 198/2019 realmente usa H/4, isso é endurecimento material. Para o contexto da Barra/Recreio (gabarito 2 pavimentos, H ≈ 5m), o mínimo absoluto de 3m prevalece sempre — risco operacional baixo. Para projetos multi-pavimento fora de zona de gabarito restrito, Hely deve confirmar o denominador exato no Art. 5º da LC 198/2019 antes do primeiro uso de Oscar.

**R6 — Tabela de banheiros carece de nota explicativa (Lúcio, 21/09):** a tabela mostra "banheiro com duto → 1/8" maior que "banheiro com ventilação natural → 1/10", o que é contraintuitivo. A lógica: quando o duto serve o ar, a janela atende APENAS à iluminação (exigência maior: 1/8); quando a mesma abertura serve luz E ar, a proporção pode ser menor (1/10). Oscar DEVE ter ciência desse detalhe antes de parametrizar janelas de banheiro no Revit.

**R7 — Altura H dos prismas deve incluir espessura de lajes (Lúcio, 21/09):** os exemplos usam "H = n_pavimentos × pé-direito". H real inclui a espessura das lajes (≈ 20–25 cm por andar). Para 4 pavimentos, H real ≈ 10,8–11,0 m vs. 10 m estimado. O erro se torna material em edifícios de 10+ pavimentos. Oscar deve parametrizar o Revit com a altura total real do prisma (piso do 1º compartimento servido ao topo do último), não com estimativa simplificada.

---

## FONTES VERIFICADAS

- **LC 198/2019 (COE RJ)** — Arts. 5º, 12º, 14º, 17º, 18º — lidos em [camara.rj.gov.br](https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/c1982019.html) ✓ (fonte primária)
- **Instituto Bramante** — notas sobre pé-direito e ventilação no COE (complementar, confirmado pela fonte primária)
