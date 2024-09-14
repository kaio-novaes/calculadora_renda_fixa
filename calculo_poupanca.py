def calcular_rendimento_poupanca(valor_investido, taxa_mensal, dias):
    """
    Calcula o rendimento de um investimento na Poupança.
    """
    taxa_poupanca_diaria = (1 + taxa_mensal / 100) ** (1 / 30.41) - 1  # Converte a taxa mensal para diária
    rendimento_bruto = valor_investido * (1 + taxa_poupanca_diaria) ** dias
    return rendimento_bruto
