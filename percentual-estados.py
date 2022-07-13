""" Questão 4

Dados para a questão:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53 """

# Calcula o faturamento total da distribuidora
def faturamento_total(faturamento):
    total = 0.0

    for estado in faturamento:
        total += faturamento[estado]

    return total

# Dado o faturamento total, calcula e exibe o percentual de cada estado
def percentual_de_representacao(faturamento, total):
    print("Percentual de representação por estado:")

    for estado in faturamento:
        percentual = faturamento[estado] * 100.00 / total
        print(estado, "-", round(percentual, 2), "%")

# Função principal
def main():

    # Valores de faturamento por estado
    dados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    # Executa as funções
    total = faturamento_total(dados)
    percentual_de_representacao(dados, total)

main()