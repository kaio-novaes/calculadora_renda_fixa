def calcular_rendimento_lcx(valor_investido, taxa_di, dias):
    """
    Calcula o rendimento de um investimento em LCI/LCA.
    """
    taxa_diaria = (1 + taxa_di / 100) ** (1 / 365) - 1  # Converte a taxa DI anual para diária
    valor_final = valor_investido * ((1 + taxa_diaria) ** dias)
    return valor_final
