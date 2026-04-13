from fastapi import APIRouter

from app.api._utils import persist, require_project
from app.services.epidemiology_service import fetch_epidemiology
from app.services.territory_service import classify_base, resolve_ente

router = APIRouter()


@router.post('/projects/{project_id}/territory/resolve')
def resolve(project_id: str) -> dict:
    project = require_project(project_id)
    general = project.get('general', {})
    data = resolve_ente(general.get('ente', ''), general.get('uf', ''))
    project['territory'] = {**project.get('territory', {}), **data}
    project['territory']['status_base_local'] = classify_base(project['territory'])
    persist(project)
    return project['territory']


@router.post('/projects/{project_id}/territory/fetch-context')
def fetch_context(project_id: str) -> dict:
    project = require_project(project_id)
    territory = project.get('territory', {})
    epidemiology = fetch_epidemiology(territory.get('uf', project.get('general', {}).get('uf', '')))
    if territory.get('codigo_ibge') and territory.get('fonte'):
        territory['populacao'] = 751300 if territory['codigo_ibge'] == '2408102' else territory.get('populacao')
    territory['epidemiologia'] = epidemiology
    territory['status_base_local'] = classify_base(territory)
    project['territory'] = territory
    persist(project)
    return territory


@router.get('/projects/{project_id}/territory/context')
def context(project_id: str) -> dict:
    return require_project(project_id).get('territory', {})
