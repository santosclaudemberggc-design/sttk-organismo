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
| Recuo lateral | 0,90 m | LC 270/2024 Art. 364 delega ao **COES** (Lei Complementar 198/2019): mínimo de 2,50m só é exigido no regime "afastado das divisas" (gabarito 6pav/20m); no regime "não afastado" (4pav/14m) não há mínimo | **Provavelmente conforme** — ver análise abaixo |
| Gabarito | 9,20 m (2 pavimentos após ampliação) | 14 m se não afastado das divisas / 20 m se afastado | **Dentro do limite** do regime "não afastado" com folga (9,20 m vs. 14 m) |
| Terreno | 360 m² | 600 m² (lote mínimo) | Abaixo do mínimo — plausível por ser lote pré-existente (Alvará 2011), não impede modificação por si só |

**Análise final do recuo lateral (resolvida em 13/07/2026, com fonte oficial completa):** o gabarito final pretendido (9,20 m) fica bem dentro do envelope do regime "não afastado das divisas" (limite 14 m) — e o COES (Art. 4º) só exige o mínimo de 2,50 m de afastamento lateral/fundos **se** o projeto optar pelo regime "afastado das divisas" (pra ganhar gabarito maior, 6pav/20m). Como este projeto não precisa desse gabarito maior, ele pode se enquadrar como "não afastado das divisas" — e nesse regime, o recuo lateral de 0,90 m **não é uma não conformidade**. Isso corrige as 2 rodadas anteriores desta análise (a 1ª citou a lei errada — Decreto 3.046/81 —, a 2ª ainda tratava o recuo como pendência sem conseguir confirmar o mecanismo exato). Fontes primárias completas: `01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\LC270_2024_PlanoDiretorLUOS.pdf` e `COES_LeiComplementar198_2019.pdf`.

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

## Emissão (simulada, 2ª submissão aprovada — formato do Anexo IV e mérito do recuo lateral resolvidos; PRPA e ART do calculista seguem como pendências documentais separadas)
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
3. **Recuo lateral (0,90 m proposto) — RESOLVIDO em 13/07/2026, com fonte oficial completa (LC 270/2024 + COES).** O afastamento lateral/fundos não vem da LC 270/2024 (Art. 364 remete ao COES). Pelo COES (Art. 4º), o mínimo de 2,50m só é exigido se o projeto optar pelo regime "afastado das divisas" (gabarito 6pav/20m); no regime "não afastado" (4pav/14m, onde este projeto se encaixa com folga — gabarito final 9,20m), não há mínimo de afastamento lateral. **Não é mais tratado como pendência de mérito em aberto.**
4. **Lacuna de conhecimento**: possível ambiguidade no critério de escolha entre Anexo III e Anexo IV (construção nova/modificação vs. uni-bifamiliar/demais tipos) — não confirmado com fonte oficial, fica como pendência de verificação futura.
5. **Correções de fonte legislativa (13/07/2026, mesmo dia, em 2 etapas):** (a) a pesquisa secundária do Hely indicou Decreto 3.046/1981 para este lote — a fonte oficial (RIU/SMDU) confirmou que é LC 270/2024, ZRM3 D da AP4, a mesma lei/zona do Caso 1 (Rua Claude Monet); (b) a leitura integral da LC 270/2024 + COES resolveu de vez a dúvida do recuo lateral (item 3 acima), que nas 2 rodadas anteriores ainda ficava em aberto. Reforça a regra "fonte oficial completa sempre vence fonte secundária ou parcial".
