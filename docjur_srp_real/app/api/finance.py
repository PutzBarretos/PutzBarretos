import uuid

from fastapi import APIRouter, HTTPException

from app.api._utils import persist, require_project
from app.services.finance_service import brl

router = APIRouter()


@router.post('/projects/{project_id}/items')
def add_item(project_id: str, payload: dict) -> dict:
    project = require_project(project_id)
    item = {
        'id': str(uuid.uuid4()),
        'nome': payload.get('nome'),
        'unidade': payload.get('unidade'),
        'quantidade_maxima': payload.get('quantidade_maxima', 0),
        'valor_unitario_referencia': payload.get('valor_unitario_referencia', 0.0),
        'natureza': payload.get('natureza', ''),
        'peso_cenario': payload.get('peso_cenario', 0),
    }
    total = float(item['quantidade_maxima']) * float(item['valor_unitario_referencia'])
    item['total_calculado'] = total
    item['total_formatado'] = brl(total)
    project.setdefault('items', []).append(item)
    persist(project)
    return item


@router.patch('/projects/{project_id}/items/{item_id}')
def update_item(project_id: str, item_id: str, payload: dict) -> dict:
    project = require_project(project_id)
    for item in project.get('items', []):
        if item['id'] == item_id:
            for key in ['nome', 'unidade', 'quantidade_maxima', 'valor_unitario_referencia', 'natureza', 'peso_cenario']:
                if key in payload:
                    item[key] = payload[key]
            total = float(item['quantidade_maxima']) * float(item['valor_unitario_referencia'])
            item['total_calculado'] = total
            item['total_formatado'] = brl(total)
            persist(project)
            return item
    raise HTTPException(status_code=404, detail='Item não encontrado')


@router.delete('/projects/{project_id}/items/{item_id}')
def delete_item(project_id: str, item_id: str) -> dict:
    project = require_project(project_id)
    old = len(project.get('items', []))
    project['items'] = [i for i in project.get('items', []) if i['id'] != item_id]
    if len(project['items']) == old:
        raise HTTPException(status_code=404, detail='Item não encontrado')
    persist(project)
    return {'status': 'deleted'}
