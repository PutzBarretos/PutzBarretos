from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.qualification_service import build_qualification

router = APIRouter()


@router.post('/projects/{project_id}/qualification')
def generate(project_id: str) -> dict:
    project = require_project(project_id)
    project['qualification'] = build_qualification()
    persist(project)
    return project['qualification']
