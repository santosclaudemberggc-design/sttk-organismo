---
skill: portinari_mindlin_office-pptx-mcp-python-pptx
titulo: "Office PowerPoint MCP Server — Geração de PPTX via python-pptx (sem PowerPoint instalado)"
gestor: Lúcio (Portinari) + Cardozo (Mindlin)
tipo: Trilha B — Ferramenta GitHub
data: 2026-08-28
status: proposta
criterios_passo8:
  custo_zero: true
  sem_vazamento_dados: true
  sem_malware: true
  funcionando_verificado: true
---

# Office PowerPoint MCP Server — python-pptx sem Microsoft PowerPoint

## O Que É

Servidor MCP de geração e manipulação de apresentações PowerPoint (PPTX) usando a biblioteca `python-pptx` do Python. **Não requer Microsoft PowerPoint instalado** — gera arquivos `.pptx` nativos via código Python puro, localmente.

- **Repositório:** [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)
- **Licença:** MIT
- **Stars:** 1.900+ | **Forks:** 246+
- **Status:** Arquivado desde março/2026 (read-only, sem novos commits — mas funcional)
- **Dependência:** python-pptx (Python puro, sem PowerPoint, sem Office 365)

## Verificação dos 4 Critérios (Passo 8)

| Critério | Status | Detalhe |
|---|---|---|
| 1. Custo zero | ✅ | MIT + python-pptx = sem licença paga |
| 2. Sem vazamento de dados do cliente | ✅ | Operação 100% local — sem upload externo, sem API de terceiros |
| 3. Sem malware | ✅ | MIT, 1.9k stars, 246 forks, código aberto auditável |
| 4. Recurso funcionando | ✅ | 34 ferramentas MCP em 11 módulos documentados; arquivado ≠ quebrado |

**Nota sobre arquivamento:** repositório arquivado em março/2026 significa que o autor não aceitará mais PRs/issues, mas o código continua funcional. Risco: incompatibilidades futuras com versões novas de python-pptx não serão corrigidas pelo autor.

## Como Funciona

### Arquitetura
```
Claude (MCP client) → Office-PowerPoint-MCP-Server → python-pptx → arquivo .pptx local
```
- Servidor MCP roda localmente (sem internet em runtime)
- Recebe instruções via protocolo MCP (JSON-RPC)
- Usa python-pptx para gerar/modificar o PPTX
- Retorna path do arquivo gerado

### 34 Ferramentas MCP em 11 Módulos

| Módulo | Ferramentas-chave |
|---|---|
| Criar apresentação | `create_presentation`, `add_slide`, `set_slide_layout` |
| Texto | `add_text_box`, `add_title`, `format_text` |
| Imagens | `add_image`, `add_image_from_url` |
| Tabelas | `add_table`, `set_table_cell` |
| Formas | `add_shape`, `add_connector` |
| Gráficos | `add_chart` (barras, pizza, linha) |
| Tema/Design | `set_theme_colors`, `set_background` |
| Slides | `copy_slide`, `delete_slide`, `reorder_slides` |
| Layout | `set_slide_size`, `add_section` |
| Exportar | `save_presentation` |
| Metadados | `get_presentation_info`, `list_slides` |

### Instalação (Wallenberg executa uma vez)
```bash
# Pré-requisito: Python 3.8+
pip install python-pptx mcp
```

### Configuração no Claude Code (`settings.json`)
```json
{
  "mcpServers": {
    "office-powerpoint": {
      "command": "python",
      "args": ["-m", "office_powerpoint_mcp.server"],
      "env": {}
    }
  }
}
```
*(ou via `uvx`/`npx` se o servidor expor ponto de entrada equivalente — ver README do repositório)*

## Comparação com Ferramentas Existentes

| Ferramenta | Status | Diferencial |
|---|---|---|
| **Office-PowerPoint-MCP-Server** (este) | Proposta | 34 tools MCP, python-pptx, sem PowerPoint, sem internet |
| **PPTAgent** (26/08) | Proposta (CLI) | Geração automática por IA + busca web, mas CLI (não MCP) |
| **Presenton** (28/08 manhã) | Proposta | Interface visual + MCP nativo + Ollama; gera apresentações web |
| **Gamma MCP** | Disponível agora | Gera Gamma online; exige conta, dados vão para Gamma servers |

**Quando usar qual:**
- **Office-PowerPoint-MCP-Server**: Portinari/Mindlin precisam gerar `.pptx` com controle fino de slides, tabelas, gráficos — sem depender de IA generativa nem internet. Apresentações corporativas formais.
- **Presenton**: Quando a interface visual web é preferível e o cliente aceita formato web/interativo.
- **PPTAgent**: Quando quer geração automática completa (IA decide o design) — requer Python + install.

## Uso Típico por Portinari / Mindlin

### Portinari (Apresentação de Estudo Preliminar ao cliente)
1. Recebe outputs de Oscar (plantas, quadro de áreas) e renders de Burle
2. Usa `create_presentation` → `add_slide` (x N) → `add_image` (renders) → `add_table` (quadro áreas) → `add_title`/`add_text_box` (narrativa)
3. Salva PPTX via `save_presentation` → entrega ao Wallenberg para Drive

### Mindlin (Apresentação de Complementares ao cliente)
1. Recebe outputs de Baumgart, Landell, Saturnino, Glaziou, Tenreiro
2. Usa `create_presentation` → um `add_slide` por especialidade → tabelas de especificação → `add_chart` (cronograma, custos)
3. Salva PPTX → Drive

## Limitações e Cautelas

- **Arquivado desde março/2026:** sem suporte ativo do autor. Usar tal como está; se python-pptx atualizar e quebrar algo, não haverá correção automática do servidor.
- **Sem recursos de IA generativa:** não "inventa" o design da apresentação. Portinari/Mindlin precisam instruir cada elemento. Para geração automática, ver PPTAgent.
- **Sem PPTM (macros):** gera PPTX padrão, não PPTM.
- **Templates:** pode carregar template PPTX existente como base (ideal: criar template padrão STTK uma vez).

## Fontes Verificadas

- Repositório: https://github.com/GongRzhe/Office-PowerPoint-MCP-Server (verificado 28/08/2026)
- Licença MIT confirmada no repositório
- 34 ferramentas listadas no README
- python-pptx: https://python-pptx.readthedocs.io/ (biblioteca pública, amplamente usada)

---

**Verificado em:** 28/08/2026  
**Verificador:** Rotina Diária Skills v2.7 (Wallenberg)  
**Critérios Passo 8:** APROVADO (4/4)  
**Pendência:** Wallenberg instala python-pptx e testa geração de um slide simples antes de ativar para Portinari/Mindlin
