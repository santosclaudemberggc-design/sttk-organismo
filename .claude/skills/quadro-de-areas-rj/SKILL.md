---
name: quadro-de-areas-rj
description: Quadro de áreas legal do Rio de Janeiro (LC 270/2024 Arts. 345-353; COES LC 198/2019 Arts. 8º, 9º, 26, 31 e glossário; Dec. 3.046/81 Disposições Gerais na Barra/Recreio) traduzido em FATOR DE CÔMPUTO por área para a ferramenta Vitruvius `criar_quadro_areas` (listas `fatores` e `manuais`, esquemas TO, CA e PERM) — o que entra e o que sai da ATE, da projeção (TO) e da Superfície Mínima Drenante (SMD), com artigo e página de cada regra e a marca "interpretação — Gate" onde a lei não diz. Use sempre que Hely montar quadro de áreas do DULI (Anexo III ou IV), Oscar/Lúcio conferir TO, CA ou permeabilidade de um estudo (volumetria, partido, Estudo Preliminar), Villaça precisar da ATE computável, ou alguém perguntar "isso computa?", "entra na taxa de ocupação?", "quanto tem de ser permeável?", "concregrama conta?", "varanda/beiral/garagem/piscina/deck entra na conta?", mesmo que o pedido não cite a LC 270 pelo nome.
status: proposta-em-treino
version: v0.1
data: 2026-10-20
dono: Kelsen (Legal)
agente_principal: Hely (DULI, quadro de áreas legal)
agentes_cross: Oscar/Lúcio (Estudo Preliminar, volumetria), Villaça (viabilidade CAB x CAM), Vitruvius (ferramenta criar_quadro_areas)
origem: "Pedido de Claudemberg (20/10/2026) via Kelsen. Pesquisa de procedimento em D:/011_VITRUVIUS/PESQUISA_QUADRO_AREAS_20-10.md (vídeos de SP/interior: procedimento de Revit, NÃO regra do Rio). Redação e leitura do primário: Hely, 20/10/2026."
fonte_primaria_lida: "Hely, 20/10/2026, por TEXTO (pdftotext por página, sem rasterização): LC 270/2024 (LC270_2024_PlanoDiretorLUOS.pdf) pp. 122-130 (Arts. 344-363); COES consolidado SMU (COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf) pp. 5-6 (Arts. 8º-9º), 13 (Art. 26), 14 (Art. 28), 17 (Art. 31), 22 (Art. 39 §5º), 24-30 (glossário); Dec. 3.046/81 (Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf) pp. 2-5 (Cap. II, Disposições Gerais I-XXXI); Dec. 45.917/2019 pp. 1-2 (Arts. 1º-11). NÃO relido nesta rodada: Anexo XXI da LC 270 (p. 275, conferido por imagem pelo Hely em 14/10/2026)."
---

# Quadro de áreas — Rio de Janeiro (fator de cômputo para o Vitruvius)

> RESSALVA. Skill em treino, não ratificada. Todo número que ela ajuda a produzir é **análise preliminar** até passar pelo Gate da Coordenação (Claudemberg, via Kelsen/Artigas). Status de vigência das normas: a LC 270, o COES consolidado e o Dec. 45.917 foram baixados da Busca Fácil da SMU; reconfirmar o status no ponto de uso (`legal-base-legislativa-bairro`, passo obrigatório). O Dec. 3.046/81 não aparece por número na Busca Fácil (pendência aberta do Hely, 01/10/2026).

## 0. O que esta Skill é, e o que ela não é

A ferramenta `criar_quadro_areas` do Vitruvius calcula:

- **TO** = Σ(projeção x fator) / área do lote
- **CA** = Σ(área construída por pavimento x fator) / área do lote
- **Permeabilidade** = Σ(área x fator) / área do lote
- e compara com `{toMax %, caMax, tpMin %}`.

Esta Skill diz **qual fator** cada tipo de área recebe no Rio, e **de onde** ele vem. Ela **não** traz TO, CAB, CAM nem gabarito de zona ou subzona: esses saem do Anexo XXI da LC 270 ou do RIU do lote (Skill `legal-base-legislativa-bairro`). Não complementa nem substitui as Skills de varanda, vaga e Dec. 3.046 — remete a elas.

