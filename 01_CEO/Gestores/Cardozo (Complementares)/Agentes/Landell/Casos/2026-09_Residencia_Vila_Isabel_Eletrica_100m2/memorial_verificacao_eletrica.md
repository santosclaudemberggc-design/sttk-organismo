# Memorial de Verificação Elétrica — Revisão de Proposta Preliminar

**Projeto:** Residência térrea "Vila Isabel/RJ" (cliente fictício) — Construção do Zero, 100 m².
**Caso:** Exame 2 (Shadow → Assisted), Caso E1 simples — cenário fictício de treino, sem cliente real.
**Revisor:** Landell (Automação+Elétrica), equipe Cardozo (Complementares).
**Data:** 09/09/2026.
**Documento revisado:** proposta preliminar elaborada por parceiro terceirizado (6 itens), entregue para verificação item a item antes de virar memorial definitivo.
**Base normativa:** NBR 5410:2004 (vigente — única com força normativa hoje), via Skill `nbr5410-eletrica-automacao`.

---

## 1. Dados de partida (Briefing aprovado por Cardozo)

- Programa: 2 quartos + 1 suíte, sala/cozinha integrada, área de serviço externa coberta, banheiro social, banheiro de suíte, garagem descoberta (1 vaga) — 7 ambientes.
- Chuveiro elétrico da suíte: **5.500 W** (informado).
- Chuveiro do banheiro social: **potência não informada**.
- Automação: nenhuma solicitada — fora de escopo deste caso.
- Fornecimento: **monofásico 127 V, a confirmar com a Light**.

---

## 2. Revisão item a item da proposta preliminar

### Item 1 — "Toda a iluminação da casa (7 ambientes) em um único circuito de 15 A"

**Veredito: NÃO CONFORME.**

A NBR 5410:2004 exige divisão de circuitos por finalidade e por área/cômodo, justamente para limitar a extensão de um defeito (curto, sobrecarga, falha de disjuntor) a apenas parte da instalação — não à casa inteira. A Skill `nbr5410-eletrica-automacao` registra explicitamente: *"Divisão de circuitos obrigatória: iluminação (exclusivo por cômodo/área)..."*. Concentrar a iluminação de 7 ambientes distintos em um único circuito de 15 A contraria esse princípio: qualquer falha no circuito (ou desarme do disjuntor) apaga a casa inteira, o que a norma busca evitar. Precisa ser redividida por ambiente/agrupamento de ambientes, dimensionada pela carga real de cada ponto.

### Item 2 — "Banheiro social e banheiro da suíte: dispensado o DR, quadro em ambiente seco, risco considerado baixo"

**Veredito: NÃO CONFORME.**

A exigência de DR 30 mA está ligada ao ambiente onde o circuito **atende** (banheiro — área molhada, risco de choque por contato direto/indireto), não à localização do quadro de distribuição. A Skill é direta: *"DR (30mA) obrigatório em banheiro, área de serviço e cozinha."* — sem exceção por secura do local do quadro. Este é o mesmo tipo de armadilha já barrada no Exame 1 (tentativa de dispensar DR por raciocínio de tensão/ambiente do quadro em vez do ambiente atendido pelo circuito).

### Item 3 — "Chuveiro da suíte (5.500 W) dividindo o mesmo circuito de 20 A com as tomadas de uso geral do banheiro"

**Veredito: NÃO CONFORME — item de maior risco da proposta.**

Duas violações independentes:
1. **Circuito TUE não pode ser compartilhado.** A Skill exige *"TUE (tomada de uso específico, circuito exclusivo por equipamento — chuveiro, ar-condicionado, forno)"*. Chuveiro é sempre circuito exclusivo, nunca dividido com TUG.
2. **O disjuntor de 20 A é fisicamente incompatível com a carga informada, mesmo isolado.** Corrente de projeto do chuveiro a 127 V: IB = P/V = 5.500 W / 127 V ≈ **43,3 A**. Um disjuntor de 20 A nem sequer sustenta o chuveiro sozinho — desarmaria continuamente ou, se substituído por um de maior capacidade sem redimensionar o condutor, geraria sobreaquecimento. Não há "folga de corrente" nesse disjuntor: a proposta partiu de premissa numérica errada.

### Item 4 — "Aterramento TN-C, reaproveitando o condutor PEN da rede aérea da concessionária"

**Veredito: NÃO CONFORME.**

A Skill registra: *"Aterramento e proteção: sistema TN-S recomendado em obra nova."* Construção do zero deve adotar TN-S (condutor de proteção PE separado do neutro dentro da instalação), não reaproveitar o PEN da concessionária como esquema interno TN-C. Usar TN-C dentro da edificação nova elimina a separação PE/N exigida para proteção adequada contra contatos indiretos e não é a prática recomendada para obra nova.

