---
pop: POP-LEGAL-02
titulo: Outorga Onerosa do Direito de Construir — contrapartida CAB→CAM
area: Legal — base legislativa por bairro/subzona
autor: Hely (Agente executor, equipe de Kelsen)
criado: 2026-07-20
origem: Conteúdo pesquisado e testado contra fonte oficial por Wallenberg em 16/07/2026; formalizado como POP/Skill oficial por Claudemberg na Reunião Semanal de 20/07/2026
status: oficial — aprovado por Claudemberg na Reunião Semanal de 20/07/2026
principios: 8 (Rastreabilidade), 9 (Padronização), 18 (Ética e conformidade)
---

# POP-LEGAL-02 — Outorga Onerosa do Direito de Construir (contrapartida CAB→CAM)

## 1. Objetivo e por que existe
Definir como calcular e aplicar corretamente a **contrapartida financeira** devida quando um projeto constrói **acima do Coeficiente de Aproveitamento Básico (CAB)** e **até o Coeficiente de Aproveitamento Máximo (CAM)** do lote — a Outorga Onerosa do Direito de Construir (OODC). Este POP também situa a OODC dentro do conjunto de instrumentos correlatos do Rio (Outorga de Alteração de Uso, Direito de Superfície, "Mais Valerá"), para que Hely não confunda qual instrumento se aplica a cada caso.

**Este POP não substitui julgamento jurídico caso a caso** — ver TRAVA A (seção 6). Ele padroniza a fórmula operacional, as fontes e os limites de confiança conhecidos.

## 2. Regra de ouro deste POP
**Até o CAB, constrói-se de graça. Do CAB ao CAM, paga-se contrapartida (Outorga Onerosa). Acima do CAM, não há outorga possível por este instrumento** — exige instrumento excepcional próprio (fora do escopo padrão deste POP; ver TRAVA A). No Rio, a contrapartida tem natureza de **multa compensatória** (LC 281/2025, art. 39), e **a licença só é emitida com a contrapartida quitada** (art. 20) — não é uma opção posterior ao licenciamento, é condição para ele.

## 3. Base legal (hierarquia)
1. **Estatuto da Cidade — Lei Federal 10.257/2001, arts. 28-31**: fundamento nacional do instrumento "Outorga Onerosa do Direito de Construir".
2. **LC 270/2024 (Plano Diretor/LUOS)**: define CAB e CAM por zona (Anexo XXV é a referência do Plano Diretor para a fórmula-base do cálculo da contrapartida pura CAB→CAM — ver ressalva de confiança na seção 7).
3. **LC 274/2024**: regulamenta os instrumentos — Outorga de Alteração de Uso (Fórmulas 2/3 do Anexo XXV) e Direito de Superfície em Áreas Públicas (Fórmula 1 com CAB = 1,0).
4. **LC 281/2025 ("Mais Valia/Mais Valerá")**: regula construir/legalizar **além** dos parâmetros mediante contrapartida — processo 100% digital. **Traz a fórmula operacional verbatim no art. 18** e os descontos/isenções no art. 19. É a lei mais recente e a fonte primária da fórmula operacional usada neste POP.

## 4. Fórmula operacional verbatim (LC 281/2025, art. 18 = LC 274/2024)

### Residencial multifamiliar (pelo construtor, antes do habite-se)
```
C = (1,2·Ac + 0,6·Ad + 0,6·Acpp) × VR/m² × P × TR
```

### Residencial unifamiliar/bifamiliar, ou unidade isolada (pelo particular)
```
C = (0,8·Ac + 0,4·Ad + 0,4·Acpp) × VR/m² × P × TR
```

### Comercial
Mesma estrutura, trocando `VR/m² × P × TR` por `VC/m² × T`:
```
C = (fatores de área) × VC/m² × T
```

### Legenda das variáveis
| Símbolo | Significado |
|---|---|
| C | Contrapartida (valor final a pagar) |
| Ac | Área coberta |
| Ad | Área descoberta |
| Acpp | Área coberta sobre piso permitido |
| VR/m² | Valor unitário padrão **Residencial** |
| VC/m² | Valor unitário padrão **Predial** (comercial) |
| P | Fator Posição do Imóvel |
| TR / T | Fator Tipologia |

## 5. De onde vem VR/VC — TRAVA obrigatória de fonte
**VR/VC NÃO é uma Planta Genérica de Valores (PGV) separada.** É o **Valor Unitário Padrão Predial/Residencial já usado na guia do IPTU do exercício corrente**, com fatores de correção de imóvel novo, aferido diretamente no cadastro fundiário (LC 281/2025, art. 18, incisos I e II). Isso significa:
- Não buscar tabela de PGV avulsa como se fosse fonte independente.
- O valor de referência correto vem do **cadastro fundiário do imóvel/guia de IPTU do exercício**, não de uma médiaestimada.
- Se o lote ainda não tem cadastro fundiário definitivo (ex.: terreno recém-desmembrado), sinalizar a Kelsen — é uma lacuna de dado, não decidir por estimativa.

## 6. Isenções e descontos (art. 18, IV e art. 19)
- **Isenção total**: residencial, sendo a **única propriedade do requerente no Município**, com até **80 m² totais** (art. 18, IV).
- **Desconto de 30%**: lotes nas **AP3 e AP5** (inclui Jacarepaguá, Cidade de Deus, Rio das Pedras) — art. 19, II.
- **Parcelamento**: até **60 vezes**, corrigido por **IPCA-E** — art. 19, I.
- **Desconto à vista de 30-50%**: previsto no art. 19, III/IV, mas vinculado a **janela temporal de 2025**.

