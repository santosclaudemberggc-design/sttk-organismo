---
name: portinari-pptAgent-geracao-apresentacao-pptx
description: "PPTAgent — gerador de PowerPoint automatizado via IA (MIT, 5k+ estrelas GitHub, PPTX real). Portinari descreve o projeto em linguagem natural e recebe slides prontos para apresentação ao cliente."
metadata:
  type: skill
  data: 26/08/2026
  gestor_alvo: Lúcio (Arquitetura)
  agente_consumidor: Portinari (Agente de Apresentações)
  status: proposta
  fonte: github.com/icip-cas/PPTAgent
---

# PPTAgent — Geração Automática de Apresentação PPTX

## Para qual Agente serve
Lúcio (Gestor Arquitetura) → Portinari (Agente de Apresentações) — montagem de apresentação ao cliente nas etapas de Estudo Preliminar e Anteprojeto.

## Status
proposta

## O que a ferramenta faz

Gera arquivos **PowerPoint (.pptx) reais** a partir de um prompt textual ou documento de referência. Usa um modelo de linguagem fine-tuned para design de slides (DeepPresenter-9B) e opera em dois estágios:
1. Analisa slides de referência (pode usar template existente)
2. Gera novos slides de forma iterativa, mantendo coerência visual e de conteúdo

Saída: arquivo `.pptx` compatível com PowerPoint, Google Slides e LibreOffice.

## Como se usa

### Via CLI (mais simples)
```bash
# Instalar (Python, sem chave de API)
pip install pptagent

# Gerar apresentação
uvx pptagent generate "Apresentação Estudo Preliminar: residência 300m² em Ipanema, partido minimalista, 3 alternativas de fachada" -o apresentacao_cliente.pptx
```

### Via Web UI (Docker — preferível para uso recorrente)
```bash
docker compose up
# Acessa em: http://localhost:7861
```

### Modelo gratuito (sem custo de API)
O modelo recomendado é o **DeepPresenter-9B**, disponível no Hugging Face gratuitamente. Configurar no `config.yaml`:
```yaml
model: DeepPresenter-9B
source: huggingface
```

## Evidência de segurança (Princípio 3)

- **Custo:** zero — MIT license, modelo DeepPresenter-9B gratuito no HuggingFace, sem API key de terceiro necessária
- **Vazamento de dado:** não vaza — execução 100% local (CLI ou Docker local); nenhum dado de projeto enviado para servidor externo quando usando DeepPresenter-9B localmente
- **Idoneidade:**
  - Repositório: `icip-cas/PPTAgent` no GitHub
  - Licença: MIT (confirmado)
  - Estrelas: **5.000+** (578 forks) — tração de comunidade muito alta
  - Commits: 426 no branch principal — ativo
  - README claro e documentação detalhada
  - Sem sinal de typosquatting

## Fluxo de integração STTK

```
Oscar (Revit) → [entrega: partido, programa, renders]
Burle → [entrega: 4-6 renders narrativos sequenciados]
Portinari → [descreve projeto + insere renders]
  ↓
PPTAgent generate "narrativa do projeto" → apresentacao.pptx
Portinari → [revisa, ajusta, finaliza]
  ↓
Cliente (apresentação estruturada, narrativa, visual)
```

## Limitações honestas

- Qualidade de layout depende do modelo e do template de referência fornecido — resultado inicial pode precisar de ajuste manual de design
- Não insere renders automaticamente nas posições certas — Portinari precisa adicionar as imagens após a geração do esqueleto textual (ou fornecer via template)
- Não substitui o juízo narrativo de Portinari (Ato 1 problema, Ato 2 solução, Ato 3 resultado) — é ferramenta de estruturação, não de decisão criativa
- Docker requer instalação local; CLI requer Python 3.10+

## Roadmap de adoção sugerido

1. **Drenagem implanta** — instalação CLI + Docker local
2. **Teste piloto** — Portinari usa em 1 projeto piloto (Estudo Preliminar real)
3. **Validação** — comparar tempo de montagem manual (2-3h) vs. PPTAgent + revisão (< 45min meta)
4. **Go/No-Go** — decisão em Reunião Semanal após piloto

## Fonte

- GitHub: github.com/icip-cas/PPTAgent
- Verificado em 26/08/2026 por WebFetch direto do repositório
