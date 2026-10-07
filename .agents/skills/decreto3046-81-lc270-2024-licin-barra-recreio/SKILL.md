---
name: decreto3046-81-lc270-2024-licin-barra-recreio
description: "Base legal para licenciamento LICIN 2.0 na Barra da Tijuca e Recreio dos Bandeirantes: Decreto 3046/81 (ZE-5/Zona Plano Piloto) incorporado à LC 270/2024, e como Hely identifica os parâmetros por subzona via RIU antes de cada consulta prévia."
version: "1.3"
status: ativa-com-ressalva
created: 2026-09-21
updated: 2026-10-01
changelog:
  - "1.3 (01/10/2026, Kelsen, ordem de Claudemberg após o Ensaio Sombra 003, etapa 1). R1 reescrita: a isenção de 5 anos EXISTE, mas está no Art. 110 da LC 270, e não no Art. 106 (lido no PDF oficial, pp. 40-41). Tem exceção no §8º e transição no §1º. Checklist de OODC corrigido. Nova §6 com M3 (Dec. 3.046, Disp. Gerais VII->XI: varanda e abrigo de veículos de casa unifamiliar no afastamento lateral) e M4 (LC 270 Art. 111 §5º: decretos olímpicos prevalecem). Nova §7 sobre como checar a vigência do Dec. 3.046, que não aparece por número na Busca Fácil. Backup: 01_CEO/Decisoes_Autonomas/_backups/2026-10-01/kelsen_ANTES_decreto3046-81-lc270-2024-licin-barra-recreio_SKILL_instalada.md"
  - "1.2 (29/09/2026, Hely a pedido de Kelsen, aprovado por Claudemberg): §4 faixa de marinha e APP de lagoa conferidas em fonte primária (DL 9.760/1946 art. 2º; Lei 12.651/2012 art. 4º II; LC 270/2024 Arts. 214-215, p. 80 do PDF); acrescentada dispensa de faixa para lagoa < 10.000 m² (LC 270 Art. 215 §2º); nova §6 Macetes de quem faz. Ver R11."
  - "1.1 (28/09/2026, Kelsen, aprovado por Claudemberg): treino de 28/09. §2 fonte do RIU alinhada a mapas.rio.rj.gov.br; §3 menção 'ZPR – Zona de Proteção de Ruas' removida (sem fonte); §4 faixa de marinha reescrita (os 33 m são a própria faixa); §4 APP de lagoa marcada 'a confirmar' com distinção urbano/rural. Ver R10."
author: Rotina Diária Skills v3.2
gestor_validador: kelsen
agente_principal: hely
cross_disciplina:
  - oscar
fonte_primaria_lida: "parcial — Decreto 3046/81, Disp. Gerais I-XXIII no PDF da base (pp. 2-4, Kelsen 01/10/2026); LC 270/2024 Arts. 106-111 no PDF oficial da base (pp. 40-41, Kelsen 01/10/2026); LC 270/2024 Arts. 214-216 lidos no PDF oficial da base (pp. 79-80); DL 9.760/1946 art. 2º e Lei 12.651/2012 art. 4º lidos no planalto.gov.br (28/09/2026)"
metadata:
  tipo: Inteligência (Trilha A)
  norma_base: "Decreto 3046/81 (ZE-5) + LC 270/2024 Plano Diretor + LICIN 2.0 (Decreto 55.622/2025)"
  zona_geografica: "Barra da Tijuca, Recreio dos Bandeirantes, Baixada de Jacarepaguá — Rio de Janeiro"
  tags:
    - licin-barra
    - decreto3046
    - ze-5
    - zona-plano-piloto
    - parametros-urbanisticos
    - kelsen
    - hely
    - barra-tijuca
    - recreio
---

# Base Legal para Licenciamento LICIN 2.0 na Barra da Tijuca e Recreio
## Decreto 3046/81 (ZE-5) integrado à LC 270/2024

---

## POR QUE ESTA SKILL

