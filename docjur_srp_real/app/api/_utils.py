from fastapi import HTTPException

from app.services.storage import get_project, save_project


def require_project(project_id: str) -> dict:
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail='Projeto não encontrado')
    return project


def persist(project: dict) -> dict:
    return save_project(project)
