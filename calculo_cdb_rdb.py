def calcular_rendimento_cdb(valor_investido, taxa_di, dias):
    """
    Calcula o rendimento de um investimento em CDB / RDB.
    """
    if valor_investido <= 0 or dias <= 0:
        raise ValueError("O valor investido e o número de dias devem ser maiores que zero.")
    
    taxa_diaria = (1 + taxa_di / 100) ** (1 / 365) - 1  # Converte a taxa DI anual para diária
    valor_final = valor_investido * ((1 + taxa_diaria) ** dias)
    return valor_final

def calcular_iof(valor_investido, rendimento_bruto, dias):
    """
    Calcula o IOF (Imposto sobre Operações Financeiras) com base no prazo em dias.
    A alíquota diminui progressivamente conforme a tabela fornecida.
    """
    if valor_investido <= 0 or rendimento_bruto < 0 or dias < 0:
        raise ValueError("O valor investido, rendimento bruto e o número de dias devem ser maiores que zero.")
    
    tabela_iof = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80,
        7: 76, 8: 73, 9: 70, 10: 66, 11: 63, 12: 60,
        13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40,
        19: 36, 20: 33, 21: 30, 22: 26, 23: 23, 24: 20,
        25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
    }
    
    percentual_iof = 0
    for dia_limite, aliquota in sorted(tabela_iof.items()):
        if dias <= dia_limite:
            percentual_iof = aliquota
            break
    
    percentual_iof /= 100
    return rendimento_bruto * percentual_iof

def calcular_aliquota_ir(dias):
    """
    Calcula a alíquota de Imposto de Renda (IR) com base no prazo em dias.
    """
    if dias <= 0:
        raise ValueError("O número de dias deve ser maior que zero.")
    
    if dias <= 180:
        return 22.5
    elif dias <= 360:
        return 20
    elif dias <= 720:
        return 17.5
    else:
        return 15