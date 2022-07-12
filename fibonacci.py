""" Questão 2 """

# Calcula se o valor da entrada pertence ou não à sequência de Fibonacci
def fib(x, y, number):

    # Se for um valor da sequência, exibe mensagem positiva
    if number == x or number == y:
        print("Pertence à sequência.")

    # Se for maior do que o maior número, continua procurando
    elif number > y:
        fib(y, x+y, number)

    # Se for maior do que o menor número e não tiver entrado no elif acima, exibe mensagem negativa
    elif number > x:
        print("Não pertence à sequência.")


# Função principal
def main():

    # Recebe apenas valor inteiro
    while True:
        try:
            number = int(input("Digite um número:"))
            break
        except ValueError:
            print("Digite apenas números inteiros.")
            continue

    # Chama função fib, informando os primeiros números da sequência
    fib(0, 1, number)

main()