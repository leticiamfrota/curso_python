#criando uma matriz
def criar_matriz(num_linhas,num_colunas):
    matriz = []
    for i in range(num_linhas):
        lista = []
        for j in range(num_colunas):
            valor = int(input(f"Digite o elemento [{i}][{j}]:"))
            lista.append(valor)
        matriz.append(lista)
    for i in matriz:
        print(i)

def ler_matriz():
    num_linhas = int(input("Digite o num de linhas: "))
    num_colunas = int(input("Digite o num de colunas: "))
    return criar_matriz(num_linhas, num_colunas) 

ler_matriz()