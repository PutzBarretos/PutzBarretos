from fastapi import APIRouter, HTTPException

from app.services.storage import create_project, get_project

router = APIRouter()


@router.post('/projects')
def create(payload: dict) -> dict:
    return create_project(payload)


@router.get('/projects/{project_id}')
def get(project_id: str) -> dict:
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail='Projeto não encontrado')
    return project
