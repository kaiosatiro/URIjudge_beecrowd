while True:
    n = int(input())
    if n == 0: break
    matriz = []
    for _ in range(n):
        _ = [1 for _ in range(n)]
        matriz.append(_)
        
    for linha in range(n // 2 + 1):
        for coluna in range(n // 2 + 1):
            matriz[linha][coluna] = 1 + min(linha, coluna)
        i = 0
        for coluna in range(n - 1, n // 2 , -1):
            matriz[linha][coluna] = matriz[linha][i]
            i += 1

    i = 0
    for linha in range(n - 1, (n // 2)-1, -1):
        matriz[linha] = matriz[i]
        i += 1

    for linha in matriz:
        for a, i in enumerate(linha):
            if a == 0:
                print(' ', i, end='')
            else:
                print(f'{i:>4}', end='')
        print()
    print()
