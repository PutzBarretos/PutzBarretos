from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.export_service import export_project

router = APIRouter()


@router.post('/projects/{project_id}/export')
def export(project_id: str) -> dict:
    project = require_project(project_id)
    project['exports'] = export_project(project)
    persist(project)
    return project['exports']