**Vídeos e blogs de SP não valem aqui.** O 0,7 do concregrama, o "beiral até 0,80 m não entra" e o "varanda acima de 1 m entra" são regras de outros municípios (pesquisa de 20/10, fontes V1-V7 e Sienge). No Rio, vale o texto abaixo.

Convenção de marca em cada fator:
- **lei** = texto expresso, com artigo e página do PDF da base (`Fontes_Legislacao/` do Hely).
- **lei (leitura direta)** = decorre do caput sem esforço (ex.: área descoberta não é "área coberta").
- **interpretação — Gate** = a lei não diz; o fator é escolha nossa, conservadora salvo indicação, e precisa de validação antes de virar premissa de cliente.

## 1. ATE / CA — o que entra e o que sai (LC 270, Arts. 345-347)

- **Art. 345** (p. 122): CA = ATE permitida / área do terreno. CAB e CAM no Anexo XXI (§2º). **AP4, ZPP:** onde o IAA da subzona do Dec. 3.046 é < 1, CAB = IAA (§4º III a, p. 123); CAM = IAA da subzona (§5º, p. 123). CAB = CAM -> sem OODC (§3º).
- **Art. 346** (p. 123): ATE = CA x área do terreno.
- **Art. 347 caput** (p. 123): ATE = **soma de toda área coberta** das edificações, menos as partes dos incisos (p. 124). §1º: essas partes também ficam fora da OODC.

| Elemento | Fator CA | Fonte |
|---|---|---|
| Área coberta fechada de qualquer pavimento acima do solo | 1 | lei — Art. 347 caput, p. 123 |
| Portaria, marquise, pórtico, pergolado, platibanda, beiral, acessos | 0 | lei — Art. 347 I, p. 124 |
| Vaga coberta ou descoberta, inclusive acesso e manobra (sem limite de nº) | 0 | lei — Art. 347 II, p. 124 (ver Skill de vaga) |
| Guarda de bicicletas | 0 | lei — Art. 347 III, p. 124 |
| Compartimentos e terraços cobertos de uso comum (grupamento) | 0 | lei — Art. 347 IV, p. 124 |
| Guarita | 0 | lei — Art. 347 V, p. 124; COES Art. 26 §1º, p. 13 |
| Edícula — fora da ZPP | 0 só "nas condições do COES"; na dúvida, **1** | lei — Art. 347 V, p. 124 + interpretação — Gate (ver §1.1) |
| Edícula — ZPP (Barra/Recreio), unifamiliar | **1** | lei — Dec. 3.046 Disp. Gerais XV, p. 3 (ver §1.1) |
| Varanda / sacada de unidade residencial, em balanço ou reentrante | 0 | lei — Art. 347 VI, p. 124; COES Art. 8º §4º, p. 5 |
| Varanda térrea saliente (nem balanço nem reentrante), fora da ZPP | **1** (conservador) | interpretação — Gate (COES §4º só nomeia "balanço ou reentrante") |
| Varanda aberta, coberta ou descoberta — ZPP | 0 | lei — Dec. 3.046 VII, pp. 2-3 (unifamiliar: remete ao XI) |
| Subsolo | 0 | lei — Art. 347 VII, p. 124 |
| Caixa d'água, casa de máquinas, compartimento técnico (qualquer nível) | 0 | lei — Art. 347 VIII, p. 124 |
| Jirau | 0 nas condições do COES | lei — Art. 347 IX, p. 124 (raro em unifamiliar) |
| Área descoberta (piscina, deck, terraço descoberto, quintal) | 0 | lei (leitura direta) — Art. 347 caput: só soma área coberta |
| Saliência de jardineira/ar-condicionado até 0,40 m sobre afastamento frontal — ZPP | 0 | lei — Dec. 3.046 XIV, p. 3 |
| Aproveitamento da cobertura do último pavimento — ZPP | 1 | lei — Dec. 3.046 XXVIII, p. 5 ("a ser computado na A.T.E.") |
| Varanda fechada fora do COES §10 (não retrátil, incorporada) | 1 | lei — COES Art. 8º §§10-11, p. 6 (LC 192/2018) |

### 1.1 Edícula — tensão aberta (não decida sozinho)

