#!/usr/bin/env python3
"""Build the AISC (Bon View) submission manuscript as a .docx from Markdown sources.

The journal template (a .docx supplied by the editor) is used as the package: its
styles, headers, footers, page setup, logo and front-matter layout are kept, and the
body is regenerated from manuscript/submission/*.md using the same paragraph, table,
figure and section-break patterns as the template draft.

Usage:
    python scripts/build_aisc_docx.py --template "C:/path/AISC-12351.docx" \
        --out manuscript/submission/MCP_SoK_Manuscript_AISC.docx

Standard library only. Citations are written as [@key] in the sources, numbered by first
appearance, and resolved against manuscript/submission/references.tsv.
"""
import argparse
import glob
import html
import os
import re
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'manuscript' / 'submission'
FIGDIR = ROOT / 'manuscript' / 'figures'

RPR_BASE = '<w:rFonts w:cs="Times New Roman"/>{b}{i}<w:color w:val="{color}"/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
PPR_BODY = '<w:autoSpaceDE w:val="0"/><w:autoSpaceDN w:val="0"/><w:adjustRightInd w:val="0"/><w:spacing w:after="0"/>'
CITE_OPEN, CITE_CLOSE = '\ue000', '\ue001'


def esc(t):
    return html.escape(t, quote=False)


# ---------------------------------------------------------------- sources
def read_sources():
    meta, blocks = {}, []
    files = sorted(glob.glob(str(SRC / '0*_*.md')))
    if not files:
        sys.exit('no source parts found in ' + str(SRC))
    lines = []
    for f in files:
        lines += Path(f).read_text(encoding='utf-8').split('\n') + ['']
    i = 0
    para = []

    def flush():
        nonlocal para
        if para:
            blocks.append(('p', ' '.join(s.strip() for s in para)))
            para = []

    while i < len(lines):
        ln = lines[i]
        if ln.startswith('@') and ':' in ln and not blocks and not para:
            k, v = ln[1:].split(':', 1)
            meta[k.strip()] = v.strip()
        elif ln.startswith(':::table'):
            flush()
            head = [x.strip() for x in ln[len(':::table'):].split(' | ')]
            label, caption, widths = head[0], head[1], head[2].replace('widths=', '')
            rows = []
            i += 1
            while not lines[i].startswith(':::'):
                if lines[i].strip():
                    rows.append([c.strip() for c in lines[i].split(' | ')])
                i += 1
            ncol = len(rows[0])
            assert all(len(r) == ncol for r in rows), (label, [len(r) for r in rows])
            blocks.append(('table', label, caption, [float(w) for w in widths.split(',')], rows))
        elif ln.startswith(':::figure'):
            flush()
            head = [x.strip() for x in ln[len(':::figure'):].split(' | ')]
            blocks.append(('figure', head[0], head[1], head[2], float(head[3]), head[4] if len(head) > 4 else ''))
            i += 1
            assert lines[i].startswith(':::'), 'figure block must be closed with :::'
        elif ln.startswith('## '):
            flush()
            blocks.append(('h2', ln[3:].strip()))
        elif ln.startswith('# '):
            flush()
            blocks.append(('h1', ln[2:].strip()))
        elif not ln.strip():
            flush()
        else:
            para.append(ln)
        i += 1
    flush()
    return meta, blocks


def read_refs():
    refs = {}
    order = []
    for ln in (SRC / 'references.tsv').read_text(encoding='utf-8').split('\n'):
        if ln.strip():
            k, flag, text = ln.split('\t', 2)
            refs[k] = {'na': flag == 'NA', 'text': text}
            order.append(k)
    return refs


# ---------------------------------------------------------------- citations
def number_citations(blocks, refs):
    seen = []
    cite_re = re.compile(r'\[@([^\]]+)\]')

    def scan(text):
        for m in cite_re.finditer(text):
            for k in m.group(1).split(';'):
                k = k.strip().lstrip('@')
                if k not in refs:
                    sys.exit('unknown reference key: ' + k)
                if k not in seen:
                    seen.append(k)

    for b in blocks:
        if b[0] in ('p', 'h1', 'h2'):
            scan(b[1])
        elif b[0] == 'table':
            scan(b[2])
            for r in b[4]:
                for c in r:
                    scan(c)
        elif b[0] == 'figure':
            scan(b[2])
            scan(b[5])
    return {k: n + 1 for n, k in enumerate(seen)}, seen


