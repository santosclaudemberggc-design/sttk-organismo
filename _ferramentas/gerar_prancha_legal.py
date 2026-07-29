#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gerar_prancha_legal.py — Motor de compilacao de prancha de PROJETO LEGAL (PDF).

Organismo STTK / Sttickler Empreendimentos.
Autor: Hely (Agente Executor do Projeto Legal, equipe de Kelsen).
Criado em 21/07/2026 sob determinacao de Claudemberg via Wallenberg -> Kelsen.

O QUE ESTE SCRIPT E:
    Um motor de desenho de prancha. Ele NAO conhece nenhum caso.
    Todos os dados do caso vem de um arquivo JSON externo (--caso).

O QUE ESTE SCRIPT NAO E:
    Nao e um gerador de projeto. Ele nao desenha geometria de arquitetura.
    Onde deveria haver desenho vindo do Anteprojeto, ele carimba um
    PLACEHOLDER explicito. Preencher geometria por conta propria e proibido
    (identidade do Hely; Principio 8 - Rastreabilidade).

REGRA DURA IMPLEMENTADA NO MOTOR:
    Todo valor ou e REAL com fonte rastravel, ou e PENDENTE declarado.
    Nao existe caminho de codigo que estime, arredonde ou complete um numero.
    Celula sem valor sai como "PENDENTE" com destaque visual, nunca vazia.

USO:
    python gerar_prancha_legal.py --caso caso.json --saida prancha.pdf

FORMATO DA FOLHA:
    Parametrizado no JSON (chave "formato"): A0..A4, orientacao paisagem.
    Base normativa: ABNT NBR 10068 (folha de desenho - leiaute e dimensoes).
    O Decreto Rio 55.622/2025 (LICIN 2.0) NAO fixa formato de prancha
    (verificado por varredura de texto integral em 21/07/2026: nenhuma
    ocorrencia de "formato", "escala", "A1", "A0", "ABNT" ou "NBR").
"""

import argparse
import json
import sys
from datetime import date

from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------------------------------------------------------------------
# FORMATOS DE FOLHA — ABNT NBR 10068, serie A, orientacao paisagem (mm)
# ---------------------------------------------------------------------------
FORMATOS = {
    "A0": (1189, 841),
    "A1": (841, 594),
    "A2": (594, 420),
    "A3": (420, 297),
    "A4": (297, 210),
}

# Margens NBR 10068: margem esquerda maior (arquivamento/encadernacao)
MARG_ESQ = 25.0
MARG_OUT = 10.0

# Legenda (carimbo) NBR 10068: largura maxima 175 mm para A0-A2
CARIMBO_W = 175.0
CARIMBO_H = 62.0

# Escala tipografica por formato. Uma prancha A1 lida a 1 m de distancia exige
# corpo maior que uma folha A4 lida na mao; sem isso o texto "afoga" na folha.
ESCALA_TIPO = {"A0": 1.85, "A1": 1.50, "A2": 1.15, "A3": 1.00, "A4": 0.85}
S = 1.0  # definido em tempo de execucao por _set_escala()


def _set_escala(formato):
    global S
    S = ESCALA_TIPO.get(formato, 1.0)
    return S

# Paleta
C_LINHA = colors.HexColor("#1A1A1A")
C_TEXTO = colors.HexColor("#111111")
C_FRACO = colors.HexColor("#666666")
C_PEND = colors.HexColor("#B45309")   # ambar — pendencia
C_ALERTA = colors.HexColor("#B91C1C")  # vermelho — nao conformidade
C_FUNDO_PEND = colors.HexColor("#FEF3C7")
C_FUNDO_ALERTA = colors.HexColor("#FEE2E2")
C_FUNDO_CAB = colors.HexColor("#E5E7EB")
C_MARCA = colors.Color(0.85, 0.20, 0.20, alpha=0.13)
C_PLACEHOLDER = colors.HexColor("#9CA3AF")
C_FUNDO_PH = colors.HexColor("#F3F4F6")

# Marcador textual de pendencia usado no JSON do caso
TOKEN_PENDENTE = "PENDENTE"


# ---------------------------------------------------------------------------
# Utilitarios de texto
# ---------------------------------------------------------------------------
def _limpa(txt):
    """Helvetica base do reportlab e latin-1. Troca o que nao couber."""
    if txt is None:
        return ""
    txt = str(txt)
    subs = {
        "—": "-", "–": "-", "‘": "'", "’": "'",
        "“": '"', "”": '"', "…": "...", "→": "->",
        "×": "x", "≥": ">=", "≤": "<=", "²": "2",
        "•": "-", "●": "-", "◦": "-", "⚠": "!",
        "✓": "OK", "✗": "X", " ": " ",
    }
    for k, v in subs.items():
        txt = txt.replace(k, v)
    return txt.encode("latin-1", "replace").decode("latin-1")


def quebra(texto, fonte, tam, larg_mm):
    """Quebra texto em linhas que cabem em larg_mm."""
    texto = _limpa(texto)
    larg = larg_mm * mm
    linhas = []
    for bruto in texto.split("\n"):
        palavras = bruto.split()
        if not palavras:
            linhas.append("")
            continue
        atual = palavras[0]
        for p in palavras[1:]:
            if stringWidth(atual + " " + p, fonte, tam) <= larg:
                atual += " " + p
            else:
                linhas.append(atual)
                atual = p
        linhas.append(atual)
    return linhas


def texto_bloco(c, x, y, texto, fonte="Helvetica", tam=8, larg=100,
                lead=None, cor=C_TEXTO):
    """Desenha texto com quebra automatica. 'tam' e o corpo base (A3=1,0);
    a escala do formato e aplicada aqui. Retorna o y final (mm)."""
    tam = tam * S
    # lead em MILIMETROS. Se nao informado, 1,30 x corpo.
    lead_mm = (lead * S) if lead else (tam * 1.30 / mm)
    c.setFillColor(cor)
    c.setFont(fonte, tam)
    yy = y
    for ln in quebra(texto, fonte, tam, larg):
        c.drawString(x * mm, yy * mm, ln)
        yy -= lead_mm
    return yy


def eh_pendente(valor):
    return isinstance(valor, str) and TOKEN_PENDENTE in valor.upper()


# ---------------------------------------------------------------------------
# Elementos fixos da folha
# ---------------------------------------------------------------------------
def moldura(c, W, H):
    c.setStrokeColor(C_LINHA)
    c.setLineWidth(1.6)
    c.rect(MARG_ESQ * mm, MARG_OUT * mm,
           (W - MARG_ESQ - MARG_OUT) * mm, (H - 2 * MARG_OUT) * mm)


def marca_dagua(c, W, H, texto):
    """Marca d'agua diagonal, atravessando a folha, translucida."""
    c.saveState()
    c.translate(W / 2 * mm, H / 2 * mm)
    c.rotate(30)
    c.setFillColor(C_MARCA)
    tam = 46 if W > 700 else 30
    c.setFont("Helvetica-Bold", tam)
    t = _limpa(texto)
    c.drawCentredString(0, -tam * 0.35, t)
    c.setFont("Helvetica-Bold", tam * 0.55)
    c.drawCentredString(0, -tam * 1.45, t)
    c.drawCentredString(0, tam * 0.90, t)
    c.restoreState()


