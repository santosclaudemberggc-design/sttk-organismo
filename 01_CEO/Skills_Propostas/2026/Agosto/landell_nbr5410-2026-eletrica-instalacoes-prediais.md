# NBR 5410 — Skill de Inteligência Técnica Elétrica

## Para qual Agente serve
**Landell** (Automação + Elétrica) — equipe de Cardozo (Gestor Complementares). Esta é uma Skill de **Trilha A (Inteligência)**: normas técnicas e técnicas de projetar instalações elétricas prediais, não ferramenta de software. Alimenta o saber-fazer de Landell em projetos de instalações elétricas de baixa tensão.

## Status
proposta — aguardando ratificação de Claudemberg

## O que esta Skill ensina

### Norma Vigente e Status da Revisão

| Norma | Situação | Observação |
|-------|----------|------------|
| **ABNT NBR 5410:2004** | ✅ **Vigente** | Única versão com força normativa. Usar para todos os projetos agora. |
| **NBR 5410 (revisão 2026)** | ⏳ Em segunda consulta pública | Publicação prevista fim de 2026 — ainda **NÃO tem força normativa**. Monitorar. |
| **ABNT NBR 5419** | ✅ Vigente | Proteção contra descargas atmosféricas (SPDA) — vinculada ao projeto elétrico |

**Atenção de Landell:** a "NBR 5410 2026" ainda não foi publicada. Todo projeto protocolado hoje segue a versão 2004. A revisão entrará em vigor após publicação oficial — verificar em ABNT antes de qualquer mudança de referência normativa.

---

### 1. Parâmetros Fundamentais (NBR 5410:2004 Vigente)

#### Divisão de Circuitos Obrigatória
- **Iluminação:** circuito exclusivo por cômodo/área
- **Tomadas de uso geral (TUG):** circuitos separados da iluminação
- **Tomadas de uso específico (TUE):** circuito exclusivo por equipamento (chuveiro, ar-condicionado, forno, etc.)
- **Potência máxima por circuito monofásico:** 1.500 W (tomadas gerais) / sem limite fixo em TUE (definido pelo equipamento)

#### Capacidade de Condutores
- Dimensionar por **método de referência** (forma de instalação) e **corrente de projeto**
- Fatores de correção: temperatura ambiente, agrupamento de cabos, tipo de isolação (PVC / EPR / XLPE)
- Cabos não halogenados (LSHF): recomendados em áreas de escape e ambientes críticos — a revisão 2026 os incorporará formalmente, mas já é boa prática atual

#### Aterramento e Proteção
- **Sistema TN-S:** recomendado em edificações novas (condutor neutro e PE separados)
- **DPS (Dispositivo de Proteção contra Surtos):** obrigatório em instalações com equipamentos sensíveis
- **DR (Diferencial Residual):** obrigatório para circuitos de banheiro, área de serviço e cozinha (30 mA)

---

### 2. O que Muda na Revisão 2026 (para monitorar)

A revisão ainda em consulta pública sinaliza 3 eixos de mudança:

#### 2a. Tabelas de Corrente Alinhadas à IEC 60364-5-52
- Revisão completa das tabelas de correntes admissíveis
- Métodos de referência internacionais: B1, B2, C, D, E, F, G
- Dimensionamento mais preciso por método de instalação + agrupamento + temperatura
- **Impacto prático:** seções de cabos calculadas poderão ser diferentes — rever projetos antigos quando a norma for publicada

#### 2b. Harmonização com NBR 5419 (SPDA)
- Integração formal de seções sobre proteção contra descargas atmosféricas
- Eliminação de contradições entre normas separadas
- Aterramento e equipotencialização unificados

#### 2c. Novas Tecnologias Incorporadas
- **Infraestrutura de recarga de VE (veículo elétrico):** circuitos, capacidade, tomadas tipo 2
- **Instalações de geração distribuída (solar):** interface com inversor e ponto de conexão
- **Iluminação pública e equipamentos urbanos** integrados ao escopo

---

### 3. Automação Residencial — Landell como Landell+Automação

Landell cobre elétrica E automação. Pontos técnicos básicos de automação predial que devem aparecer no briefing antes de Landell projetar:

