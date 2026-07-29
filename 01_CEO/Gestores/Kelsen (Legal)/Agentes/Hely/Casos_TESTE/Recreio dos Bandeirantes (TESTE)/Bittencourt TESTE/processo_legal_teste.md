---
status: TESTE — não é cliente real
caso: 2
data_teste: 2026-07-13
gestor: Kelsen
executor: Hely (primeiro caso rodado já na arquitetura Kelsen→Hely)
---

# ⚠️ CENÁRIO DE TESTE — NENHUM DADO AQUI É REAL

Todo conteúdo deste arquivo — requerente, imóvel, matrícula, CPF, respostas da prefeitura — é fictício, gerado pelo Pesquisador de Testes (`D:\010_PESQUISADOR DE TESTES`) para validar o Gestor Legal (Kelsen) e sua equipe (Hely). **Nunca copiar para `000_CLIENTES` real, nem tratar como caso verdadeiro.**

Cenário-fonte: `D:\010_PESQUISADOR DE TESTES\Cenarios de Teste\Kelsen (Legal)\2026-07-13_Projeto-Legal-TESTE-Athos-Bulcao.md`

## Requerente e imóvel (fictícios)
- **Requerente**: Eduardo Trávassos Bittencourt (divorciado)
- **Imóvel**: Rua Athos Bulcão, nº 88 (fictício), Recreio dos Bandeirantes, RJ — CEP 22790-661 (rua/CEP reais, CL 346478; número/lote/matrícula fictícios)
- **Matrícula RGI**: 000.001-TESTE | **Área do terreno**: 360,00 m² (12,00 x 30,00 m)
- **Situação**: casa unifamiliar térrea existente (15 anos), Alvará original nº 00000-TESTE/2011 cobrindo 180,00 m² averbados. Edícula/varanda gourmet de 25,00 m² construída há ~3 anos, SEM averbação (irregular).
- **Natureza da obra**: MODIFICAÇÃO — ampliação (novo 2º pavimento, 95,00 m²) + regularização (edícula irregular, 25,00 m²)

## Projeto arquitetônico de origem
Autor: **Agente interno da própria estrutura Sttickler** (Equipe de Arquitetura do organismo, fictício) — ao contrário do Caso 1. Apoio pontual: Eng. Paulo Renato Fagundes (calculista estrutural externo), CREA RJ-000000-TESTE — dimensionamento da laje do novo pavimento.

## Legislação aplicável — achado do teste (pesquisa secundária) x fonte oficial (correção)

**Pesquisa do Hely (fonte secundária, na hora do teste):** encontrou referência ao Decreto Rio nº 3.046/1981, subzona A-20 — lote mínimo 600 m², gabarito 2 pavimentos, IAA 1,25, taxa de ocupação 50%, afastamento frontal 5 m, afastamento de divisas 2,50 m. Confiança baixa/média, sem acesso à fonte oficial na hora.

**Confirmação com fonte oficial (Relatório de Informações Urbanísticas da SMDU, `mapas.rio.rj.gov.br`, consultado por Claudemberg em 13/07/2026 — mesmo dia):** a Rua Athos Bulcão **NÃO** está no Decreto 3.046/1981 — está na **mesma zona do Caso 1 (Rua Claude Monet)**: **ZRM3 D da AP 4**, base legal **Lei Complementar 270/2024**. A pesquisa secundária errou a base legal nos **dois** casos-teste do dia, não só no primeiro — reforça ainda mais a regra "fonte oficial sempre vence fonte secundária" que já tinha virado proposta de Skill.

**Parâmetros reais confirmados (LC 270/2024, ZRM3 D da AP4):**
- Lote mínimo: 600 m² | Testada mínima: 12 m
- CA básico: 0,8 | CA máximo: 1,0
- Taxa de ocupação máxima: 50%
- Afastamento frontal mínimo: 5 m
- **Gabarito: 4pav/14m se NÃO afastado das divisas, ou 6pav/20m se afastado das divisas** — não existe um "recuo lateral mínimo fixo" isolado como a fonte secundária indicou; o mecanismo real é um trade-off entre afastamento lateral e gabarito permitido.
- Existe ainda a Operação Urbana Consorciada do Legado Olímpico (Setor III-H, LC 284/2025), que pode elevar CAM a 3 / TO a 30% / gabarito a 12pav-36m, mas condicionada a regras próprias — não confirmado se este lote está na área receptora.

