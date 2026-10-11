# TREINO DE SKILL — CASO FICTÍCIO (não é cliente real)

**Skill:** `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj` (v1.1, ativa-com-ressalva)
**Data:** 29/09/2026 — Rotina Diária v3.4.0, Passo 4.7 (treino obrigatório em caso fictício, decisão de Claudemberg 28/09).
**Montado por:** Wallenberg (caso e iscas) / Lúcio (conferência) | **Executado por:** Oscar (sem web, sem Revit, sem ver as iscas)

## 1. Caso (FICTÍCIO)
Casa "Marapendi-V", Recreio, lote de frente para a lagoa a oeste. Sala com 36 m² de piso; cliente quer pano de vidro de 16 m², piso a teto, fachada oeste, "sem brise, para não atrapalhar a vista". Pé-direito duplo de 7,80 m. Fornecedor oferece "vidro refletivo prata FS 0,18, TL 12%" e diz "com esse vidro passa em qualquer norma". Cliente quer etiqueta PBE "A".
Perguntas: (1) Pt,APP e o significado no prescritivo; (2) vidro e pé-direito cabem no simplificado?; (3) o vidro resolve?; (4) proposta no EP; (5) ressalvas.

Iscas plantadas (não reveladas a Oscar): FS 0,18 < 0,20 e pé-direito 7,80 > 7,50 m (ambos mandam para simulação); TL 12% ameaça iluminação do COES; "sem brise" no poente contraria a Skill de proteção solar (vertical/AHF); 17%/0,87/5,70 vêm de minuta; zona bioclimática não confirmada; INI-R voluntária × NBR 15575 obrigatória (R3).

## 2. Resposta do Oscar (resumo fiel)
1. Pt,APP = 16/36 = 44% contra ~17% da referência (§2, §5). Não atende ao prescritivo, que não enxerga FS nem sombra; não é reprovação, passa para outro método (§3.1). O prescritivo chega no máximo à classe C, então nunca daria a "A" (§2).
2. Não cabe no simplificado por dois critérios: FS 0,18 < 0,20 e pé-direito 7,80 > 7,50 m (Tabela 6.1, §2) → simulação (Anexo C, §5). U do vidro não informado, critério não conferível.
3. Vidro não resolve: "passa em qualquer norma" sem base; falta U e laudo do vidro composto (§4.1); TL 12% escurece e ameaça a iluminação do COES (§4.2, Skill `coe-lc198-...`); o FS baixo é o que tira a sala do simplificado; refletivo prata muda a imagem, render do Burle com o vidro real (§4.4).
4. EP: avisar que a comprovação será por simulação, com custo de consultoria na proposta (§3.4); ordem do §3.3 — sombreamento vertical no poente (brise vertical espaçado/móvel que preserva a vista) ou empenas/varanda reentrante até 1,50 m não computável (`lucio-protecao-solar` §2, `varandas-nao-computaveis`); depois vidro de controle solar FS ≥ 0,20 e TL compatível com COES, FS/TL/U de catálogo (§4.1–4.2); reduzir área só por último; não prometer etiqueta "A"; "sem brise" fica como decisão informada e registrada do cliente.
5. Ressalvas: R1 (0,87/5,70/17% da minuta, confirmar na NBR 15575-1 §11.4.7.2); R2 (zona da INI-R para o Rio, 8 zonas × indício 4A, `nbr15220-3`); R3/R4 (INI-R voluntária × NBR 15575 obrigatória; passar na etiqueta não comprova a 15575; obra nova pode precisar de simulação de qualquer forma); Skill sem FS de produto comercial (§4.5); tudo preliminar até o Gate do Maurício.

Obs.: a resposta passou um pouco das 15 linhas pedidas (formatação em sublistas); conteúdo não inflado. Oscar registrou a execução no próprio estado (liberado desta vez).

## 3. Veredito do Lúcio: OK
Pegou as 6 iscas, todas com seção citada: FS < 0,20 e pé-direito > 7,50 (os dois, não só um); TL × COES; "sem brise" contrariando o poente vertical/AHF, com alternativa que preserva a vista em vez de ceder; valores de minuta (R1); zona não confirmada (R2); INI-R × NBR 15575 (R3/R4). Acrescentou pontos corretos não pedidos: prescritivo teto classe C (etiqueta "A" impossível por esse caminho), U ausente na oferta do fornecedor, render com o vidro real, Gate do Maurício. Nenhum número inventado.

## 4. Correções sugeridas à Skill (não editadas)
Nenhum erro de conteúdo apareceu; só lacunas de checklist que o Oscar cobriu por conta própria e um Agente menos atento poderia pular:
- §5 (checklist): acrescentar item "TL do vidro compatível com a iluminação natural exigida pelo COES" — hoje o alerta está só no §4.2, e o checklist pede TL mas não diz contra o quê conferir.
- §5 (checklist): acrescentar item "cliente quer etiqueta A/B? O prescritivo não serve (teto classe C) — avisar no EP". Está na tabela do §2, mas não vira passo de verificação.
- §3 ou §5: uma linha para o caso "cliente recusa sombreamento": registrar como decisão informada do cliente, com a consequência (simulação/classe menor) declarada, em vez de premissa silenciosa.
- §3.2: explicitar que FS abaixo de 0,20 não "melhora" a avaliação no simplificado — tira o ambiente dele (o texto do §2 já diz, mas o §3.2 sugere "FS menor" sem o piso de 0,20).
