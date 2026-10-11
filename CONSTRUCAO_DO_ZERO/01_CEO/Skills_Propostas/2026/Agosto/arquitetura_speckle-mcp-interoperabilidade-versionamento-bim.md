---
name: arquitetura-speckle-mcp-interoperabilidade-versionamento-bim
description: "Conector MCP comunitário (bimgeek/speckle-mcp, 14 estrelas) para o Speckle — hub open-source de dados AEC (US$19,2M captados, Series A) que versiona e sincroniza modelos entre Revit/Rhino/Grasshopper/outras ferramentas na nuvem; ângulo novo — interoperabilidade/coordenação entre ferramentas diferentes, distinto do Vitruvius (manipulação direta de um único modelo Revit) e de tudo já mapeado no mês."
metadata:
  type: skill_proposta
  gestor_alvo: "Lúcio (Arquitetura) — equipe de Oscar, cenário de coordenação com arquiteto parceiro externo que usa ferramenta BIM diferente do organismo (Rhino/Grasshopper em vez de Revit) ou que precise de histórico versionado do modelo entre etapas"
  data: 2026-08-12
  fonte_principal: "github.com/bimgeek/speckle-mcp, pulsemcp.com/servers/bimgeek-speckle, speckle.systems (site oficial + blog de funding)"
  status: proposta_arquivada
---

# Speckle MCP — interoperabilidade e versionamento de dados BIM entre ferramentas

## Para quem serve
Equipe do Gestor Lúcio (Arquitetura) — em especial **Oscar**, no cenário em que o arquiteto parceiro externo usa uma ferramenta BIM diferente do Revit (Rhino, Grasshopper, SketchUp, ArchiCAD — Speckle conecta todas), ou quando é preciso manter histórico versionado do modelo entre etapas (Levantamento -> Briefing -> Estudo Preliminar -> Anteprojeto) sem depender de troca manual de arquivo. Ângulo **novo** dentro da busca contínua deste mês: nenhuma das 7 Skills anteriores de Agosto cobria **interoperabilidade entre ferramentas BIM diferentes** — todas miravam render/vídeo (saída visual), entrada 2D->BIM, documentação executiva, design generativo ou QA/QC dentro de um único modelo.

## O que é — verificado em fontes que não se citam entre si
**Speckle** é uma empresa/plataforma real de infraestrutura de dados 3D para AEC, com **licença Apache 2.0** (open-source de fato, não freemium disfarçado) — confirmado no próprio site oficial (speckle.systems) e no blog de anúncio de captação. Levantou **US$19,2 milhões em 3 rodadas**, incluindo uma Series A de **US$12,5 milhões liderada pela Addition** (23/10/2024) — sinal de tração real, não projeto de garagem. A própria plataforma reporta (site oficial, 2026) mais de **146 mil projetos** e **11,8 mil organizações** usando o serviço.

- **Mecanismo:** Speckle funciona como hub central na nuvem — conectores desktop (para Revit, Rhino, Grasshopper e outras ferramentas) publicam e carregam geometria e parâmetros como "streams" versionados. Duas equipes usando softwares diferentes podem trocar o mesmo modelo sem exportar/importar arquivo manualmente, com histórico de cada versão preservado.
- **O conector MCP** (`bimgeek/speckle-mcp`, autor Mucahit Bilal Goker) é projeto **comunitário**, não oficial da Speckle — expõe via protocolo MCP: listar e buscar projetos por nome/descrição, recuperar detalhes e versões de modelo, consultar objetos e propriedades dentro de uma versão específica. Permite que um Agente (Oscar) pergunte em linguagem natural sobre o estado do modelo compartilhado sem abrir o Revit.
- **Checagem de idoneidade (só leitura, sem clonar/instalar/executar nada nesta rotina):** repositório com **14 estrelas, 8 forks, 17 commits**; README coerente e específico (pré-requisitos, instalação via `uv`, variáveis de ambiente, lista de tools, seção de troubleshooting); nome não é typosquatting de projeto famoso; nenhum pedido de rodar script fora do fluxo padrão de instalação de MCP. Sinal de projeto pequeno mas genuíno, não abandonado nem suspeito — não confundir a maturidade do **conector** (comunitário, modesto) com a maturidade da **plataforma** Speckle (empresa financiada, adoção real).

