#!/usr/bin/env python3
"""Verify SHA-256 checksums of all frozen repository files against manifests/freeze_manifest_sha256.json."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'manifests/freeze_manifest_sha256.json'

def main():
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    files = data['files']
    for rel_path, meta in files.items():
        fpath = ROOT / rel_path
        assert fpath.exists(), f"Missing frozen file: {rel_path}"
        digest = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert digest == meta['sha256'], f"SHA-256 mismatch for {rel_path}: expected {meta['sha256']}, got {digest}"
    print(f"[OK] Verified SHA-256 integrity across all {len(files)} frozen repository files.")

if __name__ == '__main__':
    main()
