# Aplicação dos 6 achados médios do Bardi (reconferência 31/10, nota 8,25), 02/11/2026

- **Ordem:** Claudemberg ("Sim, corrigir"), via Lúcio. Frente: Construção do Zero.
- **Fonte dos achados:** `Agentes_Diretos\Bardi (Examinador)\parecer_briefing_unico_v2_reconferencia_31-10.md`, seção 3, M1 a M6 (lido inteiro nesta execução, 129 linhas).
- **Arquivo editado:** `briefing_modelo_v2_proposta.md` (lido inteiro antes de editar, 406 linhas; só Edit em trechos). Também `briefing_modelo_v2_diferencas.md` (seção nova "Ajustes médios da reconferência do Bardi").
- **Não tocado:** Ensaio 003, Drive, Revit. Sem commit.
- As linhas abaixo são as da proposta **depois** das edições (o cabeçalho cresceu 6 linhas, por isso as linhas do Bardi andaram).

## M1. INT-04 com duas origens na D-2

- **O que mudou:** a INT-04 saiu da lista "usam os cômodos da PRG-01". Ficou uma origem só, a INT-01, igual à linha da INT-04 (L176: "os cômodos do INT-01").
- **Linha:** L397 (era L388).
- **Antes:** "CLI-01, INT-01 e INT-04 usam os cômodos da PRG-01 [...]; a INT-02 e a INT-04 usam os cômodos marcados na INT-01"
- **Depois:** "CLI-01 e INT-01 usam os cômodos da PRG-01 [...]; a INT-02 e a INT-04 usam só os cômodos marcados na INT-01"

## M2. MOR-01 em texto livre

- **O que mudou:** a MOR-01 virou grade, uma linha por pessoa, com parentesco (texto curto, sem nome), faixa de idade (0 a 11 / 12 a 17 / 18 a 59 / 60 anos ou mais) e "mora na casa: sempre / às vezes". A 1ª linha é "eu, quem responde". O texto ao cliente pede para não escrever nome nem data de nascimento (LGPD). As condições que dependiam dela passaram a usar a faixa de idade.
- **Linhas e trechos:**

| Linha | Antes | Depois |
|---|---|---|
| L76 MOR-01 | "Para cada pessoa: parentesco e idade." / "TXT (uma linha por pessoa)" | "Não escrevam nome nem data de nascimento." / "GR (uma linha por pessoa [...]): parentesco [...]; faixa de idade [...]; mora na casa → sempre / às vezes" |
| L77 RES-01 | "alguém com menos de 18 anos ou outro adulto além de quem responde" | "1ª caixa: [...] faixa "0 a 11 anos" ou "12 a 17 anos". 2ª caixa: [...] além da 1ª (quem responde) [...] "18 a 59 anos" ou "60 anos ou mais"" |
| L79 MOR-02 | "quem (só o parentesco da MOR-01 [...])"; "Sobre criança, só com a 1ª caixa da RES-01 marcada" | "escolher uma ou mais pessoas da lista da MOR-01, que mostra só o parentesco e a faixa de idade"; nota interna: as faixas 0 a 11 e 12 a 17 só aparecem com a 1ª caixa |
| L89 texto da RES-01 | "informei o parentesco e a idade deles" | "informei o parentesco e a faixa de idade deles" |
| L91 regra da RES-01 | "a MOR-02 não pode ser respondida sobre a criança" | "[...] sobre as pessoas da MOR-01 com faixa "0 a 11 anos" ou "12 a 17 anos"" |
| L104 regra da CON-01 | "por pessoa de 60 anos ou mais na MOR-01" | "por pessoa com a faixa "60 anos ou mais" na MOR-01" |
| L279 C-2 | "MOR-01 com pessoa de 60 anos ou mais" | "MOR-01 com alguma linha na faixa "60 anos ou mais"" |
| L321 C-12 | "MOR-01 com criança" | "MOR-01 com alguma linha na faixa "0 a 11 anos" (criança; [...] de acordo do Glaziou pendente)" |
| L398 D-2 | (não havia) | "Condições sobre a MOR-01": a grade e qual faixa abre ou dispara o quê |

- **Duas escolhas minhas que ficam para Lúcio confirmar:**
  1. As condições valem para "sempre" e "às vezes" (lado seguro). Marquei na L76: "[A CONFERIR: Lúcio, se "às vezes" deve disparar a C5 e a C-12]".
  2. Na C-12, "criança" virou a faixa 0 a 11. Adolescente (12 a 17) não dispara a proteção de planta tóxica e espinho. A C-12 tinha de acordo do Glaziou; essa leitura precisa de novo de acordo dele, via Cardozo (marcado na L321).
- **Não feito (fora da ordem de Lúcio):** o M2 também diz que a D-2 não cita a PRG-02 nem a AUT-02. Não acrescentei: a lista de cômodos da AUT-02 não está escrita em lugar nenhum, e eu teria de inventar a origem.

## M3. Códigos e notas internas no texto ao cliente

- **O que mudou:** nas 5 linhas, a nota saiu da coluna Pergunta ou Tipo / opções e foi para a coluna Condição, com o rótulo "Nota interna:". Nenhuma nota foi apagada. A legenda (L43) e a D-1 (L384, campo novo "Nota interna") dizem que o cliente não vê essas notas. A legenda também marca como internas as marcas de origem "(opções do F2)", "(opções do FORM-INT)" e as regras "(esta opção só aparece se...)", que estão em outras linhas.

