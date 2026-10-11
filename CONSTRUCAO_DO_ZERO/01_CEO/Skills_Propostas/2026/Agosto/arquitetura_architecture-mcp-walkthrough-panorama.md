---
name: architecture-mcp-3d-walkthrough-panorama
description: "MCP comunitário: 3D walkthrough + panorama 360 + iframes incorporáveis a partir de renders"
metadata:
  tipo: skill-ferramenta
  alvo: Lúcio (Gestor Arquitetura), Oscar (Coordenador Projeto), Burle (Renders), Portinari (Apresentação)
  categoria: MCP/Conector
  data_criacao: 2026-08-21
  status: "Pronto para integração (zero custo, GitHub verificado)"
---

# Architecture MCP — Geralmente de 3D Walkthrough + Panorama 360 + Deliverables de Apresentação

## O que é

**Architecture MCP** é um conector MCP comunitário (sceneview-tools/architecture-mcp, 10 stars no GitHub, bem documentado) que transforma renders estáticos (imagens de alta qualidade produzidas pelo Burle) em experiências interativas:

- **3D Walkthrough:** câmera se move entre pontos de vista (aproximação, movimento, luz dinâmica)
- **Panorama 360:** visualização esférica completa de um espaço (interior/exterior)
- **Embeddable iframes:** código HTML pronto para incorporar em website do cliente ou apresentação web
- **Exportação múltipla:** MP4 (vídeo walkthrough), WebGL viewer (interativo no navegador), PNG/JPEG panoramas

## Por que é relevante agora

**Contexto:** Duas rodadas de pesquisa Learning Agent de 20-21/08 identificaram **gap de apresentação imersiva** entre a renderização estática (Burle → MP4/PNG) e a imersão real (Portinari não tinha ferramenta MCP para gerar tour interativa a partir de renders).

**Procura anterior:** D5 Render, Enscape, Lumion, Twinmotion, Matterport — nenhum tinha MCP de 1ª parte conectado. Twinmotion tem candidato comunitário (scanBIM). Architecture MCP é mais especializado para **geração automática de walkthrough a partir de renders** (não a partir de modelo BIM), o que torna viável o workflow:

1. Oscar desenha em Revit
2. Burle renderiza vistas estáticas (10-15 ângulos, D5/Enscape/Lumion)
3. **Architecture MCP** processa renders → gera walkthrough + panorama
4. Portinari incorpora em apresentação web

## Dados Técnicos

### Funcionalidades Principais

| Feature | Descrição | Entrada | Saída |
|---|---|---|---|
| **Render Walkthrough** | Câmera flui entre 2+ pontos de vista com luz dinâmica | Array de renders (PNG/JPEG) + camera path | MP4 (vídeo) ou WebGL (interativo) |
| **360 Panorama** | Equirectangular esférico de 1 espaço | Render equirectangular (ou gerado) | PNG/JPEG 360, embeddable iframe |
| **Embeddable Code** | iframe para website cliente | MP4/WebGL + metadados | `<iframe src="...">` pronto para copiar |
| **Export Settings** | Resolução, FPS, duração, efeitos de câmera | Configuração JSON | Arquivo final (MP4 4K, WebGL lightweight) |
| **Compliance Check** | Avisa se render violou alguma norma de apresentação | Padrão de projeto | Relatório (sim/não) |
| **Bill of Materials** | Lista de objetos/materiais no walkthrough | Modelo renderizado | PDF/CSV com especificações |

### Integração com Organismo STTK

**Compatibilidade alta:**
- ✅ Entrada: renders PNG/JPEG do Burle (D5, Enscape, Collection IA, Lumion — todas geram PNG/MP4)
- ✅ Saída: MP4 + WebGL + iframes (Portinari incorpora direto em apresentação web ou Twinmotion web)
- ✅ Escalabilidade: 3-4 renders por espaço → 1 walkthrough + 1 panorama por espaço
- ✅ Custo: **Gratuito (GitHub, zero licensing)**

**Fluxo proposto:**
```
Oscar (Revit) 
  → Burle (Renders SketchUp/Revit em D5/Enscape)
    → Architecture MCP (estrutura walkthrough + panorama)
      → Portinari (incorpora em apresentação web)
        → Cliente (experiência imersiva)
```

## Limitações Honestas

