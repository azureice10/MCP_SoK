"""Verify the public v2 CSVs and reproduce their headline counts."""
import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def read_csv(name):
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def index(rows, key, size):
    result = {row[key]: row for row in rows}
    require(len(rows) == len(result) == size and "" not in result,
            f"Unexpected size, empty key, or duplicate {key}")
    return result


def counts(rows, key):
    return Counter(row[key] for row in rows)


def main():
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, name = line.split(maxsplit=1)
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        require(actual == expected, f"SHA-256 mismatch: {name}")

    corpus = read_csv("dataset_s3_corpus_215_v2.csv")
    studies = index(corpus, "record_id", 215)
    require(counts(corpus, "tier") == {"E1": 91, "E2": 119, "E3": 1, "E4": 4},
            "Unexpected study tiers")
    require(counts(corpus, "in_conservative_170")["Yes"] == 199,
            "Unexpected conservative corpus size")
    require("S-Corpus-030" not in counts(corpus, "Dataset_ID"), "IC1 exclusion missing")

    defenses = read_csv("dataset_s4_defenses_112_v2.csv")
    index(defenses, "record_id", 112)
    for row in defenses:
        study = studies.get(row["record_id"])
        require(study and study["tier"] == row["evidence_tier"],
                f"Invalid defense-to-corpus link: {row['record_id']}")
    require(counts(defenses, "in_conservative_84")["Yes"] == 102,
            "Unexpected conservative defense count")
    require(counts(defenses, "maturity_level") == {"L0": 20, "L1": 90, "L2": 2},
            "Unexpected defense maturity counts")
    require(counts(defenses, "adaptive_evaluation")["Yes"] == 6,
            "Unexpected adaptive defense count")

    advisories = read_csv("dataset_temporal_E4_256.csv")
    index(advisories, "HO", 256)
    require(counts(advisories, "decision") == {"Include E4": 216, "Exclude": 40},
            "Unexpected screening counts")
    require(sum(row["decision"] == "Exclude" and row["exclusion_code"].startswith("G6 ")
                for row in advisories) == 7, "Unexpected G6 exclusions")
    eligible = [row for row in advisories if row["decision"] == "Include E4"]
    require(counts(eligible, "absorbed") == {"Yes": 136, "Partial": 53, "No": 27},
            "Unexpected temporal coverage counts")
    require(all("2026-09-26" <= row["published"] <= "2026-11-16" for row in eligible),
            "Advisory date outside temporal window")
    clusters = defaultdict(set)
    for row in eligible:
        clusters[row["cluster_primary"]].add(row["absorbed"])
    require(len(clusters) == 137 and "" not in clusters, "Unexpected cluster count")
    require(sum(fits == {"Yes"} for fits in clusters.values()) == 90,
            "Unexpected direct-fit cluster count")
    require(sum("No" not in fits for fits in clusters.values()) == 123,
            "Unexpected extension-inclusive cluster count")
    print("Verified: 215 corpus records, 112 defenses, and 216 of 256 eligible advisories.")
    print("Temporal coverage: 136 direct fits, 53 extensions, and 27 unclassified.")


if __name__ == "__main__":
    main()