### Item 5 — "Cabos LSHF (não halogenados) na cozinha e área de serviço"

**Veredito: CONFORME (item aceitável, não obrigatório nesses ambientes específicos).**

A Skill cita *"Cabos LSHF recomendados em áreas de escape"* — cozinha e área de serviço não são tecnicamente "áreas de escape/rotas de fuga" no sentido estrito da norma, então o item não decorre de uma exigência específica da NBR 5410 para esses ambientes. Ainda assim, não contraria a norma: é um reforço voluntário de segurança contra propagação de incêndio, sem custo relevante, como o próprio parceiro observou. Não bloqueia avanço do projeto.

### Item 6 — "Carga de tomadas da cozinha dividida em 2 circuitos de TUG distintos, por ultrapassar 1.500 W somados nas tomadas de bancada"

**Veredito: CONFORME.**

A Skill fixa: *"Potência máxima por circuito monofásico: 1.500W em TUG."* Ultrapassar esse limite nas tomadas de bancada da cozinha e dividir em 2 circuitos de TUG é a aplicação correta da regra. Item sem ressalva.

---

## 3. Pendências bloqueantes (dado não informado no Briefing)

1. **Potência do chuveiro do banheiro social — não informada.** Sem esse dado não é possível dimensionar IB, escolher disjuntor (In) nem seção de condutor (Iz) desse circuito TUE. Não presumido por Landell — precisa ser fornecido por Cardozo/cliente antes de fechar o memorial de cálculo definitivo.
2. **Tipo real de fornecimento da Light — "monofásico 127 V, a confirmar".** Isso é crítico neste caso porque o chuveiro da suíte (5.500 W) resulta em ~43,3 A a 127 V — corrente de projeto elevada, que exige condutor robusto, maior queda de tensão a considerar e disjuntor de maior capacidade. Se a Light confirmar disponibilidade de circuito em 220 V (monofásico 220 V ou bifásico) para essa unidade, a solução técnica do circuito do chuveiro muda substancialmente (corrente cai para ~25 A). Landell não decide essa premissa sozinho — fica pendente de confirmação antes do dimensionamento final do circuito do chuveiro da suíte.

## 4. Notas técnicas de partida (elaboradas por Landell para o memorial definitivo, após pendências resolvidas)

- **Norma aplicável:** NBR 5410:2004 (vigente). Não há revisão publicada com força normativa em 2026 — não citar a "NBR 5410 2026" como exigência.
- **Divisão de circuitos:** iluminação separada por ambiente/agrupamento (nunca 1 único circuito para os 7 ambientes); TUG separado de iluminação; cozinha com no mínimo 2 circuitos de TUG (carga de bancada > 1.500 W, conforme item 6 aprovado); TUE exclusivo por equipamento (chuveiro suíte, chuveiro banheiro social — pendente potência).
- **Proteção:** DR 30 mA obrigatório nos circuitos que atendem banheiro social, banheiro da suíte e área de serviço (áreas molhadas); DPS no quadro de distribuição geral.
- **Aterramento:** TN-S, com condutor de proteção (PE) dedicado desde o quadro — não reaproveitar PEN da rede aérea internamente.
- **Circuito do chuveiro da suíte:** dimensionamento (IB/In/Iz) suspenso até confirmação da tensão de fornecimento com a Light (pendência 2 acima).
- **Circuito do chuveiro do banheiro social:** dimensionamento suspenso até informação da potência do equipamento (pendência 1 acima).

---

## 5. Conclusão

**A proposta preliminar NÃO pode avançar como está.** De 6 itens revisados, 4 são não conformes (itens 1, 2, 3 e 4) — sendo o item 3 o de maior risco (disjuntor fisicamente incompatível com a carga, além do compartilhamento indevido de circuito TUE). Há ainda 2 pendências bloqueantes de dado não informado no Briefing.

**Correções bloqueantes (impedem virar memorial definitivo):**
- Redividir a iluminação por ambiente (item 1).
- Reincluir DR 30 mA nos dois banheiros (item 2).
- Isolar o circuito do chuveiro da suíte como TUE exclusivo e redimensionar disjuntor/condutor pela corrente real (item 3).
- Trocar o esquema de aterramento para TN-S (item 4).
- Obter a potência do chuveiro do banheiro social (pendência 1).
- Confirmar com a Light o tipo real de fornecimento — 127 V ou 220 V — antes de fechar o circuito do chuveiro da suíte (pendência 2).

**Não bloqueante (pode manter, é observação apenas):**
- Item 5 (LSHF em cozinha/área de serviço) — aceitável como reforço voluntário, sem exigência normativa específica para esses ambientes.

Itens conformes sem ressalva: item 6.
