# Adendo de pendências — Etapa 03, v8 (Ensaio Sombra 003)

**Data:** 08/10/2026 | **Autor:** Lúcio (auditoria) | **Escopo:** adendo às peças v8; as peças v8 não foram alteradas.

## 1. Art. 31 III e IV do COES (LC 198/2019, texto consolidado SMU)

Fonte: COES consolidado SMU, p. 17 do PDF (Capítulo IV, Seção I, Condições das Edificações Unifamiliares e Bifamiliares), lida por Kelsen na página.

- Preâmbulo, verbatim: "...desde que mantidas as condições de salubridade e higiene da habitação, ficam dispensadas das seguintes exigências:"
- Art. 31 III, verbatim: "vagas de estacionamento;"
- Art. 31 IV, verbatim: "afastamento frontal, para estacionamento coberto de veículos, em telha vã, com um pavimento de altura;"

**O que isso significa para a etapa 3:**
- O texto não fixa dimensão de vaga e não define "telha vã". A dimensão de vaga continua no Art. 29 I e II (2,50 × 5,00 m).
- A v8 não usa a dispensa do Art. 31 III nem a do IV.
- Qualquer uso dessa dispensa (ex.: vaga sem demarcação ou abrigo em telha vã no afastamento) exige verificação primária e passa pelo Gate, da mesma forma que a R6 (reprovada em 08/10/2026).

## 2. Resíduos corrigidos

- **Skill de vaga (`vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`, v1.4):** a leitura de que a manobra é dividida entre vagas foi retirada do texto de lei; a linha de manobra compartilhada diz que é leitura, não texto, e que a área total não é calculada por soma de 25 m² por vaga. A linha 52 (preâmbulo do Art. 31) confere com o texto verbatim e não tem resíduo. A linha 91 está em branco na versão atual.
- **Skill de levantamento (`levantamento-topografico-cadastral-orientado-duli-licin-rj`, v1.9):** a referência ao "Art. 29 IV" para manobra compartilhada foi corrigida. O Art. 29 IV é acesso às faixas de circulação, mínimo 2,50 m; a divisão da manobra entre vagas é leitura, não texto. Backup em `CONSTRUCAO_DO_ZERO/01_CEO/Decisoes_Autonomas/_backups/2026-10-08/`.

## 3. Claim do AUTO_TESTE_R6 corrigido

A frase "zero ocorrências de LACRADO" foi substituída pelo que foi verificado: o termo "LACRADO" aparece só no registro AUTO_TESTE_R6, como referência ao nome da pasta de gabaritos; nenhuma ocorrência em peça, conta ou tabela.

## 4. Respostas de Claudemberg às decisões da etapa 3 (08/10/2026)

- **C1 — número de vagas no Briefing: 4 vagas.** A v8 usa 4 vagas no Briefing.
- **C2 — vaga descoberta no afastamento frontal: SIM, entra como alternativa nova.** Status jurídico, sem afirmar viabilidade: vedada na ZE-5 pelo Dec. 3.046 XXII (p. 4), salvo exceção específica da subzona, que não foi verificada; LC 270 Art. 363 §2º XII é divergente e está em Gate. A alternativa só pode ser apresentada como possibilidade a verificar, não como solução viável.
- **C3 — uso real da interpretação R6:** reprovada por Claudemberg e Maurício em 08/10/2026. Não pode ser usada em caso real; a v8 não a usa.
