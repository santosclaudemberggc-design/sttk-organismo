---
name: feedback_memoria_continua_nao_zerada
description: O arquivo de estado de cada agente não é "renascer do zero" — é aprendizado contínuo; o agente sempre começa entendendo o que já fez e aprendendo com os próprios erros
metadata:
  type: feedback
---

Correção de Claudemberg em 20/07/2026, durante o detalhamento do Lúcio (Gestor Arquitetura): **"em sua memória ele aprende com os erros e com tudo que já fez, ele sempre começa com o entendimento do que já fez, nunca começa com memória zero."**

**Por quê:** o mecanismo de arquivo de estado (ver [[sttickler_arquivo_estado_agentes]]) já existia com uma seção "aprendizados que não posso esquecer" — mas a linguagem usada pra descrever o mecanismo em `kelsen.md`/`hely.md` ("Você nasce zerado a cada acionamento") enfatiza errado o que importa. O ponto não é "começar do zero e só ter um bilhete curto" — é o oposto: **o agente sempre carrega o entendimento acumulado de tudo que já fez, erros incluídos**, e é isso que o arquivo de estado deve garantir na prática, não só a mecânica técnica de "sessão nova, contexto vazio".

**Como aplicar:** ao escrever a seção de arquivo de estado de qualquer Gestor/Agente novo (Lúcio e sua equipe, e futuros), enquadrar como "você sempre começa lendo o que já fez e aprendeu — nunca memória zero", não como "nasce zerado". Isso muda ênfase, não mecânica (o arquivo continua sendo a única ponte entre uma execução e outra, tecnicamente). Sinalizar a Claudemberg se ele quiser que a redação já existente em `kelsen.md`/`hely.md` ("nasce zerado") seja ajustada pra esse mesmo enquadramento, já que foi escrita antes dessa correção.
