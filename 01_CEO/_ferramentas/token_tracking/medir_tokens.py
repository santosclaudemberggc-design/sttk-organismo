#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
medir_tokens.py — Medicao REAL de consumo de tokens do organismo STTK.

Le os transcripts de sessao do Claude Code (JSONL) desta pasta de projeto e
extrai numeros REAIS de uso de token por conversa. Sem projecao, sem estimativa
multiplicada: so o que o campo `message.usage` de cada resposta do assistente
registrou.

Metrica principal ("contexto inicial"):
  Para o PRIMEIRO turno do assistente em cada sessao, soma
      input_tokens + cache_creation_input_tokens + cache_read_input_tokens
  Isso e o tamanho do contexto que foi montado ANTES de qualquer trabalho:
  system prompt + CLAUDE.md + memoria + definicoes de ferramentas + 1a msg.
  E exatamente o que o "Plano de Otimizacao de Tokens" prometeu encolher
  (slices de CLAUDE.md em 30/07, consolidacao de MEMORY.md em 29/07).

Saidas (na mesma pasta deste script):
  - token_metrics.json  -> dados por sessao + rollup semanal (para o Painel)
  - RELATORIO_TOKENS.md  -> relatorio legivel com as tabelas

Uso:
    python medir_tokens.py
    python medir_tokens.py --transcripts "C:/caminho/para/os/jsonl"
