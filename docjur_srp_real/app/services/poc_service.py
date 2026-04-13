
def build_poc() -> dict:
    checklist = [
        "Cadastro e anamnese",
        "Captura estruturada",
        "Associação entre caso e imagem",
        "Priorização de risco",
        "Apoio à decisão clínica rastreável",
        "Laudo remoto",
        "Relatórios/exportações",
        "Logs, perfis e segurança",
        "Suporte e continuidade",
    ]
    eliminatorios = [
        "Reprovar se não prioriza casos.",
        "Reprovar se não há apoio à decisão clínica rastreável.",
        "Reprovar se apoio à decisão substitui ato médico.",
        "Reprovar se não associa imagem e caso adequadamente.",
        "Reprovar se não emite laudo/devolutiva em fluxo auditável.",
    ]
    return {
        "checklist": checklist,
        "eliminatorios": eliminatorios,
        "portaria": "Minuta de portaria com comissão titular/suplente, competências formais e regra de substituição.",
        "comunicado": "Minuta de comunicado oficial de nomeação da comissão da POC.",
        "subcomissoes": [
            "Captura clínica e campo",
            "Backoffice, priorização e laudo",
            "Segurança, logs e relatórios",
            "Implantação, treinamento e suporte",
        ],
    }
