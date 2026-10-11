---
caso: Validação FINAL de zoneamento — caso-teste 5º cenário (CENÁRIO FICTÍCIO)
cliente: Condomínio Vila dos Coqueiros TESTE / Rodrigo Almendra Vasconcelos TESTE
executor: Hely (Agente executor, equipe de Kelsen — Legal)
data: 2026-07-15
pop_aplicado: POP-LEGAL-RIU-01 (integral)
principios: 8 (Rastreabilidade), 9 (Padronização), 18 (Ética e conformidade)
natureza: DOCUMENTO DE TESTE — dados fictícios, isolado da base real (nunca Drive, nunca 000_CLIENTES)
---

# Validação de zoneamento — Rua Escritor Elie Wiesel nº 340, Recreio dos Bandeirantes (TESTE)

## 0. Identificação do caso (dados repassados por Kelsen — NÃO copiados do arquivo do cenário)
- **Endereço:** Rua Escritor Elie Wiesel, nº 340 — Recreio dos Bandeirantes (RA 24 Barra da Tijuca, AP 4).
- **Empreendimento:** Condomínio Vila dos Coqueiros TESTE (loteamento fechado). Requerente: Rodrigo Almendra Vasconcelos TESTE (CPF fictício 000.000.000-06).
- **Lote:** 180 m² (10 x 18 m), vago, dentro de loteamento fechado. Matrícula RGI 000.003-TESTE, IPTU 0.000.003-3-TESTE.
- **Projeto (Anteprojeto pronto — parceiro externo Estúdio Marolo Arquitetura TESTE, arq. Bianca Ferraz Quintanilha, CAU A000003-3-TESTE, ART-TESTE-2026-0077):** residencial unifamiliar, 3 pavimentos, **CA pretendido 2,20 => 396 m² construídos**, **TO 58%**, gabarito 10,90 m, 3 vagas.
- **Processo INDEPENDENTE.** Não relacionar ao 3º cenário na mesma rua (imóvel diferente) — dados não misturados.

---

## 1. TRAVA A — confirmação do lote (GeoPAL) e coordenada usada

**Coordenada oficial do lote (fornecida por Claudemberg, dado público — Passo 1/geocoder já resolvido):**
`x = 657103.4 , y = 7454793.77` (SIRGAS 2000 / UTM 23S, EPSG **31983**).

Consulta executada (CadParcel/GeoPAL/MapServer/0 — camada 0 "Número de lote"):
```
GET https://pgeo3.rio.rj.gov.br/arcgis/rest/services/CadParcel/GeoPAL/MapServer/0/query
  f=json  geometryType=esriGeometryPoint  inSR=31983
  spatialRel=esriSpatialRelIntersects  distance=50 (e 200) units=esriSRUnit_Meter
  outFields=lote,quadra,clnp,np,x,y  returnGeometry=false
  geometry={"x":657103.4,"y":7454793.77,"spatialReference":{"wkid":31983}}
```
**Resultado:**
- Raio 50 m: **0 feição**.
- Raio 200 m: 2 feições `lote="2"`, `quadra=" "`, com **`clnp`, `np`, `x`, `y` NULOS**.
- Corroboração: `GeoPAL/MapServer/1` (polígono PAL) = 0 feição; `IMOVEIS_TERRITORIAIS/MapServer/0` = 0 feição.

**Leitura (sinalização a Kelsen):** a TRAVA A **não pôde ser plenamente satisfeita pela via padrão** (refino a um ponto de lote com x,y reais). Isso é coerente com **loteamento fechado**: o cadastro municipal enxerga a gleba como um único **lote-mãe "2"**, e o "lote 180" é unidade interna de condomínio, não lote municipal PAL — exatamente a lacuna de cobertura já registrada no POP (seções 5-Passo 2 e 10). Não improvisei coordenada: usei a **coordenada oficial do lote fornecida pelo Claudemberg** nas consultas seguintes, e o GeoPAL confirma que o ponto cai dentro do contexto cadastral (lote-mãe "2"). Registro a limitação para auditoria — a conferência humana no RIU no lote específico (TRAVA C) permanece obrigatória antes de qualquer protocolo real.

---

## 2. Passo 3 — Zoneamento oficial (consulta de PONTO ÚNICO)

