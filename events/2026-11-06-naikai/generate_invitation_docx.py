#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""「いやしのおうち」内覧会 関係業者向け案内文（A4・Word）を生成する。

使い方:
    python3 generate_invitation_docx.py
出力:
    invitation-a4.docx （このスクリプトと同じフォルダ）
"""
import os
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

GREEN = RGBColor(0x3C, 0x8B, 0x72)
GREEN_LINE = "6FB89C"
GREEN_PALE = "EBF6F1"
GOLD_INK = RGBColor(0x5A, 0x3D, 0x0E)
INK = RGBColor(0x33, 0x33, 0x31)

BODY_EA = "游明朝"       # 本文：明朝（Windows 標準）
HEAD_EA = "游ゴシック"   # 見出し：ゴシック
BODY_ASCII = "Yu Mincho"
HEAD_ASCII = "Yu Gothic"


def set_run_font(run, size=None, ea=BODY_EA, ascii_font=BODY_ASCII,
                 bold=False, color=None, spacing=None):
    run.font.size = Pt(size) if size else run.font.size
    run.font.bold = bold
    if color is not None:
        run.font.color.rgb = color
    run.font.name = ascii_font
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    rfonts.set(qn('w:eastAsia'), ea)
    rfonts.set(qn('w:ascii'), ascii_font)
    rfonts.set(qn('w:hAnsi'), ascii_font)
    if spacing is not None:
        sp = OxmlElement('w:spacing')
        sp.set(qn('w:val'), str(int(spacing)))  # 1/20 pt
        rpr.append(sp)


def add_para(doc, align=None, space_after=6, space_before=0, line=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    if align is not None:
        p.alignment = align
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    if line is not None:
        pf.line_spacing = line
    return p


def run_text(p, text, **kw):
    r = p.add_run(text)
    set_run_font(r, **kw)
    return r


def set_bottom_border(paragraph, color=GREEN_LINE, size=12):
    pPr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), str(size))
    bottom.set(qn('w:space'), '6')
    bottom.set(qn('w:color'), color)
    pbdr.append(bottom)
    pPr.append(pbdr)


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def set_cell_text(cell, lines, label=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.line_spacing = 1.3
    if isinstance(lines, str):
        lines = [lines]
    for i, ln in enumerate(lines):
        if i > 0:
            p = cell.add_paragraph()
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.line_spacing = 1.3
        if label:
            run_text(p, ln, size=10.5, ea=HEAD_EA, ascii_font=HEAD_ASCII,
                     bold=True, color=GREEN)
        else:
            run_text(p, ln, size=10.5, color=INK)


def set_table_borders(table, color="D9D4C4", size=6):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), str(size))
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), color)
        borders.append(el)
    tblPr.append(borders)


def build():
    doc = Document()

    # 既定スタイルの日本語フォント
    normal = doc.styles['Normal']
    normal.font.size = Pt(10.5)
    normal.font.name = BODY_ASCII
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts'); rpr.append(rfonts)
    rfonts.set(qn('w:eastAsia'), BODY_EA)

    # A4 ・ 余白
    sec = doc.sections[0]
    sec.page_width = Mm(210)
    sec.page_height = Mm(297)
    sec.top_margin = Mm(22)
    sec.bottom_margin = Mm(18)
    sec.left_margin = Mm(22)
    sec.right_margin = Mm(22)

    # 発信日（右）
    p = add_para(doc, WD_ALIGN_PARAGRAPH.RIGHT, space_after=10)
    run_text(p, "2026年10月吉日", size=10.5, color=INK)

    # 宛名（左）
    p = add_para(doc, WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    run_text(p, "関係業者 各位", size=14, ea=HEAD_EA, ascii_font=HEAD_ASCII,
             bold=True, color=INK, spacing=20)

    # 差出人（右）
    sender = [
        ("株式会社 癒し家", dict(size=12, ea=HEAD_EA, ascii_font=HEAD_ASCII, bold=True, color=GREEN)),
        ("代表取締役　加賀谷 徹（臨床心理士）", dict(size=10.5, color=INK)),
        ("〒543-0001　大阪府大阪市天王寺区上汐3丁目6-14-505C", dict(size=9.5, color=INK)),
        ("女性専用グループホーム「いやしのおうち」", dict(size=9.5, color=INK)),
        ("TEL 080-6619-2027 ／ Email iyashiya.a1@gmail.com", dict(size=9.5, color=INK)),
    ]
    for i, (txt, kw) in enumerate(sender):
        p = add_para(doc, WD_ALIGN_PARAGRAPH.RIGHT,
                     space_after=(8 if i == len(sender) - 1 else 1),
                     space_before=(4 if i == 0 else 0), line=1.3)
        run_text(p, txt, **kw)

    # タイトル
    p = add_para(doc, WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=2)
    run_text(p, "「いやしのおうち」内覧会のご案内", size=17,
             ea=HEAD_EA, ascii_font=HEAD_ASCII, bold=True, color=GREEN, spacing=40)
    p = add_para(doc, WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    run_text(p, "― ほっとできる、もうひとつのうち ―", size=10,
             ea=HEAD_EA, ascii_font=HEAD_ASCII, color=GOLD_INK, spacing=30)
    set_bottom_border(p)

    # 本文
    body = [
        "拝啓　晩秋の候、貴社ますますご清栄のこととお慶び申し上げます。平素は格別のご高配を賜り、厚く御礼申し上げます。",
        "　さて、このたび弊社は、大阪府大東市に女性専用のグループホーム（共同生活援助・定員4名）「いやしのおうち」を開設する運びとなりました。つきましては、日頃よりお世話になっております関係業者の皆様に、施設を実際にご覧いただく内覧会を下記のとおり開催いたします。",
        "　当日は、館内のご見学に加え、事業内容のご説明や個別のご相談もお受けいたします。ご多用のところ誠に恐縮ではございますが、ぜひご来場賜りますようご案内申し上げます。",
    ]
    for t in body:
        p = add_para(doc, WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line=1.6)
        run_text(p, t, size=10.5, color=INK)
    p = add_para(doc, WD_ALIGN_PARAGRAPH.RIGHT, space_after=6)
    run_text(p, "敬具", size=10.5, color=INK)

    # 記
    p = add_para(doc, WD_ALIGN_PARAGRAPH.CENTER, space_after=4, space_before=2)
    run_text(p, "記", size=12, ea=HEAD_EA, ascii_font=HEAD_ASCII, bold=True, color=GREEN)

    rows = [
        ("日　時", ["2026年11月6日（金）　10:00 〜 16:00", "（受付 15:30 まで・入退場自由）"]),
        ("会　場", ["女性専用グループホーム「いやしのおうち」（女性専用・定員4名）",
                   "〒574-0011　大阪府大東市北条5-8-31"]),
        ("アクセス", ["JR学研都市線「四条畷駅」より徒歩約13分（「野崎駅」より徒歩約23分）"]),
        ("内　容", ["施設のご見学 ／ 事業内容のご説明 ／ 個別のご相談"]),
        ("お申込み", ["事前のお申込みは不要です。人数把握のため、ご来場予定の場合は",
                    "前日までにお電話・メールにてご一報いただけますと幸いです。"]),
        ("お問合せ", ["株式会社 癒し家　TEL 080-6619-2027（受付 9:00〜18:00／土日祝可）",
                    "Email iyashiya.a1@gmail.com"]),
    ]
    table = doc.add_table(rows=len(rows), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    table.columns[0].width = Mm(28)
    table.columns[1].width = Mm(138)
    for i, (label, vals) in enumerate(rows):
        c0, c1 = table.rows[i].cells
        c0.width = Mm(28)
        c1.width = Mm(138)
        shade_cell(c0, GREEN_PALE)
        set_cell_text(c0, label, label=True)
        set_cell_text(c1, vals)

    # 以上
    p = add_para(doc, WD_ALIGN_PARAGRAPH.RIGHT, space_before=6, space_after=14)
    run_text(p, "以　上", size=10.5, color=INK)

    # フッター
    p = add_para(doc, WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    set_bottom_border(p, color="E3C883", size=6)
    p = add_para(doc, WD_ALIGN_PARAGRAPH.CENTER, space_before=4)
    run_text(p, "運営：株式会社 癒し家（代表 加賀谷 徹／臨床心理士）　／　公式サイト：resumecor-lang.github.io/iyashinouchi-site",
             size=8.5, ea=HEAD_EA, ascii_font=HEAD_ASCII, color=RGBColor(0x6b, 0x6b, 0x66))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invitation-a4.docx")
    doc.save(out)
    print("saved:", out)


if __name__ == "__main__":
    build()
