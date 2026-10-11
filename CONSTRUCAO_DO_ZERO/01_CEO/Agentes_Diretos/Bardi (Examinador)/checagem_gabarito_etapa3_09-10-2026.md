# Checagem de gabarito — Etapa 03 (Levantamento) — Ensaio Sombra 003

**Data:** 09/10/2026 · **Autor:** Bardi (Examinador) · **Pendência:** bardi-gabarito-g4-isca2-08-10
**Gabarito conferido (NÃO alterado, lacre preservado):** `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi/ensaio_003/etapa_03_gabarito.md`
**Regra:** erro de gabarito é registrado aqui, não reescrito no lacre. Não desconta de Oscar nem de Lúcio.

## 1. Fontes lidas nesta checagem (caminho + página do PDF)

| Sigla | Documento | Caminho | Páginas lidas |
|---|---|---|---|
| COES | LC 198/2019 (COES), acervo | `D:\008_Normas ABNT\002_Prefeitura_RJ\COE LC 198-2019 Codigo de Obras e Edificacoes do Rio.pdf` | p. 6 (Art. 8 §§1–2 e Art. 8 caput); p. 7 (Art. 8 §4); p. 15 (Arts. 22–24, lido só para conferir a referência antiga); p. 19 (Art. 29 I–III); p. 21 (Art. 31 caput, I–VI, p.ú.) |
| D3046 | Dec. 3.046/81 + Instruções Normativas | `CONSTRUCAO_DO_ZERO\01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf` (não está em `D:\008`) | pp. 2–3 (Cap. II, Disp. Gerais VI, VII, X, XI) |
| LC270 | LC 270/2024 (Plano Diretor/LUOS) | `CONSTRUCAO_DO_ZERO\01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\LC270_2024_PlanoDiretorLUOS.pdf` | PDF p. 125 (Art. 350 I–VIII) |
| DULI | Dec. 55.622/2025, Anexo I (modelos) | `...\Fontes_Legislacao\Decreto55622_2025_AnexoI_ModelosDULI.pdf` | pp. 1–2: são só desenhos-modelo; **o texto do item 1 não aparece** |
| Dossiê | Enunciado da etapa 3, dossiê 5.1, 5.2, 5.4 | `CONSTRUCAO_DO_ZERO\01_CEO\Casos_TESTE\ensaio_003\etapa_03_levantamento\enunciado.md` | fonte do caso, não primário |

## 2. Tabela isca a isca

