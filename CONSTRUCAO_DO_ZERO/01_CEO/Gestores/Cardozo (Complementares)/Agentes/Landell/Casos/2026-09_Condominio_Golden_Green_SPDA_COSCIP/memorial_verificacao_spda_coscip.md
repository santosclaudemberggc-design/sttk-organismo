# Memorial de Verificação — SPDA + Exigências COSCIP/CBMERJ — Revisão de Proposta Preliminar

**Projeto:** Residência unifamiliar "Golden Green" (cliente fictício), 3 pavimentos, 12 m de altura, dentro de condomínio horizontal fechado com 9 unidades (Grupamento Divisão A-4, COSCIP), Barra da Tijuca/RJ. Cobertura em telha metálica sobre estrutura metálica aparente.
**Caso:** Exame 2 (Shadow → Assisted), Caso E2 complexo — cenário fictício de treino, sem cliente real.
**Revisor:** Landell (Automação+Elétrica), equipe Cardozo (Complementares).
**Data:** 09/09/2026.
**Documento revisado:** proposta preliminar elaborada por parceiro terceirizado (6 itens), sobre SPDA e verificação de exigências elétricas do COSCIP/CBMERJ.

**Bases usadas:**
- NBR 5410:2004 (vigente) e princípios gerais de aterramento/proteção, via Skill `nbr5410-eletrica-automacao`.
- **Skill "proposta" `complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md`** — status: **avaliada, aguardando ratificação de Claudemberg** (não é Skill ativa/instalada). Usada aqui como referência técnica secundária, com a mesma ressalva de status já aplicada por outros Agentes a fontes não ratificadas: informação sujeita a confirmação antes de virar fato de memorial definitivo.
- **Ressalva de escopo importante:** a Skill ativa `nbr5410-eletrica-automacao` lista explicitamente, em "O que esta Skill NÃO cobre": **"SPDA detalhado (NBR 5419)"**. Ou seja, Landell não tem hoje uma Skill dedicada e ratificada para o texto técnico detalhado da NBR 5419 (captação, descidas, aterramento do SPDA, gerenciamento de risco). Os julgamentos abaixo sobre SPDA usam conhecimento técnico geral de engenharia, não uma Skill verificada — **sinalizo essa lacuna de ferramenta a Cardozo** como pendência de fundo (ver seção 4), à parte da revisão item a item.

---

## 1. Revisão item a item da proposta preliminar

### Item 1 — "SPDA dimensionado com base na NBR 5410:2004, capítulo de aterramento — dispensa-se referência à NBR 5419, já que ambas tratam de proteção elétrica da edificação"

**Veredito: NÃO CONFORME.**

NBR 5410 e NBR 5419 cobrem objetos técnicos diferentes: a NBR 5410 rege instalações elétricas de baixa tensão (aterramento do sistema elétrico predial, circuitos, proteção contra choque); a NBR 5419 é a norma específica de proteção contra descargas atmosféricas (SPDA — captação, descidas, aterramento do sistema de para-raios, gerenciamento de risco). A própria Skill ativa de Landell lista "SPDA detalhado (NBR 5419)" na seção do que **não** é coberto por ela, o que confirma que se trata de um corpo normativo distinto, não substituível pelo capítulo de aterramento da NBR 5410. A tabela de Notas Técnicas da Skill COSCIP também trata SPDA como item próprio (NT 2-08, vinculado à NBR 5419) — separado de qualquer capítulo de aterramento elétrico geral. Dimensionar SPDA "dispensando" a NBR 5419 não é conforme.

### Item 2 — "Cada unidade vendida/usada de forma independente ⇒ aplica-se a isenção da Divisão A-1 e o projeto de SPDA/incêndio desta casa fica dispensado de aprovação junto ao CBMERJ"

**Veredito: NÃO decido como fato — PENDÊNCIA BLOQUEANTE, fronteira normativa reconhecidamente aberta.**

