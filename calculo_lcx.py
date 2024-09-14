def calcular_rendimento_lcx(valor_investido, taxa_di, meses):
    """
    Calcula o rendimento de um investimento em LCI/LCA.
    """
    taxa_diaria = (1 + taxa_di / 100) ** (1 / 12) - 1  # Converte a taxa DI obtida para diária.
    valor_final = valor_investido

    for _ in range(meses):
        valor_final *= (1 + taxa_diaria)

    return valor_final
