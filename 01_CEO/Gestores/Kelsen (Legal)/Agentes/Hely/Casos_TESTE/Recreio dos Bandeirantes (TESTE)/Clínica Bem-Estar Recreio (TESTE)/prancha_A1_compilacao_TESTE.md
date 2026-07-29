---
status: TESTE — não é cliente real
caso: 3
data_teste: 2026-07-15
gestor: Kelsen
executor: Hely
referencia_pop: POP-ARQ-PL-01 (POP – PROJETO LEGAL, ARQUITETURA) + MEMORIAL DESCRITIVO - Projeto Legal + Planilha de Enviáveis Externos
---

# ⚠️ CENÁRIO DE TESTE — NENHUM DADO AQUI É REAL

Compilação descritiva da prancha do Projeto Legal em formato A1, para o caso-teste Clínica Bem-Estar Recreio (TESTE). Como é teste fictício, sem pranchas reais em CAD/Revit do Anteprojeto, este arquivo descreve **estrutura, layout e conteúdo de cada folha**, exatamente como eu organizaria a compilação real se as pranchas AP-TESTE-2026-020 a 027 existissem em arquivo. Não desenhei nada do zero — a origem de todo o conteúdo geométrico é o Anteprojeto do Estúdio Bruma Arquitetura (parceiro externo, PRPA candidato), que preciso adequar ao padrão legal, não alterar.

## Conferência prévia (Seção 7.2 do POP) — feita antes de organizar a prancha

**⚠️ CORREÇÃO REGISTRADA EM 15/07/2026 — ERRO DE ZONEAMENTO CONFIRMADO POR CLAUDEMBERG.** Esta conferência foi originalmente feita (14/07/2026) sobre a zona **ZRM3 subzona O**, que era um **erro de consulta** — corrigido para **ZRM2 subzona G**, fonte: RIU oficial (`mapas.rio.rj.gov.br`)/print de Claudemberg, mesmo CL 476218. Mantenho abaixo o registro do que mudou, sem apagar o histórico (Princípio 8 — Rastreabilidade). Ver causa raiz completa em `processo_legal_teste.md` (item 1/3) e em `Fontes_Legislacao/_indice_fontes.md`.

Antes de compilar, confirmei (valores reais, ZRM2 G):
- **Recuo frontal**: 5,00 m proposto = exatamente o mínimo exigido para ZRM2 G/AP4 (Art. 363/Anexo XXI-equivalente, confirmado via camada oficial `LBB_Zoneamento_urbano_vigente`, campo `AFAST_FRON`: 5 — este valor bateu tanto na consulta errada quanto na real). **Conforme.**
- **Gabarito**: 11,80 m pretendido. Na subzona real (ZRM2 G), o limite é **4pav/14m nos dois regimes** (afastado e não afastado — sem vantagem de gabarito por se afastar das divisas, diferente do que a consulta errada de ZRM3 O indicava: 8pav/26m afastado vs. 3pav/11m não afastado). O gabarito pretendido cabe folgadamente sob 14 m em qualquer um dos dois regimes — **não há mais obrigatoriedade de adotar o regime "afastado das divisas"** só por causa do gabarito. Ainda assim, **o pacote não me forneceu o recuo lateral/de fundos proposto pelo Anteprojeto** — não posso confirmar conformidade com o mínimo geral do COES (LC 198/2019, Art. 4º: 2,50 m ou 1/5 da altura) sozinho. **Sinalizado como pendência ativa, com risco reduzido em relação ao registro anterior, mas não eliminada.**
- **Coeficiente de aproveitamento — ACHADO GRAVE, reavaliado em 15/07/2026**: CAM real = **1,0** (não 2,0 como constava). **CAM 1,0 × 500 m² = 500 m² máximo permitido.** Área pretendida 980 m² (bruta, antes de exclusões de subsolo não aflorado da ATE, Art. 346-347 LC 270/2024) — **quase o dobro do limite legal (980 ÷ 500 = 1,96x), não conformidade grave de coeficiente de aproveitamento**, não é mais "dentro do limite com folga pequena" como o registro original (sobre o CAM 2,0 errado) concluía. Isso não é ajuste fino de prancha — é achado que precisa ser resolvido no dimensionamento do projeto antes de qualquer compilação final. Ver reavaliação completa da contrapartida/ICS no processo principal (item 1/3): a situação agora é de **estouro de CAM**, não de uso de faixa de contrapartida entre CAB e CAM.
- **Taxa de Ocupação**: máx. **50%** (não 70% como constava) — 250 m² de projeção (não 350 m²). Não tenho a área de projeção horizontal do pavimento térreo no pacote para confirmar — **fica pendente de conferência quando as pranchas reais chegarem**, não presumo conformidade. Com o limite real mais baixo (50% em vez de 70%), esta conferência fica ainda mais crítica quando as pranchas chegarem.
- **Coerência plantas × áreas**: não aplicável ainda neste teste (sem pranchas CAD reais) — mas o Quadro de Áreas Legal abaixo já reflete o uso/vagas corrigidos do item 9 do processo, não os números originais do Anteprojeto.

