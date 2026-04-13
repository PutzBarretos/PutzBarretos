from typing import Any


def fetch_epidemiology(uf: str) -> dict[str, Any]:
    # Nesta fase, apenas baseline com fonte explícita para evitar "sem fonte, sem número".
    if uf.upper() in {"RN", "AP"}:
        return {
            "incidencia_estimativa": None,
            "observacao": "Dados epidemiológicos detalhados pendentes de integração automática com base oficial INCA/DATASUS.",
            "fonte": "Integração oficial pendente",
        }
    return {"incidencia_estimativa": None, "observacao": "Sem fonte oficial disponível nesta instância.", "fonte": None}
