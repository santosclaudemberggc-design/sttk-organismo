---
name: legal-art-crea-responsabilidade-tecnica-rj
description: "ART (Anotação de Responsabilidade Técnica) do CREA-RJ para profissionais de engenharia terceirizados que assinam parte do Projeto Legal ou Estrutural da Sttickler — sistema 2026 georreferenciado e antifraude, valor calculado pelo custo de obra (Sinduscon-Rio). Use sempre que Hely (ou Kelsen) precisar orientar/verificar a ART de um engenheiro terceirizado (ex.: calculista estrutural, engenheiro de fundação), estimar o valor de referência de uma ART de execução ou de regularização de obra, ou explicar por que o profissional que assina precisa estar de fato vinculado ao endereço da obra. NÃO cobre RRT do CAU/RJ (ver nota de escopo abaixo) nem os parâmetros urbanísticos do lote (isso é `legal-base-legislativa-bairro`)."
---

# ART do CREA-RJ — sistema georreferenciado 2026

Skill da área Legal do Sistema Orgânico STTK. Quem consome na prática: **Hely** (Agente executor). Quem retém e decide quando aplicar: **Kelsen** (Gestor Legal).

## Para quem é isto, de fato

A Sttickler assina a maior parte do escopo residencial com **RRT do CAU** (Claudemberg, ou o arquiteto parceiro externo — ver regra de PRPA no `CLAUDE_gestor_slice.md`). **Esta Skill não é sobre isso.** Ela existe para a fatia do trabalho que ainda depende de um **profissional CREA** — tipicamente um engenheiro terceirizado (calculista estrutural, engenheiro de fundação, engenheiro civil de obra), quando o escopo do projeto exige uma Anotação de Responsabilidade Técnica em vez de, ou além de, o RRT do arquiteto.

**Se o caso é 100% RRT/CAU, esta Skill não se aplica** — não force o enquadramento.

## O que mudou — Ato Normativo CREA-RJ nº 001/2025 (2026)

Dois pontos confirmados pelo próprio CREA-RJ, publicados em 15/01/2026:

1. **Valor da ART calculado pelo custo da obra.** O valor da ART de execução de obra passa a ser calculado com base no **custo mínimo de construção por m² publicado pelo Sinduscon-Rio** — a mesma referência usada para CUB em orçamento. A mesma regra vale para ART de **regularização/legalização** de obra iniciada ou concluída sem profissional habilitado (relevante em casos de regularização, ex.: ampliação + legalização).
2. **Sistema georreferenciado e antifraude.** O CREA-RJ está implantando ART parametrizada e georreferenciada, integrada a banco de dados — exige comprovação de onde o serviço é executado, e o sistema alerta o Conselho se o mesmo CPF emitir várias ARTs no mesmo dia em locais distantes ("canetinha"). Não muda o processo do Hely, mas é contexto relevante: **o profissional que assina precisa de fato estar vinculado ao endereço da obra** — isso passou a ser auditado automaticamente, não é mais só boa prática.

## O que fazer, na prática

Ao lidar com ART de engenheiro terceirizado (não CAU do Claudemberg) num caso real:

1. **Valor de referência:** vem do custo/m² do Sinduscon-Rio vigente na data da ART, não de tabela fixa antiga. Confirme a tabela atual do Sinduscon-Rio antes de orçar — ela é publicada periodicamente e desatualiza rápido, no mesmo padrão de qualquer índice de custo de construção.
2. **Vínculo geográfico:** confirme que o profissional que assina de fato atuou/vai atuar no endereço da obra — o sistema audita isso, e uma ART emitida "de longe" pode ser sinalizada.
3. **Regularização:** se o caso envolver obra iniciada/concluída sem profissional habilitado, a mesma regra de cálculo por custo se aplica à ART de regularização.

## Confiabilidade da fonte — grau médio, não confirmado em primário

