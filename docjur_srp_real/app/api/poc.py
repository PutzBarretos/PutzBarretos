from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.poc_service import build_poc

router = APIRouter()


@router.post('/projects/{project_id}/poc')
def generate(project_id: str) -> dict:
    project = require_project(project_id)
    project['poc'] = build_poc()
    persist(project)
    return project['poc']
