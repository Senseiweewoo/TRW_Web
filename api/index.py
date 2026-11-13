import os
import sys

# Ensure application directories are on python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
TRW_DIR = os.path.join(PARENT_DIR, "TRW_Web")

for path in [PARENT_DIR, TRW_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

from app import app