**Confronto com os parâmetros propostos, já corrigido (2ª correção, 13/07/2026 — após leitura integral da LC 270/2024 e do COES):**

| Parâmetro | Proposto | Limite real | Situação |
|---|---|---|---|
| Recuo lateral | 0,90 m | LC 270/2024 Art. 364 delega ao **COES** (LC 198/2019). Piso de 2,50 m é **incondicional** (Art. 4º, II); para **unifamiliar** o número é **1,50 m** (Art. 31, p.ú.). Ficar abaixo não é infração — **enquadra** como "não afastada das divisas" (Art. 4º, §1º, II), ao custo do gabarito menor (4pav/14m) | **Conforme quanto à fachada** — mas item **NÃO ENCERRADO**: ver não conformidades condicionais 3.1 a 3.5 |
| Gabarito | 9,20 m (2 pavimentos após ampliação) | 14 m se não afastado das divisas / 20 m se afastado | **Dentro do limite** do regime "não afastado" com folga (9,20 m vs. 14 m) |
| Terreno | 360 m² | 600 m² (lote mínimo) | Abaixo do mínimo — plausível por ser lote pré-existente (Alvará 2011), não impede modificação por si só |

**Análise final do recuo lateral — FUNDAMENTO CORRIGIDO em 20/07/2026 (4ª rodada; autorização de Wallenberg, execução de Kelsen).**

> ⚠️ A redação anterior desta análise ("o COES Art. 4º só exige o mínimo de 2,50 m **se** o projeto optar pelo regime afastado das divisas; no regime não afastado não há mínimo") **fica revogada por não corresponder ao texto do COES.** Ela acertou o destino pelo caminho errado, e o caminho errado é o que se reaproveita em outros casos. Origem do vício: `Fontes_Legislacao/_indice_fontes.md`, corrigido no mesmo dia.

**Conclusão mantida quanto à fachada, por outro fundamento:**
- O piso de **2,50 m** do **Art. 4º, II** é **incondicional** — não depende de escolha de regime. A condicional do texto ("quando utilizados para ventilar ou iluminar") acrescenta o critério de 1/5 da altura, não dispensa o piso.
- Esta é uma **casa unifamiliar**, então o número aplicável não é 2,50 m e sim **1,50 m**, por força do **Art. 31, parágrafo único** — artigo que as três rodadas anteriores nunca consultaram.
- O fundamento correto é o **Art. 4º, §1º, II**: ficar abaixo do afastamento mínimo **não configura infração**, e sim **enquadra a edificação como "não afastada das divisas"** — categoria legal cujo preço é o teto de gabarito menor do Anexo XXI (ZRM3 D/AP4: 4pav/14m). Com 9,20 m pretendidos, o projeto cabe nesse teto com folga.
- **Por esse fundamento — e só por ele — os 0,90 m não são, isoladamente, não conformidade.**

**O item NÃO está encerrado.** O enquadramento como "não afastado" não libera a divisa para todos os elementos da edificação. Ver não conformidades condicionais **3.1 a 3.5** na seção de pendências.

Fontes primárias: `...\Fontes_Legislacao\LC270_2024_PlanoDiretorLUOS.pdf` e `COES_LeiComplementar198_2019.pdf` — conferidas em texto literal, não por resumo interno.

## Anexo I — DULI (rascunho de teste)
- Tipo de licença: Modificação (ampliação + regularização)
- Requerente: Eduardo Trávassos Bittencourt (CPF/RG fictícios)
- Imóvel: Rua Athos Bulcão, 88, Recreio dos Bandeirantes — Matrícula 000.001-TESTE
- PRPA: **A confirmar formalmente com Claudemberg** — projeto arquitetônico produzido por Agente interno, logo a regra aponta para Claudemberg (CAU, 2026), diferente do Caso 1
- Documentos anexados: Ficha de Levantamento (c/ fotos da edícula irregular), Estudo Preliminar, Anteprojeto (AP-TESTE-2026-010 a 015), Certidão de matrícula RGI, Alvará original nº 00000-TESTE/2011, Certidão negativa de IPTU, RG/CPF

## Anexo II — Declaração de Responsabilidade
Pendente a ART do Eng. Paulo Renato Fagundes (cálculo estrutural da nova laje) — **bloqueio documental independente da questão do PRPA**, não confundir uma pendência com a outra.

