import requests

def obter_taxa_poupanca():
    """
    Obtém a taxa Poupança mais atualizada disponível pelo Banco Central do Brasil.
    """
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.195/dados/ultimos/1?formato=json'
    return obter_taxa(url)

def obter_taxa_di():
    """
    Obtém a taxa DI mais atualizada disponível pelo Banco Central do Brasil.
    """
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/1?formato=json'
    return obter_taxa(url)

def obter_taxa(url):
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