def fmt_numbers(nums):
    nums = sorted(set(nums))
    parts, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            parts.append(f'{nums[i]}\u2013{nums[j]}')
        else:
            parts += [str(n) for n in nums[i:j + 1]]
        i = j + 1
    return ', '.join(parts)


def sub_cites(text, numbering):
    def rep(m):
        ks = [k.strip().lstrip('@') for k in m.group(1).split(';')]
        return '[' + CITE_OPEN + fmt_numbers([numbering[k] for k in ks]) + CITE_CLOSE + ']'
    return re.sub(r'\[@([^\]]+)\]', rep, text)


# ---------------------------------------------------------------- inline xml
class Rels:
    def __init__(self):
        self.links = {}

    def link(self, url):
        if url not in self.links:
            self.links[url] = f'rIdAISCh{len(self.links) + 1}'
        return self.links[url]


def run(text, sz, bold=False, italic=False, color='000000', extra=''):
    if not text:
        return ''
    rpr = RPR_BASE.format(b='<w:b/><w:bCs/>' if bold else '', i='<w:i/><w:iCs/>' if italic else '', color=color, sz=sz) + extra
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


URL_RE = re.compile(r'https?://[^\s,;)]+[^\s,;).]')


def inline(text, numbering, sz, rels, bold=False, italic=False):
    text = sub_cites(text, numbering)
    out = []
    # bold / italic segmentation
    tokens = re.split(r'(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*))', text)
    for tok in tokens:
        if not tok:
            continue
        b, it = bold, italic
        if tok.startswith('**') and tok.endswith('**') and len(tok) > 4:
            tok, b = tok[2:-2], True
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            tok, it = tok[1:-1], True
        # citations
        for seg in re.split(f'({CITE_OPEN}[^{CITE_CLOSE}]*{CITE_CLOSE})', tok):
            if not seg:
                continue
            if seg.startswith(CITE_OPEN):
                out.append(run(seg[1:-1], sz, b, it, color='0000FF'))
                continue
            # urls
            pos = 0
            for m in URL_RE.finditer(seg):
                out.append(run(seg[pos:m.start()], sz, b, it))
                rid = rels.link(m.group(0))
                out.append(f'<w:hyperlink r:id="{rid}" w:history="1">'
                           + run(m.group(0), sz, b, it, color='0563C1', extra='<w:u w:val="single"/>') + '</w:hyperlink>')
                pos = m.end()
            out.append(run(seg[pos:], sz, b, it))
    return ''.join(out)


# ---------------------------------------------------------------- blocks
def p_body(text, numbering, rels):
    return (f'<w:p><w:pPr>{PPR_BODY}<w:ind w:firstLine="360"/><w:jc w:val="both"/></w:pPr>'
            + inline(text, numbering, 18, rels) + '</w:p>')


def p_blank():
    return f'<w:p><w:pPr>{PPR_BODY}<w:jc w:val="both"/></w:pPr></w:p>'


def p_spacer():
    return '<w:p><w:pPr><w:keepNext/><w:spacing w:after="0"/></w:pPr></w:p>'


def p_heading(level, text):
    num = '<w:ilvl w:val="0"/>' if level == 1 else '<w:ilvl w:val="1"/>'
    return (f'<w:p><w:pPr><w:pStyle w:val="Heading{level}"/><w:numPr>{num}<w:numId w:val="0"/></w:numPr><w:jc w:val="left"/></w:pPr>'
            f'<w:r><w:rPr><w:szCs w:val="22"/></w:rPr><w:t>{esc(text)}</w:t></w:r></w:p>')


def p_caption(text, numbering, rels):
    return (f'<w:p><w:pPr><w:keepNext/>{PPR_BODY}<w:jc w:val="center"/></w:pPr>'
            + inline(text, numbering, 18, rels, bold=True) + '</w:p>')


SECT_2COL = ('<w:p><w:pPr><w:spacing w:after="0"/><w:sectPr><w:type w:val="continuous"/><w:pgSz w:w="12240" w:h="15840"/>'
             '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="709" w:footer="709" w:gutter="0"/>'
             '<w:cols w:num="2" w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr></w:pPr></w:p>')
SECT_1COL = ('<w:p><w:pPr><w:spacing w:after="0"/><w:sectPr><w:type w:val="continuous"/><w:pgSz w:w="12240" w:h="15840"/>'
             '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="709" w:footer="709" w:gutter="0"/>'
             '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr></w:pPr></w:p>')


