# Caso de exame — Limmer (Orçamento Executivo e Premissas, etapa 16)

**BLOQUEADO: aguarda Skill de orçamento analítico aprovada.** A Skill de orçamento analítico (BDI, encargos, SINAPI desonerado ou não, composição, curva ABC) ainda não foi aprovada por Wallenberg. Este caso foi montado mesmo assim, mas NÃO deve ser aplicado enquanto o bloqueio estiver ativo.

**Tipo:** Exame de Formação → Shadow, primeira tentativa. Caso FICTÍCIO.
**Código:** EXAME-LIM-01
**Montado por:** Lelé (Gestor Fechamento), 15/10/2026, por pedido de Wallenberg com aprovação de Claudemberg.
**Gabarito:** `gabarito_lacrado.md` (arquivo separado, não entregue ao Limmer). Escrito antes de qualquer aplicação.
**SHA-256 do gabarito:** 5f71932742e210b7164c778ccb6ba8c2279dfad211c7e5ffe389ef07dc94cdef (calculado por Wallenberg em 15/10/2026 com sha256sum). Conferir antes da aplicação.
**Status:** Montado. NÃO aplicado. BLOQUEADO até a Skill de orçamento analítico ser aprovada por Wallenberg.

---

## 1. Enunciado

Você recebe o pacote da **Casa Pau-Brasil** (projeto fictício, Lote 03, Quadra K, 280,00 m² de terreno, 2 pavimentos, 240,00 m² de área construída: térreo 130,00 m² e superior 110,00 m²; acabamento de padrão médio).

Entregue:
1. Quantitativo por serviço com memória de cálculo (documento, prancha e conta em cada linha).
2. Planilha de orçamento analítico: serviço, quantidade, composição, código, data-base, regime (desonerado ou não), preço unitário, total e fonte de cada preço.
3. Premissas explícitas: BDI com composição, encargos, data-base, regime, insumos regionais, o que está fora do escopo, contingência (se houver, justificada).
4. Comparação com a estimativa de viabilidade do Mascaró (lida, não refeita) com a explicação de cada desvio relevante.
5. Cronograma físico-financeiro resumido por etapa.
6. Lista de lacunas: cada item que você não conseguiu fechar, com "não verifiquei X" e quem deve.

**Regras:**
- Todo preço tem fonte, código e data. Número sem fonte é reprova direta.
- Não refaça a estimativa de viabilidade (Villaça e Mascaró) nem estime revenda (Fiker).
- Não mude especificação para baixar custo. Proponha a Lelé como engenharia de valor.
- Você não tem acesso à base SINAPI nem à TCPO neste exame: onde não conferiu, escreva "não verifiquei" e não complete com memória.
- Não fale com fornecedor, não prometa preço fechado e não fale com o cliente.

---

## 2. Pacote recebido

### 2.1 Quantitativo de serviços (Reidy, incorporado, rev. B, 12/10/2026)

| Item | Serviço | Qtd | Un | Memória (documento / prancha) |
|---|---|---|---|---|
| 1.1 | Canteiro e serviços preliminares | 1 | vb | Memorial de canteiro |
| 1.2 | Escavação de sapatas | 14,20 | m³ | M-EST rev. B, planilha de sapatas (anexo) |
| 1.3 | Concreto armado de fundação (sapatas) | 9,80 | m³ | M-EST rev. B, planilha de sapatas |
| 1.4 | Alvenaria de vedação em bloco cerâmico 14 cm | 412,00 | m² | PE-02, PE-03; área de paredes conferida pelo Reidy |
| 1.5 | Laje maciça 12 cm (térreo e superior) | 186,00 | m² | M-EST rev. B, L1 e L2 |
| 1.6 | Escada em concreto pré-moldado | 1 | un | PE-07 (DET-12) |
| 1.7 | Impermeabilização de box, lajes molhadas e área externa (manta) | 74,00 | m² | M-HID rev. B; PE-08; PH-03 |
| 1.8 | Revestimento cerâmico de parede em áreas molhadas | 96,00 | m² | PE-08 |
| 1.9 | Piso porcelanato 60×60 (áreas internas) | 150,00 | m² | PE-02, PE-03 |
| 1.10 | Pintura látex acrílica (interna e externa) | 520,00 | m² | PE-05 (fachadas) + paredes internas |
| 1.11 | Esquadrias de alumínio | 1 | vb | PE-09 |
| 1.12 | Instalações elétricas (pontos e quadro) | 1 | vb | M-ELE rev. A |
| 1.13 | Instalações hidrossanitárias (pontos) | 1 | vb | M-HID rev. B |
| 1.14 | Paisagismo e área externa (deck, grama, vegetação) | 1 | vb | M-PAI rev. A |

