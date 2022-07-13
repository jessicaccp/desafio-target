""" Questão 5 """

# Recebe uma string e a inverte
def main():

    # Lê o input como uma lista
    string_list = list(input("Digite a string a ser invertida: "))

    tamanho = len(string_list)

    # Realiza as operações baseado no índice
    for i in range(tamanho//2):
        aux = string_list[i]
        string_list[i] = string_list[tamanho-i-1]
        string_list[tamanho-i-1] = aux

    # Transforma a lista em string
    string = "".join(string_list)
    
    print(string)

main()