## Anexo IV — Quadro Explicativo de Áreas (modificação)

| Parcela | Descrição | Área (m²) | Situação | Referência |
|---|---|---|---|---|
| I | Área existente averbada | 180,00 | Regular | Alvará nº 00000-TESTE/2011 |
| II | Área objeto de regularização | 25,00 | A regularizar | Ficha de Levantamento + registro fotográfico |
| III | Área de ampliação nova | 95,00 | Nova construção (2º pavimento) | Anteprojeto AP-TESTE-2026-010 a 015 |
| **Total pretendido** | | **300,00** | | |

**Resposta simulada da SMDU** (processo LICIN-TESTE-2026-0000456): PEDIDO DE AJUSTE — quadro apresentado de forma consolidada (300,00 m²), sem o detalhamento exigido para regularização combinada com ampliação. Anexo IV acima já é a versão discriminada (revisada), que resolveu o pedido de ajuste na simulação.

## Emissão (simulada, 2ª submissão aprovada — formato do Anexo IV resolvido; PRPA e ART do calculista seguem como pendências documentais separadas)

> ⚠️ **Ressalva de 20/07/2026:** esta emissão simulada foi produzida em 13/07/2026 sob o fundamento do recuo lateral que hoje se sabe errado, e **antes** de existirem as condicionais 3.1–3.5 e o item 6 (TO/ATE). **A simulação de aprovação não vale como validação de conformidade do caso** — se este fosse cliente real, o pacote não subiria para o Maurício sem antes fechar as condicionais. Registrado como aprendizado de processo: aprovação simulada com fundamento viciado não é aprovação.
- Minuta da Licença — modificação (ampliação + regularização)
- Guia de arrecadação
- Anexo IV revisado (3 parcelas discriminadas, tabela acima)
- Termo de Responsabilidade

## Fluxo pós-aprovação
Não passa por Compatibilização — segue direto pra fila de espera do **Gate 16 (Liberação de Obra)**.

## Fechamento de obra
Por ser modificação de edificação existente (não unidade nova): **Aceitação de Obras** — não Habite-se.

## Pendências e sinalizações (registradas no teste — 3 distintas, não confundir)
1. **PRPA**: a confirmar formalmente — aponta para Claudemberg (CAU, 2026), por o projeto arquitetônico ser de Agente interno da Sttickler.
2. **ART do Eng. Paulo Renato Fagundes** (calculista estrutural) — ainda não emitida, bloqueio documental independente do item 1.
3. **Recuo lateral (0,90 m proposto) — REABERTO em 20/07/2026. Conclusão mantida quanto à fachada, FUNDAMENTO CORRIGIDO, e item NÃO encerrado.**
   A marcação anterior ("RESOLVIDO em 13/07/2026") fica revogada. Ela repousava sobre leitura errada do COES Art. 4º (ver análise corrigida acima): o piso de 2,50 m é **incondicional**, não atrelado a regime de gabarito; e para **unifamiliar** o número aplicável é **1,50 m** (Art. 31, p.ú.), artigo nunca consultado nas três rodadas anteriores. O fundamento correto é o **Art. 4º, §1º, II** — ficar abaixo do mínimo **enquadra** a edificação como "não afastada das divisas", categoria legal cujo preço é o gabarito menor (4pav/14m), que os 9,20 m respeitam. Por esse fundamento, os 0,90 m não são, isoladamente, não conformidade.
   **Restam as não conformidades condicionais abaixo, que nenhuma rodada anterior levantou.**

   - **3.1 — Varanda/sacada a menos de 1,50 m da divisa (COES Art. 8º, §3º) — CONDICIONAL, potencialmente IMPEDITIVA.** Literal: *"Para edificações não afastadas das divisas, as varandas e sacadas deverão guardar uma distância lateral mínima de um metro e cinquenta centímetros das divisas laterais e de fundos do lote."* O regime "não afastado" **não** dispensa esta distância. A **edícula/varanda gourmet de 25 m²** — justamente o objeto da regularização — é o elemento em risco. **Pendência:** posição exata do elemento em relação a cada divisa. Se estiver a menos de 1,50 m, nenhum regime resolve: só recuo físico do elemento.
   - **3.2 — Marquise a menos de 1,50 m da divisa (COES Art. 9º, IV) — CONDICIONAL.** Literal: *"as marquises situadas sobre os afastamentos laterais e de fundos deverão guardar distância mínima de um metro e cinquenta centímetros das divisas do lote."* **Pendência:** existe marquise, beiral projetado ou cobertura de acesso sobre a faixa de 0,90 m? Nunca levantado.
   - **3.3 — Iluminação/ventilação por faixa que não é espaço externo (COES Art. 17, §1º c/c §3º) — CONDICIONAL, potencialmente IMPEDITIVA.** A faixa de 0,90 m não é afastamento (abaixo de 1,50 m) nem prisma (Art. 5º, §1º, II: nenhum lado *"menor que um metro"*; PVI exige 3 m). Logo não é o *"espaço externo"* do Art. 17, §1º, e o §3º exige que *"os compartimentos de permanência prolongada deverão sempre possuir ventilação e iluminação natural"*. **Pendência:** há abertura nessa fachada? De que compartimento? Se for de permanência prolongada, a reprovação **não é automática** — depende de outra abertura qualificante que sozinha atenda 1/8 da área (Art. 18). Faltam área do compartimento e áreas de vão.
   - **3.4 — Afastamento frontal (5 m na ZRM3 D/AP4) — NÃO VERIFICADO.** O caso nunca registrou o afastamento frontal proposto.
   - **3.5 — Afastamento da edícula em relação à edificação principal (COES Art. 26) — CONDICIONAL.** Literal: *"Será permitida a construção [...] de edículas, com até dois pavimentos, destinadas a compartimentos de apoio às partes comuns da edificação, devendo atender aos afastamentos em relação à edificação, e observar o afastamento frontal exigido para o local."* Para unifamiliar, 1,50 m (Art. 31, p.ú.). **Pendência:** distância entre a edícula e a casa.

