---
name: reservatorio-retardo-decreto23940-aguas-pluviais-rj
description: Reservatório de retardo (e de reuso) de águas pluviais obrigatório no Rio de Janeiro — Decreto 23.940/2004 + Resolução Conjunta SMG/SMO/SMU 001/2005 — quando é exigido, fórmula de volume (V = 0,15 × Ai × h; AP4 Barra/Recreio h = 0,06 m), orifício de descarga, regras de projeto, condição de Habite-se e o limiar baixo da Lei Estadual 9.164/2020 para unifamiliar. Use sempre que Saturnino (ou Glaziou/Baumgart) for projetar drenagem de lote, reservatório pluvial, cisterna, ou conferir o que trava o Habite-se — mesmo que o pedido só mencione "caixa de retenção", "cisterna", "drenagem do lote" ou "alagamento", sem citar o decreto pelo nome.
version: v1.1
status: ativa-com-ressalva
data: 2026-09-28
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_principal: Saturnino (Hidrossanitário)
agentes_cross: Glaziou (área permeável, jardim de chuva), Baumgart (reservatório enterrado em solo mole / lençol alto), Oscar (implantação no lote), Hely via Kelsen (Termo de Responsabilidade no licenciamento)
validacao: Cardozo 28/09/2026 — PROCEDE COM RESSALVA (C1-C4 aplicadas na v1.1; R1-R7 registradas abaixo)
---

# Skill: Reservatório de Retardo de Águas Pluviais no Rio de Janeiro (Decreto 23.940/2004 + Resolução Conjunta SMG/SMO/SMU 001/2005)

> ⚠️ RESSALVA DE FONTE — (1) Os decretos que alteraram o 23.940 (Decreto 26.168/2006, isenção para habitação de baixa renda, e Decreto 32.119/2010, que "altera casos de isenção") foram identificados só pela lista da Fundação Rio-Águas; o texto deles **não foi lido**. (2) A Lei Estadual 9.164/2020 (unifamiliar com cobertura > 100 m²) foi lida apenas em matéria jornalística (Omnia, 05/01/2021), não no texto publicado pela ALERJ. (3) **Vigência do rito:** falta confirmar que o Decreto 23.940 e o rito da Res. Conj. (licenciamento "junto à SMU") continuam valendo sem mudança depois do COES (LC 198/2019), da LC 270/2024 e do LICIN 2.0. Checagem de Kelsen/Hely. Ao aplicar em caso real, o Agente sinaliza essas três lacunas e trata o enquadramento como provisório.

## 1. POR QUE ESSA SKILL EXISTE

Barra da Tijuca, Recreio e Jacarepaguá são baixada com lençol raso, lagoas e canais — e alagam. A Prefeitura cobra do lote uma parte da solução: **reter a chuva que o lote impermeabilizou e soltar devagar**. O reservatório de retardo **condiciona o Habite-se** (Decreto 23.940, Art. 2º §4º). Esquecer no projeto significa descobrir o problema na vistoria final, com a obra pronta e sem lugar para enterrar uma caixa.

As Skills que Saturnino já tem (`nbr10844-1989-aguas-pluviais` para calha/condutor e `nbr16783-reuso-agua` para reuso) **não cobrem esta obrigação municipal**. Esta Skill fecha essa lacuna.

## 2. QUANDO É OBRIGATÓRIO (texto primário)

| Situação | Regra | Fonte |
|---|---|---|
| Empreendimento com **área impermeabilizada > 500 m²** | Reservatório de retardo obrigatório | Decreto 23.940/2004, Art. 1º ("empreendimentos"). A Res. Conj. 001/2005, Art. 1º, diz "empreendimentos **novos**" e "igual ou superior" |
| Multifamiliar, industrial, comercial ou misto novo com **telhado > 500 m²**, ou multifamiliar com **≥ 50 unidades** | Também um **reservatório de reuso** (fins não potáveis) + pelo menos 1 ponto de água de reuso | Decreto, Art. 3º ("superior"); Res. Conj., Art. 2º ("igual ou superior") |
| **Reforma/acréscimo** | Exigido quando a área acrescida (ou soma de acréscimos desde 2004) for ≥ 100 m² **e** a impermeabilizada total (existente + nova) passar de 500 m². O volume é calculado só sobre a **área impermeabilizada acrescida** | Decreto, Art. 6º |
| Estacionamento descoberto com fim comercial | 30% da área com piso drenante ou naturalmente permeável | Decreto, Art. 5º |