| Aspecto | O que definir antes de projetar |
|---------|--------------------------------|
| **Protocolo** | KNX (mais robusto, padrão europeu), Zigbee/Z-Wave (sem fio, residencial), Modbus (industrial) |
| **Topologia** | Barramento centralizado vs. mesh distribuído |
| **Integração com elétrica** | Atuadores de automação precisam de circuito dedicado; planejamento conjunto |
| **Compatibilidade com BMS** | Em projetos maiores, verificar com Cardozo se o cliente exige BMS integrado |

---

### 4. Checklist Prático para Landell (início de todo projeto)

**Ao receber Briefing de Cardozo:**
- [ ] Identificar: tipo de edificação (residencial/comercial) e carga total estimada (kVA)
- [ ] Solicitar: planta com pontos de tomada/iluminação por ambiente + lista de equipamentos fixos (TUE)
- [ ] Verificar: sistema de fornecimento da concessionária (monofásico / bifásico / trifásico)
- [ ] Definir: sistema de aterramento (TN-S para obras novas)
- [ ] Calcular: corrente de projeto por circuito, fator de demanda, dimensionar condutores (NBR 5410:2004)
- [ ] Especificar: disjuntores (curva B/C), DRs 30 mA nos circuitos úmidos, DPS em painel
- [ ] Verificar: há previsão de VE, solar ou automação? → reservar circuitos/dutos agora
- [ ] Verificar: compatibilizar shafts elétricos com Saturnino (água/esgoto) — separação mínima 30 cm (NBR 5410 + NBR 5419)
- [ ] Verificar: acesso a ABNT NBR 5410:2004 atualização caso nova versão seja publicada antes do protocolo

**Erros comuns que Landell deve evitar:**
1. Não separar TUG de TUE (provoca sobrecarga e disparo de disjuntores)
2. Não instalar DR em circuitos de banheiro/cozinha (violação de norma + risco de choque)
3. Dimensionar cabo sem fator de agrupamento (superaquecimento em eletroduto cheio)
4. Não prever DPS em painel geral (surtos destroem equipamentos eletrônicos)
5. Compartilhar shaft elétrico com tubulação de esgoto sem separação física

---

### 5. Coordenação com Outros Agentes de Cardozo

- **Saturnino (Hidrossanitário):** shafts separados + 30 cm de distância mínima entre tubulações
- **Baumgart (Estrutural):** passagens de eletrodutos em laje/viga devem ser previstas no memorial estrutural antes da concretagem
- **Glaziou (Paisagismo):** iluminação externa/jardim precisa de circuito TUE separado com proteção IP65+
- **Tenreiro (Interiores):** posição de tomadas, interruptores e pontos de luz deve ser validada pelo projeto de interiores antes de finalizar prumadas

---

## O que esta Skill NÃO cobre
- Projetos de média tensão (ANEEL + concessionária local — escopo separado)
- Telecomunicações e cabeamento estruturado (NBR 14565)
- Projetos de CFTV e segurança eletrônica (normas específicas de segurança)
- Projetos de SPDA detalhado (NBR 5419 — pode ser Skill separada)

## Limitações honestas
- A revisão da NBR 5410 ainda está em segunda consulta pública (junho/2026) — as mudanças listadas são previstas, não confirmadas. Qualquer projeto protocolado agora segue obrigatoriamente a versão 2004.
- Tabelas de correntes admissíveis da norma 2004 não foram reproduzidas nesta Skill — Landell deve consultar a norma diretamente para dimensionamento de cabos.
- Valores de potência por tomada (100 W/TUG) e metodologia completa de cálculo de carga: ver NBR 5410:2004, capítulos 3 e 4.

## Fontes
- GreenGold Engenharia — "Revisão da NBR 5410 entra em segunda consulta nacional em 2026" (greengoldengenharia.com.br — WebFetch 28/08/2026)
- GreenGold Engenharia — "Revisão NBR 5410 2026: projeto elétrico de baixa tensão" (greengoldengenharia.com.br — WebFetch 28/08/2026)
- eletricapredial.com — "NBR 5410 Atualizada 2026: Versão em Vigor e o Que Exige" (WebSearch 28/08/2026)
- Data de verificação: 28/08/2026
