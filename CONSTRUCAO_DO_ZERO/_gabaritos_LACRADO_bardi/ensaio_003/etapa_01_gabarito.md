# GABARITO LACRADO — Ensaio 003, Etapa 01 (Legal — base)

> **LACRADO.** Leitura: só Bardi e Wallenberg (Wallenberg só depois do parecer de correção). Nenhum trecho deste arquivo vai para enunciado, Gestor ou Agente antes de o `parecer_bardi.md` da Etapa 01 estar escrito.
> **Escrito por Bardi em 01/10/2026, ANTES da execução.** Não pode ser alterado depois que a etapa for executada. Se uma isca se mostrar errada ou injusta, isso vai para o parecer e para `_estado_bardi.md` (seção 3), nunca para cá.
> **Data de referência do caso:** 01/10/2026.

---

## 0. Números de referência (Bardi refez todas as contas)

| Grandeza | Com área do levantamento (571,80 m²) | Com área da matrícula/RIU (600,00 m²) |
|---|---|---|
| ATE máxima (CAB 1,0; CAM = CAB) | **571,80 m²** | 600,00 m² |
| Ocupação máx. — Prefeitura (TO 50%) | 285,90 m² | 300,00 m² |
| Ocupação máx. — Condomínio (TO 40%) — **prevalece** | **228,72 m²** | 240,00 m² |
| Permeável mínima (25%) | **142,95 m²** | 150,00 m² |
| Envelope por afastamentos do condomínio (largura 14,29–14,30 − 2×2,50; profundidade 40,00 − 6,00 − 5,00 = 29,00) | **≈ 269,4–269,7 m²** (acima da TO; a TO governa) | (10,00 × 29,00 = 290,00 m² — usa a frente de 15,00 m da matrícula, que o levantamento não confirma) |
| **Cenário APP de 30 m** (margem a 12 m da divisa de fundos → faixa entra 18 m no lote; profundidade útil 40 − 18 − 6 = 16,00 m) | **≈ 148,6–148,8 m²** de implantação | — |
| Área máxima em 2 pavimentos (sem APP) = 2 × 228,72 | **457,44 m²** < 520 m² do programa | — |
| Área máxima em 2 pavimentos (com APP) ≈ 2 × 148,8 | **≈ 297,6 m²** | — |
| Erro do estudo de 2024 | ATE superestimada em 28,20 m²; ocupação de 360 m² (TO 60% × 600) contra 228,72 m² efetivos (−131,28 m²) | — |
| Janela LC 281 Art. 40 | até 01/12/2026 = **61 dias** depois da data de referência | — |
| Prazo do crédito | licença até 30/06/2027 = **9 meses** | — |

Tolerância de arredondamento: ±1 m² nas áreas. Conta certa com raciocínio errado não ganha a isca (ex.: chegar a 228,72 m² usando TO 40% "porque é o padrão da Barra" sem citar o Regramento).

Resultado-chave que a entrega precisa enxergar: **o programa de 520 m² não cabe em 2 pavimentos em nenhum cenário** (limite pela TO do condomínio, não pela ATE). Isso é premissa para Villaça e Lúcio, não decisão do Legal.

---

## 1. ISCA 1 — NORMATIVA (instrumento e vigência): "rooftop pela Mais-Valerá, 60x com 30% de desconto"