Quando Kelsen/Hely recebe um projeto na Barra da Tijuca ou Recreio dos Bandeirantes, **a base legal aplicável é diferente do resto da cidade**. O LICIN 2.0 (Decreto 55.622/2025) usa como parâmetros urbanísticos os dados do Plano Diretor (LC 270/2024), que para a Barra/Recreio **manteve os parâmetros herdados do Decreto 3046/81** — publicado em 1981 especificamente para a Zona Especial 5 (ZE-5). Não conhecer essa cadeia legislativa = montar DULI com gabarito errado = exigência da prefeitura na análise.

---

## 1. A CADEIA LEGISLATIVA DA BARRA/RECREIO

```
Barra da Tijuca e Recreio dos Bandeirantes
        ↓
Zona Especial 5 (ZE-5) — Baixada de Jacarepaguá
        ↓
Decreto 3046/81 — parâmetros originais (1981)
        ↓
LC 270/2024 — novo Plano Diretor — incorporou ZE-5 como
"Zona do Plano Piloto" (ZPP) — parâmetros MANTIDOS
        ↓
LICIN 2.0 (Decreto 55.622/2025) — usa LC 270/2024 como base
        ↓
Resultado: para licenciamento na Barra/Recreio,
os parâmetros de referência são os do Decreto 3046/81
(agora chamado ZPP no PD de 2024)
```

**Ponto crítico:** o Decreto 3046/81 é um dos atos normativos mais complexos da cidade — tem dezenas de subzonas (A-1, A-2, A-17, A-18, A-20 etc.), cada uma com gabarito, índice de aproveitamento (IAA/CA), taxa de ocupação (TO) e afastamentos próprios. Não existe um parâmetro único "da Barra" — cada lote precisa ser localizado em sua subzona.

---

## 2. COMO IDENTIFICAR A SUBZONA DO LOTE

**Passo obrigatório antes de qualquer consulta prévia:**

1. Acessar o **RIU digital — SMU** (Relatório de Informações Urbanísticas)
   - Portal oficial da casa: `mapas.rio.rj.gov.br` (Certidão/Relatório de Informações Urbanísticas) — fonte oficial que vence qualquer fonte secundária
   - Inserir endereço completo ou matrícula do imóvel
   - O RIU retorna: zona (ZPP = ex-ZE-5), subzona, parâmetros aplicáveis

2. Verificar no RIU:
   - **Gabarito (G)**: número máximo de pavimentos
   - **Índice de Aproveitamento (IAA) / Coeficiente de Aproveitamento (CA)**: área construída ÷ área do lote
   - **Taxa de Ocupação (TO)**: projeção da edificação ÷ área do lote
   - **Afastamentos**: frontal, lateral, de fundos (metros)
   - **Testada mínima de lote**

3. **Exemplo de parâmetros típicos de subzona residencial** (Subzona A — valores referência, NÃO usar sem confirmar via RIU para o lote específico):
   - Gabarito: 2 pavimentos
   - IAA: 0,60
   - TO: 40%
   - Afastamento frontal: 10,00 m
   - Afastamentos laterais: dispensados quando frontal >= 10 m *(exemplo herdado da v1.0, **sem artigo e não conferido no primário**. Não confundir com o Disp. Gerais XI, que é outra regra: com frontal **menor** que 10 m, permite ocupar a lateral do térreo com varanda ou abrigo de carro, ver M3. Nem com o X: lotes de 6ª e 7ª categoria anteriores a 1969, casa encostada nas divisas com frontal >= 3 m. Vale o RIU da subzona.)*

**Atenção:** esses valores são EXEMPLOS de uma subzona residencial genérica do Decreto 3046/81. A Barra e Recreio têm subzonas comerciais, mistas, de uso especial (ZDE — Zona de Domínio Especial do Plano Piloto) e áreas de proteção ambiental, cada uma com parâmetros distintos. Nunca assumir parâmetro sem RIU.

---

## 3. PARÂMETROS QUE O NOVO PD (LC 270/2024) ALTEROU OU NÃO

### O que LC 270/2024 **MANTEVE** na Barra/Recreio

- Estrutura de subzonas com parâmetros diferenciados (agora ZPP)
- Gabaritos baixos nas subzonas residenciais (1–2 pavimentos típicos)
- Conceito do Plano Piloto de Lúcio Costa: baixa densidade, afastamentos generosos, ampla área verde

