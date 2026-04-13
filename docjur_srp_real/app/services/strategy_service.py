from typing import Any

PROFILES = {
    "assistencial": {
        "resumo": "Prioriza triagem, priorização de risco, laudo remoto e apoio clínico rastreável.",
        "vantagens": ["Resposta clínica mais rápida", "Maior foco no núcleo assistencial"],
        "riscos": ["Menor investimento inicial em expansão territorial"],
        "pesos": {"assistencial": 0.55, "estruturacao": 0.30, "territorio": 0.15},
    },
    "estruturante": {
        "resumo": "Prioriza implantação, treinamento, governança e consolidação operacional.",
        "vantagens": ["Base operacional robusta", "Maior previsibilidade de execução"],
        "riscos": ["Retorno assistencial imediato mais lento"],
        "pesos": {"assistencial": 0.35, "estruturacao": 0.50, "territorio": 0.15},
    },
    "territorial": {
        "resumo": "Prioriza cobertura geográfica, capilaridade e mobilização territorial.",
        "vantagens": ["Maior alcance populacional", "Apoio a mutirões e campanhas"],
        "riscos": ["Demanda logística e coordenação elevadas"],
        "pesos": {"assistencial": 0.40, "estruturacao": 0.20, "territorio": 0.40},
    },
}


def simulate(valor_global: float, tipo_ente: str) -> dict[str, Any]:
    options = []
    suggested = "assistencial" if tipo_ente == "municipio" else "estruturante"
    reason = "Perfil municipal com maior benefício imediato na fila assistencial e priorização de risco."
    for name, profile in PROFILES.items():
        p = profile["pesos"]
        options.append(
            {
                "id": name,
                "resumo": profile["resumo"],
                "vantagens": profile["vantagens"],
                "riscos": profile["riscos"],
                "distribuicao": {
                    "assistencial": valor_global * p["assistencial"],
                    "estruturacao": valor_global * p["estruturacao"],
                    "territorio": valor_global * p["territorio"],
                },
            }
        )
    return {"options": options, "suggested": suggested, "why": reason}
