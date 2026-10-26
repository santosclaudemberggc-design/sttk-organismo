# Parecer Kelsen — Pendências A e B, Ensaio Sombra 003, etapa 05 (21/10/2026)

Pedido de Wallenberg, autorizado por Claudemberg em 21/10/2026. A execução (leitura das fontes e tentativa no Vitruvius) foi do Hely. A conclusão é minha. Este texto é análise preliminar, não parecer final. Modelo, programa, gabarito lacrado e `_estado_ensaio_003.json` não foram alterados.

Fontes (pasta `Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/`): LC 270/2024 (PDF), Dec. 3.046/81 (PDF), COES LC 198/2019 consolidado SMU (PDF). A página citada é a do PDF. O status vigente na Busca Fácil não foi reconsultado hoje.

## Pendência A — gabarito e número de pavimentos

**Conclusão: (b) o 3º pavimento não é permitido. A diferença de área é decisão do cliente.**

Fundamentos:
- LC 270, Anexo XXI, p. 275, linha ZPP: o gabarito diz "ver Dec. nº 3046/1981". LC 270, Art. 433, p. 153: o Dec. 3.046 continua valendo na ZPP. LC 270, Art. 354 §3º, p. 127: ficam mantidas as condições de cômputo de pavimentos da ZPP.
- O limite de 2 pavimentos vem do RIU fictício do caso (`caso_sombra_003.md` §5.3), porque a subzona "A-ENS" não existe no Dec. 3.046. Ele vem também do Regramento do condomínio, Art. 7º: "2 pavimentos, altura máxima 8,50 m [...] Vedado pavimento de cobertura, terraço habitável". São duas travas independentes.
- **Subsolo:** não conta como pavimento (LC 270, Art. 354 II a, p. 127). Mas o subsolo não pode ter uso residencial (Art. 356, p. 128), o Regramento, Art. 8º, o veda e o nível d'água está a 0,90 m. Não resolve.
- **Cobertura:** é excluída da contagem só como telhado ou área técnica (Art. 354 II c, p. 127; COES, glossário "TELHADO", p. 29). O aproveitamento do Dec. 3.046 XXVIII (p. 5) esbarra no Regramento, Art. 7º.
- **Pavimento de uso comum:** pelo Dec. 3.046 XVII–XVIII (p. 3) e pelo COES, glossário (p. 28), é área comum. Não se aplica a casa unifamiliar.
- **Teto de área:**

| Item | Área (m²) |
|---|---|
| ATE: 1,0 × 571,60 | 571,60 |
| Projeção máxima (TO de 40% do condomínio) | 228,64 |
| Teto computável: 2 × 228,64 (2º pavimento só na projeção do inferior, Art. 354 §7º, p. 128) | 457,28 |
| Pedido do cliente | ~520 |
| Diferença computável | ~62,7 |

O que passar do teto computável só entra como área não computável: varandas e vagas, LC 270 Arts. 347 e 350 (pp. 124-125).

**Ressalva ao Gate de Claudemberg (não muda a conclusão b):** a LC 270, Art. 354 II b (p. 127), não conta jirau como pavimento "nas condições do COES". Só que o COES, Art. 16 (p. 8), só regula jirau em loja não residencial. Ficam em aberto três pontos: se o jirau se aplica a casa unifamiliar, se fura o teto de 2 × TO e se o condomínio aceita. Pela regra, é interpretação e vai ao Gate.

## Pendência B1 — vaga descoberta no afastamento lateral

**Conclusão: permitida pela legislação municipal, com a condição de plantar 1 árvore por vaga. O condomínio não trata do assunto, então confirmar com a Comissão de Obras (Regramento, Art. 9º).**

- **Dec. 3.046 XXII, p. 4:** "Será permitida a utilização da área livre do lote para estacionamento ou guarda de veículos [...] excetuada aquela do afastamento frontal mínimo obrigatório, desde que seja efetivado o plantio de, no mínimo 1 (uma) árvore por vaga." A exceção é só a faixa frontal.
- **Dec. 3.046 XI, p. 3:** em casa unifamiliar com afastamento frontal abaixo de 10 m, o afastamento lateral do térreo pode receber abrigo de veículos aberto e coberto por telha-vã. Isso reforça que a vaga descoberta cabe ali.
- **COES, Art. 4º II, p. 3:** fixa o afastamento lateral mínimo de 2,50 m e não veda estacionamento. **LC 270, Art. 363 §2º, p. 130:** restringe só a faixa frontal. **LC 270, Art. 364, p. 130:** remete o afastamento lateral ao COES.
- **Skill de vaga, R3:** a vedação vale só para o afastamento frontal na ZPP.
- **Atenção para Arquitetura (não é mérito legal):**
  - As vagas descobertas 454843 e 454851 exigem 2 árvores, e elas não estão no modelo.
  - O piso das vagas é "CALCADA". Isso afeta a permeabilidade mínima.
  - A faixa tem exatamente 2,50 m. Conferir o acesso e a manobra pelo COES, Art. 29 II (p. 15).

