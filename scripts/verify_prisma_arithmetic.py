import os
import sys
import pandas as pd

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    
    screening_path = os.path.join(repo_root, "data", "screening", "prisma_screening_pool_614.csv")
    corpus_path = os.path.join(repo_root, "data", "corpus", "mcp_sok_corpus_171.csv")
    background_path = os.path.join(repo_root, "data", "corpus", "background_set_b_11.csv")
    metadata_path = os.path.join(repo_root, "data", "corpus", "corpus_metadata_182.csv")
    validation_path = os.path.join(repo_root, "data", "validation", "e4_validation_set_22.csv")
    
    print("=== VERIFYING PRISMA ARITHMETIC CLOSURE ===")
    df_screening = pd.read_csv(screening_path)
    df_corpus = pd.read_csv(corpus_path)
    df_background = pd.read_csv(background_path)
    df_metadata = pd.read_csv(metadata_path)
    df_validation = pd.read_csv(validation_path)
    
    n_screening = len(df_screening)
    n_corpus = len(df_corpus)
    n_background = len(df_background)
    n_metadata = len(df_metadata)
    n_validation = len(df_validation)
    
    print(f"Screening Pool: {n_screening} records (Expected: 614)")
    print(f"MCP Synthesis Corpus: {n_corpus} records (Expected: 171)")
    print(f"Background Set B: {n_background} records (Expected: 11)")
    print(f"Consolidated Extracted Metadata: {n_metadata} records (Expected: 182)")
    print(f"E4 Validation Set: {n_validation} records (Expected: 22)")
    
    assert n_screening == 614, f"Mismatch: screening {n_screening} != 614"
    assert n_corpus == 171, f"Mismatch: corpus {n_corpus} != 171"
    assert n_background == 11, f"Mismatch: background {n_background} != 11"
    assert n_metadata == 182, f"Mismatch: metadata {n_metadata} != 182"
    assert n_corpus + n_background == n_metadata, "Arith error: corpus + background != metadata"
    assert n_validation == 22, f"Mismatch: validation {n_validation} != 22"
    
    # Check baseline vs supplementary in screening
    n_baseline = (df_screening["source_pool"] == "Baseline").sum()
    n_supp = (df_screening["source_pool"] == "Supplementary").sum()
    print(f"Baseline Phase: {n_baseline} (Expected: 460)")
    print(f"Supplementary Phase: {n_supp} (Expected: 154)")
    assert n_baseline == 460, f"Mismatch: baseline {n_baseline} != 460"
    assert n_supp == 154, f"Mismatch: supplementary {n_supp} != 154"
    assert n_baseline + n_supp == 614, "Arith error: baseline + supp != 614"
    
    n_included = (df_screening["final_decision"] == "Include").sum()
    n_excluded = (df_screening["final_decision"] == "Exclude").sum()
    print(f"Total Included: {n_included} (Expected: 182)")
    print(f"Total Excluded: {n_excluded} (Expected: 432)")
    assert n_included == 182, f"Mismatch: included {n_included} != 182"
    assert n_excluded == 432, f"Mismatch: excluded {n_excluded} != 432"
    assert n_included + n_excluded == 614, "Arith error: included + excluded != 614"
    
    # Baseline breakdown
    base_inc = (df_screening[df_screening["source_pool"] == "Baseline"]["final_decision"] == "Include").sum()
    base_exc = (df_screening[df_screening["source_pool"] == "Baseline"]["final_decision"] == "Exclude").sum()
    print(f"Baseline Included: {base_inc} (Expected: 157)")
    print(f"Baseline Excluded: {base_exc} (Expected: 303)")
    assert base_inc == 157, f"Mismatch: base_inc {base_inc} != 157"
    assert base_exc == 303, f"Mismatch: base_exc {base_exc} != 303"
    
    # Supplementary breakdown
    supp_inc = (df_screening[df_screening["source_pool"] == "Supplementary"]["final_decision"] == "Include").sum()
    supp_exc = (df_screening[df_screening["source_pool"] == "Supplementary"]["final_decision"] == "Exclude").sum()
    print(f"Supplementary Included: {supp_inc} (Expected: 25)")
    print(f"Supplementary Excluded: {supp_exc} (Expected: 129)")
    assert supp_inc == 25, f"Mismatch: supp_inc {supp_inc} != 25"
    assert supp_exc == 129, f"Mismatch: supp_exc {supp_exc} != 129"
    
    print("\nPRISMA ARITHMETIC VERIFICATION PASSED WITH 100% ACCURACY!")

if __name__ == "__main__":
    main()
