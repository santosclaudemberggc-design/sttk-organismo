# Erros registrados — Etapa 04 (Briefing), Ensaio Sombra 003

**Registro:** 13/10/2026, a pedido de Claudemberg. Objetivo: melhorar Skills e agentes com base no que errou.
**Versões:** v1 (reprovada 09/10), v2 (entrega antiga, não avaliada), v3 (reprovada 13/10, Oscar 4,25 / Lúcio 6,50), v4 (reprovada 13/10, Oscar 4,75 / Lúcio 6,50). Etapa aprovada com pendências por Claudemberg em 13/10/2026.

## 1. Erros do executor (Oscar — Agente)
1. SMD omitida nas peças (v3 e v4). Regra de cálculo: LC 270 Art. 352 (20% da área livre pela TO da zona).
2. Organograma e esquemas só em tabela/ASCII; a Skill nbr6492 (l. 33) pede gráfico.
3. Soma dos 520 m² não aparece no quadro.
4. Habite-se de 1999 presente na v3 e perdido na v4 (isca 2).
5. Legal-oodc não lida na execução (isca 3: janela 01/12/2026, AP4 fora do Art. 19 II, contrapartida à vista).
6. Declaração de leitura contraditória e Glob amplo em `**/Fontes_Legislacao/*.pdf` (R1).
7. Área "não computável" (62,56 m²) tratada sem artigo.
8. Regime do H1 ausente na linha E-13 (v3) e no §1 (v3/v4).
9. P-04 com premissa de locação B sem fonte.
10. Página do Dec. 3.046 citada errada (VII na p. 2, correto p. 3).
11. COES Art. 31 IV e LC 270 Art. 350 II não considerados (agora conflito para Kelsen).
12. Dispensa "abaixo de 10.000 m²" atribuída à Etapa 03 sem fonte (v3, corrigida na v4 como "não lido").

## 2. Erros do Gestor (Lúcio — auditoria)
1. Auditoria "aprovado com ressalvas" sem cruzar o Resumo do enunciado (SMD ficou de fora).
2. "OK" para acesso do Oscar com prova só declarada pelo executor.
3. "Atende" no regime do H1 sem conferir E-13.
4. Afirmações de verificação sem prova colada (R2 e herança).
5. Referência "04 M-14" inexistente na entrega.

## 3. Erros da Skill
1. **legal-base-legislativa-bairro**: citava SMD (Arts. 351–353) sem a regra do Art. 352. Corrigida pelo Kelsen (bloco SMD, exemplo, aviso de TO da zona).
2. **nbr6492**: l. 33 diz que organograma é gráfico; o Oscar não seguiu. Revisar a cobertura da Skill.
3. **arquitetura-nbr9050-acessibilidade** v1.1: linha 15 dizia "exigido para habite-se", contra COES Art. 31 V (p. 17). Corrigida na v1.2, mas linhas 20 e 90 ainda citam exigência para habite-se (pendência para o Lúcio).
4. **vaga-estacionamento** v1.6: sem erro de conteúdo; rótulos v1.0/v1.1/v1.3 aparecem em outros documentos.
5. **decreto3046-81** (R2): cita "vaga v1.0". Pendente para a próxima edição.
6. **legal-oodc** v1.1: cobre LC 301 Art. 58; Anexo XXV (Fórmula 1) continua lacuna.

## 4. Erros do Examinador (Bardi) — gabarito e enunciado
1. GB-1: seção 3 dava por aberta a lacuna da legal-oodc já fechada. Corrigido.
2. GB-2: frente 14,29 vs 14,30 sem explicação. Corrigido (14,30 frente; 14,29 fundos, menor largura).
3. GB-3: TO 50% vs 40% sem decisão. Marcado como decisão pendente de Claudemberg.
4. GB-4: "construída máxima 297,28" (enunciado linha 45) — rótulo errado; o número é computável. Não corrigido no enunciado.
5. Enunciado pede metragem por ambiente que o caso não traz (não descontado).
6. Cabeçalho do gabarito ainda diz "SHA256 PENDENTE" (hash correto no JSON).

## 5. Erros de processo
1. Agentes sem shell não fazem backup byte a byte nem calculam hash. Wallenberg calculou os hashes.
2. Prompt do Lúcio citou nomes de pasta de gabarito e parecer, mesmo com a regra de não citar.
3. `_estado_oscar.md` não foi gravado nesta rodada (Oscar grava na próxima ativação).
4. Livro-razão e `_estado_lucio.md` acrescentados sem backup integral.
5. Entrega v2 (12/10) gravada antes do lacre e sem registro de gabarito alterado.

## 6. Pendências abertas para Skills e agentes
- Kelsen: TO 50% × 40% para SMD (Anexo XXI); varanda COES Art. 31 IV × alternativa A; dispensa de faixa Art. 215 §2º; Lei 13.146; Lei 12.651 Art. 4º II b; DL 9.760 Art. 2º; CC 1.301–1.302; Anexo XXV.
- Lúcio: nbr9050 linhas 20 e 90 (habite-se); Oscar grava estado; incluir gráfico na Skill nbr6492 para organograma.
- Acervo: NBR 9050:2020 ausente (só 2015).
- Bardi: remover "SHA256 PENDENTE" do cabeçalho do gabarito; decidir GB-3 com Claudemberg.
- Enunciado: remover metragem por ambiente sem dado; corrigir rótulo "construída máxima" (linha 45).
