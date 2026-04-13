import json
from pathlib import Path

from app.config import OUTPUT_DIR


def export_project(project: dict) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pid = project["id"]
    json_path = OUTPUT_DIR / f"{pid}.json"
    docx_path = OUTPUT_DIR / f"{pid}.docx"
    pdf_path = OUTPUT_DIR / f"{pid}.pdf"

    json_path.write_text(json.dumps(project, ensure_ascii=False, indent=2), encoding="utf-8")
    docx_path.write_bytes(b"DOCX_PLACEHOLDER")
    pdf_path.write_bytes(b"%PDF-1.4\n% placeholder\n")

    return {"json": str(json_path), "docx": str(docx_path), "pdf": str(pdf_path)}