**Divergência de redação:** o decreto diz "superior a 500 m²" e a resolução diz "igual ou superior", tanto no retardo (Art. 1º) quanto no reuso (Art. 3º × Art. 2º). Em lote com exatamente 500 m², adote o texto mais exigente (resolução) e sinalize a dúvida.

**Casa unifamiliar STTK típica (lote de 360 a 600 m²):** quase sempre fica **abaixo** dos 500 m² impermeabilizados, então o decreto municipal não se aplica. **Mas confira a Lei Estadual 9.164/2020 (seção 6)**, que tem um limiar muito mais baixo para unifamiliar.

## 3. COMO DIMENSIONAR (fórmula oficial)

**Volume do reservatório de retardo** (Decreto, Art. 2º; Res. Conj., Art. 11):

```
V = k × Ai × h
V  = volume (m³)
k  = 0,15 (coeficiente de abatimento)
Ai = área impermeabilizada (m²): telhados, coberturas, terraços, pavimentos descobertos
h  = 0,06 m nas AP 1, 2 e 4 | 0,07 m nas AP 3 e 5
```

**Barra da Tijuca, Recreio e Jacarepaguá ficam na AP4 → h = 0,06 m.** Isso vem de conhecimento geral, não do texto do decreto: **confirme a AP do lote no RIU**, não pelo nome do bairro. (Guaratiba, Campo Grande e Santa Cruz ficam na AP5 → 0,07 m.)

Exemplos AP4:
- 600 m² impermeabilizados → V = 0,15 × 600 × 0,06 = **5,4 m³**
- 1.000 m² → **9,0 m³**

**Reservatório de reuso** (quando exigido): a mesma fórmula, com **Ai = área do telhado** apenas (Res. Conj., Art. 2º §1º).

**Orifício de descarga** (Res. Conj., Art. 14):

```
S = Q / (Cd × √(2gh))
S  = área do orifício (m²)
Q  = vazão do lote ANTES da impermeabilização, "conforme as normas de Drenagem urbana da Secretaria Municipal de Obras"
Cd = 0,61
h  = carga sobre o centro do orifício (m)
Velocidade no orifício: mínimo 1,0 m/s, máximo 4,0 m/s (§1º)
Cota de fundo do orifício: acima da rede existente e compatível com ela (§2º)
```

Para o Q pré-impermeabilização, **inferência não lida**: a norma de drenagem aplicável hoje deve ser a da Rio-Águas (Portaria O/SUB-Rio-Águas 004/2010, com curva IDF). É a mesma lacuna já registrada na Skill NBR 10844: Saturnino consulta a IDF do bairro antes de fechar número.

## 4. REGRAS DE PROJETO (Res. Conj. 001/2005)

**Reservatório de retardo (Art. 12):**
- resistente a esforços mecânicos, com acesso para manutenção e esgotamento total;
- **extravasor por gravidade** para a rede pública, com a seção acima do nível máximo útil do cálculo (inciso IV);
- **orifício de descarga** que solta o volume aos poucos (inciso V; cota de fundo pelo Art. 14 §2º).

**Destino da água retida (Decreto, Art. 2º §3º):** infiltrar no solo (regra geral), **ou** lançar na rede pública após 1 hora de chuva (por gravidade ou bomba), **ou** mandar para o reservatório de reuso.

**Reservatório de reuso (Res. Conj., Arts. 3º a 9º):**
- capta **só água de telhado**, com grelha que retém folhas e detritos;
- revestido, liso, impermeável, tampado, com acesso para limpeza;
- extravasor que joga o excesso no reservatório de retardo, com dispositivo **antirretorno** (Art. 4º VII-VIII);
- limpeza e desinfecção **a cada 6 meses** (desinfetante ≥ 50 mg/L, contato ≥ 12 h);
- uso restrito: lavagem de carro, piso e rega de jardim (Art. 6º);
- ponto de água a **1,80 m do piso**, em nicho com portinhola e fecho, com a placa "ÁGUA IMPRÓPRIA PARA CONSUMO HUMANO" (Art. 9º);
- **nenhuma ligação** com a rede potável (Decreto, Art. 4º III; Res. Conj., Art. 8º).

