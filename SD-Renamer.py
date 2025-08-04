import os
import re
from pathlib import Path
from datetime import datetime

# ===== SORTING METHODS =====
def sort_by_name(file):
    """Sort files alphabetically by name (case-insensitive)."""
    return file.name.lower()

def sort_by_extension(file):
    """Sort files by extension, then by name."""
    return (file.suffix.lower(), file.name.lower())

def sort_by_mtime(file):
    """Sort files by modification time (oldest first)."""
    return os.path.getmtime(file)

def sort_by_ctime(file):
    """Sort files by creation time (oldest first)."""
    return os.path.getctime(file)

def sort_by_size(file):
    """Sort files by size (smallest first)."""
    return file.stat().st_size

def sort_by_numeric_part(file):
    """Sort files by the first number found in the filename."""
    match = re.search(r'\d+', file.name)
    return int(match.group()) if match else 0

# ===== DIRECTORY  =====
SOURCE_DIR = r"ENTER_SOURCE_PATH_HERE"
TARGET_DIR = r"ENTER_TARGET_PATH_HERE"

# ===== SORT METHOD =====
SORT_SOURCE = sort_by_name
SORT_TARGET = sort_by_mtime

# ===== MAIN FUNCTION =====
def rename_files_to_match(source_dir, target_dir, sort_method):
    """Renames files in target_dir to match source_dir, using the specified sorting method."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")
    if not target_path.exists():
        raise FileNotFoundError(f"Target directory not found: {target_dir}")

    # Get and sort files using the chosen method
    source_files = sorted([f for f in source_path.iterdir() if f.is_file()], key=sort_method)
    target_files = sorted([f for f in target_path.iterdir() if f.is_file()], key=sort_method)

    if len(source_files) != len(target_files):
        print(f"⚠️ WARNING: File count mismatch (Source: {len(source_files)}, Target: {len(target_files)})")

    # Backup directory
    backup_dir = target_path / "backup_original_files"
    backup_dir.mkdir(exist_ok=True)

    # Rename files
    for i, (src, tgt) in enumerate(zip(source_files, target_files)):
        new_name = tgt.with_stem(src.stem).with_suffix(src.suffix)
        backup_path = backup_dir / tgt.name

        # Create backup (if not exists)
        if not backup_path.exists():
            tgt.rename(backup_path)
            tgt = backup_path  # Update reference

        # Rename (skip if target exists)
        if new_name.exists():
            print(f"⏩ Skipped (exists): {tgt.name} → {new_name.name}")
        else:
            tgt.rename(new_name)
            print(f"✅ Renamed {i+1}/{len(source_files)}: {tgt.name} → {new_name.name}")

    print(f"\n✔️ Done! Original files backed up in: {backup_dir}")

# ===== RUN THE SCRIPT =====
if __name__ == "__main__":
    rename_files_to_match(SOURCE_DIR, TARGET_DIR, SORT_METHOD)