**Itens que bateram entre a versão errada e a real (não eram o problema): afastamento frontal 5 m, lote mínimo 360 m², testada mínima 10 m.** O erro estava nos parâmetros de aproveitamento e gabarito.

**Registro (Princípio 8 — Rastreabilidade):** as pendências ativas (recuo lateral não informado — risco reduzido; TO não conferível, agora contra limite mais baixo; e o achado grave de estouro de CAM) vão junto no reporte a Kelsen — não fecho a prancha como "pronta para protocolo" enquanto elas não forem resolvidas com o Anteprojeto real em mãos, e o estouro de CAM em particular precisa de decisão sobre redimensionamento do projeto, não é uma pendência que se resolve só com documentação.

---

## Estrutura da prancha compilada — formato A1 (594 x 841 mm), múltiplas folhas

Adotei o padrão de 1 prancha A1 por conteúdo principal (não empilhar tudo numa única folha ilegível), com bloco de identificação padronizado (carimbo) repetido em todas as folhas — nome do projeto, endereço, requerente, PRPA, escala, data, nº da folha/total, código do projeto.

### Folha 01/09 — Capa e Índice + Planta de Situação
- Bloco de identificação completo (Requerente: Clínica TESTE-QA Bem-Estar Recreio Serviços Médicos LTDA.; Imóvel: Rua Escritor Elie Wiesel, 215, Recreio dos Bandeirantes — Matrícula 000.002-TESTE)
- Índice de folhas (lista as 9 folhas desta prancha)
- Planta de situação do lote (escala 1:500 ou 1:1000) — localização do lote no quarteirão, orientação norte, logradouros lindeiros, CL 476218
- Quadro-resumo dos parâmetros urbanísticos aplicados (**ZRM2 G/AP4** — corrigido de "ZRM3 O", erro de consulta de 14/07/2026, corrigido em 15/07/2026 para ZRM2 G, fonte: RIU oficial/print de Claudemberg; CAB/CAM/TO/gabarito/afastamento — tabela do processo principal), com nota de fonte (LC 270/2024 + Decreto 56.561/2025, via consulta oficial de 15/07/2026)

### Folha 02/09 — Implantação Legal
- Implantação do lote conforme código local (**ZRM2 G/AP4** — corrigido de "ZRM3 O", erro de consulta de 14/07/2026, corrigido em 15/07/2026, fonte: RIU oficial/print de Claudemberg): amarração do afastamento frontal (5,00 m, cotado); gabarito 4pav/14m em ambos os regimes (afastado e não afastado) — não há mais obrigatoriedade de adotar "afastado das divisas" só pelo gabarito, diferente do registro anterior; afastamentos laterais/fundos **com cota pendente de confirmação com o Anteprojeto real** (nota visível na prancha: "recuo lateral/fundos — CONFERIR contra Anteprojeto original; mínimo COES Art.4º = 2,50m ou 1/5 da altura, se exigido")
- Acesso de veículos (subsolo/garagem) e de pedestres (recepção)
- Nota de demolição: indicação da edificação existente a demolir (140,00 m², Alvará nº 00000-TESTE/2005) — **com selo "PENDENTE: confirmar com Kelsen se demolição tramita no mesmo DULI ou em processo próprio"**, para não passar a falsa impressão de que já está resolvido

### Folha 03/09 — Planta Legal do Subsolo (Garagem)
- Planta cotada do pavimento de garagem, vagas demarcadas e numeradas
- Nota de vagas: "quantitativo de vagas sujeito a análise de Polo Gerador de Viagens pela CET-Rio (LC 270/2024, Art. 368 §1º II) — NÃO usar as 10 vagas em padrão residencial do Anteprojeto original sem essa confirmação"
- Vaga(s) PcD demarcada(s) — mínimo 2% do total, ao menos 1 (COES Art. 29 §2º III)

### Folha 04/09 — Planta Legal do Térreo (Recepção/Farmácia)
- Planta cotada, acessos, recepção, farmácia, sanitários (ao menos 1 acessível, conforme NBR 9050)
- Hall e poço do elevador identificados — com nota: "cabine proposta 1,00x1,25m ABAIXO do mínimo NBR 9050:2020/NBR NM 313:2008 (1,10x1,40m) para uso não residencial/coletivo — pendente de correção antes do protocolo"

### Folha 05/09 — Planta Legal do Pavimento 1 (Consultórios)
- Planta cotada, distribuição dos consultórios, circulação, saída de emergência

### Folha 06/09 — Planta Legal do Pavimento 2 (Consultórios)
- Planta cotada, distribuição dos consultórios, circulação, saída de emergência

### Folha 07/09 — Cortes Legais (2 cortes exigidos)
- Corte AA (longitudinal) e Corte BB (transversal), cotados — pé-direito de cada pavimento, gabarito total cotado (11,80 m, com nota do regime "afastado das divisas" adotado), nível do subsolo

### Folha 08/09 — Fachadas Legais (2 fachadas)
- Fachada frontal (voltada para a Rua Escritor Elie Wiesel) e fachada lateral — para aprovação legal, preservando integralmente o partido arquitetônico do Anteprojeto do Estúdio Bruma (não alterado por mim)

