import requests


def obter_taxa_di():
    """
        Obtém a taxa DI mais atualizada dispónivel pelo Banco Central do Brasil.
    """
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/1?formato=json'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção para erros HTTP
        
        if response.text.strip():  
            taxa = response.json()[0]['valor']
            return float(taxa)
        else:
            print("Erro: resposta vazia recebida do servidor.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição HTTP: {e}")
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar resposta: {e}")
    
    return None


def calcular_rendimento_cdb(valor_investido, taxa_di, meses):
    """
        Calcula o redimento de um investimento em CDB.
    """
    taxa_diaria = (1 + taxa_di / 100) ** (1 / 12) - 1 # Converte a taxa DI obtida para diária.
    valor_final = valor_investido
    
    for _ in range(meses):
        valor_final *= (1 + taxa_diaria)
    
    return valor_final


def calcular_aliquota_ir(meses):
    """
        Calcula a alíquota de Imposto de Renda (IR) com base no prazo em meses.
    """
    if meses <= 6:
        return 22.5 # 22,5%.
    
    elif meses <= 12:
        return 20 # 20%.
    
    elif meses <= 24:
        return 17.5 # 17,5%.
    
    else:
        return 15 # Mais que isso sempre terá aliquota de 15%.


def interacao_usuario():
    """
        Usário fornece as informação como: Valor de investimento e prazo.
    """
    try:
        valor_investido = float(input("Qual o valor inicial da aplicação: R$ "))
        meses = int(input("Quanto tempo o valor ficará investido (em meses): "))
    
        if valor_investido <= 0 or meses <= 0:
            raise ValueError("O valor investido e o número de meses devem ser maiores que zero.")
        
        taxa_di = obter_taxa_di()

        if taxa_di is not None:
            rendimento_total = calcular_rendimento_cdb(valor_investido, taxa_di, meses)
            rendimento_bruto = rendimento_total - valor_investido
            aliquota_ir = calcular_aliquota_ir(meses)
            ir = rendimento_bruto * (aliquota_ir / 100)

            rendimento_liquido = valor_investido + rendimento_bruto - ir

            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto:.2f}")
            print(f"Imposto de Renda (IR) ({aliquota_ir}%): R$ {ir:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido:.2f}")

        else:
            print("Não foi possível obter a taxa DI.")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    interacao_usuario()