## Pendência B2 — largura interna das vagas cobertas

**Conclusão: não provado.**

Motivo: pelo `vitruvius_get_revit_status`, o Revit estava com outro modelo aberto, o `RDMOB-PBA-04.rvt` do caso Daniel-OB (com alterações não salvas), e não o `EP_v3.rvt`. O Hely não trocou de modelo e não leu paredes de outro projeto. Também não há exportação com eixo e espessura das paredes. Nada disso serve de prova:
- a cota 454895 do Oscar (5,015 m), porque mede eixo, que é defeito conhecido;
- o "~5,275" do `relatorio_oscar_v3.md`.

Como provar: abrir o `EP_v3.rvt`, rodar `list_elements` das paredes do térreo com localização e tipo/espessura e calcular a face interna = distância entre eixos − (e1/2 + e2/2). O resultado deve ser ≥ 2,50 m por vaga (≥ 5,00 m para duas lado a lado).

## Fica em aberto
- Jirau em casa unifamiliar: vai ao Gate de Claudemberg.
- Aceite do condomínio para vaga no afastamento lateral.
- Medição em B2.
- Vigência dos atos na Busca Fácil, não reconsultada hoje.

## Complemento 21/10 — jirau e reconferência

Ordem de Claudemberg (21/10/2026), via Wallenberg. Leitura do Hely por `pdftotext -layout` com página do PDF. Desta vez não houve conferência por imagem. Auditoria e conclusão são minhas. Continua sendo análise preliminar e depende do Gate de Claudemberg. Modelo, programa, gabarito e `_estado_ensaio_003.json` não foram alterados.

### 1. Jirau

**Conclusão: INTERPRETAÇÃO.** Pela letra da lei, o jirau não conta como pavimento e fica fora da ATE. Mas a única regra que fixa as condições exigidas pela lei é para loja não residencial. Por isso não posso afirmar que ele resolve os ~520 m² em casa unifamiliar. Vai ao Gate.

Textos:
- **LC 270, Art. 354 II b, p.127:** "o número máximo de pavimentos compreende todos os pavimentos [...] exceto: [...] b) Os jiraus de qualquer unidade em qualquer nível, desde que atendida a altura máxima da edificação e as demais condições estabelecidas no [...] COES".
- **LC 270, Art. 347 IX, p.124 (não estava no parecer):** fica fora da ATE "IX - os jiraus de qualquer unidade em qualquer nível, desde que atendida a altura máxima da edificação e as demais condições estabelecidas no [COES]". O §1º diz que essas partes "não serão computadas na ATE".
- **COES, Art. 16, pp.8-9:** "Serão permitidos jiraus em lojas, localizadas no térreo ou nos subsolos de edificações não residenciais ou mistas, que não serão considerados como um pavimento". Limites: I até 50% da área útil; II até 3,00 m em cima; III no mínimo 2,20 m embaixo; IV fora da ATE. O §1º estende a regra só a lojas de edificação não residencial ou mista. O artigo não fala de residência.
- **COES, glossário:**
  - JIRAU, p.27: "piso elevado no interior de um compartimento, ocupando parcialmente a área do mesmo e atendendo às alturas e dimensões estabelecidas pela legislação".
  - PAVIMENTO, p.28: "situadas entre o plano de um piso e o teto imediatamente superior, admitindo-se um desnível máximo de 1,50m".
  - O COES não tem verbete MEZANINO. O Dicionário de Termos da LC 270 não tem verbete de jirau nem de pavimento.
- **Dec. 3.046:** não tem nenhuma ocorrência de "jirau" ou "mezanino" nas 87 páginas. O Art. 354 §3º (p.127) mantém o cômputo de pavimentos da ZPP, mas esse cômputo não trata de jirau.
- **Regramento, Art. 7º** (`caso_sombra_003.md` §5.4): "Gabarito: 2 pavimentos, altura máxima 8,50 m [...] Vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje de cobertura". O Regramento **não veda o jirau** e não fala dele. O limite de área vem do Art. 5º (TO de 40%).