## 7. AS TRAVAS (passos obrigatórios, não opcionais)
> **TRAVA A — qual instrumento se aplica a cada caso é julgamento jurídico, não decisão automática.** Existem três instrumentos distintos que podem incidir sobre um mesmo lote conforme o que o cliente pretende: (1) OODC "normal" até o CAM (este POP); (2) "Mais Valerá" (LC 281/2025) para construir/legalizar **além** dos parâmetros; (3) Outorga de Alteração de Uso (LC 274/2024, Fórmulas 2/3 do Anexo XXV) quando o pedido envolve mudança de uso, não só de área. **Hely não decide sozinho qual instrumento aplica** — este tema já está registrado como 2ª pergunta formal para o especialista externo Maurício Costa. Até resposta dele, tratar a escolha do instrumento como pendência de julgamento a sinalizar a Kelsen em todo caso concreto, não como automatismo deste POP.
>
> **TRAVA B — checar vigência dos descontos à vista antes de prometer a cliente.** Os descontos de 30-50% à vista (art. 19, III/IV) foram amarrados a uma janela temporal de 2025 e **provavelmente estão expirados em 2026** — mas isso não foi confirmado com fonte datada. **Nunca presumir que o desconto ainda vale.** Antes de comunicar qualquer percentual de desconto à vista a um cliente real, confirmar a vigência atual do art. 19, III/IV na fonte oficial (Princípio 18 — Ética e conformidade: prometer desconto expirado é risco de não conformidade e de dano à confiança do cliente).
>
> **TRAVA C — a Fórmula 1 literal do Anexo XXV da LC 270/2024 (o caso puro CAB→CAM, sem os outros instrumentos) ainda não foi extraída verbatim.** O que este POP usa (seção 4) é a fórmula **operacional das leis regulamentadoras** (LC 274/2024 e LC 281/2025, que citam e reproduzem esse mecanismo). Isso cobre a prática (é o texto que sai no Diário Oficial e é usado no processo digital), mas o texto-fonte do Anexo XXV da LC 270/2024 em si — a "Fórmula 1" no seu enunciado original do Plano Diretor — não foi conferida palavra por palavra nesta rodada. Ver seção 8 (confiança) e seção 9 (lacunas).

## 8. Exemplo ilustrativo do mecanismo de cálculo (esquemático — não é caso real)
> Este exemplo serve só para ilustrar como as variáveis se combinam. **Não usar estes números em caso real** — os valores de VR/P/TR devem vir do cadastro fundiário/guia de IPTU do lote específico (seção 5).

Residência unifamiliar, particular, com Ac = 200 m², Ad = 50 m², Acpp = 0 m²:
```
C = (0,8 × 200 + 0,4 × 50 + 0,4 × 0) × VR/m² × P × TR
C = (160 + 20) × VR/m² × P × TR
C = 180 × VR/m² × P × TR
```
Se o lote estiver em AP3 ou AP5, aplicar o desconto de 30% (art. 19, II) sobre o C calculado, antes de gerar a guia. Se o requerente comprovar única propriedade e o total (Ac+Ad+Acpp equivalente) for ≤ 80 m², C = 0 (isenção, art. 18, IV) — mas isso é exceção, não a regra geral do exemplo acima.

## 9. Confiança
**Média-alta.** A fórmula operacional (seção 4) e os descontos/isenções (seção 6) são **texto verbatim do Diário Oficial** (LC 281/2025, arts. 18-20 e 39) — confiança alta para esse trecho. O que reduz a confiança geral para "média-alta" (não "alta"):
- A Fórmula 1 literal do Anexo XXV da LC 270/2024 (o enunciado original do Plano Diretor para o caso puro) ainda não foi extraída/conferida verbatim (TRAVA C).
- A vigência atual dos descontos à vista do art. 19, III/IV não foi confirmada (TRAVA B).
- A escolha de instrumento em caso concreto é julgamento jurídico pendente de resposta do Maurício Costa (TRAVA A).

## 10. Lacunas conhecidas (sinalizadas a Kelsen)
- **Anexo XXV da LC 270/2024, Fórmula 1 literal**: ainda não extraída verbatim como texto do próprio Anexo — usar a fórmula operacional das leis regulamentadoras (seção 4) como a versão prática confiável, mas registrar que o texto-fonte do Plano Diretor em si não foi conferido palavra por palavra.
- **Vigência dos descontos à vista (art. 19, III/IV)**: janela temporal de 2025, status atual em 2026 não confirmado — TRAVA B obrigatória antes de qualquer promessa a cliente.
- **Critério de escolha de instrumento (OODC x "Mais Valerá" x Outorga de Alteração de Uso)**: pauta formal pendente com o especialista externo Maurício Costa — não decidir sozinho enquanto não houver resposta (TRAVA A).
- **Relação com o campo `ics` do RIU (POP-LEGAL-RIU-01)**: a Outorga Onerosa (este POP) e o Índice de Comércio e Serviços — ICS (ver POP-LEGAL-04) são mecanismos **distintos** — um é contrapartida financeira por construir acima do CAB, o outro é parâmetro de zoneamento que limita área de comércio/serviço no lote. Não confundir os dois ao orientar um cliente (ver POP-LEGAL-04, seção 4, para a distinção explícita).