| Linha | Antes (coluna do cliente) | Depois |
|---|---|---|
| L52 CAS-01 | "Vem marcada do Pré-Briefing [...] são as linhas 1 e 6 da TER-01" nas opções | opções só com as escolhas; "Nota interna: vem marcada do Pré-Briefing [...] são as linhas 1 e 6 da TER-01" na Condição |
| L83 ROT-02 | "o pet (se houver, PET-01)" | "o pet"; Condição: "Nota interna: a opção "o pet" se cruza com a PET-01 (se houver pet)" |
| L165 HID-03 | "(O sol já foi perguntado em SUS-01; o reservatório de água quente é escolha da equipe)" | Condição: "Nota interna: o sol já foi perguntado na SUS-01; o reservatório [...]" |
| L167 ELE-02 | "O que a casa precisa ter preparado? (câmeras e alarme já estão em SEG-01)" | "O que a casa precisa ter preparado?"; Condição: "Nota interna: câmeras e alarme já estão na SEG-01" |
| L171 AUT-02 | "Itens de SEG-01 e a irrigação do ESC-02 entram sozinhos na automação" nas opções | Condição: "Nota interna: os itens da SEG-01 e a irrigação do ESC-02 entram sozinhos na automação" |

## M4. Cabeçalho dizia APROVADO

- **Linhas:** L3 a L9 (era L3); L10, última frase (era L4).
- **Antes (L3):** "**APROVADO por Claudemberg em 31/10/2026** [...] Pendências abertas: medir o tempo na 1ª aplicação."
- **Depois (L3):** "**ESTADO EM 02/11/2026 — NÃO USAR COM CLIENTE REAL.**", seguido de: conteúdo aprovado por Claudemberg em 31/10; correções de 31/10 aplicadas; reconferência do Bardi 8,25; os 6 ajustes médios aplicados em 02/11; pendências que impedem o uso: PRV-01 (razão social, CNPJ, e-mail, prazo de guarda), Res. CD/ANPD nº 2/2022, Art. 33 para a IA, NBR 15575-1:2025.
- **Antes (L4, fim):** "Precisa de nova conferência do Bardi (nota mínima 8,00) antes de qualquer uso."
- **Depois (L10, fim):** "Nova conferência do Bardi feita em 31/10 (nota 8,25; ver o estado acima)."
- **Tirado do cabeçalho:** a frase do Hely sobre a NBR 15575-1 item 16.2 e as 2 interpretações do Kelsen. Elas continuam no histórico (C-7 e diferenças); o cabeçalho ficou só com o estado.

## M5. Sondagem sem Estrutural contratado

- **O que mudou:** aplicada a regra geral da Parte B (disciplina não contratada fica com o Oscar, só o fato de campo).

| Linha | Antes | Depois |
|---|---|---|
| L219 regra geral | "Exemplos já escritos: TI-02, TI-13, [...]" | "Exemplos já escritos: TI-01 (sondagem sem Estrutural, 02/11), TI-02, TI-13, [...]" |
| L223 TI-01 | só "O Baumgart define quantos furos [...]" | acrescido: "Sem Estrutural contratado [...]: o Oscar orienta o cliente a contratar uma empresa de sondagem, que define os furos pela norma, e registra o laudo [...]. O Oscar não dimensiona nada"; coluna Dono separa "Com Estrutural" e "Sem Estrutural" |
| L299 C-3 Gate | "TI-01, TI-05, TI-09 e TI-14 anexadas;" | "[...] anexadas (na TI-01, sem Estrutural contratado, vale o laudo da empresa de sondagem);" |

- Não citei o número da norma de sondagem na regra nova: a NBR 8036 e a NBR 6484:2020 não foram abertas nesta execução.

## M6. Pé-direito de 2,50 m e 2,30 m no texto ao cliente

- **O que mudou:** os números ficaram no texto ao cliente (decisão de Claudemberg). Entrou uma nota interna visível logo abaixo do texto da Seção 3.
- **Linha:** L129 (nova).
- **Antes:** (nada depois do texto ao cliente; o aviso só existia na C-7)
- **Depois:** "Nota interna (o cliente não vê; 02/11, achado M6 do Bardi): **[A CONFERIR: números da NBR 15575-1:2024; confirmar na edição 2025 antes do 1º cliente real]**."

## Números (recontados por Grep em 02/11)

- Nenhuma linha de código foi criada ou retirada. Continua: 63 códigos ativos; até 45 / 56 / 62; 24 tarefas internas (TI-01 a TI-14 nas L223–L236, TI-PAI nas L244–L249, TI-EST nas L255–L256, TI-ELE nas L262–L263); regras C-1 a C-17 (L273 a L369) + Parte D.
- Tempo: sem mudança (MOR-01 mantida em 2 min, estimativa).
- A tabela "Números" da proposta não mudou. O `briefing_modelo_v2_diferencas.md` ganhou a seção "Ajustes médios da reconferência do Bardi (02/11/2026)".

## O que fica para Lúcio

1. Confirmar "às vezes" nas condições da MOR-01 (L76).
2. Pedir ao Glaziou, via Cardozo, o de acordo com "criança = 0 a 11" na C-12 (L321).
3. Origem da lista de cômodos da AUT-02 e da PRG-02 na D-2 (resto do M2, não aplicado).
4. Os 7 achados baixos (B1 a B7) não foram pedidos nesta ordem.
