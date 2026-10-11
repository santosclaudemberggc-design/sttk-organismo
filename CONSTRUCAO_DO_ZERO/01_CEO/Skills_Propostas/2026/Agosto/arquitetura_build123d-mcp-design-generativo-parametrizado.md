---
name: build123d-MCP — design generativo parametrizado
description: MCP server comunitário para criação de modelos CAD 3D parametrizados via código Python
metadata:
  type: skill
  gestor_alvo: Lúcio (Arquitetura)
  agente_alvo: Oscar (Coordenador de Projeto, Estudo Preliminar)
  data_proposta: 2026-08-13
  ativo: não
---

# build123d-MCP — Design Generativo Parametrizado em 3D

## O Que É

Conector MCP comunitário que permite assistentes de IA criar modelos CAD 3D usando a biblioteca `build123d` (Python). Diferente de ferramentas que geram alternativas descritivas (como Hypar, que usa texto/programa do cliente), `build123d-MCP` permite **design generativo computacional direto** — o Agente escreve código Python estruturado, valida geometria, mede, renderiza e exporta (STEP, STL, SVG, DXF) dentro de uma sessão com o AI.

## Aplicação no Fluxo do Lúcio

**Etapa:** Estudo Preliminar (após Briefing aprovado pelo cliente)

**Função de Oscar (Coordenador):**
- Exploração de alternativas de **massas/layouts parametrizados** quando o programa do cliente permite múltiplas soluções (ex: edifício misto residencial+comercial, com proporção variável entre os dois usos)
- Validação rápida de conformidade geométrica (altura, recuos, áreas) contra parâmetros urbanísticos do Kelsen
- Comparação de cenários (x% residencial vs y% comercial) sem abrir Revit a cada mudança — ciclo de feedback mais rápido com cliente

**Diferença vs. Vitruvius (já ativo):**
- Vitruvius: manipula modelo Revit **já existente** (detalhamento, parametrização, automação de preenchimento)
- build123d: **gera** modelo desde o zero **em código**, a partir de lógica parametrizada — não é refinamento, é exploração de alternativas

**Diferença vs. Hypar (Skill de 10/08/2026):**
- Hypar: entrada é **descrição textual** do programa ("um edifício de 40 andares, 60% residencial, comercial na base")
- build123d: entrada é **script Python estruturado** escrito pelo Oscar ou claudebergado conjuntamente — controle fino sobre cada dimensão, padrão, restrição

## Capacidades

- **32+ operações CAD** nativas (criar sólidos, operações booleanas, patterns, arrays, offset, fillet, draft)
- **Renderização e preview** direto no Python (sem abrir software CAD)
- **Medição de geometria** (volumes, áreas, centróides, bounding box)
- **Exportação** em STEP/STL/SVG/DXF — compatível com Revit (STEP nativo)
- **Validação automática** de geometria (detecção de auto-interseção, manifold checks)
- **Integração com Grasshopper** (via plugin, extensão futura) para design generativo visual lado-a-lado com parametrização Python

## Idoneidade Verificada (Princípio 3)

- **44 ⭐ no GitHub** — projeto comunitário, não abandonado
- **487 commits** no branch principal — atividade contínua
- **Apache 2.0** — licença permissiva, uso comercial e modificação permitidos
- **Mantido por `pzfreo`** — desenvolvedor ativo (changelog.md documentado, PR abertos)
- **Sem sinal de typosquatting, malware ou pedido suspeito de script** — repositório segue padrão limpo

## Limitações Reconhecidas (Honestidade, Princípio 3)

- **Comunidade menor que alternativas** (Blender MCP: 25,2k ⭐; Vitruvius: N/A mas ativo em organismo)
- **Nenhuma integração visual nativa com Revit** — ciclo é: Python script → STEP → import ao Revit, não é síncrono
- **Não substitui o detalhe do Executivo** — serve só para exploração rápida de alternativas, antes do Oscar abrir Revit de verdade
- **Requer familiaridade com Python** (Oscar ou AI escrevendo código estruturado) — não é interface low-code visual

## Caso de Uso Confirmado

Não há caso ativo hoje usando build123d. **Ativa-se para futura exploração**, quando Oscar/Lúcio tiverem projeto com alto grau de liberdade paramétrica e ciclo de feedback rápido com cliente (ex: edifício misto com proporções variáveis, ou estudo de envoltória climática com rotações/inclinações).

## Fonte

- **Repositório:** https://github.com/pzfreo/build123d-mcp
- **Documentação:** Included in repository (CHANGELOG.md, README)
- **Verificação de segurança:** WebFetch + Grep (apenas leitura, nada clonado/instalado)

---

## Nota Técnica: Por Que Agora?

Diferente de Hypar (geração a partir de programa textual) e Helonic (validação de compatibilização 2D), build123d resolve um terceiro ângulo: **geração parametrizada de modelo 3D a partir de lógica computacional**, sem intermediação de BIM tradicional. Útil quando a regra de decisão é clara e codificável (ex: "se x > 40%, então fachada nord-oeste recua 5m e ganho solar aumenta 10%") mas não cabe bem em interface Revit.

Classificado como **ângulo oitavo distinto** do mês de Agosto/2026, complementar ao Vitruvius (manipulação) e Hypar (geração de texto).