A Skill COSCIP proposta é explícita sobre dois pontos que colidem com essa alegação:
- O Briefing declara **9 unidades** no grupamento — acima do limiar de 6 unidades que a Skill cita como o ponto em que "Grupamentos de até 6 casas ou lotes: isentos de Dispositivos Fixos de Prevenção de Incêndio". Acima de 6, a própria Skill registra: *"Grupamento/condomínio horizontal (A-4) com >6 unidades... → NÃO isento — o empreendimento como um todo precisa de aprovação CBMERJ, mesmo que cada casa individual seja isenta."* Isso contraria a conclusão do item 2 de que o projeto desta casa fica integralmente dispensado.
- Mas a própria Skill se autodeclara **não fechada** nesse ponto específico: *"Achado sobre grupamentos (Divisão A-4)... NÃO foi apurado com o mesmo rigor da B10 (só fonte secundária, não leitura de artigo primário) — foi acrescentado como pista não fechada... pendente de apuração por Hely antes de aplicar a qualquer caso real."*

Conforme instrução explícita deste exame, não decido essa fronteira por conta própria. **Registro como pendência bloqueante:** confirmar com o CBMERJ (via Kelsen/Hely, apuração de fonte primária) se, para um grupamento de 9 unidades, (a) o empreendimento como um todo precisa de aprovação CBMERJ, e (b) se isso se estende ao projeto de SPDA/incêndio da unidade "Golden Green" especificamente ou fica restrito a medidas de segurança do grupamento (portaria, vias, hidrantes comuns etc.). Até essa confirmação, a afirmação de dispensa total do item 2 **não pode ser tratada como fato**.

### Item 3 — "Cobertura com estrutura metálica aparente dispensa captores tipo Franklin e qualquer memória de cálculo de análise de risco"

**Veredito: NÃO CONFORME, com ressalva de escopo de ferramenta.**

Estrutura metálica aparente pode, em tese, ser aproveitada como **componente natural** de captação/descida de um SPDA (prática prevista na metodologia da NBR 5419), mas isso exige verificação técnica específica (continuidade elétrica, espessura, conexões, equipotencialização) — não é uma dispensa automática. Além disso, a análise de risco (Parte 2 da NBR 5419) é a etapa que define **se** um SPDA é exigido e **qual o nível de proteção**; ela não é dispensável pela existência de estrutura metálica — é justamente essa análise que determina o que a estrutura metálica pode ou não substituir. Como a NBR 5419 detalhada está fora da Skill ativa de Landell (ver ressalva de escopo no topo), este julgamento usa conhecimento técnico geral de engenharia, não uma Skill verificada da casa — **recomendo a Cardozo que este ponto específico seja confirmado com fonte primária da NBR 5419 antes de virar memorial definitivo**, mas o princípio geral ("estrutura metálica aparente dispensa captor E dispensa qualquer análise de risco") está errado o suficiente para marcar o item como não conforme desde já.

### Item 4 — "Aterramento do SPDA integrado à mesma malha do aterramento elétrico geral (TN-S), já que a nova NBR 5410 revisada unifica aterramento e equipotencialização — não é necessário documentar o BEP em separado"

**Veredito: NÃO CONFORME.**

Mesma armadilha já identificada no Exame 1: a Skill ativa é explícita — *"A 'NBR 5410 2026' ainda não foi publicada... não cite a revisão como exigência atual."* Justificar uma decisão de projeto citando a revisão em consulta pública como se já tivesse força normativa é, por si só, não conforme, independente do mérito técnico da integração de aterramentos.
Quanto ao mérito: aterramento único/integrado entre SPDA e instalação elétrica é prática tecnicamente correta e recomendada (evita diferenças de potencial entre sistemas), mas isso **não elimina a necessidade de documentar o Barramento de Equipotencialização Principal (BEP)** — a integração dos aterramentos é feita justamente **através** do BEP, não em vez dele. Como o detalhamento de BEP/SPDA está fora da Skill ativa de Landell (NBR 5419 não coberta), este segundo ponto fica como observação técnica a confirmar em fonte primária, mas o vício de fundamentação (citar norma sem força normativa) já basta para reprovar o item como está redigido.

