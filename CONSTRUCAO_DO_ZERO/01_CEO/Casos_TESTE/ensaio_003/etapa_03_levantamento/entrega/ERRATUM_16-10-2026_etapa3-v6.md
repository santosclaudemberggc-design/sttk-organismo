# ERRATUM — Etapa 03 (Levantamento), Ensaio 003 — 16/10/2026

**Autor:** Lúcio (Gestor Arquitetura), rodada agendada da Drenagem Contínua.
**Escopo:** correção das notas de auditoria e da citação do parecer v6 (pendência `erro-ensaio003-etapa3-v6-lucio-08-10`).
**Não altera:** entrega v6 (reprovada), v7, nem v8 (referência aprovada). Nada foi reaberto.
**Fontes primárias lidas nesta rodada:** `CONSTRUCAO_DO_ZERO/01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` (pp. 15, 17, 19), `COES_LeiComplementar198_2019_impressaoWeb_Claudemberg.pdf` (p. 19), `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf` (p. 3), `enunciado.md` (itens 5.1 a 5.3).

| # | Afirmação no parecer v6 / nas notas | Verificação | Correção |
|---|---|---|---|
| 1 | COES Art. 29 III está na p. 19 | Consolidado SMU p. 15: "III - deverão estar obrigatoriamente demarcadas, exceto quando estiver atendida a proporção mínima de vinte cinco metros quadrados de área de estacionamento por vaga...". P. 19 = Art. 34 §3º a Art. 35 §6º. Na cópia impressionWeb, p. 19 = Art. 34. | Art. 29 III está na **p. 15**. Não está na p. 19. |
| 2 | "25 m²/vaga tem base em Art. 29 I+II" | I = vaga 2,50 × 5,00 m; II = manobra 2,50 × 5,00 m. Os 25 m² não aparecem em I nem em II. 12,50 + 12,50 = 25,00 é soma minha, não texto. | O 25 m² é o **limiar de dispensa de demarcação** do III. I e II dão as dimensões. |
| 3 | "571,80 como área oficial" (v6 P1 l. 20) | Enunciado 5.1: matrícula 15 × 40 = **600 m²**. 5.3: RIU **600 m²**. 5.2: levantamento 2024, 14,30 × 40 = **571,80 m²**. Enunciado l. 41: "Se mantiver 14,30 m, a área fica 571,80 m² (não 600 m²)". | A área oficial (matrícula e RIU) é 600 m². 571,80 é a medida de 2024 adotada para cálculo até regularizar a divisa, com a divergência documentada. (v7 nota 00, E2, já corrigiu.) |
| 4 | Alternativa A "vedada" sem qualificador (v6 P2 l. 12; Matriz l. 24; nota 00 l. 27) | "Vedada" depende de Dec. 3.046 XXII, citado da Skill decreto3046 v1.5. Não reconferi o XXII no PDF nesta rodada. A aplicação à subzona não está confirmada (K1, Kelsen). A tensão com LC 270 Art. 363 §2º XII está em Gate. | Ler: "vedada na leitura restritiva do Dec. 3.046 XXII; subzona a confirmar (K1); tensão com LC 270 Art. 363 §2º XII em Gate". |
| 5 | C-9 "lê o XI pela metade" | Não encontrei a palavra "metade" no C-9 (anexo v6 l. 115-122) nem no XI. O XI (Dec. 3.046, p. 3, verbatim): "os afastamentos laterais no pavimento térreo poderão ser ocupados por varandas ou abrigos de veículos, **desde que abertos e cobertos por telha-vã**, não sendo as respectivas áreas computadas na A.T.E. e da taxa de ocupação." O C-9 usa a faixa lateral inteira (2,50 × 29,00 = 72,50 m²), omite a condição "telha-vã" e não cita a fonte da largura de 2,50 m. | Falha real: C-9 omite a condição do XI e não cita a fonte da largura. A conclusão "B inviável" não muda: a condição só restringe, então não cabe mais área. |
| 6 | Errata da l. 181 "pendente" (C-8, nota 00 l. 50) | Existe como pendência do Kelsen em `pendencias.json`, id `lacuna-kelsen-dec3046-xxii-vaga-afastamento-frontal-07-10-2026` (ação: registrar errata da l. 181 do parecer Legal da Etapa 01). | Tratar como pendente, citando esse id. A errata ainda não foi registrada. |
| 7 | G "Atendido (auditoria minha feita)" (nota 00 v6 l. 49) | Nota 00 v6 l. 33 já admite: "não refiz as 27 comparações... confiei na conferência do Oscar". A l. 49 contradiz a l. 33. | Ler: "Atendido por conferência do Oscar; não refeito por mim" (ver §3 abaixo). |
| 8 | Art. 31 III–IV (p. 17) | Lido nesta rodada no PDF SMU p. 17: III "vagas de estacionamento;" e IV "afastamento frontal, para estacionamento coberto de veículos, em telha vã, com um pavimento de altura;". | Já estava verbatim na Skill de vaga §2-bis (conferido pelo Kelsen em 08/10). Passou a constar também no §5-bis da Skill de levantamento v1.12. |
| 9 | Gate da R6 (C3 de Claudemberg) | Declarado na Skill de levantamento §5-bis (item C3, v1.7 em diante) e na Skill de vaga (l. 17, 88, 110). A entrega v8 traz "sujeita ao Gate" (l. 4 do DULI v8 e nota v8). | Já estava declarado; não foi preciso incluir. A v8 diz "Gate do Maurício", lido como Gate da Coordenação validado por Claudemberg desde 09/10 (cabeçalho do estado). |

## Limite declarado
- O item 4 não foi revalidado no PDF do Dec. 3.046 (p. 4). Permanece citação da Skill decreto3046 v1.5.
- A largura de 2,50 m da faixa lateral do C-9 não tem fonte primária nesta rodada.
- Nenhum número de dimensão ou de área foi alterado.

## §3 Correção das notas de auditoria
- Nota 00 v6 (`entrega/v6/00_nota_auditoria_lucio_003_v6.md`): linha 49 deve ler "Atendido por conferência do Oscar; não refeito por mim (ver linha 33 e ERRATUM item 7)".
- Nota 00 v7 (`entrega/v7/00_nota_auditoria_lucio_003_v7.md`): a divergência "p. 19 × p. 15" fica resolvida por este erratum (item 1).