"""

import argparse
import json
import os
import statistics
from collections import defaultdict
from datetime import datetime, date, timedelta

# Pasta padrao dos transcripts deste projeto (Claude Code / desktop).
DEFAULT_TRANSCRIPTS = os.path.expanduser(
    r"~/.claude/projects/D--000-ESTRUTURA-DEPARTAMENTO-DE-PROJETO"
)

# Marcos do plano de otimizacao — para cruzar com a curva de contexto.
MARCOS = [
    ("2026-07-29", "Item 1: consolidacao MEMORY.md (18 -> 3 arquivos)"),
    ("2026-07-30", "Item 2: CLAUDE.md fatiado em slices por papel"),
    ("2026-08-05", "Item 3: arquivos de estado em JSON"),
    ("2026-08-13", "Item 5: cache incremental do Google Drive"),
]

# Multiplicadores de custo relativo (Anthropic): entrada = 1x, escrita de cache
# = 1.25x, leitura de cache = 0.1x, saida ~ 5x entrada. Serve so para uma
# coluna "custo-equivalente" comparavel entre sessoes — nao e fatura real.
C_IN, C_CWRITE, C_CREAD, C_OUT = 1.0, 1.25, 0.10, 5.0


def iso_week(d: date) -> str:
    y, w, _ = d.isocalendar()
    return f"{y}-S{w:02d}"


def week_start(d: date) -> date:
    return d - timedelta(days=d.isocalendar()[2] - 1)


def parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_session(path):
    """Extrai metricas de um arquivo .jsonl de sessao. None se nao tiver uso."""
    first_ts = last_ts = None
    git_branch = None
    turns = []  # cada turno do assistente com usage
    is_sidechain_only = True

    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue

            ts = parse_ts(o.get("timestamp"))
            if ts:
                if first_ts is None or ts < first_ts:
                    first_ts = ts
                if last_ts is None or ts > last_ts:
                    last_ts = ts

            if not git_branch and o.get("gitBranch"):
                git_branch = o["gitBranch"]

            msg = o.get("message")
            if not isinstance(msg, dict):
                continue
            usage = msg.get("usage")
            if not isinstance(usage, dict):
                continue

            sidechain = bool(o.get("isSidechain"))
            if not sidechain:
                is_sidechain_only = False

            it = usage.get("input_tokens", 0) or 0
            cw = usage.get("cache_creation_input_tokens", 0) or 0
            cr = usage.get("cache_read_input_tokens", 0) or 0
            ot = usage.get("output_tokens", 0) or 0
            think = 0
            det = usage.get("output_tokens_details")
            if isinstance(det, dict):
                think = det.get("thinking_tokens", 0) or 0

            turns.append({
                "ts": ts,
                "sidechain": sidechain,
                "input": it,
                "cache_write": cw,
                "cache_read": cr,
                "output": ot,
                "thinking": think,
                "context": it + cw + cr,
                "model": msg.get("model"),
            })

    if not turns or first_ts is None:
        return None

    main_turns = [t for t in turns if not t["sidechain"]] or turns
    main_turns.sort(key=lambda t: (t["ts"] or first_ts))

    # 1o turno com contexto real (> 0). Sessoes continuadas/compactadas as vezes
    # abrem com um turno sintetico de usage zerado — ignoramos esses.
    reais = [t for t in main_turns if t["context"] > 0]
    if not reais:
        return None
    contexto_inicial = reais[0]["context"]
    contexto_pico = max(t["context"] for t in reais)
    models = sorted({t["model"] for t in turns if t["model"]})

    def _s(key, src=turns):
        return sum(t[key] for t in src)

    custo_eq = (
        _s("input") * C_IN
        + _s("cache_write") * C_CWRITE
        + _s("cache_read") * C_CREAD
        + _s("output") * C_OUT
    )
    cache_read_total = _s("cache_read")
    cache_base_total = _s("input") + _s("cache_write") + cache_read_total
    cache_hit_ratio = (cache_read_total / cache_base_total) if cache_base_total else 0.0

    dur_min = round((last_ts - first_ts).total_seconds() / 60.0, 1)

    return {
        "session_id": os.path.basename(path).replace(".jsonl", ""),
        "data": first_ts.date().isoformat(),
        "inicio": first_ts.isoformat(),
        "fim": last_ts.isoformat(),
        "duracao_min": dur_min,
        "git_branch": git_branch,
        "modelos": models,
        "turnos_assistente": len(turns),
        "turnos_principais": len(main_turns),
        "turnos_subagente": len(turns) - len(main_turns),
        "somente_subagente": is_sidechain_only,
        "contexto_inicial": contexto_inicial,
        "contexto_pico": contexto_pico,
        "input_total": _s("input"),
        "cache_write_total": _s("cache_write"),
        "cache_read_total": cache_read_total,
        "output_total": _s("output"),
        "thinking_total": _s("thinking"),
        "cache_hit_ratio": round(cache_hit_ratio, 4),
        "custo_equivalente": round(custo_eq),
    }


def human(n):
    if n is None:
        return "-"
    if n >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(int(n))


def build(transcripts_dir):
    files = [
        os.path.join(transcripts_dir, f)
        for f in os.listdir(transcripts_dir)
        if f.endswith(".jsonl")
    ]
    sessions = []
    for p in files:
        try:
            s = load_session(p)
        except OSError:
            s = None
        if s:
            sessions.append(s)
    sessions.sort(key=lambda s: s["inicio"])

    # ---- Rollup semanal (so conversas de trabalho: >= 3 turnos principais) ----
    trabalho = [
        s for s in sessions
        if s["turnos_principais"] >= 3 and not s["somente_subagente"]
    ]
    by_week = defaultdict(list)
    for s in trabalho:
        d = date.fromisoformat(s["data"])
        by_week[iso_week(d)].append(s)

    semanal = []
    for wk in sorted(by_week):
        grp = by_week[wk]
        ctx = [s["contexto_inicial"] for s in grp]
        hit = [s["cache_hit_ratio"] for s in grp]
        semanal.append({
            "semana": wk,
            "inicio_semana": week_start(date.fromisoformat(grp[0]["data"])).isoformat(),
            "sessoes": len(grp),
            "contexto_inicial_mediana": int(statistics.median(ctx)),
            "contexto_inicial_media": int(statistics.mean(ctx)),
            "contexto_inicial_min": min(ctx),
            "contexto_inicial_max": max(ctx),
            "cache_hit_ratio_medio": round(statistics.mean(hit), 4),
            "output_total": sum(s["output_total"] for s in grp),
            "custo_equivalente_total": sum(s["custo_equivalente"] for s in grp),
        })

    # ---- Baseline vs. atual: media das 2 primeiras semanas com n>=3 sessoes
    #      contra a media das 2 ultimas. Evita comparar contra uma semana de
    #      1 unica sessao (ruido). Convencao de sinal: variacao_pct POSITIVA
    #      = contexto encolheu (bom); NEGATIVA = contexto cresceu.
    delta = None
    solidas = [w for w in semanal if w["sessoes"] >= 3]
    if len(solidas) >= 2:
        base = solidas[:2]
        atual = solidas[-2:]
        bm = statistics.mean(w["contexto_inicial_mediana"] for w in base)
        am = statistics.mean(w["contexto_inicial_mediana"] for w in atual)
        delta = {
            "semanas_base": [w["semana"] for w in base],
            "semanas_atual": [w["semana"] for w in atual],
            "contexto_base": int(bm),
            "contexto_atual": int(am),
            "variacao_abs": int(bm - am),
            "variacao_pct": round((bm - am) / bm * 100, 1) if bm else 0.0,
            "direcao": "reducao" if am < bm else "aumento",
        }

    caching = {
        "sessoes_com_cache": sum(1 for s in sessions if s["cache_read_total"] > 0),
        "sessoes_total": len(sessions),
        "cache_hit_ratio_medio_trabalho": (
            round(statistics.mean([s["cache_hit_ratio"] for s in trabalho]), 4)
            if trabalho else 0.0
        ),
    }

    return {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "transcripts_dir": transcripts_dir,
        "sessoes_lidas": len(sessions),
        "sessoes_trabalho": len(trabalho),
        "periodo": {
            "de": sessions[0]["data"] if sessions else None,
            "ate": sessions[-1]["data"] if sessions else None,
        },
        "prompt_caching": caching,
        "baseline_vs_atual": delta,
        "semanal": semanal,
        "sessoes": sessions,
    }


def write_report(data, out_md):
    L = []
    P = L.append
    P("# Relatorio de Tokens — MEDICAO REAL")
    P("")
    P(f"**Gerado em:** {data['gerado_em']}  ")
    P(f"**Fonte:** transcripts de sessao do Claude Code (`{data['transcripts_dir']}`)  ")
    P(f"**Sessoes lidas:** {data['sessoes_lidas']} "
      f"(**{data['sessoes_trabalho']}** conversas de trabalho, >= 3 turnos)  ")
    if data["periodo"]["de"]:
        P(f"**Periodo:** {data['periodo']['de']} -> {data['periodo']['ate']}  ")
    P("")
    P("> Todo numero abaixo vem do campo `message.usage` de cada resposta do "
      "assistente. Nao ha projecao nem estimativa multiplicada.")
    P("")

    c = data["prompt_caching"]
    P("## 1. Prompt caching — ja esta ligado?")
    P("")
    P(f"- Sessoes com leitura de cache (`cache_read_input_tokens` > 0): "
      f"**{c['sessoes_com_cache']} / {c['sessoes_total']}**")
    P(f"- Cache hit ratio medio (conversas de trabalho): "
      f"**{c['cache_hit_ratio_medio_trabalho']*100:.1f}%** do contexto de entrada "
      f"vem de cache")
    P("")
    if c["sessoes_com_cache"] > 0:
        P("**Conclusao:** o prompt caching nativo da Anthropic **ja opera** nas "
          "sessoes deste projeto. O Item 7 (\"aguardando API Claude v1.9+\") "
          "descreve um bloqueio que nao existe — o ganho ja esta sendo colhido.")
    else:
        P("**Conclusao:** nenhuma leitura de cache observada.")
    P("")

    d = data["baseline_vs_atual"]
    P("## 2. Contexto inicial por conversa — baseline vs. atual")
    P("")
    if d:
        rotulo = "REDUCAO" if d["direcao"] == "reducao" else "AUMENTO"
        P(f"- Base ({', '.join(d['semanas_base'])}): mediana **{human(d['contexto_base'])}** tokens de contexto inicial")
        P(f"- Atual ({', '.join(d['semanas_atual'])}): mediana **{human(d['contexto_atual'])}** tokens")
        P(f"- Resultado medido: **{rotulo} de {abs(d['variacao_pct']):.1f}%** "
          f"({human(abs(d['variacao_abs']))} tokens)")
        P("")
        if d["direcao"] != "reducao":
            P("> O plano projetava 45-70% de **reducao** de contexto por conversa. "
              "A medicao real mostra o contrario: o contexto inicial nao caiu apos "
              "os slices de CLAUDE.md (30/07) nem a consolidacao de MEMORY.md (29/07).")
    else:
        P("- Dados insuficientes (menos de 2 semanas com conversas de trabalho).")
    P("")

    P("## 3. Evolucao semanal (mediana do contexto inicial)")
    P("")
    P("| Semana | Inicio | Sessoes | Mediana | Media | Min | Max | Cache hit |")
    P("|---|---|--:|--:|--:|--:|--:|--:|")
    for w in data["semanal"]:
        P(f"| {w['semana']} | {w['inicio_semana']} | {w['sessoes']} "
          f"| {human(w['contexto_inicial_mediana'])} | {human(w['contexto_inicial_media'])} "
          f"| {human(w['contexto_inicial_min'])} | {human(w['contexto_inicial_max'])} "
          f"| {w['cache_hit_ratio_medio']*100:.0f}% |")
    P("")
    P("**Marcos do plano de otimizacao (para cruzar com a curva):**")
    for dt, desc in MARCOS:
        P(f"- {dt} — {desc}")
    P("")

    P("## 4. Sessoes (todas, mais recente primeiro)")
    P("")
    P("| Data | Sessao | Br. | Turnos | Ctx inicial | Ctx pico | Saida | Cache read | Custo-eq |")
    P("|---|---|---|--:|--:|--:|--:|--:|--:|")
    for s in reversed(data["sessoes"]):
        sid = s["session_id"][:8]
        br = (s["git_branch"] or "-")
        br = br.split("/")[-1][:14]
        P(f"| {s['data']} | `{sid}` | {br} | {s['turnos_principais']}"
          f"{('+' + str(s['turnos_subagente'])) if s['turnos_subagente'] else ''} "
          f"| {human(s['contexto_inicial'])} | {human(s['contexto_pico'])} "
          f"| {human(s['output_total'])} | {human(s['cache_read_total'])} "
          f"| {human(s['custo_equivalente'])} |")
    P("")
    P("_Custo-eq = input*1 + cache_write*1.25 + cache_read*0.1 + output*5. "
      "Comparavel entre sessoes; nao e fatura._")
    P("")

    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


PANEL_DEFAULT = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "Painel_Fundador", "painel_economia_tokens.html",
))


def write_panel(data, out_html):
    """Painel estatico do Fundador — resolvido ao abrir, sem dado externo."""
    sem = data["semanal"]
    d = data["baseline_vs_atual"]
    c = data["prompt_caching"]
    atual = sem[-1] if sem else None

    maxmed = max((w["contexto_inicial_mediana"] for w in sem), default=1) or 1
    bars = []
    for w in sem:
        h = round(w["contexto_inicial_mediana"] / maxmed * 100)
        bars.append(
            f'<div class="bar"><div class="fill" style="height:{h}%"></div>'
            f'<div class="bl">{w["semana"].split("-")[1]}</div>'
            f'<div class="bv">{w["contexto_inicial_mediana"]//1000}k</div></div>'
        )

    if d and d["direcao"] == "reducao":
        verdito = (f'Contexto por conversa: <b>reducao de {abs(d["variacao_pct"]):.1f}%</b> '
                   f'({human(d["contexto_base"])} &rarr; {human(d["contexto_atual"])} tokens).')
        vclass = "good"
    elif d:
        verdito = (f'Contexto por conversa: <b>sem reducao</b> — {human(d["contexto_base"])} '
                   f'&rarr; {human(d["contexto_atual"])} tokens ({d["variacao_pct"]:+.1f}%). '
                   f'Os slices de CLAUDE.md e a consolidacao de MEMORY.md nao moveram esta curva.')
        vclass = "warn"
    else:
        verdito = "Dados insuficientes."
        vclass = "warn"

    html = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Economia de Tokens STTK</title>
<style>
:root {{
  --paper:#F1EEE6; --surface:#FBFAF5; --ink:#222A2B; --ink-soft:#5B6360;
  --ink-faint:#8A8F88; --line:#E4DFD3; --brand:#2A4A46;
  --good:#3E7A57; --warn:#B57F32;
}}
@media (prefers-color-scheme: dark) {{ :root {{
  --paper:#13171A; --surface:#1B2124; --ink:#EAE6DC; --ink-soft:#9CA39D;
  --ink-faint:#767C77; --line:#2B3336; --brand:#82B4AB;
  --good:#61A67C; --warn:#D3A155;
}} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--paper); color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:15px; line-height:1.5; }}
.wrap {{ max-width:960px; margin:0 auto; padding:32px 24px; }}
h1 {{ font-size:22px; margin:0 0 2px; }}
.sub {{ color:var(--ink-soft); font-size:13px; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
  gap:16px; margin-bottom:24px; }}
.card {{ background:var(--surface); border:1px solid var(--line);
  border-radius:12px; padding:16px 18px; }}
.k {{ font-size:11px; text-transform:uppercase; letter-spacing:.05em;
  color:var(--ink-faint); font-family:"Cascadia Code",monospace; }}
.v {{ font-size:28px; font-weight:600; margin-top:4px; }}
.v small {{ font-size:13px; font-weight:400; color:var(--ink-soft); }}
.verd {{ background:var(--surface); border:1px solid var(--line);
  border-left:3px solid var(--warn); border-radius:8px; padding:14px 16px;
  margin-bottom:24px; font-size:14px; }}
.verd.good {{ border-left-color:var(--good); }}
.chart {{ background:var(--surface); border:1px solid var(--line);
  border-radius:12px; padding:20px 18px 12px; }}
.chart h2 {{ font-size:13px; margin:0 0 16px; color:var(--ink-soft);
  font-weight:600; }}
.bars {{ display:flex; align-items:flex-end; gap:10px; height:150px; }}
.bar {{ flex:1; display:flex; flex-direction:column; align-items:center;
  height:100%; justify-content:flex-end; position:relative; }}
.fill {{ width:100%; max-width:46px; background:var(--brand);
  border-radius:4px 4px 0 0; min-height:2px; }}
.bl {{ font-size:10px; color:var(--ink-faint); margin-top:6px; }}
.bv {{ font-size:10px; color:var(--ink-soft); position:absolute; top:-16px; }}
.foot {{ color:var(--ink-faint); font-size:12px; margin-top:20px; }}
</style></head><body><div class="wrap">
<h1>Economia de Tokens STTK &mdash; medicao real</h1>
<div class="sub">Fonte: {data['sessoes_lidas']} transcripts de sessao ({data['periodo']['de']} &rarr; {data['periodo']['ate']}). Gerado {data['gerado_em']} por <code>medir_tokens.py</code>. Sem projecao.</div>

<div class="grid">
  <div class="card"><div class="k">Contexto inicial / conversa (atual)</div>
    <div class="v">{human(atual['contexto_inicial_mediana']) if atual else '-'} <small>mediana {atual['semana'] if atual else ''}</small></div></div>
  <div class="card"><div class="k">Variacao vs. base (tamanho do contexto)</div>
    <div class="v">{-d['variacao_pct']:+.1f}%<small> &nbsp;{'menor' if d and d['direcao']=='reducao' else 'maior'}</small></div></div>
  <div class="card"><div class="k">Prompt caching</div>
    <div class="v">{c['cache_hit_ratio_medio_trabalho']*100:.0f}%<small> hit &middot; {c['sessoes_com_cache']}/{c['sessoes_total']} sessoes</small></div></div>
  <div class="card"><div class="k">Conversas medidas</div>
    <div class="v">{data['sessoes_trabalho']}<small> &nbsp;&ge;3 turnos</small></div></div>
</div>

<div class="verd {vclass}">{verdito}</div>

<div class="chart"><h2>Mediana do contexto inicial por semana ISO (tokens)</h2>
<div class="bars">{''.join(bars)}</div></div>

<div class="foot">Contexto inicial = input + cache_creation + cache_read do 1o turno real do assistente.
Marcos: 29/07 consolidacao MEMORY.md &middot; 30/07 slices CLAUDE.md &middot; 05/08 estado JSON &middot; 13/08 cache Drive.
Nenhum marco produziu degrau visivel nesta curva &mdash; o unico ganho real de token e o prompt caching, ativo desde sempre.</div>
</div></body></html>"""
    with open(out_html, "w", encoding="utf-8") as fh:
        fh.write(html)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--transcripts", default=DEFAULT_TRANSCRIPTS,
                    help="Pasta com os arquivos .jsonl de sessao")
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--panel", default=PANEL_DEFAULT,
                    help="Caminho do painel HTML a (re)gerar; vazio para pular")
    args = ap.parse_args()

    tdir = os.path.abspath(os.path.expanduser(args.transcripts))
    if not os.path.isdir(tdir):
        raise SystemExit(f"Pasta de transcripts nao encontrada: {tdir}")

    data = build(tdir)

    out_json = os.path.join(args.outdir, "token_metrics.json")
    out_md = os.path.join(args.outdir, "RELATORIO_TOKENS.md")
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    write_report(data, out_md)

    if args.panel:
        write_panel(data, args.panel)
        print(f"Escrito: {args.panel}")

    print(f"Sessoes lidas         : {data['sessoes_lidas']}")
    print(f"Conversas de trabalho : {data['sessoes_trabalho']}")
    if data["periodo"]["de"]:
        print(f"Periodo               : {data['periodo']['de']} -> {data['periodo']['ate']}")
    c = data["prompt_caching"]
    print(f"Sessoes com cache     : {c['sessoes_com_cache']}/{c['sessoes_total']} "
          f"(hit medio {c['cache_hit_ratio_medio_trabalho']*100:.1f}%)")
    d = data["baseline_vs_atual"]
    if d:
        print(f"Contexto inicial      : {d['contexto_base']} -> {d['contexto_atual']} "
              f"({d['direcao'].upper()} {abs(d['variacao_pct']):.1f}%)  "
              f"[{'+'.join(d['semanas_base'])} -> {'+'.join(d['semanas_atual'])}]")
    print(f"\nEscrito: {out_json}")
    print(f"Escrito: {out_md}")


if __name__ == "__main__":
    main()
