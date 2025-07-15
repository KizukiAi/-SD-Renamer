import os
from pathlib import Path

def rename_files_to_match(source_dir, target_dir):
    """
    Renames files in target directory to match corresponding files in source directory.
    Source files are sorted alphabetically, target files by modification date.
    """
    # Verify paths exist
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    if not source_path.exists():
        print(f"ERROR: Source directory does not exist: {source_dir}")
        return
    if not target_path.exists():
        print(f"ERROR: Target directory does not exist: {target_dir}")
        return
    
    # Sort files differently in each directory
    source_files = sorted(source_path.iterdir(), key=lambda x: x.name)  # Sort by name
    target_files = sorted(target_path.iterdir(), key=os.path.getmtime)  # Sort by date
    
    if len(source_files) != len(target_files):
        print(f"WARNING: Different file counts - Source: {len(source_files)}, Target: {len(target_files)}")
        return
    
    # Rename files while preserving original extensions
    for src_file, tgt_file in zip(source_files, target_files):
        if src_file.is_file() and tgt_file.is_file():
            new_name = tgt_file.with_name(src_file.name).with_suffix(src_file.suffix)
            
            # Handle name conflicts
            if new_name.exists():
                temp_name = tgt_file.with_name(f"temp_{tgt_file.name}")
                tgt_file.rename(temp_name)
                tgt_file = temp_name
            
            tgt_file.rename(new_name)
            print(f"Renamed: {tgt_file.name} -> {new_name.name}")

# Configure your paths here
source_dir = r"ENTER_TARGET_PATH_HERE"  # Directory with original filenames
target_dir = r"ENTER_TARGET_PATH_HERE"  # Directory with files to be renamed

rename_files_to_match(source_dir, target_dir)