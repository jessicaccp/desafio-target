""" Questão 3 """

# Bibliotecas
import json
import sys

# Calcula os valores de maior e menor faturamento no mês,
# ignorando dias sem faturamento
def maior_menor(dados):
    maior, menor = 0.0, 0.0

    for entrada in dados:
        if maior == 0.0 and menor == 0.0 and entrada['valor'] != 0.0:
            maior = entrada['valor']
            menor = entrada['valor']
        elif entrada['valor'] > maior:
            maior = entrada['valor']
        elif entrada['valor'] < menor and entrada['valor'] != 0.0:
            menor = entrada['valor']

    return maior, menor

# Calcula a média mensal de faturamento, ignorando dias sem faturamento
def media_mensal(dados):
    soma = 0.0
    dias = 0

    for entrada in dados:
        if entrada['valor'] != 0.0:
            soma += entrada['valor']
            dias += 1

    return soma/dias

# Calcula o número de dias cujo faturamento diário foi maior que a média mensal
def dias_faturamento_superior(media, dados):
    dias = 0

    for entrada in dados:
        if entrada['valor'] > media:
            dias += 1

    return dias

# Função principal
def main():

    # Abre e lê o arquivo .json
    try:
        arquivo = open('dados.json')
        dados = json.load(arquivo)
    except:
        print('Erro ao abrir o arquivo "dados.json". Tente novamente.')
        sys.exit(1)

    # Executa funções
    maior, menor = maior_menor(dados)
    media = media_mensal(dados)
    dias = dias_faturamento_superior(media, dados)

    # Resultado
    print("Menor valor de faturamento: ", menor)
    print("Maior valor de faturamento: ", maior)
    print("Dias com faturamento diário superior à média mensal: ", dias)

main()