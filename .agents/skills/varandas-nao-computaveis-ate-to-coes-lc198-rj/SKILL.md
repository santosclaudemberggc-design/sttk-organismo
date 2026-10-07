---
name: varandas-nao-computaveis-ate-to-coes-lc198-rj
description: Varandas e sacadas não computáveis na ATE e na Taxa de Ocupação no Rio de Janeiro — COES (LC 198/2019) Art. 8º §§1º-11 + Decreto 45.917/2019 Art. 6º — distâncias à testada e às divisas, brise vazado ≥ 50%, laje técnica de ar-condicionado, envidraçamento retrátil sem licença, e a brecha de área útil fora da conta. Use sempre que Hely montar quadro de áreas/DULI, ou Oscar/Lúcio definir varanda, sacada, terraço de cobertura ou brise em projeto residencial no RJ — mesmo que o pedido só mencione "área computável", "ATE", "taxa de ocupação", "varanda" ou "fechamento de varanda", sem citar o COES pelo nome.
version: v1.2
status: ativa-com-ressalva
data: 2026-09-28
atualizado: 2026-10-01 (v1.2, Kelsen, ordem de Claudemberg após o Ensaio Sombra 003. Nova §4.1 sobre o regime da ZPP: Dec. 3.046/81 VII e XI. Backup em 01_CEO/Decisoes_Autonomas/_backups/2026-10-01/kelsen_ANTES_varandas-nao-computaveis-ate-to-coes-lc198-rj_SKILL_instalada.md)
tipo: Inteligência (Trilha A)
gestor_alvo: Kelsen (Legal)
agente_principal: Hely (Projeto Legal: quadro de áreas, DULI)
agentes_cross: Oscar/Lúcio (partido e fachada), Baumgart (balanço), Tenreiro (fechamento com vidro retrátil)
validacao: Kelsen 28/09/2026 — PROCEDE COM RESSALVA (C1-C3 aplicadas na v1.1; R1-R4 registradas abaixo)
---

# Skill: Varandas e Sacadas Não Computáveis na ATE e na Taxa de Ocupação (COES, LC 198/2019, Art. 8º)

> ⚠️ RESSALVA DE FONTE — (1) Conferido no texto consolidado oficial da SMU (PDF de 07/01/2026, arquivado em `Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`): o Art. 8º não tem alteração. O COES só foi alterado pela LC 283/2025 (Art. 35 §7º) e pela LC 291/2025 (Art. 2º §7º). Falta conferir, na Busca Fácil, se existe ato posterior a 07/01/2026. (2) **Confirmado em 01/10/2026:** a Barra/Recreio (ZPP, Dec. 3.046/81 incorporado pela LC 270/2024) **tem regra própria** de varanda, que está na §4.1. Ainda não se sabe qual regra prevalece quando o COES e o Dec. 3.046 divergem, e isso vai ao Gate do Maurício. Em caso real, o Hely confirma a subzona no RIU e trata o benefício como provisório até lá.

## 1. POR QUE ESSA SKILL EXISTE

Em lote onde cada m² de ATE é disputado, saber **o que não entra na conta** vale tanto quanto saber o CA. O COES diz, em texto primário, que **varanda e sacada de unidade residencial, em balanço ou reentrante, não entram nem na ATE nem na Taxa de Ocupação**. Poucos exploram isso até o limite.

**Correção de rota interna:** a Skill de Lúcio `arquitetura_partido-conforto-termico-orientacao-solar-tipologias-rj.md` (16/09, linhas 70-72) diz "área máxima: 20% da área útil (não computa no CA)" e "projeção máxima 2 m (Decreto 7336/1988)". **No texto do COES, o limite de 20% vale para edificação NÃO residencial (§5º)**, não para residencial (§4º, sem limite de área). O Art. 8º controla varanda por distância à testada e às divisas, não por projeção. Ver seção 6.

## 2. O TEXTO QUE IMPORTA (LC 198/2019, Art. 8º, e Decreto 45.917/2019)

