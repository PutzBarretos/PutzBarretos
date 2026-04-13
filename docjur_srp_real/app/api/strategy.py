from fastapi import APIRouter, HTTPException

from app.api._utils import persist, require_project
from app.services.strategy_service import PROFILES, simulate

router = APIRouter()


@router.post('/projects/{project_id}/strategy/simulate')
def run_simulation(project_id: str) -> dict:
    project = require_project(project_id)
    valor_global = float(project.get('general', {}).get('valor_global', 0) or 0)
    tipo_ente = project.get('territory', {}).get('tipo_ente', 'municipio')
    result = simulate(valor_global, tipo_ente)
    project['strategy'] = result
    persist(project)
    return result


@router.get('/projects/{project_id}/strategy/options')
def options(project_id: str) -> dict:
    return require_project(project_id).get('strategy', {})


@router.post('/projects/{project_id}/strategy/select')
def select(project_id: str, payload: dict) -> dict:
    project = require_project(project_id)
    choice = payload.get('choice')
    if choice not in PROFILES:
        raise HTTPException(status_code=400, detail='Cenário inválido')
    project.setdefault('strategy', {})['selected'] = choice
    persist(project)
    return project['strategy']