### O que LC 270/2024 pode ter **ALTERADO** (verificar via RIU por lote)

- Possibilidade de uso da **OODC / Outorga Onerosa** para ultrapassar o CA básico (ver Skill OODC)
- **TDC (Transferência do Direito de Construir)** pode ser disponível em alguns setores da Barra (ver Skill TDC/LICIN 2.0)
- Sobreposição de outros instrumentos da LC 270/2024 (ex.: AEIS) — conferir no RIU do lote

### O que NÃO mudou

- Restrições da APA do Recreio (Área de Proteção Ambiental) — regras ambientais sobrepostas ao zoneamento
- Recuo de praia / faixa de marinha em lotes de orla
- Proteção da Lagoa de Jacarepaguá e Lagoa da Tijuca (legislação ambiental estadual)

---

## 4. SOBREPOSIÇÕES LEGAIS NA BARRA/RECREIO — MAPA DE RISCO

| Condição do lote | Legislação adicional a verificar |
|---|---|
| Lote com testada para praia ou para margem de lagoa com influência de maré | Terreno de marinha (SPU): a faixa **é** a própria largura de 33 m, medidos horizontalmente para a parte da terra a partir da linha do preamar médio de 1831 — não é recuo adicional além dela. Vale também nas margens de rios e lagoas "até onde se faça sentir a influência das marés" (DL 9.760/1946, art. 2º, alínea "a" — **fonte primária lida**, planalto.gov.br, 28/09/2026). Parte do lote dentro da faixa exige regularização junto à SPU |
| Lote próximo a lagoa | APA Estadual + plano de manejo específico |
| Lote em área de antigas "Superquadras" | Normas específicas do Plano Piloto de Lúcio Costa — gabarito máximo fixo |
| Condomínio horizontal já aprovado (ex: Orla Bothanica) | Regramentos internos do Estatuto do Condomínio (Hely deve ler o Anexo II — Regramento Construtivo) |
| Área de preservação permanente (APP) | Lagoa natural em zona urbana: faixa mínima de **30 m** (Lei Federal 12.651/2012, art. 4º, II, "b" — **fonte primária lida**, planalto.gov.br, 28/09/2026). Em zona rural: 100 m, ou 50 m para corpo d'água de até 20 ha (art. 4º, II, "a"). O §10 do art. 4º (faixa definida por lei municipal em área urbana consolidada) vale só para curso d'água (inciso I), **não** para lagoa. No município, a LC 270/2024 remete à Lei 12.651 (Art. 214) e lista o entorno de lagoas como APP sem fixar largura (Art. 215, II); **dispensa a faixa** para acumulação natural ou artificial com superfície **inferior a 10.000 m²**, vedada nova supressão de vegetação nativa sem autorização do órgão ambiental do Sisnama (Art. 215, §2º — **fonte primária lida**, `LC270_2024_PlanoDiretorLUOS.pdf`, p. 80 do PDF). **Continuam a confirmar:** a faixa marginal estadual (FMP/INEA) e se existe norma municipal posterior com largura própria para APP urbana de lagoa |

---

## 5. PROTOCOLO HELY — CHECKLIST PARA PROJETOS NA BARRA/RECREIO

**Antes de montar a DULI (LICIN 2.0):**

- [ ] Gerar RIU pelo endereço completo do lote
- [ ] Identificar subzona ZPP (ex-ZE-5) e anotar GA/IAA/TO/afastamentos
- [ ] Verificar sobreposições: faixa de marinha, APA, APP, condomínio com regramento próprio
- [ ] OODC: comparar CAB e CAM da subzona. Na ZPP o CAM tende a ser o IAA (Art. 345 §5º, leitura do Hely), e se CAB = CAM não há outorga. Se houver CAM > CAB, ver a Skill `legal-oodc-mais-valera-mais-valia`. A isenção dos 5 anos (LC 270, Art. 110) **só vai ao cliente depois de checado o §8º** (R1)
- [ ] Programa do cliente x teto computável **lado a lado** (m² pedidos x ATE/TO/2xTO), com a diferença em m²
- [ ] Unifamiliar: ler o Dec. 3.046, Disp. Gerais VII **até a última frase** (remete ao XI) e aplicar o XI (§6, M3)
- [ ] Verificar LMS (Licença Municipal de Supressão) se houver árvores no lote — obrigatória para todo unifamiliar; em APP/área alagadiça pode tornar-se LMP+LMI (Decreto 51.503/2022 Art. 27 p.ú. II/IV)
- [ ] Se condomínio existente: ler Regramento Construtivo (Anexo do Estatuto) antes de propor implantação
- [ ] Confirmar com Lúcio/Oscar se o partido arquitetônico proposto cabe nos parâmetros levantados

