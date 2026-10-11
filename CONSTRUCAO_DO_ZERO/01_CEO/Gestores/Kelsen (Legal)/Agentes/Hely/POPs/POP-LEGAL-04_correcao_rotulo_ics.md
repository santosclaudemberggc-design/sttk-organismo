---
pop: POP-LEGAL-04
titulo: Correção de rótulo — ICS é Índice de Comércio e Serviços, não "Compensação Social"
area: Legal — base legislativa por bairro/subzona (erratum/correção terminológica)
autor: Hely (Agente executor, equipe de Kelsen)
criado: 2026-07-20
origem: Conteúdo pesquisado e testado contra fonte oficial por Wallenberg em 16/07/2026; formalizado como POP/Skill oficial por Claudemberg na Reunião Semanal de 20/07/2026
status: oficial — aprovado por Claudemberg na Reunião Semanal de 20/07/2026
principios: 8 (Rastreabilidade), 9 (Padronização), 18 (Ética e conformidade)
---

# POP-LEGAL-04 — Correção de rótulo: ICS = Índice de Comércio e Serviços

## 1. Objetivo e por que existe
Corrigir formalmente um rótulo usado incorretamente em registros anteriores: **ICS não é "Índice de Compensação Social"**, e **não é contrapartida financeira nem pagamento**. É um **parâmetro de zoneamento** — o mesmo campo `ics` que a API oficial do RIU (ver `POP-LEGAL-RIU-01`) já devolve por coordenada. Este POP existe para que Hely (e qualquer leitura futura dos registros) não repita o erro nem confunda ICS com a Outorga Onerosa (`POP-LEGAL-02`).

## 2. Regra de ouro deste POP
**ICS = Índice de Comércio e Serviços.** É um limite de **área**, não um valor a pagar. Define quanto de comércio/serviço cabe no lote, calculado sobre a Área Total Edificável (ATE) — nunca tratar como sinônimo de contrapartida, compensação, ou isenção temporária.

## 3. Definição oficial (fonte primária, texto verbatim)
**Fonte**: Dicionário de Termos oficial da LC 270/2024 (2ª edição, 04/12/2025), SMDU — Art. 344, IX / Art. 367.

> **"ÍNDICE DE COMÉRCIO E SERVIÇOS - ICS: Parâmetro urbanístico representado pelo índice que define a área máxima de comércio e serviços permitida no terreno, mediante a multiplicação do seu valor pela Área Total Edificável (ATE)."**

Onde:
```
ATE = CA × área do terreno
```
(CA = Coeficiente de Aproveitamento aplicável; ATE já definida em `LC270_2024_PlanoDiretorLUOS.pdf`, Art. 346-347, arquivo local em `../Fontes_Legislacao/`.)

## 4. O que ICS NÃO é — distinções obrigatórias
- **Não é contrapartida nem pagamento.** O mecanismo de pagar por construir acima do CAB é a **Outorga Onerosa do Direito de Construir** (`POP-LEGAL-02`) — instrumento totalmente diferente. Ao orientar um caso, nunca apresentar ICS como se fosse "o valor a pagar por comércio" — ICS é limite de área, não é preço.
- **Não existe "fórmula de contrapartida do ICS"** nem **"isenção de 5 anos" ligada ao ICS**. Essa ideia era confusão com o **IPTU progressivo no tempo**: parcelamento/edificação/utilização compulsórios → IPTU progressivo por até 5 anos → desapropriação. Isso é uma **penalidade para imóvel ocioso**, sem qualquer relação com o ICS — não é uma isenção, e não é sobre comércio/serviço.

## 5. Relação com o `POP-LEGAL-RIU-01`
O campo `ics` já retornado pela API de zoneamento (`POP-LEGAL-RIU-01`, seção 5, Passo 3, entre os campos de `LBB_Zoneamento_urbano_vigente`) **é exatamente este parâmetro**. Os exemplos já registrados naquele POP (seção 9) — ICS 0,6 (Exemplo A, Estrada dos Bandeirantes), ICS 0,4 (Âncora do Claudemberg) — são valores corretos de ICS como coeficiente multiplicador da ATE, não valores monetários. Não é preciso reconsultar a API por causa desta correção — o dado já estava certo, **o rótulo/nome que às vezes foi usado ao redor dele é que estava errado**.

## 6. Nota de rastreabilidade (Princípio 8) — não apagar registros antigos
Registros anteriores a 20/07/2026 usaram o rótulo incorreto **"Índice de Compensação Social"** para se referir ao ICS. Especificamente identificado:
- **Registro Diário de 15/07/2026, caso Clínica Bem-Estar Recreio.**
- **`Fontes_Legislacao/_indice_fontes.md`**, entrada da LC 284/2025 (Operação Urbana Legado Olímpico): o texto atual descreve a contrapartida própria da OUC como **"adicional/distinta da ICS (0,3 do CAM) já registrada para o regime-base ZRM2 G"** — o valor numérico (0,3) está correto como ICS do lote, mas a glosa entre parênteses ("0,3 do CAM") sugere que o ICS é uma fração do CAM, o que **não é a definição oficial** (ICS multiplica a ATE, não o CAM diretamente — ver seção 3). Isso não é um erro do valor, é uma imprecisão na explicação ao lado do valor.

**Não apagar nenhum desses registros.** Este POP serve como a correção a ser lida junto — qualquer leitura de registro anterior a 20/07/2026 que mencione "Índice de Compensação Social" ou glose ICS como fração do CAM deve ser lida com a definição correta desta seção (Índice de Comércio e Serviços, multiplicador da ATE).

## 7. Confiança
**Alta** — definição extraída verbatim do Dicionário de Termos oficial da LC 270/2024 (fonte primária, SMDU), sem necessidade de interpretação.

## 8. Lacunas conhecidas (sinalizadas a Kelsen)
- Nenhuma lacuna de mérito identificada na definição em si (fonte oficial verbatim, seção 3).
- **Ação recomendada, não executada por Hely sozinho**: revisar a glosa "(0,3 do CAM)" na entrada da LC 284/2025 do `_indice_fontes.md` (ver seção 6) para deixá-la tecnicamente precisa ("0,3 × ATE do lote", não "do CAM") — sinalizado aqui para Kelsen decidir se e quando ajustar aquele arquivo, já que ele é histórico de pesquisa, não um POP formal (Princípio 8: preferível anotar a correção a reescrever silenciosamente um registro já existente).
