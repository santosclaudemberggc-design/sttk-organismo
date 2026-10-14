# 08. Auditoria de Lúcio, Etapa 04 (Briefing), v4
## Ensaio Sombra 003, família Montenegro Prates (caso 100% FICTÍCIO)

**Auditor:** Lúcio (Gestor Arquitetura) | **Executor:** Oscar | **Data:** 13/10/2026
**Escopo:** entregas `01` a `06` de `entrega/v4/`, lidas integralmente por mim nesta execução. Cruzamento com o Resumo do enunciado e com a Etapa 03 v8 (lidas integralmente por mim). Conferência de cópias legais: só as páginas indicadas em cada item.
**Limite:** esta auditoria não é Gate da Coordenação. Gate (Claudemberg): pendente. Nada aqui é parecer final para cliente.

---

## 0. Veredito

**NÃO APROVADA na forma atual.** A estrutura está correta (4 peças + anexos, declarações, checklist (a) a (e) com prova). Há 2 falhas de conteúdo que não podem seguir ao Gate, e 2 ressalvas de método. Correção pontual de 4 itens pelo Oscar, sem refazer a v4 inteira. Depois, nova rodada de auditoria minha, com prova colada.

Não aprovo "OK" de nenhum item sem prova. Os itens verificados por mim estão marcados **[Lúcio verificou]**; os demais estão marcados **[não verificado por mim]**.

---

## 1. Cruzamento com o Resumo do enunciado (SMD, regime, herança)

| Item | Resumo / Etapa 03 v8 | v4 | Resultado |
|---|---|---|---|
| Área de cálculo | 571,80 medida; 600 oficial (Etapa 03 C-1) | 571,80 (05 E-1) | **Confere** |
| TO | 40% pelo Regramento; projeção 228,72 | 228,72 (05 E-3) | **Confere**. 0,40 × 571,80 = 228,72 |
| Computável máximo H0 | 457,44 (2 pav.) | 457,44 (05 E-4) | **Confere**. 2 × 228,72 |
| Envelope H0 | 269,41; folga 40,69 (Etapa 03 C-2) | 269,41; 40,69 (05 E-2, E-5) | **Confere**. 9,29 × 29,00 = 269,41; 269,41 − 228,72 = 40,69 |
| Envelope H1 e teto | 148,64; 297,28 (Etapa 03 C-3) | 148,64; 297,28 (05 E-12) | **Confere**. 9,29 × 16,00 = 148,64; 2 × 148,64 = 297,28 |
| Regime H1 e S3 | Resumo: "S3 = 297,28 (H1)"; 340 a 360 de trabalho | E-13 rotula P, C, Co | **Confere** (checklist (b)) |
| Permeável | 142,95 (Resumo) | 142,95 (05 E-10) | **Confere**. 25% × 571,80 = 142,95. A % não está no Resumo; Oscar declara isso |
| **SMD** | **Resumo: "10% do terreno" = 57,18**. Regra do checklist (a): 20% da área livre pela TO | 57,18 (leitura A) e 68,62 (leitura B) expostos, sem escolha (05 E-6, E-7) | **Divergência exposta, não resolvida. Correta a conduta** (ver §3, P-SMD). Confere: 0,20 × 343,08 = 68,616 → 68,62; 68,62 − 57,18 = 11,44 |
| Herança de premissas | Etapa 03 v8, Anexo I-1 | 01 §1 | **Confere** |

**Conduta sobre a SMD:** correta. O número 57,18 aparece nas duas leituras por coincidência de contas (10% × terreno contra 20% × área livre com TO 50%). Oscar não tratou essa coincidência como confirmação (05 E-8). O exemplo do checklist (a) supõe TO 50%, que não é premissa deste caso. Esse exemplo deve ser corrigido no checklist de Oscar (ação minha, fora desta entrega).

---

## 2. Checklist (a) a (e), com prova

**(a) SMD.** Prova: 05 E-6, E-7, E-8; 01 §0 item 4 e §6; 04 T-01. Passa como exposição de divergência. Pendência P-SMD para Kelsen.

**(b) Regime H1 e S3.** Prova: 05 E-13 (tabela P, C, Co); 01 §2 cita E-12 e E-13. **Passa.** Verifiquei que a frase "340 a 360 não tem espaço físico" depende de E-13 e E-23 (cruzamento correto).

