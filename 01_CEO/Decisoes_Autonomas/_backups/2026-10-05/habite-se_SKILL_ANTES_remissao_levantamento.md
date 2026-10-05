---
name: habite-se-aceitacao-licin
description: Fluxo de Habite-se e Aceitação de Obra dentro do LICIN 2.0 (Decreto 55.622/2025) — reporte de fases da obra, vistoria final, documentos exigidos, e a ferramenta pública de consulta de status. Use sempre que o futuro Agente de Fechamento precisar orientar sobre encerramento administrativo de obra, checar se um Habite-se pode ser obtido, ou distinguir Habite-se de Aceitação de Obra — mesmo que o pedido só mencione "conclusão de obra", "vistoria final" ou "posse", sem citar a norma pelo nome.
---

# Habite-se e Aceitação de Obra — Fluxo dentro do LICIN 2.0

Skill de Inteligência Técnica da área Fechamento (Gestor ainda não implantado). É mapa, não cópia de parâmetro — regra geral de toda Skill do organismo (ver `legal-base-legislativa-bairro`): confirme sempre o status jurídico na Busca Fácil (SMU) antes de citar em peça real.

## 1. A obra precisa ser reportada em 4 marcos, não só no fim

O Decreto 55.622/2025 (LICIN 2.0), **Art. 5º**, obriga o requerente a informar dentro do próprio processo: (a) data de início da obra, (b) conclusão das fundações, (c) conclusão da primeira laje, (d) conclusão da obra. Se o Agente de Fechamento só entrar em cena no fim da obra, chega tarde — o processo espera reporte progressivo desde o início. Pode caber ao Agente de Arquitetura/Coordenação acompanhar isso ao longo da obra, não só o Fechamento — decisão de desenho de fluxo pendente para quando os dois Gestores existirem.

## 2. A vistoria confere contra o PROJETO aprovado, não contra a obra em si

**Art. 8º:** a vistoria para Habite-se/Aceitação verifica atendimento aos itens do **Art. 3º** (dimensões do lote, gabarito, afastamentos etc.) **por comparação com o projeto aprovado**. Qualquer divergência obra-x-projeto é o que trava o Habite-se — reforça que a prancha compilada é a fonte de verdade, não a obra construída em si.

## 3. Documentos: o que o decreto exige e em qual momento *(corrigido em 01/10/2026 por Kelsen, no PDF oficial)*

- **No requerimento da licença (Art. 6º e parágrafo único):** o DULI vem acompanhado de documento em que o PRPA, o PREO e o requerente declaram que atendem ao Plano Diretor, à LUOS, ao COES e às demais normas (modelo no **Anexo II**). Isso é do **início** do processo, e não do Habite-se. A v1.0 desta Skill tratava essas declarações como documento do Habite-se, o que estava errado.
- **Antes de começar a obra (Art. 4º §4º):** declaração do PRPA, do PREO e do requerente de que as liberações dos órgãos consultados correspondem ao projeto licenciado (**Anexo V**). Se a licença saiu antes das anuências, ela vale **3 meses** e é prorrogável ou revalidável enquanto a obra não começa (§2º).
- **Para o Habite-se ou a Aceitação (Art. 8º):** o decreto só exige a **vistoria** dos itens do Art. 3º, os 13 incisos: dimensões do lote, alinhamento, cota de soleira, TO, superfície drenante, ATE, gabarito, afastamentos, profundidade, área coletiva, uso e tipologia, nº de unidades e ICS. **Não lista documento próprio.** Se a SMDU pedir algo a mais, é exigência do caso; confirmar na hora e não presumir.

## 4. Dois desfechos distintos — não confundir

**Habite-se** (obra nova, com criação de unidade) vs. **Aceitação de Obra** (modificação/reforma sem criação de unidade nova) — mesma distinção já aplicada para demolição. Usar sempre a nomenclatura correta, nunca "conclusão de obra" genérica. *(Nota de 01/10/2026: o Art. 8º só nomeia os dois desfechos. O critério "unidade nova x modificação" é prática da casa e **não está escrito no decreto**. Não citar o Art. 8º como fonte desse critério.)*

## 5. Ferramenta de consulta pública, sem chamado

`certidoessmdeis.rio.gov.br` — consulta status de Habite-se/Aceitação de qualquer imóvel do Rio por número de certidão, processo ou endereço. Útil para due diligence de terreno e para conferir se o processo do cliente já concluiu.

## O que esta Skill NÃO cobre
- Prazo para solicitar Habite-se após conclusão — o decreto não traz prazo explícito, não inventar um. Confirmar direto com SMDU/Busca Fácil se crítico.
- Valor de taxas (DARM) — muda com frequência, não é parâmetro de Skill.
- O processo de obra em si (execução, mestre de obras, PREO) — fora do escopo de Construção do Zero da Sttickler.

## Fontes e confiabilidade
- Decreto 55.622/2025, Arts. 3º, 4º, 5º, 6º e 8º: **conferidos no PDF oficial da base** (`Fontes_Legislacao/Decreto55622_2025_LICIN2.0.pdf`, pp. 2-3) por Kelsen em 01/10/2026. **Confiança alta** para o texto. O §3 foi corrigido nessa conferência. A v1.0 usava o agregador LegisWeb, com confiança média. Continua valendo checar a vigência na Busca Fácil no dia do uso. Backup do antes: `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/kelsen_ANTES_habite-se-aceitacao-licin_SKILL_instalada.md`.
- Portal Carioca Digital — página de Certidão de Habite-se/Aceitação

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Wallenberg para formalizar, especialmente antes de o Gestor Fechamento ser criado.
