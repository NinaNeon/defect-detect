"""
IMDD-1M Dataset Preparation Script
====================================
Downloads and preprocesses the IMDD-1M dataset from Google Drive.

Usage:
    python prepare_dataset.py --output_dir ./data
    python prepare_dataset.py --output_dir ./data --domain 266_353mvtec
    python prepare_dataset.py --output_dir ./data --verify_only

Requirements:
    pip install gdown tqdm pillow pandas
"""

import os
import sys
import json
import hashlib
import argparse
import zipfile
from pathlib import Path

# ------------------------------------------------------------------ #
# 1.  GOOGLE DRIVE IDs                                                 #
#     type="folder" -> gdown downloads the entire folder              #
#     type="file"   -> gdown downloads a single zip/archive           #
#     Remaining domains (classes 266+): paste IDs when available.     #
# ------------------------------------------------------------------ #
DOMAIN_REGISTRY = {
    # domain_folder_name : (drive_id, type, expected_md5_or_None)
    "0-4aircraft4000":       ("1Yzwp9QXh8pytgxvJWcKrW4gvRvwVQDxa", "folder", None),
    "5-10MT_tiles":          ("1Ojy6wHdz7RnIUIV6PNhz2c02Eruttg0j",  "file",   None),
    "11-19NEU-DET":          ("1CuMvi_VUqcywiMFDSEY8lbxSdbtUQ4Kr",  "file",   None),
    "20-24wall1000":         ("1ypZCvyC9hCKZ0Lm7ptBVs28_G6drEtMr",  "file",   None),
    "25-30OLED":             ("1Dh6lBKL6BkPWJcGU_DNeSI1AsJ10llqu",  "file",   None),
    "31-38solarcell":        ("1mG6UydqG8asd9u5EnpuT20y5npIOPXHu",  "folder", None),
    "39-258fabric":          ("1fLXox6uaKebbOxWtQjRKV_C2sEg9ZZXY",  "folder", None),
    "259-265gear":           ("1KweVPT4JqtEbu94O18_viISoF9wrdYqC",  "folder", None),
    # ---- classes 266+ : fill in when ready -------------------------
    "266_353mvtec":          ("YOUR_DRIVE_ID_HERE", "folder", None),
    "354_355solarcrack":     ("YOUR_DRIVE_ID_HERE", "file",   None),
    "356_366aluminum":       ("YOUR_DRIVE_ID_HERE", "folder", None),
    "367waterheat":          ("YOUR_DRIVE_ID_HERE", "folder", None),
    "368_377alu_voc":        ("YOUR_DRIVE_ID_HERE", "folder", None),
    "378_396baijiu":         ("YOUR_DRIVE_ID_HERE", "folder", None),
    "397_398silicon":        ("YOUR_DRIVE_ID_HERE", "folder", None),
    "399_405steel_pipe":     ("YOUR_DRIVE_ID_HERE", "folder", None),
    "406_542VisA":           ("YOUR_DRIVE_ID_HERE", "folder", None),
    "543_551_ic_chip":       ("YOUR_DRIVE_ID_HERE", "folder", None),
    "552_557tungsten_gas":   ("YOUR_DRIVE_ID_HERE", "folder", None),
    "558_559semiconductor":  ("YOUR_DRIVE_ID_HERE", "folder", None),
    "560_561concrete":       ("YOUR_DRIVE_ID_HERE", "folder", None),
    "562_563iccad":          ("YOUR_DRIVE_ID_HERE", "folder", None),
    "570gear":               ("YOUR_DRIVE_ID_HERE", "folder", None),
    "571watercooled":        ("YOUR_DRIVE_ID_HERE", "folder", None),
    "572real-iad":           ("YOUR_DRIVE_ID_HERE", "folder", None),
}


# ------------------------------------------------------------------ #
# 2.  DOWNLOAD HELPERS                                                 #
# ------------------------------------------------------------------ #
def _ensure_gdown():
    try:
        import gdown
        return gdown
    except ImportError:
        print("[ERROR] gdown not found. Install it with:  pip install gdown")
        sys.exit(1)


def download_domain(drive_id: str, drive_type: str, dest_dir: Path, domain: str) -> bool:
    """Download a folder or file from Google Drive using gdown."""
    gdown = _ensure_gdown()

    if drive_type == "folder":
        print(f"  Downloading folder: {domain} ...")
        gdown.download_folder(id=drive_id, output=str(dest_dir), quiet=False)
        return (dest_dir / domain).exists() or dest_dir.exists()
    else:
        # single file (zip or archive)
        zip_dest = dest_dir / f"{domain}.zip"
        print(f"  Downloading file: {domain} ...")
        gdown.download(id=drive_id, output=str(zip_dest), quiet=False, fuzzy=True)
        return zip_dest.exists()