Respostas:
- **Conta como pavimento?** Não, pela letra do Art. 354 II b ("de qualquer unidade"). Isso fica condicionado às "condições do COES".
- **Entra na ATE ou na área computável?** Não, pelo Art. 347 IX, com a mesma condição. Por isso ele **não esbarra** no teto computável, ao contrário do que eu supunha na ressalva acima.
- **Ajuda a chegar a ~520 m²?** Só se a dúvida do Gate for resolvida a favor. Faltam ~62,7 m² sobre o teto computável de 457,28 m². Também é preciso caber em 8,50 m com 2 pavimentos, o que é apertado.

**Dúvida exata para o Gate de Claudemberg:**
1. A LC 270 admite jirau "de qualquer unidade" nas "condições do COES". O COES só dá condições para loja não residencial ou mista. Em casa unifamiliar, o jirau:
   - (i) é admitido, aplicando por analogia os limites do Art. 16 (50% da área útil do compartimento, até 3,00 m em cima e 2,20 m embaixo); ou
   - (ii) não é admitido, porque a remissão ao COES não tem objeto para residência?
2. A Comissão de Obras do condomínio (Regramento, Art. 9º) conta o jirau como "pavimento" no Art. 7º?

### 2. Reconferência das citações do parecer

| Citação | Resultado |
|---|---|
| Anexo XXI, p.275, ZPP "ver Dec. 3046" | conferido (por imagem em 14/10; hoje só por texto) |
| Art. 433, p.153 | **corrigido:** pp.152-153 |
| Art. 354 §3º, p.127 | conferido |
| Art. 354 II a, p.127 (subsolo) | conferido |
| Art. 356, p.128 (subsolo sem uso residencial) | conferido |
| Art. 354 II c, p.127 | conferido |
| COES, glossário TELHADO, p.29 | conferido |
| Dec. 3.046 XXVIII, p.5 | conferido |
| Dec. 3.046 XVII-XVIII, p.3 | conferido |
| COES, glossário PUC, p.28 | conferido |
| Art. 354 §7º, p.128 | **corrigido o uso.** O texto "será permitida a ocupação do segundo pavimento na projeção do pavimento inferior" é permissão, não restrição. O teto de 2 × projeção vem da TO de 40% (Regramento, Art. 5º) somada aos 2 pavimentos |
| Arts. 347 e 350, pp.124-125 | **corrigido:** Art. 347 nas pp.123-124 (ATE: vagas no II, varandas no VI); Art. 350 nas pp.124-125 (exclusão da **projeção/TO**, não da ATE) |
| Art. 354 II b, p.127 | conferido; falta o Art. 347 IX, p.124 (acrescentado acima) |
| COES, Art. 16, p.8 | **corrigido:** pp.8-9 |
| Dec. 3.046 XXII, p.4 (trecho entre aspas) | conferido |
| Dec. 3.046 XI, p.3 | conferido (unifamiliar com afastamento frontal < 10,00 m) |
| COES, Art. 4º II, p.3 | conferido |
| LC 270, Art. 363 §2º, p.130 | conferido. Nota: o XII permite vaga no afastamento frontal de unifamiliar na regra geral, mas na ZPP prevalece o Dec. 3.046 XXII |
| LC 270, Art. 364, p.130 | conferido |
| COES, Art. 29 II, p.15 | **corrigido:** o II é a área de manobra; o acesso de 2,50 m é o **IV**. Citar o II e o IV |
| Regramento, Arts. 7º, 8º e 9º | conferidos (§5.4) |
| `caso_sombra_003.md` §5.3 | conferido: 2 pavimentos, "A-ENS"; o RIU dá TO de 50% e prevalece a de 40% do Regramento, Art. 5º |
| **Área do lote: 571,60** | conferido: 571,60 m² (base do Gate de 20/10, a menor entre medida e informada 571,80) |

**Quadro:** ATE de 571,60; projeção de 0,40 × 571,60 = **228,64**; teto computável de 2 × 228,64 = **457,28**; diferença para ~520 ≈ **62,7 m²**. A conclusão (b) da Pendência A não muda.

### 3. Vigência

**Não consegui consultar a vigência.** Tentativas do Hely em 21/10:
- `rio.rj.gov.br/web/buscafacil`: abriu, mas não tem busca por número. O link de consulta (`smaonline.rio.rj.gov.br/conlegis/ConLegislacao.asp`) deu **HTTP 404**.
- leismunicipais: **HTTP 403**.
- `doweb.rio.rj.gov.br` e Câmara: **sem DNS** no ambiente (erro 6).

O status vigente de LC 270/2024, LC 198/2019 e Dec. 3.046/1981 continua sem conferência. É preciso consulta manual ou outra rede. Nos próprios PDFs, a LC 270 traz redações da LC 274/2024.
