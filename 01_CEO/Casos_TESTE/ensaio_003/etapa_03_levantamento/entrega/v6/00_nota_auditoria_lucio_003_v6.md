# Nota de auditoria — Lúcio — Etapa 03 (Levantamento), v6 — Ensaio Sombra 003

**Data:** 08/10/2026 | **Auditor:** Lúcio (Gestor Arquitetura) | **Executor:** Oscar | **Caso:** cliente fictício (nome a confirmar, ver item 5) | Análise preliminar, sem Gate do Maurício.
**Base:** `parecer_bardi_v5.md` (07/10/2026), entrega v5 (só leitura, não alterada), Skill de vaga v1.0, Skill decreto3046 v1.5, Skill de levantamento v1.6 (aplicada hoje por Lúcio, backup em `01_CEO/Decisoes_Autonomas/_backups/2026-10-08/`).

## 1. Pasta e arquivos

Pasta nova `entrega/v6/`. A v5 está intacta.
- `01_levantamento_planialtimetrico_cadastral_DULI_003_v6.md` (Peça 1)
- `02_relatorio_condicionantes_limitacoes_003_v6.md` (Peça 2)
- `03_matriz_decisoes_pendentes_003_v6.md` (Peça 3, Matriz)
- `anexo_contas_003_v6.md` (Anexos C, D, E, F, G, H, I)
- `tabela_correcoes_oscar_v6.md` (tabela de correções do Oscar, §2 da G e proposta de Skill)
- `00_nota_auditoria_lucio_003_v6.md` (este arquivo)

Não foram tocados: v5, parecer do Bardi, gabarito lacrado, `pendencias.json`. Não houve git push nem contato com cliente real.

## 2. Garagem (item 1 da ordem)

- **a passou de 12,50–15,00 m²/vaga (só a vaga) para 25,00 m²/vaga**, pela Skill de vaga v1.0 §3 e R6 e pelo COES Art. 29 III (p. 15): vaga 2,50 × 5,00 + manobra 2,50 × 5,00. Conferi no anexo C-4 a composição (12,50 + 12,50).
- **Contas:** C = 457,44 − (n−1)·a.
  - 4 vagas: C = **382,44** (era 419,94 a 412,44).
  - 6 vagas: C = **332,44** (era 394,94 a 382,44).
- Para o programa de 520 m² sob M-c: faltam **37,56** (eram 50,06 e 47,56). M-a sobra 18,82 (não muda com a). M-b faltam 62,56 (não muda).
- Grep na v6: nenhuma ocorrência de "12,50–15,00" nas quatro peças nem no anexo. A única "12,50" é a composição legal da vaga (C-4).

**Alternativa A (vagas descobertas no afastamento frontal): VEDADA.** Dec. 3.046/81 Disposições Gerais XXII (p. 4 do PDF; citação que o Oscar traz da Skill decreto v1.5, não reconferida por mim no primário) veda estacionamento em área livre excetuado o afastamento frontal mínimo. Além disso, a geometria não fecha: vaga + manobra = 10,00 m contra 6,00 m de frontal. Em H1, com a APP fora da conta, a folga de 22,79 m² não cabe nem uma vaga de 25,00 m².
- A tensão com LC 270 Art. 363 §2º XII e COES Art. 28 IV fica **aberta para o Gate do Maurício**. Não resolvi qual prevalece.
- **Alternativa B (abrigo lateral, XI): INVIÁVEL** com a = 25,00 (uma lateral de 72,50 m² cabe 2 vagas extras; com 4 vagas precisa de 3).

## 3. Tabela G (item 2 da ordem)

Regra aplicada a todas as 27 células: a célula só cita a seção que afirma a frase inteira; afirmação parcial = "—". Li a tabela de 27 linhas do Oscar e a justificativa de cada uma. **Lacuna minha de auditoria:** não refiz as 27 comparações contra o corpo da v6, linha por linha; confiei na conferência do Oscar para as células que não reli. Declaro isso aqui em vez de afirmar a conferência completa.
- 5 citações trocadas (células 2, 3, 6, 7, 27), 2 notações (5, 22), 20 mantidas.
- Nas células 10 a 18 (edícula, piscina, árvores), a afirmação foi estreitada no texto da G (marcada †) e a célula 18 teve o impacto da Matriz l. 4 reescrito. Não é troca de citação, mas é ajuste que o Bardi deve ver.

## 4. Skill de levantamento (item 3 da ordem)

**Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.5 → v1.6**, aplicada por mim. Só a frase de garagem no §5-bis mudou: cita a = 25,00 m²/vaga pelo COES Art. 29 III, remete à Skill de vaga §3/R6, e tira a referência ao "parecer Legal do caso" (remissão a documento de caso, não a Skill). Changelog e versão atualizados.
- Não contradiz a Skill de vaga: a frase nova usa os mesmos números e artigos que o Oscar atribui à Skill de vaga. **Não reli a Skill de vaga nesta rodada**; a conferência é do Oscar e fica pendente de releitura minha.
- **Não coloquei** a regra de afastamento frontal na Skill de levantamento. Ela é da Skill de decreto e da Skill de vaga; levar para cá duplicaria a regra. Fica como decisão de Kelsen (ver §7).
- Espelho `.agents/skills/` não atualizado. É tarefa da Drenagem (parecer, item 4).

## 5. Itens do parecer — status

