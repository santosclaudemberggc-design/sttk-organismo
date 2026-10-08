# Adendo à entrega v7 — R6 reprovada (08/10/2026)

**Autor:** Lúcio (auditoria) | **Escopo:** Etapa 03 do Ensaio 003, pasta `entrega/v7/` | **Peças aprovadas:** não reescritas

## (a) Decisão

A R6 foi **reprovada em 08/10/2026 por Claudemberg e Maurício Costa**. A R6 é a regra que tratava 25 m² por vaga (vaga mais manobra) como área de garagem.

Regra vigente: só entra em caso real regra que siga norma ou regra de mercado que a valide.

## (b) Efeito sobre as contas da v7

As contas de garagem da v7 que usam **25 m² por vaga** (cenário a = 25,00) **não valem para caso real**. Ficam como cenário de leitura interna, sem validade para cliente, para Gate ou para protocolo.

## (c) Situação da área de garagem

A área de garagem por vaga fica **pendente de verificação primária**. Não há número válido de área de garagem por vaga nesta entrega. Os limites inferior e superior de "a" também ficam em aberto.

## (d) Onde a v7 usa a R6 (para localizar)

Números das linhas em cada arquivo da v7.

**02_relatorio_condicionantes_limitacoes_003_v7.md**
- l. 4: "a = 25,00" como cenário de todo número que depende de "a".
- l. 12: condição "a ≤ 40,69; com a = 25,00: 253,72" (folga do envelope).
- l. 15: "V ≥ 37,56 m²; capacidade 56,38 m²" (varandas com a = 25,00).
- l. 16: "com n = 4 e a = 25,00: 382,44 m²" (garagem computável).
- l. 47–48: "Fonte de a" e "Faixa de a: superior 25,00 m²", com citação da R6 da Skill de vaga.
- l. 53: alternativa B "inviável com a = 25,00".
- l. 57: H1, "4 vagas ocupam 100,00 m²" com a = 25,00.
- l. 66: "vaga descoberta (25,00 m²) não cabe".
- l. 105: térreo "153,72 m² com 4 vagas, contra 228,72 m² com 1 vaga (cenário a = 25,00)".

**03_matriz_decisoes_pendentes_003_v7.md**
- l. 6: "a = m² por vaga: pendente; os números com a = 25,00 são cenário".
- l. 10: "V ≥ 62,56 − a (com a = 25,00: V ≥ 37,56)".
- l. 28: linha 13, "153,72 com 4 vagas".
- l. 37: linha 22, "a = pendente (cenário 25,00)", citando Skill de vaga §3 e R6.

**anexo_contas_003_v7.md**
- l. 5: mudança (i) da v7, "a = pendente (cenário 25,00)".
- l. 53: "Limite superior, 25,00 m²: vaga (12,50) + manobra integral (12,50)", citando Skill de vaga §3 e R6.
- l. 55–56: "a = pendente; cenário usado: 25,00".
- l. 61: A = 457,44 + a + V.
- l. 64–72: **C-5** inteiro (tabela H0 com a = 25,00: 4 vagas → C = 382,44, G = 100,00; 6 vagas → C = 332,44, G = 150,00).
- l. 76–82: **C-6** inteiro (tabela H1, a = 25,00).
- l. 88–90: **C-7** (V = 37,56; capacidade 56,38; "81,38 − a").
- l. 96–97: **C-7** quadro M-c (482,44) e M-b (457,44 com faltas 62,56 e 37,56).
- l. 110–111: **C-8** tabela da alternativa A com a = 25,00 (75,00 e 125,00).
- l. 113: **C-8** área e permeável com a = 25,00.
- l. 129–138: **C-9** alternativa B, "inviável com a = 25,00".
- l. 190: **C-8** "nenhuma vaga descoberta cabe na folga de 22,79".
- l. 203, 210: térreo da suíte de D. Lourdes (153,72 com 4 vagas; 103,72 com 6).
- l. 220–224: **Garagem H0** (cenário a = 25,00), programa, alternativas A e B, permeável.
- l. 250: linha de correção da v6 ("25 m² por vaga" → Art. 29 III).
- l. 260, 263: linhas 5 e 8 da tabela de decisões (C = 382,44 e 332,44, cenário).
- l. 314, 318: linhas 9 e 13 da tabela de conformidade (garagem e alternativa B).
- l. 321: "a = 25 m² por vaga" saiu como fonte primária (afirmação estreitada).
- l. 336–341: Art. 29 I–III e "a = pendente (cenário 25,00)".
- l. 361–362: tabela de pendências (linhas 12 e 13).

**00_nota_auditoria_lucio_003_v7.md**
- l. 11: termo proibido "25 m²/vaga" como tamanho de garagem; ocorrência só como cenário.
- l. 43: C3, Gate para uso real da R6.
- l. 47: "a" pendente, cenário 25,00.
- l. 56: v1.6 → v1.7 da Skill de levantamento (histórico, não muda conta).

**tabela_correcoes_oscar_v7.md**
- l. 8: item E1, fonte do "a" (citação da R6 como COES Art. 29 III).
- l. 22: item 2, "cenário 25,00 rotulado".

**01_levantamento_planialtimetrico_cadastral_DULI_003_v7.md**
- Sem conta com 25,00. Só declara leitura da Skill de vaga (l. 173 e 182). Nenhuma correção obrigatória nesta peça por causa da R6.

**ADENDO_gate_R6_08-10-2026.md** (já existente nesta pasta, não alterado por este adendo)
- Trata do Gate da R6 e do que a v8 deve tratar (l. 12, 16, 19). Vale como registro anterior; este adendo prevalece sobre ele quanto ao uso da R6.

## (e) Próxima versão

Se houver **v8**, ela refaz as contas de garagem **sem a R6**: remove os números com a = 25,00 (C-5, C-6, C-7, C-8, C-9, garagem H0, térreo, programa e tabelas de pendências), e deixa a área de garagem por vaga como pendente de verificação primária, com dono e fonte a buscar. Não reaproveita os números do cenário.

## Declaração

As peças aprovadas (01, 02, 03, `anexo_contas_003_v7.md`, `tabela_correcoes_oscar_v7.md`, `00_nota_auditoria_lucio_003_v7.md`) não foram reescritas por este adendo. Só este arquivo foi criado.
