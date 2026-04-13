from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROJECTS_DIR = DATA_DIR / "projects"
OUTPUT_DIR = DATA_DIR / "output"
DB_PATH = DATA_DIR / "docjur.db"
FRONTEND_DIR = BASE_DIR / "app" / "frontend"
TEMPLATE_MASTER_PATH = BASE_DIR / "app" / "templates" / "arp_master" / "ARP_Modelo - VF_final.md"

for directory in [DATA_DIR, PROJECTS_DIR, OUTPUT_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