6. **TO e ATE nunca foram calculados — risco real de estouro de Taxa de Ocupação (levantado em 20/07/2026).** O caso tem quadro de **áreas** (Anexo IV) mas **nenhum quadro de índices**. Com os números do próprio caso: terreno 360 m², TO máxima 50% (LC 270/2024 Art. 349) = 180 m² de projeção. Projeção aparente = 180 (casa) + 25 (edícula térrea) = **205 m² → TO 56,94%**, excedendo em exatamente os 25 m² que se pretende regularizar. ATE pretendida 300 m² contra CAB 0,8 (288 m²) e CAM 1,0 (360 m²) — acima do CAB, o que **aciona outorga onerosa**.
   **A condicional é séria e não sei resolvê-la:** o Art. 350, IV exclui da projeção as *"edículas, guaritas e pórticos, nos termos do Código de Obras"*, e o Art. 347, V faz o mesmo para a ATE — mas o COES Art. 26 define edícula como destinada a *"compartimentos de apoio às **partes comuns** da edificação"*, redação voltada a edifício, não a casa unifamiliar. O caso chama o elemento de duas coisas ao mesmo tempo ("edícula/varanda gourmet").
   - Se **qualificar** como edícula: TO e ATE conformes.
   - Se **não qualificar**: TO de 56,94% é não conformidade direta, e a ATE passa do CAB.
   **Julgamento de enquadramento não fechado — não é lacuna geométrica, é interpretação, e exige Claudemberg.** Se for por outorga, registrar a LC 270/2024 **Art. 108**: *"No caso de modificação de edificação preexistente, a outorga onerosa incidirá apenas sobre a área construída que ultrapasse aquela da edificação preexistente."*
4. **Lacuna de conhecimento**: possível ambiguidade no critério de escolha entre Anexo III e Anexo IV (construção nova/modificação vs. uni-bifamiliar/demais tipos) — não confirmado com fonte oficial, fica como pendência de verificação futura.
5. **Correções de fonte legislativa (13/07/2026, mesmo dia, em 2 etapas):** (a) a pesquisa secundária do Hely indicou Decreto 3.046/1981 para este lote — a fonte oficial (RIU/SMDU) confirmou que é LC 270/2024, ZRM3 D da AP4, a mesma lei/zona do Caso 1 (Rua Claude Monet); (b) a leitura integral da LC 270/2024 + COES resolveu de vez a dúvida do recuo lateral (item 3 acima), que nas 2 rodadas anteriores ainda ficava em aberto. Reforça a regra "fonte oficial completa sempre vence fonte secundária ou parcial".
