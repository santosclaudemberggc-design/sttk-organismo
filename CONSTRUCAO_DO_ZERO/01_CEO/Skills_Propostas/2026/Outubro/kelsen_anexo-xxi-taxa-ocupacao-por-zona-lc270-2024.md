# Skill: Taxa de ocupação (TO) por zona — Anexo XXI da LC 270/2024

**Dono:** Kelsen (Gestor Legal)
**Status:** ativa-com-ressalva
**Versão:** 1.0 (15/10/2026)
**Fonte primária:** LC 270/2024 — Anexo XXI (PARÂMETROS DAS ÁREAS DE PLANEJAMENTO), arquivo `Agentes\Hely\Fontes_Legislacao\LC270_2024_PlanoDiretorLUOS.pdf`, pp. 274 a 277 do PDF.
**Lacuna que fecha:** `lacuna-kelsen-lc270-anexo-xxi-to-zona-14-10-2026` (Ensaio 003, etapa 5). Status da lacuna no JSON: não alterado por esta Skill (quem marca é Wallenberg).

---

## 1. Por que esta Skill existe

A Skill `legal-base-legislativa-bairro` diz que a TO máxima vem do Anexo XXI, mas não traz a tabela. Esta Skill traz a tabela de TO por zona e subzona, da AP4 (Recreio, Barra, Vargem Grande) e da AP3, com a página de cada bloco. Ela **complementa** a base; não substitui nenhuma Skill instalada.

A base de SMD (Art. 352, p. 125, registro de 13/10) usa essa TO como teto da área livre. A regra do Art. 352 não foi relida nesta rodada.

## 2. Regra de ouro (não negociável)

1. **TO é por zona E subzona. Código de subzona não é único na cidade.** Antes de aceitar qualquer linha, ler o cabeçalho do bloco de Área de Planejamento (AP3 ou AP4). A subzona "A-ENS" não existe em nenhum bloco deste anexo.
2. **Linha "ver Dec. ..." não tem número aqui.** O número de TO vem do decreto citado (ver seção 4). Nunca preencher a TO de ZPP sem lote e sem subzona confirmada no RIU.
3. **Número de TO sem lote identificado não é parecer.** Sem RIU da subzona real do lote, a TO fica "não confirmada".
4. **Em caso real, a TO vence fonte secundária e vai ao RIU/Certidão da SMDU** (regra de fonte oficial, Princípio 18).

## 3. Tabela — Anexo XXI, Área de Planejamento 4 (pp. 275 a 277)

Leitura visual das páginas renderizadas (ver ressalva 5.1). Cada linha: zona · subzona · TO (%).

| Zona | Subzona | TO (%) | Pág. |
|---|---|---|---|
| ZCA 1 | — | x (sem TO) | 275 |
| ZCA 2 | A | 20 | 275 |
| ZCA 2 | B | 20 | 275 |
| ZCA 2 | C | 40 | 275 |
| ZCA 2 | D | ver Dec. nº 11990/1993 | 275 |
| ZCA 2 | E | 20 | 275 |
| ZCA 2 | F | x | 275 |
| ZCS | A | 50 | 275 |
| ZCS | B | 50 | 275 |
| ZCS | C | ver Dec. nº 38057/2013 | 275 |
| ZCS | D | 70 | 275 |
| ZCS | E | 50 | 275 |
| ZOE | — | x | 275 |
| ZPP | — | ver Dec. nº 3046/1981 | 275 |
| ZRM 1 | A | 50 | 275 |
| ZRM 1 | B | 50 | 275 |
| ZRM 1 | C | 40 | 275 |
| ZRM 1 | D | 40 | 276 |
| ZRM 2 | A | 50 | 276 |
| ZRM 2 | B | 40 | 276 |
| ZRM 2 | C | 50 | 276 |
| ZRM 2 | D | 50 | 276 |
| ZRM 2 | E | 50 | 276 |
| ZRM 2 | F | 50 | 276 |
| ZRM 2 | G | 50 | 276 |
| ZRM 2 | H | 50 (duas linhas: lote 600 m² multifamiliar e 360 m²) | 276 |
| ZRM 2 | I | 40 | 276 |
| ZRM 2 | J | 50 | 276 |
| ZRM 2 | K | 50 | 276 |
| ZRM 2 | L | 60 | 276 |
| ZRM 2 | M | 40 | 276 |
| ZRM 2 | N | 50 | 276 |
| ZRM 2 | O | 40 | 276 |
| ZRM 2 | P | 50 | 276 |
| ZRM 2 | Q | 50 | 276 |
| ZRM 2 | R | 50 | 276 |
| ZRM 2 | S | ver Dec. nº 38057/2013 | 276 |
| ZRM 2 | T | 70 | 276 |
| ZRM 2 (impresso "ZMR 2") | U | 70 | 276 |
| ZRM 3 | A | 50 | 276 |
| ZRM 3 | B | 50 | 276 |
| ZRM 3 | C | 50 | 276 |
| ZRM 3 | D | 50 | 276 |
| ZRM 3 | E | 40 | 276 |
| ZRM 3 | F | 50 | 277 |
| ZRM 3 | G | ver Lei Complementar nº 74/2005 | 277 |
| ZRM 3 | H | 40 | 277 |
| ZRM 3 | I | 40 | 277 |
| ZRM 3 | J | 50 | 277 |
| ZRM 3 | K | 40 | 277 |
| ZRM 3 | L | 50 | 277 |
| ZRM 3 | M | 50 | 277 |
| ZRM 3 | N | ver Dec. nº 35087/2013 | 277 |
| ZRM 3 | O | 70 | 277 |
| ZRU 1 | A | 50 | 277 |
| ZRU 1 | B | 50 | 277 |
| ZRU 1 | C | 50 | 277 |
| ZRU 1 | D | 50 | 277 |
| ZRU 2 | A | 50 | 277 |
| ZRU 2 | B | 50 | 277 |
| ZRU 2 | C | 50 | 277 |
| ZUM | A | 50 | 277 |
| ZUM | B | 50 | 277 |
| ZUM | C | 50 | 277 |
| ZUM | D | 50 | 277 |
| ZUPI | A | 40 | 277 |
| ZUPI | B | 70 | 277 |

