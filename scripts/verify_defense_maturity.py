import os
import sys
import pandas as pd

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    
    workbook_path = os.path.join(repo_root, "defense", "codebooks", "Lembar_Koding_Pertahanan_v1.3_FROZEN.xlsx")
    csv_path = os.path.join(repo_root, "defense", "codebooks", "defenses_85_consolidated.csv")
    
    print("=== VERIFYING DEFENSE MATURITY & CODER METRICS ===")
    if os.path.exists(workbook_path):
        df = pd.read_excel(workbook_path, sheet_name="Koding_85_Defenses")
    elif os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        print(f"ERROR: Neither workbook nor CSV found in {os.path.join(repo_root, 'defense', 'codebooks')}")
        sys.exit(1)
        
    n_def = len(df)
    print(f"Total defense records identified: {n_def} (Expected: 85)")
    assert n_def == 85, f"Mismatch: total defenses {n_def} != 85"
    
    maturity_counts = df["tingkat_kematangan"].value_counts().to_dict()
    l0 = maturity_counts.get("L0", 0)
    l1 = maturity_counts.get("L1", 0)
    l2 = maturity_counts.get("L2", 0)
    l3 = maturity_counts.get("L3", 0)
    
    print(f"Level 0 (Conceptual): {l0} (Expected: 15, 17.6%)")
    print(f"Level 1 (Offline/PoC): {l1} (Expected: 68, 80.0%)")
    print(f"Level 2 (Testbed):     {l2} (Expected: 2, 2.4%)")
    print(f"Level 3 (Production):  {l3} (Expected: 0, 0.0%)")
    
    assert l0 == 15, f"Mismatch: L0 {l0} != 15"
    assert l1 == 68, f"Mismatch: L1 {l1} != 68"
    assert l2 == 2, f"Mismatch: L2 {l2} != 2"
    assert l3 == 0, f"Mismatch: L3 {l3} != 0"
    assert l0 + l1 + l2 + l3 == 85, "Sum of maturity levels != 85"
    
    # Check empirical defenses adaptivity (L1 + L2 = 70)
    empirical = df[df["tingkat_kematangan"].isin(["L1", "L2"])]
    n_emp = len(empirical)
    print(f"Empirical defenses: {n_emp} (Expected: 70)")
    assert n_emp == 70, f"Mismatch: empirical defenses {n_emp} != 70"
    
    adapt_yes = (empirical["evaluasi_adaptif"].astype(str).str.lower().str.strip() == "yes").sum()
    print(f"Adaptive evaluation (Yes): {adapt_yes} of {n_emp} (Expected: 3, 4.3%)")
    assert adapt_yes == 3, f"Mismatch: adaptive evaluation {adapt_yes} != 3"
    
    print("\nDEFENSE METRICS AND MATURITY VERIFICATION PASSED WITH 100% ACCURACY!")

if __name__ == "__main__":
    main()