def verify_md5(path: Path, expected: str) -> bool:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    actual = h.hexdigest()
    if actual != expected:
        print(f"  [WARN] MD5 mismatch for {path.name}: expected {expected}, got {actual}")
        return False
    return True


def extract_zip(zip_path: Path, output_dir: Path):
    print(f"  Extracting {zip_path.name} ...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(output_dir)
    zip_path.unlink()  # remove zip after extraction


# ------------------------------------------------------------------ #
# 3.  PREPROCESSING: build a unified manifest                         #
# ------------------------------------------------------------------ #
def build_manifest(data_dir: Path, output_path: Path):
    """
    Walk through all domain folders and collect every sample into a
    single JSONL manifest with fields:
        domain, image_path, annotation_path (if any)
    """
    records = []
    for domain_dir in sorted(data_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        domain = domain_dir.name
        images = (
            list(domain_dir.rglob("*.jpg"))
            + list(domain_dir.rglob("*.png"))
            + list(domain_dir.rglob("*.jpeg"))
        )
        for img in sorted(images):
            ann_json = img.with_suffix(".json")
            ann_csv  = img.with_suffix(".csv")
            ann = ann_json if ann_json.exists() else (ann_csv if ann_csv.exists() else None)
            records.append({
                "domain":          domain,
                "image_path":      str(img.relative_to(data_dir)),
                "annotation_path": str(ann.relative_to(data_dir)) if ann else None,
            })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")

    print(f"\n  Manifest saved -> {output_path}  ({len(records)} samples)")
    return records


def print_stats(records):
    from collections import Counter
    domains = Counter(r["domain"] for r in records)
    print(f"\n{'Domain':<35} {'Samples':>8}")
    print("-" * 45)
    for d, n in sorted(domains.items()):
        print(f"  {d:<33} {n:>8,}")
    print("-" * 45)
    print(f"  {'TOTAL':<33} {sum(domains.values()):>8,}")


# ------------------------------------------------------------------ #
# 4.  MAIN                                                             #
# ------------------------------------------------------------------ #
def parse_args():
    p = argparse.ArgumentParser(description="IMDD-1M dataset downloader & preprocessor")
    p.add_argument("--output_dir", type=str, default="./data",
                   help="Root directory to save the dataset (default: ./data)")
    p.add_argument("--domain", type=str, default=None,
                   help="Download a single domain only (e.g. --domain 266_353mvtec)")
    p.add_argument("--verify_only", action="store_true",
                   help="Skip download; only rebuild manifest and print stats")
    p.add_argument("--no_manifest", action="store_true",
                   help="Skip manifest generation")
    return p.parse_args()


def main():
    args = parse_args()
    data_dir = Path(args.output_dir)
    data_dir.mkdir(parents=True, exist_ok=True)

    if args.domain and args.domain not in DOMAIN_REGISTRY:
        print(f"[ERROR] Unknown domain '{args.domain}'. Available: {list(DOMAIN_REGISTRY)}")
        sys.exit(1)

    domains_to_fetch = (
        {args.domain: DOMAIN_REGISTRY[args.domain]}
        if args.domain else DOMAIN_REGISTRY
    )

    # ---- download -------------------------------------------------- #
    if not args.verify_only:
        for domain, (drive_id, drive_type, expected_md5) in domains_to_fetch.items():
            if drive_id == "YOUR_DRIVE_ID_HERE":
                print(f"  [SKIP] {domain}: Drive ID not configured yet.")
                continue
            domain_dir = data_dir / domain
            if domain_dir.exists():
                print(f"  [SKIP] {domain}: already exists.")
                continue
            ok = download_domain(drive_id, drive_type, data_dir, domain)
            if not ok:
                print(f"  [ERROR] Failed to download {domain}.")
                continue
            # extract zip if file type
            zip_path = data_dir / f"{domain}.zip"
            if zip_path.exists():
                print(f"  Extracting {domain} ...")
                with zipfile.ZipFile(zip_path, "r") as z:
                    z.extractall(data_dir / domain)
                zip_path.unlink()
            if expected_md5:
                verify_md5(data_dir / domain, expected_md5)
            print(f"  [OK] {domain} ready.")

    # ---- manifest -------------------------------------------------- #
    if not args.no_manifest:
        manifest_path = data_dir / "imdd1m_manifest.jsonl"
        records = build_manifest(data_dir, manifest_path)
        print_stats(records)

    print("\nDone. Dataset is ready at:", data_dir.resolve())


if __name__ == "__main__":
    main()