**Nota cruzada com `nbr16783-reuso-agua`:** a NBR 16783 admite água não potável para descarga sanitária. Mas, quando o reuso vier da **obrigação municipal** (Art. 3º do decreto), o texto municipal lido (Res. Conj., Art. 6º) só autoriza lavagem de carro, piso e rega. Descarga sanitária com essa água não está coberta pelo texto municipal: confirmar com Vigilância Sanitária/Kelsen antes de projetar.

Água de piso descoberto (estacionamento, pátio) vai **direto para o retardo**, nunca para o reuso (Res. Conj., Art. 10).

## 5. O QUE O PROFISSIONAL EXPERIENTE FAZ NA BARRA/RECREIO (brecha válida)

1. **Reduzir Ai em vez de aumentar o reservatório.** Prática de projeto, **interpretação a confirmar**: nenhum dos dois textos define "área impermeabilizada". O decreto só trata piso drenante como permeável para estacionamento comercial (Art. 5º). A leitura de que piso drenante, jardim sobre solo natural e jardim de chuva ficam fora de Ai é razoável, mas precisa ser confirmada com SMDU/Rio-Águas via Kelsen antes de usar para ficar abaixo do limiar. Integra com a Skill `paisagismo-jardim-de-chuva` (Glaziou).
2. **Infiltrar é a regra, mas o lençol da Barra costuma impedir.** O decreto (Art. 2º §1º) já prevê reservatório "com ou sem revestimento, dependendo da altura do lençol freático". Com lençol a 1 ou 2 m (ver Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio`), infiltração é inviável. Reservatório enterrado precisa de **verificação de empuxo (flutuação) com Baumgart**. Em lençol muito raso, considere reservatório elevado ou semienterrado.
3. **Retardo e reuso num único corpo** (prática de projeto, não texto normativo): câmaras **lado a lado**, ou o retardo na **cota mais alta compatível com a rede**. O reuso extravasa para o retardo com antirretorno (Art. 4º VII-VIII). **Nunca pôr o retardo embaixo do reuso**: o extravasor do retardo precisa chegar à rede por gravidade (Art. 12 IV) e o orifício tem que ficar acima da rede (Art. 14 §2º). Com lençol e rede rasos na Barra, retardo fundo não descarrega. Confirmar as cotas com Baumgart (empuxo) e com o levantamento da rede.
4. **Reforma: calcule só a área impermeabilizada acrescida** (Art. 6º). O cliente não precisa de reservatório para a casa inteira.
5. **Documento que trava o Habite-se:** o Termo de Responsabilidade (Anexo 1 da Res. Conj., Art. 16) é assinado pelo **proprietário e pelo RT do projeto/execução**. A declaração do Art. 7º do decreto é assinada pelo **RT de execução da obra e pelo proprietário**. Kelsen/Hely incluem os dois no checklist do LICIN. **Nenhum Agente assina:** é documento de cliente e só sai pela cadeia Kelsen → Wallenberg → Claudemberg.

## 6. LEI ESTADUAL 9.164/2020: LIMIAR BAIXO PARA UNIFAMILIAR (fonte secundária, ver ressalva)

Segundo matéria de 05/01/2021 (Omnia), a Lei Estadual 9.164/2020 (dep. Samuel Malafaia e Luiz Paulo, publicada em 29/12/2020) exige:
- **unifamiliar** (até 2 unidades): reservatório de águas pluviais se o **telhado/cobertura passar de 100 m²**, **dispensado se o lote tiver ≥ 25% de superfície permeável**. Vale também para acréscimos de ≥ 100 m²;
- multifamiliar, shoppings, hospitais e prédios públicos: reservatório se as áreas impermeáveis passarem de 360 m², mais reservatório de águas cinzas.

**Consequência prática:** a casa STTK típica pode escapar do decreto municipal e **cair na lei estadual**. A brecha é a mesma: **manter ≥ 25% do lote permeável dispensa o reservatório**. Inferência sem fonte: isso tende a casar com a taxa de permeabilidade que o zoneamento já pede (confirmar no RIU).

**Antes de usar:** Kelsen/Hely confirmam no texto da ALERJ (1) o número e o conteúdo, (2) se a lei está vigente e não foi questionada no STF/TJ, e (3) como a SMDU a cobra no LICIN.

## 7. CHECKLIST DE SATURNINO (por projeto)

- [ ] AP do lote confirmada no RIU (h = 0,06 ou 0,07)
- [ ] Ai medida em planta: telhados, coberturas, terraços e pavimentos descobertos
- [ ] Enquadramento: decreto municipal (> 500 m²)? Lei estadual (telhado > 100 m² e < 25% permeável; **fonte secundária: Omnia; confirmar texto ALERJ via Kelsen/Hely**)? Reforma pelo Art. 6º?
- [ ] V calculado; reuso calculado se couber pelo Art. 3º
- [ ] Orifício dimensionado com a vazão pré-impermeabilização (norma de drenagem SMO/Rio-Águas)
- [ ] Lençol freático conferido com Baumgart (infiltração possível? empuxo?)
- [ ] Cotas do extravasor e do orifício conferidas contra a rede existente
- [ ] Localização e volume indicados em prancha (Art. 2º §4º)
- [ ] Termo de Responsabilidade (Anexo 1) e declaração do Art. 7º sinalizados para Kelsen/Hely

## 8. RESSALVAS DA VALIDAÇÃO (Cardozo, 28/09/2026)

- **R1:** conflito de uso com `nbr16783-reuso-agua` (descarga sanitária); ver nota cruzada na seção 4.
- **R2:** "novos" e "igual ou superior" vêm da Res. Conj., não do decreto; divergência registrada na seção 2.
- **R3:** a cota de fundo do orifício está no Art. 14 §2º (corrigido).
- **R4:** a ligação SMO → Rio-Águas/Portaria 004/2010 é inferência (marcada).
- **R5:** o que conta como "área impermeabilizada" não está definido nos textos (marcado na seção 5, item 1).
- **R6:** a relação com a taxa de permeabilidade do zoneamento é inferência (marcada na seção 6).
- **R7:** vigência do rito pós-COES/LC 270/LICIN 2.0 (no aviso do topo).

## 9. O QUE ESTA SKILL NÃO COBRE

- Curva IDF e cálculo do Q pré-impermeabilização (Portaria Rio-Águas 004/2010, não lida)
- Texto dos Decretos 26.168/2006 e 32.119/2010 (isenções)
- Detalhamento estrutural do reservatório (Baumgart: NBR 6118 e empuxo)
- Qualidade de água de reuso além da Res. Conj. (ver `nbr16783-reuso-agua`)

## 10. FONTES

- Decreto Municipal RJ 23.940, de 30/01/2004 (texto primário lido): http://www0.rio.rj.gov.br/smac/up_arq/DEC-23940-04-aguaspluv.pdf
- Resolução Conjunta SMG/SMO/SMU 001, de 27/01/2005 (texto primário lido): https://www.rio.rj.gov.br/documents/91265/148105/21_ResConjsmgsmosmu01-05-Dec23940.pdf
- Fundação Rio-Águas, lista de legislação municipal com emendas (lida): https://fundacaorioaguas.prefeitura.rio/legislacao-municipal-com-emendas-e-respectivos-links-de-acesso/
- Omnia, "Agora é lei no RJ: novas edificações deverão ter reservatório de águas pluviais" (05/01/2021, fonte secundária): https://www.omniaonline.com.br/agora-e-lei-no-rj-novas-edificacoes-deverao-ter-reservatorio-de-aguas-pluviais/
- Pesquisa: Rotina Diária Skills v3.2, 28/09/2026 (Wallenberg). Validação: Cardozo, 28/09/2026 (leu os dois PDFs primários na íntegra)
