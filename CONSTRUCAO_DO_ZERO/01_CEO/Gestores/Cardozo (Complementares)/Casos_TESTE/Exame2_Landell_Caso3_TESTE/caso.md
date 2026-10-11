# Exame 2 — Caso 3 (complementar retroativo) — Landell (Automação+Elétrica)

**Tipo deste caso:** Automação residencial integrada (protocolos, redundância, circuito dedicado, integração com elétrica). **Diferente dos 2 casos já aplicados** (Caso 1 = circuitos elétricos básicos residenciais; Caso 2 = SPDA + COSCIP/segurança contra incêndio). Este caso testa a outra metade do escopo de Landell: automação em si, não só elétrica pura.

**Contexto:** Cobertura duplex, Leblon/RJ. Cliente pediu automação completa: iluminação, persianas motorizadas (inclusive na varanda externa), climatização, som ambiente e controle de acesso (fechadura eletrônica na porta principal). Tenreiro já definiu que a iluminação geral usará luminárias de LED com driver dimerizável. Landell recebe a proposta técnica preliminar de um integrador terceirizado para revisão.

## Proposta técnica preliminar recebida (revisar item a item)

1. **Alimentação da central de automação:** "A central de automação (hub) será conectada em uma tomada comum do circuito de TUG da sala de estar, junto com os demais equipamentos eletrônicos do ambiente — não há necessidade de circuito exclusivo, é um equipamento de baixo consumo."

2. **Protocolo de comunicação:** "Optamos por integrar todos os dispositivos (incluindo fechadura eletrônica e sensores de alarme) via Wi-Fi doméstico comum do cliente, dispensando rede dedicada — é a solução mais moderna, sem necessidade de cabeamento ou malha própria."

3. **Dimmer de iluminação:** "Serão instalados dimmers convencionais de resistência (os mesmos já usados em outros projetos da Sttickler) em todos os pontos de luz, incluindo os pontos com luminária LED especificada por Tenreiro."

4. **Automação de persiana externa (varanda):** "O atuador motorizado da persiana da varanda será o modelo padrão indoor já usado nos ambientes internos, IP20, para manter padronização de fornecedor."

5. **DR no circuito da central de automação:** "Por ser um equipamento eletrônico sensível a variações, o circuito dedicado à central de automação (quando houver) deve dispensar o DR de 30mA, para evitar desarmes falsos que interrompam o sistema de segurança da casa."

6. **Nobreak da fechadura eletrônica:** "A fechadura eletrônica da porta principal terá um nobreak (UPS) dedicado, garantindo abertura mesmo em queda de energia da concessionária."

7. **Controle de acesso remoto:** "Configuraremos o sistema com o protocolo já definido no item 2."

**Instrução para Landell:** Revise os 7 itens, um a um. Para cada item, classifique como **CONFORME** ou **NÃO CONFORME**, citando a fonte (NBR 5410, boas práticas de protocolo KNX/Zigbee/Z-Wave/Modbus, ou a Skill de tendências de automação, conforme o caso). Se algum dado necessário para julgar um item não foi informado, não presuma — trate como **pendência bloqueante** e diga exatamente qual dado falta e a quem cobrar. Grave seu memorial de verificação no caminho padrão que você já usa (`Agentes/Landell/Casos/...`).