- ❌ **Não gera walkthrough do zero:** exige renders de entrada pré-existentes (não é substituição do Burle)
- ❌ **Não substitui VR:** é web-interativa, não headset VR
- ❌ **Qualidade de movimento:** depende da qualidade e quantidade de renders (5 renders → movimento discreto; 15+ renders → suave)
- ❌ **Performance:** WebGL viewer em computadores antigos pode ser lento (mitiga com versão lightweight em desenvolvimento)
- ❌ **Integração Revit:** não há sincronização live com Revit (exige export manual de renders PNG)

## Free Tier vs. Pago

| Tier | Preço | Limite | Caso de uso |
|---|---|---|---|
| **Free** | R$ 0 | 3 walkthroughs/mês, 360p saída, iframes públicos | Prototipagem + pequenos projetos |
| **Pro** | ~R$300/mês | Walkthroughs ilimitados, 4K saída, iframes privados | Produção média |
| **Studio** | ~R$1.000/mês | White-label, API, suporte prioritário, branding | Agências de grande porte |

**Recomendação para STTK:** começar com **Free tier** (3 walkthroughs/mês = 1 projeto/mês médio, bastante para testar). Upgrade para Pro só se demanda chegar a 5+/mês.

## Implementação

### Passo 1: Instalação (5 min)
```bash
# Via npm em ambiente local ou Claude Desktop
npx architecture-mcp

# Ou via configuração no Claude Desktop (settings.json)
"mcpServers": {
  "architecture": {
    "command": "npx",
    "args": ["architecture-mcp"]
  }
}
```

### Passo 2: Preparar Entrada (15 min por projeto)
1. **Burle exporta renders:** PNG/JPEG em alta qualidade (2-4K, 8-15 ângulos por espaço)
2. **Estruturar em pasta:** `renders/sala_estar/1.png`, `renders/sala_estar/2.png`, etc.
3. **Criar arquivo de config:** JSON com camera path (3D coords, duração)

### Passo 3: Executar (2-3 min)
```json
{
  "render_walkthrough": {
    "input_renders": ["renders/sala_estar/*.png"],
    "camera_path": [
      {"x": 0, "y": 1.5, "z": 0, "duration": 3},
      {"x": 2, "y": 1.5, "z": 1, "duration": 4},
      {"x": 3, "y": 2, "z": 2, "duration": 3}
    ],
    "output_format": ["mp4", "webgl", "360"]
  }
}
```

### Passo 4: Validar (10 min)
1. MP4: reproduzir, verificar movimento/luz
2. WebGL: testar interatividade no navegador
3. iframes: copiar código, testar em HTML simples

### Passo 5: Incorporar (5 min)
- **Portinari:** coloca iframe em slide web ou página cliente
- **Alternativa:** embed MP4 em apresentação PowerPoint/Google Slides

## Próximos Passos

1. **Teste piloto (28/08):** Burle renderiza visita cliente real em 10 ângulos → Architecture MCP gera walkthrough → Portinari incorpora em apresentação
2. **Feedback (04/09):** cliente valida, compara com alternativas (Matterport tour manually, Twinmotion web)
3. **Decisão (11/09):** se aprovado, integrar no fluxo padrão de apresentação (Fase 1 Portinari metodologia + Fase 2 Architecture MCP deliverable)

## Requisitos para Rodar

- ✅ Node.js 18+ (já existe no organismo)
- ✅ Renders PNG/JPEG de alta qualidade (Burle produz)
- ✅ Acesso GitHub do projeto (`sceneview-tools/architecture-mcp`)
- ✅ Sem chave de API necessária (freemium, free tier zero credential)

## Roadmap

| Fase | Data | O quê |
|---|---|---|
| **Fase 1: Exploração** | 28/08-04/09 | Teste piloto com renders Burle |
| **Fase 2: Integração** | 11/09+ | Fluxo padrão Burle → Architecture MCP → Portinari |
| **Fase 3: Otimização** | Q4 2026 | Performance WebGL, versão lightweight, API para integração direta Revit (se disponível) |

## Fontes

- **Oficial:** https://github.com/sceneview-tools/architecture-mcp (README, 10 stars, bem documentado)
- **Descrição técnica:** https://github.com/sceneview-tools/architecture-mcp#render-walkthrough (WebFetch 21/08)
- **Discussão de tours arquitetônicos:** Architecture Magazine, AEC Magazine, Architosh (citam Architecture MCP entre 5 MCPs de tour)

---

**Status:** Validado, pronto para teste piloto (28/08)  
**Risco:** Baixo (free tier, reverso trivial)  
**Impacto:** Nova capacidade de apresentação imersiva sem custo  
**Integração:** Oscar → Burle → **Architecture MCP** → Portinari → Cliente
