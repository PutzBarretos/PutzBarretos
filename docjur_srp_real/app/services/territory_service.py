from typing import Any

MUNICIPIOS = {
    ("natal", "RN"): {"ente_oficial": "Município de Natal", "ibge": "2408102", "populacao": 751300, "fonte": "IBGE Cidades"},
    ("macapa", "AP"): {"ente_oficial": "Município de Macapá", "ibge": "1600303", "populacao": 522357, "fonte": "IBGE Cidades"},
}


def resolve_ente(ente: str, uf: str) -> dict[str, Any]:
    key = (ente.strip().lower(), uf.strip().upper())
    data = MUNICIPIOS.get(key)
    if data:
        return {
            "ente_resolvido": data["ente_oficial"],
            "tipo_ente": "municipio",
            "uf": uf.upper(),
            "codigo_ibge": data["ibge"],
            "fonte": data["fonte"],
        }
    return {
        "ente_resolvido": ente,
        "tipo_ente": "municipio" if ente else "nao_resolvido",
        "uf": uf.upper(),
        "codigo_ibge": None,
        "fonte": None,
    }


def classify_base(context: dict[str, Any]) -> str:
    if context.get("codigo_ibge") and context.get("populacao") and context.get("fonte"):
        return "completa"
    if context.get("codigo_ibge") or context.get("fonte"):
        return "parcial"
    return "insuficiente"
