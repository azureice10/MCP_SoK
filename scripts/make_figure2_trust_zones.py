#!/usr/bin/env python3
"""Draw Figure 2 (trust zones and channels of an MCP deployment).

Usage: python scripts/make_figure2_trust_zones.py [output.png]
Default output: manuscript/figures/figure2_trust_zones.png
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / 'manuscript/figures/figure2_trust_zones.png')

plt.rcParams['font.family'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'

W, H = 1260, 1060
fig = plt.figure(figsize=(7.0, 7.0 * H / W), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis('off')

FS = 10.0     # box labels
FL = 8.6      # channel labels
FG = 9.2      # legend
TEAL = '#1F7A8C'
RED = '#B03A2E'
GREY = '#555555'
C_USER, C_HOST, C_CLIENT = '#E6E6E6', '#D9E6F4', '#C5DAEE'
C_PLAN, C_SERV, C_COMP = '#E7DEF2', '#FBE1CE', '#FEF7F1'
C_EXT, C_THETA = '#E0EED6', '#D3ECE8'


def box(x0, y0, x1, y1, fill, text=None, fs=FS, ls='-', lw=1.4, z=2, ha='center', tx=None, ty=None):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle='round,pad=0,rounding_size=8',
                                fc=fill, ec='black', lw=lw, ls=ls, zorder=z))
    if text:
        ax.text(tx if tx is not None else (x0 + x1) / 2, ty if ty is not None else (y0 + y1) / 2, text,
                ha=ha, va='center', fontsize=fs, zorder=z + 1, linespacing=1.2)


def arrow(p0, p1, color='black', lw=1.3, style='-|>', ls='-', rad=0.0, z=3, ms=11):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, lw=lw, color=color,
                                 linestyle=ls, connectionstyle=f'arc3,rad={rad}', shrinkA=0, shrinkB=0, zorder=z))


def path(points, color='black', lw=1.3, z=3, ms=11):
    """Polyline with an arrow head on the final segment."""
    xs, ys = zip(*points)
    ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, zorder=z, solid_capstyle='butt')
    ax.plot(xs[-2:], ys[-2:], color=color, lw=lw, zorder=z)
    arrow(points[-2], points[-1], color=color, lw=lw, z=z, ms=ms)


def marker(x, y, n, r=13, fs=9.2):
    ax.add_patch(plt.Circle((x, y), r, fc=TEAL, ec='white', lw=1.2, zorder=6))
    ax.text(x, y + 0.5, str(n), ha='center', va='center', fontsize=fs, color='white', fontweight='bold', zorder=7)


def label(x, y, text, fs=FL, ha='center', color='black', style='normal', bg=True):
    kw = dict(boxstyle='square,pad=0.12', fc='white', ec='none', alpha=0.9) if bg else None
    ax.text(x, y, text, ha=ha, va='center', fontsize=fs, color=color, style=style, zorder=8,
            linespacing=1.15, bbox=kw)


# ---- zones -------------------------------------------------------------
HX0, HX1, HY0, HY1 = 232, 588, 150, 650          # host H
CX0, CX1 = 268, 552                               # clients
SX0, SX1 = 768, 948                               # servers
DX0, DX1, DY0, DY1 = 748, 968, 150, 650           # composition (dashed)
XX0, XX1 = 1018, 1244                             # external systems
ROWS = [(240, 308), (370, 438), (540, 608)]       # C/S/X rows

box(HX0, HY0, HX1, HY1, C_HOST, z=1)
ax.text(HX0 + 16, HY0 + 26, 'H  Host application', ha='left', va='center', fontsize=FS, zorder=3)
box(DX0, DY0, DX1, DY1, C_COMP, ls=(0, (5, 3)), lw=1.4, z=1)

box(268, 14, 568, 104, C_PLAN, 'L  LLM planner')
box(22, 334, 170, 454, C_USER, 'U\nUser')
names = [('1', '1'), ('2', '2'), ('n', 'n')]
for (y0, y1), (sub, _) in zip(ROWS, names):
    box(CX0, y0, CX1, y1, C_CLIENT, rf'$C_{{{sub}}}$  client')
    box(SX0, y0, SX1, y1, C_SERV, rf'$S_{{{sub}}}$  server')
    box(XX0, y0, XX1, y1, C_EXT, rf'$X_{{{sub}}}$  external system')
for x in ((CX0 + CX1) / 2, (SX0 + SX1) / 2, (XX0 + XX1) / 2):
    ax.text(x, 497, r'$\vdots$', ha='center', va='center', fontsize=13, zorder=3)
box(752, 704, 964, 800, C_THETA, 'Θ  authorization\ninfrastructure')

# ---- channels ----------------------------------------------------------
# 1: U -> H
arrow((170, 394), (HX0, 394))
marker(201, 362, 1)
# L <-> H (context)
arrow((378, 106), (378, HY0 - 1), style='<|-|>', color=GREY, lw=1.2, ms=9)
label(390, 128, 'context / tool choice', ha='left', color=GREY, bg=False)
# 3: L -> S1 (tool call), elbow over the top
path([(568, 36), (898, 36), (898, ROWS[0][0])])
label(733, 18, 'tool call', bg=False)
marker(898, 104, 3)
# 2: S1 -> L (descriptions, results, resources), elbow
path([(818, ROWS[0][0]), (818, 80), (568, 80)])
label(693, 112, 'descriptions,\nresults, resources', bg=False)
marker(818, 128, 2)
# client <-> server (JSON-RPC)
for (y0, y1) in ROWS:
    yc = (y0 + y1) / 2 - (10 if (y0, y1) == ROWS[1] else 0)
    arrow((CX1, yc), (SX0, yc), style='<|-|>', color=GREY, lw=1.1, ms=8)
label((HX1 + DX0) / 2, 338, 'JSON-RPC\nstdio / HTTP', color=GREY, fs=8.2, bg=False)
# 8: S2 -> C2 peer metadata (red dashed)
y8 = 418
arrow((SX0, y8), (CX1, y8), color=RED, ls=(0, (4, 2.5)), lw=1.2, ms=9)
marker((HX1 + DX0) / 2, y8, 8)
label((HX1 + DX0) / 2, 462, 'metadata, URLs,\nlaunch directives', color=RED, fs=8.2, bg=False)
# 7: descriptor drift (inside composition box, below S2)
marker(788, 467, 7)
ax.text(808, 467, r'descriptor $t_0 \rightarrow t_1$', ha='left', va='center', fontsize=FL, style='italic', zorder=8)
# 5: S -> X privileged operation
for (y0, y1) in ROWS:
    arrow((SX1, (y0 + y1) / 2), (XX0, (y0 + y1) / 2))
marker(993, 236, 5)
# 6: composition label below the dashed box, right side
marker(988, 668, 6)
ax.text(1008, 668, r'composition over $S_1 \ldots S_k$', ha='left', va='center', fontsize=FL, zorder=8)
# 4: tokens, C <-> Theta and S <-> Theta
arrow((420, 610), (768, 760), style='<|-|>', rad=0.22, lw=1.3, ms=9)
marker(560, 718, 4)
label(560, 772, 'token issuance and presentation', bg=False)
arrow((858, 610), (858, 704), style='<|-|>', lw=1.3, ms=9)
marker(884, 676, 4)
# 8 (second path): Theta -> client, authorization-discovery URLs (red dashed)
arrow((790, 704), (500, 610), color=RED, ls=(0, (4, 2.5)), lw=1.2, rad=-0.12, ms=9)

# ---- legend ------------------------------------------------------------
ax.plot([18, W - 18], [836, 836], color='#999999', lw=0.9)
items = [(1, r'U $\rightarrow$ H: goal or approval'), (2, r'$S_i \rightarrow$ L: descriptions, results'),
         (3, r'L $\rightarrow S_i$: tool invocation'), (4, r'C $\leftrightarrow \Theta$, $S_i \leftrightarrow \Theta$: tokens'),
         (5, r'$S_i \rightarrow X_i$: privileged operation'), (6, r'Composition over $S_1 \ldots S_k$'),
         (7, r'Descriptor at $t_1$ vs. $t_0$'), (8, r'$S_i$ / $\Theta \rightarrow$ C: peer metadata')]
cols = [40, 352, 664, 958]
for k, (n, t) in enumerate(items):
    x, y = cols[k % 4], 868 + 40 * (k // 4)
    marker(x, y, n, r=12, fs=8.6)
    ax.text(x + 20, y, t, ha='left', va='center', fontsize=FG)
swatches = [(C_USER, 'User'), (C_HOST, 'Host vendor (H, C)'), (C_PLAN, 'Model provider (L)'),
            (C_SERV, r'Server operator ($S_i$)'), (C_EXT, r'External system owner ($X_i$)'), (C_THETA, r'Identity provider ($\Theta$)')]
scol = [28, 440, 852]
for k, (c, t) in enumerate(swatches):
    x, y = scol[k % 3], 970 + 36 * (k // 3)
    ax.add_patch(Rectangle((x, y - 9), 28, 18, fc=c, ec='black', lw=0.9))
    ax.text(x + 38, y, t, ha='left', va='center', fontsize=FG)

fig.savefig(OUT, dpi=300, facecolor='white')
print('saved', OUT)
