import os
import shutil
from pathlib import Path

# === CONFIG ===
folder1 = Path("C:/Users/Milsort/Dropbox/computer_vision/semantic_segmentation/data/wheat/all_training_data/tiled_data/filtered")
folder2 = Path("C:/Users/Milsort/Dropbox/computer_vision/semantic_segmentation/data/wheat/validation_data/10")
destination = Path("C:/Users/Milsort/Dropbox/computer_vision/semantic_segmentation/data/wheat/validation_data/Input_images")

# === VALIDATE PATHS ===
if not folder1.exists():
    raise FileNotFoundError(f"❌ Source folder1 not found: {folder1}")
if not folder2.exists():
    raise FileNotFoundError(f"❌ Reference folder2 not found: {folder2}")
destination.mkdir(parents=True, exist_ok=True)

# === Collect reference filenames from folder2 ===
ref_names = {
    f.stem.lower()
    for f in folder2.iterdir()
    if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
}

# === Process and copy matching files from folder1 ===
copied = 0
for file in folder1.iterdir():
    if file.is_file() and file.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}:
        if file.stem.lower() in ref_names:
            shutil.copy2(file, destination)
            print(f"✅ Copied: {file.name}")
            copied += 1

print(f"🚀 Image sync complete. {copied} files copied.")
