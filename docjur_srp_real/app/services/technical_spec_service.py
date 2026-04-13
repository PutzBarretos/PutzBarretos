from typing import Any


def build_technical_spec() -> dict[str, Any]:
    blocos = {
        "plataforma": ["Registro clínico estruturado", "Associação segura entre caso e imagem", "Histórico do caso", "Fila assistencial", "Classificação e priorização"],
        "captura": ["Conjunto de captura com padrão mínimo de imagem", "Acessório óptico/dermatoscópico/lente ou equivalente", "Iluminação, foco, nitidez, estabilidade e redução de reflexos"],
        "seguranca": ["Logs, perfis e auditoria", "Criptografia", "Backup", "Continuidade"],
        "relatorios": ["Relatórios e exportações", "Integração por API/webservice ou equivalente"],
        "apoio_clinico": ["Apoio à decisão clínica rastreável, de caráter instrumental", "Laudo remoto/devolutiva estruturada"],
    }
    return {"blocos": blocos}
