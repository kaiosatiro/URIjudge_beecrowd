def recebe():
    matriz= []
    linha= []
    for _ in range(12):
        linha= []
        for _ in range(12):
            linha.append(float(input()))
        matriz.append(linha)
    return matriz

def operacao(operador, matriz):
    soma= 0
    cont= 0
    C=1
    for l in range(11):
        for c in range(C, 12):
            soma+= matriz[l][c]
            cont+= 1
        C+= 1
    media= soma/cont    
    if operador == 'S':
        return soma
    elif operador == 'M':
        return media
        
T= input()
M= recebe()
resultado= operacao(T, M)
print(f'{resultado:.1f}')