def carimbo(c, W, H, caso, folha_num, folha_total, titulo_folha, escala):
    """Selo/carimbo NBR 10068 — canto inferior direito, todas as folhas."""
    x = W - MARG_OUT - CARIMBO_W
    y = MARG_OUT
    c.setStrokeColor(C_LINHA)
    c.setLineWidth(1.2)
    c.rect(x * mm, y * mm, CARIMBO_W * mm, CARIMBO_H * mm)

    def linha_h(dy):
        c.setLineWidth(0.5)
        c.line(x * mm, (y + dy) * mm, (x + CARIMBO_W) * mm, (y + dy) * mm)

    def linha_v(dx, y0, y1):
        c.setLineWidth(0.5)
        c.line((x + dx) * mm, (y + y0) * mm, (x + dx) * mm, (y + y1) * mm)

    def campo(dx, dy, rotulo, valor, larg, tam=6.4, cor=None):
        c.setFillColor(C_FRACO)
        c.setFont("Helvetica", 4.6)
        c.drawString((x + dx + 1.5) * mm, (y + dy + 5.6) * mm, _limpa(rotulo))
        pend = eh_pendente(valor)
        fonte = "Helvetica-Bold" if pend else "Helvetica"
        v = _limpa(valor)
        while stringWidth(v, fonte, tam) > (larg - 3) * mm and tam > 4.0:
            tam -= 0.15
        # trava dura: nenhum campo do carimbo pode invadir o vizinho
        c.saveState()
        pth = c.beginPath()
        pth.rect((x + dx) * mm, (y + dy) * mm, larg * mm, 10 * mm)
        c.clipPath(pth, stroke=0)
        c.setFillColor(cor or (C_PEND if pend else C_TEXTO))
        c.setFont(fonte, tam)
        c.drawString((x + dx + 1.5) * mm, (y + dy + 1.6) * mm, v)
        c.restoreState()

    # faixa superior: identificacao da obra
    linha_h(54)
    linha_h(44)
    linha_h(34)
    linha_h(24)
    linha_h(12)

    c.setFillColor(C_TEXTO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString((x + 2) * mm, (y + 56.5) * mm,
                 _limpa(caso.get("escritorio", "STTICKLER EMPREENDIMENTOS")))
    c.setFont("Helvetica", 5.6)
    c.setFillColor(C_FRACO)
    c.drawRightString((x + CARIMBO_W - 2) * mm, (y + 56.5) * mm,
                      _limpa(caso.get("escritorio_cnpj", "")))

    campo(0, 44, "OBRA / EMPREENDIMENTO", caso.get("obra"), CARIMBO_W)
    campo(0, 34, "ENDERECO DA OBRA", caso.get("endereco"), CARIMBO_W)

    linha_v(88, 24, 34)
    campo(0, 24, "LOTE / CL / MATRICULA RGI", caso.get("lote_matricula"), 88)
    campo(88, 24, "PROPRIETARIO / REQUERENTE", caso.get("requerente"),
          CARIMBO_W - 88)

    linha_v(60, 12, 24)
    linha_v(118, 12, 24)
    campo(0, 12, "TIPO DE PROJETO", caso.get("tipo_projeto"), 60)
    campo(60, 12, "RESPONSAVEL TECNICO (PRPA)", caso.get("prpa"), 58)
    campo(118, 12, "RRT / ART", caso.get("rrt"), CARIMBO_W - 118)

    linha_v(38, 0, 12)
    linha_v(76, 0, 12)
    linha_v(110, 0, 12)
    linha_v(140, 0, 12)
    campo(0, 0, "TITULO DA FOLHA", titulo_folha, 38, tam=5.6)
    campo(38, 0, "DATA", caso.get("data"), 38, tam=6.4)
    campo(76, 0, "ESCALA", escala, 34, tam=6.4)
    campo(110, 0, "REVISAO", caso.get("revisao"), 30, tam=6.4)
    c.setFillColor(C_FRACO)
    c.setFont("Helvetica", 4.6)
    c.drawString((x + 141.5) * mm, (y + 5.6) * mm, "PRANCHA")
    c.setFillColor(C_TEXTO)
    c.setFont("Helvetica-Bold", 11)
    c.drawString((x + 141.5) * mm, (y + 1.2) * mm,
                 "%02d/%02d" % (folha_num, folha_total))


def cabecalho(c, W, H, titulo, subtitulo=""):
    top = H - MARG_OUT
    c.setFillColor(C_TEXTO)
    c.setFont("Helvetica-Bold", 13 * S)
    c.drawString((MARG_ESQ + 4) * mm, (top - 10 * S) * mm, _limpa(titulo))
    if subtitulo:
        c.setFillColor(C_FRACO)
        c.setFont("Helvetica", 7.5 * S)
        c.drawString((MARG_ESQ + 4) * mm, (top - 15.5 * S) * mm, _limpa(subtitulo))
    c.setStrokeColor(C_LINHA)
    c.setLineWidth(0.8)
    c.line((MARG_ESQ + 4) * mm, (top - 18.5 * S) * mm,
           (W - MARG_OUT - 4) * mm, (top - 18.5 * S) * mm)
    return top - 24.0 * S


# ---------------------------------------------------------------------------
# Blocos de conteudo
# ---------------------------------------------------------------------------
def placeholder(c, x, y, w, h, titulo, escala="", nota=""):
    """Quadro de desenho NAO EXECUTADO — carimbado dentro do proprio quadro."""
    c.setFillColor(C_FUNDO_PH)
    c.setStrokeColor(C_PLACEHOLDER)
    c.setLineWidth(1.0)
    c.rect(x * mm, y * mm, w * mm, h * mm, stroke=1, fill=1)

    # hachura diagonal leve
    c.saveState()
    p = c.beginPath()
    p.rect(x * mm, y * mm, w * mm, h * mm)
    c.clipPath(p, stroke=0)
    c.setStrokeColor(colors.HexColor("#DDE1E6"))
    c.setLineWidth(0.6)
    passo = 7
    i = 0
    while i < (w + h) / passo:
        d = i * passo
        c.line((x + d) * mm, y * mm, x * mm, (y + d) * mm)
        i += 1
    c.restoreState()

    cx = x + w / 2
    t_tit, t_sel, t_esc, t_nota = 9 * S, 8.2 * S, 6.5 * S, 6.4 * S
    fw = min(w - 8, 108.0 * S)
    fh = 11.0 * S
    fx = cx - fw / 2

    # nota primeiro (para centrar o conjunto verticalmente)
    linhas_nota = quebra(nota, "Helvetica", t_nota, w - 12) if nota else []
    lead_nota = t_nota * 1.34 / mm
    alt_conj = (t_tit * 1.6 / mm) + fh + 2 + (t_esc * 2.0 / mm if escala else 0) \
        + len(linhas_nota) * lead_nota
    topo = y + h / 2 + alt_conj / 2

    c.setFillColor(C_TEXTO)
    c.setFont("Helvetica-Bold", t_tit)
    c.drawCentredString(cx * mm, topo * mm, _limpa(titulo))

    # selo obrigatorio dentro do proprio quadro de desenho
    fy = topo - (t_tit * 1.6 / mm) - fh
    c.setFillColor(C_FUNDO_ALERTA)
    c.setStrokeColor(C_ALERTA)
    c.setLineWidth(1.2)
    c.rect(fx * mm, fy * mm, fw * mm, fh * mm, stroke=1, fill=1)
    c.setFillColor(C_ALERTA)
    c.setFont("Helvetica-Bold", t_sel)
    c.drawCentredString(cx * mm, (fy + fh / 2 - t_sel * 0.36 / mm) * mm,
                        "DESENHO PLACEHOLDER - NAO E PROJETO REAL")

    yy = fy - 2 - t_esc * 1.1 / mm
    if escala:
        c.setFillColor(C_FRACO)
        c.setFont("Helvetica", t_esc)
        c.drawCentredString(cx * mm, yy * mm, _limpa("Escala prevista: " + escala))
        yy -= t_esc * 1.9 / mm
    c.setFillColor(C_PEND)
    c.setFont("Helvetica", t_nota)
    for ln in linhas_nota:
        c.drawCentredString(cx * mm, yy * mm, ln)
        yy -= lead_nota

    # etiqueta de origem
    c.setFillColor(C_FRACO)
    c.setFont("Helvetica-Oblique", 5.8 * S)
    c.drawString((x + 2) * mm, (y + 2) * mm,
                 "Origem exigida: Anteprojeto aprovado (nao fornecido a esta compilacao)")


def tabela(c, x, y, larguras, linhas, tam=7.0, alt_lin=6.2, cabecalho_=True):
    """Tabela simples. Celula com 'PENDENTE' recebe destaque ambar.
    Retorna y final (mm)."""
    tam = tam * S
    alt_lin = alt_lin * S
    larg_total = sum(larguras)
    yy = y
    for i, linha in enumerate(linhas):
        is_cab = cabecalho_ and i == 0
        # altura da linha conforme a celula que exigir mais linhas
        n = 1
        for j, cel in enumerate(linha):
            n = max(n, len(quebra(str(cel), "Helvetica", tam, larguras[j] - 3)))
        h = max(alt_lin, n * (tam * 1.30) / mm + 2.4 * S)

        tem_pend = any(eh_pendente(cel) for cel in linha)
        if is_cab:
            c.setFillColor(C_FUNDO_CAB)
        elif tem_pend:
            c.setFillColor(C_FUNDO_PEND)
        else:
            c.setFillColor(colors.white)
        c.setStrokeColor(C_LINHA)
        c.setLineWidth(0.5)
        c.rect(x * mm, (yy - h) * mm, larg_total * mm, h * mm, stroke=1, fill=1)

        cx = x
        for j, cel in enumerate(linha):
            if j > 0:
                c.setLineWidth(0.4)
                c.line(cx * mm, (yy - h) * mm, cx * mm, yy * mm)
            pend = eh_pendente(cel)
            if is_cab:
                c.setFillColor(C_TEXTO)
                fonte = "Helvetica-Bold"
            elif pend:
                c.setFillColor(C_PEND)
                fonte = "Helvetica-Bold"
            else:
                c.setFillColor(C_TEXTO)
                fonte = "Helvetica"
            c.setFont(fonte, tam)
            ty = yy - tam * 1.05 / mm - 0.4
            for ln in quebra(str(cel), fonte, tam, larguras[j] - 3):
                c.drawString((cx + 1.5) * mm, ty * mm, ln)
                ty -= (tam * 1.30) / mm
            cx += larguras[j]
        yy -= h
    return yy


def bloco_alerta(c, x, y, w, titulo, paragrafos, itens=None, altura=None):
    """Bloco de NAO CONFORMIDADE — moldura grossa, alta visibilidade."""
    itens = itens or []
    t_par, t_item, t_tit = 8.5 * S, 7.6 * S, 10.5 * S
    lead_par = t_par * 1.32 / mm
    lead_item = t_item * 1.34 / mm
    faixa = 9.0 * S

    # altura necessaria, medida de verdade (nao estimada)
    h = faixa + 4.5 * S
    for p in paragrafos:
        h += len(quebra(p, "Helvetica-Bold", t_par, w - 6)) * lead_par + 1.2
    if itens:
        h += 1.5
        for it in itens:
            h += len(quebra("- " + it, "Helvetica-Bold", t_item, w - 8)) * lead_item
    h = altura or (h + 4.0 * S)

    c.setFillColor(C_FUNDO_ALERTA)
    c.setStrokeColor(C_ALERTA)
    c.setLineWidth(2.4)
    c.rect(x * mm, (y - h) * mm, w * mm, h * mm, stroke=1, fill=1)

    c.setFillColor(C_ALERTA)
    c.rect(x * mm, (y - faixa) * mm, w * mm, faixa * mm, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", t_tit)
    c.drawString((x + 3) * mm, (y - faixa + 2.2 * S) * mm, _limpa(titulo))

    yy = y - faixa - lead_par
    for p in paragrafos:
        yy = texto_bloco(c, x + 3, yy, p, "Helvetica-Bold", 8.5,
                         w - 6, lead=t_par * 1.32 / mm / S, cor=C_ALERTA)
        yy -= 1.2
    if itens:
        yy -= 1.5
        c.setFillColor(C_ALERTA)
        c.setFont("Helvetica-Bold", t_item)
        for it in itens:
            for ln in quebra("- " + it, "Helvetica-Bold", t_item, w - 8):
                c.drawString((x + 4) * mm, yy * mm, ln)
                yy -= lead_item
    return y - h


def bloco_pendencia(c, x, y, w, titulo, itens):
    t_tit, t_it = 8.6 * S, 7.2 * S
    lead = t_it * 1.34 / mm
    linhas_tot = []
    for it in itens:
        linhas_tot += quebra("- " + it, "Helvetica", t_it, w - 8)
    h = (t_tit * 1.5 / mm) + 3.0 * S + len(linhas_tot) * lead + 2.5 * S
    c.setFillColor(C_FUNDO_PEND)
    c.setStrokeColor(C_PEND)
    c.setLineWidth(1.4)
    c.rect(x * mm, (y - h) * mm, w * mm, h * mm, stroke=1, fill=1)
    c.setFillColor(C_PEND)
    c.setFont("Helvetica-Bold", t_tit)
    c.drawString((x + 3) * mm, (y - t_tit * 1.15 / mm) * mm, _limpa(titulo))
    yy = y - (t_tit * 1.5 / mm) - 2.0 * S - lead * 0.4
    c.setFont("Helvetica", t_it)
    for ln in linhas_tot:
        c.drawString((x + 3.5) * mm, yy * mm, ln)
        yy -= lead
    return y - h


def nota_fonte(c, x, y, w, texto):
    t = 6.2 * S
    lead = t * 1.34 / mm
    c.setFillColor(C_FRACO)
    c.setFont("Helvetica-Oblique", t)
    yy = y
    for ln in quebra(texto, "Helvetica-Oblique", t, w):
        c.drawString(x * mm, yy * mm, ln)
        yy -= lead
    return yy


# ---------------------------------------------------------------------------
# Montagem das folhas
# ---------------------------------------------------------------------------
class Prancha(object):
    def __init__(self, caso, saida):
        self.caso = caso
        fmt = caso.get("formato", "A1")
        self.W, self.H = FORMATOS[fmt]
        self.fmt = fmt
        _set_escala(fmt)
        self.c = rl_canvas.Canvas(saida, pagesize=(self.W * mm, self.H * mm))
        self.c.setTitle(_limpa(caso.get("obra", "Projeto Legal")))
        self.c.setAuthor("Hely - Agente Executor do Projeto Legal (Organismo STTK)")
        self.c.setSubject("Projeto Legal - compilacao de prancha - MATERIAL DE TESTE")
        self.folhas = []          # funcoes de desenho
        self.titulos = []
        self.escalas = []

    # area util interna (abaixo do cabecalho, acima do carimbo)
    @property
    def ux(self):
        return MARG_ESQ + 4

    @property
    def uw(self):
        return self.W - MARG_ESQ - MARG_OUT - 8

    @property
    def uy_base(self):
        return MARG_OUT + CARIMBO_H + 6

    @property
    def uw_sem_carimbo(self):
        """Largura utilizavel a ESQUERDA do carimbo. Qualquer bloco desenhado
        na faixa inferior da folha tem de usar esta largura, nao 'uw' —
        senao invade a legenda (defeito observado na folha de fachadas)."""
        return (self.W - MARG_OUT - CARIMBO_W) - self.ux - 4

    def add(self, titulo, escala, fn):
        self.folhas.append(fn)
        self.titulos.append(titulo)
        self.escalas.append(escala)

    def render(self):
        total = len(self.folhas)
        for i, fn in enumerate(self.folhas):
            c = self.c
            moldura(c, self.W, self.H)
            y = cabecalho(c, self.W, self.H, self.titulos[i],
                          self.caso.get("subtitulo_folha", ""))
            fn(c, y)
            carimbo(c, self.W, self.H, self.caso, i + 1, total,
                    self.titulos[i], self.escalas[i])
            # marca d'agua POR CIMA de tudo: se desenhada por baixo, os
            # placeholders e as tabelas (que tem preenchimento opaco) a
            # recortam e ela deixa de atravessar a folha.
            marca_dagua(c, self.W, self.H, self.caso.get("marca_dagua", "TESTE"))
            c.showPage()
        self.c.save()
        return total


def montar(caso, saida):
    p = Prancha(caso, saida)
    W, H = p.W, p.H
    d = caso

    # --- Folha 1: Capa / indice / situacao / quadro do lote -----------------
    def f01(c, y):
        col_w = p.uw * 0.46
        # coluna esquerda: identificacao + indice
        yy = y
        yy = texto_bloco(c, p.ux, yy, d["obra"], "Helvetica-Bold", 15, col_w)
        yy -= 2
        yy = texto_bloco(c, p.ux, yy, d["endereco"], "Helvetica", 9, col_w)
        yy = texto_bloco(c, p.ux, yy,
                         "Requerente: " + d["requerente"], "Helvetica", 9, col_w)
        yy = texto_bloco(c, p.ux, yy,
                         "Lote/CL/Matricula: " + d["lote_matricula"],
                         "Helvetica", 9, col_w)
        yy -= 6

        yy = texto_bloco(c, p.ux, yy, "DADOS DO LOTE E DO EMPREENDIMENTO",
                         "Helvetica-Bold", 9, col_w)
        yy -= 2
        yy = tabela(c, p.ux, yy, [col_w * 0.42, col_w * 0.33, col_w * 0.25],
                    d["quadro_lote"], tam=7.0)
        yy -= 3
        yy = nota_fonte(c, p.ux, yy, col_w,
                        "Quadro exigido pelo Decreto Rio 55.622/2025, Anexo I, "
                        "III, 'QUADRO DE AREAS', item 1: a prancha que inclui a "
                        "planta de situacao deve possuir quadro com dados do "
                        "lote, informacoes do empreendimento e parametrizacao "
                        "urbanistica conforme modelo padrao do DULI.")
        yy -= 6
        yy = texto_bloco(c, p.ux, yy, "INDICE DE FOLHAS", "Helvetica-Bold", 9, col_w)
        yy -= 2
        idx = [["Folha", "Conteudo"]]
        for i, t in enumerate(p.titulos):
            idx.append(["%02d/%02d" % (i + 1, len(p.titulos)), t])
        tabela(c, p.ux, yy, [col_w * 0.18, col_w * 0.82], idx, tam=6.8, alt_lin=5.2)

        # coluna direita: placeholder da planta de situacao
        px = p.ux + p.uw * 0.50
        pw = p.uw * 0.50
        ph = y - p.uy_base
        placeholder(c, px, p.uy_base, pw, ph,
                    "PLANTA DE SITUACAO DO LOTE",
                    d["escalas"]["situacao"],
                    "Conteudo exigido (Decreto 55.622/2025, Anexo I, III): "
                    "dimensoes do terreno conforme titulo averbado; alinhamento "
                    "e n. do PAA; afastamento frontal e limite de profundidade; "
                    "imoveis confrontantes; projecoes com cotas de todos os "
                    "afastamentos; RN do meio-fio e curvas de nivel; acessos. "
                    "NENHUM desses dados geometricos foi fornecido.")

    p.add("CAPA, ÍNDICE E PLANTA DE SITUAÇÃO", d["escalas"]["situacao"], f01)

    # --- Folha 2: NAO CONFORMIDADE + parametros urbanisticos ---------------
    def f02(c, y):
        col = p.uw * 0.49
        # bloco de alerta ocupa a coluna esquerda inteira, no topo
        yy = bloco_alerta(c, p.ux, y, col,
                          d["nao_conformidade"]["titulo"],
                          d["nao_conformidade"]["paragrafos"],
                          d["nao_conformidade"]["bloqueantes"])
        yy -= 5
        yy = nota_fonte(c, p.ux, yy, col, d["nao_conformidade"]["fonte"])
        yy -= 4
        bloco_pendencia(c, p.ux, yy, col,
                        "INSTRUMENTOS VERIFICADOS QUE NAO SOCORREM ESTE CASO",
                        d["nao_conformidade"]["instrumentos_afastados"])

        # coluna direita: quadro de parametros urbanisticos (POP 7.1)
        px = p.ux + p.uw * 0.51
        yy2 = texto_bloco(c, px, y, "QUADRO DE PARAMETROS URBANISTICOS",
                          "Helvetica-Bold", 10, col)
        yy2 = texto_bloco(c, px, yy2,
                          "Indicacao exigida pela Secao 7.1 do POP-ARQ-PL-01 "
                          "(POP - PROJETO LEGAL / ARQUITETURA).",
                          "Helvetica-Oblique", 6.5, col)
        yy2 -= 3
        yy2 = tabela(c, px, yy2,
                     [col * 0.30, col * 0.16, col * 0.16, col * 0.14, col * 0.24],
                     d["quadro_parametros"], tam=6.8)
        yy2 -= 4
        nota_fonte(c, px, yy2, col, d["fonte_parametros"])

    p.add("PARÂMETROS URBANÍSTICOS E NÃO CONFORMIDADE", "S/ESC", f02)

    # --- Folha 3: implantacao legal ----------------------------------------
    def f03(c, y):
        pw = p.uw * 0.62
        placeholder(c, p.ux, p.uy_base, pw, y - p.uy_base,
                    "IMPLANTACAO LEGAL", d["escalas"]["implantacao"],
                    "Exige a geometria do Anteprojeto: projecao da edificacao "
                    "cotada, afastamentos frontal/laterais/fundos em relacao a "
                    "todas as divisas, PVs e PVIs, acessos de pedestres e "
                    "veiculos, indicacao da edificacao a demolir.")
        px = p.ux + pw + 6
        cw = p.uw - pw - 6
        yy = texto_bloco(c, px, y, "AMARRACOES LEGAIS DA IMPLANTACAO",
                         "Helvetica-Bold", 9, cw)
        yy -= 2
        yy = tabela(c, px, yy, [cw * 0.42, cw * 0.29, cw * 0.29],
                    d["quadro_implantacao"], tam=6.8)
        yy -= 5
        yy = bloco_pendencia(c, px, yy, cw, "DEMOLICAO - PROCEDIMENTO NAO CONFIRMADO",
                             d["pendencia_demolicao"])
        yy -= 4
        nota_fonte(c, px, yy, cw, d["nota_cores"])

    p.add("IMPLANTAÇÃO LEGAL", d["escalas"]["implantacao"], f03)

    # --- Folhas 4 e 5: plantas dos pavimentos ------------------------------
    def faz_folha_plantas(par):
        def fn(c, y):
            gap = 6.0
            pw = (p.uw - gap) / 2.0
            ph = y - p.uy_base - 26
            for k, pav in enumerate(par):
                placeholder(c, p.ux + k * (pw + gap), p.uy_base + 26, pw, ph,
                            "PLANTA LEGAL - " + pav["nome"],
                            d["escalas"]["plantas"], pav["nota"])
            yy = p.uy_base + 22
            texto_bloco(c, p.ux, yy,
                        "Conteudo exigido de cada planta (Decreto 55.622/2025, "
                        "Anexo I, III, 'PLANTAS DOS PAVIMENTOS'): limite do lote; "
                        "perimetro do pavimento cotado; perimetro da area sujeita "
                        "a calculo de ATE; projecao do pavimento imediatamente "
                        "superior; demonstrativo de area de ATC, ATE, varandas e "
                        "terracos descobertos; quadro descritivo do pavimento "
                        "conforme modelo padrao do DULI, com a ocupacao descrita "
                        "pelos tipos previstos (salas, vagas, partes comuns, area "
                        "tecnica etc.). Nenhum desses dados foi fornecido a esta "
                        "compilacao - area por pavimento consta como PENDENTE no "
                        "quadro de areas.", "Helvetica", 6.6, p.uw)
        return fn

    pavs = d["pavimentos"]
    p.add("PLANTAS LEGAIS - SUBSOLO E TÉRREO", d["escalas"]["plantas"],
          faz_folha_plantas(pavs[0:2]))
    p.add("PLANTAS LEGAIS - PAVIMENTOS 1 E 2", d["escalas"]["plantas"],
          faz_folha_plantas(pavs[2:4]))

    # --- Folha 6: cortes ---------------------------------------------------
    def f06(c, y):
        gap = 6.0
        pw = (p.uw - gap) / 2.0
        ph = y - p.uy_base - 30
        for k, ct in enumerate(d["cortes"]):
            placeholder(c, p.ux + k * (pw + gap), p.uy_base + 30, pw, ph,
                        ct["nome"], d["escalas"]["cortes"], ct["nota"])
        yy = p.uy_base + 26
        texto_bloco(c, p.ux, yy,
                    "Conteudo exigido de cada corte (Decreto 55.622/2025, Anexo I, "
                    "III, 'CORTES'): altura total da edificacao, altura do "
                    "embasamento e da lamina para efeito do calculo dos "
                    "afastamentos conforme o COES; altura entre pisos ate o topo "
                    "da ultima laje; perfil natural do terreno; nivel do meio-fio "
                    "e cota de soleira; desnivel do subsolo aflorado no ponto de "
                    "maior aflora; cotas de cortes e aterros; quadro descritivo "
                    "das unidades e vagas de cada pavimento representado.",
                    "Helvetica", 6.6, p.uw)

    p.add("CORTES LEGAIS", d["escalas"]["cortes"], f06)

    # --- Folha 7: fachadas -------------------------------------------------
    def f07(c, y):
        gap = 6.0
        pw = (p.uw - gap) / 2.0
        ph = y - p.uy_base - 34
        for k, fc in enumerate(d["fachadas"]):
            placeholder(c, p.ux + k * (pw + gap), p.uy_base + 34, pw, ph,
                        fc["nome"], d["escalas"]["fachadas"], fc["nota"])
        yy = p.uy_base + 30
        bloco_alerta(c, p.ux, yy, p.uw_sem_carimbo,
                     d["divergencia_fachada"]["titulo"],
                     d["divergencia_fachada"]["paragrafos"], [])

    p.add("FACHADAS LEGAIS", d["escalas"]["fachadas"], f07)

    # --- Folha 8: quadro de areas Anexo III + termo ------------------------
    def f08(c, y):
        col = p.uw * 0.60
        yy = texto_bloco(c, p.ux, y, d["quadro_areas"]["titulo"],
                         "Helvetica-Bold", 11, col)
        yy = texto_bloco(c, p.ux, yy, d["quadro_areas"]["subtitulo"],
                         "Helvetica-Oblique", 6.8, col)
        yy -= 3
        yy = tabela(c, p.ux, yy,
                    [col * 0.22, col * 0.34, col * 0.16, col * 0.28],
                    d["quadro_areas"]["linhas"], tam=7.0)
        yy -= 4
        yy = nota_fonte(c, p.ux, yy, col, d["quadro_areas"]["fonte"])
        yy -= 4
        bloco_pendencia(c, p.ux, yy, col,
                        "SUBTABELA DO ANEXO III NAO DEFINIDA",
                        d["quadro_areas"]["pendencia_subtabela"])

        # coluna direita: termo de responsabilidade (texto literal do decreto)
        px = p.ux + col + 8
        cw = p.uw - col - 8
        yy2 = texto_bloco(c, px, y, "TERMO DE RESPONSABILIDADE",
                          "Helvetica-Bold", 10, cw)
        yy2 -= 2
        yy2 = texto_bloco(c, px, yy2, d["termo_responsabilidade"],
                          "Helvetica", 7.4, cw)
        yy2 -= 10
        for rot in ["PROPRIETARIO OU ADQUIRENTE", "AUTOR DO PROJETO"]:
            c.setStrokeColor(C_LINHA)
            c.setLineWidth(0.6)
            c.line(px * mm, yy2 * mm, (px + cw * 0.75) * mm, yy2 * mm)
            c.setFillColor(C_FRACO)
            c.setFont("Helvetica", 6.8)
            c.drawString(px * mm, (yy2 - 4) * mm, rot)
            yy2 -= 16
        yy2 -= 2
        bloco_pendencia(c, px, yy2, cw, "ASSINATURAS",
                        d["pendencia_assinaturas"])

    p.add("QUADRO DE ÁREAS LEGAL (ANEXO III) E TERMO", "S/ESC", f08)

    # --- Folha 9: memorial descritivo --------------------------------------
    def f09(c, y):
        gap = 8.0
        cw = (p.uw - gap) / 2.0
        yy = y
        col = 0
        px = p.ux
        for sec in d["memorial"]:
            precisa = 5.0 + len(quebra(sec["texto"], "Helvetica", 7.4, cw)) * 3.3
            if yy - precisa < p.uy_base and col == 0:
                col = 1
                px = p.ux + cw + gap
                yy = y
            yy = texto_bloco(c, px, yy, sec["titulo"], "Helvetica-Bold", 8.4, cw)
            yy -= 0.5
            yy = texto_bloco(c, px, yy, sec["texto"], "Helvetica", 7.4, cw,
                             lead=3.3)
            yy -= 3.5

    p.add("MEMORIAL DESCRITIVO - PROJETO LEGAL", "S/ESC", f09)

    # --- Folha 10: pendencias e responsaveis tecnicos ----------------------
    def f10(c, y):
        col = p.uw * 0.58
        yy = texto_bloco(c, p.ux, y,
                         "PENDENCIAS DECLARADAS - ESTA PRANCHA NAO ESTA APTA A PROTOCOLO",
                         "Helvetica-Bold", 11, col)
        yy -= 3
        yy = tabela(c, p.ux, yy,
                    [col * 0.06, col * 0.30, col * 0.44, col * 0.20],
                    d["pendencias"], tam=6.6)
        px = p.ux + col + 8
        cw = p.uw - col - 8
        yy2 = texto_bloco(c, px, y, "RESPONSAVEIS TECNICOS E RRT/ART",
                          "Helvetica-Bold", 10, cw)
        yy2 -= 3
        yy2 = tabela(c, px, yy2, [cw * 0.22, cw * 0.48, cw * 0.30],
                     d["responsaveis"], tam=6.8)
        yy2 -= 5
        yy2 = bloco_alerta(c, px, yy2, cw, d["bloqueio_protocolo"]["titulo"],
                           d["bloqueio_protocolo"]["paragrafos"], [])
        yy2 -= 4
        nota_fonte(c, px, yy2, cw, d["rodape_rastreabilidade"])

    p.add("PENDÊNCIAS E RESPONSABILIDADE TÉCNICA", "S/ESC", f10)

    return p.render()


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Compila prancha de Projeto Legal em PDF a partir de um JSON de caso.")
    ap.add_argument("--caso", required=True, help="arquivo JSON com os dados do caso")
    ap.add_argument("--saida", required=True, help="caminho do PDF de saida")
    a = ap.parse_args()

    with open(a.caso, encoding="utf-8") as fh:
        caso = json.load(fh)

    caso.setdefault("data", date.today().strftime("%d/%m/%Y"))
    total = montar(caso, a.saida)
    print("PDF gerado: %s" % a.saida)
    print("Formato: %s paisagem (%d x %d mm) | Folhas: %d"
          % (caso.get("formato", "A1"),
             FORMATOS[caso.get("formato", "A1")][0],
             FORMATOS[caso.get("formato", "A1")][1], total))


if __name__ == "__main__":
    sys.exit(main())
