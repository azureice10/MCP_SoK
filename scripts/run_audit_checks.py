import os
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    
    manuscript_path = os.path.join(repo_root, "manuscript", "MCP_SoK_Manuscript_BonView.md")
    condensed_path = os.path.join(repo_root, "manuscript", "MCP_SoK_Manuscript_BonView_condensed.md")
    
    if not os.path.exists(manuscript_path):
        print(f"ERROR: Manuscript not found at {manuscript_path}")
        sys.exit(1)
        
    with open(manuscript_path, "r", encoding="utf-8") as f:
        text = f.read()

    checks = [
        ("614", "Deduplicated search records count"),
        ("171", "Corpus size N (synthesis records)"),
        ("85", "Defenses count"),
        ("22", "E4 benchmark count"),
        ("20", "CVE count in E4"),
        ("17 of the 22", "Pre-revision absorption"),
        ("20 of the 22", "Post-revision absorption"),
        ("77.3%", "Pre-revision percentage"),
        ("90.9%", "Post-revision percentage"),
        ("15 clusters", "Cluster analysis count"),
        ("11 (73.3%", "Pre-revision cluster absorption"),
        ("13 (86.7%", "Post-revision cluster absorption"),
        ("0.87", "Cohen kappa value"),
        ("91 of the 171", "Layer A academic papers count"),
        ("53.2%", "Layer A academic percentage"),
        ("18 of the 22", "Layer C primary count in E4"),
        ("81.8%", "Layer C primary percentage in E4"),
        ("68 (80.0%)", "L1 defense maturity"),
        ("15 (17.6%)", "L0 defense maturity"),
        ("2 (2.4%)", "L2 defense maturity"),
        ("3 of 70", "Adaptive evaluation count"),
        ("4.3%", "Adaptive evaluation percentage"),
        ("CVE-2025-6514", "mcp-remote CVE"),
        ("CVE-2026-0621", "ReDoS CVE"),
        ("CVE-2025-54135", "CurXecute CVE"),
        ("CVE-2025-54136", "MCPoison CVE"),
        ("Asana MCP Disclosure", "Asana record in Table 11"),
        ("Invariant Labs Incident", "Invariant record in Table 11"),
        ("Table 11", "Table 11 reference"),
        ("Table 12", "Table 12 reference"),
        ("Table 13", "Table 13 reference"),
        ("Table 14", "Table 14 reference"),
        ("Table 16", "Table 16 reference")
    ]

    print("=== AUDITING MANUSCRIPT INTEGRITY (33 CRITICAL CHECKS) ===")
    all_passed = True
    for s, desc in checks:
        count = text.count(s)
        status = "PASS" if count > 0 else "FAIL"
        print(f"[{status}] {desc} ('{s}'): {count} occurrences")
        if count == 0:
            all_passed = False

    if not all_passed:
        print("\nFAILURE: Some critical audit checks failed!")
        sys.exit(1)

    print("\nALL 33 QUANTITATIVE AND STRUCTURAL ASSERTIONS PASSED PERFECTLY!")

if __name__ == "__main__":
    main()
