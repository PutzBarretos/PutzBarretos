from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api import compile as compile_api
from app.api import export, finance, health, poc, projects, qualification, strategy, technical_spec, territory, validate
from app.services.storage import init_db
from app.services.template_service import ensure_master_template

app = FastAPI(title='DocJur SRP/ARP Municipal')


@app.on_event('startup')
def startup() -> None:
    init_db()
    ensure_master_template()


frontend_dir = Path(__file__).resolve().parent / 'frontend'
app.mount('/assets', StaticFiles(directory=frontend_dir), name='assets')


@app.get('/', include_in_schema=False)
def root() -> FileResponse:
    return FileResponse(frontend_dir / 'index.html')


app.include_router(health.router)
app.include_router(projects.router)
app.include_router(territory.router)
app.include_router(strategy.router)
app.include_router(finance.router)
app.include_router(qualification.router)
app.include_router(technical_spec.router)
app.include_router(poc.router)
app.include_router(compile_api.router)
app.include_router(validate.router)
app.include_router(export.router)
