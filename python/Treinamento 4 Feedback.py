def coleta(l):
    N= int(input())
    for _ in range(N):
        K= int(input())
        for _ in range(K):
            l.append(int(input()))

def exibe(lista1, lista2):
    for i in lista2:
        print(lista1[i-1])
        
lista= ['Rolien', 'Naej', 'Elehcim', 'Odranoel']
lista_casos= []
coleta(lista_casos)
exibe(lista, lista_casos)