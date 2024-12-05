def dimensoes(matriz):
    return(f'{len(matriz)}X{len(matriz[0])}')

def soma_matrizes(m1,m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz = []
        for i in range(len(m1)):
            lista = []
            for j in range(len(m1[0])):
                lista.append(0)
            matriz.append(lista)

        for i in range(len(m1)):
            for j in range(len(m1[0])):
                matriz[i][j] = m1[i][j] + m2[i][j]
        
        return matriz

    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1,m2))