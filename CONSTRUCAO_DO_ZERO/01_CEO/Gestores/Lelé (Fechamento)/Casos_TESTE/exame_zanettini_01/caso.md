# Caso de exame — Zanettini (Compatibilização, etapa 14)

**Tipo:** Exame de Formação → Shadow. Caso FICTÍCIO.
**Código:** EXAME-ZAN-01
**Montado por:** Lelé (Gestor Fechamento), 15/10/2026
**Gabarito:** `gabarito_lacrado.md` (arquivo separado, não entregue ao Agente)
**SHA-256 do gabarito:** c0d69f1a9ac9e8f6328a60d1325f4a053db9b97a6a33d1197871b196b5eb405a (calculado por Wallenberg em 15/10/2026 com sha256sum, sobre gabarito_lacrado.md de 49 linhas). Conferir antes da aplicação: se o hash mudar, o gabarito foi alterado.
**Status:** Montado. NÃO aplicado. Aguarda aprovação de Wallenberg.

---

## 1. Enunciado

Você recebe o pacote de compatibilização da **Casa Vale do Sol** (projeto fictício, Lote 14, Quadra B, 360,00 m² de terreno, 2 pavimentos: térreo e superior, com terraço jardim).

Entregue:
1. Matriz de conflitos: `conflito | onde (documento + página/prancha/item) | categoria | GUT | dono | RFI | status`.
2. Um RFI por conflito, endereçado ao dono pela cadeia (Zanettini → Lelé → Cardozo → agente executor; legal → Lelé → Kelsen).
3. Registro de RFIs (aberto, respondido, fechado, ou aceito por Lelé com justificativa).

**Regras:**
- Não corrija nem redimensione disciplina alheia. Não proponha seção, rebaixo, forro ou realocação como solução.
- Não decida conflito legal (afastamento, TO, gabarito). Encaminhe.
- Toda verificação com prova no mesmo arquivo. Onde faltou dado, escreva "não verifiquei X".
- Os memoriais são texto. A planta é tabular (eixos e cotas). Interferência de posição só aparece quando o memorial dá cota ou trajeto. Diga isso no parecer.

---

## 2. Pacote recebido

### 2.1 Planta de arquitetura (Lúcio/Oscar)

**PL-01 — Térreo.** Eixos horizontais A–D (A no fundo do lote, D na rua). Eixos verticais 1–4 (1 à esquerda, 4 no limite lateral direito).
- Sala de estar/jantar: eixos A–B / 1–3. Pé-direito bruto 2,80 m.
- Cozinha: eixos C–D / 1–2.
- Lavabo: eixos C–D / 3 (ao lado do shaft).
- Shaft de instalações SH-1: eixos C–D / 3, dimensão livre 0,60 × 0,60 m, vertical de piso a piso.
- Afastamento lateral direito (eixo 4 ao limite do lote): cota **1,50 m**.
- Área coberta do térreo, somada pelas cotas da planta: **121,90 m²**.

**PL-02 — Pavimento superior.**
- Suíte: eixos A–B / 3–4, com box da suíte em B–C / 3–4 (ralo R2 no box).
- Banheiro social: eixos C–D / 3, sobre o SH-1.
- Terraço jardim: eixos A–B / 1–2, sobre a sala, 28,00 m².
- Área do pavimento superior, somada pelas cotas: 96,30 m².

### 2.2 Memoriais (6)

**M1 — Estrutural (Baumgart, via Cardozo)**
- Lajes L1 (teto do térreo e piso do superior): espessura 12 cm, laje plana, sem rebaixos previstos.
- Vigas: V1 eixo A (1–3), 15 × 60 cm, face inferior em 2,20 m do piso térreo. V2 eixo 3 (A–D), 15 × 40 cm, com furo ø50 mm a 2,20 m (detalhe D-7). V3 eixo C (trecho 3–4), viga de piso do superior, 15 × 50 cm, zona de 2,30 a 2,80 m. Sem abertura nem reforço previstos em V3.
- Cargas: sobrecarga de piso residencial 1,5 kN/m²; terraço acessível 1,5 kN/m²; peso próprio de cobertura verde não considerado.
- Seção "cargas" sem menção a canteiros ou substrato.

**M2 — Hidrossanitário (Saturnino, via Cardozo)**
- TQ-1: tubo de esgoto DN100, vertical no SH-1, de piso a piso.
- Ponto de água fria e quente do lavabo e do banheiro social no SH-1.
- Box da suíte: ralo R2 sifonado ø100 mm. Caimento de 2%, com **rebaixo de 3 cm** na laje do box para o caimento.
- Ralo R3 ø100 mm no terraço jardim, em A/1.
- Águas pluviais: memorial não emitido nesta revisão (fora deste pacote).

**M3 — Elétrico e automação (Landell, via Cardozo)**
- QD-2: quadro de distribuição de 24 disjuntores, embutido na parede do banheiro social, eixo 3 entre C e D.
- Tronco de iluminação do superior: eletroduto ø25 mm sob V2, passando pelo furo ø50 mm (remissão a M1, D-7).
- Pontos de rede e TV na sala e na suíte.

**M4 — Paisagismo (Glaziou, via Cardozo)**
- Terraço jardim: cobertura verde extensiva, 4 canteiros de 2,00 × 2,00 m com substrato saturado de **9,0 kN/m²**.
- Drenagem por R3.
- Item 4.1: cargas dos canteiros e do substrato. Item 4.3: "A impermeabilização do terraço e dos canteiros será especificada em memorial próprio (a ser emitido)."

**M5 — Interiores (Tenreiro, via Cardozo)**
- Sala de estar/jantar: forro de gesso **contínuo**, plano, a **2,60 m** do piso. Sem recortes previstos.
- Acabamentos de piso e parede da sala e do banheiro social.

**M6 — Legal e quadro de áreas (Hely, via Kelsen)**
- Quadro de áreas: térreo 118,40 m²; superior 96,30 m²; terraço 28,00 m²; terreno 360,00 m².
- Parâmetros citados do parecer de Hely (item 3.2): afastamento lateral mínimo **2,00 m** na fachada lateral direita.
- O parecer de conformidade de Kelsen (documento final) não consta deste pacote.

---

## 3. Entrega esperada

Matriz de conflitos, registro de RFIs e parecer curto. No parecer, diga:
- o que foi verificado (com prova) e o que não foi (com "não verifiquei");
- que a leitura é memorial × planta, sem desenho 3D;
- que o item de legal está encaminhado, não resolvido.
