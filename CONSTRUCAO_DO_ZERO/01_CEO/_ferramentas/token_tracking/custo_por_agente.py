#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
custo_por_agente.py — Quanto cada agente STTK gasta de token, medido.

Le os transcripts de SUBAGENTE do Claude Code:
    ~/.claude/projects/<projeto>/<sessionId>/subagents/agent-<id>.jsonl
    ~/.claude/projects/<projeto>/<sessionId>/subagents/agent-<id>.meta.json  (agentType)

Responde a duas perguntas:
  1. Quanto cada agente (Kelsen, Lucio, Hely, Cardozo, ...) esta gastando DE FATO.
  2. Comparativo "com vs sem otimizacao de tokens": usa 30/07/2026 como corte
     (dia em que os slices de CLAUDE.md e as referencias em .claude/agents/*.md
     entraram) e mostra o contexto inicial por invocacao antes x depois.

     IMPORTANTE: nao existe medicao real de um mundo "sem otimizacao". O que este
     script mostra e o antes/depois do corte. A leitura honesta (ver RELATORIO):
     o contexto por agente NAO caiu apos a otimizacao — subiu, acompanhando o
     crescimento do proprio projeto (mais estado, mais pendencias, mais agentes).

Saidas (nesta pasta):
  - custo_por_agente.json
  - RELATORIO_CUSTO_AGENTES.md

Uso:  python custo_por_agente.py [--transcripts DIR] [--corte YYYY-MM-DD]
"""

import argparse
import glob
import json
import os
import statistics
from collections import defaultdict
from datetime import datetime

DEFAULT_TRANSCRIPTS = os.path.expanduser(
    r"~/.claude/projects/D--000-ESTRUTURA-DEPARTAMENTO-DE-PROJETO"
)
CORTE_OTIMIZACAO = "2026-07-30"  # slices CLAUDE.md + refs em .claude/agents/*.md

# Precos de tabela publica (USD por milhao de tokens):
# input / escrita de cache (5m) / leitura de cache / saida
MODEL_PRICES = {
    "claude-opus-5":              (15.0, 18.75, 1.50, 75.0),
    "claude-opus-4-8":            (15.0, 18.75, 1.50, 75.0),
    "claude-opus-4-6":            (15.0, 18.75, 1.50, 75.0),
    "claude-sonnet-5":            (3.0,  3.75,  0.30, 15.0),
    "claude-sonnet-4-6":          (3.0,  3.75,  0.30, 15.0),
    "claude-haiku-4-5-20251001":  (1.0,  1.25,  0.10,  5.0),
}
DEFAULT_PRICE = (3.0, 3.75, 0.30, 15.0)  # assume Sonnet se modelo desconhecido

# custo-equivalente normalizado (unidade abstrata, comparavel entre agentes):
CE_IN, CE_CW, CE_CR, CE_OUT = 1.0, 1.25, 0.10, 5.0


def human(n):
    if n is None:
        return "-"
    n = float(n)
    if abs(n) >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if abs(n) >= 1_000:
        return f"{n/1_000:.1f}k"
    return f"{n:.0f}"


def usd(n):
    return f"US$ {n:,.2f}"


def parse_ts(s):
    try:
        return datetime.fromisoformat((s or "").replace("Z", "+00:00"))
    except ValueError:
        return None


def iter_agent_turns(jsonl_path):
    """Rende (input, cache_write, cache_read, output, thinking, model, ts_date)."""
    for line in open(jsonl_path, "r", encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        m = o.get("message")
        if not isinstance(m, dict):
            continue
        u = m.get("usage")
        if not isinstance(u, dict):
            continue
        det = u.get("output_tokens_details") or {}
        yield (
            u.get("input_tokens", 0) or 0,
            u.get("cache_creation_input_tokens", 0) or 0,
            u.get("cache_read_input_tokens", 0) or 0,
            u.get("output_tokens", 0) or 0,
            det.get("thinking_tokens", 0) or 0,
            m.get("model") or "?",
            (o.get("timestamp") or "")[:10],
        )


def build_rotinas(tdir):
    """Custo das sessoes principais agrupado por tarefa agendada / origem."""
    rot = defaultdict(lambda: {"sessoes": 0, "custo_eq": 0.0, "usd": 0.0,
                               "turnos": 0, "d0": None, "d1": None})
    for f in glob.glob(os.path.join(tdir, "*.jsonl")):
        lines = open(f, "r", encoding="utf-8", errors="replace").readlines()
        origem = "(interativo / manual)"
        for line in lines[:8]:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = o.get("message")
            c = m.get("content") if isinstance(m, dict) else None
            if isinstance(c, str) and c.startswith("<scheduled-task name="):
                origem = c.split('"')[1]
                break
        r = rot[origem]
        r["sessoes"] += 1
        for line in lines:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = o.get("message")
            if not isinstance(m, dict) or not isinstance(m.get("usage"), dict):
                continue
            u = m["usage"]
            it = u.get("input_tokens", 0) or 0
            cw = u.get("cache_creation_input_tokens", 0) or 0
            cr = u.get("cache_read_input_tokens", 0) or 0
            ot = u.get("output_tokens", 0) or 0
            p_in, p_cw, p_cr, p_out = MODEL_PRICES.get(m.get("model", ""), DEFAULT_PRICE)
            r["turnos"] += 1
            r["custo_eq"] += it*CE_IN + cw*CE_CW + cr*CE_CR + ot*CE_OUT
            r["usd"] += (it*p_in + cw*p_cw + cr*p_cr + ot*p_out) / 1_000_000
            d = (o.get("timestamp") or "")[:10]
            if d:
                r["d0"] = min(r["d0"], d) if r["d0"] else d
                r["d1"] = max(r["d1"], d) if r["d1"] else d
    out = [{"origem": k, "sessoes": v["sessoes"], "turnos": v["turnos"],
            "custo_eq": round(v["custo_eq"]), "usd_aprox": round(v["usd"], 2),
            "periodo": f"{v['d0']} -> {v['d1']}"} for k, v in rot.items()]
    out.sort(key=lambda x: -x["usd_aprox"])
    return out


def build(tdir, corte):
    ag = defaultdict(lambda: {
        "invocacoes": 0, "turnos": 0,
        "input": 0, "cache_write": 0, "cache_read": 0, "output": 0, "thinking": 0,
        "custo_eq": 0.0, "usd": 0.0,
        "ctx0_pre": [], "ctx0_pos": [],
        "d0": None, "d1": None,
        "descricoes": [],
    })

    metas = glob.glob(os.path.join(tdir, "*", "subagents", "agent-*.meta.json"))
    for mf in metas:
        jf = mf[:-len(".meta.json")] + ".jsonl"
        if not os.path.exists(jf):
            continue
        try:
            meta = json.load(open(mf, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        at = meta.get("agentType") or "desconhecido"
        desc = (meta.get("description") or "").strip()

        turns = list(iter_agent_turns(jf))
        if not turns:
            continue

        a = ag[at]
        a["invocacoes"] += 1
        a["turnos"] += len(turns)
        if desc and len(a["descricoes"]) < 6:
            a["descricoes"].append(desc)

        ctx0 = None
        for it, cw, cr, ot, th, model, d in turns:
            a["input"] += it
            a["cache_write"] += cw
            a["cache_read"] += cr
            a["output"] += ot
            a["thinking"] += th
            a["custo_eq"] += it*CE_IN + cw*CE_CW + cr*CE_CR + ot*CE_OUT
            p_in, p_cw, p_cr, p_out = MODEL_PRICES.get(model, DEFAULT_PRICE)
            a["usd"] += (it*p_in + cw*p_cw + cr*p_cr + ot*p_out) / 1_000_000
            if d:
                a["d0"] = min(a["d0"], d) if a["d0"] else d
                a["d1"] = max(a["d1"], d) if a["d1"] else d
            if ctx0 is None:
                ctx0 = (it + cw + cr, d)

        if ctx0 and ctx0[0] > 0 and ctx0[1]:
            bucket = "ctx0_pre" if ctx0[1] < corte else "ctx0_pos"
            a[bucket].append(ctx0[0])

    # ---- monta lista ordenada por custo-eq desc ----
    linhas = []
    for at, a in ag.items():
        pre = int(statistics.median(a["ctx0_pre"])) if a["ctx0_pre"] else None
        pos = int(statistics.median(a["ctx0_pos"])) if a["ctx0_pos"] else None
        linhas.append({
            "agente": at,
            "invocacoes": a["invocacoes"],
            "turnos": a["turnos"],
            "tokens_input": a["input"],
            "tokens_cache_write": a["cache_write"],
            "tokens_cache_read": a["cache_read"],
            "tokens_output": a["output"],
            "tokens_thinking": a["thinking"],
            "custo_eq": round(a["custo_eq"]),
            "usd_aprox": round(a["usd"], 2),
            "ctx0_mediana_pre_otim": pre,
            "ctx0_mediana_pos_otim": pos,
            "ctx0_variacao_pct": (
                round((pos - pre) / pre * 100, 1) if pre and pos else None
            ),
            "periodo": f"{a['d0']} -> {a['d1']}",
            "amostra_descricoes": a["descricoes"],
        })
    linhas.sort(key=lambda x: -x["custo_eq"])

    tot_ce = sum(x["custo_eq"] for x in linhas) or 1
    tot_usd = sum(x["usd_aprox"] for x in linhas)
    for x in linhas:
        x["pct_do_total"] = round(x["custo_eq"] / tot_ce * 100, 1)

    rotinas = build_rotinas(tdir)
    usd_rotinas = sum(r["usd_aprox"] for r in rotinas)

    return {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "corte_otimizacao": corte,
        "total_invocacoes": sum(x["invocacoes"] for x in linhas),
        "custo_eq_total": round(tot_ce),
        "usd_aprox_total": round(tot_usd, 2),
        "agentes": linhas,
        "rotinas_sessao_principal": rotinas,
        "usd_aprox_sessoes_principais": round(usd_rotinas, 2),
        "usd_aprox_geral": round(tot_usd + usd_rotinas, 2),
    }


def write_report(data, path):
    L = []
    P = L.append
    P("# Custo por Agente STTK — medição real")
    P("")
    P(f"**Gerado:** {data['gerado_em']}  ")
    P(f"**Fonte:** transcripts de subagente do Claude Code (`<sessionId>/subagents/`)  ")
    P(f"**Invocações medidas:** {data['total_invocacoes']}  ")
    P(f"**Custo-equivalente total (subagentes):** {human(data['custo_eq_total'])}  ")
    P(f"**Custo aproximado em USD (tabela pública, mix de modelos):** {usd(data['usd_aprox_total'])}")
    P("")
    P("> `custo-eq` = input×1 + cache_write×1,25 + cache_read×0,10 + output×5. "
      "Unidade normalizada, comparável entre agentes. O USD usa preços de tabela "
      "por modelo — é estimativa, não a fatura real.")
    P("")

    P("## 1. Quanto cada agente gasta HOJE")
    P("")
    P("| Agente | Invoc. | Turnos | Saída | Cache read | custo-eq | % | USD aprox. | Período |")
    P("|---|--:|--:|--:|--:|--:|--:|--:|---|")
    for x in data["agentes"]:
        P(f"| **{x['agente']}** | {x['invocacoes']} | {x['turnos']} "
          f"| {human(x['tokens_output'])} | {human(x['tokens_cache_read'])} "
          f"| {human(x['custo_eq'])} | {x['pct_do_total']}% | {usd(x['usd_aprox'])} "
          f"| {x['periodo']} |")
    P(f"| **TOTAL** | {data['total_invocacoes']} | | | | "
      f"{human(data['custo_eq_total'])} | 100% | {usd(data['usd_aprox_total'])} | |")
    P("")
    P("O gasto é dominado por **cache read** (contexto relido a cada turno) e por "
      "**output**. Poucas horas de sessão longa de um agente pesam mais que dezenas "
      "de invocações curtas.")
    P("")

    P("## 2. \"Com vs sem otimização\" — contexto inicial por invocação")
    P("")
    P(f"Corte: **{data['corte_otimizacao']}** (slices de CLAUDE.md + referências de "
      "slice em `.claude/agents/*.md`).")
    P("")
    P("| Agente | ctx inicial ANTES | ctx inicial DEPOIS | variação |")
    P("|---|--:|--:|--:|")
    for x in data["agentes"]:
        if x["ctx0_mediana_pre_otim"] or x["ctx0_mediana_pos_otim"]:
            v = x["ctx0_variacao_pct"]
            vtxt = f"{v:+.1f}%" if v is not None else "—"
            P(f"| {x['agente']} | {human(x['ctx0_mediana_pre_otim'])} "
              f"| {human(x['ctx0_mediana_pos_otim'])} | {vtxt} |")
    P("")
    P("**Leitura honesta:** não existe medição de um mundo \"sem otimização\" — a "
      "otimização mexeu em arquivos compartilhados, não num parâmetro que dá para "
      "ligar/desligar. O que a tabela mostra é o antes/depois do corte, e em todos "
      "os agentes com histórico dos dois lados o contexto **subiu**, não caiu. A "
      "causa provável é o próprio projeto crescendo (estado dos agentes maior, mais "
      "pendências, mais agentes referenciados), não os slices. Ou seja: a economia "
      "atribuível ao plano de otimização, por agente, é **nula ou negativa** na "
      "medição real.")
    P("")
    P("O único ganho de token de fato presente nos dados é o **prompt caching** "
      "(ver `RELATORIO_TOKENS.md`), que já vinha ativo e não faz parte do plano.")
    P("")

    P("## 3. Contexto: custo das sessões principais (não-subagente)")
    P("")
    P("Cada rodada de rotina roda numa sessão principal (Wallenberg) que **também** "
      "gasta token, à parte dos subagentes que ela invoca.")
    P("")
    P("| Origem | Sessões | Turnos | custo-eq | USD aprox. | Período |")
    P("|---|--:|--:|--:|--:|---|")
    for r in data["rotinas_sessao_principal"]:
        P(f"| {r['origem']} | {r['sessoes']} | {r['turnos']} "
          f"| {human(r['custo_eq'])} | {usd(r['usd_aprox'])} | {r['periodo']} |")
    P(f"| **subtotal sessões principais** | | | | "
      f"{usd(data['usd_aprox_sessoes_principais'])} | |")
    P("")
    P(f"**Total geral aproximado (sessões principais + subagentes):** "
      f"{usd(data['usd_aprox_geral'])} desde ~16/07/2026.")
    P("")
    P("> USD por preço de tabela pública, mix de modelos — estimativa de ordem de "
      "grandeza, não a fatura. Serve para dizer onde o token vai: a cadeia Legal "
      "(Kelsen + Hely) é o maior bloco de subagente; as rotinas agendadas de "
      "Wallenberg são o maior bloco de sessão principal.")
    P("")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--transcripts", default=DEFAULT_TRANSCRIPTS)
    ap.add_argument("--corte", default=CORTE_OTIMIZACAO)
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()

    tdir = os.path.abspath(os.path.expanduser(args.transcripts))
    if not os.path.isdir(tdir):
        raise SystemExit(f"Pasta de transcripts nao encontrada: {tdir}")

    data = build(tdir, args.corte)
    out_json = os.path.join(args.outdir, "custo_por_agente.json")
    out_md = os.path.join(args.outdir, "RELATORIO_CUSTO_AGENTES.md")
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    write_report(data, out_md)

    print(f"Invocacoes medidas : {data['total_invocacoes']}")
    print(f"Custo-eq total     : {human(data['custo_eq_total'])}")
    print(f"USD aprox total    : {usd(data['usd_aprox_total'])}")
    print()
    print(f"{'agente':<16}{'inv':>5}{'custo-eq':>12}{'%':>7}{'USD aprox':>14}"
          f"   ctx0 pre->pos")
    for x in data["agentes"]:
        print(f"{x['agente']:<16}{x['invocacoes']:>5}{human(x['custo_eq']):>12}"
              f"{x['pct_do_total']:>6}%{usd(x['usd_aprox']):>14}   "
              f"{x['ctx0_mediana_pre_otim']}->{x['ctx0_mediana_pos_otim']}")
    print()
    print(f"Escrito: {out_json}")
    print(f"Escrito: {out_md}")


if __name__ == "__main__":
    main()
