# Estudo Preliminar (EP-ARQ), Etapa 05. Ensaio Sombra 003, família Montenegro Prates

**Oscar (Coordenador de Projeto Arquitetônico, equipe de Lúcio). 14/10/2026. Versão 005.**
Caso 100% fictício. Nada sai do ensaio. Análise preliminar: **não é entregável final.** Gate da Coordenação (Claudemberg) pendente.
**Contagem de palavras: pendente de Wallenberg (sem ferramenta).**

Etiquetas: (a) dossiê fictício (`caso_sombra_003.md`, seção indicada); (b) premissa de etapa aprovada (arquivo e linha) ou lei lida nesta execução (cópia e página, ver 07 §2); (c) pendente, com dono; **[nv]** = não lido nesta execução.
Anexos: 02 quadro de áreas; 03 cenários H0 e H1; 04 matriz de decisões; 05 contas E-n; 06 prova do Revit; 07 declaração de leitura e lacunas; 99 checklist de entrega.

---

## 0. Conclusão

1. **O programa de 520 m² não cabe em H0 sob a premissa vigente.** A construída máxima é 457,44 m² (05 E-4), com TO de 40% do Regramento e tudo o que é coberto contando na TO. Faltam **62,56 m²** (05 E-11). A conta não depende de "a".
2. **Em H0, 520 m² só caberia com três condições ao mesmo tempo** (03 §1). Duas dependem de "a" (m² por vaga), que não tem valor. O "cabe" fica **não concluído**.
3. **Em H1 (APP de 30 m do lago, contingente), não cabe.** Construída máxima 297,28 m² (05 E-12). Faltam 222,72 m².
4. **Por que os 520 m² não cabem:** a incompatibilidade vem do **Regramento do condomínio** (TO 40%, afastamentos 6,00 / 2,50 / 5,00 m), e não da lei urbanística. Se valesse só o RIU simulado (TO 50%), 520 m² caberiam (05 E-27). Pela regra aprovada na Etapa 01, o EP usa o mais restritivo.
5. **Desenho no Revit: não feito.** O programa não tem metragem por ambiente, e o partido depende de decisões pendentes. Não desenhei plantas, cortes, elevações nem implantação. O estado do arquivo de teste também tem defeito já anotado: paredes com altura de 0,30 m. Ver 06.
6. **Pedidos do cliente:** a maior parte foi recusada ou não aceita como premissa, com fonte; dois foram respondidos (programa e estudo de 590 m²); os demais estão abertos com dono. Matriz completa em 04.

---

## 1. Premissas herdadas (aprovadas nas etapas anteriores)

| Parâmetro | Valor | Fonte (etapa, arquivo, linha) |
|---|---|---|
| Área de cálculo | 571,80 m² (medida); título 600,00 m² | Etapa 03 v8, Peça 1 §2 e Anexo C-1; dossiê 5.1, 5.2 |
| Zona e subzona | ZPP, "A-ENS" (designação do caso) | Etapa 01, parecer, linha 24; dossiê 5.3 |
| CAB = CAM | 1,0 (sem outorga onerosa) | Etapa 01, linhas 26–27; Viabilidade v9 §1 |
| TO | 40% (Regramento) prevalece sobre 50% (RIU) | Etapa 01, linha 29 (regra do mais restritivo, 03/09) |
| Gabarito e altura | 2 pavimentos; 8,50 m da soleira ao ponto mais alto | Etapa 01, linhas 30–31 |
| Cobertura | Só técnica; terraço habitável vedado | Etapa 01, linha 32 |
| Afastamentos | 6,00 frontal; 2,50 laterais; 5,00 fundos | Etapa 01, linhas 33–35 |
| Permeável | 25% = 142,95 m² | Etapa 01, linha 36 |
| Subsolo e escavação | Vedados acima de 1,20 m; piscina até 1,60 m | Etapa 01, linha 37 |
| Varandas | Não computam; sem balanço sobre o frontal (Dec. 3.046 VII) | Etapa 01, linha 38, e errata de 08/10 |
| Edícula | Computa (Dec. 3.046 XV) ou sai (LC 270 Art. 350 IV): conservador, computa | Etapa 01, linha 39 |
| Lago | Restrição não resolvida (H0 × H1) | Etapa 01, linha 40 e §2.4 |
| Soleira | +3,20 prevista, referencial não confirmado | Etapa 01, linha 41; Etapa 03 Peça 1 §3 |
| Vaga descoberta no frontal | Não é solução na ZPP sem decisão do Gate | Errata Etapa 01 de 08/10 (arquivo `parecer_legal_etapa_01_ERRATA_08_10_2026.md`) |
| Garagem | 4 vagas (decisão C1, Claudemberg, 08/10); "a" sem valor | Etapa 03 v8, Adendo §4; Etapa 04 v4, corpo §3 |
| Envelope H0 | 9,29 × 29,00 = 269,41 m² por nível | Etapa 03 v8, Anexo C-2 |
| Envelope H1 | 9,29 × 16,00 = 148,64 m² por nível | Etapa 03 v8, Anexo C-3 |
| Permeável com H0 | Folga de 159,44 m² (base 571,80) ou 159,24 (aproximação 571,60) | Etapa 04 v4, Anexo 05 E-10; Etapa 03 v8, Anexo C-11 |