**Conferência cruzada:** ZRM 1 subzona B = TO 50 (pág. 275). Bate com o caso Daniel-OB, em que a Prefeitura admite 50% de TO sobre o lote (registro de 12/09/2026). Essa conferência só prova consistência entre duas leituras, não substitui a consulta ao RIU.

## 4. Tabela — Anexo XXI, Área de Planejamento 3 (pp. 274 a 275)

| Zona / setor | Subzona | TO (%) | Pág. |
|---|---|---|---|
| ZFU | — | 70 (CAM 7,0; lote mín. 1.000 m²) | 274 |
| AEIF da Fiocruz — Manguinhos, Setor 1 | — | 20 | 274 |
| AEIF — Setor 2 | — | 50 | 274 |
| AEIF — Setor 3 | — | 10 | 274 |
| AEIF — Setor 4 | — | 30 | 274 |
| AEIF — Setor 5 | — | 30 | 274 |
| AEIF — Setor 6 | — | 60 | 275 |
| AEIF — Setor 7 | — | 40 | 275 |
| AEIF — Setor 8 | — | 50 | 275 |

Nota do próprio anexo para a ZFU: "As edificações não afastadas estão sujeitas aos benefícios da OI da LC nº 229/2021" (p. 274).

**Fora desta Skill nesta rodada:** APs 1 e 2 e qualquer bloco de AP5 ou superior não foram lidos. Não usar esta tabela para essas APs.

## 5. Ressalvas (por que o status é "ativa-com-ressalva")

1. **Método de leitura.** Os valores foram lidos nas páginas renderizadas como imagem (ferramenta de leitura do PDF). A extração de texto do PDF não foi feita nesta rodada. Antes de citar um valor em parecer para cliente ou para a prefeitura, conferir a célula pela camada de texto (`pdftotext`, POP-LEGAL-06). Valores de TO com 2 dígitos são os de maior risco de leitura errada.
2. **Linha "ZRM 2 U".** No original impresso, aparece "ZMR 2" (grafia que não bate com o padrão do bloco). Tratada aqui como ZRM 2 U. Conferir no texto.
3. **Decretos e leis citados nas células "ver".** Os números estão como impressos no anexo (11990/1993, 38057/2013, 35087/2013, LC 74/2005). Não verificados contra o diploma próprio. Se o número for usado em caso real, buscar o diploma.
4. **Linhas com "x"** = o anexo não fixa TO para a zona. Não significa TO zero nem TO livre. Quando x aparecer, a TO vem de outra norma (checar a Skill da zona antes de usar).
5. **Mérito da TO na subzona real** (Cap. III do Dec. 3.046 e exceções por subzona) não está aqui. Ver seção 6.

## 6. Relação com as outras Skills

| Skill | Relação | O que faz com esta |
|---|---|---|
| `legal-base-legislativa-bairro` | **Complementa** | Aponta o Anexo XXI como fonte da TO. Esta Skill traz a tabela. Nenhuma edição nela nesta rodada. |
| `decreto3046-81-lc270-2024-licin-barra-recreio` | **Complementa** | Para a linha ZPP ("ver Dec. 3046/1981") e para a ZE-5, a TO por subzona está no decreto (ex.: A-1 uso uni/multi 50%; A-3 uni 40%). Esta Skill não dá número de ZPP. |
| `legal-oodc-mais-valera-mais-valia` | Sem sobreposição com a TO | Não usa esta tabela. |
| `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj` | Sem sobreposição | TO de garagem é outra regra (COES Art. 350 III). |

**Verificação de coerência (15/10/2026):** Grep em `.claude\skills\` por "Anexo XXI" e "taxa de ocupação" achou 9 arquivos. Nenhum deles traz TO numérica de AP4 que contradiga a tabela. As menções a "TO 40%" na Skill decreto3046 são exemplo de uma subzona genérica e estão marcadas como não usáveis sem RIU.

## 7. Como usar (passo a passo, para Hely e Kelsen)

1. Confirmar pelo RIU a AP, a zona e a subzona do lote. Não aceitar subzona de terceiro sem RIU.
2. Ler o cabeçalho do bloco da AP no Anexo XXI.
3. Achar a linha da zona + subzona na tabela desta Skill.
4. Se a célula for "ver Dec." ou "ver LC", abrir o diploma citado e achar a subzona nele. Não inferir.
5. Se a célula for "x", buscar a norma que fixa a TO da zona. Não tratar como zero.
6. Registrar: zona, subzona, TO, página do PDF e se a conferência foi por texto ou por imagem.

## 8. Erros a evitar

- Usar "A-ENS" como subzona. Ela não existe no anexo (aparece só no caso fictício do Ensaio 003).
- Usar a TO privada da convenção (ex.: 40% de convenção de condomínio) no lugar da TO municipal.
- Ler a TO de uma AP vizinha porque a subzona tem a mesma letra.
- Tratar "x" ou "ver Dec." como TO livre ou como 50% padrão.

## 9. Changelog

- **v1.0 (15/10/2026):** primeira versão. Leitura de AP4 (pp. 275 a 277) e AP3 (pp. 274 a 275) por imagem do PDF. Status ativa-com-ressalva. Criada por Kelsen (rotina autônoma, Drenagem/Skills).
