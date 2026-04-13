from typing import Any


def build_qualification() -> dict[str, Any]:
    eixos = [
        "Comprovação de solução digital em saúde com registro clínico estruturado.",
        "Comprovação de experiência em triagem dermatológica e/ou teledermatologia.",
        "Comprovação de captura clínica com dispositivo móvel e acessório óptico/dermatoscópico ou equivalente.",
        "Comprovação de implantação, treinamento e suporte operacional.",
        "Comprovação de laudo remoto e/ou campanhas territoriais, quando cabível.",
    ]
    vedacoes = [
        "Vedada exigência de mesma marca.",
        "Vedada exigência de mesmo cliente.",
        "Vedada exigência de mesma arquitetura.",
        "Vedada exigência de mesma nomenclatura comercial.",
    ]
    return {"eixos": eixos, "vedacoes": vedacoes, "texto": "\n".join(eixos + vedacoes)}
