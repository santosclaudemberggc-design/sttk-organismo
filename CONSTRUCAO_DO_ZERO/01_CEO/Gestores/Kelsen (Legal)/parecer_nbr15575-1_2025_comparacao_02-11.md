# Parecer Kelsen: NBR 15575-1, edição 2024 x edição 2025 (02/11/2026)

**Pedido:** Wallenberg, frente Construção do Zero. Comparar as duas edições nos pontos usados pelo Briefing v2 e pelas Skills.
**Quem leu:** eu (Kelsen), direto nos PDFs, por imagem de página. Não acionei o Hely: a ordem permitia ("ou leia você mesmo"), e a leitura era pontual.
**Não editei** o Briefing, as Skills, o Ensaio 003 nem o Drive. Não fiz commit.

## 0. Os dois arquivos e o total de páginas

| Edição | Arquivo | Total de páginas do PDF | Como confirmei |
|---|---|---|---|
| 2025 | `D:\008_Normas ABNT\001_ABNT\ABNT_NBR_15575_1_2025_Edificações_habitacionais_Desempenho_Parte.pdf` | **107** | Pedi as pp. 107-108 e veio só 1 página (a 107, com "95" no rodapé, fim da Bibliografia). A capa diz "95 páginas", e as 12 primeiras são romanas: 95 + 12 = 107. |
| 2024 | `D:\008_Normas ABNT\001_ABNT\ABNT NBR 15575-1-2024.pdf` | **107** | Pedi as pp. 102-110 e vieram só 6 (102 a 107). A p. 107 tem "95" no rodapé, fim da Bibliografia. Capa: "95 páginas". |

Nas duas, a página do PDF é a página da norma + 12.

**Identificação da 2025 (capa, PDF p. 1):** "Sétima edição 05.12.2025". A 2024 (PDF p. 1) diz "Sexta edição 23.01.2024". A cópia de 2024 é um download do Studocu, com a marca "Exemplar para uso exclusivo - Convênio Sistema CONFEA/CREA/MUTUA".

**O que é a 2025 (Prefácio, PDF p. 9, norma p. ix):** "A ABNT NBR 15575-1:2025 equivale ao conjunto ABNT NBR 15575-1:2024, Emenda 1, de 05.12.2025, que cancela e substitui a ABNT NBR 15575-1:2024." Logo, a 2025 é a de 2024 com a Emenda 1 aplicada. **A edição vigente é a de 2025**, agora confirmada no próprio texto da ABNT, e não mais só em fonte secundária.

## 1. Pé-direito mínimo (item 16.1.1): NÃO MUDOU

Mesmo número de item, mesma página (norma p. 64; PDF p. 76 nas duas). Texto idêntico, palavra por palavra:

- 2025, PDF p. 76: "A altura mínima de pé-direito não pode ser inferior a 2,50 m. Em vestíbulos, *halls*, corredores, instalações sanitárias e despensas, é permitido que o pé-direito seja reduzido ao mínimo de 2,30 m. Nos tetos com vigas, inclinados, abobadados ou, em geral, contendo superfícies salientes na altura piso a piso e/ou o pé-direito mínimo, devem ser mantidos pelo menos 80 % da superfície do teto, permitindo-se na superfície restante que o pé-direito livre possa descer até o mínimo de 2,30 m."
- 2024, PDF p. 76: mesmo texto.

**Conclusão:** continua 2,50 m e 2,30 m. Atenção: a lista da norma é "vestíbulos, halls, corredores, instalações sanitárias e despensas". O Briefing resume como "banheiros, corredores e despensas". O resumo não está errado, mas omite vestíbulo e hall.

## 2. Item 16.2 e Anexo F: NÃO MUDOU

**16.2.1 (norma p. 64, PDF p. 76 nas duas), texto idêntico:** "Para os projetos de arquitetura de unidades habitacionais, sugere-se prever no mínimo a disponibilidade de espaço nos cômodos da edificação habitacional para colocação e utilização dos móveis e equipamentos-padrão listados no Anexo F."

**Anexo F (norma p. 90, PDF p. 102 nas duas):** continua com a letra **F**, continua "(informativo)", com o mesmo título: "Dimensões mínimas e organização funcional dos espaços". O texto de abertura também é igual: "Este Anexo visa apresentar como sugestão [...]" e "Recomenda-se que os projetos [...] prevejam no mínimo [...] Tabela F.1, cujas dimensões são informadas na Tabela F.2."

**Tabelas F.1 (PDF p. 102) e F.2 (PDF pp. 103-105, norma pp. 91-93):** comparei linha a linha, por imagem. Os móveis, as medidas (l x p), as circulações e as observações são iguais nas duas edições. Exemplos: cama de casal 1,40 x 1,90; largura mínima da sala de estar 2,40 m; cozinha 1,50 m; banheiro 1,10 m, exceto no box.

**Notas da Tabela F.2 (PDF p. 105, norma p. 93), idênticas nas duas:**
- "NOTA 1 Esta Norma não estabelece dimensões mínimas de cômodos, deixando aos projetistas a competência de formatar os ambientes da habitação segundo o mobiliário previsto, evitando conflitos com legislações estaduais ou municipais que versem sobre dimensões mínimas dos ambientes."
- "NOTA 2 Em caso de adoção em projeto de móveis opcionais, as dimensões mínimas devem ser obedecidas."

A ressalva de 31/10 continua valendo: a Nota 2 tem um "devem". Se o projeto adota o móvel opcional, a medida mínima dele vale como regra. Essa leitura continua indo ao Gate.

