---
protocolo: PROTOCOLO-DOC-01
titulo: Checagem obrigatória de dado real de cliente antes de editar documento-base/template
autor: Wallenberg (CEO)
criado: 2026-08-08
status: RASCUNHO — para discussão na Reunião Semanal de 10/08/2026
origem: Precedente real de 03/08/2026 — o formulário "VALIDAÇÃO DA COORDENAÇÃO - Estudo Preliminar" parecia template puro e tinha 1 resposta real já registrada (caso Daniel Vivone Soares Miranda); só não virou incidente porque foi parado e escalado a tempo, com autorização explícita de Claudemberg ("só rótulo, nunca a resposta").
principios: 18 (Ética e conformidade), 15 (Redundância zero — não repetir o mesmo risco em cada Gestor)
---

# Protocolo — dado real de cliente em documento que parece template

## 1. Por que existe
Documentos que a organização trata como "base"/"template" (formulários, planilhas de controle, modelos de memorial) às vezes **já têm uso real registrado dentro deles** — resposta de formulário, linha preenchida com nome de cliente. Editar rótulo/estrutura sem checar isso primeiro arrisca alterar ou obscurecer dado real, mesmo sem intenção. Isso é fronteira (documento de cliente), não uma questão de estilo.

## 2. Regra
**Antes de qualquer Gestor ou Wallenberg editar um documento classificado como "base"/"template"/"padrão", checar se ele tem uso real registrado:**

- **Google Forms:** existe aba/planilha de respostas vinculada com >0 linha? (checar via metadata ou abrindo a planilha de respostas, não só o formulário)
- **Google Docs/Sheets "modelo":** o conteúdo tem nome de cliente, endereço, número de processo, ou qualquer dado específico de caso, em vez de placeholder genérico (`[NOME DO CLIENTE]`, `[ENDEREÇO]`)?
- **Arquivo compartilhado entre departamentos** (ex.: planilha de entregáveis usada por Legal + Arquitetura + Estrutural): mesmo sem dado de cliente, edição não é unilateral — ver `PADRAO-DOC-POP_google-docs.md`, seção 3.

## 3. Se encontrar dado real
1. **Parar a edição imediatamente** — não continuar "só nas outras partes" sem decidir isso primeiro.
2. **Sinalizar para Wallenberg** com o achado exato (qual documento, qual campo/linha, que dado).
3. **Wallenberg não decide sozinho** — mesma fronteira de "documento de cliente" da rotina de drenagem: sinaliza para Claudemberg antes de qualquer edição, mesmo que seja só o rótulo da pergunta/coluna, não a resposta em si.
4. Só depois de autorização explícita ("editar só rótulo, nunca a resposta", precedente de 03/08/2026), a edição prossegue — e mesmo assim, só na parte de estrutura/rótulo, nunca no conteúdo da resposta já registrada.
5. Registrar o caso e a decisão em `pendencias.json` e no livro-razão, mesmo que a decisão seja "não editar por enquanto".

## 4. Se não encontrar dado real (documento é template puro)
Segue o fluxo normal do `PADRAO-DOC-POP_google-docs.md` — Gestor da área ajusta ao padrão, sem necessidade de escalar.

## 5. Lacunas conhecidas
- Não há hoje um jeito automatizado de checar "tem resposta registrada" para todos os tipos de documento de uma vez — é checagem manual, por tipo, até surgir um jeito melhor.
- Este protocolo cobre o momento de edição. Não resolve o problema mais amplo de "que documentos hoje já misturam template e caso real sem ninguém saber" — isso é o que o `PLANO-AUDITORIA-DOCUMENTOS_2026-08.md` propõe mapear primeiro.
