while True:
    try:
        EPR= 0
        EHD= 0
        intrusos= 0
        n= int(input())
        for i in range(n):
            X= input().split()
            if X[1] == 'EPR':
                EPR+= 1
            elif X[1] == 'EHD':
                EHD+= 1
            else:
                intrusos+= 1
        print(f'EPR: {EPR}')
        print(f'EHD: {EHD}')
        print(f'INTRUSOS: {intrusos}')
    except:
        break

# def coleta(lista):
#     n= int(input())
#     for _ in range(n):
#         lista.append(input().split())

# def contagem(lista):
#     EPR= 0
#     EHD= 0
#     intrusos= 0
#     for i in range(len(lista)):
#         if lista[i][1] == 'EPR':
#             EPR+= 1
#         elif lista[i][1] == 'EHD':
#             EHD+= 1
#         else:
#             intrusos+= 1
#     return EPR, EHD, intrusos

# lista_alunos= [] 
# coleta(lista_alunos)
# EPR, EHD, intrusos= contagem(lista_alunos)
# print(f'EPR: {EPR}')
# print(f'EHD: {EHD}')
# print(f'INTRUSOS: {intrusos}')