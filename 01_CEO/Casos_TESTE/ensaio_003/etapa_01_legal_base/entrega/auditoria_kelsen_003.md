# Auditoria Kelsen — Ensaio Sombra 003, Etapa 01 (Legal base)

**Peça auditada:** `entrega/parecer_legal_base_003.md` (Hely, 01/10/2026)
**Gabarito usado:** `POP-GESTOR-LEGAL-01`, no que se aplica a uma etapa de **base legal pré-projeto**: Checagem B (itens 4, 4.1 a 4.4) e seções 5 a 7. A Checagem A (pranchas, quadro de áreas, ART/RRT, memorial) **não se aplica**, porque nesta etapa ainda não existe projeto.
**Método:** inspecionei o artefato e reli eu mesmo o primário nos pontos que decidem o mérito. Não me baseei no relatório resumido do Hely.
**Caso 100% fictício.** Nada saiu da pasta. Não abri, listei nem citei `_gabaritos_LACRADO/`, e o Hely declara o mesmo.

---

## 1. O que eu conferi pessoalmente no primário (Read direto no PDF, 01/10/2026)

| Ponto do parecer | Fonte relida por mim | Resultado |
|---|---|---|
| P4: as 60x com 30% de desconto não alcançam a AP4 | `LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`, p. 7, Art. 19, II (redação da LC 291/2025): só AP3, AP5, RA XVI, RA XXXIV e Rio das Pedras | **Confere** |
| P4: a licença só sai depois de quitada a contrapartida | idem, p. 8, Art. 20 caput | **Confere** |
| P2: Art. 22, III da LC 281 (não ocupar recuo nem faixa de proteção de lagoas) | idem, p. 8 | **Confere** |
| P5: APP no entorno de lagoa natural e dispensa só para superfície "inferior a dez mil metros quadrados" | `LC270_2024_PlanoDiretorLUOS.pdf`, pp. 79-80, Art. 215, II e §2º | **Confere**. "Aproximadamente 1 ha" não prova que a superfície seja inferior a 10.000 m² |
| P7: a licença pode ser emitida antes das anuências (leitura que o Hely pediu que eu confirmasse) | `Decreto55622_2025_LICIN2.0.pdf`, pp. 2-3, Art. 4º caput e §§1º-4º | **Confirmo, com precisão a acrescentar**: a licença sai com **prazo máximo de 3 meses**, prorrogável ou revalidável enquanto a obra não começa (§2º). O início da obra exige todas as anuências (§1º) e a declaração do Anexo V (§4º). Se a SMDU aplicar o §3º, o processo sai do prazo de 30 dias (Art. 2º §6º) |
| Prazo de 30 dias da SMDU e reinício da contagem a cada inconformidade | idem, pp. 1-2, Art. 2º §§1º e 5º | **Confere** |
| Dimensões do lote como 1º parâmetro analisado e vistoria do Habite-se contra o Art. 3º | idem, p. 2 (Art. 3º, I) e p. 3 (Art. 8º) | **Confere** |

Já estavam auditados por mim em rodadas anteriores e o parecer não contradiz: LC 301 Art. 58 (desconto à vista até 01/12/2026, que só incide sobre acréscimos não previstos na legislação ordinária) e Art. 38 da LC 274 revogado pela LC 281, Art. 42, II.

Ficou **no grau declarado pelo Hely**, sem releitura minha nesta rodada: LC 270 Arts. 345-354 e 363-364, COES (Arts. 4º, 8º, 31 e Glossário), Dec. 3.046/1981 (Disposições Gerais VII, XV e XXIII), Lei 12.651 Art. 4º, DL 9.760 Art. 2º e Código Civil Arts. 1.301-1.302.

---

## 2. Checagem B do POP-GESTOR-LEGAL-01, item por item

