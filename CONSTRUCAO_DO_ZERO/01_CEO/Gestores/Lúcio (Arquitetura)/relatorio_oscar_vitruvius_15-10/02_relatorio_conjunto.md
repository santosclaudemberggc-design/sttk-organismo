# Relatório conjunto Lúcio + Oscar — o que melhorar no Oscar e no Vitruvius (15/10/2026)

**Pedido:** Wallenberg, decisão de Claudemberg de 15/10/2026. **Base:** `01_diagnostico_bardi.md` (Bardi) e `01b_resposta_oscar.md` (Oscar, lida por mim na íntegra). Fontes de não repetição: `D:\011_VITRUVIUS\PEDIDOS_OSCAR\09_...` (P1–P11), `05_analise_prints_EP_v2_14-10.md` (C/N), `PADRAO_SKILL_E_AGENTE_v1.md`.
**Não feito nesta rodada:** nenhuma chamada Vitruvius, nenhum gabarito lido, ensaio e trava intocados, sem commit. A trava da v3 da Etapa 05 segue fechada até o Bloco 1.

## Posição do Oscar (resumo)
- **Grupo A:** concorda com os 13 (prova no próprio estado e na Skill).
- **Grupo B:** concorda com 9 (B3, B4, B6, B8, B11, B13, B16, B17, B18); em parte com 8 (B1, B2, B7, B9, B10, B12, B14, B15: parte é falha dele ou a descrição atual da tool já promete o recurso, sem teste); discorda de B5 no build atual (`annotate` tem norte, texto e etiqueta e funcionou em 14/10).
- **Minha leitura:** aceito as posições. Em B1 e B14 a parte dele já está coberta em A1 e na Skill §4/§6.

## Decisão conjunta sobre C1–C4
| # | Decisão | Fecha com |
|---|---|---|
| C1 cota vermelha | Indeterminado, provável **T** (tipo de cota do template). Não é A. | Teste em cópia: tipo das cotas da v2 + cota com tipo preto explícito, vista em PNG. Entra em T-a do arquivo 05 e P13. |
| C2 "NORTE" solto | **A** (origem T): remover era limpeza do Oscar. Regra na Skill §5. Pedido ao template de tirar o texto. | Já decidido. |
| C3 pé-direito/alturas | Falta de justificativa = **A** (regra no checklist §10). Divergência texto × cotas: indeterminado (A, P5 ou P7). | Só leitura no v2_r1 + log de 14/10 — **não feito**, porque o arquivo é do ensaio; a autorizar por Wallenberg. |
| C4 Cobertura 6,30→6,20 | Indeterminado, provável **B** (P7); a Skill L45 registra "323714 → 6,20" como chamada R1 do mesmo dia, então pode ser registro do Oscar. | Busca no log de 14/10 por "323714" + reprodução em cópia. A autorizar. |

## PARTE A — correções no Oscar (aplicadas)
| Erro | Regra nova | Onde | D relacionado |
|---|---|---|---|
| A1 "Atende" sem conferir | Linha "Atende" traz caminho do PNG lido nesta execução + frase do que se vê; sem caminho, Lúcio trata como falsa | Skill §6 item 6 | D2, D3, D5, D17, D19 |
| A2 leitura parcial | Tabela de leitura com versão, total e intervalo; parcial = "[parcial: Lx–Ly]", não sustenta conclusão | oscar.md (f) | — |
| A3 Glob amplo | `**` só com ordem escrita; declaração separa listado/aberto/citado | oscar.md (e) | — |
| A4 fonte errada | Citação aberta nesta execução, com trecho de até 15 palavras | oscar.md (e) | — |
| A5 conteúdo perdido | Tabela versão anterior × nova; item sumido sem linha = regressão | oscar.md (g) | — |
| A6 organograma em ASCII | Gráfico como imagem com caminho na entrega | oscar.md (h) | — |
| A7 afirmação sem fonte | Já coberto pelo checklist (d) e (e) (artigo + cópia + página); reforçado por A4 | oscar.md (d)/(e) | — |
| A8 EP sem desenhos | Peças 5.4.2 a–d sempre, em esquema, lacuna no título; omissão só com ordem escrita | Skill §9 | — |
| A9 superior sem porta, sem eixos | Prova: portas por nível, eixos nas duas direções, ambiente "ESCADA (lacuna)" | Skill §3 | — |
| A10 medidas que não fecham / partido sem justificativa | Área do lote pelos vértices ±0,01 m², conta colada; uma frase por decisão de partido | Skill §2 e §10 | D20 |
| A11 suíte NBR 9050 | Atende só com Skill nbr9050 lida inteira + cotas + PNG | Skill §10 e oscar.md (f) | — |
| A12 3D exagerado | "sem ferramenta para criar ou ajustar vista 3D" + PNG da "EP. Perspectiva" | oscar.md, Lacunas (texto antigo "sem perspectiva 3D" substituído) | — |
| A13 estado não gravado | Última escrita = `_estado_oscar.md`, linha citada no retorno | oscar.md (i) | — |
| Skill atrás das descrições (Oscar L16) | §8-bis: salvar, ajustarExistente, base_deslocamento etc. = "[descrição, não testado]" até reconferência em cópia; contorno atual segue | Skill §8-bis | D12, F4, F6 |

Skill subiu para **v1.3.0** (changelog registrado; v1.2.2, que faltava no changelog, também registrada). Lista de tools do Oscar não alterada. Backups de Wallenberg em `Decisoes_Autonomas/_backups/2026-10-15/`.

## PARTE B — pedidos novos à ferramenta (P12–P30)
Texto integral, com evidência, efeito e prioridade: `D:\011_VITRUVIUS\PEDIDOS_OSCAR\10_pedidos_relatorio_conjunto_15-10.md`. Resumo:

| # | Assunto | Prioridade |
|---|---|---|
| P12 | `export_view_image` como rotina estável (N1, B1) | Alta |
| P13 | `dimension`: escala, cor, fora do desenho; D6, D7 (C1, B10) | Alta |
| P14 | Elevação: plano distante, mover marcador, recusar vazia (C2, B9, D3, D12) | Alta |
| P15 | Folha: layout dentro da moldura, escala na mensagem, reserva de carimbo (C4, B8, D9, D11) | Alta |
| P16 | `document`: bloquear D:\007_MATERIAIS/.rte; `abrir` sem sucesso falso nem queda (D1, D4) | Alta |
| P17 | Build e contrato testado devolvidos pelo status (L15, L16) | Alta |
| P18 | Furo de laje e escada (C10, N4, B4) | Alta |
| P19 | Corte: recorte, detalhe, posição (C3, C14, B14, D10) | Média |
| P20 | Parâmetros do navegador (C7, B12, D8) | Média |
| P21 | `niveisCotovelo` sem sucesso falso (C8, B13, D5) | Média |
| P22 | Selo por nome e carimbo (C5, C6, B7) | Média |
| P23 | Cobertura inclinada (C11, B6) | Média |
| P24 | Vista 3D (N8, B11) | Média |
| P25 | Lote, topografia pelo contorno, sub-região (N5, B15, L14) | Média |
| P26 | Plano de área por regime (L13) | Média |
| P27 | `create_rectangular_room` com base/topo (L9, B2) | Média |
| P28 | `check_model`/`check_sheet` (N3) | Média |
| P29 | Porta/janela: lado, giro, espelho (L10) | Baixa |
| P30 | `find_elements` categorias; `resize_element` × R5 (L11, L12) | Baixa |

Lúcio, 15/10/2026.
