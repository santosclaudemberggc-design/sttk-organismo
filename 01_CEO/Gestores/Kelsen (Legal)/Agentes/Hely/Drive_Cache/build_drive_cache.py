"""Item 5 (13/08) - Cache local de metadados do Google Drive (modifiedTime tracking)
Evita repetir search_files()/get_file_metadata() do Drive a cada conversa: guarda
id, path e modifiedTime de cada arquivo/pasta de POPs, Memoriais e Clientes num
SQLite local, e detecta o que mudou comparando modifiedTime contra o cache.
Reexecutavel: idempotente por upsert (nao apaga o banco entre execucoes).

Como os dados chegam: este script NAO fala com a API do Drive sozinho. Quem
tem as credenciais MCP do Drive (a sessao do Wallenberg/Hely) faz a
enumeracao via search_files(parentId=...) e grava um snapshot JSON (lista de
records com id/title/mimeType/parentId/modifiedTime/path/root_scope). Este
script consome esse JSON e mantem o cache SQLite + calcula o diff. Rodar de
novo com um snapshot mais recente = sync incremental.
"""
import os
import sys
import json
import sqlite3
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "drive_cache.sqlite3")

SCHEMA = """
CREATE TABLE IF NOT EXISTS drive_files (
    id            TEXT PRIMARY KEY,
    title         TEXT NOT NULL,
    mime_type     TEXT NOT NULL,
    parent_id     TEXT,
    path          TEXT NOT NULL,
    root_scope    TEXT NOT NULL,      -- POPs | Memoriais | Clientes | ROOT
    modified_time TEXT NOT NULL,      -- modifiedTime do Drive (RFC3339, fonte da verdade p/ diff)
    leaf_synced   INTEGER NOT NULL DEFAULT 1,  -- 0 = pasta descoberta mas conteudo ainda nao enumerado
    first_seen_at TEXT NOT NULL,
    last_synced_at TEXT NOT NULL,
    removed_at    TEXT               -- preenchido quando some de um full sync (nao aparece mais)
);
CREATE TABLE IF NOT EXISTS sync_runs (
    run_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    mode          TEXT NOT NULL,     -- full | incremental
    synced_at     TEXT NOT NULL,
    input_records INTEGER NOT NULL,
    new_count     INTEGER NOT NULL,
    updated_count INTEGER NOT NULL,
    unchanged_count INTEGER NOT NULL,
    removed_count INTEGER NOT NULL
);
"""


def load_snapshot(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["synced_at"], data["records"]


def sync(snapshot_path, mode):
    synced_at, records = load_snapshot(snapshot_path)

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    new_count = updated_count = unchanged_count = 0
    seen_ids = set()

    for r in records:
        seen_ids.add(r["id"])
        leaf_synced = 1 if r.get("leaf_synced", True) else 0
        row = conn.execute(
            "SELECT modified_time FROM drive_files WHERE id = ?", (r["id"],)
        ).fetchone()

        if row is None:
            conn.execute(
                """INSERT INTO drive_files
                   (id, title, mime_type, parent_id, path, root_scope,
                    modified_time, leaf_synced, first_seen_at, last_synced_at, removed_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)""",
                (r["id"], r["title"], r["mimeType"], r.get("parentId"), r["path"],
                 r["root_scope"], r["modifiedTime"], leaf_synced, synced_at, synced_at),
            )
            new_count += 1
        elif row[0] != r["modifiedTime"]:
            conn.execute(
                """UPDATE drive_files
                   SET title=?, mime_type=?, parent_id=?, path=?, root_scope=?,
                       modified_time=?, leaf_synced=?, last_synced_at=?, removed_at=NULL
                   WHERE id=?""",
                (r["title"], r["mimeType"], r.get("parentId"), r["path"], r["root_scope"],
                 r["modifiedTime"], leaf_synced, synced_at, r["id"]),
            )
            updated_count += 1
        else:
            conn.execute(
                "UPDATE drive_files SET last_synced_at=?, removed_at=NULL WHERE id=?",
                (synced_at, r["id"]),
            )
            unchanged_count += 1

    removed_count = 0
    if mode == "full":
        # Sweep de exclusao: so faz sentido quando o snapshot cobre 100% da
        # arvore (full sync). Um snapshot incremental parcial nao pode ser
        # usado pra concluir que o resto sumiu.
        scopes = set(r["root_scope"] for r in records)
        for scope in scopes:
            cur = conn.execute(
                "SELECT id FROM drive_files WHERE root_scope=? AND removed_at IS NULL",
                (scope,),
            )
            for (existing_id,) in cur.fetchall():
                if existing_id not in seen_ids:
                    conn.execute(
                        "UPDATE drive_files SET removed_at=? WHERE id=?",
                        (synced_at, existing_id),
                    )
                    removed_count += 1

    conn.execute(
        """INSERT INTO sync_runs
           (mode, synced_at, input_records, new_count, updated_count, unchanged_count, removed_count)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (mode, synced_at, len(records), new_count, updated_count, unchanged_count, removed_count),
    )
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM drive_files WHERE removed_at IS NULL").fetchone()[0]
    size_kb = os.path.getsize(DB_PATH) / 1024
    conn.close()

    print(f"[{mode}] snapshot={os.path.basename(snapshot_path)} synced_at={synced_at}")
    print(f"  input records: {len(records)}")
    print(f"  novos: {new_count} | atualizados: {updated_count} | inalterados: {unchanged_count} | removidos: {removed_count}")
    print(f"  total no cache (ativos): {total}")
    print(f"  tamanho do banco: {size_kb:.1f} KB")
    return {
        "new": new_count, "updated": updated_count,
        "unchanged": unchanged_count, "removed": removed_count,
        "total": total, "size_kb": size_kb,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="snapshot JSON (records do Drive)")
    parser.add_argument("--mode", choices=["full", "incremental"], default="incremental")
    args = parser.parse_args()
    sync(args.input, args.mode)