| Item | Situação |
|---|---|
| Zoneamento confirmado por fonte oficial | Usou o RIU simulado como oficial, como manda o enunciado. Num caso real, o `POP-LEGAL-RIU-01` com a trava GeoPAL fica pendente, e o parecer diz isso (5.4) |
| Cada parâmetro com fonte registrada (P. 8) | **Atendido.** São 24 linhas, cada uma com fonte e etiqueta (a), (b) ou (c) |
| Armadilhas da Skill `legal-base-legislativa-bairro` | **Atendido.** Separa preexistente de obra nova (edícula), leva o afastamento lateral ao COES por mais de um artigo e checa a vigência |
| Recuos, gabarito e coeficientes | **Atendido.** Aplica o mais restritivo entre condomínio e Prefeitura em cada parâmetro: TO 40%, recuos 6,00 / 2,50 / 5,00 m, 8,50 m de altura. Mostra que quem limita a área é 2 x TO (457,44 m²), não a ATE |
| Coerência numérica | **Conferi as contas**: 0,40 x 571,80 = 228,72; 0,25 x 571,80 = 142,95; (14,29 − 5,00) x 29,00 = 269,41; 9,29 x 16,00 = 148,64. Todas fecham |
| PRPA identificado | Não definido. **Sobe** (seção 5) |
| Colisão de subzona entre APs | Não se aplica: a subzona é fictícia ("A-ENS") e o RIU do dossiê vale como oficial |
| 4.1 Status jurídico checado no ponto de uso | **Atendido, com bloqueio declarado.** Consulta ao vivo na Busca Fácil em 01/10/2026 (via curl). O Decreto 3.046/1981 não foi localizado por número, e a vigência dele foi inferida pela remissão da LC 270. É ressalva, não barra |
| 4.2 APAC, APP e restrições sobrepostas | APAC: não. APP, FMP e marinha mapeadas e **não resolvidas**, como deve ser. Existe AEI ou área protegida? Não verificável no ensaio, e o parecer declara isso |
| 4.3 Quarentena | Não se apoiou no POP-LEGAL-02. Foi ao primário da LC 281. Apontou uma divergência entre documentos da casa (ver 4.2 abaixo) |
| 4.4 LMS | **Mapeada (T4)**, com a saída correta para o rito pleno (LMP+LMI) se houver APP ou área alagadiça (Dec. 51.503/2022, Art. 27, p.ú.) |

---

## 3. Resultado: **LIBERA COM RESSALVA**

Não barro. O parecer tem as 7 seções do item 3.1 do enunciado. As contas estão abertas e fecham. As 7 perguntas têm resposta e fundamento. Nenhum parâmetro foi inventado: onde falta dado, está marcado (c), com o que falta, onde consultar e por quê. As afirmações que reli no primário conferem.

### Ressalvas (sobem por escrito)

**R1. Área de cálculo de 571,80 m² em vez de 600,00 m².** É uma escolha conservadora e bem fundamentada (LICIN, Anexo I, III, item 1; Art. 3º, I; Art. 8º), e o parecer mostra os dois cenários. Mas ela tem efeito patrimonial e civil para o cliente: o muro do Lote 16 avança sobre a linha do PAL. Quem decide é o cliente, com advogado. O Legal só recomenda.

**R2. O lago define o projeto.** APP (30 m, dispensa só abaixo de 10.000 m²), terreno de marinha (relato de maré) e FMP do INEA estão em aberto. No pior cenário confirmado por conta, o envelope cai de 269,41 m² para 148,64 m². **Achado meu, que complementa o parecer:** a LC 270, Art. 216, V (p. 80) põe as lagoas do sistema da Barra e do Recreio, "seus canais, suas APPs e faixas marginais", entre os Sítios de Relevante Interesse Paisagístico e Ambiental. Se for confirmado que a manilha liga o lago ao canal, essa remissão também precisa ser verificada. Não decidi isso, e é mais um item para a consulta à SMAC.

**R3. Licença até 30/06/2027.** É viável pela LICIN, Art. 4º §2º, mas a licença emitida assim vale **3 meses** e precisa ser revalidada até a obra começar. Antes de o cliente apostar o crédito nessa via, é preciso confirmar com o banco se "licença emitida" com esse prazo atende à condição do financiamento. Obra em maio/2027 é risco alto. Isso é decisão do cliente, informada por nós.

**R4. Tensões normativas que não decido sozinho** (Gate do Maurício, num caso real):
- Dec. 3.046 XV (a edícula computa) contra LC 270 Arts. 347 V e 350 IV;
- Dec. 3.046 VII (varanda sem balanço sobre o recuo frontal) contra COES Art. 8º §1º;
- Dec. 3.046 XXIII (garagem coberta) aplicado a unifamiliar;
- LC 281 Art. 16 §5º contra Art. 40 (pendência já aberta em 24/09);
- a ordem entre demolição e obra nova (TRAVA do POP-LEGAL-03 §5).

