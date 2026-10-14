# Auditoria de Lúcio, Etapa 05 (Estudo Preliminar), Ensaio Sombra 003
## Montenegro Prates. Lúcio, 14/10/2026. Caso 100% fictício. Análise preliminar, não aprovação.

Checklist usado: `checklist_auditoria_lucio.md` (partes 0 a 4). Entrega auditada: Oscar (01 a 07, 99), Burle (08), Portinari (09).

## 0. Antes de auditar
- Checklist do Oscar presente e preenchido nas partes (a) a (e), com prova em 99 §(b). **OK.**
- Herança recebida: Oscar declara ter recebido Etapa 01 (com duas erratas), Etapa 02 v9 e custo v8, Etapa 03 v8 (sete arquivos) e Etapa 04 v4 (nove arquivos). **Não recebeu nada além do listado.** Não há falha de processo de entrada registrada.

## 1. Herança (refiz a amostra na origem)
| Item | Origem (eu li) | Entrega (99 (a)) | Resultado |
|---|---|---|---|
| TO 40% (Regramento) prevalece sobre 50% (RIU) | `etapa_01_legal_base\entrega\parecer_legal_base_003.md`, linha 29: "Taxa de ocupação ... **40%** ... 40%" | 99 (a) linha 17; 01 §1 | Confere |
| Permeável 25% = 142,95 m² | mesmo arquivo, linha 36 | 99 (a) linha 21; 02 §B | Confere |
| Edícula computa (conservador) | mesmo arquivo, linha 39: "**Conservador: computa na ATE e na TO**" | 99 (a) linha 25; 05 E-14 | Confere |
| Vaga descoberta no frontal: não é solução sem Gate | `parecer_legal_etapa_01_ERRATA_08_10_2026.md` (lido por mim): Dec. 3.046 XXII veda estacionamento coberto no afastamento frontal | 99 (a) linha 56 | Confere. Oscar cita "ERRATA_08-10-2026.md, linhas 22–26" sem eu ter aberto esse arquivo: **não verificado por mim** |
| Divergência 1 (Oscar): "P2, P6, P-h, P-k, P-l não existem na Etapa 04 v4" | Grep em `etapa_04_briefing\entrega\v4` por "P-h", "P-k", "P-l", "P2", "P6": **P-h existe** (`04_matriz_decisoes_cliente_003_v4.md` linha 73, T-01 "SMD ... Kelsen (P-h)"); P6, P-k e P-l não aparecem; P2 aparece só como "Etapa 01 P2" (linha 37) | 07 §3 item 3 | **Parcial.** Oscar errou ao dizer que P-h não existe. P-k e P-l e P6 confirmados ausentes |
| Divergência 2 (Oscar): Etapa 03 v8 sem aprovação formal encontrada | Não reabri (ver §5). Enunciado linha 23 diz "referência aprovada" | 99 (a) linha 61 | Aceito como lacuna declarada. **Decisão de Wallenberg/Claudemberg** |

**Devolução ao Oscar por herança: não.** Nenhum parâmetro da minha lista ficou fora da tabela (a). O erro sobre P-h é de declaração, não de omissão de parâmetro.

## 2. Prova (amostra de 5 afirmações, priorizando número e "atende")
| Afirmação | Minha conta / minha leitura | Resultado |
|---|---|---|
| 0,40 × 571,80 = 228,72; × 2 = 457,44 | 228,72 × 2 = 457,44 | Confere |
| Déficit H0 = 520 − 457,44 = 62,56 | 62,56 | Confere |
| H1: 9,29 × 16,00 = 148,64; × 2 = 297,28; déficit 222,72 | 148,64 × 2 = 297,28; 520 − 297,28 = 222,72 | Confere |
| SMD: 0,10 × 571,80 = 57,18; 0,20 × (571,80 − 228,72) = 68,62 | 0,20 × 343,08 = 68,616 ≈ 68,62 | Confere |
| Sensibilidade RIU: (14,29 − 3,00) × (40,00 − 5,00 − 1,50) = 378,22 | 11,29 × 33,50 = 378,215 ≈ 378,22 | Confere |
| Permeável: folga 571,80 − 269,41 − 142,95 = 159,44; base 571,60 dá 159,24 | 302,39 − 142,95 = 159,44; 302,19 − 142,95 = 159,24 | Confere |
| Revit: 4 paredes com "Altura desconectada" 0.3; Ambientes 8; Portas 0; Janelas 0 | 06 §2.1 a §2.4 (saídas literais pasted) | Confere com o texto colado. **Não reexecutei a ferramenta.** Unidade do campo (m ou ft) **não confirmada** pelo Oscar; a conclusão "não conforme" vale nas duas leituras, porque 0,3 ft também é muito baixo |
| Edícula falta 1,70 (Regramento) e 0,70 (COES p.u.) | 2,50 − 0,80 = 1,70; 1,50 − 0,80 = 0,70 | Confere |
| Piscina: fundo 0,70 m abaixo do NA | 1,60 − 0,90 = 0,70 (pressupõe 1,60 de profundidade máxima) | Confere na conta. Profundidade real: não constam |
| Topo +11,70 = 3,20 + 8,50 | 11,70 | Confere |
| Sala 7 m: 7,00 + 2,50 = 9,50 > 8,50 | 9,50 | Confere |

