import os
import sys

# Ensure inner application directory is available on Python path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
trw_dir = os.path.join(base_dir, "TRW_Web")
if trw_dir not in sys.path:
    sys.path.insert(0, trw_dir)

from app import app
