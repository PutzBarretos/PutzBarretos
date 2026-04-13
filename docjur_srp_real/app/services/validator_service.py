from app.services.template_service import REQUIRED_SECTIONS


def validate_project(project: dict) -> dict:
    falhas = []
    compiled = project.get("compiled", {})
    structure = compiled.get("structure", [])
    for section in REQUIRED_SECTIONS:
        if section not in structure:
            falhas.append(f"Falta seção obrigatória: {section}")

    poc_text = " ".join(project.get("poc", {}).get("checklist", []))
    if "Priorização de risco" not in poc_text:
        falhas.append("POC sem priorização de risco.")
    if "Apoio à decisão clínica rastreável" not in poc_text:
        falhas.append("POC sem apoio à decisão clínica rastreável.")

    territory = project.get("territory", {})
    if territory.get("populacao") and not territory.get("fonte"):
        falhas.append("Dado territorial sem fonte oficial/verificável.")

    anti_glosa = " ".join(project.get("anti_glosa", {}).get("matriz", []))
    if "Vedada glosa automática" not in anti_glosa:
        falhas.append("Matriz anti-glosa insuficiente.")

    score = max(0, 100 - len(falhas) * 15)
    return {
        "status": "approved" if not falhas else "reproved",
        "score": score,
        "falhas": falhas,
        "publicabilidade": "modelo real para publicação" if score >= 70 else "reprovado",
    }
