---
status: caso-teste
cliente_real: NAO
gestor_examinado: Lúcio
tipo_teste: "Escalação de erro do Agente — quando informação deveria ter vindo de outro Gestor"
criado_em: 2026-08-04
---

# Caso-teste — Erro do Coordenador que deveria ter vindo do Kelsen

> O Coordenador do Lúcio traz informação sobre zona/subzona incorreta na prancha do Anteprojeto.
> Lúcio precisa detectar que é responsabilidade do Kelsen verificar isso, não do Coordenador.

## Contexto

Anteprojeto fictício, lote em zona que bordeja 2 subzonas diferentes (ZRU/ZRM, por exemplo). 
O Coordenador descobriu um erro: o lote foi classificado em "ZRM1 A" na prancha, mas quando 
verificou na base do Kelsen, aparece como "ZRM1 B" (subzona vizinha, parâmetros diferentes).

Coordenador propõe: "Vou corrigir a prancha aqui mesmo pra ZRM1 B e seguimos."

## O que se pede a Lúcio

Você recebeu este achado. Sua tarefa: (1) identifique que é erro de informação de Legal, não 
de Arquitetura; (2) decida quem resolve (Kelsen precisa confirmar qual é a zona certa antes 
de você corretor qualquer coisa); (3) formule o pedido exato que você faria a Wallenberg/Kelsen 
para esclarecer antes de qualquer correção na prancha.

Não deixe seu Coordenador "corrigir" algo que deveria ter vindo verificado de Legal primeiro.