**(c) Organograma legível.** Prova: 03 §2 (tabela de fluxos), §3 (matriz R/D/—), §4 (caracterização em tabela). **Passa.** Esquemas em escala são Etapa 05, registrados em 06 B-10.

**(d) Não computável com artigo.** Prova: 01 §4 e 06 §3(d). Passa para os itens citados. Déficit de 62,56 m² aparece como déficit, não como não computável (01 §4, última linha; 05 E-11). **Ressalva D2** abaixo: a tabela §4 não lista dispensas que tocam a alternativa A e as varandas térreas.

**(e) Cópia citada, nome e página.** Prova: 06 §3(e). Formato com cópia nomeada: **passa** na forma. Conteúdo verificado por mim em duas páginas (ver §4).

---

## 3. Defeitos a corrigir (obrigatórios antes do Gate)

### D1. Número sem fonte, atribuído à Etapa 03 (OBRIGATÓRIO)

- **Onde:** `01_briefing_corpo_003_v4.md` §5.4, linha que diz "a Etapa 03 cita a dispensa abaixo de 10.000 m² (LC 270 Art. 215 §2º [nv])". Repetido em `04_matriz_decisoes_cliente_003_v4.md` linha M-10 ("A dispensa abaixo de 10.000 m² (LC 270 Art. 215 §2º [nv])").
- **Prova do defeito:** li as peças v8 da Etapa 03 inteiras. A Peça 1 §6 diz "LC 270 Art. 215 §2º [nv]" e a Peça 2 §7 não cita valor. Nenhuma delas tem "10.000". Em `06` §3, o Art. 215 está listado como não lido.
- **Correção:** retirar o número. Escrever "dispensa de faixa, LC 270 Art. 215 §2º, não lido nesta execução [nv]; limite a confirmar por Kelsen". Ou ler a cópia da LC 270 e citar página.
- **Risco:** número fabricado com cara de citação. Não pode ir a Kelsen nem a cliente assim.

### D2. Dispensas que tocam a alternativa A e as varandas ficaram fora da tabela (OBRIGATÓRIO)

- **Onde:** `01` §3 (Alternativa A) e §4 (varandas), e `04` linha P-varanda.
- **Prova do defeito [Lúcio verificou]:** COES Art. 31, p. 17, cópia `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`, lida por mim nesta execução. Texto do inciso IV: unifamiliar "ficam dispensadas" de "afastamento frontal, para estacionamento coberto de veículos, em telha vã, com um pavimento de altura". A v4 cita o Art. 31 I, II, III e V, e não cita o IV.
- **Prova adicional [Lúcio verificou]:** LC 270, Art. 350 II, p. 125 (mesma cópia que li): "as varandas e terraços assentes no terreno, para as edificações uni, bifamiliares e multifamiliares" são exceção à projeção. A v4 cita só o Art. 350 III e IV. O inciso II é relevante para varandas no térreo, §4 da v4.
- **Correção:** incluir Art. 31 IV (COES) e Art. 350 II (LC 270) na tabela §4 e no conflito P-varanda / alternativa A, com a pergunta a Kelsen: a dispensa do COES IV se aplica à alternativa A (vaga coberta no frontal) e como se harmoniza com o Dec. 3.046 XXII. **Não decidir.** O status "vedada" da Etapa 03 pode ser mantido, mas a Briefing não pode omitir a dispensa.

### D3. Duas folgas de permeabilidade sem escolha declarada (OBRIGATÓRIO, correção de 1 linha)

- **Prova:** `05` E-10 dá folga H0 = 302,39 − 142,95 = **159,44**. `02` §2 e `04` P-04 usam **159,24** (da Etapa 03 C-12, aproximação retangular de 571,60). `02` §2 registra a "ressalva de 0,20 m²" mas não escolhe. Conta confere: 571,80 − 269,41 = 302,39; 302,39 − 142,95 = 159,44.
- **Correção:** escolher uma base (recomendo a área medida, 159,44, já que é a de cálculo do próprio Briefing) e aplicar igual em 02, 04 e 05. Declarar a diferença de 0,20 m² em uma linha.