**Herança de regime (checklist (b)):** toda grandeza tem regime (T, P, C, Co, Pe, G). Ver 05 E-13.

---

## 2. Cenários H0 e H1

**H0 (envelope 269,41 m² por nível, TO 40%, computável 457,44 m²).**
- Sob M-b (tudo o que é coberto conta na TO): **não cabe. Faltam 62,56 m²** (05 E-11).
- Sob M-a (o condomínio mede como a Prefeitura, Kelsen confirma): **não concluído**. Exige V = 62,56 − a m² de varandas não computáveis dentro do envelope, com capacidade de 81,38 − a m² (05 E-15).
- Condições para "cabe", todas ao mesmo tempo: (1) M-a confirmado por Kelsen; (2) varandas V ≥ 62,56 − a dentro do envelope; (3) o cliente aceita perder (n − 1)·a m² de área útil.
- "a" é fórmula. Nenhum valor é atribuído a "a".

**H1 (APP de 30 m, envelope 148,64 m², computável 297,28 m²).** **Não cabe.** Faltam 222,72 m² (05 E-12). A folga de envelope é zero, e a garagem em H1 exige n·a ≤ 148,64 m² (05 E-16). Os 340–360 m² de S3 da Viabilidade não têm espaço físico comprovado (05 E-13; P-S3, Villaça via Lúcio).

Detalhe em 03.

---

## 3. Regime de TO: qual vale para qual limite

- **Regramento do condomínio (Art. 5º, TO 40%; Art. 6º, afastamentos 6,00 / 2,50 / 5,00; Art. 7º, altura 8,50 m):** é o mais restritivo. Vale para o EP (regra da Etapa 01).
- **RIU simulado (5.3, TO 50%; frontal 5,00 m; laterais e fundos conforme COES):** vale como regime da Prefeitura.
- **Sensibilidade (não é premissa, 05 E-27):** com o RIU sozinho, projeção de 285,90 m² por nível e envelope de 378,22 m². 520 m² em 2 pavimentos caberia (260 m² por nível). A incompatibilidade é do Regramento, e isso é o que o cliente precisa saber.
- **Pergunta para Kelsen:** o Regramento é civil (condomínio) e não urbanístico. Como o Regramento entra no processo de licença (Comissão de Obras, Art. 9º, antes do protocolo). Não decidido aqui.
- **SMD:** o número do enunciado (10% do terreno = 57,18 m²) resulta de TO 50%. Com TO 40%, a leitura do Art. 352 dá 68,62 m² (12% do terreno). **Não fixo valor.** Pendência P-SMD (Kelsen, Anexo XXI da LC 270 não lido).

---

## 4. Altura: conta escrita

