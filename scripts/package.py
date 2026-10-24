#!/usr/bin/env python3
"""offer-coach 打包脚本：版本号自动递增 + 手册版本同步 + zip 产出。

用法：
    python scripts/package.py              # patch 递增并打包（v1.0.0 -> v1.0.1）
    python scripts/package.py --minor      # minor 递增
    python scripts/package.py --major      # major 递增
    python scripts/package.py --no-bump    # 不递增，按当前版本重新打包
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = REPO_ROOT / "VERSION"
SKILL_DIR = REPO_ROOT / "offer-coach"
DIST_DIR = REPO_ROOT / "dist"
MANUALS = [REPO_ROOT / "docs" / "用户手册.md", REPO_ROOT / "docs" / "技术手册.md"]

# 打包时排除：鲁班优化数据文件与临时产物
EXCLUDE_NAMES = {
    "results.tsv", "diagnostics.tsv", "test-prompts.json",
    "rejected_edits.md", "hardening_report.json", "distill_report.json",
}
EXCLUDE_SUFFIXES = {".bak"}


def read_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip().lstrip("v")


def bump(version: str, part: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def write_version(v: str) -> None:
    VERSION_FILE.write_text(f"v{v}\n", encoding="utf-8")


def sync_manuals(v: str) -> None:
    """手册首页的版本行统一改写为当前版本（行首格式：> 版本：vX.Y.Z）"""
    pat = re.compile(r"^(>?\s*版本[：:]\s*)v[\d.]+\s*(.*)$")
    for doc in MANUALS:
        if not doc.exists():
            print(f"[warn] 手册缺失，跳过同步：{doc}")
            continue
        lines = doc.read_text(encoding="utf-8").splitlines()
        hit = False
        for i, line in enumerate(lines):
            m = pat.match(line)
            if m:
                lines[i] = f"{m.group(1)}v{v}{m.group(2)}"
                hit = True
                break
        if not hit and lines:
            lines.insert(1, f"\n> 版本：v{v}")
        doc.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"[sync] {doc.name} -> v{v}")


def make_zip(v: str) -> Path:
    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / f"offer-coach-v{v}.zip"
    if out.exists():
        out.unlink()
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(SKILL_DIR.rglob("*")):
            if p.is_dir():
                continue
            if p.name in EXCLUDE_NAMES or p.suffix in EXCLUDE_SUFFIXES:
                continue
            zf.write(p, Path("offer-coach") / p.relative_to(SKILL_DIR))
            count += 1
    print(f"[zip] {out}（{count} 个文件）")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--minor", action="store_true")
    ap.add_argument("--major", action="store_true")
    ap.add_argument("--no-bump", action="store_true")
    args = ap.parse_args()

    part = "major" if args.major else "minor" if args.minor else "patch"
    old = read_version()
    new = old if args.no_bump else bump(old, part)
    print(f"[version] v{old} -> v{new}（{part}）")
    if not SKILL_DIR.is_dir():
        print(f"[error] 技能目录不存在：{SKILL_DIR}")
        return 1
    if not args.no_bump:
        write_version(new)
    sync_manuals(new)
    out = make_zip(new)
    print(f"[done] {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