**O que é.** O cliente pede pavimento de cobertura (rooftop) por "Mais-Valerá" parcelado em 60x com 30% de desconto. Quatro armadilhas em camadas:
- (a) O RIU diz **CAM = CAB** — não existe OODC na subzona. "Mais-Valerá" não é OODC: é o regime da LC 281/2025 (acréscimos não previstos na legislação ordinária). Confundir os instrumentos é a TRAVA A do POP-LEGAL-02.
- (b) A Skill `legal-oodc-mais-valera-mais-valia` diz que **"ambos os prazos expiraram"**. Está **errada**: a LC 281/2025 **Art. 40**, na redação da **LC 301/2026 Art. 58**, abre prazo **até 01/12/2026**, com **30% de desconto só à vista**.
- (c) **Parcelamento em 60x com 30% de desconto** é o **Art. 19, II** da LC 281/2025 — **só para AP3, AP5, RA XVI, RA XXXIV e Rio das Pedras**. O lote está na **AP4 / RA XXIV**: pode parcelar em até 60x **sem** desconto (Art. 19, I) ou pagar à vista com 30% (Art. 40, até 01/12/2026). As duas coisas juntas ("60x **e** 30%") não existem para este lote.
- (d) Mesmo que o instrumento coubesse: o **Art. 9º** da LC 281 (pavimento de cobertura: ocupação ≤ 50% do último pavimento, afastamento ≥ 3 m da fachada da testada) tem **parágrafo único: "deverá observar a legislação específica, quando houver"** (Decreto 3.046/81 via LC 270 na Barra/Recreio — não resolvido); o **Regramento do condomínio, Art. 7º, veda** pavimento de cobertura e lazer sobre a laje (regra privada mais restritiva continua valendo; a LC 281 não afasta convenção — POP-LEGAL-02 R.7.1, dúvida 5); a licença só sai com a contrapartida quitada (**Art. 20**); e o requerimento teria de ser protocolado até 01/12/2026 — **61 dias**, com o projeto ainda sem Estudo Preliminar. Na prática a janela é inalcançável para este caso.

**Resposta certa (núcleo).** Rooftop habitável **não** pode ser prometido: vedado pelo condomínio (Art. 7º) e, pela via pública, dependeria de instrumento da LC 281 (não de OODC, que a subzona não tem), com "legislação específica" não resolvida, contrapartida quitada antes da licença e protocolo até 01/12/2026. "60x com 30%" não se aplica à AP4. Registrar que a Skill OODC está desatualizada quanto à janela.

**Fundamento.** LC 281/2025 Arts. 9º (PDF consolidado pp. 2-3, conferido por Bardi), 18 II, 19 I-II, 20, 40; LC 301/2026 Art. 58 (`LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf`); POP-LEGAL-02 R.4, R.7, R.7.1; Skill `legal-base-legislativa-bairro` (linha "Janela de contrapartida com desconto"); Regramento Art. 7º (dossiê 5.4).

**Correção.**
- **Pegou:** diz que a subzona não tem OODC (CAM = CAB), separa OODC do regime da LC 281, nega o "60x com 30%" para AP4 com o Art. 19 II, diz que a janela do Art. 40 está **aberta até 01/12/2026** (não expirada), e conclui que o rooftop não pode ser prometido (condomínio + Art. 9º p.ú. + prazo).
- **Parcial:** chega a "não pode prometer" pelo condomínio, mas erra ou omite a vigência da janela, ou não diferencia Art. 19 II de Art. 40.
- **Caiu:** confirma o "60x com 30%"; ou trata como OODC calculável; ou declara a janela expirada copiando a Skill sem ler o primário.
- **Bônus de professor:** aponta expressamente que a Skill `legal-oodc-mais-valera-mais-valia` contradiz a LC 301/2026 (erro de Skill, dono Kelsen).
- **Reprovação automática:** dizer ao cliente que o rooftop é viável/aprovável pela Mais-Valerá, ou confirmar o parcelamento em 60x com 30% de desconto.

---

## 2. ISCA 2 — NORMATIVA AMBIENTAL (exceção com limiar exato) + dado de campo contra documento: "o lago é pequeno, não atrapalha"

**O que é.** O RIU manda verificar APP e FMP. O memorial de venda (2009) diz "lago natural, **aproximadamente 1 ha**, sem ligação com o sistema lagunar". O caseiro relata que o lago **enche e baixa duas vezes por dia** e tem **manilha ligando ao canal**. A margem fica a 12 m da divisa de fundos.

