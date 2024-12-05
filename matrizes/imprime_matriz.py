def imprime_matriz(matriz):
    for linha in matriz:
        for i, elemento in enumerate(linha):
            if i < len(linha) - 1:
                print(elemento, end=" ")
            else:
                print(elemento)
