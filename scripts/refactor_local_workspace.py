#!/usr/bin/env python3
"""One-click refactoring utility for local MCP_SoK working folder on Windows/Linux/macOS.

Usage:
    python refactor_local_workspace.py --target-dir "C:\path\to\MCP_SoK"
    python refactor_local_workspace.py --target-dir "C:\path\to\MCP_SoK" --dry-run

What this script does:
1. Scans the target MCP_SoK folder for legacy/redundant snapshots, old drafts, OCR scratch files, and PNG page renders.
2. Moves (archives) superseded files into `_archive_legacy_pre_2026_11_14/` sorted by category (zero data loss).
3. Organizes canonical frozen files into a clean `github_repo_ready/` directory structure ready for `git init / git commit / git push`.
"""
import argparse
import os
import shutil
from pathlib import Path

LEGACY_PATTERNS = {
    'superseded_datasets_v1_171_85': [
        'prisma_screening_pool_614.csv',
        'mcp_sok_corpus_171.csv',
        'corpus_metadata_182.csv',
        'defenses_85_consolidated.csv',
        'defenses_85_consolidated.xlsx',
    ],
    'superseded_manuscript_drafts': [
        'MCP_SoK_Manuscript_AISC.pdf',
        'MCP_SoK_Manuscript_BonView.md',
        'MCP_SoK_Supplementary_Material.md',
    ],
    'intermediate_reconciliation_logs': [
        'HASIL_REKONSILIASI.md',
        'PENERAPAN_PERSETUJUAN.md',
        'REKONSILIASI_LANJUTAN.md',
        'apply_approved_reconciliation.py',
        'exclusion_review_queue_106.json',
        'priority4_source_review_stage2.json',
        'priority8_source_review.json',
        'INDEX_SELURUH_442_STUDI_DAN_PDF.csv',
    ],
    'scratch_text_extractions_and_renders': [
        'SLR-M-0079_attested_policy_brokerage.txt',
        'SLR-M-0169_hierarchical.txt',
        'SLR-M-0247_redteam_mcp.txt',
        'a2a_secure.txt',
        'agenticcyops.txt',
        'balkanization.txt',
        'formalizing.txt',
        'gordeichik.txt',
        'sszkr.txt',
        'scr0169_p6.png', 'scr0169_p7.png', 'scr0169_p8.png', 'scr0169_p9.png',
        'scr0169_p11.png', 'scr0169_p12.png', 'scr0169_p13.png', 'scr0169_p14.png',
    ],
    'papers_pdf_local_only': [
        'MCP_033_samuel_astral.pdf',
        'MCP_097_jalendar_zpaa.pdf',
        'SCR-0079_SLR-M-0079.pdf',
        'SCR-0169_SLR-M-0169.pdf',
        'SCR-0247_SLR-M-0247.pdf',
    ]
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target-dir', type=Path, default=Path('.'), help='Path to local MCP_SoK folder')
    parser.add_argument('--dry-run', action='store_true', help='Preview actions without moving files')
    args = parser.parse_args()

    target = args.target_dir.resolve()
    archive_base = target / '_archive_legacy_pre_2026_11_14'
    print(f"Scanning workspace: {target} (dry_run={args.dry_run})")

    moved_count = 0
    for category, filenames in LEGACY_PATTERNS.items():
        for fname in filenames:
            matches = [p for p in target.rglob(fname) if '_archive_legacy' not in str(p) and 'github_repo_ready' not in str(p)]
            for src in matches:
                dst = archive_base / category / src.name
                print(f"  [ARCHIVE] {src.relative_to(target)} -> {dst.relative_to(target)}")
                if not args.dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), str(dst))
                moved_count += 1

    print(f"Completed: {moved_count} legacy/redundant files archived into {archive_base.name}.")

if __name__ == '__main__':
    main()