## 3. Outros trechos do Briefing que citam a 15575

Fiz um Grep de "15575" no `briefing_modelo_v2_proposta.md`. Achei 4 linhas: 9, 128, 130 e 308. Todas tratam só de três coisas: o pé-direito (16.1.1), o Anexo F (informativo, com "sugere-se prever no mínimo") e a obrigação de seguir a norma. **Nenhum trecho mudou na 2025.** O que precisa mudar no Briefing é só a marca de pendência:
- l. 9: "NBR 15575-1:2025 (ler e confirmar os números de pé-direito da Seção 3)". Pode sair: está lido e confirmado.
- l. 130: "[A CONFERIR: números da NBR 15575-1:2024; confirmar na edição 2025 antes do 1º cliente real]". Pode sair: os números são iguais na 2025.
- l. 308: "texto lido na edição de 2024 do acervo; a edição vigente é a de 2025, segundo fonte secundária ainda não conferida na ABNT" e "só ficam firmes depois de alguém ler a edição de 2025 (Kelsen, item 9)". As duas frases ficaram superadas: a 2025 foi lida, e a vigência está no Prefácio (PDF p. 9).

Quem edita o Briefing é o Oscar (via Lúcio). Eu não editei.

**O que a 2025 mudou (sem efeito no Briefing):** na Bibliografia (norma p. 94, PDF p. 106), a 2025 incluiu a "ABNT NBR 15220-2" (Resistência e transmitância térmica, ISO 6946:2017 MOD) como item [6]. Por isso a lista passou de 23 para 24 itens. Isso indica que a Emenda 1 mexeu na parte de desempenho térmico. **Não comparei a norma inteira**: li só as pp. 1-3, 5-11, 76-77 e 102-107 da 2025, e as pp. 1, 76 e 102-107 da 2024. Se alguém usar a Seção 11 (térmico), precisa comparar de novo.

**Erro de cópia da própria ABNT (não muda nada para nós):** no Prefácio de 2025 (PDF p. 9), o parágrafo de transição ainda fala da "ABNT NBR 15575-1:2021" e da "versão anterior [...] 15575-1:2013". A p. ii da 2025 diz "© ABNT 2024".

## 4. Skills que citam "NBR 15575-1:2024" e precisam passar para 2025

Fiz um Grep em todo o projeto. Só estas 2 Skills citam a edição, cada uma em duas cópias, `.claude` e `.agents`, com as mesmas linhas:

**`coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj/SKILL.md`** (dono: Lúcio/Oscar, editada por mim e pelo Hely em 31/10)
- l. 5 (descrição/changelog): "NBR 15575-1:2024 item 16.1.1: 2,50 m; 2,30 m"
- l. 52: título "### Casa unifamiliar ou bifamiliar (COES Art. 31 + NBR 15575-1:2024, item 16.1.1)"
- l. 56: "NBR 15575-1:2024, item 16.1.1 (p. 64 da norma, p. 76 do PDF do acervo ...)"
- l. 224 (2 ocorrências): "segue a NBR 15575-1:2024 item 16.1.1" e "NBR 15575-1:2024 pp. 76, 102 e 105 do PDF"
- l. 228 (fontes): "NBR 15575-1:2024 — `D:\008_Normas ABNT\abnt-nbr-15575-12024-...-requisitos-gerais_compress.pdf`". Este arquivo é **uma terceira cópia** da 2024, na raiz do acervo, e não é o arquivo de 2024 que está em `001_ABNT`. Trocar para o PDF de 2025. As páginas 76, 102 e 105 continuam certas na 2025.

**`layout-mobiliario-dimensoes-residencial/SKILL.md`** (dono: Lúcio)
- l. 3 (descrição): "mínimo (NBR 15575-1:2024 Anexo F)"
- l. 21: "a NBR 15575-1:2024 Anexo F (informativo, "sugere-se prever no mínimo", item 16.2.1)"
- l. 31: tabela de faixas, "| **Mínimo** | NBR 15575-1:2024 Anexo F |"
- l. 87: "NBR 15575-1:2024, Anexo F, Tabelas F.1 e F.2 (pp. 90-93)". As páginas da norma continuam certas na 2025.

**`layout-mobiliario-dimensoes-residencial/references/medidas_por_comodo.md`**
- l. 4: "[NBR] NBR 15575-1:2024, Anexo F (faixa mínima)"
- l. 137: "NBR 15575-1:2024, Anexo F, pp. 90-93"

A troca em todas é só de rótulo (2024 → 2025) e, na l. 228, do caminho do PDF. Nenhum número muda. Arquivos fora de Skills que também citam a 2024 (pareceres, correções e pesquisas datados de 28/10 a 02/11) são registro histórico e não precisam de edição. São eles: `parecer_coes_art31_lc270_31-10.md`, `correcoes_31-10/kelsen.md`, `oscar_aplicacao*.md`, `briefing_modelo_v2_diferencas.md`, `pesquisa_externa_layout_mobilia_28-10.md` e o parecer do Bardi de 31/10.

## Decisão

**Libera.** Os números do Briefing (2,50 m / 2,30 m; Anexo F informativo com "sugere-se prever no mínimo"; Nota 2 com "devem") estão confirmados na edição vigente, a de 2025, lida no PDF. Faltam três coisas: (a) o Oscar tira as marcas de pendência das l. 9, 130 e 308; (b) os donos das Skills trocam o rótulo nos arquivos listados acima; (c) a leitura da Nota 2 continua indo ao Gate de Claudemberg, como já estava.
