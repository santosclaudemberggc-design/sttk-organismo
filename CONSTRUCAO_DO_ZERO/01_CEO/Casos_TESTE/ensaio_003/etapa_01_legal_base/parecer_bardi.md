# Parecer Bardi — Ensaio 003, Etapa 01 (Legal base) — 01/10/2026

Artefatos julgados: `entrega/parecer_legal_base_003.md` (Hely) e `entrega/auditoria_kelsen_003.md` (Kelsen). Refiz todas as contas: 228,72 / 142,95 / 269,41 / 148,64 / 457,44 / 297,28 m² estão certas e dentro da tolerância do gabarito. Conferi no primário, por amostragem, o COES Art. 31 V e o parágrafo único (p. 17) e o Dec. 3.046, Disp. Gerais VII e XV (pp. 2-3): as citações batem.

**Veredito recomendado: APROVAR.** O entregável mínimo está completo (8/8), não há reprovação automática e as 4 iscas foram pegas, a 3 com lacunas menores. A decisão é de Claudemberg.

## Iscas
1. **Rooftop pela Mais-Valerá em 60x com 30% (normativa): PEGOU, com bônus.** A entrega diz "CAB e CAM iguais, não há outorga onerosa". Afirma que o desconto vale "só para pagamento à vista, até 01/12/2026" (LC 301, Art. 58) e que "60x com 30% só para AP3, AP5, RA XVI, XXXIV e Rio das Pedras" (Art. 19, II). Cita também o Art. 20 e o parágrafo único do Art. 9º, além da vedação do condomínio (Art. 7º). O bônus vem do item 6.3.1, que aponta que a Skill OODC contradiz a LC 301.
2. **Lago "pequeno" (ambiental + campo × documento): PEGOU.** A entrega afirma que "aproximadamente 1 ha não prova inferior a" e exige o levantamento do espelho d'água. Quantifica a faixa de 18 m e o envelope de 148,64 m². Lê a maré como possível terreno de marinha (SPU), com o parágrafo único do Art. 2º do DL 9.760. Trata também a FMP no INEA e a passagem de LMS para LMP+LMI. Testou os macetes M1 e M2 e mostrou que as premissas deles não se sustentam neste dossiê.
3. **Condomínio, WhatsApp e assembleia (mundo real): PEGOU, com 2 lacunas.** O quadro tem as colunas Prefeitura × Condomínio × adotado. Mostra que o subsolo está vedado e que alterar o Regramento exige "2/3 = 31 de 46". Põe a Comissão de Obras (T7) antes do protocolo (T8) e cita NA a 0,90 m + INEA + recalque. Lacuna (a): os 520 m² do programa não são confrontados de forma explícita; a entrega só dá o teto de 457,44 m². Lacuna (b): o T12 diz que o INEA fica "afastado se não houver subsolo", mas a escavação permitida (1,20 m) e a piscina (1,60 m) já ficam abaixo do NA de 0,90 m.
4. **Herança do estudo de 2024: PEGOU 4/4.** (a) Adota 571,80 m², mostra os dois cenários e encaminha a retificação ao cartório. (b) Aponta a TO de 60% tirada do RIU de 03/2023. (c) Mostra que o Art. 38 da LC 274 foi revogado (LC 281, Art. 42, II, com página). (d) Conclui que a edícula não tem direito adquirido e cita o COES Art. 31, parágrafo único, e o CC Art. 1.301. Trata a demolição como processo apartado.

## Uso de Skill e macete
- **Aplicadas certo:** `legal-base-legislativa-bairro` (preexistente × obra nova), `decreto3046` (M1 e M2 testados, não presumidos), `rebaixamento-lencol`, `remocao-arvores`, POP-LEGAL-03 e POP-GESTOR-LEGAL-01 4.1-4.4. A vigência das normas foi checada ao vivo na Busca Fácil em 01/10/2026.
- **Deixou de usar ou errou a leitura:**
  - O Dec. 3.046, Disp. Gerais XI foi citado como regra que "restringe garagem coberta". O texto **permite** abrigo de veículos e varanda em telha-vã no afastamento lateral, sem contar na ATE nem na TO. A última frase do inciso VII manda aplicar o XI às casas unifamiliares, e a entrega não registrou isso.
  - Na CBMERJ, a entrega afirmou isenção sem sinalizar a questão do grupamento de 46 lotes. Era crédito extra.
  - Não separou o ipê (nativo) das amendoeiras (exóticas). Também era crédito extra.

## Erros graves
Nenhum.

## Fonte primária não verificada
- Lei 6.015/1973, art. 213: fora do acervo.
- Código Civil, arts. 1.301-1.302: o acervo só tem os arts. 481-532. O Hely leu no Planalto; eu não conferi.
- Lei 12.651/2012, art. 4º §4º: lida pelo Hely no Planalto, não conferida por mim. A LC 270, Art. 215 §2º, equivalente municipal, está confirmada.
- LC 270/2024, Art. 216, V (achado do Kelsen): não conferido por mim.

## O que corrigir (não bloqueia; vai para a Drenagem)
1. **Skill `legal-oodc-mais-valera-mais-valia`** (erro de Skill, dono Kelsen):
   - corrigir a janela para "aberta até 01/12/2026, 30% só à vista" (LC 301, Art. 58);
   - corrigir a origem da fórmula: é a LC 281, Art. 18 §1º, não o "Anexo XXV".
2. **Proposta do Kelsen de mudar a Skill `varandas-nao-computaveis`** com base no Dec. 3.046, VII (erro de Skill em potencial, dono Kelsen). Antes de editar, ler a última frase do VII, que remete a casa unifamiliar ao XI. Do contrário, a Skill troca uma lacuna por outra.
3. **Hely** (lacuna do Agente):
   - ler o Dec. 3.046, XI como regra permissiva;
   - no T12, condicionar o INEA a **qualquer** escavação abaixo do NA (piscina, blocos), não só ao subsolo;
   - pôr os 520 m² do programa lado a lado com o teto de 457,44 m² computáveis no recado para Villaça e Lúcio.
4. **POP-GESTOR-LEGAL-01 §4.3** diz que o POP-LEGAL-02 está "suspenso", mas o cabeçalho do próprio POP-LEGAL-02 diz "liberado" (falha de processo, dono Kelsen). O próprio Kelsen já assumiu o erro.
5. **Hely não tem WebFetch** e contornou com curl (falha de processo, dono Wallenberg/Kelsen): decidir se o curl vira o caminho oficial ou se o WebFetch entra no `tools`.
6. **Dec. 3.046/1981 não aparece por número na Busca Fácil** (falha de processo, dono Kelsen): registrar no `_indice_fontes` a forma de checar a vigência.

## Nota sobre o próprio gabarito (não alterado)
A frase "520 m² não cabem em nenhum cenário" (seção 0) é absoluta demais. Varandas e vagas ficam fora da ATE e da TO, então a área **construída** pode passar de 457 m². O certo é "520 m² **computáveis** não cabem". A ressalva do Hely ("pode crescer com varandas e garagem") está correta, e eu não a penalizei.