Afirmações de PDF (COES Art. 8º §§1º–8º, Art. 29, Art. 31; LC 270 Arts. 215, 347, 350, 352, 353, 363; Dec. 3.046 Disp. Gerais VII, XI, XIV, XV, XXII, XXIII; LC 281 Art. 19 e 20; LC 301 Art. 58): **não verifiquei** por mim. Oscar declara leitura nas páginas indicadas (99 (b)). Pela minha regra, leitura só do Oscar = "não verificado por Lúcio", não OK. Ficam para conferência de Kelsen no que é legal (ver §4).

## 3. Entregável mínimo (enunciado, item por item)
| Item | Situação | Minha leitura |
|---|---|---|
| Entrega 1, corpo ≤ 2.500 palavras | Atende; contagem pendente de Wallenberg | Não contei. Declarado |
| Entrega 2, Revit: implantação, plantas, cortes, elevações | **Não atende** | Motivo do Oscar: sem metragem por ambiente e partido com decisões pendentes. **Parcialmente aceito:** o envelope H0 (9,29 × 29,00) já é dado aprovado e podia ter sido desenhado como implantação esquemática com lacunas marcadas. Não foi. Deficit real, registrado |
| Entrega 3, quadro de áreas por ambiente e regime | Parcial | Soma por ambiente não fecha. Declarado |
| Entrega 4, H0 e H1 | Atende | 03 |
| Entrega 5, matriz | Atende | 04 |
| Entrega 6, Burle e Portinari | Atende agora | 08 e 09 (ver §4) |
| Entrega 7, declaração de leitura e lacunas | Atende | 07 |
| Trava "altura das paredes conferida contra pé-direito" | Conferida; **não conforme** | Declarado. Não entregue como correto |

## 4. Skills e Agentes
- Skill `nbr6492-2021-memoriais-por-etapa-projeto` (EP-ARQ, item 5.4): **lida só por Grep** (linhas 35, 47, 61). A Skill do EP é a principal do enunciado. **Lacuna de forma (d), declarada pelo Oscar.** Ação: Oscar relê a Skill inteira no Etapa 06; não bloqueia esta etapa.
- Burle (08): **não gerou nenhuma imagem.** Motivos: pausa de orçamento do Higgsfield (decisão de Claudemberg, 17/08), ausência de base de projeto, e `generate_image`/`generate_video` **não apareceram na lista de funções da sessão dele**, sem teste. Aceito como bloqueio de ferramenta declarado. Recusas dos três pedidos (banco, poente, 7 m) estão fundamentadas em fonte.
- Portinari (09): roteiro de 12 lâminas, todas com "PRELIMINAR. NÃO APROVADO". **Recusou a marcação "aprovada" para o banco** (Helena, 14/10). Não usou render. Não afirmou sol da tarde nem cabe de 520 m². Correto.

## 5. Ressalvas que vão junto à entrega
1. Entrega 2 (desenhos no Revit) não atendida. Faltam implantação, plantas, cortes e elevações. Isso é deficit do exame, não é aceito como "não aplicável".
2. Oscar errou ao dizer que P-h não existe na Etapa 04 v4 (existe em T-01). Corrigir na nota.
3. Unidade do campo "Altura desconectada" não confirmada (m ou ft).
4. Leituras de PDF e de Regramento: declaradas pelo Oscar, não verificadas por Lúcio.
5. Skill nbr6492 lida só por Grep.
6. Enunciado diz "Etapa 03 v8 aprovada" e "Etapa 04 aprovada com pendências". Oscar não achou registro de aprovação da 03 v8, e a 04 v4 tem auditorias 004, 004b e 004c com "NÃO APROVADO" (`etapa_04_briefing\entrega\v4\08_auditoria_lucio_004c.md`, conforme meu estado). **Decisão de Wallenberg/Claudemberg.** Não resolvi.
7. Defeitos de 13/10 não corrigidos no arquivo de teste (paredes, sufixo " 8"). Correto não corrigir sem decisão.
8. Contagem de palavras pendente de Wallenberg, em todos os arquivos.

## 6. Resultado da minha auditoria
- Partes 1 (herança) e 2 (prova): **fecham sem falha de herança e sem prova ausente**, com a ressalva do P-h e das leituras de PDF marcadas "não verificado por Lúcio".
- Parte 3: entregável incompleto na Entrega 2 e na Skill 6492.
- **Não devolvi ao Oscar**, porque a regra de devolução pede falta de herança ou prova, e não há nenhuma. As ressalvas 1 e 2 ficam para o Bardi e para a próxima etapa.
- Esta auditoria não é aprovação. Pronta para o Bardi com ressalvas declaradas. Gate da Coordenação (Claudemberg) pendente.