## O que NÃO foi confirmado (limite do achado, Princípio 3)
- **Exige conta/API key da Speckle** para funcionar (mencionado no README, não testado nesta rotina) — não é acesso gratuito e anônimo; o organismo não tem hoje uma conta Speckle configurada.
- **Conector é comunitário, de autor único, sem grande adoção** (14 estrelas é ordem de grandeza bem menor que o Blender MCP de 01/08, 25,2k estrelas) — registrado como achado real, não como solução madura pronta para produção.
- **Não substitui o Vitruvius.** São ferramentas complementares, não concorrentes: Vitruvius manipula diretamente um modelo Revit local (criar parede, cotar ambiente); Speckle sincroniza/versiona dados **entre** modelos/ferramentas diferentes. Só faz sentido se e quando houver necessidade real de trocar dados com um parceiro que não usa Revit — hoje não há caso confirmado disso no fluxo do Lúcio.
- **Nenhuma fonte confirma uso por escritório brasileiro** nem integração testada com o fluxo LICIN 2.0/RIU.

## Por que é achado relevante para o organismo
Hoje a coordenação com o arquiteto parceiro externo depende de troca de arquivo Revit e comunicação informal (mesmo padrão que já gerou desvio de cadeia nos Exames 1 e 2 de Oscar/Burle/Portinari em agosto). Se o parceiro um dia usar outra ferramenta BIM, ou se for necessário auditar o histórico de mudanças de um modelo entre etapas, o Speckle é a plataforma de mercado que resolve isso de forma nomeada e verificável — registrado como proposta para esse cenário futuro, mesmo tratamento dado às Skills anteriores sem uso confirmado no fluxo real de hoje.

## Continuidade da busca desta rodada (12/08/2026)
- **Render/vídeo/tour 360 (D5, foco principal por instrução de 11/08):** sem achado novo — fórum oficial do D5 Render segue com pedido aberto de console/API Python sem resposta da fabricante (mesmo estado de 11/08); nenhuma integração MCP encontrada.
- **CAU/RJ:** nenhuma resolução nova datada de agosto/2026 — resultados trouxeram só concurso público CAU/RJ 2026 e anuidade 2026 (sem relação com RRT/ART/exercício profissional).
- **LICIN 2.0/SMDU:** nenhum decreto/LC novo além do já conhecido Decreto 55.622/2025.
- **Outros MCPs de BIM/IFC no GitHub, avaliados e não transformados em Skill:** `openbim-mcp`, `ifc-mcp` (flinker-app), `ifcx-mcp` (louistrue), `IFC-MCP` (ekkodale), `smartaec-ifc-bim` (33 estrelas) — todos leem/consultam arquivos IFC estáticos (útil para auditoria pontual de um arquivo exportado), mas nenhum tem a mesma tração de mercado nem a mesma proposta de interoperabilidade **entre ferramentas em tempo real** que o Speckle tem — descartados por redundância de categoria frente ao achado principal do dia, não por falha de verificação.
- **Sustentabilidade/energia (cove.tool, IES VE) — não reaberto:** já registrado e descartado em 10/08 por falta de Gestor Complementares implantado; sem novidade que mude essa análise.
- **Orçamento Brasil:** confirmado que Togal.AI segue sendo a única ferramenta internacional nomeada com presença no mercado brasileiro (~US$99/mês); nenhuma ferramenta nacional nova com nome verificável além do já conhecido OrçaFascio (agregador de base de preços, não IA de takeoff) — sem achado novo, item já coberto/revertido em 10/08.

## Fontes
- https://github.com/bimgeek/speckle-mcp (repositório original — 14 estrelas, 8 forks, 17 commits)
- https://www.pulsemcp.com/servers/bimgeek-speckle (descrição das tools, autor, data de lançamento)
- https://speckle.systems/blog/speckle-raises-12-5-million-to-build-the-first-aec-data-hub/ (Series A, Addition)
- https://opensource.construction/projects/speckle/ (licença Apache 2.0, natureza open-source)
