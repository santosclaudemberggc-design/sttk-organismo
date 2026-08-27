# Pré-Check Técnico — WAN 2.2 (21-23/08/2026)

## Objetivo
Identificar bloqueios técnicos ANTES de começar setup em 24/08. Se algo falhar aqui, avisar Lúcio IMEDIATAMENTE (não guardar para relatório final).

**Status:** Em andamento (21/08)

---

## Checklist 1: Repositório WAN 2.2

- [ ] **GitHub repo acessível?** https://github.com/Wan-Video/Wan2.2
  - Status: Verificar acesso
  - Resultado: ___________
  - Problema (se houver): ___________

- [ ] **Licença Apache 2.0 confirmada?** (libre para uso comercial e self-hosted)
  - Status: Verificar LICENSE file
  - Resultado: ___________
  - Problema (se houver): ___________

- [ ] **README possui instruções de setup?** (Python, CUDA, PyTorch versões específicas)
  - Status: Verificar estrutura do repo
  - Resultado: ___________
  - Problema (se houver): ___________

- [ ] **Exemplos/test cases disponíveis no repo?** (para validação básica)
  - Status: Verificar pasta `examples/` ou similar
  - Resultado: ___________
  - Problema (se houver): ___________

---

## Checklist 2: Hardware — GPU e VRAM

- [ ] **GPU Instalada:** RTX 4090?
  - Ferramenta teste: `nvidia-smi` (PowerShell/CMD)
  - Resultado esperado: GPU detectada, CUDA Compute Capability 8.9+
  - Resultado real: ___________
  - VRAM disponível (total): ___________
  - VRAM livre (antes de qualquer process): ___________
  - Problema (se houver): ___________

- [ ] **Requisito WAN 2.2:** 8-12GB VRAM típico, 6GB mínimo
  - Status: Comparar resultado acima com requisito
  - OK / MARGINAL / INSUFICIENTE: ___________
  - Problema (se houver): ___________

---

## Checklist 3: Python e Gerenciamento de Dependências

- [ ] **Python 3.10+ instalado?**
  - Ferramenta teste: `python --version` (PowerShell)
  - Resultado esperado: Python 3.10.x, 3.11.x, ou 3.12.x
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **pip atualizado?**
  - Ferramenta teste: `pip --version`
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **venv ou conda disponível?** (para isolamento de ambiente)
  - Resultado real: ___________
  - Problema (se houver): ___________

---

## Checklist 4: PyTorch e Dependências ML

- [ ] **PyTorch 2.0+ instalado com CUDA support?**
  - Ferramenta teste: `python -c "import torch; print(torch.__version__, torch.cuda.is_available())"`
  - Resultado esperado: "2.0.x True" ou "2.1.x True"
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **CUDA 11.8+ disponível?**
  - Ferramenta teste: `nvidia-smi` (já executado acima)
  - Resultado esperado: CUDA Version 11.8, 12.0, ou 12.1
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **cuDNN instalado?** (tipicamente dentro do PyTorch CUDA package, mas confirmar)
  - Ferramenta teste: `python -c "import torch; print(torch.backends.cudnn.version())"`
  - Resultado esperado: Número de versão (e.g., 8803 para cuDNN 8.8.0)
  - Resultado real: ___________
  - Problema (se houver): ___________

---

## Checklist 5: Git e Clone do Repositório

- [ ] **Git instalado e acessível?**
  - Ferramenta teste: `git --version`
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **Acesso ao GitHub (SSH ou HTTPS)?**
  - Ferramenta teste: `git ls-remote https://github.com/Wan-Video/Wan2.2.git` (HTTPS)
  - Resultado esperado: Lista de refs (branches, tags)
  - Resultado real: ___________
  - Problema (se houver): ___________

---

## Checklist 6: Espaço em Disco

- [ ] **Espaço em disco disponível?** (modelo WAN 2.2 precisa ~10-20GB para pesos + código + outputs)
  - Ferramenta teste: `Get-Volume` (PowerShell) ou `df -h` (WSL)
  - Espaço disponível (drive que vai hospedar código): ___________
  - Espaço disponível (drive que vai hospedar outputs): ___________
  - Problema (se houver): ___________

---

## Checklist 7: Variáveis de Ambiente e Configurações

- [ ] **PYTHONPATH set corretamente?** (se necessário para imports custom)
  - Resultado real: ___________
  - Problema (se houver): ___________

- [ ] **CUDA_HOME e LD_LIBRARY_PATH set (em WSL)?** (se rodar em Bash)
  - Resultado real: ___________
  - Problema (se houver): ___________

---

## Checklist 8: Teste de Inferência Mínima

- [ ] **Conseguir rodar um prompt mínimo de teste?** (texto → vídeo de 2 segundos)
  - Ferramenta teste: Script Python basic com import do WAN 2.2
  - Resultado esperado: Sucesso, vídeo gerado ou erro técnico específico
  - Resultado real: ___________
  - Tempo tomado: ___________
  - Problema (se houver): ___________

---

## Resumo de Bloqueios Encontrados

| Checklist | Item | Bloqueio? | Severidade | Ação Recomendada |
|-----------|------|-----------|-----------|-----------------|
| 1 | GitHub acesso | [ ] | — | — |
| 2 | GPU/VRAM | [ ] | — | — |
| 3 | Python | [ ] | — | — |
| 4 | PyTorch/CUDA | [ ] | — | — |
| 5 | Git | [ ] | — | — |
| 6 | Disco | [ ] | — | — |
| 7 | Env vars | [ ] | — | — |
| 8 | Teste mínimo | [ ] | — | — |

---

## Plano de Escalonamento (Se Bloqueio Encontrado)

**REGRA:** Não guardar bloqueio para 27/08 (relatório final).

- **21/08 (hoje):** Descoberta de bloqueio → e-mail para Lúcio mesmo dia à noite
- **22/08 (amanhã):** Validação com Lúcio, possível alternativa ou mitigação
- **24/08:** Proceder com setup ou pivô a LTX-2.3

---

## Informações de Contato para Bloqueio Crítico

- **Gestor:** Lúcio (Arquitetura)
- **E-mail:** [Via cadeia de comando — não direto]
- **Escalação:** Se Lúcio indisponível, sinalizar a Wallenberg via Lúcio

---

**Arquivo criado:** 21/08/2026  
**Próximo passo:** Executar checklists 22-23/08, preencher campos  
**Responsável:** Burle (Agente de Renders e Vídeos)
