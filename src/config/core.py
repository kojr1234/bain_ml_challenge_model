from pathlib import Path

import src

SOURCE_ROOT = Path(src.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent()
DATASET_DIR = PACKAGE_ROOT / 'data'