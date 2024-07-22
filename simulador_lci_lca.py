import requests


def obter_taxa_lcx():
    """
        Obtém a taxa DI mais atualizada dispónivel pelo Banco Central do Brasil.
    """
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/1?formato=json'

    try:
        response = requests.get(url)
        response.raise_for_status()

        taxa = response.json()[0]['valor']
        return float(taxa)
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
    
    except KeyError as e:
        print(f"Erro ao processar resposta JSON - chave não encontrada: {e}")
    
    except IndexError as e:
        print(f"Erro ao processar resposta JSON - índice inválido: {e}")

    return None


def calcular_rendimento_lcx(valor_investido, taxa_di, meses):
    """
        Calcula o rendimento de um investimento em LCI/LCA.
    """
    taxa_diaria = (1 + taxa_di / 100) ** (1 / 12) - 1 # Converte a taxa DI obtida para diária.
    valor_final = valor_investido
    
    for _ in range(meses):
        valor_final *= (1 + taxa_diaria)

    return valor_final


def interacao_usuario():
    """
        Usuário fornece as informações como: Valor de investimento e prazo.
    """
    try:
        valor_investido = float(input("Qual o valor inicial da aplicação: R$ "))
        meses = int(input("Quanto tempo o valor ficará investido (em meses): "))
    
        if valor_investido <= 0 or meses <= 0:
            raise ValueError("O valor investido e o número de meses devem ser maiores que zero.")

        taxa_lcx = obter_taxa_lcx()

        if taxa_lcx is not None:
            rendimento_liquido = calcular_rendimento_lcx(valor_investido, taxa_lcx, meses)

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