def tbl(rows, weights, numbering, rels):
    total = 9360
    s = sum(weights)
    w = [int(round(total * x / s)) for x in weights]
    w[-1] += total - sum(w)
    borders = '<w:top w:val="single" w:sz="12" w:space="0" w:color="auto"/><w:bottom w:val="single" w:sz="12" w:space="0" w:color="auto"/>'
    x = ['<w:tbl><w:tblPr><w:tblW w:w="9360" w:type="dxa"/><w:jc w:val="center"/>'
         f'<w:tblBorders>{borders}</w:tblBorders><w:tblLayout w:type="fixed"/>'
         '<w:tblCellMar><w:left w:w="85" w:type="dxa"/><w:right w:w="85" w:type="dxa"/></w:tblCellMar>'
         '<w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/></w:tblPr>']
    x.append('<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{c}"/>' for c in w) + '</w:tblGrid>')
    for ri, row in enumerate(rows):
        head = ri == 0
        trpr = '<w:trPr><w:cantSplit/>' + ('<w:tblHeader/>' if head else '') + '<w:jc w:val="center"/></w:trPr>'
        cells = []
        # keep short tables on one page: every row except the last stays with the next
        keep = '<w:keepNext/>' if len(rows) <= 10 and ri < len(rows) - 1 else ''
        for ci, cell in enumerate(row):
            tcb = f'<w:tcBorders>{borders}</w:tcBorders>' if head else ''
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{w[ci]}" w:type="dxa"/>{tcb}</w:tcPr>'
                         f'<w:p><w:pPr>{keep}<w:spacing w:before="20" w:after="20"/></w:pPr>'
                         + inline(cell, numbering, 17, rels) + '</w:p></w:tc>')
        x.append('<w:tr>' + trpr + ''.join(cells) + '</w:tr>')
    x.append('</w:tbl>')
    return ''.join(x)


def png_size(path):
    with open(path, 'rb') as f:
        d = f.read(32)
    return struct.unpack('>II', d[16:24])


