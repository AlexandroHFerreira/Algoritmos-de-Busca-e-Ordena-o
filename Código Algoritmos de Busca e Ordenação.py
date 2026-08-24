def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


while True:
    print("\n===== ALGORITMOS =====")
    print("1 - Busca Linear")
    print("2 - Busca Binária")
    print("3 - Bubble Sort")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        lista = [5, 3, 8, 1, 9, 11, 7]
        alvo = 9

        resultado = busca_linear(lista, alvo)

        print("\nLista:", lista)
        print("Procurando:", alvo)
        print("Resultado:", resultado)

    elif opcao == "2":
        lista = [1, 3, 5, 7, 9, 11, 13, 15]
        alvo = 11

        resultado = busca_binaria(lista, alvo)

        print("\nLista:", lista)
        print("Procurando:", alvo)
        print("Resultado:", resultado)

    elif opcao == "3":
        lista = [5, 3, 8, 1]

        print("\nLista original:", lista)

        bubble_sort(lista)

        print("Lista ordenada:", lista)

    elif opcao == "4":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida. Escolha 1, 2, 3 ou 4.")