from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.validator_service import validate_project

router = APIRouter()


@router.post('/projects/{project_id}/validate')
def validate(project_id: str) -> dict:
    project = require_project(project_id)
    project['validation'] = validate_project(project)
    persist(project)
    return project['validation']
