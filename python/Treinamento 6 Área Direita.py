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
    c= 7
    for linha in range(5, 0, -1):
        for colun in range(c, 12):
            soma+= matriz[linha][colun]
            cont+= 1
        c+= 1
    c= 7
    for linha in range(6, 11):
        for colun in range(c, 12):
            soma+= matriz[linha][colun]
            cont+= 1
        c+=1
        media= soma/cont
    if operador == 'S':
        return soma
    elif operador == 'M':
        return media
          
O= input()
M= recebe()
resultado= operacao(O, M)
print(f'{resultado:.1f}')