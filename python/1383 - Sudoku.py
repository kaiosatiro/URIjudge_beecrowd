def mini_matriz(matriz, m):
    lista = []
    if m == 1:
        for l in range(3):
            for c in range(3):
                lista.append(matriz[l][c])
        return lista
    elif m == 2:
        for l in range(3):
            for c in range(3,6):
                lista.append(matriz[l][c])
        return lista
    elif m == 3:
        for l in range(3):
            for c in range(6,9):
                lista.append(matriz[l][c])
        return lista
    elif m == 4:
        for l in range(3,6):
            for c in range(3):
                lista.append(matriz[l][c])
        return lista
    elif m == 5:
        for l in range(3,6):
            for c in range(3,6):
                lista.append(matriz[l][c])
        return lista
    elif m == 6:
        for l in range(3,6):
            for c in range(6,9):
                lista.append(matriz[l][c])
        return lista
    elif m == 7:
        for l in range(6,9):
            for c in range(3):
                lista.append(matriz[l][c])
        return lista
    elif m == 8:
        for l in range(6,9):
            for c in range(3,6):
                lista.append(matriz[l][c])
        return lista
    elif m == 9:
        for l in range(6,9):
            for c in range(6,9):
                lista.append(matriz[l][c])
        return lista
    pass


def testa_matriz(matriz):
    #Exame de linhas
    for linha in matriz:
        if len(set(linha)) != 9:
            return False
    #Exame de colunas
    for coluna in range(9):
        lista = []
        for linha in matriz:
            lista.append(linha[coluna])
        if len(set(lista)) != 9:
            return False
    #Exame de mini_matrizes 3x3
    for m in range(1, 10):
        lista = mini_matriz(matriz, m)
        if len(set(lista)) != 9:
            return False
    # for coluna in range(0, 7, 3):  
    #     lista = []
    #     for linha in matriz:
    #         lista.append(linha[0 + coluna])
    #         lista.append(linha[1 + coluna])
    #         lista.append(linha[2 + coluna])
    #         if linha == 2:
    #             if len(set(lista)) != 9:
    #                 return False
    #             lista = []
    #         elif linha == 5:
    #             if len(set(lista)) != 9:
    #                 return False
    #             lista = []
    #         elif linha == 8:
    #             if len(set(lista)) != 9:
    #                 return False                                            
    return True


n = int(input())
lista = {}
for i in range(1, n+1):
    matriz = []
    for _ in range(9):
        k = input().split(' ')
        matriz.append(k)
    lista[i] = matriz

for i in range(1, n+1):
    teste = testa_matriz(lista[i])
    print(f'''Instancia {i}
{'SIM' if teste else 'NAO' }
''')

# 2
# 1 3 2 5 7 9 4 6 8
# 4 9 8 2 6 1 3 7 5
# 7 5 6 3 8 4 2 1 9
# 6 4 3 1 5 8 7 9 2
# 5 2 1 7 9 3 8 4 6
# 9 8 7 4 2 6 5 3 1
# 2 1 4 9 3 5 6 8 7
# 3 6 5 8 1 7 9 2 4
# 8 7 9 6 4 2 1 5 3
# 1 3 2 5 7 9 4 6 8
# 4 9 8 2 6 1 3 7 5
# 7 5 6 3 8 4 2 1 9
# 6 4 3 1 5 8 7 9 2
# 5 2 1 7 9 3 8 4 6
# 9 8 7 4 2 6 5 3 1
# 2 1 4 9 3 5 6 8 7
# 3 6 5 8 1 7 9 2 4
# 8 7 9 6 4 2 1 3 5