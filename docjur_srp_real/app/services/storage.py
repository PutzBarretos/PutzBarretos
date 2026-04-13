import json
import sqlite3
import uuid
from datetime import datetime
from typing import Any

from app.config import DB_PATH


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = _conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def create_project(payload: dict[str, Any]) -> dict[str, Any]:
    project_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    record = {
        "id": project_id,
        "general": payload,
        "territory": {},
        "strategy": {},
        "items": [],
        "qualification": {},
        "technical_spec": {},
        "poc": {},
        "anti_glosa": {},
        "compiled": {},
        "validation": {},
        "exports": {},
    }
    conn = _conn()
    conn.execute(
        "INSERT INTO projects (id, payload, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (project_id, json.dumps(record, ensure_ascii=False), now, now),
    )
    conn.commit()
    conn.close()
    return record


def get_project(project_id: str) -> dict[str, Any] | None:
    conn = _conn()
    row = conn.execute("SELECT payload FROM projects WHERE id = ?", (project_id,)).fetchone()
    conn.close()
    return json.loads(row["payload"]) if row else None


def save_project(project: dict[str, Any]) -> dict[str, Any]:
    now = datetime.utcnow().isoformat()
    conn = _conn()
    conn.execute(
        "UPDATE projects SET payload = ?, updated_at = ? WHERE id = ?",
        (json.dumps(project, ensure_ascii=False), now, project["id"]),
    )
    conn.commit()
    conn.close()
    return project