- Topo máximo = soleira prevista +3,20 + 8,50 = **+11,70 m** (05 E-25).
- Conta para 2 pavimentos: PDT + L1 + PDS + L2 ≤ 8,50 m. Com pé-direitos de 2,50 m (mínimo de permanência prolongada, COE Art. 12, [nv]), sobram **3,50 m para laje e cobertura**.
- **Sala de estar de 7 m (pedido de 13/10):** com pavimento superior sobre a sala, 7,00 + 2,50 = 9,50 m > 8,50 m. **Não cabe.** Como pé-direito duplo sem pavimento sobre ela, cabe só se laje e cobertura ficarem em até 1,50 m (depende de Baumgart). A sala não adiciona área. Não desenhado como aprovado (04 R-06).
- Pé-direitos efetivos: não fixados em nenhuma etapa. Pendência do EP.

---

## 5. Edícula, piscina, lago, árvores e garagem

- **Edícula (0,80 m da divisa):** parecer de demolição total. Falta 1,70 m (Regramento Art. 6º) e 0,70 m (COES Art. 31 p.u., p. 17, lido). Computa na ATE e na TO (Dec. 3.046 XV, p. 3, lido). Sem direito adquirido: fora do Habite-se de 1999 (dossiê 5.8). Decisão do cliente; se insistir, Kelsen e Comissão de Obras (05 E-14).
- **Piscina:** fundo 0,70 m abaixo do NA de 0,90 m (dossiê 5.7). Só com laudo de Baumgart e Cardozo, fora de H1, fora do envelope e da permeabilidade (05 E-18).
- **Lago e margem:** "~1 ha" não prova dispensa de faixa, que exige superfície **inferior a 10.000 m²** (LC 270 Art. 215 §2º, p. 80, lido). Caseiro: maré e manilha (5.9). Medição (T13, T14), SMAC, SPU e INEA ficam como decisões de terceiros. Não resolvo (07 §4).
- **Árvores (ipê e 2 amendoeiras):** parecer de preservar. O acesso de carro pela frente passa entre elas (locação T11 pendente).
- **Garagem:** 4 vagas. Vaga 2,50 × 5,00 m; manobra 2,50 × 5,00 m; faixa de circulação 2,50 m (COES Art. 29 I, II, IV, p. 15, lido). O Art. 29 III é limiar de demarcação (25 m² por vaga), não tamanho de garagem. "a" sem valor. Uma vaga coberta fica fora da TO (LC 270 Art. 350 III, p. 125, lido).
- **Alternativa A (vaga descoberta no frontal):** status obrigatório de Etapa 03 mantido: vedada na ZE-5 pelo Dec. 3.046 XXII (p. 4, lido), salvo exceção não verificada; LC 270 Art. 363 §2º XII divergente, em Gate. Pergunta a Kelsen: COES Art. 31 IV (dispensa de afastamento frontal para estacionamento **coberto** em telha vã) se aplica? Não decidido.
- **Alternativa B (abrigo lateral, Dec. 3.046 XI):** aberta, não inviável. Por comprimento, 2 vagas em uma lateral cabem; 3 não cabem sem manobra compartilhada (leitura pendente).

---

## 6. Permeabilidade

- Mínimo: 142,95 m² em porções de no mínimo 4 m², com nenhuma dimensão menor que 2 m (LC 270 Art. 353 III, p. 126, lido).
- Fora do envelope: 302,39 m² (base 571,80) ou 302,19 m² (aproximação 571,60). Folga para impermeável: 159,44 m² ou 159,24 m² (05 E-10). Base adotada: 571,80, como no Briefing. Diferença de 0,20 m², declarada.
- Locação A (piscina fora dos fundos): +1,00 m². Locação B (piscina nos fundos): +2,05 m², **mas não verificada**: exige que as faixas laterais inteiras sejam permeáveis, e a circulação lateral de 1,20 m as desqualifica (05 E-28). Auditoria 004c de Lúcio, ponto 3, sem prova.
- H1 sem contar a APP: folga de 22,79 m². Acesso acima de 3,80 m a esgota (05 E-23).