**Diferente da Skill de base legislativa (`legal-base-legislativa-bairro`), o conteúdo aqui NÃO foi confirmado por leitura direta do texto primário.** A tentativa de `WebFetch` direto no PDF do Ato Normativo 001/2025 retornou HTTP 403; o conteúdo desta Skill vem de uma página do próprio domínio `crea-rj.org.br` (`/mudanca-na-art/`), que é fonte oficial mas de segundo grau (resumo do Conselho sobre o próprio Ato Normativo, não o Ato Normativo lido linha a linha).

**Antes de aplicar isto a um caso real com ART de terceiro em jogo, Hely deve tentar de novo o acesso ao PDF primário** (`crea-rj.org.br/wp-content/uploads/2026/01/0001-2026-Ato-Normativo.pdf`) — por outro método se o WebFetch continuar bloqueando (o mesmo padrão de bloqueio já resolvido para outras fontes: baixar via `curl` com user-agent, ou pedir confirmação humana via Chrome). Enquanto isso não acontecer, trate valor e regra como **indicativo**, não como número final para cobrar de cliente ou repassar a engenheiro terceirizado.

## Nota de escopo — RRT do CAU/RJ NÃO está aqui, e por quê

Existe uma proposta de Skill separada sobre a **Deliberação Plenária CAU/RJ nº 009/2026**, que sugere alterar o Art. 8º da Resolução CAU/BR 91/2014 (RRT). **Essa proposta não virou Skill formal** — decisão de Kelsen em 03/09/2026, mantida deliberadamente fora daqui:

- É **sugestão do CAU/RJ ao CAU/BR**, não texto vigente — o CAU/RJ só propõe, quem altera a Resolução 91 é o CAU/BR, e isso não aconteceu até hoje.
- **A proposta colide com a numeração já vigente do próprio Art. 8º**: o artigo já tem §5º (RRT Social) e vai até §8º; RRT Derivado já é matéria do inciso IV + §4º (Res. CAU/BR 184/2019). A sugestão da CEP-RJ tenta inserir um §5º novo onde já existe um — achado confirmado por Kelsen/Hely em 31/08/2026, registrado em `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/_indice_fontes.md`, seção "REGISTRO — 31/08/2026 — DOMÍNIO CAU/RRT".
- Fica como **monitoramento apenas**, não como base ativa — mesmo tendo sido incluída na ratificação em bloco de 03/09/2026 junto com as demais 4 propostas desta rodada. Kelsen não formaliza como Skill um texto que colide com a norma vigente que ele mesmo já conferiu; recomendação registrada de volta à Diária de Skills antes de qualquer nova tentativa de ratificação (`pendencias.json`, item `skill-caurj-rrt-009-2026-lacuna-numeracao`).
- Gatilho de recheck: qualquer Resolução nova do CAU/BR alterando o Art. 8º da Resolução 91/2014, ou providência formal do CAU/BR sobre a DP CAU/RJ 009/2026.

## Escopo, crescimento e manutenção

Cobertura atual: ART de execução/regularização de obra por engenheiro CREA terceirizado, contexto Rio de Janeiro. Cresce por demanda — não expandir para outros tipos de ART (ex.: projeto, direção técnica) sem caso real que justifique (Princípio 19).

Lacuna que você encontrar **não vira conhecimento oficial por decisão sua**. Reporte a Kelsen; ele avalia e leva a Wallenberg, que formaliza (Função 5).

## Fontes

- [Mudança na ART — CREA-RJ](https://www.crea-rj.org.br/mudanca-na-art/) (domínio oficial, mas fonte de segundo grau — ver "Confiabilidade da fonte" acima)
- [Ato Normativo 001/2025 (PDF)](https://www.crea-rj.org.br/wp-content/uploads/2026/01/0001-2026-Ato-Normativo.pdf) — citado pela fonte acima, **ainda não acessado diretamente** (HTTP 403 no WebFetch)
- Pesquisado em 19/07/2026 (rotina diária de Wallenberg); Skill integrada em 03/09/2026 (ratificação em bloco por Claudemberg)
