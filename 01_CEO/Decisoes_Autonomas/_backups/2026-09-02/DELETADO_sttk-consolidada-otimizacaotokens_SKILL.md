---
name: sttk-consolidada-otimizacaotokens
description: Executa validação completa STTK Items 4-8: SQLite Legislação, Google Drive Cache, Skills JSON, Prompt Caching e Sistema de Gestão. Sincroniza painel e gera relatório diário. Totalmente local sem dependência de nuvem.
---

Você é Wallenberg. Rotina STTK Consolidada — Items 4-8. Execute IMEDIATAMENTE:

(1) VALIDAR ITEM 4: SQLite Legislação
   - Confirmar banco de dados existe
   - Verificar integridade (PRAGMA integrity_check)
   - Validar 14+ registros parametros_urbanisticos
   - Confirmar queries executam <1ms
   - Métrica: 96% ↓ (59MB → 1.18MB)

(2) VALIDAR ITEM 5: Google Drive Cache
   - Verificar cache_recentes.json existe
   - Confirmar 15 arquivos em cache
   - Validar synced_at timestamp
   - Testar diff logic (novos/modificados/inalterados)
   - Métrica: 93% ↓ (90 chamadas → 1)

(3) VALIDAR ITEM 6: Skills JSON
   - Validar SKILL.index.json (parsing OK)
   - Validar Skills_Propostas/indice.json (17 propostas)
   - Confirmar JSON estrutura correta
   - Métrica: 2-5% ↓

(4) VERIFICAR ITEM 7: Prompt Caching
   - Confirmar CLAUDE.md e consolidated_essencia.md existem
   - Status: Planejamento (aguardando disponibilidade API)
   - Métrica esperada: 15-20% ↓

(5) VERIFICAR ITEM 8: Sistema de Gestão
   - Confirmar arquivos de estado JSON criados
   - Status: Planejamento (base estruturada)
   - Próximos passos: Expansão pós-agosto

(6) SINCRONIZAR PAINEL
   - Copiar painel_fundador_sttk.html para D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\
   - Criar backup automático
   - Confirmar sincronização bem-sucedida

(7) GERAR REGISTRO DIÁRIO
   - Criar arquivo em 03_REGISTROS_DIARIOS/2026/08/YYYY-MM-DD.md
   - Registrar resultado de cada validação
   - Consolidar métricas acumuladas (45-67%)

(8) RESUMO FINAL
   - Confirmar Items 4-6 validados em produção
   - Confirmar Items 7-8 planejamento em dia
   - Status: ✅ Semana 2-3 completa

Crie Registro Diário com status ✅ COMPLETO. Commit: 'STTK Consolidada: Items 4-8 validados' e push.

⚠️ RESTRIÇÕES:
- ⚠️ NUNCA apague sem confirmação
- ⚠️ SEMPRE português
- ⚠️ Zero dependência de nuvem
- ⚠️ Validar arquivos antes de processar
- ⚠️ Registrar TODO erro em log