Até lá, o parecer adota a leitura conservadora em cada caso, e mantenho isso como premissa para Villaça e Lúcio.

**R5. Risco civil.** A janela da edícula a 0,80 m (CC Arts. 1.301-1.302) e a divisa com o Lote 16. O Alvará não cobre nenhum dos dois (POP-GESTOR-LEGAL-01 §6).

### O que devolvo ao Hely (não bloqueia a etapa)
- Acrescentar a remissão da LC 270 Art. 216, V na Pergunta 5 e no mapa de trâmites (T4), marcada (c).
- Na Pergunta 7, deixar explícito o prazo de 3 meses da licença do Art. 4º §2º e o ponto a confirmar com o banco.

Nenhum dos dois muda conclusão, número ou premissa. São complementos.

---

## 4. O que sobe a Wallenberg

1. **PRPA não definido.** Não cabe ao Legal decidir.
2. **Divergência interna da casa sobre o POP-LEGAL-02.** O cabeçalho dele diz "reconstruído e liberado em 28/07/2026", e a Skill `legal-base-legislativa-bairro` diz "quarentena encerrada". O meu POP-GESTOR-LEGAL-01 §4.3 ainda diz "SUSPENSO desde 23/07/2026", e foi essa a instrução que passei ao Hely. **O erro é meu**: o POP é meu e está desatualizado, ou o cabeçalho está errado. Corrijo em rodada própria, com backup. Para este parecer não teve efeito, porque o Hely foi direto ao primário (LC 281/301).
3. **Divergências entre Skills e o primário**, como proposta de correção aos donos das Skills (não edito Skill):
   - `legal-oodc-mais-valera-mais-valia`: diz que as janelas venceram, mas a LC 301 Art. 58 as estende até 01/12/2026 (só à vista). A fórmula está na LC 281 Art. 18 §1º, não num "Anexo XXV".
   - `decreto3046-81-lc270-2024-licin-barra-recreio`: a R1 pode fechar quanto ao texto do Art. 106 (não há isenção de 5 anos). Os macetes M1 e M2 dependem de premissas, área medida e ausência de maré, que precisam ser provadas caso a caso. Este dossiê mostra por que nunca devem ser presumidas.
   - `varandas-nao-computaveis-ate-to-coes-lc198-rj`: na ZPP, o Dec. 3.046 VII é mais restritivo que o COES Art. 8º §1º quanto a balanço sobre o recuo frontal.
   - `habite-se-aceitacao-licin`: Arts. 5º e 8º conferidos no PDF oficial. A confiança pode subir.
4. **Bloqueio de ferramenta.** O Decreto 3.046/1981 não aparece por número na Busca Fácil, e o status direto dele segue sem confirmação. O Hely não tem WebFetch e contornou com curl, o que funcionou.

## 4.1 ERRATA (Kelsen, 01/10/2026, depois do parecer do Bardi; o texto acima fica como estava, para rastreio)
- **Item 3, `decreto3046`, "a R1 pode fechar (não há isenção de 5 anos)": ERRADO.** A isenção existe na **LC 270, Art. 110** (p. 40), e não no Art. 106. Tem exceção no §8º. Nem eu nem o Hely lemos o artigo vizinho.
- **Item 3, `legal-oodc`, "a fórmula está na LC 281 Art. 18 §1º, não num Anexo XXV": INCOMPLETO.** A fórmula da OODC pura é a **Fórmula 1 do Anexo XXV** (LC 270, Art. 111). O Art. 18 §1º é a fórmula do outro regime, o da LC 281. A Skill misturava os dois. Corrigi separando os dois regimes.
- **Item 3, `varandas`, "o Dec. 3.046 VII é mais restritivo": vale para multifamiliar.** Para a casa unifamiliar, a última frase do VII remete ao **XI**, que é permissivo. O ponto continua em aberto.
- As correções foram aplicadas nas Skills e nos POPs (livro-razão de Outubro, 01/10/2026).

## 5. Paradas obrigatórias respeitadas
Nada foi protocolado ou enviado, e nenhum órgão, condomínio ou cliente foi contatado. As respostas ao cliente são **texto para revisão** e não saem daqui sem Claudemberg (POP-GESTOR-LEGAL-01 §7). Toda conclusão de mérito é **análise preliminar**.

— Kelsen, Gestor Legal, 01/10/2026
