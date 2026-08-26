# Fase 2: Integração de Otimizações de Tokens
## Status: Planejado para 26/08/2026 (próxima sessão da rotina)

**Autor:** Wallenberg  
**Data de Criação:** 25/08/2026  
**Cronograma:** 26/08/2026 (execução automática)  
**Bloqueador:** Nenhum (integração é refactoring de código existente)

---

## 📋 Objetivo

Conectar as estruturas otimizadas (SQLite, Cache, Skills JSON) aos fluxos diários, economizando **40-66% de tokens** nas conversas do Claude Code.

**Status Atual:** 
- Estruturas criadas ✓
- Estruturas validadas ✓
- **Integração aos fluxos: ❌ FALTANDO**

---

## 🔧 Tarefas de Integração (3 módulos)

### Módulo 1: Integrar Cache do Drive (Item 5)
**Arquivo Principal:** `wallenberg-rotina-diaria-skills-v2_SKILL.md`  
**Problema Atual:** Rotina chama `list_recent_files()` do MCP Google Drive a cada execução (90 chamadas/dia = overhead)  
**Solução:** Usar `cache_recentes.json` como fonte primária antes de chamar API

**Passos de Integração:**
1. Ler `cache_recentes.json` no início da rotina (localização: `.../01_CEO/_ferramentas/drive_cache/cache_recentes.json`)
2. Validar `synced_at` timestamp — se < 24h, usar cache direto
3. Se > 24h, chamar `list_recent_files()` e atualizar `cache_recentes.json`
4. Loop sobre arquivos em cache (em vez de resultado bruto da API)

**Ficheiro de Código (pseudocódigo):**
```python
# Em wallenberg-rotina-diaria-skills-v2_SKILL.md, função "pesquisar_drive"
cache_path = "01_CEO/_ferramentas/drive_cache/cache_recentes.json"
cache = load_json(cache_path)

# Validar age do cache
cache_age_hours = (datetime.now() - parse_iso(cache['synced_at'])).total_seconds() / 3600
if cache_age_hours < 24:
    files = cache['arquivos'].values()  # Usar cache
    print(f"✓ Cache recente ({cache_age_hours:.1f}h), usando {len(files)} arquivos em cache")
else:
    # Cache expirou, sincronizar
    files = list_recent_files(...)  # MCP Drive
    cache['synced_at'] = datetime.now().isoformat()
    cache['arquivos'] = {f['id']: f for f in files}
    save_json(cache_path, cache)
    print(f"✓ Cache atualizado, {len(files)} arquivos novos")

# Resto da rotina usa 'files' sem saber se veio de cache ou API
for file in files:
    yield file
```

**Redução Esperada:** 93% ↓ (90 chamadas → 1/dia, se cache < 24h)

---

### Módulo 2: Integrar SQLite de Legislação (Item 4)
**Arquivo Principal:** `wallenberg-rotina-diaria-skills-v2_SKILL.md`  
**Problema Atual:** Rotina pesquisa legislação via WebFetch + agregadores (ABNT, Legislação, etc) — baixa textos inteiros a cada busca  
**Solução:** Consultar SQLite `legislacao_index.sqlite3` antes de WebFetch

**Passos de Integração:**
1. Ler `legislacao_index.sqlite3` (localização: `.../Kelsen/Hely/Fontes_Legislacao/indice_sqlite/legislacao_index.sqlite3`)
2. Preparar queries: `SELECT * FROM parametros_urbanisticos WHERE topico LIKE ?`
3. Se encontra na base, retornar + sinalizar "checado em 25/08" (evita re-pesquisar)
4. Se não encontra, fazer WebFetch + registrar achado novo em log

**Ficheiro de Código (pseudocódigo):**
```python
# Em wallenberg-rotina-diaria-skills-v2_SKILL.md, função "pesquisar_legislacao"
import sqlite3

db_path = "01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/indice_sqlite/legislacao_index.sqlite3"
conn = sqlite3.connect(db_path, timeout=2)

def buscar_na_base(topico_palavra_chave):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT norma, artigos, vigencia FROM parametros_urbanisticos WHERE topico LIKE ? LIMIT 5",
        (f"%{topico_palavra_chave}%",)
    )
    results = cursor.fetchall()
    return results if results else None

# Na rotina:
topico = "transferencia de densidade"
resultado_sqlite = buscar_na_base(topico)

if resultado_sqlite:
    print(f"✓ Encontrado no SQLite: {resultado_sqlite[0][0]}")
    return resultado_sqlite[0]  # Retorna sem WebFetch
else:
    print(f"⚠ Não encontrado no SQLite, pesquisando web...")
    resultado_web = webfetch(f"legislação rio {topico}")
    # Registrar em log para Hely adicionar ao SQLite depois
    return resultado_web
```