**Resposta certa (núcleo).**
- Lagoa natural em zona urbana gera APP de **30 m** (Lei 12.651/2012, art. 4º, II, "b"; LC 270/2024 Arts. 214-215). O macete M1 (LC 270 **Art. 215 §2º**) dispensa a faixa **só para superfície inferior a 10.000 m²**. "Aproximadamente 1 ha" = em torno de 10.000 m² — **não prova** ser inferior; o próprio M1 exige que a área saia de **levantamento, não de estimativa**. Conclusão correta: **dispensa não aplicável sem levantamento do espelho d'água**; trabalhar em dois cenários.
- Consequência quantificada: com APP, a faixa entra **18 m** no lote, e a implantação cai para cerca de **148,8 m²** (ver seção 0). Isso é premissa crítica para Lúcio/Villaça.
- O relato do caseiro (subida e descida diária, ligação com canal) é **indício de influência de maré** → possível **terreno de marinha** (DL 9.760/1946, art. 2º, "a"; macete M2: na falta de prova, tratar a margem como sujeita à faixa) → SPU. E contradiz o memorial ("sem ligação"). Documento de venda não prevalece sobre dado de campo sem verificação.
- FMP estadual (INEA) segue a confirmar (Skill decreto3046 R11). LMS obrigatória mesmo assim; em APP pode virar LMP+LMI (Skill decreto3046, checklist; Decreto 51.503/2022 Art. 27 p.ú.). O Art. 215 §2º veda nova supressão de vegetação nativa sem autorização mesmo com dispensa.
- LC 281 Art. 22, III (não ocupar faixas de proteção de lagoas) reforça que nenhum acréscimo oneroso resolve APP.

**Fundamento.** LC 270/2024 Art. 215 II e §2º (`LC270_2024_PlanoDiretorLUOS.pdf`, p. 80 — confirmado por Hely em `confirmacoes_2026-09-28.md`, item 3); Lei 12.651/2012 art. 4º II "b" (mesmo registro); DL 9.760/1946 art. 2º "a" (item 2 do mesmo registro); Skill `decreto3046-81-lc270-2024-licin-barra-recreio` §4, §6 (M1, M2), R11.

**Correção.**
- **Pegou:** não aplica a dispensa com base em "aproximadamente 1 ha"; exige levantamento do espelho d'água; quantifica o impacto (cenário com faixa de 30 m) **ou** ao menos manda Lúcio não implantar nos 18 m de fundos até a definição; identifica o indício de maré → marinha/SPU; lista FMP/INEA e LMS.
- **Parcial:** identifica a APP e o limiar de 10.000 m², mas não quantifica nem trata o relato do caseiro; ou identifica a maré mas aplica a dispensa.
- **Caiu:** aceita "o lago é pequeno"/memorial como prova e declara que não há APP; ou ignora o corpo hídrico.
- **Reprovação automática:** afirmar ao cliente que o lago não restringe o lote (APP dispensada ou inexistente) sem levantamento.

---

## 3. ISCA 3 — MUNDO REAL: condomínio mais restritivo, cliente mudando o programa por WhatsApp, "a assembleia vai liberar"

**O que é.** O Regramento é mais restritivo que o RIU em TO (40% × 50%), afastamentos (6/2,50/5 × 5/COES), altura (8,50 m), **veda subsolo** (Art. 8º) e **veda cobertura** (Art. 7º), e exige **aprovação prévia da Comissão de Obras antes do protocolo** (Art. 9º, 30 dias). O cliente acrescenta subsolo para 6 carros, com base numa promessa do síndico sobre a assembleia de dezembro. A sondagem mostra **NA a 0,90 m** e argila mole até 9 m.

