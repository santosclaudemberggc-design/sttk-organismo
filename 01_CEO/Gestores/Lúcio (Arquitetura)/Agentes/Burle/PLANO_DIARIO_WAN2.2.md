# Plano Dia-a-Dia — WAN 2.2 Setup & Testes (21-28/08/2026)

## 21/08 (quarta) — HOJE — Preparação e Comunicação

**O que fazer:**
- [x] Lê instrução de Wallenberg
- [x] Atualiza arquivo de estado (`_estado_burle.md`)
- [x] Cria 10 prompts de teste (`PROMPTS_WAN2.2_TESTE.md`)
- [x] Cria checklist pré-técnico (`PRECHECK_WAN2.2_TECNICO.md`)
- [x] Comunica a Lúcio via handoff (`HANDOFF_WALLENBERG_21_08_2026.txt`)
- [ ] Valida que consegue acessar GitHub WAN 2.2 (teste básico de acesso em navegador)

**Resultado esperado:** Lúcio está informado, plano está claro, estrutura está pronta.

**Se bloqueio encontrado:** Avisar Lúcio hoje mesmo (quarta à noite se possível).

---

## 22/08 (quinta) — Pré-Check Técnico — PARTE 1

**O que fazer:**
- [ ] Executa checklist 1 (GitHub acessível, licença, README, exemplos)
- [ ] Executa checklist 2 (GPU RTX 4090, VRAM disponível)
- [ ] Executa checklist 3 (Python 3.10+, pip, venv/conda)

**Ferramentas:** 
- Navegador (acessar GitHub)
- PowerShell (nvidia-smi, python --version, pip --version)

**Resultado esperado:** Primeira metade do pré-check preenchida.

**Se bloqueio encontrado:** Avisar Lúcio no mesmo dia.

---

## 23/08 (sábado) — Pré-Check Técnico — PARTE 2

**O que fazer:**
- [ ] Executa checklist 4 (PyTorch 2.0+, CUDA 11.8+, cuDNN)
- [ ] Executa checklist 5 (Git, clone do repositório)
- [ ] Executa checklist 6 (Espaço em disco)
- [ ] Executa checklist 7 (Variáveis de ambiente)
- [ ] Executa checklist 8 (Teste de inferência mínima — if possible)
- [ ] Preenche resumo de bloqueios

**Ferramentas:**
- PowerShell (Python imports, git commands)
- Eventualmente: IDE ou Text Editor se precisar escrever script test mínimo

**Resultado esperado:** Pré-check 100% preenchido. Decisão: Go ou Not-Go.

**Se bloqueio encontrado:** Avisar Lúcio no mesmo dia (sábado).

**Se tudo OK:** Confirmado ready para 24/08.

---

## 24/08 (domingo) — Setup Real

**O que fazer:**
- [ ] Fork repositório WAN 2.2 em local de trabalho (se não feito em 23/08)
- [ ] Cria ambiente virtual (venv ou conda) isolado
- [ ] Instala dependências (PyTorch com CUDA, outras libs conforme README)
- [ ] Valida setup (teste básico, importa módulo, verifica GPU)
- [ ] Documenta tempo e qualquer ajuste necessário

**Ferramentas:**
- PowerShell (setup, pip install, validação)
- Navegador (se documentação do repo precisar ser consultada)

**Resultado esperado:** Ambiente pronto, primeira run de teste (dummy prompt) funciona.

**Se bloqueio encontrado durante setup:** Avisar Lúcio IMEDIATAMENTE (domingo à noite se necessário).

**Se tudo OK:** Pronto para começar Prompt 1 em 25/08.

---

## 25/08 (segunda) — Testes Prompts 1-5

**O que fazer:**
- [ ] Executa Prompts 1-5 (tópicos fixos de arquitetura)
- [ ] Registra para cada: tempo geração (min), resolução, duração vídeo, qualidade (1-5), notas
- [ ] Preenche matriz de teste (`PROMPTS_WAN2.2_TESTE.md`)

**Resultado esperado:** 5 vídeos gerados, matriz parcialmente preenchida, padrão de qualidade/velocidade observado.

**Se bloqueio encontrado:** Avisar Lúcio IMEDIATAMENTE.

---

## 26/08 (terça) — Testes Prompts 6-10

**O que fazer:**
- [ ] Executa Prompts 6-10 (acervo + inventados)
- [ ] Registra para cada: tempo geração (min), resolução, duração vídeo, qualidade (1-5), notas
- [ ] Completa matriz de teste (`PROMPTS_WAN2.2_TESTE.md`)
- [ ] Analisa dados: velocidade média, qualidade média, padrões de erro (se houver)

**Resultado esperado:** 10 vídeos gerados, matriz completa, análise estatística pronta.

**Se bloqueio encontrado:** Avisar Lúcio IMEDIATAMENTE.

---

## 27/08 (quarta) — Análise e Relatório Final

**O que fazer:**
- [ ] Compara WAN 2.2 com Open-Generative-AI anterior (se tiver logs) — velocidade, estética, consistência
- [ ] Avalia: "Pronto pra produção?" (sim/não/com ressalva)
- [ ] Se não pronto: identifica bloqueio exato (problema técnico específico)
- [ ] Escreve relatório final: `RELATORIO_WAN2.2_BURLE.md`
  - Seção 1: O que é WAN 2.2 (2-3 frases)
  - Seção 2: Setup completado (quais passos, tempo, fácil vs. tricky)
  - Seção 3: Testes (quadro 10 prompts com dados)
  - Seção 4: Qual ferramenta é melhor? (números)
  - Seção 5: Pronto pra produção? (sim/não/ressalva)
  - Seção 6: Se não pronto, qual é bloqueio exato?
- [ ] Entrega relatório a Lúcio

**Resultado esperado:** Relatório formal, estruturado, com dados concretos.

**Antes de enviar:** Relê a instrução de Wallenberg, confirma que relatório responde todas as 6 seções obrigatórias.

---

## 28/08 (quinta) — Decisão Final

**O que fazer:**
- [ ] Aguarda feedback de Lúcio + Wallenberg sobre relatório
- [ ] Possíveis desfechos:
  1. **Go:** WAN 2.2 entra em produção, aguarda próximos casos (Portinari começa a receber material visual)
  2. **Not-Go:** Pivô a LTX-2.3 ou outro plano de Wallenberg
  3. **Com ressalva:** Segue com WAN 2.2 mas com limitações documentadas (ex: velocidade, VRAM marginal)

**Próxima ação:** Depende da decisão. Se Go, fica pronto para receber casos reais de Lúcio.

---

## Escalação Rápida

Se **qualquer coisa** travar em:
- **21-24/08:** Avisar Lúcio (não crítico, mas não deixe passar a repouso)
- **25-26/08:** Avisar Lúcio IMEDIATAMENTE (risco de deadline)
- **27/08:** Avisar Lúcio IMEDIATAMENTE (última chance antes de relatório)

---

## Notas

- **Nível de sigilo:** Essa é tarefa operacional de Burle com Lúcio. Wallenberg já decidiu. Não há segredo, mas comunicar sempre por cadeia (Lúcio → Burle).
- **Backup plan:** Se WAN 2.2 falhar completamente em 24/08, fallback é LTX-2.3 (GitHub: https://github.com/Lightricks/LTX-Video, 12k stars, $10/1M tokens).
- **Qualidade de entrega:** Mesma do Exame 1, 2, 3. Não é experimento casual — é decisão de ferramenta oficial que vai na produção.

---

**Plano criado:** 21/08/2026  
**Responsável:** Burle (Agente de Renders e Vídeos)  
**Status:** Pronto para execução
