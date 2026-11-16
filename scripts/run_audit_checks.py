#!/usr/bin/env python3
"""Verify supplementary files and figures against frozen data, and (when available) the manuscript text.

The full manuscript text is not distributed in the public repository (journal similarity screening).
Checks 1-3 always run. Check 4 runs only if a local copy exists at
manuscript/_private/MCP_SoK_Manuscript_Revised_AISC.md (gitignored) and is reported as SKIPPED otherwise.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_MS = ROOT / 'manuscript/_private/MCP_SoK_Manuscript_Revised_AISC.md'

STALE = ['S-Def-27', 'S-Def-52', '71 baseline defenses, the 14 initial supplementary defenses, the 2 restored',
         'upgraded `Jalendar/ZPAA`', '3 of 72', '1,180 servers', '182 MCP-specific', '180 MCP-specific', '2 of 72',
         '52 (72.2%', '120 adversarial trials', 'JWS capability', '120-trial']


def check_public(supp_text, ds_text):
    # 1. Figures shipped with the repository
    for fig in ['figure1_prisma_flow.png', 'figure2_trust_zones.png']:
        fig_path = ROOT / 'manuscript/figures' / fig
        assert fig_path.exists() and fig_path.stat().st_size > 50000, f"Missing or empty figure file: {fig_path}"
    # 2. Frozen metrics and identifiers in the public supplementary files
    for phrase in ['179 MCP-specific', '2 of 71', '51 (71.8%', 'S-Def-16']:
        assert phrase in supp_text, f"Missing key frozen phrase in supplementary material: {phrase}"
    for phrase in ['S-Def-16', 'S-Def-84']:
        assert phrase in ds_text, f"Missing key identifier in research dataset: {phrase}"
    for bad in STALE:
        assert bad not in supp_text, f"Found stale/incorrect phrase in supplementary material: {bad}"
    # 3. Completeness
    assert len(supp_text) > 10000 and len(ds_text) > 50000, "Supplementary files incomplete"


def check_private(ms_text, supp_text):
    words = len(ms_text.split())
    assert words >= 3500, f"Manuscript length {words} < 3,500 words"
    ref_section = ms_text[ms_text.find('## References'):]
    ref_lines = [l.strip() for l in ref_section.splitlines() if re.match(r'^\d+\.\s+', l.strip())]
    assert len(ref_lines) == 60, f"Expected 60 references in main bibliography, found {len(ref_lines)}"
    recent = sum(1 for l in ref_lines if re.search(r'\((202[1-6])[a-z]?[,\)]', l))
    share = recent / len(ref_lines)
    assert share >= 0.60, f"Recent reference share {share:.1%} < 60%"
    assert not [l for l in ref_lines if 'arxiv' in l.lower()], "Found arXiv preprints in main bibliography"
    assert not [l for l in ref_lines if 'nvd.nist.gov' in l.lower()], "Found raw CVE URLs in main bibliography"
    for fig_rel in ['figures/figure1_prisma_flow.png', 'figures/figure2_trust_zones.png']:
        assert fig_rel in ms_text, f"Figure reference missing in manuscript: {fig_rel}"
    for phrase in ['179 MCP-specific', '88 defenses', '69 (78.4%', '17 (19.3%', '2 of 71', '51 (71.8%',
                   'Fifteen of the 88 defenses (17.0%', 'S-Def-16', 'S-Def-23', 'S-Def-84', 'S-Def-85',
                   'MCP_SoK_Supplementary_Research_Dataset']:
        assert phrase in ms_text, f"Missing key frozen phrase in manuscript: {phrase}"
    for bad in STALE:
        assert bad not in ms_text, f"Found stale/incorrect phrase in manuscript: {bad}"
    return words, len(ref_lines), share


def main():
    supp_text = (ROOT / 'supplementary/MCP_SoK_Supplementary_Material_Revised.md').read_text(encoding='utf-8')
    ds_text = (ROOT / 'supplementary/MCP_SoK_Supplementary_Research_Dataset.md').read_text(encoding='utf-8')
    check_public(supp_text, ds_text)
    print("[OK] Public audit passed: figures present, frozen metrics and identifiers consistent, no stale phrases in supplementary material.")
    if PRIVATE_MS.exists():
        words, n, share = check_private(PRIVATE_MS.read_text(encoding='utf-8'), supp_text)
        print(f"[OK] Private manuscript audit passed: {words} words, {n} references ({share:.1%} from 2021-2026, 0 arXiv/CVE in main refs).")
    else:
        print("[SKIPPED] Private manuscript audit: manuscript/_private/ not present (full text is not distributed publicly).")


if __name__ == '__main__':
    main()