| Dispositivo | Regra | Uso prático |
|---|---|---|
| Art. 8º caput | Permite varandas e sacadas **abertas**, em balanço ou reentrantes | Precisa ser aberta para valer o benefício |
| §1º | Sobre o afastamento **frontal**: pode ocupar toda a fachada, recuando **≥ 1,00 m da testada** | Varanda avança sobre o recuo frontal |
| §2º | Sobre os afastamentos **lateral e de fundos**: toda a fachada, a **≥ 2,50 m das divisas** | |
| §3º | Edificação **não afastada** das divisas: **≥ 1,50 m** das divisas laterais e de fundos | Onde os projetos mais reprovam (já registrado em `legal-base-legislativa-bairro`) |
| **§4º** | **Varandas e sacadas de unidades residenciais, em balanço ou reentrantes, não são computadas na ATE e na Taxa de Ocupação** | O benefício. Sem limite de área escrito no artigo |
| §5º | Não residencial / parte não residencial de misto: não computa **até 20% da área útil** | O limite de 20% é daqui, não do residencial |
| §6º | Permite churrasqueira, fechamento lateral do piso ao teto e brise, veneziana, treliça, cobogó ou muxarabi, **desde que vazados com ≥ 50% de aeração do vão**; não conta como fechamento se feito na construção ou em reforma geral de fachada | Proteção solar sem perder o benefício (ligar com `lucio-protecao-solar-externa-dispositivos-rj`) |
| §7º | A laje de teto da varanda do último pavimento pode virar **terraço descoberto** da cobertura, quando a cobertura for permitida | Área de lazer na cobertura |
| §8º | Laje técnica em balanço para ar-condicionado, **até 1,00 m** do plano da fachada | Tira a condensadora da varanda |
| §9º | Varanda acrescida a prédio com Habite-se há **> 5 anos** pode ter pilar no afastamento (seção ≤ 35×35 cm, ≤ 1,50 m da fachada, com autorização condominial e solução uniforme em toda a fachada) | Retrofit, fora do foco STTK (construção do zero) |
| §10 | Fechamento **sem licenciamento** só com vidro totalmente retrátil, sem esquadria, sem incorporar a varanda aos cômodos (LC 145/2014) | O cliente pode envidraçar depois sem perder o enquadramento |
| §11 | Qualquer outro fechamento segue a LC 192/2018 (contrapartida) | Fechar de outro jeito vira área computável e paga |
| **Dec. 45.917/2019, Art. 6º** | Entre edificações: **≥ 5,00 m entre varandas projetadas sobre o afastamento** | Grupamentos/condomínios com várias casas no mesmo lote |

## 3. A BRECHA VÁLIDA (como o profissional experiente usa)

1. **Varanda generosa é área útil fora da conta.** Numa unifamiliar com CA justo, uma varanda reentrante no social cria uma "sala externa" que não consome ATE nem TO, desde que continue **aberta**. **Limite:** varanda reentrante com mais de 1,50 m de profundidade que ventila ou ilumina um cômodo passa a ser calculada como prisma (COES, Art. 5º §5º). Confira com `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj` antes de aprofundar.
2. **Varanda também anda sobre o afastamento** (§1º a §3º): a projeção avança sobre o recuo frontal até 1 m da testada. Na Barra, onde os afastamentos frontais costumam ser grandes, isso é muito espaço.
3. **Brise vazado ≥ 50% não "fecha" a varanda** (§6º). Na fachada poente, dá para sombrear de verdade sem perder o enquadramento. **Não confunda os regimes:** brise sobre afastamento **fora** da varanda segue o COES, Art. 4º §3º (no máximo 1 m da fachada, vazado, sem virar piso utilizável).
4. **Condensadora fora da varanda** (§8º): a laje técnica de 1 m não precisa roubar área da varanda.
5. **Envidraçamento posterior sem licença** (§10), desde que retrátil e sem incorporar a varanda. Explique ao cliente que **transformar a varanda em sala** (derrubar a esquadria interna) tira o benefício e cai na LC 192/2018.

