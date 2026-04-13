from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.technical_spec_service import build_technical_spec

router = APIRouter()


@router.post('/projects/{project_id}/technical-spec')
def generate(project_id: str) -> dict:
    project = require_project(project_id)
    project['technical_spec'] = build_technical_spec()
    persist(project)
    return project['technical_spec']