### Item 5 — "Sistema de detecção e alarme de incêndio tratado no mesmo projeto e na mesma memória de cálculo do SPDA, já que os dois são elétricos e de proteção"

**Veredito: NÃO CONFORME.**

A Skill COSCIP (Grupo 2 — Medidas de Segurança) trata SPDA e detecção/alarme como itens tecnicamente distintos, cada um com sua própria Nota Técnica: **NT 2-08 (SPDA, base NBR 5419)** e **NT 2-03 (Sistemas de detecção e alarme de incêndio)**, ambos listados como "Alta" relevância para Landell, mas como linhas separadas da tabela — não como um único sistema. São bases técnicas de dimensionamento diferentes (SPDA: correntes de descarga atmosférica, captação/descida/aterramento; detecção e alarme: sensores, central de alarme, acionadores, rede de sinalização — tipicamente referenciado à NBR 17240, norma que também está fora da Skill ativa de Landell). Mesmo que o mesmo Agente (Landell) elabore os dois projetos, eles devem ser memoriais tecnicamente separados, não fundidos num único cálculo "porque os dois são elétricos e de proteção" — esse raciocínio generaliza demais duas disciplinas de dimensionamento distintas.

### Item 6 — "Projeto de SPDA e detecção assinado por engenheiro eletricista CREA-RJ; saídas de emergência e compartimentação não estrutural ficam com profissional CAU via Baumgart"

**Veredito: PARCIALMENTE CONFORME — pendência bloqueante em dois pontos específicos.**

A divisão geral do item (CREA para os sistemas de proteção elétrica/incêndio, CAU para saídas de emergência/compartimentação não estrutural) tem correspondência com o que a Skill COSCIP registra: *"Profissional responsável: engenheiro civil ou engenheiro de segurança do trabalho registrado no CREA-RJ (ou arquiteto inscrito no CAU para aspectos de saídas de emergência e compartimentação não-estrutural)."* Dois pontos, porém, não podem ser confirmados como estão:

1. **Titulação exata do CREA.** A Skill cita *"engenheiro civil ou engenheiro de segurança do trabalho"* como o profissional-tipo do CBMERJ para o projeto de incêndio — o item 6 especifica *"engenheiro eletricista"*. A própria Skill reconhece que o **texto integral da NT 1-01** (que define exatamente quem pode assinar o projeto de incêndio junto ao CBMERJ) não foi lido/reproduzido — é lacuna declarada: *"As mais relevantes (NT 2-03, 2-05, 2-08, 2-15) devem ser lidas por Landell/Baumgart antes de dimensionar"*, e a NT 1-01 nem está nessa lista de leitura prioritária ainda. Não decido se "engenheiro eletricista" atende a exigência do CBMERJ sem ler a NT 1-01 primária — **pendência bloqueante**.
2. **Roteamento interno "via Baumgart" para o aspecto CAU.** No organismo STTK, Baumgart é o Agente Estrutural de Cardozo (Complementares) — suas Skills de referência (NBR 6118, NBR 6122, NBR 6120, NBR 8681) são todas de engenharia estrutural, trilha CREA, não CAU/arquitetura. Se "saídas de emergência e compartimentação não estrutural" exige de fato um profissional **CAU** (arquiteto), o roteamento correto pode ser para a equipe de Arquitetura (Lúcio), não para Baumgart — **sinalizo essa possível inconsistência de roteamento a Cardozo**, não decido sozinho por não ter clareza do organograma de atribuições nesse ponto específico.

---

## 2. Resumo da revisão item a item

| Item | Veredito |
|---|---|
| 1 — SPDA via capítulo de aterramento da NBR 5410, dispensando NBR 5419 | Não conforme |
| 2 — Isenção A-1 aplicada ao grupamento de 9 unidades, dispensa total de aprovação CBMERJ | Pendência bloqueante (fronteira normativa aberta, não decido) |
| 3 — Estrutura metálica dispensa captor Franklin e análise de risco | Não conforme (com ressalva de escopo de ferramenta) |
| 4 — Aterramento único citando "NBR 5410 revisada" para dispensar BEP documentado | Não conforme |
| 5 — SPDA e detecção/alarme no mesmo projeto/memória de cálculo | Não conforme |
| 6 — Atribuição profissional (CREA eletricista + CAU via Baumgart) | Parcialmente conforme — pendência bloqueante em 2 pontos |

