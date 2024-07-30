# Simulador de Renda Fixa

## Investimentos Financeiros - Simulador de Rendimentos

Este conjunto de scripts Python calcula o rendimento de diferentes tipos de investimentos com base nas informações fornecidas pelo usuário. Cada script é projetado para calcular o rendimento de um tipo específico de investimento, utilizando taxas fornecidas pelo Banco Central do Brasil.

### Funcionalidades:

#### Poupança:

Obtém a taxa de poupança mais recente.
Calcula o rendimento bruto e líquido de um investimento em poupança.

#### CDB:

Obtém a taxa DI mais recente.
Calcula o rendimento bruto e líquido de um investimento em CDB, incluindo o cálculo do Imposto de Renda (IR) com base na alíquota aplicável.

#### LCI/LCA:

Obtém a taxa DI mais recente.
Calcula o rendimento bruto e líquido de um investimento em LCI/LCA.


#### Bibliotecas: 

* **requests** para requisições HTTP.

#### Versão do Python:

* Python 3.12.

#### Como Usar:

Forneça o valor inicial do investimento e o prazo em meses quando solicitado.
O script exibirá o rendimento bruto, o imposto de renda (para CDB) e o valor líquido final.

#### Metodologia de Cálculo:

* **Taxas:** As taxas são obtidas via API do Banco Central do Brasil.
* **Rendimento:** Calculado utilizando a fórmula de capitalização composta.
* **Imposto de Renda (para CDB):** Calculado com base na alíquota progressiva de IR, dependendo do prazo do investimento.