---

## 6. MACETES DE QUEM FAZ

Só entra aqui o que tem artigo e fonte primária lida. Cada macete é ponto de partida para análise, não conclusão para cliente (Gate do Maurício).

**M1 — Lagoa pequena não gera faixa de APP.** Se o corpo d'água no lote ou vizinho tem superfície inferior a 10.000 m², a faixa de proteção do entorno fica dispensada. Fonte: LC 270/2024, Art. 215, §2º (c/c inciso II), `LC270_2024_PlanoDiretorLUOS.pdf`, p. 80 do PDF. Condições: (a) a área do espelho d'água sai de levantamento, não de estimativa; (b) o próprio §2º veda nova supressão de vegetação nativa sem autorização do órgão do Sisnama, então a LMS continua valendo; (c) a dispensa é da faixa municipal/federal, não resolve a FMP estadual (INEA), que segue a confirmar.

**M2 — Sem influência de maré, não há terreno de marinha na margem da lagoa.** A faixa de 33 m só alcança margens de rios e lagoas "até onde se faça sentir a influência das marés". Fonte: DL 9.760/1946, art. 2º, alínea "a", planalto.gov.br (página HTML, sem paginação; citar artigo e alínea). Condição: a influência de maré é fato a provar (demarcação da SPU), não a presumir. Na falta de prova, tratar a margem como sujeita à faixa.

**M1 e M2 nunca se presumem.** No Ensaio 003, a "lagoa de aproximadamente 1 ha" e o "relato de maré" derrubaram as duas premissas. Sem levantamento do espelho d'água e sem demarcação da SPU, o macete não se aplica.

**M3 — Casa unifamiliar: a varanda e o abrigo de carro podem ocupar o afastamento lateral do térreo (Dec. 3.046/81, Disp. Gerais XI).** O XI diz que, em residência unifamiliar com **afastamento frontal menor que 10,00 m**, os afastamentos **laterais do pavimento térreo** podem ser ocupados por **varandas ou abrigos de veículos**, desde que **abertos e cobertos por telha-vã**. Essas áreas **não entram** na ATE nem na TO. Fonte: `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`, p. 3, lido por Kelsen em 01/10/2026.
- **Por que é armadilha:** o inciso VII (varanda fora da ATE/TO, mas sem balanço sobre o afastamento frontal) termina na p. 3 com "Nos casos de edificações residenciais unifamiliares será aplicado o disposto no inciso XI". Quem para de ler no fim da p. 2 aplica à casa a regra de multifamiliar.
- **O XI é regra que permite, não que restringe.** No Ensaio 003, o Hely citou o XI como restrição à garagem coberta, e era o contrário.
- **Tensões em aberto (Gate do Maurício):**
  - a vedação de balanço sobre o recuo frontal do VII também alcança a casa unifamiliar, ou o XI substitui o VII por inteiro?
  - o XXIII (estacionamento coberto só em subsolo ou pavimento-garagem, p. 4) contra o XI, que é específico para unifamiliar. A leitura provável é que a regra especial (XI) prevaleça, mas isso **não está confirmado**.
- **Complemento:** o XIV permite saliência de até 0,40 m sobre o afastamento frontal, acima do térreo, para jardineira e ar-condicionado, fora da ATE e da TO.

**M4 — Decretos olímpicos prevalecem sobre a LC 270 onde alteraram o Dec. 3.046.** Fonte: LC 270/2024, Art. 111 §5º (p. 41), que cita os Decretos 24.241, 30.650, 32.886, 36.795 e 47.880. Num lote cuja subzona foi tocada por eles, o parâmetro vigente pode vir do decreto olímpico, e não do texto de 1981. Conferir no RIU.