def fig_para(rid, name, descr, width_in, size, docpr_id):
    cx = int(width_in * 914400)
    cy = int(cx * size[1] / size[0])
    return (f'<w:p><w:pPr><w:spacing w:before="60" w:after="0"/><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:noProof/></w:rPr>'
            f'<w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{docpr_id}" name="{esc(name)}" descr="{esc(descr)}"/><wp:cNvGraphicFramePr>'
            '<a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr>'
            f'<pic:cNvPr id="{docpr_id}" name="{esc(name)}"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="{rid}"/>'
            '<a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/>'
            f'<a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            '</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')


def p_note(text, numbering, rels):
    if text.startswith('Note:'):
        lead, rest = 'Note: ', text[5:].strip()
    else:
        lead, rest = '', text
    return (f'<w:p><w:pPr>{PPR_BODY}<w:jc w:val="both"/></w:pPr>' + (run(lead, 18, bold=True) if lead else '')
            + inline(rest, numbering, 18, rels) + '</w:p>')


def p_reference(text, rels):
    t = text
    parts = re.split(r'(\*[^*]+\*)', t)
    out = []
    base = '<w:rFonts w:eastAsia="Times New Roman"/>{i}<w:color w:val="{c}"/><w:szCs w:val="18"/>'
    for part in parts:
        if not part:
            continue
        it = part.startswith('*') and part.endswith('*') and len(part) > 2
        if it:
            part = part[1:-1]
        pos = 0
        for m in URL_RE.finditer(part):
            seg = part[pos:m.start()]
            if seg:
                out.append(f'<w:r><w:rPr>{base.format(i="<w:i/><w:iCs/>" if it else "", c="000000")}</w:rPr><w:t xml:space="preserve">{esc(seg)}</w:t></w:r>')
            rid = rels.link(m.group(0))
            out.append(f'<w:hyperlink r:id="{rid}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/>'
                       f'{base.format(i="", c="0563C1")}</w:rPr><w:t>{esc(m.group(0))}</w:t></w:r></w:hyperlink>')
            pos = m.end()
        seg = part[pos:]
        if seg:
            out.append(f'<w:r><w:rPr>{base.format(i="<w:i/><w:iCs/>" if it else "", c="000000")}</w:rPr><w:t xml:space="preserve">{esc(seg)}</w:t></w:r>')
    return ('<w:p><w:pPr><w:pStyle w:val="references"/><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
            + ''.join(out) + '</w:p>')


# ---------------------------------------------------------------- front matter
def rebuild_paragraph(doc, anchor, runs_fn):
    """Replace the paragraph that contains `anchor` text, keeping its pPr."""
    i = doc.find(anchor)
    if i < 0:
        sys.exit('anchor not found in template: ' + anchor)
    s = doc.rfind('<w:p ', 0, i)
    e = doc.find('</w:p>', i) + len('</w:p>')
    para = doc[s:e]
    assert para.count('<w:p ') == 1, 'nested paragraph for anchor ' + anchor
    ppr = re.search(r'<w:pPr>.*?</w:pPr>', para, re.S)
    ppr = ppr.group(0) if ppr else ''
    rprs = re.findall(r'<w:r\b[^>]*>(<w:rPr>.*?</w:rPr>)', para, re.S)
    head = re.match(r'<w:p [^>]*>', para).group(0)
    return doc[:s] + head + ppr + runs_fn(rprs) + '</w:p>' + doc[e:]


def front_matter(doc, meta, numbering, rels):
    def t(rpr, text):
        return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'

    doc = rebuild_paragraph(doc, 'Security of Model Context Protocol', lambda r: t(r[0], meta['title']))
    doc = rebuild_paragraph(doc, 'Abstract:', lambda r: t(r[0], 'Abstract:') + t(r[1], ' ' + meta['abstract']))
    doc = rebuild_paragraph(doc, 'Keywords:', lambda r: t(r[0], 'Keywords:') + t(r[1], ' ' + meta['keywords']))

    def authors(r):
        rp = r[0]
        sup = rp.replace('</w:rPr>', '<w:vertAlign w:val="superscript"/></w:rPr>')
        return (t(rp, 'Raden Budiarto Hadiprakoso') + t(sup, '1*') + t(rp, ', I Komang Setia Buana') + t(sup, '2')
                + t(rp, ', and Herman Kabetta') + t(sup, '3'))
    doc = rebuild_paragraph(doc, 'Raden Budiarto Hadiprakoso', authors)
    emails = ['raden.budiarto@poltekssn.ac.id', 'komang.setia@poltekssn.ac.id', 'herman.kabetta@poltekssn.ac.id']
    ital = '<w:rPr><w:i/></w:rPr>'
    sup_i = '<w:rPr><w:i/><w:vertAlign w:val="superscript"/></w:rPr>'
    spans = []
    for m in re.finditer(r'w:val="Affiliation"', doc):
        s = doc.rfind('<w:p ', 0, m.start())
        e = doc.find('</w:p>', m.start()) + len('</w:p>')
        if 'Politeknik' in doc[s:e]:
            spans.append((s, e))
    if len(spans) != 3:
        sys.exit(f'expected 3 affiliation paragraphs, found {len(spans)}')
    for n, (s, e) in reversed(list(enumerate(spans, 1))):
        head = re.match(r'<w:p [^>]*>', doc[s:e]).group(0)
        ppr = re.search(r'<w:pPr>.*?</w:pPr>', doc[s:e], re.S).group(0)
        body = (f'<w:r>{sup_i}<w:t>{n}</w:t></w:r>'
                + t(ital, ' Cryptographic Engineering, Politeknik Siber dan Sandi Negara, Indonesia, ' + emails[n - 1]))
        doc = doc[:s] + head + ppr + body + '</w:p>' + doc[e:]

    def corr(r):
        return (t(r[0], '*Corresponding author:') + t(r[1], ' Raden Budiarto Hadiprakoso, Cryptographic Engineering, '
                 'Politeknik Siber dan Sandi Negara, Indonesia. Email: raden.budiarto@poltekssn.ac.id'))
    doc = rebuild_paragraph(doc, '*Corresponding author:', corr)
    return doc


# ---------------------------------------------------------------- main
def build(template, out):
    meta, blocks = read_sources()
    refs = read_refs()
    numbering, order = number_citations(blocks, refs)
    rels = Rels()

    zin = zipfile.ZipFile(template)
    doc = zin.read('word/document.xml').decode('utf-8')
    rels_xml = zin.read('word/_rels/document.xml.rels').decode('utf-8')

    doc = front_matter(doc, meta, numbering, rels)

    # cut the old body
    h = doc.find('w:val="Heading1"')
    start = doc.rfind('<w:p ', 0, h)
    end = doc.rfind('<w:sectPr')
    old_body = doc[start:end]
    kept = doc[:start] + doc[end:]

    # figures: add image relationships
    figrels = {}
    next_fig = 0

    out_xml = []
    first_h1 = True
    in_text = False
    for b in blocks:
        kind = b[0]
        if kind == 'h1':
            if out_xml:
                out_xml.append(p_blank())
            out_xml.append(p_heading(1, b[1]))
            out_xml.append(p_spacer())
        elif kind == 'h2':
            out_xml.append(p_blank())
            out_xml.append(p_heading(2, b[1]))
            out_xml.append(p_spacer())
        elif kind == 'p':
            out_xml.append(p_body(b[1], numbering, rels))
        elif kind == 'table':
            _, label, caption, weights, rows = b
            out_xml += [SECT_2COL, p_blank(), p_caption(label, numbering, rels), p_caption(caption, numbering, rels),
                        tbl(rows, weights, numbering, rels), p_blank(), SECT_1COL]
        elif kind == 'figure':
            _, label, caption, fname, width, note = b
            fpath = FIGDIR / fname
            next_fig += 1
            rid = f'rIdAISCf{next_fig}'
            figrels[rid] = fname
            out_xml += [SECT_2COL, p_blank(), p_caption(label, numbering, rels), p_caption(caption, numbering, rels),
                        fig_para(rid, fname, caption, width, png_size(fpath), 900 + next_fig)]
            if note:
                out_xml.append(p_note(note, numbering, rels))
            out_xml += [p_blank(), SECT_1COL]
    # references
    out_xml.append(p_heading(1, 'References'))
    out_xml.append(p_spacer())
    for k in order:
        out_xml.append(p_reference(refs[k]['text'], rels))

    new_body = ''.join(out_xml)
    doc_out = kept[:start] + new_body + kept[start:]

    # relationships: drop old hyperlinks and unreferenced images, add new ones
    used = set(re.findall(r'r:(?:embed|id)="(rId\d+)"', doc_out))
    old_ids = set(re.findall(r'r:(?:embed|id)="(rId\d+)"', old_body)) - used
    new_rels = []
    removed_targets = []
    for m in re.finditer(r'<Relationship [^>]*/>', rels_xml):
        r = m.group(0)
        rid = re.search(r'Id="([^"]+)"', r).group(1)
        typ = re.search(r'Type="([^"]+)"', r).group(1)
        if rid in old_ids and (typ.endswith('/hyperlink') or typ.endswith('/image')):
            if typ.endswith('/image'):
                removed_targets.append('word/' + re.search(r'Target="([^"]+)"', r).group(1))
            continue
        new_rels.append(r)
    # any remaining hyperlink relationships that are no longer referenced
    final_rels = []
    for r in new_rels:
        rid = re.search(r'Id="([^"]+)"', r).group(1)
        typ = re.search(r'Type="([^"]+)"', r).group(1)
        if typ.endswith('/hyperlink') and rid not in used:
            continue
        final_rels.append(r)
    for url, rid in rels.links.items():
        final_rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
                          f'Target="{html.escape(url, quote=True)}" TargetMode="External"/>')
    for rid, fname in figrels.items():
        final_rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                          f'Target="media/{fname}"/>')
    head = rels_xml[:rels_xml.find('<Relationship ')]
    rels_out = head + ''.join(final_rels) + '</Relationships>'

    # keep media still referenced by another relationship file
    other_refs = ''
    for n in zin.namelist():
        if n.endswith('.rels') and n != 'word/_rels/document.xml.rels':
            other_refs += zin.read(n).decode('utf-8', 'ignore')
    drop = {t for t in removed_targets if Path(t).name not in other_refs and Path(t).name not in rels_out}

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
        orig = list(zin.namelist())
        names = sorted(orig, key=lambda n: (n != '[Content_Types].xml', orig.index(n)))
        for n in names:
            if n in drop:
                continue
            if n == 'word/document.xml':
                zout.writestr(n, doc_out.encode('utf-8'))
            elif n == 'word/_rels/document.xml.rels':
                zout.writestr(n, rels_out.encode('utf-8'))
            else:
                zout.writestr(zin.getinfo(n), zin.read(n))
        for fname in set(figrels.values()):
            zout.write(FIGDIR / fname, f'word/media/{fname}')
    return numbering, refs, order


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--template', required=True)
    ap.add_argument('--out', default=str(SRC / 'MCP_SoK_Manuscript_AISC.docx'))
    a = ap.parse_args()
    numbering, refs, order = build(a.template, a.out)
    print(f'built {a.out}: {len(order)} references numbered by first citation')
