def brl(value: float) -> str:
    inteiro, decimal = f"{value:.2f}".split(".")
    inteiro_formatado = ""
    while inteiro:
        inteiro_formatado = ("." + inteiro[-3:] + inteiro_formatado) if inteiro_formatado else inteiro[-3:]
        inteiro = inteiro[:-3]
    return f"R$ {inteiro_formatado},{decimal}"