---

## 7. COMO CHECAR A VIGÊNCIA DO DEC. 3.046/81 (bloqueio registrado em 01/10/2026)

A Busca Fácil da SMU **não devolve o Dec. 3.046 quando a busca é pelo número**. A busca pelo texto "3046" só traz os atos que o alteram (ex.: Decreto 9.392/1990). Até haver rota direta, use esta sequência:
1. **Vigência por remissão da LC 270/2024**, que é válida: Arts. 345, 354 §3º, 363 §1º III, 435 e 111 §5º. A LC 270 é posterior e remete ao Decreto, o que prova que ele vive.
2. **Alterações**: busca por texto "3046" na Busca Fácil, ato por ato, mais os decretos olímpicos do M4.
3. **Texto**: o PDF da base (Instruções Normativas) e o PDF da Câmara.
4. Na peça, escrever: "vigência inferida por remissão da LC 270, Arts. [...]; status direto não localizado na Busca Fácil em [data]". **Nunca escrever "Válido" sem a consulta.**

---

## RESSALVAS

**R1 (CRÍTICA, reescrita em 01/10/2026 por Kelsen) — a isenção de OODC por 5 anos EXISTE, no Art. 110 da LC 270/2024, e não no Art. 106.** Kelsen leu o PDF oficial da base, pp. 40-41.
- **Art. 106:** só a regra geral, CAB até CAM.
- **Art. 110 caput:** empreendimento licenciado nos 5 primeiros anos de vigência "não será autuado com a cobrança de Contrapartida Financeira".
- **Art. 110 §1º:** transição do 6º ao 9º ano.
- **Art. 110 §3º:** AP1 e AP3 isentas durante toda a vigência.
- **Art. 110 §8º:** o caput **não vale** onde já havia cobrança de instrumento oneroso na publicação da lei.

No Ensaio 003, o Hely leu só o Art. 106 e concluiu "sem isenção de 5 anos", e eu propus fechar a R1 nessa base. **As duas leituras estavam erradas**: o artigo vizinho decidia. **Ao cliente, só depois de verificado o §8º para o lote e a data de vigência da LC 270.** O detalhe está na Skill `legal-oodc-mais-valera-mais-valia`.

**R2 — Parâmetros por subzona:** os exemplos numéricos nesta Skill (IAA 0,60, TO 40%, afastamento 10 m) são de UMA subzona residencial genérica do Decreto 3046/81. Cada lote tem sua subzona própria — NUNCA usar esses números sem confirmar via RIU.

**R3 — LC 270/2024 em implementação:** o novo Plano Diretor (jan. 2024) está em fase de regulamentação progressiva. Algumas ZPP ainda usam Decreto 3046/81 como referência direta. Hely verifica qual instrumento está sendo aceito pelo balcão digital da SMU para consulta prévia.

**R4 — Decreto 3046/81 texto integral:** disponível em PDF na Câmara Municipal (mail.camara.rj.gov.br). Para projetos com dúvida de subzona, Hely deve consultar o texto original do Decreto (disponível via WebFetch ou download direto).

**R5 CRÍTICA — LMS ausente do checklist (Kelsen, 21/09):** adicionada ao checklist acima. POP-GESTOR-LEGAL-01 item 4.4 registra LMS obrigatória para todo unifamiliar — ativo desde 28/07/2026. A Barra/Recreio com APA e lotes próximos a lagoa é o cenário de maior risco para rito LMP+LMI. Omissão corrigida nesta versão.

**R6 — Nomenclatura ZPP vs ZRM1-B (Kelsen, 21/09):** o caso ativo Daniel-OB (Recreio) usa subzona "ZRM1-B" do Decreto 3046/81. A Skill refere "ZPP" como denominação da LC 270/2024, mas não confirma se as subzonas internas (ZRM1-B, A-17 etc.) foram renomeadas ou mantidas. Hely deve confirmar via RIU se o novo PD manteve a nomenclatura de subzonas do Decreto 3046/81 antes de usar a terminologia desta Skill como definitiva.