### Folha 09/09 — Quadro de Áreas Legal (Anexo III) + Memorial + ARTs

**Quadro Explicativo de Áreas — Anexo III (edificação nova)**, já com uso reclassificado e observação de vagas (não os números originais do Anteprojeto):

| Pavimento | Descrição | Área (m²) | Uso (reclassificado) |
|---|---|---|---|
| Subsolo | Garagem | (a confirmar c/ Anteprojeto) | Uso de Serviços II (S-II) — apoio |
| Térreo | Recepção / Farmácia | (a confirmar c/ Anteprojeto) | Uso de Serviços II (S-II) / Comercial I (farmácia) |
| Pav. 1 | Consultórios | (a confirmar c/ Anteprojeto) | Uso de Serviços II (S-II) — CNAE 86.3 |
| Pav. 2 | Consultórios | (a confirmar c/ Anteprojeto) | Uso de Serviços II (S-II) — CNAE 86.3 |
| **Total pretendido** | | **980,00** | |

Nota na própria folha: "Uso enquadrado como Serviços II (S-II), CNAE 86.3 — Atividades de atenção ambulatorial executadas por médicos e odontólogos, conforme Decreto Rio nº 56.561/2025 (Anexo IV/AP4) c/c LC 270/2024 Art. 338 VIII. NÃO usar a expressão 'institucional de saúde' como categoria formal — não corresponde à nomenclatura legal (ver Art. 338 XVI, reservado a instituições públicas/assistenciais sem fins lucrativos)."

**Bloco de Memorial Descritivo** (resumo na própria folha, documento completo em arquivo separado — ver abaixo): descrição do uso, do partido arquitetônico preservado do Anteprojeto, dos parâmetros urbanísticos aplicados e das pendências declaradas.

**Bloco de ARTs/RRTs** — com destaque visual (moldura/selo) para a pendência:
- PRPA: Arqto. Fábio Noronha Salgueiro (Estúdio Bruma Arquitetura), CAU A000001-1-TESTE — **ART-TESTE-2026-0031 (emitida)** ✓
- PREO: **[ ] PENDENTE — "Construtora executora: A DEFINIR". Nenhuma ART/RRT emitida. NÃO PROTOCOLAR sem este campo preenchido."** — destaque vermelho/moldura de alerta, não apenas nota de rodapé, exatamente para não passar despercebido numa conferência rápida da prancha.

---

## Memorial Descritivo — Projeto Legal (resumo, documento-arquivo separado do POP)

Estrutura seguida (conforme Memorial Descritivo padrão de Legal):
1. Identificação do requerente e do imóvel
2. Situação atual (casa a demolir) e situação pretendida (clínica nova, uso Serviços II)
3. Parâmetros urbanísticos aplicados e fonte (**ZRM2 G/AP4** — corrigido de "ZRM3 O", erro de consulta de 14/07/2026 corrigido em 15/07/2026, fonte: RIU oficial/print de Claudemberg; LC 270/2024 + Decreto 56.561/2025)
4. Descrição do partido arquitetônico (preservado do Anteprojeto do Estúdio Bruma — não alterado)
5. Quadro de áreas (remete à Folha 09/09)
6. Responsáveis técnicos (PRPA confirmado; PREO pendente — destacado)
7. Pendências declaradas (demolição/processo, vagas PGV, elevador, AVCB) — mesma lista do processo principal, para o memorial não contradizer o dossiê

## Status desta compilação

**NÃO está pronta para protocolo.** Faltam, no mínimo, antes de eu poder fechar a prancha como final:
1. Recuo lateral/fundos real do Anteprojeto (conferência geral do COES — já não é mais condição obrigatória para o regime de gabarito, ver correção de 15/07/2026 acima, mas segue pendente de confirmação)
2. Área de projeção horizontal do térreo (para conferir TO, agora contra o limite real de 50%, não 70%)
3. Áreas reais por pavimento (hoje só tenho o total de 980 m² do pacote, não a discriminação por pavimento — usei "(a confirmar)" no quadro acima em vez de estimar)
4. Confirmação de vagas (CET-Rio/PGV) e correção do elevador (cabine)
5. PREO com ART/RRT
6. Resposta sobre AVCB
7. **NOVO (15/07/2026, achado grave) — Coeficiente de aproveitamento estourado**: CAM real 1,0 × 500 m² = 500 m² máximo permitido; projeto pretende 980 m² brutos, quase o dobro do limite legal. Isto **não é uma pendência documental que eu resolvo compilando a prancha** — é um achado de mérito que precisa de decisão de Kelsen (e possivelmente Wallenberg/Claudemberg) sobre redimensionamento do projeto ou busca de instrumento legal aplicável, antes de qualquer prancha ser considerada avançável. Ver detalhe no processo principal (item 1/3) e a contradição registrada com a simulação de "2ª submissão aprovada" (item 9 do processo).

Reporto tudo isso a Kelsen no reporte consolidado — não decido sozinho preencher essas lacunas nem o achado de estouro de CAM.
