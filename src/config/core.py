from pathlib import Path

import src

SOURCE_ROOT = Path(src.__file__).resolve().parent
ROOT = SOURCE_ROOT.parent
DATASET_DIR = SOURCE_ROOT / "data"