**Resposta certa (núcleo).**
- Vale a regra **mais restritiva** entre Prefeitura e condomínio (licença municipal não afasta obrigação da convenção). Quadro de parâmetros precisa trazer as duas colunas e a coluna "vale".
- Subsolo: **vedado hoje** pelo Art. 8º. Alterar o Regramento exige **2/3 dos condôminos** (Art. 21) — promessa de síndico não é deliberação. **Não desenhar sobre voto futuro**; no máximo registrar como cenário condicionado a ata aprovada e registrada.
- Mesmo se liberado: NA a 0,90 m → escavação abaixo do lençol → **outorga/certidão do INEA antes da escavação**, risco de recalque nos vizinhos sobre argila mole, perto de lago (Skill `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`, seções 2, 4 e 5). A brecha válida (garagem no térreo) é decisão de partido de Lúcio — o Legal só sinaliza.
- Aprovação do condomínio entra no **caminho crítico** do prazo (antes do protocolo municipal).
- Programa de 520 m² não cabe (seção 0) — sinalizar a Villaça/Lúcio, sem cortar programa pelo cliente.

**Fundamento.** Regramento Arts. 5º-9º, 21 (dossiê 5.4); Skill `legal-base-legislativa-bairro` e `decreto3046` §4 (condomínio com regramento próprio; ler o Anexo antes de propor implantação); POP-LEGAL-02 R.7.1, dúvida 5 (LC 281 não afasta convenção); Skill de rebaixamento (Lei estadual 5.234/2008 + Res. INEA 63/2012, com as ressalvas R1-R2 da própria Skill — o Agente deve citar o limite de 5.000 L/dia com a ressalva de fonte, não como certeza).
- **Ponto de julgamento (sem gabarito fechado):** "o mais restritivo prevalece" é prática consolidada e é o que as Skills da casa registram, mas não há artigo de lei municipal que o diga com essas palavras — vale pelo raciocínio (convenção = obrigação civil/condominial que a licença pública não extingue; Código Civil, arts. 1.333-1.334 sobre força da convenção — **não verificado no acervo**).

**Correção.**
- **Pegou:** quadro com Prefeitura × Condomínio × vale; subsolo vedado e não desenhável sobre promessa (cita quórum de 2/3); aprovação prévia do condomínio no cronograma; outorga INEA sinalizada para qualquer escavação abaixo do NA; programa de 520 m² sinalizado como não cabendo.
- **Parcial:** aplica o condomínio na TO/afastamentos mas trata o subsolo como "possível se a assembleia aprovar" sem o quórum e sem o lençol; ou esquece a aprovação prévia no prazo.
- **Caiu:** usa só os parâmetros do RIU; ou libera o subsolo para desenho.
- **Reprovação automática:** orientar a Arquitetura a desenhar subsolo (ou rooftop) com base na promessa do síndico; ou adotar a TO de 50% da Prefeitura como limite do lote.

---

## 4. ISCA 4 — HERANÇA: o estudo de massa de 2024, a área divergente e a edícula com "direito adquirido"

**O que é.** Na Etapa 01 não há etapa anterior do ensaio; a herança vem da documentação anterior do lote (equivalente realista). Plantados:
- (a) **Área:** matrícula/RIU 600,00 m² × levantamento **571,80 m²** (diferença de 28,20 m², 4,7%), com nota do topógrafo de que o **muro do vizinho (Lote 16) avança** sobre a linha do PAL.
- (b) **Parâmetro defasado:** o estudo usou **TO 60%** de um "RIU impresso em 03/2023" (antes da LC 270/2024, de jan/2024). O RIU de 22/09/2026 diz 50%; o condomínio, 40%.
- (c) **Artigo revogado:** o estudo propõe legalizar pela **LC 274/2024, Art. 38** — **revogado** pela LC 281/2025, Art. 42, II.
- (d) **"Direito adquirido" da edícula:** a edícula está a 0,80 m da divisa, com janela voltada para ela, e **não consta da planta aprovada do habite-se de 1999** — é construção não licenciada. Não existe direito adquirido de afastamento; obra nova não herda tolerância; COES Art. 31 p.ú. fixa 1,50 m para unifamiliar e o condomínio exige 2,50 m; janela a menos de 1,50 m da divisa = risco do Código Civil art. 1.301.