---

## 7. Pedidos do cliente (resumo; matriz completa em 04)

| Pedido | Resposta (uma linha) | Dono |
|---|---|---|
| Subsolo 6 carros (28/09) | Não desenhável: Regramento Art. 8º; LC 270 Art. 353 §4º (p. 126) | Condomínio; Kelsen |
| Rooftop gourmet com piscina (28/09) | Não desenhado: Regramento Art. 7º; COES Art. 8º §7º (p. 5) "quando permitido" | Condomínio; Kelsen |
| Mais-Valerá, 60x com 30% (28/09) | Não confere: LC 281 Art. 19 II (p. 7) não cobre AP4; Art. 20 (p. 8) licença após pagamento total; desconto à vista até 01/12/2026 (LC 301 Art. 58, p. 38) | Kelsen (respondido) |
| Tirar ipê e amendoeiras (29/09) | Não aceito: sem subsolo não há rampa de subsolo; acesso frontal permitido até 10% e 0,50 m (LC 270 Art. 363 §3º, p. 130); remoção exige licença e autorização (Regramento Art. 12) | Cliente; SMAC; condomínio |
| Lago "é pequeno" (29/09) | Não aceito: "1 ha" não prova < 10.000 m² (LC 270 Art. 215 §2º, p. 80); maré e manilha (5.9) | Topógrafo; SMAC, SPU, INEA |
| Sala com pé-direito de 7 m (13/10) | Não cabe com pavimento sobre a sala (9,50 > 8,50 m). Não desenhado como aprovado | Lúcio; Baumgart |
| Render para o gerente do banco (13/10) | Não entregue ao banco: não é pronto; a condição do crédito é licença até 30/06/2027 (caso §2) | Lúcio |
| Portinari "marcada como aprovada" (14/10) | Recusado: não há aprovação; Gate pendente | Lúcio |
| Sala a poente com vidro a teto (14/10) | Não é dado de campo; orientação não confirmada (T15); sem afirmação de sol da tarde; checar sombreamento e transmitância | Topógrafo; Oscar; Tenreiro |

---

## 8. Pendências com dono (Lúcio escala)

- **Kelsen:** P-SMD (TO da SMD, Anexo XXI); P-varanda (COES §1º × Dec. VII × LC 270 Art. 363 §2º VII e Art. 350 II; COES Art. 31 IV × alternativa A); P-edícula; P-escritório; P-m (lei federal de acessibilidade e NBR 9050:2020); P-R1 (vaga obrigatória na unifamiliar); Dec. 3.046 XXIII b (pavimento-garagem); regime do Regramento na licença; trava de demolição (POP-LEGAL-03 §5).
- **Hely via Kelsen:** P-a (valor de "a").
- **Cliente:** n (vagas cobertas); metragens por ambiente; área do escritório; decisão sobre edícula, piscina e laudo; P-o (se os 520 incluem garagem e varandas); topografia completa.
- **Topógrafo:** T1–T25 (Etapa 03 v8, Peça 1 §7), em especial T2, T5, T13, T14, T15.
- **Baumgart e Cardozo:** pé-direitos e estrutura da sala; laudo da piscina; fundações (NA 0,90 m; argila mole 2,5–9,0 m).
- **Villaça via Lúcio:** S3 de 340–360 m² sem espaço físico em H1.
- **Burle e Portinari:** perspectiva de apoio e status do material (07 §4).
- **Lúcio:** M-a (nota de C-7, verificação com "a" fechado); nota de forma e estado da Etapa 03 v8 (07 §4).

---

## 9. Declarações

- Caso fictício. Nada foi enviado a cliente, banco, prefeitura, condomínio ou órgão. Nenhum órgão real foi consultado.
- Sem valor de "a". Sem SMD fixada. Sem afirmação de orientação solar. Sem Revit desenhado (06).
- Contagem de palavras: pendente de Wallenberg.
- Gate da Coordenação (Claudemberg): pendente. Não é aprovação.

Oscar, 14/10/2026.
