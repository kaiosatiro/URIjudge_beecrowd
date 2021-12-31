# while True:
#     try:
#         n, m = input().split()
#         qt = 0
#         for x in range(int(n), int(m)+1):
#             if len(set(list(str(x)))) == len(str(x)):
#                 qt += 1
#         print(qt)  
#     except EOFError:
#         break

while True:
    try:
        def comparador(numero):
            numero  = str(numero)
            lista = list(numero)
            if len(set(lista)) == len(numero):
                return True
            else:
                return False
            # lista = list(str(numero))
            # for i in lista:
            #     v = lista.count(i)
            #     if v > 1:
            #         return False
            # return True
        n,m = input().split(' ')
        lista= []
        for i in range(int(n), int(m)+1):
            valido = comparador(i)
            if valido:
                lista.append(i)
        print(len(lista))
    except EOFError:
        break

