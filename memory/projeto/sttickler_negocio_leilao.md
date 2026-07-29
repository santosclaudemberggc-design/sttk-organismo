---
name: sttickler-negocio-leilao
description: "Modelo de negócio real da Sttickler — quais serviços são precificação própria vs. leilão de arquitetos parceiros, descoberto numa proposta comercial real"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Modelo de negócio real — Leilão de arquitetos parceiros

Descoberto em 09/07/2026 ao ler a proposta comercial real do cliente Daniel (Recreio dos Bandeirantes, RJ), em `D:\001_STTICKLER\001_Projetos 2023 - Sttikler Empreendimentos\...\Daniel - OB\Proposta\Segunda Proposta Orçamentaria de projeto de arquitetura - Daniel _20260302_135641_0000.pdf` (25 páginas, feita no Canva).

## Como funciona
A Sttickler cobra **preço próprio** em só 3 serviços: **Projeto Legal, Projeto de Interiores e Compatibilização de Projetos**. Pra todo o resto (Arquitetura, Complementares — Estrutural/Elétrico/Hidrossanitário, Automação, Paisagismo), o cliente escolhe entre **arquitetos parceiros** que cotam o mesmo escopo — a Sttickler não coloca markup em cima do valor do parceiro, só gerencia e fiscaliza ("Responsabilidade da Contratada": gerenciar/fiscalizar o parceiro, zelar pelo cronograma, tirar dúvidas — não produzir).

Confirmação visível na tabela real da proposta: nas 3 colunas de arquitetos parceiros (123 Projetei, MCosta, G&M), **Projeto Legal e Projeto de Interiores têm valor idêntico nas 3 colunas** — prova de que são serviço próprio da Sttickler, não repasse.

## Catálogo definitivo de serviços (11 itens, substitui o agrupamento de 6 categorias da proposta antiga)
1. Projeto de Arquitetura
2. Projeto Legal
3. Projeto Estrutural
4. Projeto Elétrico
5. Projeto Hidrossanitário
6. Projeto de Interiores
7. Projeto de Automação
8. Projeto de Paisagismo
9. Compatibilização de Projetos
10. Projeto Executivo
11. Orçamento Executivo de Obra

CFTV e Telefonia (que apareciam como item separado na proposta antiga) foram absorvidos por Automação. Compatibilização entra como linha própria na mesma tabela de Leilão inicial (não numa proposta separada mais adiante).

## Como isso muda os Agentes do organismo
Isso é a base pra decidir quais Agentes devem **produzir** (Legal, Interiores, Compatibilização) vs. quais devem apenas **coordenar/auditar** o que o arquiteto parceiro entrega (todo o resto, hoje). Ver [[sttickler_ceo_wallenberg]] função 10 (Organizador do Leilão) e [[sttickler_revit_capacidade]] pra viabilidade técnica de cada um.

## Onde fica a margem, e decisão sobre mostrar isso ao cliente (10/07/2026)
Confirmado pelo usuário: o ganho real da Sttickler nesse modelo é a **coordenação dos projetos**, embutida especificamente no valor de **Compatibilização** (não é markup espalhado em cada linha — é concentrado ali). Legal e Interiores são precificados à parte mas não necessariamente carregam a mesma lógica de "taxa de coordenação".

**Decisão de design da proposta:** o cliente **não precisa ver** qual serviço é da Sttickler e qual é do parceiro — essa distinção existia como selo verde/marcação na tabela e nos cards de etapa, e foi **removida** do modelo (ver [[sttickler_ceo_wallenberg]], seção de Documento de Referência). É informação de uso **interno** (coordenação e estrutura orgânica do CEO Wallenberg/Gestores), sem necessidade de aparecer pro cliente.

## CAU do Claudemberg em 2026 — resolve quase todo o limite de ART/RRT (corrigido 10/07/2026)
Usuário confirmou que vai tirar seu **CAU** (Conselho de Arquitetura e Urbanismo) ainda em 2026. Primeira leitura desta memória dizia que isso só cobria o lado de arquitetura — **errado, corrigido após verificação por busca**. Pela Resolução CAU/BR nº 21/2012, arquiteto registrado no CAU tem atribuição pra assinar RRT de Legal, Estrutural (exceto fundação profunda), Elétrico de baixa tensão (padrão residencial) e Hidrossanitário — ou seja, cobre praticamente todo o escopo técnico de Construção do Zero. Detalhe completo e fontes em [[sttickler_revit_capacidade]].

## Condições de pagamento (contexto, da proposta real)
7% de desconto via PIX/boleto (30% entrada + 20% em 30 dias + 20% em 90 dias + 30% na entrega), ou parcelado em até 3x sem juros no cartão (4x-12x com juros).