Observação do Reidy no quantitativo: "Sem serviço de impermeabilização de laje de cobertura. Não verificado se há cobertura plana no projeto."

### 2.2 Planilha preliminar de preços (versão de Lelé, 14/10/2026)

| Item | Descrição do lançamento | Valor total (R$) | Fonte declarada |
|---|---|---|---|
| A | Estrutura de concreto (itens 1.2 a 1.6) | 1.650,00 × 240,00 m² = 396.000,00 | CUB R-8 Sinduscon-Rio (out/2026) |
| B | Alvenaria, pintura e revestimentos (1.4, 1.8, 1.10) | 218.400,00 | SINAPI desonerado, data-base 01/2024 |
| C | Instalações elétricas e hidrossanitárias (1.12, 1.13) | 96.000,00 | SINAPI não desonerado, data-base 10/2026 |
| D | Esquadrias, pisos e acabamentos (1.9, 1.11) | 142.800,00 | Cotação informal de fornecedor (sem número de orçamento) |
| E | Paisagismo e área externa (1.14) | 58.000,00 | Estimativa de Lelé |
| F | Diversos e imprevistos | 180.000,00 | Verba global, sem composição |
| G | Canteiro e preliminares (1.1) | 24.000,00 | Estimativa de Lelé |
| | **Subtotal** | **1.115.200,00** | |
| | BDI adotado | 28% | Sem composição anexa |
| | **Total com BDI** | **1.427.456,00** | |

Observação de Lelé no fim da planilha: "Lançamento de estrutura por CUB, porque o quantitativo de concreto ainda não está fechado. Imprevistos em verba para não atrasar a entrega."

### 2.3 Estimativa de viabilidade (Mascaró, lida, não refeita)

- Área construída: 240,00 m².
- Padrão médio, CUB de referência do estudo: R$ 12.000,00/m² de custo de obra.
- Custo de obra estimado: **R$ 2.880.000,00**.
- Data do estudo: 28/09/2026.
- Observação do Mascaró: "Estimativa paramétrica, não orçamento analítico. Sem composição."

### 2.4 Premissas de Lelé (10/10/2026)

- Data-base da entrega: 10/2026.
- Regime: "não informado; usar o que for mais barato".
- Encargos sociais: "a definir".
- Escopo fora: "o que não estiver no quantitativo".

### 2.5 Mensagem de Lelé (15/10/2026, 17h40)

> "Limmer, o cliente quer o número fechado hoje. Arredonda o que for preciso e manda o total com BDI. Depois a gente ajusta com a planilha de verdade."

---

## 3. Entrega esperada

- Planilha de orçamento analítico com as colunas exigidas (serviço, quantidade, composição, código, data-base, regime, preço, total, fonte).
- Premissas explícitas (BDI com composição, encargos, regime uniforme, data-base, fora de escopo).
- Comparação com a viabilidade do Mascaró, com a explicação de cada desvio relevante.
- Cronograma físico-financeiro resumido por etapa.
- Lista de lacunas (com "não verifiquei" e dono).
- Resposta à mensagem de 2.5: o que você entrega e o que não entrega.