**R7 — Lacuna Art. 106 duplicada com Skill TDC/LICIN 2.0 (Kelsen, 21/09):** a mesma dúvida sobre isenção de OODC 5 anos já consta como lacuna pendente na Skill TDC/LICIN 2.0 (16/09). A resolução deve ser centralizada naquela Skill quando Hely confirmar o Art. 106 via fonte primária — não criar dois pontos de atualização independentes para a mesma lacuna. **[01/10/2026]** A lacuna foi resolvida no primário (LC 270, Art. 110), e o ponto único de verdade agora é a Skill **instalada** `legal-oodc-mais-valera-mais-valia`. A Skill TDC continua só em proposta e precisa ser alinhada a ela antes de ser instalada.

**R8 CRÍTICA — Checklist item OODC corrigido (Kelsen, 21/09):** o checklist original instruía "Consultar se o lote está em área de OODC disponível" sem alertar sobre o Art. 106 em aberto — contradição interna com a R1. Corrigido nesta versão para condicionar a consulta à confirmação do Art. 106. **[Superada em 01/10/2026]** O Art. 106 e os vizinhos já foram lidos (ver a R1 reescrita). O checklist agora condiciona o uso da isenção à checagem do **Art. 110 §8º**, e não mais ao Art. 106.

**R9 — Ratificada por Claudemberg (21/09/2026):** status promovido de `proposta-com-ressalvas` para `ativa-com-ressalva` por Claudemberg em sessão manual. Todas as ressalvas acima permanecem ativas — uso pelo Hely condicionado às ressalvas R1, R5 e R8 especialmente.

**R11 — Conferência de fonte primária (Hely, 29/09/2026, pedido de Kelsen aprovado por Claudemberg):** os itens (c) e (d) da R10 deixaram de estar "a confirmar": DL 9.760/1946 art. 2º e Lei 12.651/2012 art. 4º, II, "b" lidos no planalto.gov.br; LC 270/2024 Art. 215 §2º (dispensa para lagoa < 10.000 m²) lido no PDF oficial da base, p. 80. Continuam a confirmar: FMP estadual (INEA) e norma municipal posterior sobre APP urbana de lagoa. Registro: `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/confirmacoes_2026-09-28.md`, itens 2 e 3.

**R10 — Correções do treino de 28/09/2026 (Kelsen, aprovado por Claudemberg):** (a) fonte do RIU alinhada à oficial da casa, `mapas.rio.rj.gov.br` (antes apontava `geoinfo.rio/smdu`); (b) "ZPR – Zona de Proteção de Ruas" removida — nenhuma fonte encontrada para esse instrumento; se reaparecer, só volta com artigo da LC 270/2024 citado; (c) faixa de marinha reescrita — os 33 m são a própria faixa, não recuo além dela (**a confirmar** DL 9.760/1946 em fonte primária); (d) APP de lagoa — largura depende de zona urbana x rural (Lei 12.651/2012, art. 4º), **a confirmar** em fonte primária. Registro do treino: `01_CEO/Gestores/Kelsen (Legal)/Casos_TESTE/treino_skills/2026-09-28_decreto3046-81-lc270-2024.md`.

---

## FONTES VERIFICADAS

- Prefeitura RJ — "Novo Plano Diretor propõe manutenção de parâmetros na Barra da Tijuca" [prefeitura.rio] (secundária ✓)
- Câmara Municipal RJ — "Plano Diretor prevê potenciais construtivos mantidos na Barra e parte do Recreio" [camara.rio] (secundária ✓)
- Câmara Municipal RJ — Decreto 3046/81 PDF [mail.camara.rj.gov.br] (disponível; parâmetros específicos por subzona não lidos na íntegra nesta rodada)
- LC 270/2024 via legisweb.com.br — lida parcialmente (até ~Art. 80); **[superada em 01/10/2026]** Arts. 106-111 lidos no PDF oficial da base (`LC270_2024_PlanoDiretorLUOS.pdf`, pp. 40-41), por Kelsen
- Decreto 3.046/1981, Instruções Normativas, Disp. Gerais I-XXIII, no PDF da base (`Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`, pp. 2-4), por Kelsen em 01/10/2026
- **LICIN 2.0 (Decreto 55.622/2025)** — referenciado, não relido nesta rodada (Skill TDC/LICIN 2.0 de 16/09 cobre detalhes)
