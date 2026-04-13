from app.services.template_service import get_master_structure


def compile_document(project: dict) -> dict:
    structure = get_master_structure()
    compiled = {
        "structure": structure,
        "status": "compiled",
        "preview": [f"{idx+1}. {section}" for idx, section in enumerate(structure)],
        "project_id": project["id"],
    }
    return compiled