**Validação:** Antes de implementar, confirmar com Kelsen que o SQLite tem os campos esperados (`topico`, `norma`, `artigos`, `vigencia`)

**Redução Esperada:** 96% ↓ (59 MB → 1.18 MB de dados trafegados por consulta)

---

### Módulo 3: Indexar Skills JSON (Item 6)
**Arquivo Principal:** `wallenberg-rotina-diaria-skills-v2_SKILL.md` + novo índice  
**Problema Atual:** Rotina pesquisa Skills em `01_CEO/Skills_Propostas/2026/*/indice.json` manualmente (sem prefiltro)  
**Solução:** Criar índice consolidado `Skills_Propostas/_index_consolidado.json` e consultar por categoria/gestor/palavra-chave

**Passos de Integração:**
1. Consolidar todos os `indice.json` mensais em um único arquivo indexado por:
   - `gestor`: Kelsen, Lúcio, Cardozo, etc
   - `categoria`: Legal, Arquitetura, Complementares, Fechamento
   - `palavra_chave`: lista de termos (ex: ["transferência", "densidade", "CAB"])
2. Gerar índice em tempo de build (rodar 1x/mês pós-novo-mês)
3. Pesquisa rápida: `index['Kelsen']`, `index['Arquitetura']`, etc

**Ficheiro JSON:**
```json
{
  "_meta": {"consolidado_em": "2026-08-25T14:37:00Z", "meses_cobertos": "Julho 2026"},
  "por_gestor": {
    "Kelsen": [
      {"data": "2026-07-16", "titulo": "Base legal Anexo I", "arquivo": "legal_anexo-i-base-legal-decreto-48719-21.md"},
      {"data": "2026-07-16", "titulo": "ART georreferenciada", "arquivo": "legal_art-georreferenciada-crea-rj-2026.md"},
      ...
    ],
    "Lúcio": [...],
    "Cardozo": [...]
  },
  "por_categoria": {
    "Legal": [...],
    "Arquitetura": [...],
    "Complementares": [...]
  },
  "por_palavra_chave": {
    "transferência": [{ref: "Kelsen", ...}],
    "densidade": [...],
    "NBR": [{ref: "Arquitetura", ...}],
    ...
  }
}
```

**Passos de Integração:**
1. Gerar `_index_consolidado.json` via script Python (localização: `01_CEO/Skills_Propostas/_index_consolidado.json`)
2. Rotina diária consulta índice antes de ler arquivos individuais
3. Se pesquisa for "NBR 6118 estrutural", retorna `index['por_palavra_chave']['NBR'][...] + index['Cardozo'][...]`

**Redução Esperada:** 2-5% ↓ (parsing mais rápido, menos I/O de disco)

---

## 📊 Redução Total Esperada Após Fase 2

| Módulo | Redução | Status |
|--------|---------|--------|
| Cache Drive (Módulo 1) | 93% ↓ | 🔄 Integração |
| SQLite Legislação (Módulo 2) | 96% ↓ | 🔄 Integração |
| Skills JSON (Módulo 3) | 2-5% ↓ | 🔄 Integração |
| **TOTAL** | **45-67% ↓** | **🔄 Planejado** |

---

## ✅ Checklist de Execução (26/08/2026)

- [ ] **Módulo 1:** Ler `cache_recentes.json`, validar age, integrar em `wallenberg-rotina-diaria-skills-v2_SKILL.md`
- [ ] **Módulo 2:** Validar schema do SQLite com Kelsen, integrar consulta de legislação
- [ ] **Módulo 3:** Gerar `_index_consolidado.json`, testar busca por gestor/categoria/palavra-chave
- [ ] **Teste:** Rodar rotina manual amanhã e medir tempo de execução antes/depois
- [ ] **Registro:** Entrada em `Agosto.md` + atualizar `pendencias.json` (estado: resolvida)
- [ ] **Publicação:** Atualizar `wallenberg-rotina-diaria-skills-v2_SKILL.md` com novo código

---

## 🔐 Notas de Segurança

- SQLite é arquivo estático — sem risco de injeção
- Cache JSON carrega dados estruturados — parse com cuidado
- Índice consolidado: regenerar 1x/mês (evita drift)
- WebFetch fallback: sempre disponível se base falhar

---

## 📌 Referências

- **Item 4 (SQLite):** `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/indice_sqlite/legislacao_index.sqlite3`
- **Item 5 (Cache):** `01_CEO/_ferramentas/drive_cache/cache_recentes.json`
- **Item 6 (Skills):** `01_CEO/Skills_Propostas/2026/Julho/indice.json` (modelo)
- **Rotina a editar:** `01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md`

---

**Status Final:** 🔄 **Pronto para execução 26/08/2026**

Próxima sessão da rotina `wallenberg-drenagem-continua` ou `wallenberg-rotina-diaria-skills` lê este arquivo e executa os 3 módulos em paralelo.
