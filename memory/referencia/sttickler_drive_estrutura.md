---
name: sttickler-drive-estrutura
description: "Mapeamento real do Google Drive \"Dptº de Projetos\" da Sttickler e regra de filtro de escopo (Construção do Zero vs. outros produtos)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Estrutura real do Drive "Dptº de Projetos" (Sttickler)

Confirmada por exploração direta via MCP do Google Drive em 09/07/2026 (ferramentas `mcp__014dedc9-41ba-4ccb-9bf4-e296d09b271e__*`, carregadas via ToolSearch quando deferidas).

## Pastas raiz de "Dptº de Projetos"
- **000_CLIENTES** — `Bairro > Nome do Cliente > pastas de projeto`. Onde `criar_novo_projeto()` do código legado já grava.
- **001_MATERIAL DE CONTROLE INTERNO** — fonte de conhecimento pra virar Skills do CEO Wallenberg. 7 subpastas (ver abaixo).
- **002_** — ainda não existe / reservada, usuário não sabe pra quê ainda.
- **003_RELATORIOS_CONSELHO** — destino dos relatórios mensais do CEO, uma pasta por ano/mês.

## Subpastas de 001_MATERIAL DE CONTROLE INTERNO e escopo
| Pasta | Conteúdo | Está no organismo (Construção do Zero)? |
|---|---|---|
| 001_PROCEDIMENTOS | POPs organizados por Gestor — subpastas nomeadas **"GESTOR {ÁREA}"** (ex.: "GESTOR LEGAL", confirmado por Hely em 20/07/2026 — não é só "Legal") | ✅ tudo |
| 002_CETIFICAÇÃO | Certificação de Arquitetos Parceiros + Política de Precificação — cobre todos os produtos no mesmo documento (não separável por pasta) | ✅ mas cross-produto; sem Gestor "dono" fixo — tratado como pauta do Padronizador (função 6 do CEO) |
| 003_CHECKLIST | "VALIDAÇÃO DE FORMULÁRIO" e "VALIDAÇÃO DE ENTREGA DE PROJETO" (genéricos) + pasta "Reforma" isolada | ✅ os 2 genéricos / ❌ Reforma |
| 004_FORMULÁRIOS | `CONSTRUÇÃO NOVA` / `REFORMA` | ✅ Construção Nova / ❌ Reforma |
| 005_PLANILHAS | `CONSTRUÇÃO NOVA` / `REFORMA` | ✅ Construção Nova / ❌ Reforma |
| 006_MEMORIAIS DESCRITIVOS | Por Gestor + pasta "ESPECIAIS" (que contém Reforma/Retrofit/Home Staging) | ✅ pastas por Gestor / ❌ ESPECIAIS |
| 007_PLANILHAS DE CONTROLE | Interno (Construção Nova/Reforma/Retrofit) + Externo (planilha "Controle de entregáveis p/ arq. externos", por disciplina: Arquitetônica, Estrutural, Elétrica...) | ✅ Construção Nova + Externo / ❌ Reforma/Retrofit do Interno |

## Regra de filtro de escopo (confirmada consistente em todas as pastas testadas)
**Sempre que existir uma subpasta nomeada Reforma, Retrofit ou Home Staging, ela é excluída do organismo. O resto entra.** Permite filtrar por caminho de pasta, sem precisar interpretar o conteúdo de cada arquivo pra saber se é do escopo certo — mais simples e menos sujeito a erro.

## Sobre arquitetos parceiros (contexto de negócio)
A Sttickler hoje opera contratando **arquitetos parceiros externos** pra executar os projetos (não é tudo equipe interna). A 002_CETIFICAÇÃO é o gate de entrada pra saber se um parceiro está apto a trabalhar com a empresa; a Planilha de Controle de Entregáveis (007) define o que deve ser entregue e como, por disciplina. Isso pode importar quando os Agentes dos Gestores forem definidos — parte da função de um Agente pode ser **coordenar/auditar um parceiro terceirizado**, não necessariamente produzir o projeto tecnicamente do zero.
