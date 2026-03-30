import os,shutil, pathlib
from PIL import Image

org_dir = pathlib.Path("2-Kuvantunnistus/original-images")
new_dir = pathlib.Path("2-Kuvantunnistus/images")

def make_subset(subset_name: str, filenames: list):
    for category in ["mug"]:
        dir = new_dir / subset_name / category
        os.makedirs(dir, exist_ok=True)
        for fname in filenames:
            shutil.copyfile(src=org_dir / fname, dst=dir / fname)
            
            
mug_files = [f for f in os.listdir(org_dir) if f.startswith("mug") and f.endswith(".jpg")]
make_subset("train", mug_files[:10])
make_subset("validation", mug_files[10:15])
make_subset("test", mug_files[15:20])