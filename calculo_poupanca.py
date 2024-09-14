def calcular_rendimento_poupanca(valor_investido, taxa_mensal, meses):
    """
    Calcula o rendimento de um investimento na Poupança.
    """
    taxa_poupanca = taxa_mensal / 100
    rendimento_bruto = valor_investido

    for _ in range(meses):
        rendimento_bruto += rendimento_bruto * taxa_poupanca

    return rendimento_bruto