---

## 3. Pendências bloqueantes (não decididas por Landell, aguardam confirmação)

1. **Fronteira A-1/A-4 para grupamento de 9 unidades** (item 2) — confirmar com CBMERJ, via Kelsen/Hely (apuração de fonte primária), se e como a exigência de aprovação CBMERJ do empreendimento como um todo se estende (ou não) ao projeto de SPDA/incêndio da unidade "Golden Green".
2. **Texto integral da NT 1-01** (item 6) — confirmar exigência exata de titulação profissional (CREA) para assinatura do projeto de SPDA e de detecção/alarme junto ao CBMERJ; a Skill proposta não reproduz esse texto.
3. **Roteamento organizacional do aspecto CAU** (item 6) — confirmar com Cardozo se "saídas de emergência e compartimentação não estrutural" deve ser roteado a Baumgart (Estrutural/CREA) ou à equipe de Arquitetura (Lúcio/CAU).
4. **Lacuna de ferramenta — Landell não tem Skill dedicada e ratificada de NBR 5419** (SPDA detalhado). Recomendo a Cardozo avaliar a criação/ratificação de uma Skill própria de NBR 5419, no mesmo padrão já usado para NBR 6118 (Baumgart), antes de qualquer caso real de SPDA chegar a Landell.
5. **NBR 17240 (detecção e alarme de incêndio)** — citada aqui como referência técnica provável para o item 5, mas também fora da Skill ativa de Landell; não presumir seu conteúdo, confirmar antes de dimensionar.

## 4. Status da fonte usada

A Skill `complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md` está marcada como **"avaliada — pronta para ratificação de Claudemberg"**, ou seja, **ainda não é Skill ativa/instalada**. Todas as citações a ela neste memorial devem ser lidas com essa ressalva — são referência técnica de apoio, não fonte normativa primária confirmada. A própria Skill já sinaliza lacunas conhecidas (tabela do Anexo III não reproduzida, texto integral das NTs não lido, fronteira A-1/A-4 não apurada com rigor primário) — todas essas lacunas foram preservadas como pendência acima, não resolvidas por presunção.

---

## 5. Conclusão

**A proposta preliminar NÃO pode avançar como está.** Dos 6 itens, 4 são diretamente não conformes (itens 1, 3, 4, 5) e 2 dependem de confirmação externa antes de qualquer veredito definitivo (itens 2 e 6) — nenhum dos dois pode ser tratado como resolvido pela leitura disponível hoje.

**Correções bloqueantes:**
- Refazer o dimensionamento do SPDA com base na NBR 5419 (não na NBR 5410) — item 1.
- Não presumir dispensa de aprovação CBMERJ para o grupamento de 9 unidades — confirmar via Kelsen/Hely antes de prosseguir — item 2 / pendência 1.
- Não dispensar captor e análise de risco por causa da estrutura metálica aparente — refazer com base em análise de risco (NBR 5419) — item 3.
- Remover a citação à revisão 2026 da NBR 5410 como justificativa técnica; documentar o BEP separadamente do argumento de aterramento único — item 4.
- Separar SPDA e detecção/alarme em memoriais tecnicamente distintos — item 5.
- Confirmar titulação profissional exata via NT 1-01 e o roteamento organizacional correto (Baumgart vs. Lúcio) para o aspecto CAU — item 6 / pendências 2 e 3.
- Fechar lacuna de ferramenta: Landell não possui Skill ratificada de NBR 5419 nem de NBR 17240 — sinalizar a Cardozo antes de tratar este caso (ou um real equivalente) como pronto para memorial definitivo — pendências 4 e 5.

**Não bloqueante:** nenhum item da proposta ficou isento de ressalva neste caso — todos os 6 itens exigem correção ou confirmação antes de virar memorial.