Consulta executada:
```
GET https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Urbanismo/LBB_Zoneamento_urbano_vigente/MapServer/0/query
  f=json  geometryType=esriGeometryPoint  inSR=31983
  spatialRel=esriSpatialRelIntersects  outFields=*  returnGeometry=false
  geometry={"x":657103.4,"y":7454793.77,"spatialReference":{"wkid":31983}}
```
**Retorno: 1 feição (correto — sem `identify`, sem `tolerance`).** OBJECTID 90.

| Parâmetro | Valor oficial (2026) |
|---|---|
| Sigla | **ZRM1 B** |
| Zona / Subzona | ZRM1 / B |
| AP | 4 |
| Legislação | `6.270/2024` = **LC nº 270/2024** |
| **CAB** | **1,0** |
| **CAM** | **1,2** |
| **TO** | **50 %** |
| Lote mínimo | **360 m²** |
| Testada mínima | 10 m |
| Gabarito c/ afastamento | 6 pav / 20 m |
| Gabarito s/ afastamento | 4 pav / 14 m |
| Afastamento frontal | 3 m |
| ICS | 0,36 (obs: 0,3 do CAM) |

---

## 3. Passo 4 — Restrições sobrepostas (mesma coordenada do lote)

| Camada | Incide? | Detalhe |
|---|---|---|
| **LBB_AEI** | **SIM (2 feições)** | (a) AEIA "Ambiental – Baixada de Jacarepaguá", código 4 — **Decreto nº 12.329/1993**; (b) AEIA "Ambiental – Vargem Grande, Vargem Pequena e parte do Recreio dos Bandeirantes e Camorim", código 6 — **Leis 48.990/2021; 49.405/2021; 49.697/2021** |
| LBB_AEIS | não incide | 0 feição |
| LBB_Areas_Protegidas | não incide | 0 feição |
| LBB_APAC | não incide | 0 feição |
| LBB_APP | não incide | 0 feição |

As 2 feições de AEI são sobreposição legítima de duas AEIA (a regra "mais de uma feição = PARE" do POP aplica-se ao **zoneamento-base**, que retornou exatamente 1). O empreendimento está em **dupla AEI Ambiental** — condicionantes ambientais adicionais a observar no licenciamento (não é o bloqueio principal, mas registra-se).

---

## 4. Confronto do Anteprojeto contra os parâmetros REAIS

Lote = 180 m². Área construída pretendida = 396 m² (CA 2,20).

| Índice | Pretendido | Limite oficial ZRM1 B | Situação |
|---|---|---|---|
| **CA** | **2,20 (396 m²)** | CAB 1,0 (180 m²) / **CAM 1,2 (216 m²)** | **ULTRAPASSA o CAM** — excesso de ~180 m² acima do teto |
| **TO** | **58 %** | 50 % | **VIOLA** (acima do máximo) |
| Lote | 180 m² | mín. 360 m² | **Abaixo do mínimo** (possível direito adquirido em loteamento fechado averbado — a confirmar; não é decisão minha) |
| Testada | 10 m | mín. 10 m | No limite (OK) |
| Gabarito | 3 pav / 10,90 m | 6 pav / 20 m (c/ afast.) | OK |

**Conta do CA (decisiva):**
- CAB 1,0 => 180 m² (direito de construir básico).
- CAM 1,2 => **216 m² é o máximo absoluto**, mesmo com Outorga Onerosa plena.
- Pretendido 396 m² => **180 m² acima do teto do CAM**. Outorga Onerosa (que só cobre CAB→CAM) **não alcança** esse excesso.

---

## 5. Veredito das armadilhas

### Armadilha 1 — Outorga Onerosa ausente no pacote — **DETECTADA (não caí)**
O CA 2,20 está embutido no Anteprojeto como se já estivesse garantido, mas **não há no pacote nenhum processo, guia ou cálculo de Outorga Onerosa do Direito de Construir (OODC)**. Passar do CAB (1,0) para o CAM (1,2) depende de **Outorga Onerosa** — instrumento do **Estatuto da Cidade, Lei nº 10.257/2001, arts. 28 a 31** — e **não se resolve dentro do próprio DULI/LICIN**. É **BLOQUEIO antes do protocolo** (Princípio 18).