**Limite ético/legal:** "reentrante" não é quarto disfarçado. Varanda com esquadria interna removida em projeto, ou com vedação que impede a aeração, **é área computável**. Hely não monta quadro de áreas que conte como varanda um espaço que funciona como cômodo. É a responsabilidade técnica de Claudemberg (CAU/RRT) que está em jogo.

## 4. ATENÇÃO NA BARRA/RECREIO

- O lote pode estar sob o regime da **LC 270/2024, que incorporou o Decreto 3046/81** (Skill `decreto3046-81-lc270-2024-licin-barra-recreio`), com parâmetros próprios por subzona. **Antes de contar com o §4º, Hely confirma na SMDU/RIU se a subzona tem regra própria de cômputo de varanda** (R1).
- Condomínios da Barra costumam ter **regulamento construtivo próprio**, mais restritivo que a lei (caso Daniel-OB, Anexo II). A varanda pode ser legal e mesmo assim barrada pelo condomínio. É matéria civil: sinalize ao cliente.
- Em caso real, tudo é análise preliminar até passar pelo **Gate do Maurício** (R4).

### 4.1 O regime da ZPP: Dec. 3.046/81, Disposições Gerais VII e XI (lido por Kelsen em 01/10/2026, `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`, pp. 2-3)

| Situação na ZPP | Regra | Diferença em relação ao COES |
|---|---|---|
| **Multifamiliar e outros usos (VII)** | Varandas abertas, cobertas ou descobertas, **não computam** na ATE, na área útil mínima nem na TO. Devem **respeitar o afastamento frontal mínimo** da subzona, **sem balanço sobre ele** | **Mais restritivo** que o COES Art. 8º §1º, que deixa a varanda avançar até 1,00 m da testada |
| **Casa unifamiliar (VII, última frase -> XI)** | O VII termina com "Nos casos de edificações residenciais unifamiliares será aplicado o disposto no inciso XI". O **XI** permite, com **frontal menor que 10,00 m**, ocupar os **afastamentos laterais do térreo** com **varandas ou abrigos de veículos**, abertos e cobertos por **telha-vã**, fora da ATE e da TO | **Mais permissivo** que o COES §2º e §3º no térreo lateral, mas só nessas condições |
| **Saliência na fachada (XIV)** | Até 0,40 m sobre o afastamento frontal, acima do térreo, só para jardineira e ar-condicionado, fora da ATE e da TO | Parecido com a laje técnica do §8º do COES, com limite menor |

**Em aberto (Gate do Maurício; até lá, leitura conservadora):**
- a vedação de balanço sobre o afastamento frontal do VII também vale para a **unifamiliar**, ou o XI substitui o VII por inteiro para a casa? **Até decidir: não projetar varanda de casa em balanço sobre o afastamento frontal mínimo na ZPP.**
- quando o COES (lei geral posterior) e o Dec. 3.046 (regime especial preservado pela LC 270) dizem coisas diferentes, qual prevalece? Hoje, aplicar o **mais restritivo** dos dois em cada ponto, salvo o benefício expresso do XI.

**Erro registrado:** na validação de 28/09 e na auditoria do Ensaio 003, eu (Kelsen) disse "o Dec. 3.046 VII é mais restritivo que o COES §1º" sem ler a última frase do VII. Para a casa unifamiliar, que é o nosso caso, o VII manda aplicar o XI. A regra serve para multifamiliar; para a casa é tensão em aberto.

## 5. CHECKLIST DE HELY (quadro de áreas)

