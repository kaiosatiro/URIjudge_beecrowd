def perfeito(n):
    acum= 0
    for i in range(1, n):
        if n % i == 0:
            acum+= i
    return acum == n

N= int(input())
for _ in range(N):
    X= int(input())
    if perfeito(X):
        print(f'{X} eh perfeito')
    else:
       print(f'{X} nao eh perfeito')
       
# Numeros perfeitos:
# 5
# 6
# 28
# 496
# 8128
# 33550336
# 8589869056
