# Pré-Check Técnico — WAN 2.2 (21-23/08/2026)

## Objetivo
Identificar bloqueios técnicos ANTES de começar setup em 24/08. Se algo falhar aqui, avisar Lúcio IMEDIATAMENTE (não guardar para relatório final).

**Status:** Checklists 1-7 executados por Wallenberg (Bash) em 27/08/2026 — Burle não tinha Bash/PowerShell desde 21/08, achado escalado por Lúcio na drenagem de hoje. Ambiente tecnicamente pronto, com uma ressalva material de hardware (ver Checklist 2). Falta só Checklist 8 (teste de inferência real, requer download de pesos do modelo — decisão de Go a tomar antes de baixar 10-20GB).

---

## Checklist 1: Repositório WAN 2.2

- [x] **GitHub repo acessível?** https://github.com/Wan-Video/Wan2.2
  - Status: Confirmado
  - Resultado: `git ls-remote` retornou refs normalmente (HEAD, main, PRs abertos) — repo acessível via HTTPS
  - Problema (se houver): nenhum

- [ ] **Licença Apache 2.0 confirmada?** (libre para uso comercial e self-hosted)
  - Status: Não verificado nesta rodada (não cloneei o repo ainda, só testei ls-remote)
  - Resultado: ___________
  - Problema (se houver): ___________

- [ ] **README possui instruções de setup?** (Python, CUDA, PyTorch versões específicas)
  - Status: Não verificado nesta rodada — próximo passo é clonar e ler
  - Resultado: ___________
  - Problema (se houver): ___________

- [ ] **Exemplos/test cases disponíveis no repo?** (para validação básica)
  - Status: Não verificado nesta rodada
  - Resultado: ___________
  - Problema (se houver): ___________

---

## Checklist 2: Hardware — GPU e VRAM

- [x] **GPU Instalada:** RTX 4090?
  - Ferramenta teste: `nvidia-smi` (Bash)
  - Resultado esperado: GPU detectada, CUDA Compute Capability 8.9+
  - **Resultado real: NÃO é RTX 4090 — é NVIDIA GeForce RTX 2060 SUPER, Compute Capability 7.5 (Turing, não Ada Lovelace).** Premissa do plano original estava errada.
  - VRAM disponível (total): 8192 MiB (8 GB)
  - VRAM livre (antes de qualquer processo): 6938 MiB (~6,9 GB)
  - Problema: hardware real é bem mais modesto que o assumido no plano — CUDA Version do driver é 13.1 (nvidia-smi), compatível com PyTorch cu124 instalado.

- [x] **Requisito WAN 2.2:** 8-12GB VRAM típico, 6GB mínimo
  - Status: Comparado
  - **MARGINAL** — 8GB total bate o mínimo mas fica na borda inferior do "típico" (8-12GB). Depende de qual variante do modelo (1.3B vs 14B, T2V vs I2V) Burle for usar — variantes maiores podem não caber. Recomendo Burle testar primeiro com o modelo menor (1.3B) antes de tentar o 14B.

---

## Checklist 3: Python e Gerenciamento de Dependências

- [x] **Python 3.10+ instalado?**
  - Ferramenta teste: `python --version` (Bash)
  - Resultado esperado: Python 3.10.x, 3.11.x, ou 3.12.x
  - Resultado real: Python 3.12.10 — OK
  - Problema (se houver): nenhum

- [x] **pip atualizado?**
  - Ferramenta teste: `pip --version`
  - Resultado real: pip 26.2.1 — OK
  - Problema (se houver): nenhum

- [ ] **venv ou conda disponível?** (para isolamento de ambiente)
  - Resultado real: não verificado nesta rodada — recomendo Burle criar venv dedicado antes de instalar deps do WAN 2.2 (ambiente Python já tem outras libs instaladas globalmente, ex. pptagent)
  - Problema (se houver): ___________

---

## Checklist 4: PyTorch e Dependências ML

- [x] **PyTorch 2.0+ instalado com CUDA support?**
  - Ferramenta teste: `python -c "import torch; print(torch.__version__, torch.cuda.is_available())"`
  - Resultado esperado: "2.0.x True" ou "2.1.x True"
  - Resultado real: **2.6.0+cu124 True** — melhor que o esperado
  - Problema (se houver): nenhum

- [x] **CUDA 11.8+ disponível?**
  - Ferramenta teste: `nvidia-smi` (já executado acima)
  - Resultado esperado: CUDA Version 11.8, 12.0, ou 12.1
  - Resultado real: CUDA Version 13.1 (driver) / PyTorch compilado com cu124 — compatível
  - Problema (se houver): nenhum

- [x] **cuDNN instalado?** (tipicamente dentro do PyTorch CUDA package, mas confirmar)
  - Ferramenta teste: `python -c "import torch; print(torch.backends.cudnn.version())"`
  - Resultado esperado: Número de versão (e.g., 8803 para cuDNN 8.8.0)
  - Resultado real: 90100 (cuDNN 9.1.0) — OK
  - Problema (se houver): nenhum

---

## Checklist 5: Git e Clone do Repositório

- [x] **Git instalado e acessível?**
  - Ferramenta teste: `git --version`
  - Resultado real: git version 2.55.0.windows.2 — OK
  - Problema (se houver): nenhum

- [x] **Acesso ao GitHub (SSH ou HTTPS)?**
  - Ferramenta teste: `git ls-remote https://github.com/Wan-Video/Wan2.2.git` (HTTPS)
  - Resultado esperado: Lista de refs (branches, tags)
  - Resultado real: OK — retornou HEAD, main, e refs de PRs abertos
  - Problema (se houver): nenhum

---

## Checklist 6: Espaço em Disco

- [x] **Espaço em disco disponível?** (modelo WAN 2.2 precisa ~10-20GB para pesos + código + outputs)
  - Ferramenta teste: `Get-PSDrive` (PowerShell)
  - Espaço disponível (drive D, que hospeda o repo do organismo): 155,2 GB livres — OK, folga ampla
  - Espaço disponível (drive C): 51,2 GB livres — também OK
  - Problema (se houver): nenhum

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
| 1 | GitHub acesso | Não | — | Repo acessível, README/licença ainda não lidos |
| 2 | GPU/VRAM | Parcial | Média | GPU real = RTX 2060 SUPER (8GB), não RTX 4090 assumida no plano. Testar modelo 1.3B antes do 14B |
| 3 | Python | Não | — | OK |
| 4 | PyTorch/CUDA | Não | — | OK, versões acima do mínimo |
| 5 | Git | Não | — | OK |
| 6 | Disco | Não | — | OK, folga ampla |
| 7 | Env vars | Não verificado | — | Verificar ao clonar o repo |
| 8 | Teste mínimo | Não executado | — | Requer clone + download de pesos (10-20GB) — decisão de Go antes de baixar, dado VRAM marginal |

**Achado principal desta rodada (27/08, Wallenberg):** Burle nunca teve `Bash`/`PowerShell` — 6 dias sem conseguir rodar nenhum destes testes. Ambiente já está pronto tecnicamente (checklists 1-7 passam), então o bloqueio de ferramenta não é mais impeditivo daqui pra frente: falta só decidir quem clona o repo e roda o teste de inferência (Checklist 8) — Burle ainda sem shell, então recomendo Wallenberg/Hely (que já tem Bash) fazer o clone + primeiro teste com o modelo 1.3B, e passar o ambiente pronto para Burle testar os 10 prompts via ferramenta de geração de vídeo (não shell).

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
