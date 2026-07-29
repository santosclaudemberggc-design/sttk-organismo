---
name: sttickler_licin_demolicao_ics_rj
description: Demolição no LICIN 2.0 (total vs parcial) e o que é o ICS do zoneamento (correção de rótulo)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 24d9ef72-4792-4c6f-9897-f58654189f89
---

Fecha as pendências #2 e #3 encaminhadas em 15/07/2026 (Cérebro, Função 3). Pesquisado por Wallenberg em 16/07/2026 contra fonte oficial. Complementa [[sttickler_licin_licenciamento_rj]] e [[sttickler_riu_api_oficial]] (o RIU retorna o campo `ics`).

**Item 2 — Demolição + construção nova é 1 processo ou 2? Depende de total vs parcial:**
- **Demolição TOTAL** = licença/processo **próprio e separado** ("Licença de demolição de edificação", serviço do carioca.rio; só o proprietário pode requerer; prazo 30 dias corridos). Logo: demolição total + obra nova = **2 processos** (a demolição + o LICIN da construção).
- **Demolição PARCIAL** = NÃO tem licença separada — é tratada como **"modificação com decréscimo de área"**, dentro do próprio projeto de modificação (**1 processo**).
- No projeto de modificação, a convenção de cores (Decreto 55622/2025, LICIN 2.0): **amarelo = demolição, vermelho = construção nova ou a legalizar, preto = existente sem modificação**.
- **Confiança média** no encadeamento exato: a licença de construção depende do protocolo/emissão da licença de demolição prévia (indicado pelas páginas de serviço), mas não confirmei verbatim se podem tramitar em paralelo ou se a demolição tem que estar emitida antes de protocolar a obra. Confirmar com Kelsen/Hely/Maurício antes de prometer sequência a cliente real.

**Item 3 — CORREÇÃO DE RÓTULO: ICS = Índice de Comércio e Serviços (NÃO "Compensação Social").**
Fonte: Dicionário de Termos oficial da LC 270/2024 (2ª ed., 04/12/2025), SMDU. Verbatim: *"ÍNDICE DE COMÉRCIO E SERVIÇOS - ICS: Parâmetro urbanístico representado pelo índice que define a área máxima de comércio e serviços permitida no terreno, mediante a multiplicação do seu valor pela Área Total Edificável (ATE)."* (Art. 344 IX; Art. 367.) **ATE = Área Total Edificável = CA × área do terreno.**
- É um **parâmetro de zoneamento** (o mesmo `ics` que o RIU devolve por coordenada, ex.: 0,36 / 0,4 / 0,6), que limita quanto de comércio/serviço cabe no lote. **NÃO é uma contrapartida nem pagamento.**
- Consequência: a pendência antiga "fórmula do ICS + isenção de 5 anos" partia de premissa errada (rótulo trocado). Não há "fórmula de contrapartida do ICS" nem "isenção de 5 anos" ligada a ele. O "5 anos" que aparecia é provável confusão com o **IPTU progressivo no tempo** (parcelamento/edificação/utilização compulsórios → IPTU progressivo por até 5 anos → desapropriação), que é penalidade para imóvel ocioso, não isenção. Pagamento por construir acima do CAB é a Outorga Onerosa — ver [[sttickler_outorga_onerosa_rj]].
- Registros internos que chamavam ICS de "Índice de Compensação Social" (ex.: Registro Diário 15/07, pendências do caso 3) devem ser lidos com essa correção.