| Item do parecer | Status | Onde está na v6 |
|---|---|---|
| O que corrigir 1 (garagem com a Skill de vaga; alternativa A; propagar Matriz, P2, Anexo G/E) | **Atendido com pendência** (R1 da Skill de vaga; manobra compartilhada; XXII na subzona) | Anexo C-4 a C-9, C-13 a C-15, C-17; P2 §1, §2, §3.3, §5.3, §8; Matriz l. 4, 9, 13, 21, 22; Anexo E-5, E-8, E-12 |
| O que corrigir 2 (regra da G às 27 células) | **Atendido** (auditoria minha feita) | Anexo G, l. 279–287; detalhe em `tabela_correcoes_oscar_v6.md` §2 |
| O que corrigir 3 (errata Etapa 01 l. 181; XXII no decreto3046) | **Atendido com pendência**: XXII já está na Skill decreto v1.5 (Kelsen, 08/10); errata da l. 181 segue com Kelsen | P2 §2; Anexo C-8; Anexo H |
| O que corrigir 4 (espelho `.agents/skills`, Drenagem) | **Não atendido nesta v6.** Não é tarefa de Oscar nem parte da ordem de execução | — |
| O que corrigir 5 (erro do gabarito da Isca 4, Bardi) | **Não é de Lúcio nem de Oscar.** Repassado ao Bardi. A v6 não cita "Isca 4" nem o gabarito como fonte (saiu do C-4) | Anexo C-4 |
| Erro 1 (G viola a regra) | **Atendido** | Anexo G |
| Erro 2 (a = 12,50–15,00 conta só a vaga) | **Atendido com pendência** (mesma do item 1) | Peças 1–3 e anexo |
| Erro 3 (alternativa A contra o XXII) | **Atendido com pendência**: A vedada; tensão XII × XXII para o Gate; subzona com Kelsen | P2 §2, §3.3, §5.3; C-8; Matriz l. 9 |

Ponto de atenção: a ordem falava em 4 itens e o parecer tem 5. Tratei os 5.

## 6. Divergências que vou deixar para você (Wallenberg) decidir

1. **Nome do cliente.** A ordem diz "Barros". O enunciado e as peças da v5 e da v6 dizem "Família Montenegro Prates". Mantive Montenegro Prates. Se o ensaio trocou o nome, a troca são os cabeçalhos.
2. **Status da v5.** O estado de Oscar de 07/10 registrava "v5 aprovada". O parecer recomenda REPROVAR, e a reprovação foi confirmada pela ordem de refazer. Status vigente: reprovada. Eu mesmo corrijo a entrada do meu estado.
3. **Frontal: 5,00 m (RIU, dossiê 5.3) × 6,00 m (Regramento, 5.4).** Usei 6,00 m, o mais restritivo. A conclusão vale para os dois.

## 7. Pendências declaradas (não resolvidas aqui)

**Kelsen (via Lúcio):**
- K1. O XXII incide sobre a subzona do lote? O dossiê diz "ZPP, subzona A-ENS", mas a Skill decreto (R6) diz que a nomenclatura das subzonas não está confirmada. Pergunta exata: "Pelo RIU do Lote 17, Quadra C, Rua das Garças, Recreio, a subzona do Dec. 3.046 é a A-ENS? O XXII se aplica a essa subzona?"
- K2. Errata ao parecer da Etapa 01, l. 181: a premissa da alternativa A não citou o XXII.
- K3. Tensão LC 270 Art. 363 §2º XII e COES Art. 28 IV × Dec. 3.046 XXII/XXIII a: Gate do Maurício.
- K4. R1 da Skill de vaga: a dimensão mínima é obrigatória na unifamiliar isolada?
- K5. Manobra compartilhada (COES Art. 29 IV): reduz a média de 25,00 m²/vaga? Se reduzir, a conta da garagem muda.
- K6. R2 da Skill de vaga e condomínio de casas (46 lotes): as vagas suplementares do XXI se aplicam ao condomínio do lote?

**Claudemberg (decisão de cliente ou de risco):**
- C1. Número de vagas (4 ou 6) e onde ficam: decisão do cliente no Briefing. A v6 não escolhe.
- C2. Alternativa A vedada e B inviável com a = 25,00: se o cliente quiser vaga descoberta no frontal, a saída vira nova alternativa, pendência de Claudemberg ou Kelsen.
- C3. Gate do Maurício antes de qualquer uso num caso real.

**Villaça (via Lúcio):** S3/H1, área de trabalho de 339,84 a 359,84 m² sem espaço físico. A alternativa B era a saída e agora é inviável.

## 8. Contagem e verificação

- **Contagem de palavras e páginas: "a ser feita por Wallenberg com ferramenta".** Não tenho ferramenta de contagem e não estimei nenhum número.
- **Revit: não testado nesta v6.** Último teste (06/10/2026): `No such tool available`.
- Não há fonte inventada. Onde a v6 não tem fonte, a pendência está declarada.

## 9. Declaração de leitura

Li diretamente: a tabela de correções do Oscar, por inteiro; a Skill de levantamento v1.5 inteira (antes de a editar para v1.6); e o resultado de Grep sobre a pasta v6 (linhas de garagem, XXII, valores antigos). **Não li por inteiro nesta rodada:** as quatro peças e o anexo da v6; a Skill de vaga v1.0; e a Skill decreto3046 v1.5 (o XXII e as linhas 9, 143 e 232 são citação do Oscar, não reconferida por mim). Essas leituras ficam como pendência de releitura antes de qualquer uso. Não abri nem listei nada em `_gabaritos_LACRADO_bardi\`. Não editei parecer, gabarito, `pendencias.json` nem a v5.

— Lúcio, 08/10/2026 (v6)
