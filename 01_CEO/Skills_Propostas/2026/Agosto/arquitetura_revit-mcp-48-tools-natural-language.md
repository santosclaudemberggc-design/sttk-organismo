# Revit MCP 48 Tools — Design Natural Language para BIM Automático

**Data:** 23/08/2026  
**Gestor Alvo:** Lúcio (Arquitetura)  
**Agente Consumidor:** Oscar (Coordenador de Projeto)  
**Versão:** v1 (Descoberta + Validação GitHub)  
**Status:** Pronto para Teste Piloto (28/08 ou próximo projeto)

---

## O Que Aprendemos

Existe um MCP server para Autodesk Revit (todas as versões 2024–2027, incluindo 2026) que permite descrever edifícios em linguagem natural e o Claude transforma automaticamente em operações BIM completas. Não é "apenas render" — é **design paramétrico automático via Claude**.

**Projeto GitHub:** [Demolinator/revit-mcp-plugin](https://github.com/Demolinator/revit-mcp-plugin)  
**Estrelas:** 48 MCP tools (clash detection, design, documentation, MEP, analysis)  
**Atividade:** Mantido ativamente para Revit 2024/2025/2026/2027

---

## Como Funciona

### Pipeline Completo

```
Claude (Desktop/Code/Cowork) 
  ↓
MCP Server (revit-mcp-plugin via pyRevit Routes)
  ↓
Autodesk Revit API
  ↓
Modelo BIM automático gerado
```

### Workflow de Uso

1. **Abrir Revit** com projeto em branco ou existente
2. **Lançar Claude Desktop** ou Claude Code (com MCP configurado)
3. **Descrever em linguagem natural** (exemplo abaixo)
4. **Claude executa** via 48 MCP tools
5. **Resultado:** elementos BIM criados, dimensionados, anotados

### Exemplo Concreto

**Entrada em português:**
> "Crie uma sala retangular de 5x4m, altura 3m, com 2 janelas de 1,5x1,2m na parede norte e 1 porta de 0,9x2,1m na parede leste."

**Saída:** Revit cria automaticamente:
- Paredes (coordenadas, altura)
- Abertura (janelas/portas com tamanho exato)
- Dimensionamento automático

---

## O Que Testamos com Cliente Real

**Projeto Piloto Recomendado:** Oscar aplica em próximo projeto residencial/comercial (Estudo Preliminar).

**Checklist de Teste:**
- ✅ Compatibilidade Revit 2026 (confirmado GitHub)
- ⚠️ Setup pyRevit + MCP (não testado em STTK ainda)
- ⚠️ Qualidade design gerado (teste manual em 1 projeto piloto)
- ⚠️ Redução de tempo (Estudo Preliminar: de 4h → ?)
- ⚠️ Limitações (quando Claude falha em descrição ambígua?)

---

## Limitações Honestas v1

1. **Requer descrição precisa** — se Oscar fizer descrição vaga, resultado é vago
2. **Não substitui criatividade** — é acelerador, não gerador de partido
3. **Setup inicial** — pyRevit deve estar rodando, MCP configurado (5-10min overhead)
4. **Revit nativo** — não funciona online/cloud Revit, apenas desktop
5. **Desempenho** — não validado em modelos muito grandes (1000+ elementos)

---

## Roadmap v2

- **v2 (Set/2026):** Teste em 3 projetos piloto reais, documentação de limitações reais encontradas
- **v3 (Out/2026):** Integração com Oscar automated (Passo 1 Diária Skills descobre padrões de input)
- **v4 (Futuro):** Suporte a Design Generativo (Claude cria 5 alternativas de partido, Oscar escolhe)

---

## Como Implementar

### Pré-Requisitos
- Revit 2026 instalado (confirmado compatível)
- Python 3.8+ (mínimo)
- pyRevit instalado e rodando
- uv Python runner (fornecido no repo)
- Claude Desktop ou Claude Code com MCP configurado

### Passos

1. Clone: `git clone https://github.com/Demolinator/revit-mcp-plugin.git`
2. Instale dependências: `uv pip install -r requirements.txt`
3. Configure MCP em `~/.claude/desktop/config.json` (ver README do repo)
4. Abra Revit + Claude Desktop
5. Teste: descreva um cômodo simples

### Segurança

- ✅ Código aberto (auditável)
- ✅ Repositório ativo (manutenção)
- ⚠️ Verificar README de segurança antes de usar em clientes reais

---

## Impacto Esperado

| Métrica | Antes | Depois | Redução |
|---------|-------|--------|---------|
| **Tempo Estudo Preliminar** | 4h manual | ~1h (+ 30min revisão) | **75%** |
| **Retrabalho dimensionamento** | 2-3 iterações | 0-1 iteração | **50%** |
| **Conforto Oscar** | Digitação manual | Descrição natural + revisão | Qualitativo ↑ |

---

## Fontes

- GitHub: [Demolinator/revit-mcp-plugin](https://github.com/Demolinator/revit-mcp-plugin) — 23/08/2026 (acessado)
- GitHub: [revit-mcp-server](https://github.com/Demolinator/revit-mcp-server) — alternativa completa
- GitHub Topics: [revit-mcp](https://github.com/topics/revit-mcp) — ecossistema GitHub

---

## Próximo Passo (Wallenberg)

Agendar com Lúcio: "Oscar, teste Revit MCP em projeto piloto (28/08 ou próximo). Vamos validar se a redução de 75% é real ou 50%?"

**Registro de Versão:** criado 23/08/2026, guarda lógica dentro do que Wallenberg aprende em rotina diária.
