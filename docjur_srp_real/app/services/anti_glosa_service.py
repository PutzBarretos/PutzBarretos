
def build_anti_glosa() -> dict:
    matriz = [
        "Vedada glosa automática por meta quantitativa isolada.",
        "Vedada perda integral do item nuclear por simples não atingimento de meta.",
        "Exigir causalidade, proporcionalidade, motivação e imputabilidade.",
        "Avaliar Item 1 por estrutura assistencial disponibilizada e evidências do Anexo VII.",
    ]
    os_model = {
        "campos": [
            "contratante",
            "contratada",
            "item_frente_acionada",
            "finalidade_executiva",
            "local_abrangencia",
            "periodo",
            "quantitativos_limites",
            "evidencias_minimas",
            "responsaveis",
        ]
    }
    return {"matriz": matriz, "ordem_servico": os_model, "diretrizes": "Uso da OS com rastreabilidade e vínculo a evidências de execução."}