| Isca (gabarito) | Erro | Conta/leitura refeita | Saída | Fonte + página | Status |
|---|---|---|---|---|---|
| **Isca 1** — varanda sobre recuo frontal | **G1** | Sem conta numérica. Leitura do inciso aplicado. | O gabarito manda aplicar o **VII** (vedação de balanço frontal). Mas o próprio VII termina: "Nos casos de edificações residenciais unifamiliares será aplicado o disposto no inciso **XI**". O XI só trata de **afastamentos laterais do térreo** ocupados por varanda ou abrigo, não de balanço frontal. A conclusão "balanço frontal vedado para esta casa" não se sustenta pelo texto. | D3046 VII (p. 2 fim, p. 3 início); D3046 XI (p. 3). COES Art. 8 §1 (p. 6): varanda sobre o frontal pode ocupar a fachada, recuo mínimo 1 m da testada. COES Art. 8 §4 (p. 7): varanda em balanço ou reentrante não computa na ATE nem na TO. | **G1 CONFIRMADO.** Leitura do VII × XI em aberto (Skill decreto3046, M3, Gate do Maurício). Erro de página no gabarito: "COES Art. 8º §2º, p. 5" → é **p. 6**. Art. 8 §2 (2,50 m) está correto. |
| **Isca 2** — muro vizinho, 571,80 × 600 | **G4** | Frente 14,30 m × 40,00 m = **572,00 m²** (não 571,80, como diz o dossiê 5.2). Matrícula 15,00 × 40,00 = 600,00. TO 40% × 571,80 = 228,72 (bate com a premissa Legal). Envelope premissa do gabarito (frontal 6, laterais 2,50, fundos 5): largura = 15,00 − 2×2,50 = 10,00; profundidade = 40 − 6 − 5 = 29; 10 × 29 = **290,00**. Com frente 14,30: largura = 14,30 − 5,00 = 9,30; 9,30 × 29 = **269,70**. Perda = 0,70 × 29 = **20,30 m²**. | O gabarito diz "envelope cai para 170–190 m²" e usa "5,8 × 29 = 168". O 5,8 vem de 14,30 − 6 − 2,50: subtrai o frontal da largura e só um lateral. A perda real é ~20 m², não ~100 m². A fórmula impressa "(15 − 5 − 2,50 − 2,50) × (40 − 6 − 5)" dá 5 × 29 = 145, não 290. | Premissa de frontal/fundos/laterais: dossiê 5.4 (condomínio), não primário. Laterais 2,50: dossiê 5.4. TO 40%: dossiê 5.4. COES Art. 31 p.ú. (p. 21): 1,50 m mínimo para unifamiliar, piso legal, não o do condomínio. | **G4 CONFIRMADO.** Dossiê inconsistente: 14,30 × 40 = 572,00 ≠ 571,80 (erro de enunciado, meu, a registrar). Não verificado: texto do item 1 do Anexo I (ver §3). |
| **Isca 3** — edícula 0,80 m da divisa | sem erro de conta | 0,80 m < 1,50 m (COES p.ú.) e < 2,50 m (condomínio, dossiê 5.4). A violação se mantém com qualquer um dos dois limites. | Conclusão do gabarito (demolição recomendada, violação de afastamento) está **correta**. | COES Art. 31 p.ú. (p. 21): "afastamentos laterais ... de edificações unifamiliares ... quando exigidos, serão de, no mínimo, um metro e cinquenta centímetros". | **Correta na conta.** Erro de página: gabarito cita "Art. 31 p.ú., p. 17" → é **p. 21**. Código Civil art. 1.301 (1,50 m para janela): não verificado (ver §3). |
| **Isca 4** — garagem consome projeção | **G2** | Premissas do gabarito, 4 vagas: 228,72 − 60 = 168,72; × 2 pav = 337,44; + 70 (varanda/técnica) = **407,44**; 520 − 407,44 = **112,56 faltam**. 6 vagas: 228,72 − 90 = 138,72; × 2 = 277,44; + 50 = 327,44; falta **192,56**. | O gabarito diz "407 cabe em 520, com folga de ~100 m²" para 4 vagas. Contradição aritmética: 407 < 520, falta 113. A conclusão "4 vagas: programa cabe" é **falsa pela própria conta**. A "resposta aceitável" tem o mesmo erro (folga ~120). | LC270 Art. 350 III (PDF p. 125): só **uma** vaga coberta fica fora da projeção, então vagas 2 em diante entram na projeção. Premissa do gabarito suportada. Vaga = 15 m² no gabarito: **sem fonte** (lição do Bardi, v5). COES Art. 29 I (p. 19): vaga 2,50 × 5,00 = 12,50 m². | **G2 CONFIRMADO.** Sensibilidade (não é a resposta oficial): 4 vagas, 1 excluída, 15 m² → falta 82,56; 4 vagas, 12,50 m², sem exclusão → falta 92,56; 4 vagas, 12,50 m², 1 excluída → falta 67,56. **Em nenhuma combinação 520 cabe com 4 vagas.** Manobra (Art. 29 II, p. 19) não contada: R6 reprovada em 08/10, Gate pendente. Ponto de julgamento: quais m² do programa 520 são computáveis (regime de medição), que o gabarito não fixou. |

## 3. Referências de página corrigidas (não são conta, mas o parecer cita)

- **COES Art. 29 I–III: p. 19** (lido). A referência "Art. 29 III, p. 15" dos pareceres v7 e v8 está **errada**: p. 15 contém os Arts. 22–24 (lido). Erro meu, já registrado no estado.
- **COES Art. 31 (caput, III, IV, p.ú.): p. 21** (lido). Gabarito diz p. 17.
- **COES Art. 8 §2º: p. 6** (lido). Gabarito diz p. 5 (p. 5 contém o Art. 5).

## 4. Fonte primária não verificada nesta checagem

- **Anexo I do Dec. 55.622, item 1** ("medidas locais quando houver divergência"): não localizado. O PDF do Anexo I é só o modelo gráfico. Ler o texto do Decreto 55.622 (`Decreto55622_2025_LICIN2.0.pdf` na mesma pasta) em rodada própria.
- **Código Civil art. 1.301** (Isca 3, 1,50 m): não está no acervo `D:\008`, nem no excerto do Hely (`CodigoCivil_Lei10406_2002_ExcertoCompraVenda_Art481-532`, que só cobre arts. 481–532).
- **Dossiê 5.4** (afastamentos 6,00/2,50/5,00 e TO 40% do condomínio): é regulamento de condomínio, não primário. Não consta no acervo nem no Hely.
- **Dec. 3.046 e LC 270**: estão no acervo do Hely (`Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao`), **não** no `D:\008`. A Rotina Acervo de Normas deve copiá-los para `D:\008`.
- **Vaga de 15 m²** (gabarito, Isca 4): sem fonte. Não usar como número de conta.

## 5. Resumo

- Erros confirmados no gabarito: **G1 (Isca 1), G2 (Isca 4), G4 (Isca 2)**.
- Erros de página no gabarito: COES Art. 8 §2º (p. 6), COES Art. 31 p.ú. (p. 21).
- Erro novo, não estava em pendência: a fórmula impressa do envelope (Isca 2) é aritmeticamente errada, e a "resposta aceitável" da Isca 4 inverte a conclusão.
- Erro de enunciado meu (dossiê): 14,30 × 40 = 572,00, não 571,80.
- Gabarito não reescrito. Registro para Claudemberg decidir se mantém lacrado com errata ou se arquiva (ver `criterio-erro-gabarito-vs-nota-08-10`).
