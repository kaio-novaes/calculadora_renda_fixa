from api import obter_taxa_poupanca, obter_taxa_di
from calculo_poupanca import calcular_rendimento_poupanca
from calculo_cdb_rdb import calcular_rendimento_cdb, calcular_aliquota_ir, calcular_iof
from calculo_lcx import calcular_rendimento_lcx
import logging

logging.basicConfig(level=logging.INFO)

def converter_para_dias(periodo, unidade):
    """
    Converte o período para dias com base na unidade fornecida.
    """
    if unidade == 'dias':
        return periodo
    elif unidade == 'meses':
        return periodo * 30.41  # Média de dias por mês
    elif unidade == 'anos':
        return periodo * 365  # Média de dias por ano (incluindo anos bissextos)
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

        meses = dias / 30.41  # Para cálculo da Poupança e LCI/LCA em meses

        # Poupança
        taxa_poupanca = obter_taxa_poupanca()
        if taxa_poupanca is not None:
            rendimento_liquido = calcular_rendimento_poupanca(valor_investido, taxa_poupanca, meses)
            rendimento_bruto = rendimento_liquido - valor_investido
            print("\n** Poupança **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido:.2f}")
        else:
            print("Não foi possível obter a taxa da Poupança.")

        # CDB / RDB
        taxa_di = obter_taxa_di()
        if taxa_di is not None:
            rendimento_total = calcular_rendimento_cdb(valor_investido, taxa_di, meses)
            rendimento_bruto = rendimento_total - valor_investido
            aliquota_ir = calcular_aliquota_ir(dias)
            ir = rendimento_bruto * (aliquota_ir / 100)
            iof = calcular_iof(valor_investido, rendimento_bruto, dias)
            rendimento_liquido = valor_investido + rendimento_bruto - ir - iof
            print("\n** CDB **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto:.2f}")
            print(f"Imposto de Renda (IR) ({aliquota_ir}%): R$ {ir:.2f}")
            print(f"IOF: R$ {iof:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido:.2f}")
        else:
            print("Não foi possível obter a taxa DI.")

        # LCI / LCA
        taxa_lcx = obter_taxa_di()
        if taxa_lcx is not None:
            rendimento_liquido = calcular_rendimento_lcx(valor_investido, taxa_lcx, meses)
            rendimento_bruto = rendimento_liquido - valor_investido
            print("\n** LCI / LCA **")
            print(f"Valor da Aplicação: R$ {valor_investido:.2f}")
            print(f"Rendimento Bruto: R$ {rendimento_bruto:.2f}")
            print(f"Valor Líquido: R$ {rendimento_liquido:.2f}")
        else:
            print("Não foi possível obter a taxa da LCI/LCA.")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    interacao_usuario()
