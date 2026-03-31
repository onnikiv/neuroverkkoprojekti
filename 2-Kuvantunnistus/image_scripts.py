import os, shutil, pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
org_dir = BASE_DIR / "original-images" / "mug-images"
new_dir = BASE_DIR / "images"

def make_subset(subset_name: str, filenames: list):
    for category in ["mug"]:
        subset_dir = new_dir / subset_name / category
        os.makedirs(subset_dir, exist_ok=True)
        for fname in filenames:
            shutil.copyfile(src=org_dir / fname, dst=subset_dir / fname)
            
            
mug_files = [f for f in os.listdir(org_dir) if f.startswith("mug") and f.endswith(".png")]
if not mug_files:
    raise FileNotFoundError(f"No mug image files found in {org_dir}")

make_subset("train", mug_files[:10])
make_subset("validation", mug_files[10:15])
make_subset("test", mug_files[15:20])