---
name: skill-proposta-fechamento-habite-se-aceitacao
description: "PROPOSTA — fluxo oficial de Habite-se/Aceitação de Obra dentro do LICIN 2.0 (Decreto 55.622/2025), com os artigos que regem reporte de fases da obra e vistoria final; relevante para o futuro Gestor Fechamento"
metadata:
  type: skill_proposta
  status: proposta_pendente_reuniao_mensal
  gestor_alvo: Gestor Fechamento — não implantado
  data: 2026-07-23
---

# Skill proposta: Habite-se e Aceitação de Obra — fluxo dentro do LICIN 2.0

## Para quem é
**Gestor Fechamento**, ainda não implantado — segunda proposta de Skill dirigida a esse Gestor (a primeira foi orçamento executivo por IA, 19/07/2026). Cobre o outro lado do trabalho de Fechamento: não só o custo, mas o **encerramento administrativo** que precede o Gate 16 (Liberação de Obra). O Gate 16 em si (dupla aprovação Claudemberg + Gestor) não muda — esta Skill é sobre o que precisa estar pronto **antes** dele chegar lá.

## O que ensina/entrega — é mapa, não cópia de parâmetro
Regra já fixada para toda Skill do organismo desde 20/07/2026 (ver `legal-base-legislativa-bairro`): esta Skill aponta onde está o artigo e como confirmar, não trava o texto legal como verdade permanente. Confirmar sempre no status jurídico da Busca Fácil (SMU) antes de citar em peça real, mesma disciplina do Legal.

1. **A obra precisa ser reportada em 4 marcos, não só no fim.** O Decreto 55.622/2025 (LICIN 2.0), **Art. 5º**, obriga o requerente a informar dentro do próprio processo: (a) data de início da obra, (b) conclusão das fundações, (c) conclusão da primeira laje, e (d) conclusão da obra. Achado relevante para o organismo: se o Agente de Fechamento (quando existir) só entrar em cena no fim da obra, ele chega tarde — o processo espera reporte progressivo desde o início. Isso é possivelmente uma pendência que caberia ao Agente de Arquitetura/Coordenação acompanhar ao longo da obra, não só o Fechamento — decisão de desenho de fluxo para quando os dois Gestores existirem.
2. **A vistoria de Habite-se/Aceitação confere contra o que foi aprovado, não contra o que foi construído em si.** **Art. 8º** do mesmo decreto: a vistoria para concessão de habite-se ou aceitação verifica o atendimento aos itens listados no **Art. 3º** (dimensões do lote, gabarito, afastamentos, etc.) **por comparação com o(s) projeto(s) aprovado(s)**. Ou seja: qualquer divergência de obra-x-projeto aprovado é o que trava o Habite-se — reforça por que o organismo já trata "prancha compilada = fonte de verdade" como central (ver teste de capacidade de 21/07, prancha PDF).
3. **Documentos exigidos no fechamento: DULI + 3 declarações de conformidade.** **Art. 6º e parágrafo único**: Documento Único de Licenciamento Integrado (DULI, já emitido no início do processo) mais declarações de conformidade do PRPA (profissional responsável pelo projeto — Claudemberg, no padrão residencial), do PREO (profissional responsável pela execução — normalmente o construtor/mestre de obras, não necessariamente a Sttickler) e do requerente, nos modelos dos Anexos I e II do decreto.
4. **Existem dois desfechos distintos, não um só:** **Habite-se** (obra nova, com criação de unidade) vs. **Aceitação de Obra** (modificação/reforma sem criação de unidade nova). O organismo já registra essa distinção para demolição (ver [[sttickler_licin_demolicao_ics_rj]]) — o mesmo par se aplica aqui e deve usar a mesma nomenclatura, para não confundir com "conclusão de obra" genérica.
5. **Existe uma ferramenta pública de consulta pronta, sem precisar pedir nada à prefeitura.** `certidoessmdeis.rio.gov.br` permite consultar o status de Habite-se/Aceitação de qualquer imóvel do Rio por número de certidão, número de processo ou endereço — útil tanto para due diligence de terreno (antes do início) quanto para conferir se o próprio processo do cliente já foi concluído, sem abrir chamado. Mesma lógica de "ferramenta oficial sem clique" já validada para o RIU (ver [[sttickler_riu_api_oficial]]) — vale checar depois se esse portal tem endpoint público equivalente, ou se é só formulário de tela.

## O que esta Skill deliberadamente não cobre
- **Prazo para solicitar Habite-se após a conclusão:** o decreto consultado não trouxe prazo explícito — não inventar um. Se isso for crítico para o fluxo de Fechamento, confirmar diretamente com SMDU/Busca Fácil quando o Gestor for criado, não assumir "imediato" nem copiar prazo de outro município.
- **Valor de taxas (DARM) do fechamento** — muda com frequência, não é parâmetro de Skill (mesmo tratamento dado a CUB/SINAPI em 19/07 e anuidade CAU em 20/07).
- **O processo de obra em si (execução, mestre de obras, PREO)** — fora do escopo de Construção do Zero enquanto produto Sttickler; a Skill cobre só o encerramento administrativo que toca o organismo.

## Fontes e confiabilidade
- **Decreto 55.622/2025 (LICIN 2.0), Arts. 3º, 5º, 6º e 8º** — texto consultado via agregador LegisWeb (`legisweb.com.br`, id 471595), não a fonte primária da Prefeitura. **Confiança média** — mesma ressalva já registrada para agregadores desde 19-20/07 (Diário Oficial/Portal Carioca Digital bloquearam fetch direto, HTTP 403, mesmo padrão do Decreto 45.917/2019 já pendente). Confirmar os artigos no PDF oficial do decreto antes de qualquer uso real em peça de cliente.
- Portal Carioca Digital — página "Certidão de Habite-se/Aceitação" (`carioca.rio/servicos/consultar-certidao-de-habite-se-aceitacao`) e página "Licença para construção, modificação, LICIN e prorrogação de obras" — confirmam o portal de consulta e a existência das duas modalidades (habite-se vs. aceitação).
- Pesquisado em 23/07/2026, rotina diária do Wallenberg.

## Ação proposta
Quando o Gestor Fechamento for criado: (a) desenhar o ponto de entrada do Agente de Fechamento no fluxo considerando que o LICIN 2.0 espera reporte progressivo desde o início da obra, não só no fim; (b) usar `certidoessmdeis.rio.gov.br` como primeira checagem de status antes de qualquer contato com a prefeitura; (c) tratar Habite-se e Aceitação como dois rótulos distintos, nunca intercambiáveis, no material que o Agente produzir.

## Governança
Proposta pendente — não cria o Gestor Fechamento nem qualquer Agente (decisão estrutural, fora do escopo desta rotina). Fica arquivada para quando Claudemberg decidir avançar a construção desse Gestor (Princípio 13).
