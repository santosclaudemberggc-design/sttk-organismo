# Aplicação das correções do Briefing Único v2 (Oscar, 31/10/2026, noite)

- **Pedido:** Claudemberg, via Lúcio: aplicar as correções da revisão final.
- **Arquivos editados:**
  - `briefing_modelo_v2_proposta.md`
  - `briefing_modelo_v2_diferencas.md`
  - Skill `layout-mobiliario-dimensoes-residencial` v1.0 → v1.1, nas duas cópias (`.claude\skills\` e `.agents\skills\`). As linhas 32, 33 e 39 foram editadas igualmente nas duas cópias. Conferência: as duas têm 75 linhas no SKILL.md e 123 no references. Isso é contagem, não prova byte a byte.
- **Fontes:**
  - `briefing_revisao_final_8_agentes_31-10.md` (seção "Decisões de Claudemberg");
  - `auditoria_cardozo.md` (seções 2 a 6);
  - `kelsen.md` (itens 1 a 14);
  - baumgart, landell, saturnino, tenreiro e glaziou (texto exato);
  - transcrição `briefing_formularios_drive_transcricao_30-10.md` (L10: campo "Tipo de residência").
- **Não toquei** no Ensaio 003, no Drive nem no Revit. Não fiz commit.

## 1. Os 34 passos da auditoria do Cardozo (seção 4)

| # | Passo | Status | Observação |
|---|---|---|---|
| 1 | ESC-01, opção "Automação (inclui o projeto Elétrico)"; Condição com C-13 | aplicado | — |
| 2 | ESC-02, Usado por + Tenreiro + Baumgart | aplicado | — |
| 3 | MOR-02, texto do Kelsen | aplicado | Usado por: Oscar, Tenreiro, Glaziou |
| 4 | TER-01 depois da SOC-02, Usado por Oscar, Baumgart, Saturnino, Landell | aplicado | Na Condição, entram a ligação com a CAS-01 e a regra "linha 6 só se a lei permitir". A TER-01 ficou na Seção 2, como manda a auditoria, e não foi levada para junto da CAS-01 |
| 5 | PRG-01 com "lavanderia / área de serviço"; T-9 e G-6 a critério do Oscar | aplicado | **T-9 em parte:** entraram banheiro social e closet (ordem de Claudemberg). Brinquedoteca, rouparia e depósito **não** entraram, porque a ordem cita só os dois primeiros. **G-6 aplicado**, com o texto da G-2b ajustado. Sem Paisagismo, o dono é o Oscar (nota) |
| 6 | EST-01 e EST-03 + Glaziou | aplicado | — |
| 7 | EST-02 + Baumgart; "Prefira fotos sem pessoas" | aplicado | — |
| 8 | EST-06 depois da EST-03 | aplicado | — |
| 9 | SUS-01 e SUS-02 (Saturnino) | aplicado | — |
| 10 | GOU-01 (Saturnino) + Tenreiro | aplicado | — |
| 11 | HID-02 com "Lavanderia / área de serviço" e área gourmet condicional | aplicado | — |
| 12 | CLI-01 + Tenreiro | aplicado | — |
| 13 | HID-04 com os textos ajustados | aplicado | Fica na Seção 5, depois da GOU-01 |
| 14 | HID-03, Condição única | aplicado | — |
| 15 | ELE-01 (Landell 8) | aplicado | — |
| 16 | ILU-02, INT-01 (com a condição T-8), INT-02, INT-04 e nota T-2 | aplicado | **INT-01 pela condição do Cardozo:** a lista só traz o que a PRG-01 e o ESC-02 têm (com os banheiros e a área gourmet), sem brinquedoteca, rouparia, depósito, jardim e playground. Motivo: a T-9 foi aceita só em parte |
| 17 | PAI-02 e PAI-04 com o ajuste (sem "nenhuma lei obriga"); Decisão "(D6, C-16)" | aplicado | O cabeçalho da 6-bis passou a dizer que a PAI-02 e a PAI-04 ganharam o aviso |
| 18 | TI-01 (Baumgart 1a) | aplicado | — |
| 19 | TI-02, dono e texto (Saturnino 3b e 5b) | aplicado | — |
| 20 | TI-03 com a lista nova | aplicado | — |
| 21 | TI-04, TI-05, TI-10 | aplicado | — |
| 22 | TI-13 (Saturnino 3a), com a lista de 5 perguntas | aplicado | **K1:** "antes do link 'em casa'" virou "antes de o cliente receber a parte 'em casa'". Entrou também a marca do projeto de gás [PENDENTE: Claudemberg] |
| 23 | TI-14 do Kelsen | aplicado | — |
| 24 | Tabela TI-EST com os ajustes (i) e (ii) | aplicado | O ajuste (iii), a marca "interpretação a confirmar no Gate", também entrou no texto da TI-EST-02 |
| 25 | Tabela TI-ELE; TI-ELE-02 com o ajuste de LGPD | aplicado | — |
| 26 | TI-PAI-03, frase final | aplicado | — |
| 27 | TI-PAI-06, texto único | aplicado | — |
| 28 | Nota "Piscina: quem cuida de quê" | aplicado | — |
| 29 | C-1, texto único | aplicado | Entrou a CAS-01 ("ainda não sei" conta como resposta). A ACE-01 não é obrigatória |
| 30 | C-2 (NIV-01, sai a MED-01, Landell, Saturnino, Tenreiro, Kelsen) | aplicado | Entraram também as linhas da Arquitetura: o choque C5 × C4, a ACE-01 e a "VIS-02 exceto 'nada'" |
| 31 | C-3, texto único | aplicado | — |
| 32 | C-8, T-3 e T-4 | aplicado | Uma frase a mais registra que a ILU-02 e a INT-04 vêm do FORM-INT |
| 33 | C-12 (G-2c, G-8, linha SUS, G-7) | aplicado | A G-7 entra porque a PET-01 ganhou "ainda não sei". A G-8 cita a CON-01, e não "a K2" |
| 34 | C-13, C-14, C-15, C-16, C-17 | **aplicado em parte** | **C-13:** aplicada; acrescentei a ILU-02 à lista de "contém Elétrico", porque a condição dela é "Interiores ou Elétrico" (coerência). **C-14:** aplicada com os ajustes; a linha do elevador cita a ACE-01. **C-15:** aplicada com o ajuste da descarga. **C-16:** itens 1 e 2 aplicados. A frase de abertura da Glaziou ("com a frase 'é regra nossa, não da lei'") foi ajustada para "regra do escritório"/"é uma regra nossa", para não contrariar o ajuste G-2a/G-2b do próprio Cardozo. **O item 3 (G-9) NÃO foi aplicado como decidido:** a ordem de Claudemberg manda marcar [PENDENTE: Claudemberg]. Ficou marcado assim, e a proteção continua só como disparo da C-12. **C-17:** aplicada; a dúvida sobre a IA ficou marcada [PENDENTE: Claudemberg] |

## 2. Os 14 itens do Kelsen

| # | Item | Status | Observação |
|---|---|---|---|
| 1 | PRV-01 | aplicado | Marcas padronizadas como "[PENDENTE: Claudemberg (...)]": razão social e CNPJ, prazo de guarda, e-mail |
| 2 | CON-01 | aplicado | — |
| 3 | MOR-02 | aplicado | — |
| 4 | RES-01 | aplicado | — |
| 5 | Transferência internacional | aplicado como **C-17** | — |
| 6 | DEC-01 | aplicado | — |
| 7 | Frase da C-7 (D4, "salubre", "pé-direito") e trecho "Saúde" | aplicado | A frase também aparece como texto informativo no começo da Seção 3, como o Kelsen sugeriu |
| 8 | TI-14 + linha na C-2 + C-3 | aplicado | — |
| 9 | Edição da NBR 15575-1 (C-7 e cabeçalho) | aplicado | — |
| 10 | NBR 9575:2010 | aplicado | Pelo texto único do passo 27 |
| 11 | Idoso = 60 anos ou mais | aplicado | Na C-2 |
| 12 | C-1 | aplicado | Pelo passo 29 |
| 13 | EST-02 "Prefira fotos sem pessoas" | aplicado | — |
| 14 | Recontar | feito | Ver seção 4 |

## 3. Parte própria da Arquitetura

| Item | Status | Como |
|---|---|---|
| 1. Tipo de casa no início | aplicado | **CAS-01** na Seção 0, depois da ID-02. O campo "Tipo de residência" existe no Pré-Briefing (transcrição L10), mas as opções dele não foram transcritas. Por isso **não dá para afirmar que ele já cobre** térrea, sobrado e três andares. A solução não duplica: a CAS-01 vem marcada pelo Pré-Briefing quando o campo trouxer o dado (C-9), e o cliente só confere; quando não trouxer, o cliente responde. Marca: [A CONFERIR: opções do campo]. Subsolo e mais um andar **não** se perguntam na CAS-01: ficam nas linhas 1 e 6 da TER-01 |
| 2. Elevador e plataforma; choque do ALTO 5 | aplicado | **ACE-01** na Seção 1, depois da MOR-03. Aparece se a CAS-01 for diferente de "térrea". Opções: elevador, plataforma, espaço reservado, não precisa, ainda não sei. Linha nova na C-2 para o choque: a sala sobe (C4), a suíte de C5 fica no térreo e o partido tem elevador ou plataforma. **Julgamento meu, Lúcio confirma:** se a ACE-01 for "não precisa" ou ficar em branco, fica no mínimo o espaço reservado, com o motivo escrito no EP. Idoso = 60 anos ou mais (Lei 10.741/2003, Art. 1º) |
| 3. ALTO 2 | aplicado | Regra geral no topo da Parte B: disciplina não contratada → Oscar no Levantamento, só o fato de campo; cálculo vira nota |
| 4. D1 | aplicado | A MED-01 virou linha RETIRADA; a C-2 ganhou a linha do NIV-01 (T-10); sai a linha da MED-01; C-1 com B7 = NIV-01. Skill v1.1: "faixa pedida" → faixa pelo NIV-01 (econômico/médio → conforto; alto/premium → alto padrão; sem NIV-01 → conforto) |
| 5. K1 | aplicado | Legenda, C-4, C-6, TI-12 e TI-13 sem link, pasta, Forms ou Drive de montagem. C-4 = "uma sessão por cliente no Sistema de Gestão, isolada; nenhum cliente vê a do outro". **Parte D nova:** D-1 campos, D-2 condições e listas, D-3 o que fica guardado, D-4 isolamento |
| 6a. VIS-02 com "nada" | aplicado | Na C-2 e na C-12: "qualquer opção exceto 'nada'" |
| 6b. PET-01 "ainda não sei" | aplicado | Na linha "tem pet" |
| 6c. Lavanderia / área de serviço | aplicado | PRG-01, HID-02 e INT-01 |
| 6d. Banheiro social e closet na PRG-01 | aplicado | "Banheiro social, fora das suítes (quantos)" e "closet (onde: suíte do casal / outras suítes)". O "(closet?)" saiu da suíte do casal |
| 6e. Recontar | feito | Linha "Números", tabela "Tempo" e arquivo de diferenças |
| 7. Arquivo de diferenças | aplicado | Totais, legenda (PAD-01 → proposta no EP), destinos desatualizados (EST-04, VIS-01, VIS-03, INT-02, cores, iluminação, reuso, sondagem, sistema estrutural) e tabela nova "anterior × nova". Ressalvas atualizadas |

**Pendências marcadas "[PENDENTE: Claudemberg]" no Briefing:**
- dono do projeto de gás (nota da Parte B e TI-13);
- G-9, planta tóxica ou com espinho (C-16, item 3);
- e-mail de privacidade e prazo de guarda (PRV-01, CON-01, D-3);
- Art. 33 para a IA (C-17).
- Também marcadas: razão social e CNPJ.

## 4. Contagens finais (conferidas por Grep nas linhas da tabela)

| O quê | Número |
|---|---|
| Códigos de pergunta ativos | **63** (68 criados − 5 retirados: PAD-01, EST-04, VIS-01, VIS-03, MED-01) |
| Por seção | Seção 0 = 6 · Seção 1 = 10 · Seção 2 = 10 · Seção 3 = 1 · Seção 4 = 5 · Seção 5 = 8 · Seção 6 = 12 · Seção 6-bis = 6 · Seção 7 = 5 |
| Só Arquitetura | 38 fixas + 7 condicionais (RES-01, MOR-02, ACE-01, HID-02, SUS-02, GOU-01, HID-04) = **até 45** |
| Pacote completo sem Paisagismo | **até 56** (45 + 11; ELE-02 e automação nunca juntas) |
| Pacote completo com Paisagismo | **até 62** |
| Tarefas internas | **24** (TI-01 a TI-14 = 14; TI-PAI = 6; TI-EST = 2; TI-ELE = 2) |
| Regras | C-1 a C-17 + Parte D |
| Tempo (estimativa, não medido) | Reunião 46,5 min (só Arq) / 54 (completo). Casa 34 / 53 |

## 5. O que fica fora (não feito e por quê)

- A Skill `layout-mobiliario-dimensoes-residencial` ainda tem duas coisas antigas:
  - na L22, a frase ao cliente sem a D4;
  - na L21 e na seção 3, a citação "NBR 15575-1:2024".
  - Não editei, porque a ordem pedia só a "faixa pedida". O dono decide; a frase vigente está no Briefing.
- Skill `nbr9575-impermeabilizacao` ("2024"): não é minha (auditoria do Cardozo, seção 6).
- Pendências do Kelsen continuam abertas:
  - a CON-01 cobre a visita?;
  - Res. Conj. 001/2005, Art. 6º;
  - Lei 9.164/2020;
  - casa na divisa e mais um pavimento;
  - lista de invasoras;
  - NBR 15575-1:2025 não lida.
- As normas sem texto oficial no acervo continuam iguais (lista na seção 6 da auditoria).
- Ambíguo, decidido por mim e marcado para Lúcio:
  - códigos CAS-01 e ACE-01;
  - lugar da ACE-01 (Seção 1);
  - a saída "espaço reservado" no choque C5 × C4;
  - ILU-02 na lista da C-13.
- O Briefing precisa de nova conferência do Bardi (nota mínima 8,00) antes de qualquer uso.
