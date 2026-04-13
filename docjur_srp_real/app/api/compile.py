from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.anti_glosa_service import build_anti_glosa
from app.services.compiler_service import compile_document

router = APIRouter()


@router.post('/projects/{project_id}/anti-glosa')
def anti_glosa(project_id: str) -> dict:
    project = require_project(project_id)
    project['anti_glosa'] = build_anti_glosa()
    persist(project)
    return project['anti_glosa']


@router.post('/projects/{project_id}/compile')
def compile_project(project_id: str) -> dict:
    project = require_project(project_id)
    project['compiled'] = compile_document(project)
    persist(project)
    return project['compiled']
