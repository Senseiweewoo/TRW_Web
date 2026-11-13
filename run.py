import os
import sys

# Ensure the inner application directory is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, "TRW_Web")
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from app import app

if __name__ == "__main__":
    print("Starting School Library Web Application...")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)
