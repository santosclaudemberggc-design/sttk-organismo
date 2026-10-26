# Revisão final das falhas — Ensaio Sombra 003 (etapas 1-5)

Bardi, 21/10/2026, a pedido de Wallenberg. Base: `_estado_ensaio_003.json` (regra l. 4; `encerramento_21_10`), `notas_assertividade.md`, pareceres das etapas 1-5, `etapa_04_briefing/diagnostico_repeticao.md`, `Registro_Erros/registro.json`, `D:\011_VITRUVIUS\VITRUVIUS_ERROS_RAIZ.md` (E-30 a E-32) e `mapa_prontidao_etapas_04_17.md`. Sem nota nova. **Tudo da seção 3 em diante é PROPOSTA: nada se aplica sem Claudemberg.**

## 1. Resultado por etapa

| Etapa | Tentativas | Notas (versão que fechou) | Resultado | Fonte |
|---|---|---|---|---|
| 01 Legal base | 1 | Kelsen 8,50 · Hely 8,75 | Aprovada 01/10 | estado, histórico etapa 1; notas l. 7-8 |
| 02 Viabilidade | 9 (v1-v9, antes do teto de 3) | v9: Villaça 8,00 · Fiker 10,00 | Aprovada 05/10 | estado, etapa 2 v9; notas l. 9-32 |
| 03 Levantamento | 8 (v1-v8) | v7: Lúcio 8,20 · Oscar 8,50; v8 vira referência (Lúcio 8,70 · Oscar 8,50) | Aprovada 08/10 | estado, etapa 3 v7/v8; notas l. 33-57 |
| 04 Briefing | 3 contadas (v1, v3, v4; v2 anulada por lacre violado) | v4: Lúcio 6,50 · Oscar 4,75 | Encerrada no teto, "aprovada com pendências" 13/10 (abaixo de 8,00) | estado, etapa 4; `diagnostico_repeticao.md` |
| 05 Estudo Preliminar | 3 (v1, v2, v3; Fase 3 do modelo 7,60 → 8,75) | v3 final: Lúcio 8,25 · Oscar 8,50 · Burle 9,50 · Portinari 8,00 | Aprovada 21/10, com trava da 06 (corte ≥ 17,31 m²) | estado, `etapa_5_aprovada`; `parecer_bardi_v3_final.md` |

Leitura: Legal passou de primeira; Arquitetura (Lúcio/Oscar) gastou 14 das 24 tentativas e é a única que fechou etapa abaixo de 8,00.

## 2. Falhas agrupadas por padrão

| # | Padrão | Ids do registro / fonte |
|---|---|---|
| P1 | **Afirmação sem prova colada** ("Atende", "verificado", "declarado em X" sem trecho, imagem ou saída da ferramenta) | E-2026-10-19-03, -06; E-2026-10-21-01, -02 (largura da vaga), -10 (deck só por Grep) |
| P2 | **Gestor deixa passar "atende" falso** (auditoria do Lúcio aprova o que o produto não cumpre) | E-2026-10-19-06; E-2026-10-21-06 (fechou sem propor o corte), -10; Etapa 04 v3/v4 (SMD omitida aprovada) |
| P3 | **Herança que some** (número de etapa aprovada não chega à seguinte; regressão entre versões) | E-2026-10-19-01 (SMD/TO 50%), -04 (TO privada × zona); E-2026-10-21-11 (SMD não recalculada em 571,60); Habite-se 1999 sumido na 04 v4 |
| P4 | **Skill errada ou incompleta** | E-2026-10-19-02 (nbr9050 l. 15), -04, -05; E-2026-10-21-05 (fator 0 sem artigo), -10; P-2026-10-19-09 (Anexo XXI sem Skill); Skill de vaga Art. 29 III/IV (notas l. 45, 50, 55) |
| P5 | **Skill lida e não usada** | E-2026-10-19-05 (Art. 31 III-IV; 3 de 10 Skills declaradas na 04) |
| P6 | **Limite privado × público confundido** (Regramento 40% × RIU 50%; "limite da prefeitura") | E-2026-10-19-04; E-2026-10-21-06, -09 |
| P7 | **Ferramenta com defeito** (Vitruvius) | E-30 (escada/patamar), E-31 (base do quadro de áreas), E-32 (resize falso sucesso; cota mede eixo; piscina/deck fora da soma; colisão de nome na exportação); P-2026-10-19-01 (plugin desconectado) |
| P8 | **Falta de ferramenta** | P-2026-10-19-02 (Bardi sem hash/contagem); Burle sem render (mapa l. 10); Hely sem WebFetch (mapa l. 12); P-2026-10-19-10 (NBR 9050:2020 fora do acervo) |
| P9 | **Acabamento de desenho e de peça ao cliente** | E-2026-10-21-07, -08, -09 |
| P10 | **Erro do examinador (gabarito/enunciado)** | E-2026-10-19-07, -08, -09; P-2026-10-19-03; P-2026-10-19-05 (nome do gabarito visível) |
| P11 | **Dessincronização de cópias** (Skills e agentes em 3 lugares) | P-2026-10-19-04, -11 |
| P12 | **Rotina Diária sem foco** | P-2026-10-19-06, -07, -08 |

## 3. Propostas por padrão