- LC 270 Art. 347 V e Art. 350 IV tiram a edícula da ATE e da TO "nas condições do COES".
- COES Art. 26 (p. 13) define edícula permitida como apoio **às partes comuns da edificação** — texto pensado para grupamento; não está claro que a edícula de casa unifamiliar se enquadre.
- Dec. 3.046 XV (p. 3), ZPP, unifamiliar: edícula de até 2 pavimentos **computa** ATE e TO.
- Fator de trabalho: **1** na ZPP (lei); **1** fora dela até o Gate dizer o contrário (interpretação — Gate). Tensão já levada a Kelsen em 01/10/2026 (pendência "Ensaio 003 — tensões normativas da ZPP", item 1).

## 2. TO — fórmula e o que entra na projeção (LC 270, Arts. 349-350)

- **Art. 349** (p. 124): TO = (Área da Projeção Horizontal da Edificação x 100) / Área do Terreno. Máximo por zona/subzona no Anexo XXI (p.ú.). ZPP: Anexo XXI diz "ver Dec. 3046" (p. 275, lido por imagem em 14/10; não relido hoje) — TO sai da subzona, **e só com o lote identificado** (Skill `decreto3046-...`; registro `TO_ZPP_ZE5_por_subzona_Dec3046_14-10-2026.md`).
- **Art. 350 caput** (p. 125): a projeção inclui **toda a área coberta** da edificação, menos:
  - I — áreas **em balanço** de varandas, sacadas, saliências e marquises, nos termos do COES;
  - II — varandas e terraços **assentes no terreno**, em uni, bi e multifamiliares;
  - III — estacionamento coberto nos termos do COES, uni e bifamiliar, **limitado a uma vaga**;
  - IV — edículas, guaritas e pórticos, nos termos do COES;
  - V — subsolo; VI — castelos d'água e ETE; VII — embasamento; VIII — teatro e cinema.
- COES glossário, "PROJEÇÃO HORIZONTAL" (p. 28): toda a área coberta, excluídas as áreas em balanço, como varandas, sacadas e saliências. COES Art. 39 §5º (p. 22): projeção é definida pela LUOS.
- COES Art. 8º §4º (p. 5): varanda e sacada residencial, em balanço ou reentrante, fora da ATE **e da TO**.