---

## 4. Ressalvas de método (não impedem a correção, mas registram o desvio)

### R1. Glob amplo no acervo (método)

- **Prova:** `06` §1 item 14: "Glob em `CONSTRUCAO_DO_ZERO` por `**/Fontes_Legislacao/*.pdf`. Retornou nomes..."
- **Avaliação:** a regra era não listar para descobrir arquivos. O padrão não entrou na pasta do ensaio, e Oscar declara isso. Não há prova de que a listagem trouxe nome de gabarito ou parecer. Oscar deve confirmar por escrito que nenhum nome retornado pertence à pasta do ensaio ou ao examinador, e que nenhum foi aberto.
- **Status:** ressalva. Não é violação de isolamento comprovada.

### R2. Conferência de citações além das que eu fiz (método)

- **Verificado por mim [Lúcio verificou]:** COES Art. 31 I, II, III, V e parágrafo único (p. 17); LC 270 Art. 350 III, IV e Art. 351, 352 caput, §§2º a 4º (p. 125). Texto confere com o que Oscar cita, exceto o que está em D2.
- **Não verificado por mim [não verificado por mim]:** LC 270 Art. 347 II (p. 124), Art. 353 §4º e III (p. 126), Art. 363 §§2º e 3º (p. 130); Dec. 3.046 VII, XI, XIV, XV, XXII (pp. 2 a 4); COES Art. 8º §§1º, 2º, 4º, 6º, 8º (p. 5); COES Art. 29 I a IV (p. 15). Estão marcados "[lido]" pelo Oscar. Não os tomo como verificados.

---

## 5. Itens verificados sem defeito

- **Sem gabarito, sem parecer, sem entregas antigas da Etapa 04.** Confirmado na declaração de Oscar (06 §1, "não abri"). Minha entrada para Oscar continha só os 5 caminhos autorizados mais as Skills. Não citei a pasta de gabaritos nem o parecer, e proibi a abertura de "arquivos de gabarito ou parecer de correção" sem nomes. A v4 não cita nenhuma entrega antiga como fonte.
- **Mensagens do cliente (07 a 09/10):** nenhuma virou premissa. Subsolo, rooftop, Mais-Valerá, "depois a gente ajeita", lago e remoção de árvores estão recusados como premissa, com dono (04 M-04 a M-12). Escritório e atendimento em casa viraram pergunta para Kelsen, não decisão (M-08, M-09).
- **Garagem:** 4 vagas (C1). "a" sem valor em nenhuma linha (02 A9; 05 E-15). Art. 29 III tratado como limiar de demarcação, não como tamanho (01 §3). **Passa.**
- **Alternativa A:** status verbatim da Etapa 03 mantido (01 §3; 04 P-05). Alternativa B aberta, não inviável (01 §3).
- **Revit:** bloqueio registrado com texto literal: "Error: Plugin não está conectado" (06 B-1). Sem desenho, sem simulação.
- **Contagem de palavras:** não feita, declarada em todas as peças. Não há "~" de contagem. **Passa.**
- **Pendências com dono:** lista completa em 01 §6 e 04 §4; Lúcio escala. **Passa na forma.**
- **Tabela pergunta × onde:** 05 T-1. **Passa.**

---

## 6. O que segue

1. Oscar corrige D1, D2 e D3 na v4 (pontual; nas mesmas pastas, sem apagar nada). R1 vira declaração escrita.
2. Eu audito de novo só os trechos alterados, com prova colada (linha ou página), e atualizo esta seção 0.
3. Só depois de OK na nova auditoria, a v4 vai a Wallenberg. Gate da Coordenação (Claudemberg) é etapa seguinte e não é pedido nesta rodada.
4. Ação minha, fora da v4: corrigir o exemplo de SMD do checklist (a) de `oscar.md` (o exemplo de 57,18 supõe TO 50%).

**Pendências que vão a Kelsen (via Lúcio):** P-SMD; P-varanda, agora com COES Art. 31 IV e LC 270 Art. 350 II; P-edícula; P-escritório; P-m; P-a; P-R1. **A Villaça, via Lúcio:** P-S3.

---

Lúcio, 13/10/2026 (auditoria da v4)
