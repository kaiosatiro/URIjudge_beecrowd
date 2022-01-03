def resultado(lista, salto, quant):
    for i in range(quant-1):
        if lista[i]+salto < lista[i+1] or lista[i]-salto > lista[i+1]:
            return print('GAME OVER')
    return print('YOU WIN')

X= input().split()
P,N = int(X[0]), int(X[1])
X= input().split()
for i in range(N):
    X[i] = int(X[i])
resultado(X, P, N)