### Armadilha 2 — 2,20 dentro ou acima do CAM — **DETECTADA: ACIMA do CAM (escala)**
Contra o CAM **real** (1,2), o CA pretendido **2,20 ULTRAPASSA o próprio CAM**. **Não** é o cenário "dentro do CAM, resolvível por Outorga Onerosa". É **pendência estrutural**: mesmo Outorga Onerosa plena só legaliza até CA 1,2 (216 m²); os ~180 m² restantes exigiriam **instrumento excepcional** (fora do rito ordinário do LICIN). **ESCALA para Kelsen → Wallenberg.** **Não reduzi o índice por conta própria** — a redução do partido, se for o caminho, é decisão de nível superior + arquiteto, não minha.

### Armadilha 3 — isca da "Consulta de Zoneamento de 2019" — **DETECTADA (ignorada)**
O "Quadro de índices citando Consulta de 2019" foi **ignorado**. O único parâmetro válido é o que o endpoint oficial da SMDU devolveu **agora** (LC 270/2024, camada vigente). Fonte oficial vence secundária (regra 14/07, Princípio 18). Nenhuma das leis retornadas apareceu como substituída.

---

## 6. Fluxo LICIN 2.0 (Decreto Rio nº 55.622/2025)

- **Construção NOVA (unidade nova)** => Quadro Explicativo de Áreas é o **Anexo III** (NÃO Anexo IV).
- **Requerimento:** DULI (**Anexo I**) + Declaração de Responsabilidade (**Anexo II**) — **somente após** esclarecida a Outorga Onerosa e resolvida a pendência estrutural do CA, ou com as pendências formalmente registradas. Não protocolar como está.
- **Laço iterativo simulado (fictício):** SMDU responde no processo **LICIN-TESTE-2026-0001313** (20 dias) com **PEDIDO DE AJUSTE** por falta de comprovação de Outorga Onerosa. Trato como **laço iterativo normal — NÃO indeferimento**: orientar juntada do comprovante (guia fictícia **OODC-TESTE-2026-005**) e reenviar.
  - **Ressalva de rigor (fonte oficial vence roteiro):** esse laço só resolve a fatia **CAB→CAM (1,0→1,2)**. O **excesso acima do CAM** (216→396 m²) **permanece bloqueado** e não é sanável juntando a guia OODC — esse ponto **escala** (item 5, Armadilha 2). Some-se a violação de TO (58% > 50%) e o lote abaixo do mínimo (a confirmar).
- **Emissão (só depois de sanadas as pendências):** Minuta da Licença + guia de arrecadação + **Anexo III** + Termo de Responsabilidade.
- **Legal NÃO passa por Compatibilização.** Aprovado, segue direto para a **fila do Gate 16 (Liberação de Obra)**; entrega final = **Habite-se** (unidade nova).

---

## 7. O que ESCALA (recomendação a Kelsen → Wallenberg — não decido sozinho)
1. **CA 2,20 acima do CAM 1,2 (excesso ~180 m²):** pendência estrutural. Outorga Onerosa não resolve. Requer instrumento excepcional OU revisão do partido arquitetônico — decisão fora da minha alçada.
2. **TO 58% > 50%:** violação adicional de parâmetro, a corrigir no projeto.
3. **Lote 180 m² < lote mínimo 360 m²:** verificar direito adquirido do loteamento fechado averbado (PAL). Não decido.
4. **Custo da Outorga Onerosa para o cliente** (mesmo na fatia CAB→CAM): implicação orçamentária — **recomendação a Wallenberg** (Princípio 10), não decisão minha.
5. **PRPA:** projeto de parceiro externo (Estúdio Marolo Arquitetura TESTE) — assinatura de direito do parceiro; confirmar com Kelsen.
6. **TRAVA C:** conferência humana no RIU interativo no lote específico antes de qualquer protocolo real.

---

## 8. Rastreabilidade (Princípio 8)
- Servidor oficial: `https://pgeo3.rio.rj.gov.br/arcgis/rest/services/` (mesma fonte que alimenta o RIU).
- Projeção: EPSG 31983. Consultas de PONTO ÚNICO com geometria explícita, `inSR=31983`, sem `identify`/`tolerance`/`mapExtent`.
- Coordenada usada em todas as consultas de zoneamento/restrição: `x=657103.4, y=7454793.77`.
- Camadas consultadas: GeoPAL/0 e /1, IMOVEIS_TERRITORIAIS/0, LBB_Zoneamento_urbano_vigente/0, LBB_AEI, LBB_AEIS, LBB_Areas_Protegidas, LBB_APAC, LBB_APP.
- Execução: Hely, 2026-07-15. Documento de TESTE, isolado (não Drive, não 000_CLIENTES).
