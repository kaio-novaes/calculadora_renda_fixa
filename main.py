import logging
from api import obter_taxa_poupanca, obter_taxa_di
from calculo_poupanca import calcular_rendimento_poupanca
from calculo_cdb_rdb import calcular_rendimento_cdb, calcular_aliquota_ir, calcular_iof
from calculo_lcx import calcular_rendimento_lcx

logging.basicConfig(level=logging.INFO)

def converter_para_dias(periodo, unidade):
    """
    Converte o período para dias com base na unidade fornecida.
    """
    if unidade == 'dias':
        return int(periodo)
    elif unidade == 'meses':
        return int(round(periodo * 30,41666666666667))  # Média de dias por mês
    elif unidade == 'anos':
        return int(round(periodo * 365))  # Número fixo de dias por ano
    else:
        raise ValueError("Unidade inválida. Escolha entre 'dias', 'meses' ou 'anos'.")  

def interacao_usuario():
    try:
        valor_investido = float(input("Qual o valor inicial da aplicação: R$ "))
        periodo = float(input("Qual o período de investimento? "))
        unidade = input("Qual a unidade do período? (dias, meses, anos): ").strip().lower()

        # Converte o período para dias
        dias = converter_para_dias(periodo, unidade)

        if valor_investido <= 0 or dias <= 0:
            raise ValueError("O valor investido e o número de dias devem ser maiores que zero.")

        # Poupança
        taxa_poupanca = obter_taxa_poupanca()
        if taxa_poupanca is not None:
            rendimento_bruto_poupanca = calcular_rendimento_poupanca(valor_investido, taxa_poupanca, dias) - valor_investido
            rendimento_liquido_poupanca = valor_investido + rendimento_bruto_poupanca
            print("\n** Poupança **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto_poupanca:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido_poupanca:.2f}")
        else:
            print("Não foi possível obter a taxa da Poupança.")

        # CDB / RDB
        taxa_di = obter_taxa_di()
        percentual_di_cdb = 100  # O percentual DI padrão de 100 para CDBs
        if taxa_di is not None:
            rendimento_bruto_cdb = calcular_rendimento_cdb(valor_investido, taxa_di * percentual_di_cdb / 100, dias) - valor_investido
            iof = calcular_iof(valor_investido, rendimento_bruto_cdb, dias)
            rendimento_bruto_cdb_ajustado = rendimento_bruto_cdb - iof  
            aliquota_ir = calcular_aliquota_ir(dias)
            ir = rendimento_bruto_cdb_ajustado * (aliquota_ir / 100)
            rendimento_liquido_cdb = valor_investido + (rendimento_bruto_cdb_ajustado - ir)
            
            print("\n** CDB / RDB **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto_cdb + valor_investido - valor_investido:.2f}")
            if iof > 0:
                print(f"IOF: R$ {iof:.2f}")
            print(f"Imposto de Renda (IR) ({aliquota_ir}%): R$ {ir:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido_cdb:.2f}")
        else:
            print("Não foi possível obter a taxa DI.")

        # LCI / LCA
        taxa_lcx = obter_taxa_di()  
        percentual_di_lcx = 100  # O percentual DI padrão de 100 para LCI/LCA
        if taxa_lcx is not None:
            rendimento_bruto_lcx = calcular_rendimento_lcx(valor_investido, taxa_lcx * percentual_di_lcx / 100, dias) - valor_investido
            rendimento_liquido_lcx = valor_investido + rendimento_bruto_lcx
            print("\n** LCI / LCA **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto_lcx:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido_lcx:.2f}")
        else:
            print("Não foi possível obter a taxa da LCI/LCA.")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    interacao_usuario()