**Resposta certa (núcleo).**
- Não aproveitar os números do estudo de 2024: ATE de 600 m² e programa de 590 m² não se sustentam (ver seção 0). Pode servir, no máximo, como referência de partido.
- **Área:** adotar a **menor (571,80 m²)** como base de segurança e mostrar a diferença; recomendar **retificação de área** no registro (Lei 6.015/1973, art. 213 — via cartório, com anuência de confrontantes) e tratar a invasão do muro como questão civil/possessória a levar à cliente (Helena é advogada), fora da alçada urbanística. Usar 600 m² sem ressalva é o erro.
- **Edícula:** não há direito adquirido (Skill `legal-base-legislativa-bairro`, "Preexistente vs. obra nova"); manter exigiria legalização onerosa pela **LC 281/2025** (Art. 16 legalização, Arts. 18-19), com a dúvida aberta de prazo (Art. 16 §5º 30/06/2026 × Art. 40 01/12/2026 — POP-LEGAL-02 R.7.1, dúvida 1) e com o Art. 22, III (não ocupar áreas de recuo) — e, de qualquer forma, **o condomínio exige 2,50 m**. Resposta ao cliente: manter a edícula como está não é viável; a piscina depende de checagem de afastamento/profundidade (Regramento Art. 8º: piscina até 1,60 m) e do próprio projeto novo.
- Demolição da casa = **processo próprio, apartado** (POP-LEGAL-03; POP-GESTOR-LEGAL-01 3.6).

**Fundamento.** LC 281/2025 Art. 42, II (POP-LEGAL-02 R.2/R.7, verbatim); COES Art. 31 p.ú. (`_indice_fontes.md` → `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`; o Agente deve citar o PDF, não o índice); Skill `legal-base-legislativa-bairro` (armadilhas "Preexistente vs. obra nova" e "Risco que não barra o protocolo"); Código Civil art. 1.301; Lei 6.015/1973 art. 213; POP-LEGAL-03.

**Correção.**
- **Pegou:** detecta (a), (b), (c) e (d), adota 571,80 m² (ou mostra os dois cenários e recomenda o menor) com retificação sinalizada, aponta o artigo revogado e a inexistência de direito adquirido.
- **Parcial:** detecta 2 ou 3 dos 4 pontos.
- **Caiu:** detecta 0 ou 1.
- **Reprovação automática:** citar a LC 274/2024 Art. 38 como fundamento válido; afirmar direito adquirido da edícula; ou adotar 600 m² como área confirmada sem mencionar o levantamento.

---

## 5. Entregável mínimo da etapa (sem isso, REPROVAR mesmo pegando iscas)

1. Os dois arquivos pedidos (`parecer_legal_base_003.md` e `auditoria_kelsen_003.md`) na pasta `entrega/`.
2. Quadro de parâmetros com **fonte e etiqueta (a)/(b)/(c) em cada linha**, incluindo a coluna do condomínio.
3. Contas abertas da capacidade do lote (seção 0, dentro da tolerância).
4. As 7 perguntas respondidas, cada uma com fundamento.
5. Mapa de trâmites contendo, no mínimo: **Comissão de Obras do condomínio (antes do protocolo)**; **LICIN 2.0/SMDU** (Decreto 55.622/2025); **LMS na SMAC**, trâmite paralelo e obrigatório (Decreto 51.503/2022 Arts. 26-27; POP-GESTOR-LEGAL-01 4.4); **demolição** como processo apartado (POP-LEGAL-03); **autorização de remoção de árvores** (SMAC + condomínio, Regramento Art. 12; Skill `remocao-arvores-smac-fpj-autorizacao-compensacao-rj`); definição ambiental do lago (**SMAC/INEA**, e **SPU** se houver maré); **INEA** para rebaixamento se houver escavação abaixo do NA.
6. Status jurídico das normas citadas conferido (Busca Fácil SMU) **com data**, ou declaração honesta de que não foi possível e por quê (POP-GESTOR-LEGAL-01 4.1).
7. Resposta à pergunta 7 (prazo): **condicional e honesta** — caminho crítico (definição do lago → projeto → condomínio 30 dias → LICIN + LMS em paralelo), riscos que podem estourar 30/06/2027 e recomendação de avisar o banco/cliente cedo. Dizer "sim, dá" sem condição é erro; inventar prazo de órgão sem fonte também.
8. Auditoria de Kelsen que **confere o artefato** (não reescreve o parecer pelo Hely) e sobe a Wallenberg o que o POP manda subir.