- [ ] A varanda é aberta (sem esquadria que a incorpore ao cômodo)?
- [ ] Em balanço ou reentrante? Unidade residencial?
- [ ] Distâncias: ≥ 1,00 m da testada; ≥ 2,50 m (afastada) ou ≥ 1,50 m (não afastada) das divisas laterais e de fundos
- [ ] Grupamento: ≥ 5,00 m entre varandas sobre o afastamento entre edificações (Dec. 45.917/2019, Art. 6º)
- [ ] Reentrante com > 1,50 m de profundidade servindo cômodo? Então vira prisma (COES, Art. 5º §5º)
- [ ] Brise/cobogó com ≥ 50% de aeração, se houver
- [ ] Subzona da LC 270/2024 (Dec. 3046/81 incorporado) com regra própria de cômputo? (RIU/SMDU)
- [ ] Lote na ZPP? Aplicar a §4.1: ler o Dec. 3.046 VII **até a última frase**. Unifamiliar segue o XI (frontal < 10 m, lateral do térreo, aberto, telha-vã). Sem balanço sobre o frontal mínimo até o Gate
- [ ] Regulamento do condomínio conferido
- [ ] Varanda lançada **fora** da ATE e da TO no quadro de áreas, com citação do Art. 8º §4º da LC 198/2019

## 6. PENDÊNCIA GERADA (para Lúcio)

A Skill de partido de 16/09 (`arquitetura_partido-conforto-termico-orientacao-solar-tipologias-rj.md`, em proposta) aplica ao residencial o limite de 20% do §5º (não residencial) e cita uma projeção máxima de 2 m (Decreto 7336/1988) sem conferir. Kelsen (28/09) concorda com a correção e recomenda **retirar** a linha dos 2 m até alguém conferir o decreto de 1988. Lúcio corrige para: "residencial: não computa na ATE nem na TO (LC 198/2019, Art. 8º §4º), sem limite de área no artigo; 20% vale só para não residencial (§5º)".

**Remissão cruzada sugerida por Kelsen:** acrescentar em `legal-base-legislativa-bairro` (linha 85, Art. 8º §3º) uma remissão a esta Skill. Fica para a Drenagem/Kelsen, com backup.

## 7. RESSALVAS DA VALIDAÇÃO (Kelsen, 28/09/2026)

- **R1 (parcialmente fechada em 01/10/2026):** a regra própria da ZPP existe e está na §4.1 (Dec. 3.046 VII, XI e XIV, lidos no primário). Continuam abertos: o alcance da vedação frontal do VII sobre a unifamiliar; qual prevalece, COES ou Dec. 3.046, nos pontos em que divergem; a remissão ao COES Art. 1º §3º, que não foi conferida; e os decretos olímpicos (LC 270, Art. 111 §5º) que possam ter mexido na subzona.
- **R2:** limite de profundidade da varanda reentrante que serve cômodo (COES, Art. 5º §5º), incorporado na seção 3.
- **R3:** brise sobre afastamento fora da varanda segue o Art. 4º §3º, incorporado na seção 3.
- **R4:** Gate do Maurício antes de parecer final; o condomínio pode ser mais restritivo.

## 8. FONTES

- **COES (LC 198/2019) consolidado oficial da SMU**, PDF gerado em 07/01/2026, pp. 5-6 (lido por Kelsen 28/09/2026): `01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\Fontes_Legislacao\COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`
- **Decreto 45.917/2019** (regulamenta o COES), Art. 6º (lido por Kelsen 28/09/2026): `...\Fontes_Legislacao\Decreto45917_2019_RegulamentaCOES.pdf`
- **Decreto 3.046/1981**, Instruções Normativas, Disp. Gerais VII, XI, XIV e XXIII (lido por Kelsen em 01/10/2026, pp. 2-4): `...\Fontes_Legislacao\Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`
- LC 198/2019, Art. 8º, texto original, Câmara Municipal RJ (lido 28/09/2026): https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/c1982019.html
- LC 198/2019, LegisWeb (lido 28/09/2026, §6º a §11): https://www.legisweb.com.br/legislacao/?id=373951
- Dicionário de Termos Técnicos da LC 270/2024, 2ª ed., dez/2025, SMDU (consultado: não define o cômputo de varanda): https://desenvolvimentourbano.prefeitura.rio/wp-content/uploads/sites/52/2025/12/Dicionario-de-Termos-LC-270-2a-edicao-04_12_2025.pdf
- Pesquisa: Rotina Diária Skills v3.2, 28/09/2026 (Wallenberg). Validação: Kelsen, 28/09/2026
