---
name: baumgart-freecad-mcp-fem-estrutural
description: "FreeCAD MCP com análise FEM/CalculiX gratuita para projeto estrutural — candidato Passo 8 para Baumgart"
metadata:
  type: skill
  gestor_alvo: Cardozo (Complementares) — Baumgart (Agente Estrutural)
  status: proposta
  data: 2026-08-27
  fonte: github.com/sandraschi/freecad-mcp
---

# FreeCAD MCP — FEM Estrutural com CalculiX

## Para qual Agente serve

**Baumgart** (Agente de Estrutural, equipe de Cardozo) — análise de tensão/deformação, cálculo de fundações básicas, verificação de segurança estrutural em elementos individuais (pilares, vigas, lajes simples). Complementa o memorial técnico que o Baumgart já redige.

## Status

**proposta** — aguarda avaliação de Cardozo + implantação pela Drenagem Contínua.

## O que a ferramenta faz

**freecad-mcp** (sandraschi/freecad-mcp) expõe o motor CAD open-source FreeCAD como servidor MCP, acessível via Claude. Inclui 46 tools no total, com foco em:

- **Análise FEM com CalculiX:** stress (tensão), strain (deformação), deslocamento, fator de segurança
- **10 presets de material:** aço, alumínio, titânio, fibra de carbono + outros
- **Malha automática** via Gmsh (sem configuração manual de elemento finito)
- Modelagem 3D paramétrica (paredes, pisos, telhados, IFC)
- Exportação para IFC, STEP, STL

## Como se usa

**Requisitos técnicos:**
- Python 3.13+
- FreeCAD 1.1.1+ (gratuito, instalável em Windows)
- Ports: 10944 (MCP server), 10945 (dashboard)
- Opcional: Gmsh (para meshing automático)

**Instalação:**
```bash
just bootstrap
start.ps1
```

**Configuração Claude Code (`claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "freecad-mcp": {
      "transport": "sse",
      "url": "http://localhost:10944/sse"
    }
  }
}
```

**Fluxo para Baumgart:**
1. Baumgart recebe briefing de Cardozo com geometria básica do projeto
2. FreeCAD MCP modela o elemento estrutural (pilar, viga, laje)
3. Claude aciona `run_fem_analysis` com material "aço" e cargas do projeto
4. CalculiX retorna tensão máxima, fator de segurança, ponto crítico
5. Baumgart usa resultado no memorial técnico (NBR 6118:2026)

## Evidência de segurança (Princípio 3)

- **Custo:** zero. FreeCAD é GPL, freecad-mcp é MIT. Nenhum SaaS, nenhum cartão.
- **Vazamento de dado:** zero. Tudo roda localmente (localhost:10944). Sem upload para servidor externo.
- **Idoneidade:** README coerente, Python bem estruturado, 61 commits, desenvolvimento ativo. Ausência de pedido de credencial suspeita ou script oculto.

## Limitações honestas

- **Baixa tração:** 20 stars, 2 forks — baixo endosso da comunidade vs. outros MCPs desta lista. Risco: pode ter bugs não descobertos.
- **Não substitui software de cálculo estrutural certificado** (TQS, Eberick, SAP2000). Para memoriais técnicos CAU/RRT que exigem cálculo normativo completo, o Baumgart ainda precisa de software dedicado.
- **Análise FEM básica:** elementos de barra e placa — não cobre análise dinâmica, vento, sísmica ou outros casos especializados NBR 6118.
- **Instalação manual:** exige setup local (Python 3.13, FreeCAD 1.1.1) — não é plug-and-play.
- **Python 3.13+ obrigatório:** versão atual; verificar compatibilidade antes de instalar.

## Fonte

- GitHub: [sandraschi/freecad-mcp](https://github.com/sandraschi/freecad-mcp)
- Data de verificação: 27/08/2026
- Verificado por: leitura direta do README + código (sem clone, sem instalação)
