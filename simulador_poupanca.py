import requests


def obter_taxa_poupanca():
    """
        Obtém a taxa Popança mais atualizada disponível pelo Banco Central do Brasil.
    """
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.195/dados/ultimos/1?formato=json'

    try:
        response = requests.get(url)
        response.raise_for_status()

        taxa = response.json()[0]['valor']
        return float(taxa)
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")

    except (KeyError, IndexError) as e:
        print(f"Erro ao processar resposta: {e}")

    return None


def calcular_rendimento_poupanca(valor_investido, taxa_mensal, meses):
    """
        Calcula o rendimento de um investimento na Poupança.
    """
    taxa_poupaca = taxa_mensal / 100

    rendimento_bruto = valor_investido

    for _ in range(meses):
        rendimento_bruto += rendimento_bruto * taxa_poupaca

    return rendimento_bruto


def interacao_usuario():
    """
        Usuário fornece as informações como: Valor de investimento e prazo.
    """
    try:
        valor_investido = float(input("Qual o valor inicial da aplicação: R$ "))
        meses = int(input("Quanto tempo o valor ficará investido (em meses): "))
    
        if valor_investido <= 0 or meses <= 0:
            raise ValueError("O valor investido e o número de meses devem ser maiores que zero.")
        
        taxa_poupanca = obter_taxa_poupanca()

        if taxa_poupanca is not None:
            rendimento_liquido = calcular_rendimento_poupanca(valor_investido, taxa_poupanca, meses)

            rendimento_bruto = rendimento_liquido - valor_investido

            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido:.2f}")

    except ValueError as ve:
        print(f"Erro: {ve}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição HTTP: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    interacao_usuario()