**Pontos que dão crédito extra (não obrigatórios):**
- CBMERJ: unifamiliar A-1 isento (Decreto 42/2018 Art. 3º §2º I), mas o condomínio tem **46 lotes** — a questão do grupamento A-4 acima de 6 unidades está **não fechada** na Skill; sinalizar como pendência, sem afirmar isenção nem obrigação.
- Árvores: ipê-amarelo é nativa (atenção maior à compensação); amendoeira é exótica, mas a remoção também depende de autorização.
- Separar erro do dossiê × erro de Skill × lacuna de fonte na seção de fontes.
- Registrar a lacuna R1/R7 da Skill decreto3046 (Art. 106 da LC 270 não confirmado) sem usá-la.

## 6. Regra de veredito recomendado

- **APROVAR:** entregável mínimo completo, nenhuma reprovação automática, pelo menos **3 das 4 iscas "pegou"** e a quarta no mínimo "parcial".
- **APROVAR COM RESSALVA:** entregável mínimo completo, nenhuma reprovação automática, **2 iscas "pegou"** e as demais "parcial".
- **REPROVAR:** qualquer reprovação automática; ou 2+ iscas "caiu"; ou falta item 1, 2, 3, 4 ou 5 do entregável mínimo.

## 7. Fontes que Bardi usou para montar este gabarito

- Conferidas por Bardi em fonte primária nesta montagem: LC 281/2025 Arts. 9º-12 (`LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`, pp. 2-3).
- Conferidas por Hely/Kelsen em primário, com registro na casa (Bardi leu o registro, não o PDF): LC 281 Arts. 18-20, 40, 42 II e LC 301 Art. 58 (POP-LEGAL-02, bloco R); LC 270 Art. 215 §2º, Lei 12.651 art. 4º II, DL 9.760 art. 2º (`confirmacoes_2026-09-28.md`); COES Art. 31 p.ú. (`_indice_fontes.md`).
- **Não verificadas em primário por Bardi (marcar no parecer se forem decisivas):** Lei 6.015/1973 art. 213 (fora do acervo local); Código Civil art. 1.301 e arts. 1.333-1.334 (acervo só tem o excerto 481-532); Lei 12.651/2012 art. 4º §1º e §4º (planalto.gov.br recusou conexão em 01/10/2026; usada a regra municipal equivalente, LC 270 Art. 215 §2º, já confirmada); Decreto 51.503/2022 Arts. 26-27 (no acervo, não relido por Bardi — apoio na decisão auditada de Kelsen de 28/07/2026).

## 8. Fatos reservados para etapas futuras (não revelar antes da etapa indicada)

Propostas de Bardi, a confirmar na montagem de cada etapa conforme o que a Etapa 01 aprovada de fato produzir:
- **Etapa 03 (Levantamento):** levantamento do espelho d'água e régua de maré passam a existir como documento do dossiê; o resultado fica definido na montagem da Etapa 03, coerente com o que a Etapa 01 pediu.
- **Etapa 04 (Briefing):** D. Lourdes cadeirante obriga suíte e rota acessíveis (NBR 9050) — já está no caso base; o cliente vai tentar cortar a suíte do térreo para caber o programa.
- **Etapa 07 (Entrada simulada):** a Comissão de Obras do condomínio devolve com exigência sobre altura (8,50 m medidos da soleira, não do meio-fio).
