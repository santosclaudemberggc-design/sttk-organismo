# Anexo 06. Declaração de leitura, bloqueios e checklist (a) a (e)
## Ensaio Sombra 003, Montenegro Prates (caso 100% FICTÍCIO). Oscar, 13/10/2026, v4

Caso fictício. Não consultei órgão real. Nada foi protocolado, enviado a prefeitura, condomínio ou concessionária.

---

## 1. Declaração de leitura (só o aberto nesta execução, por caminho)

Caminhos completos: a base é `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\CONSTRUCAO_DO_ZERO\`. Todos os caminhos abaixo partem dela.

**Entradas do Briefing (lidas inteiras):**

1. `01_CEO\Casos_TESTE\ensaio_003\etapa_04_briefing\enunciado.md`
2. `01_CEO\Casos_TESTE\ensaio_003\etapa_03_levantamento\entrega\v8\01_levantamento_planialtimetrico_cadastral_DULI_003_v8.md`
3. `01_CEO\Casos_TESTE\ensaio_003\etapa_03_levantamento\entrega\v8\02_relatorio_condicionantes_limitacoes_003_v8.md`
4. `01_CEO\Casos_TESTE\ensaio_003\etapa_03_levantamento\entrega\v8\03_matriz_decisoes_pendentes_003_v8.md`
5. `01_CEO\Casos_TESTE\ensaio_003\etapa_03_levantamento\entrega\v8\anexo_contas_003_v8.md`

**Estado do próprio Agente (lido, não é fonte de premissa):**

6. `01_CEO\Gestores\Lúcio (Arquitetura)\Agentes\Oscar\_estado_oscar.md` (lido inteiro, em duas partes)

**Skills (carregadas pela Skill tool; conteúdo lido nesta execução):**

7. Skill `nbr6492-2021-memoriais-por-etapa-projeto` (fonte secundária da NBR 6492:2021)
8. Skill `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj` (v1.6, changelog de 10/10/2026)
9. Skill `varandas-nao-computaveis-ate-to-coes-lc198-rj`
10. Skill `decreto3046-81-lc270-2024-licin-barra-recreio`

**Cópias legais do acervo (fontes primárias, lidas por página, `01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\`):**

11. `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`, páginas 5, 15 e 17.
12. `LC270_2024_PlanoDiretorLUOS.pdf`, páginas 124, 125, 126 e 130.
13. `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`, páginas 2, 3 e 4.

**Listagem (só nomes, nenhum arquivo aberto):**

14. Glob em `CONSTRUCAO_DO_ZERO` por `**/Fontes_Legislacao/*.pdf`, rodado nesta execução (ajuste de 13/10/2026). Retornou 40 caminhos, todos em `01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\`. **Declaração:** nenhum nome retornado pertence à pasta do ensaio (`01_CEO\Casos_TESTE\ensaio_003\`) nem ao examinador (`01_CEO\Agentes_Diretos\Bardi (Examinador)\`). **Correção à declaração de que nenhum foi aberto:** dois desses 40 foram abertos nesta execução, por página, para conferir o texto de D2: `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` p. 17 e `LC270_2024_PlanoDiretorLUOS.pdf` p. 125 (itens 11 e 12). Os outros 38 não foram abertos. **Base:** comparei os 40 nomes da listagem desta execução com os dois prefixos. **Não verifiquei:** se o Glob listou tudo o que existe em `CONSTRUCAO_DO_ZERO` (a ferramenta não informa limite); pastas fora de `CONSTRUCAO_DO_ZERO`; o conteúdo dos arquivos (só nomes); nem a lista do Glob da execução anterior, que não guardei.

**Ferramenta Revit (leitura de status, sem escrita):**

15. `mcp__vitruvius__vitruvius_get_revit_status`, uma chamada.

**Não abri nesta execução (declaração explícita):**

- Nenhum arquivo de gabarito.
- Nenhum parecer de correção do examinador (Bardi).
- Nenhuma entrega antiga da Etapa 04 (`entrega/`, `entrega/v2/`, `entrega/v3/`). Os arquivos `_v2` e `checagem_oscar_v2.md` existentes na pasta v2 não foram abertos nem alterados.
- Nenhuma outra versão da Etapa 03 (v1 a v7).
- Nenhum parecer da Etapa 01 (Hely), nenhum Regramento do condomínio, nenhuma Viabilidade (Villaça v9) e nenhuma errata: o que sei delas vem do Resumo do enunciado e das peças da Etapa 03 v8, e está marcado como dossiê ou [nv].
- Nenhum Anexo XXI da LC 270, nenhum LC 270 Art. 215 e 278, nenhum COES Art. 28 ou 35, e do Art. 8º só os §§1º, 2º, 4º, 6º e 8º, nenhum texto da NBR 6492, NBR 9050 ou lei federal de acessibilidade.

---

## 2. Bloqueios e ferramentas

| # | Bloqueio | Literal ou detalhe | Efeito |
|---|---|---|---|
| B-1 | Revit (Vitruvius): status | `mcp__vitruvius__vitruvius_get_revit_status` retornou: **"Error: Plugin não está conectado"**. A ferramenta existe; o plugin não está ativo na sessão. | Não houve desenho nem simulação. Esta etapa não tem desenho, então o bloqueio não afeta o Briefing. Registrado para Lúcio |
| B-2 | NBR 9050:2020 | Não está no acervo local. Não lida. | Dimensões de acessibilidade "a definir" (02 §1, 03 §4). Pendência P-m |
| B-3 | NBR 6492:2021 (texto integral) | Só a Skill (fonte secundária) foi lida. Itens 5.2, 5.2.1 e 5.2.2 vêm da Skill | Toda citação da norma é [nv], com a Skill como fonte |
| B-4 | Lei federal de acessibilidade | Não lida | Enquadramento da suíte térrea: P-m (Kelsen) |
| B-5 | LC 270 Anexo XXI (TO por zona) | Não lido | SMD: não é possível confirmar qual TO vale. P-SMD (Kelsen) |
| B-6 | Regramento do condomínio (Art. 6º, 7º, 8º, 12) | Não lido. Conteúdo vem do Resumo do enunciado e da Etapa 03 v8 (dossiê) | Citações do Regramento são "dossiê" |
| B-7 | Contagem de palavras | Sem ferramenta de contagem nesta execução | "Contagem não feita, a ser feita por Wallenberg com ferramenta." |
| B-8 | Metragens por ambiente | Não constam nas entradas autorizadas | Planilha com "a definir". Não procurei em outro lugar |
| B-9 | Gate da Coordenação | Pendente de Claudemberg | Nada é entregável final |
| B-10 | Esquemas em escala (PN-ARQ 5.2.1 b) | Não são desenho, mas representação gráfica. Adiados para a Etapa 05 | Gráficos em texto e tabela nesta entrega. Dono Oscar e Lúcio |
| B-11 | Ferramentas de escrita, de cliente e de comunicação | Não usei nem contatei ninguém | Perguntas em pendências com dono; Lúcio escala |

---

## 3. Checklist (a) a (e), com prova

### (a) SMD: divergência exposta, não resolvida

Prova, em duas leituras, com a divergência:

- **Leitura A (enunciado, Resumo):** "Superfície Mínima Drenante (SMD): 10% do terreno". 0,10 × 571,80 = **57,18 m²** (`05_anexo`, E-6).
- **Leitura B (LC 270 Art. 352, caput, cópia `LC270_2024_PlanoDiretorLUOS.pdf`, p. 125):** texto verbatim: "A SMD corresponde a vinte por cento da área livre do terreno resultante da aplicação da Taxa de Ocupação máxima, definida no Anexo XXI desta Lei Complementar." Área livre = 571,80 − 228,72 = 343,08; 0,20 × 343,08 = **68,62 m²** (`05_anexo`, E-7).
- **Divergência:** 68,62 − 57,18 = 11,44 m². Expostas em: `01_corpo` §0 item 4 e §6 (P-SMD); `04_matriz` T-01; `05_anexo` T-2.
- **Não copiei 57,18 como resultado.** A TO é 40% (Resumo; 228,72 = 40% × 571,80). O exemplo de 57,18 do checklist corresponde a TO de 50% (E-8, sensibilidade, não é premissa).
- **Pendência:** P-SMD para Kelsen: qual TO e qual base valem para a SMD. O Art. 352 remete ao Anexo XXI, não lido.

### (b) Regime: H1 e S3 rotulados na E-13

- E-13 da `05_anexo` rotula cada grandeza com P, C ou Co, incluindo H1 (envelope 148,64 P; teto 297,28 C) e S3 (297,28 C; 340–360 Co).
- A `01_corpo` §2 cita E-12 e E-13 em cada afirmação de H1 e S3.
- Nenhum "atende" de regime foi escrito sem cruzar com a E-13. A conclusão "340–360 não tem espaço físico" depende de E-13 e E-23.

### (c) Organograma legível, além de ASCII

- `03_organograma_esquemas_003_v4.md` §2: tabela de fluxos (pessoas, visitas, serviço, carro, acesso de D. Lourdes), com origem, destino, requisito, condição e dono.
- `03_organograma_esquemas_003_v4.md` §3: matriz de relações funcionais, com marcação R, D e —, em tabela.
- `03_organograma_esquemas_003_v4.md` §4: caracterização de cada ambiente em tabela.
- Não há gráfico de imagem nesta entrega. Os esquemas em escala ficam para a Etapa 05 (B-10).

### (d) Não computável: cada item com artigo

Exemplos com artigo e página (tabela completa em `01_corpo` §4 e `02_planilha` §1 e §2):

- **Garagem, 1 vaga coberta fora da TO:** LC 270 Art. 350 III, p. 125, texto: "estacionamento coberto nos termos do Código de Obras e Edificações Simplificado, nas edificações uni e bifamiliares, limitado a uma vaga".
- **Garagem, acesso e manobra fora da ATE:** LC 270 Art. 347 II, p. 124, texto: "locais cobertos e descobertos destinados à vagas de estacionamento e guarda de veículos, inclusive seus acessos e áreas de manobra".
- **Varandas em balanço ou reentrantes:** COES Art. 8º §4º, p. 5, texto: "as varandas e sacadas de unidades residenciais, quando em balanço ou reentrantes, não serão computadas na Área Total Edificável – ATE e na Taxa de Ocupação." Sujeita ao conflito frontal (ver a linha "Varanda sobre o afastamento frontal" na `01_corpo` §4).
- **Saliência de jardineira e ar-condicionado:** Dec. 3.046 XIV, p. 3, até 0,40 m, acima do térreo, fora da ATE e da TO.
- **Laje técnica de ar-condicionado:** COES Art. 8º §8º, p. 5, até 1,00 m do plano da fachada.
- **Piscina descoberta na faixa frontal:** LC 270 Art. 363 §2º V, p. 130. Regime de cômputo na TO não lido: pendência P-piscina, sem artigo de cômputo, portanto não listada como não computável.
- **Déficit de 62,56 m² (520 − 457,44):** não é item não computável. Aparece como déficit (`01_corpo` §4, última linha; `02_planilha` §2; `05_anexo` E-11).
- **Edícula:** não é não computável. Dec. 3.046 XV, p. 3, computa na ATE e na TO. Conflito com LC 270 Art. 350 IV, p. 125 (P-edícula).

### (e) Cópia citada: artigo, página e nome da cópia lida

Formato usado: "[lei] Art. X, p. N, cópia [nome do arquivo]". Todas as citações abaixo foram abertas nesta execução (página no PDF):

| Citação | Cópia lida | Página | Texto (verbatim, parcial) |
|---|---|---|---|
| COES Art. 8º §1º | `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` | p. 5 | "Sobre o afastamento frontal, as varandas e sacadas poderão ocupar toda a fachada e deverão recuar, no mínimo, um metro da testada do terreno." |
| COES Art. 8º §2º | idem | p. 5 | "...deverão distar, no mínimo, dois metros e cinquenta centímetros das divisas laterais e de fundos do lote." |
| COES Art. 8º §4º | idem | p. 5 | ver item (d) |
| COES Art. 8º §6º | idem | p. 5 | churrasqueiras integradas à fachada, vazados com aeração de 50% |
| COES Art. 8º §8º | idem | p. 5 | "...com distância máxima de um metro..." |
| COES Art. 29 I, II, III, IV | idem | p. 15 | vaga 2,50 × 5,00 (paralela 2,50 × 6,00); manobra 2,50 × 5,00; III limiar de 25 m²; IV faixa 2,50 m |
| COES Art. 31 caput, I, II, III, V e p.u. | idem | p. 17 | "dispensadas das seguintes exigências" (I área mínima; II dimensões; III vagas; V acessibilidade); p.u.: afastamentos laterais "quando exigidos" de no mínimo 1,50 m |
| COES Art. 31 IV | idem | p. 17 | dispensa (caput: unifamiliares e bifamiliares) do "afastamento frontal, para estacionamento coberto de veículos, em telha vã, com um pavimento de altura" |
| LC 270 Art. 347 II | `LC270_2024_PlanoDiretorLUOS.pdf` | p. 124 | ver item (d) |
| LC 270 Art. 350 III e IV | idem | p. 125 | ver item (d) |
| LC 270 Art. 350 I e II | idem | p. 125 | II: "as varandas e terraços assentes no terreno, para as edificações uni, bifamiliares e multifamiliares"; I: "áreas em balanço destinadas a varandas, sacadas, saliências e marquises nos termos do Código de Obras e Edificações Simplificado" |
| LC 270 Art. 352 caput, §§2º–4º | idem | p. 125 | ver (a) |
| LC 270 Art. 353 III e §4º | idem (p. 126) | p. 126 | porções ≥ 4 m² e nenhuma dimensão < 2 m; "Não será admitida nas SMD a implantação de subsolos." |
| LC 270 Art. 363 §2º V, VII, XII e §3º | idem | p. 130 | piscina descoberta; varandas balanceadas "até o limite estabelecido pelo COES"; estacionamento apenas em uni e bifamiliares "nos termos do COES"; rampas ≤ 10% e ≤ 0,50 m |
| Dec. 3.046 VII | `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf` | p. 2 | "Nos casos de edificações residenciais unifamiliares será aplicado o disposto no inciso XI." |
| Dec. 3.046 X | idem | p. 2 | lotes de 6ª e 7ª categoria anteriores a 1969 (não aplicado ao caso) |
| Dec. 3.046 XI | idem | p. 3 | "Nas edificações de uso residencial unifamiliar, com afastamento frontal inferior a 10,00 m, os afastamentos laterais no pavimento térreo poderão ser ocupados por varandas ou abrigos de veículos, desde que abertos e cobertos por telha-vã..." |
| Dec. 3.046 XIV | idem | p. 3 | saliências, até 0,40 m, acima do térreo |
| Dec. 3.046 XV | idem | p. 3 | edícula de até 2 pavimentos computada na ATE e na TO |
| Dec. 3.046 XXI, XXII, XXIII a | idem | p. 4 | XXII: "excetuada aquela do afastamento frontal mínimo obrigatório"; XXIII a: "com exclusão das áreas de afastamento mínimo frontal obrigatório" |

**Citações sem cópia lida, marcadas [nv]:** COES Art. 28 II (pé-direito, via Skill); COES Art. 35 §§2º–3º (via Skill); LC 270 Art. 215 §2º (via Etapa 03 v8); LC 270 Art. 278 XIV (via Etapa 03 v8); LC 270 Art. 458 (via Etapa 03 v8); NBR 6492:2021 (via Skill); NBR 9050:2020 (não está no acervo: "2020 não lida, pendente"); lei federal de acessibilidade (não lida); Regramento do condomínio Art. 6º, 7º, 8º e 12 (dossiê, Resumo e Etapa 03 v8).

---

## 4. Verificação de forma (regra da Etapa 04, 13/10)

- Corpo (`01_corpo`): não há estimativa de palavras. Declarado "contagem não feita, a ser feita por Wallenberg com ferramenta" (corpo, cabeçalho e §7).
- Remissões do corpo para os anexos (02, 03, 04, 05): conferidas por Grep de "Anexo 03-E" e "E-N" nesta entrega. Os resíduos de "Anexo 03-E" foram trocados por "Etapa 03, Anexo E, item N", para não confundir com os anexos desta entrega.
- Os anexos 02 a 05 usam a numeração própria (E-n na 05; A1 a A15 na 02; M-, P-, T- na 04). Não há mais número solto sem dono ou sem fonte.

---

Oscar, 13/10/2026 (v4)
