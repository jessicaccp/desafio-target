""" Questão 2 """

# Calcula se o valor da entrada pertence ou não à sequência de Fibonacci
def fib(x, y, numero):

    # Se for um valor da sequência, exibe mensagem positiva
    if numero == x or numero == y:
        print("Pertence à sequência.")

    # Se for maior do que o maior número, continua procurando
    elif numero > y:
        fib(y, x+y, numero)

    # Se for maior do que o menor número e não tiver entrado no elif acima, exibe mensagem negativa
    elif numero > x:
        print("Não pertence à sequência.")

# Chama função fib, informando os primeiros números da sequência
def checa_se_numero_esta_em_fib(numero):
    fib(0, 1, numero)

# Função principal
def main():

    # Recebe apenas valor inteiro
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero < 0:
                raise ValueError
            break
        except ValueError:
            print("Digite apenas números inteiros não-negativos.")
            continue

    # Faz a verificação
    checa_se_numero_esta_em_fib(numero)

main()