| Padrão | Tipo | Proposta | Dono |
|---|---|---|---|
| P1 | **criar novo** | Bloco obrigatório "Prova" no fim de toda entrega: cada "Atende" com trecho colado, saída bruta da ferramenta ou imagem; sem isso, a palavra vira "não verificado". Uma regra só, no slice de Agente, em vez de repetir em cada Skill. | Wallenberg → Claudemberg |
| P2 | **recriar** | Recriar a auditoria do Gestor como tabela fixa: entregável mínimo item a item + amostra de 5 afirmações conferidas no artefato + "limites legais conferidos (projeção bruta × teto)". Auditoria sem a tabela = Gestor não entregou. | Lúcio (vale para todo Gestor: Wallenberg → Claudemberg) |
| P3 | **criar novo** | Tabela "herança recebida" no início de cada etapa (número, origem, versão), gerada pelo Bardi no enunciado e conferida pelo Gestor (já proposta em E-2026-10-19-01). | Bardi + Lúcio |
| P4 | **ajustar** | Corrigir as Skills apontadas (nbr9050, checklist SMD do Oscar, quadro-de-areas-rj com artigo do fator 0 e linha do Regramento, vaga) e instalar a do Anexo XXI. Cada correção com a pergunta de teste do registro. | Lúcio (nbr9050, checklist); Kelsen (quadro, vaga, Anexo XXI) |
| P5 | **ajustar** | Tabela "Skill lida → onde foi usada", linha vazia = devolução pelo Gestor (E-2026-10-19-05). | Lúcio |
| P6 | **ajustar** | Na Skill quadro-de-areas-rj e no deck: todo limite escrito com o dono ("condomínio, Regramento Art. 5º" × "município, LC 270"). Bardi passa a ter isca fixa de "qual limite?" em toda etapa de Arquitetura. | Kelsen + Lúcio; Bardi |
| P7 | **organizar** | Fechar E-32 (4 defeitos) e conferir E-30/E-31 antes da Etapa 06; enquanto não fechar, a Skill do Oscar manda conferir medida depois do resize e não provar largura útil por cota de face. | Wallenberg (Vitruvius) → Claudemberg |
| P8 | **criar novo** | Script só de leitura para hash e contagem (P-2026-10-19-02); decisão do orçamento de render do Burle e do WebFetch do Hely; NBR 9050:2020 na lista de compra. | Wallenberg → Claudemberg |
| P9 | **ajustar** | Checklist de "limpeza de prancha" na Skill nbr6492-representacao-grafica (cota solta, rótulo sobreposto, vista exportada da data certa); Portinari confere data de cada imagem do deck. | Lúcio |
| P10 | **organizar** | Instalar a Skill de checagem pré-lacre (P-2026-10-19-03), mover os gabaritos para fora do repositório (P-2026-10-19-05), decidir as erratas pendentes das etapas 03 e 04. | Bardi; Wallenberg → Claudemberg |
| P11 | **criar novo** | Script que compara as 3 cópias de Skills e os pares agente .md × .toml (P-2026-10-19-04, -11). | Wallenberg → Claudemberg |
| P12 | **ajustar** | Passo 0 da Diária lê o registro e pendências abertas; pesquisa só com lacuna aberta (P-2026-10-19-06 a -08). | Wallenberg → Claudemberg |

## 4. Membros abaixo de 8,00 na média

| Membro | Média (n) | Leitura | Proposta |
|---|---|---|---|
| Lúcio (Gestor) | 7,81 (14) | Puxado pelas etapas 04 e 05 v1-v2: auditoria que aprova sem prova (P1, P2). | Recriar a auditoria (P2) e um exame curto só de auditoria antes da Etapa 06: entrega plantada com 3 "atende" falsos; passa com 8,00. Sem mudança de nível até passar. |
| Oscar (Agente) | 7,57 (16) | Melhorou na v3 (8,75 e 8,50); os baixos vêm de prova ausente, herança e ferramenta. | Manter na equipe; exame de regressão nas 4 pendências do EP (E-2026-10-21-01, -02, -07, -08) junto com o corte; separar no parecer o desconto de ferramenta (P7) do de declaração. |
| Skill arquitetura-nbr9050 | 7,50 (1) | Contradição da l. 15 aberta desde 09/10. | Ajustar (E-2026-10-19-02) e retestar com a pergunta do registro. |

Demais Skills e membros ficaram em 8,00 ou mais. Villaça (8,14) e legal-base (8,00) estão no limite: acompanhar.

## 5. O que herda o Ensaio 004

- **Etapas 6-17**, com os bloqueios do mapa: 06 🔴 (pranchas, cortes e quadro dependem do Vitruvius: E-32 aberto; Burle sem render); 07 🟡 (Hely sem WebFetch; quadro depende da 06); 08-13 🟡 (memorial em texto; o enunciado deve dizer o que o Agente prepara e o que só o habilitado assina); 14-15 🟡 (Zanettini e Reidy em Shadow; sem clash); 16 🟡 (SINAPI via Wallenberg); 17 🟡 (trava sem 14-16).
- **Trava de entrada da 06:** E-2026-10-21-06, corte de ≥ 17,31 m² na projeção bruta (245,95 → ≤ 228,64 m², TO 40% do Regramento), decisão de Claudemberg de 21/10.
- **Itens abertos:** E-2026-10-19-01 a -07 e -09; E-2026-10-21-01 a -11; P-2026-10-19-01 a -11; E-30 a E-32 do Vitruvius; abertos do estado de 21/10 (largura interna das vagas cobertas; vigência dos atos na Busca Fácil; responsável do E-2026-10-21-05); conversão da vaga 2 em guarda no modelo e no quadro.
- **Caso do 004 — proposta para Claudemberg:** reusar o caso Montenegro a partir do `EP_v3.rvt`, porque as etapas 6-17 são cumulativas e um caso novo exigiria refazer 1-5 antes de testar o que nunca foi testado. Três condições: (1) o 004 começa pela correção do corte e das pendências do EP, como entrada da 06, sem contar tentativa; (2) iscas novas só com fatos novos (o time já conhece o lote, então herança velha não mede mais nada); (3) depois do 004, um caso novo curto refaz 1-5 para medir se as correções da seção 3 seguraram (regressão).
