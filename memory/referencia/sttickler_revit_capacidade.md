---
name: sttickler-revit-capacidade
description: "O que é tecnicamente viável hoje (09/07/2026) para agentes de IA produzirem dentro do Revit da Autodesk, e o limite legal do ART/RRT"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Capacidade real de agentes de IA no Revit (checado 09/07/2026)

**Importante:** este é um campo que muda rápido — revalidar com busca antes de confiar cegamente se already houver muito tempo passado desde 09/07/2026.

## O que existe hoje
A Autodesk lançou em junho/2026 um **Revit Public MCP Server** oficial (Tech Preview, add-on pro Revit 2027) que conecta um assistente de IA direto num modelo Revit ao vivo. Hoje é **só leitura** — proposital, pra estabelecer confiança antes de liberar escrita. Existem também MCP servers de terceiros (ex: ArchiLabs, 100+ ferramentas) que já fazem criação/edição de modelo por linguagem natural.

## Por disciplina (mapeado pro catálogo de 11 serviços em [[sttickler_negocio_leilao]])
| Serviço | Situação em 09/07/2026 | Por quê |
|---|---|---|
| Compatibilização | Pronto | É só leitura/análise (achar interferência entre modelos) — exatamente o que o MCP oficial já faz. |
| Projeto de Interiores | Curto prazo | Pouco regulado, sem ART/RRT — sobretudo memorial, layout, especificação (trabalho de texto). |
| Projeto Legal | Curto prazo | Mais compilação/checagem contra legislação do que modelagem. |
| Arquitetura, Estrutural, Elétrico, Hidrossanitário, Automação, Paisagismo | Exige investimento de engenharia | Escrita de modelo hoje só via MCP de terceiros (não o oficial da Autodesk ainda) ou Dynamo/pyRevit + Automation API (execução em nuvem). Tecnicamente possível, mas é projeto de software de verdade, não algo que se resolve numa conversa. |

## Limite permanente — ART/RRT (CORRIGIDO em 10/07/2026, ver correção abaixo)
Todo projeto técnico exige **assinatura de profissional licenciado** no Brasil (RRT via CAU ou ART via CREA). Isso **não desaparece com IA melhor** — mesmo que um agente produza o desenho inteiro, um humano licenciado precisa revisar e assinar. "Substituir o parceiro" numa disciplina significa, no máximo, trocar quem produz o rascunho — a revisão/assinatura humana continua obrigatória.

**Correção importante (10/07/2026):** a primeira versão desta memória dizia que Estrutural/Elétrico/Hidrossanitário exigem CREA (engenheiro) e que o CAU do Claudemberg não cobriria essas 3. **Isso estava errado.** Verificado por busca — a Resolução CAU/BR nº 21/2012 (art. 3º), com base no art. 2º da Lei 12.378/2010, dá ao arquiteto/urbanista registrado no CAU atribuição pra assinar RRT de:
- **Projeto Estrutural** (concreto, metal, madeira) — cobre fundação **rasa** (sapata, bloco, radier, NBR 6122). **Não cobre fundação profunda** (estaca) — isso continua exigindo CREA.
- **Projeto Elétrico predial de baixa tensão** — cobre o padrão residencial (Construção do Zero). Alta tensão/escopo não-residencial continua CREA.
- **Projeto Hidrossanitário predial** — água, esgoto, águas pluviais, gás canalizado.

**Conclusão prática:** com o CAU do Claudemberg (2026), ele pode assinar pessoalmente RRT de Legal, Estrutural, Elétrico e Hidrossanitário pra projetos residenciais típicos — cobre praticamente todo o escopo de Construção do Zero. Só fica de fora: fundação profunda e qualquer coisa fora do padrão residencial (aí sim precisa de CREA externo). Isso reduz MUITO a dependência de engenheiro terceirizado só pra assinatura — mas não elimina a exigência de revisão humana licenciada em si, só muda quem pode ser essa pessoa.

Sources: [Arquiteto pode assinar projeto estrutural?](https://ricardocandello.com.br/blog/arquiteto-pode-assinar-projeto-estrutural/), [Lei 12.378/2010 - Planalto](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12378.htm), [Resolução CAU/BR Nº 21/2012](https://transparencia.caubr.gov.br/resolucao21/), [Conheça os sete grupos de atividades - CAU/BR](https://caubr.gov.br/conheca-os-sete-grupos-de-atividades-dos-arquitetos-e-urbanistas/), [Justiça reafirma: Arquitetos podem assinar projetos de energia de baixa tensão - CAU/BR](https://caubr.gov.br/justica-reafirma-arquitetos-podem-assinar-projetos-de-energia-de-baixa-tensao/).

Sources (buscadas em 09/07/2026): [Revit Public MCP Server - Autodesk AEC Tech Drop](https://www.autodesk.com/blogs/aec/2026/06/17/revit-public-mcp-server/), [Revit MCP - ArchiLabs](https://archilabs.ai/posts/revit-model-context-protocol), [Building for Agentic AI - Autodesk Platform Services](https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services).

---

## Bridge Vitruvius — o MCP que usamos de fato (verificado 16/07/2026)

Diferente do MCP oficial da Autodesk (só leitura), temos um bridge próprio chamado **Vitruvius** conectando ao Revit ao vivo (testado no Revit 2026, doc "Projeto2") **com escrita real**. O que ele **cria de fato hoje**: nível, parede (entre 2 pontos, em metros), porta e janela (hospedadas em parede, por offset), piso (contorno fechado). Leitura: status, model_info, níveis, tipos, elementos, ambientes (`list_rooms`), detalhe de elemento. Edição: apagar elemento. Coordenadas em metros, X→leste / Y→norte.

**GAP de capacidade (PENDÊNCIA — levar ao sistema/desenvolvimento do MCP):** o Vitruvius **não tem comando para criar Ambiente (Room)** nem para gerar **cotas/dimensões**. `list_rooms` só lê ambientes existentes; não há `create_room` nem `create_dimension`. Consequência prática: ao montar um cômodo pela automação, o Room (que calcula área/nome/acabamento no quadro de áreas) e as cotas alinhadas precisam ser inseridos **manualmente** no Revit (`Arquitetura → Ambiente`; `Anotar → Cota Alinhada`/atalho DI). Constatado ao criar um cômodo-teste de 4×3 m no Páv. térreo. **Ação:** incluir criação de Room e de cotas no roadmap do bridge Vitruvius — sem isso, o fluxo de projeto legal/arquitetura não fecha 100% por automação. Relaciona-se ao limite de escrita em [[sttickler_negocio_leilao]] (disciplinas que hoje só coordenam o parceiro).