| Elemento | Fator TO | Fonte |
|---|---|---|
| Térreo coberto + todo pavimento superior que sai do contorno do térreo (área coberta) | 1 | lei — Art. 350 caput, p. 125 |
| Varanda/sacada residencial em balanço ou reentrante | 0 | lei — Art. 350 I, p. 125; COES Art. 8º §4º, p. 5 |
| Varanda ou terraço assente no terreno (uni/bi/multi) | 0 | lei — Art. 350 II, p. 125 |
| Marquise em balanço (COES Art. 9º, pp. 5-6: altura útil >= 2,50 m, água para dentro do lote, >= 1,50 m das divisas laterais/fundos) | 0 | lei — Art. 350 I, p. 125 |
| Marquise apoiada em pilares | 1 | interpretação — Gate (o I só exclui a marquise "em balanço") |
| Beiral | **1** (conservador) | interpretação — Gate: o Art. 350 não nomeia "beiral" (o 347 I nomeia, mas só para ATE). Leitura favorável possível: beiral = saliência em balanço (350 I + glossário) -> 0. Decidir no Gate |
| Pergolado vazado, sem cobertura | 0 | interpretação — Gate (não é "área coberta"; se receber telha, vidro ou policarbonato, vira 1) |
| Garagem coberta — 1ª vaga, uni/bifamiliar, nos termos do COES | 0 | lei — Art. 350 III, p. 125 |
| Garagem coberta — 2ª vaga em diante | 1 | lei — Art. 350 III, p. 125 ("limitado a uma vaga") |
| Abrigo de veículo ou varanda no afastamento lateral do térreo, aberto e em telha-vã, unifamiliar com afastamento frontal < 10 m — ZPP | 0 | lei — Dec. 3.046 XI, p. 3 |
| Edícula | ver §1.1 (ZPP: 1 por lei; fora: 1 conservador) | Art. 350 IV p. 125 x Dec. 3.046 XV p. 3 |
| Guarita, pórtico | 0 | lei — Art. 350 IV, p. 125 |
| Subsolo (enterrado/semienterrado, Art. 354 §8º p. 128) | 0 | lei — Art. 350 V, p. 125 |
| Compartimento técnico no térreo (que não seja castelo d'água/ETE) | 1 | lei — Art. 350 caput (não está entre as exceções) |
| Piscina descoberta, deck descoberto, quintal | 0 | lei (leitura direta) — Art. 350 caput: só área coberta |
| Piscina coberta | 1 | lei (leitura direta) — área coberta, não listada nas exceções |

**Lembrete do método (checklist do Hely, item 1):** em casa de 2 pavimentos com TO baixa, o limite que morde costuma ser **2 x TO**, não a ATE. Mostre os dois.

**Na ZPP**, a regra de garagem coberta tem tensão aberta: Dec. 3.046 XXIII (pp. 4-5) só admite local coberto para veículo em subsolo ou pavimento-garagem; se isso alcança a casa unifamiliar está em aberto (pendência de 01/10, item 3). Ver `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`.

## 3. Permeabilidade / SMD (LC 270, Arts. 351-353)

- **Art. 351** (p. 125): SMD = percentual mínimo do terreno **livre de impermeabilização em qualquer nível**, preferencialmente com cobertura vegetal existente.
- **Art. 352 caput** (p. 125): SMD = **20% da área livre resultante da TO máxima** do Anexo XXI. Para a ferramenta: `tpMin % = 0,20 x (100 - TOmax %)`. Ex.: TOmax 50% -> tpMin 10% do lote. É o TO **máximo da zona**, não o TO do projeto.
- Art. 352 §2º (p. 125, redação da LC 274): "infraestrutura verde" = dispositivos que ampliam a área drenante com vegetação, técnicas e materiais. **Não fixa coeficiente para nenhum material.** §1º e §7º vetados.
- Art. 352 §3º-§4º e §8º (pp. 125-126): solo de drenagem insuficiente -> medidas compensatórias, até fora do lote na mesma sub-bacia, com aceite do órgão de drenagem.
- Art. 352 §5º (p. 126): isentos — ZCA e ZA; ZDM e ZEI na AP3; normas específicas; **áreas sem exigência de TO**. §6º: 15 bairros da AP3 = 70% da área livre mínima.
- **Art. 353** (p. 126): III — a SMD pode ser dividida, **cada porção >= 4 m² e nenhuma dimensão < 2 m**; II — conectada à drenagem; **§4º — não se admite subsolo na SMD.**
- Dec. 3.046/81: varredura do texto não achou regra de permeabilidade ou área drenante (0 ocorrências). **Na ZPP, a SMD do Art. 352 calculada com a TO da subzona é interpretação — Gate** (o Anexo XXI manda "ver Dec. 3046" para a TO).

| Elemento | Fator PERM | Fonte |
|---|---|---|
| Jardim/gramado sobre solo natural, porção >= 4 m² e lados >= 2 m | 1 | lei — Arts. 351 e 353 III, pp. 125-126 |
| Porção drenante menor que 4 m² ou com lado < 2 m | 0 | lei — Art. 353 III, p. 126 (não conta para a SMD) |
| Jardim sobre laje, sobre subsolo ou telhado verde | 0 | lei — Art. 351 ("em qualquer nível") e Art. 353 §4º, pp. 125-126 |
| Edificação, piscina, calçada, piso cimentado/cerâmico, muro | 0 | lei (leitura direta) — Art. 351, impermeabilizado |
| Concregrama / piso intertravado drenante / brita | **0** (conservador) | interpretação — Gate. **A lei do Rio não fixa fração.** Não usar o 0,7 de SP. Fator diferente de 0 só com aceite expresso (Gate, ou órgão de drenagem via §2º/§3º) |
| Deck de madeira vazado sobre solo natural, sem laje | **0** (conservador) | interpretação — Gate (pode ser 1 se o solo abaixo ficar sem impermeabilização; a lei não trata deck) |

Se o Gate aceitar fração para algum material, ela entra **na lista `fatores` com a fonte da aceitação**, nunca como número de mercado.

## 4. Barra da Tijuca / Recreio (ZPP — Dec. 3.046/81, mantido pela LC 270)

Leia antes a Skill `decreto3046-81-lc270-2024-licin-barra-recreio`. O que muda no quadro de áreas (Dec. 3.046, Cap. II, Disposições Gerais, que valem para todas as subzonas salvo disposição específica — p. 2):

- **VI** (p. 2): A.T.E. = I.A.A. x S. CAB = CAM = IAA quando IAA < 1 (LC 270 Art. 345 §§4º-5º, pp. 122-123).
- **VII** (pp. 2-3): varanda aberta, coberta ou descoberta, fora da ATE, da área útil mínima e da TO; mas respeita o afastamento frontal mínimo, **sem balanço sobre ele**. Unifamiliar: aplica-se o **XI** (permissivo).
- **XI** (p. 3): unifamiliar com afastamento frontal < 10 m: varanda ou abrigo de veículo no afastamento lateral do térreo, aberto e em telha-vã, fora da ATE e da TO.
- **XIV** (p. 3): saliência <= 0,40 m (jardineira, ar-condicionado) sobre o afastamento frontal, fora da ATE e da TO.
- **XV** (p. 3): edícula de unifamiliar, até 2 pavimentos, **computa** ATE e TO.
- **XXIII-XXIV** (pp. 4-5): garagem coberta só em subsolo ou pavimento-garagem; rampa a >= 5 m do alinhamento.
- **XXVIII** (p. 5): cobertura aproveitada computa ATE; até 50% do pavimento inferior; afastamentos de 5 m (3 m em A-1 e A-20).

**Não cite TO, IAA nem gabarito de subzona sem o lote identificado** (RIU / `POP-LEGAL-RIU-01`). E confirme a AP antes de ler a linha do Anexo XXI: parte da AP4 hoje é zoneada pela LC 270 (ZCS etc.), não pela subzona do Dec. 3.046 (caso "Av. Projetada Canal 2"). Tensões abertas com a LC 270/COES (edícula, varanda, garagem): pendência do Hely de 01/10/2026, decisão de Kelsen.

## 5. Listas para o Vitruvius — casa unifamiliar típica

Convenção de nomes no Revit (as regex dependem disso): cada Área recebe nome com prefixo de tipo. A ferramenta usa a **primeira** regra que casar; por isso as regras específicas vêm antes da genérica `.*`. Fatores valem para **fora da ZPP**; ajustes da ZPP no fim.

### 5.1 `fatores` (por esquema)

```json
{
  "TO": [
    {"padrao": "(?i)^varanda (balanco|reentrante)", "fator": 0, "fonte": "lei: LC270 Art.350 I p.125; COES Art.8 §4 p.5"},
    {"padrao": "(?i)^sacada", "fator": 0, "fonte": "lei: LC270 Art.350 I p.125; COES Art.8 §4 p.5"},
    {"padrao": "(?i)^varanda terrea|^terraco terreo", "fator": 0, "fonte": "lei: LC270 Art.350 II p.125"},
    {"padrao": "(?i)^marquise balanco", "fator": 0, "fonte": "lei: LC270 Art.350 I p.125; COES Art.9 pp.5-6"},
    {"padrao": "(?i)^marquise apoiada", "fator": 1, "fonte": "interpretacao - Gate"},
    {"padrao": "(?i)^beiral", "fator": 1, "fonte": "interpretacao - Gate (conservador; leitura favoravel = 0)"},
    {"padrao": "(?i)^pergolado vazado", "fator": 0, "fonte": "interpretacao - Gate (sem cobertura)"},
    {"padrao": "(?i)^garagem coberta vaga 1$", "fator": 0, "fonte": "lei: LC270 Art.350 III p.125 (limitado a uma vaga)"},
    {"padrao": "(?i)^garagem coberta", "fator": 1, "fonte": "lei: LC270 Art.350 III p.125 (2a vaga em diante)"},
    {"padrao": "(?i)^edicula", "fator": 1, "fonte": "interpretacao - Gate fora da ZPP; lei na ZPP (Dec.3046 XV p.3)"},
    {"padrao": "(?i)^(guarita|portico)", "fator": 0, "fonte": "lei: LC270 Art.350 IV p.125"},
    {"padrao": "(?i)^subsolo", "fator": 0, "fonte": "lei: LC270 Art.350 V p.125"},
    {"padrao": "(?i)^(piscina descoberta|deck|quintal|jardim|calcada)", "fator": 0, "fonte": "lei (leitura direta): Art.350 caput, so area coberta"},
    {"padrao": "(?i)^piscina coberta", "fator": 1, "fonte": "lei (leitura direta): Art.350 caput"},
    {"padrao": ".*", "fator": 1, "fonte": "lei: LC270 Art.350 caput p.125 (toda area coberta)"}
  ],
  "CA": [
    {"padrao": "(?i)^(varanda (balanco|reentrante)|sacada)", "fator": 0, "fonte": "lei: LC270 Art.347 VI p.124; COES Art.8 §4 p.5"},
    {"padrao": "(?i)^varanda terrea", "fator": 1, "fonte": "interpretacao - Gate (COES §4 so nomeia balanco/reentrante)"},
    {"padrao": "(?i)^(marquise|portico|pergolado|platibanda|beiral|acesso)", "fator": 0, "fonte": "lei: LC270 Art.347 I p.124"},
    {"padrao": "(?i)^garagem", "fator": 0, "fonte": "lei: LC270 Art.347 II p.124 (sem limite de vagas)"},
    {"padrao": "(?i)^bicicletario", "fator": 0, "fonte": "lei: LC270 Art.347 III p.124"},
    {"padrao": "(?i)^guarita", "fator": 0, "fonte": "lei: LC270 Art.347 V p.124"},
    {"padrao": "(?i)^edicula", "fator": 1, "fonte": "interpretacao - Gate fora da ZPP; lei na ZPP (Dec.3046 XV p.3)"},
    {"padrao": "(?i)^subsolo", "fator": 0, "fonte": "lei: LC270 Art.347 VII p.124"},
    {"padrao": "(?i)^(tecnico|caixa d.agua|casa de maquinas)", "fator": 0, "fonte": "lei: LC270 Art.347 VIII p.124"},
    {"padrao": "(?i)^(piscina descoberta|deck|terraco descoberto|quintal)", "fator": 0, "fonte": "lei (leitura direta): Art.347 caput, so area coberta"},
    {"padrao": ".*", "fator": 1, "fonte": "lei: LC270 Art.347 caput p.123"}
  ],
  "PERM": [
    {"padrao": "(?i)^jardim solo natural", "fator": 1, "fonte": "lei: LC270 Arts.351 e 353 III pp.125-126 (porcao >= 4 m2, lados >= 2 m)"},
    {"padrao": "(?i)^jardim (sobre laje|sobre subsolo)|^telhado verde", "fator": 0, "fonte": "lei: LC270 Art.351 e Art.353 §4 pp.125-126"},
    {"padrao": "(?i)^concregrama|^piso drenante|^brita", "fator": 0, "fonte": "interpretacao - Gate (lei do Rio nao fixa fracao; nao usar 0,7 de SP)"},
    {"padrao": "(?i)^deck", "fator": 0, "fonte": "interpretacao - Gate (conservador)"},
    {"padrao": ".*", "fator": 0, "fonte": "lei (leitura direta): LC270 Art.351 (impermeabilizado)"}
  ]
}
```

Se a ferramenta só aceitar `{padrao, fator}`, retire `fonte` do JSON enviado e mantenha esta tabela como prova anexa ao quadro.

**Ajustes na ZPP (Barra/Recreio):** TO e CA `^edicula` = 1 por **lei** (Dec. 3.046 XV, p. 3); CA `^varanda terrea` = 0 por **lei** (Dec. 3.046 VII, pp. 2-3), se não estiver em balanço sobre o afastamento frontal mínimo; acrescentar `^abrigo lateral telha-va` = 0 em TO e CA (Dec. 3.046 XI, p. 3, só com afastamento frontal < 10 m); `^cobertura aproveitada` = 1 em CA (XXVIII, p. 5). Garagem coberta fora do subsolo: tensão XXIII aberta — não modele sem Kelsen.

### 5.2 Exemplos de `manuais` (contornos desenhados à mão)

Medidas são de exemplo; o contorno real vem do modelo.

```json
[
  {"esquema": "TO",   "nome": "Varanda balanco sala (1o pav)", "fator": 0, "contorno": "contorno da laje em balanco, alem da face do terreo",       "fonte": "lei: LC270 Art.350 I p.125"},
  {"esquema": "CA",   "nome": "Varanda balanco sala (1o pav)", "fator": 0, "contorno": "mesmo contorno, area de piso",                              "fonte": "lei: LC270 Art.347 VI p.124"},
  {"esquema": "TO",   "nome": "Sacada suite",                   "fator": 0, "contorno": "contorno da sacada",                                         "fonte": "lei: COES Art.8 §4 p.5"},
  {"esquema": "TO",   "nome": "Beiral fachada norte",           "fator": 1, "contorno": "faixa do beiral alem da face da parede",                    "fonte": "interpretacao - Gate"},
  {"esquema": "TO",   "nome": "Garagem coberta vaga 1",         "fator": 0, "contorno": "retangulo 2,50 x 5,00 m da 1a vaga",                         "fonte": "lei: LC270 Art.350 III p.125"},
  {"esquema": "TO",   "nome": "Garagem coberta vaga 2",         "fator": 1, "contorno": "retangulo da 2a vaga",                                       "fonte": "lei: LC270 Art.350 III p.125"},
  {"esquema": "CA",   "nome": "Garagem coberta (vagas + manobra)", "fator": 0, "contorno": "toda a garagem coberta",                                  "fonte": "lei: LC270 Art.347 II p.124"},
  {"esquema": "PERM", "nome": "Deck piscina",                   "fator": 0, "contorno": "contorno do deck",                                           "fonte": "interpretacao - Gate"},
  {"esquema": "PERM", "nome": "Piscina",                        "fator": 0, "contorno": "espelho d'agua + borda",                                     "fonte": "lei (leitura direta): Art.351"},
  {"esquema": "PERM", "nome": "Jardim solo natural fundos",     "fator": 1, "contorno": "porcao >= 4 m2 e lados >= 2 m, sem subsolo embaixo",          "fonte": "lei: LC270 Art.353 III e §4 p.126"}
]
```

## 6. Validação antes de entregar o quadro

1. **Área do lote vem do Levantamento** (medida local), digitada como parâmetro "Área do lote" em Informações do Projeto — não medida no desenho e não copiada do título. Se divergir do título/PAL, as **duas** vão para a planta de situação (Dec. 55.622, Anexo I, item 1) e a escolha da área que entra nos índices é feita com o Hely e declarada no quadro (Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj`, §3-§4). Usar a menor das duas até a decisão é **interpretação — Gate** (conservadora).
2. **As áreas do esquema PERM (ou do térreo) somam 100% do lote.** Se não fecham, há contorno faltando ou sobreposto. Não entregue.
3. Programa pedido x teto computável lado a lado, com diferença em m² e a palavra "computável" ou "construída" (checklist do Hely, item 1). Mostre ATE e 2 x TO.
4. Toda linha com fator 0 ou fração tem fonte: artigo + página, ou "interpretação — Gate".
5. `toMax`, `caMax` e a TO usada no `tpMin` vêm do RIU ou do Anexo XXI **do lote**, com a fonte escrita no quadro.
6. Varanda que foi fechada, cômodo disfarçado de varanda ou garagem virando sala: fator 1 (Skill de varandas, "limite ético/legal").
7. **Todo resultado é análise preliminar até o Gate da Coordenação (Claudemberg).** Nunca vai a cliente nem a protocolo como parecer final antes disso.

## 7. O que a lei do Rio não fixa (lido hoje, procurado e não achado)

- Fração de permeabilidade para concregrama, piso drenante, brita ou deck (LC 270 Arts. 351-353; COES; Dec. 3.046: 0 ocorrências de "concregrama", "semipermeável" na regra de SMD).
- Beiral na projeção da TO (o Art. 350 não o nomeia; o 347 I só trata de ATE).
- Pergolado na TO (o Art. 350 não o nomeia).
- Profundidade máxima de beiral ou de varanda para não computar (o Art. 8º do COES não tem limite de área nem de balanço para o residencial). Atenção: varanda reentrante com mais de 1,50 m que ventila ou ilumina cômodo passa a ser tratada como prisma (COES Art. 5º §5º, conforme a Skill de varandas) — é regra de ventilação, não muda o fator, mas pode inviabilizar o desenho.
- Regra de permeabilidade própria do Dec. 3.046/81.
- Edícula de casa unifamiliar fora da ZPP (COES Art. 26 fala de apoio às partes comuns).

## 8. Relação com outras Skills (coerência)

- `legal-base-legislativa-bairro`: de onde vêm TO, CAB, CAM e SMD do lote. Esta Skill não repete parâmetro de zona.
- `varandas-nao-computaveis-ate-to-coes-lc198-rj`: condições de distância, fechamento e brise. Esta Skill só dá o fator.
- `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`: dimensão da vaga e regra da 1ª vaga. Mesma leitura do Art. 350 III e 347 II.
- `decreto3046-81-lc270-2024-licin-barra-recreio`: subzona, IAA e TO na ZPP.
- `levantamento-topografico-cadastral-orientado-duli-licin-rj`: origem da área do lote e escolha título x medida local.
