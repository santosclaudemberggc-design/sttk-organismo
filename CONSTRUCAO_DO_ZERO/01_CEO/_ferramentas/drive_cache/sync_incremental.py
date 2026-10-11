#!/usr/bin/env python3
"""
Item 5 — Google Drive Cache Incremental.

Uso real: o Agente/Gestor chama mcp__Google_Drive__list_recent_files (ou
search_files) UMA vez por sessão, salva a resposta bruta em JSON, e roda
este script contra o cache local (cache_recentes.json). Só os arquivos
com modifiedTime novo ou desconhecido entram na lista "precisa buscar
conteúdo" — o resto é servido do cache sem nova chamada MCP.

Não inventa dado: se o cache nunca foi sincronizado, todo mundo entra
como "novo" (comportamento correto na primeira sincronização).
"""
import json
import sys
from pathlib import Path

CACHE_PATH = Path(__file__).parent / "cache_recentes.json"


def load_cache(path=CACHE_PATH):
    if not path.exists():
        return {"synced_at": None, "fonte": None, "arquivos": {}}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache, path=CACHE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def diff(cache_atual, arquivos_buscados):
    """arquivos_buscados: dict fileId -> {title, modifiedTime, ...} (saída crua do MCP)."""
    cache_antigo = cache_atual.get("arquivos", {})
    novos, modificados, inalterados = [], [], []
    for file_id, meta in arquivos_buscados.items():
        anterior = cache_antigo.get(file_id)
        if anterior is None:
            novos.append(file_id)
        elif anterior.get("modifiedTime") != meta.get("modifiedTime"):
            modificados.append(file_id)
        else:
            inalterados.append(file_id)
    return {"novos": novos, "modificados": modificados, "inalterados": inalterados}


def is_cache_fresh(cache, ttl_horas=1):
    """Decide se vale a pena chamar a MCP de novo, ou servir do cache local."""
    from datetime import datetime, timezone, timedelta
    synced_at = cache.get("synced_at")
    if not synced_at:
        return False
    dt = datetime.fromisoformat(synced_at.replace("Z", "+00:00"))
    return datetime.now(timezone.utc) - dt < timedelta(hours=ttl_horas)


if __name__ == "__main__":
    cache = load_cache()
    print(f"Cache local: {len(cache.get('arquivos', {}))} arquivos, sincronizado em {cache.get('synced_at')}")

    # Teste 1: comparar o cache contra ele mesmo (simula 2ª conversa no mesmo dia,
    # nenhum arquivo mudou no Drive) -> espera 0 novos, 0 modificados.
    resultado_repeticao = diff(cache, cache["arquivos"])
    print("\nTeste 1 — mesma foto comparada contra si mesma (nenhuma mudança real no Drive):")
    print(f"  novos={len(resultado_repeticao['novos'])} "
          f"modificados={len(resultado_repeticao['modificados'])} "
          f"inalterados={len(resultado_repeticao['inalterados'])}")
    assert resultado_repeticao["novos"] == [] and resultado_repeticao["modificados"] == [], \
        "Falha: comparar o cache contra si mesmo não pode gerar novos/modificados"

    # Teste 2: cache vazio (primeira sincronização) -> todo mundo é "novo".
    resultado_primeira_sync = diff({"arquivos": {}}, cache["arquivos"])
    print("\nTeste 2 — primeira sincronização (cache vazio):")
    print(f"  novos={len(resultado_primeira_sync['novos'])} "
          f"modificados={len(resultado_primeira_sync['modificados'])} "
          f"inalterados={len(resultado_primeira_sync['inalterados'])}")
    assert len(resultado_primeira_sync["novos"]) == len(cache["arquivos"]), \
        "Falha: primeira sincronização deveria marcar todos os arquivos como novos"

    # Teste 3: simular 1 arquivo modificado (POP MASTER com novo modifiedTime).
    arquivos_com_1_mudanca = dict(cache["arquivos"])
    pop_master_id = "12yu6ed91FQSuPwgDxZg-oXE4x5IDYN3Lv7SS4FIO2MU"
    arquivos_com_1_mudanca[pop_master_id] = {
        **arquivos_com_1_mudanca[pop_master_id],
        "modifiedTime": "2026-08-13T09:00:00.000Z",
    }
    resultado_1_mudanca = diff(cache, arquivos_com_1_mudanca)
    print("\nTeste 3 — 1 arquivo com modifiedTime novo (POP MASTER editado):")
    print(f"  novos={len(resultado_1_mudanca['novos'])} "
          f"modificados={resultado_1_mudanca['modificados']} "
          f"inalterados={len(resultado_1_mudanca['inalterados'])}")
    assert resultado_1_mudanca["modificados"] == [pop_master_id]
    assert len(resultado_1_mudanca["inalterados"]) == len(cache["arquivos"]) - 1

    print("\n✅ 3/3 testes passaram.")
    print(f"\nis_cache_fresh(ttl=1h) agora: {is_cache_fresh(cache, ttl_horas=1)} "
          f"(cache gravado em 13/08 00:00 UTC — esperado False depois de 1h)")
