from pathlib import Path

from app.config import TEMPLATE_MASTER_PATH

REQUIRED_SECTIONS = [
    "Edital",
    "Anexo I — Termo de Referência",
    "Anexo II — Modelo de Proposta Comercial",
    "Anexo III — Minuta de Ata de Registro de Preços",
    "Anexo IV — Requisitos Técnicos Mínimos da Solução, da Operação Assistida e do Conjunto de Captura",
    "Anexo V — Roteiro e Checklist Objetivo da POC",
    "Anexo VI — Fluxo Assistencial e Regulatório Mínimo",
    "Anexo VII — Documentos Mínimos para Aceite, Medição e Fiscalização do Item 1",
    "Anexo VIII — Minuta de Portaria de Nomeação da Comissão Técnica de Avaliação da POC",
    "Anexo IX — Minuta de Comunicado Oficial de Nomeação da Comissão de POC",
    "Anexo X — Modelo Simplificado de Ordem de Serviço",
    "Anexo XI — Diretrizes de Uso da Ordem de Serviço",
]


def ensure_master_template() -> None:
    path = Path(TEMPLATE_MASTER_PATH)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join([f"# {s}" if i == 0 else f"## {s}" for i, s in enumerate(REQUIRED_SECTIONS)]), encoding="utf-8")


def get_master_structure() -> list[str]:
    ensure_master_template()
    return REQUIRED_SECTIONS
