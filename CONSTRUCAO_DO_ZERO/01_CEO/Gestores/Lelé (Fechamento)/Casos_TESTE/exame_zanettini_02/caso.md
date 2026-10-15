# Caso de exame — Zanettini (Compatibilização, etapa 14)

**Tipo:** Exame de Formação → Shadow, segunda tentativa. Caso FICTÍCIO.
**Código:** EXAME-ZAN-02
**Montado por:** Lelé (Gestor Fechamento), 15/10/2026, por pedido de Wallenberg com aprovação de Claudemberg.
**Gabarito:** `gabarito_lacrado.md` (arquivo separado, não entregue ao Agente). Escrito antes de qualquer aplicação.
**SHA-256 do gabarito:** d945177a2c1650618365d049d29d034dcf928049bc4c0c4fbb73121c17404714 (calculado por Wallenberg em 15/10/2026 com sha256sum). Conferir antes da aplicação: se mudar, o gabarito foi alterado.
**Status:** Montado. NÃO aplicado. Aguarda aprovação de Wallenberg.

---

## 1. Enunciado

Você recebe o pacote de compatibilização da **Casa Aroeira** (projeto fictício, Lote 07, Quadra F, 300,00 m² de terreno, 2 pavimentos: térreo com escritório, cozinha, lavanderia e banheiro de serviço; superior com duas suítes).

Entregue:
1. Matriz de conflitos: `conflito | onde (documento + página/prancha/item) | categoria | GUT | dono | RFI | status`.
2. Um RFI por conflito, endereçado ao dono pela cadeia (Zanettini → Lelé → Cardozo → agente executor; legal → Lelé → Kelsen).
3. Registro de RFIs (aberto, respondido, fechado, ou aceito por Lelé com justificativa).

**Regras:**
- Não corrija nem redimensione disciplina alheia. Não proponha furo, reforço, viga, realocação ou nova cisterna como solução.
- Não decida conflito legal (taxa de ocupação, afastamento, gabarito). Encaminhe.
- Toda verificação com prova no mesmo arquivo. Onde faltou dado, escreva "não verifiquei X".
- Os memoriais são texto. A planta é tabular (eixos e cotas). Interferência de posição só aparece quando o memorial dá cota ou trajeto. Diga isso no parecer.

---

## 2. Pacote recebido

### 2.1 Planta de arquitetura (Lúcio/Oscar)

**PL-01 — Plantas de pavimentos (térreo e superior, em uma prancha).** Eixos horizontais A–C (A no fundo do lote, C na rua). Eixos verticais 1–3 (1 à esquerda).

*Térreo:*
- Escritório: eixos A–B / 1. Cotas 3,20 m × 4,00 m. Pé-direito bruto 2,80 m.
- Cozinha: eixos B–C / 1–2. Janela J-02 na fachada C/1, vão de 1,20 m, peitoril 0,90 m, verga 2,10 m.
- Lavanderia: eixos A–B / 2–3. Porta da lavanderia no eixo 2, vão 0,80 m, verga 2,10 m.
- Banheiro de serviço: eixos A–B / 3.
- Viga V-B (eixo B, trecho 1–3): ver M1.
- Área coberta do térreo: indicada em M6. Não somei as cotas (planta simplificada).

*Superior:*
- Suíte 1: eixos A–B / 1–2.
- Suíte 2: eixos B–C / 2–3, sobre a cozinha e a lavanderia.
- Reservatório superior: eixo C/3, dentro da suíte 2 (ver M2).

### 2.2 Memoriais (6)

**M1 — Estrutural (Baumgart, via Cardozo)**
- Laje L1 (teto do térreo e piso do superior): espessura 12 cm, laje plana, sem rebaixos previstos.
- Viga V-B (eixo B, trecho 1–3): 15 × 50 cm, face inferior em 2,15 m do piso térreo. Sem furo, abertura ou reforço previsto.
- Cargas: sobrecarga de piso residencial 1,5 kN/m²; peso próprio da laje. Reservatórios e caixas d'água: não considerados nesta revisão.
- Fundações: dimensionadas conforme "sondagem SPT do lote (anexo)". Anexo não incluso neste pacote.

**M2 — Hidrossanitário e gás (Saturnino, via Cardozo)**
- Ramal de esgoto DN75 da cozinha: trecho horizontal em eixo B, de 1 a 2, à cota 2,30 m do piso térreo.
- Ramal de água fria do banheiro de serviço: trecho em A/3, cota 0,30 m do piso.
- Ventilação mecânica da cozinha: duto de exaustão ø100 mm, trecho horizontal em A/2–3, cota 2,30 m do piso térreo.
- Gás GLP: tubo embutido em C/2, registro a 1,60 m do piso.
- Reservatório superior de água fria: 1.000 L, base 1,00 × 1,00 m, eixo C/3, sobre a laje da suíte 2.
- Cisterna enterrada de 5.000 L, a 1,20 m da divisa, eixo A (fundo do lote). Dimensões e fundação: "conforme projeto de reuso (não emitido nesta revisão)".
- Tubo de queda de águas pluviais PQ-1 ø75 mm, vertical em C/1, centro a 1,00 m do piso (dentro da largura de J-02).

**M3 — Elétrico e automação (Landell, via Cardozo)**
- QD-1: quadro de distribuição de 18 disjuntores, embutido na parede da lavanderia, eixo 3 entre A e B.
- Tomadas de bancada da cozinha a 1,10 m do piso, eixo B/1.
- Iluminação do escritório com luminárias de sobrepor, sem forro.

**M4 — Interiores (Tenreiro, via Cardozo)**
- Escritório: pé-direito de projeto 2,70 m (item 2.1).
- Cozinha: armário de parede fechado, módulo de 1,00 m no eixo C/2, de 0,00 a 2,10 m do piso, sem painel de acesso.
- Acabamentos de piso e parede da cozinha e do escritório.

**M5 — Paisagismo (Glaziou, via Cardozo)**
- Área permeável do lote: 62,00 m².
- Jardim frontal sem canteiro elevado e sem sobrecarga sobre laje.
- Drenagem do jardim: por infiltração no próprio solo.

**M6 — Legal e quadro de áreas (Hely, via Kelsen)**
- Quadro de áreas: escritório 13,60 m²; área coberta do térreo 152,00 m²; área do superior: 118,40 m²; terreno 300,00 m².
- Parâmetro citado do parecer de Hely (item 3.1): taxa de ocupação máxima de 50%.
- O parecer de conformidade de Kelsen (documento final) não consta deste pacote.

---

## 3. Entrega esperada

Matriz de conflitos, registro de RFIs e parecer curto. No parecer, diga:
- o que foi verificado (com prova) e o que não foi (com "não verifiquei");
- que a leitura é memorial × planta, sem desenho 3D;
- que o item de legal está encaminhado, não resolvido.
