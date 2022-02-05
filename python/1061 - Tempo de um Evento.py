di = int(input().strip('Dia '))
hi, mi, si = map(int, input().split(' : '))
df = int(input().strip('Dia '))
hf, mf, sf = map(int, input().split(' : '))

d = df - di
h = 0 
m = 0
s = 0

# Horas
if hi < hf: 
    h += hf - hi
elif hi > hf: 
    d -= 1
    h += (24 - hi + hf)

# Minutos
if mi < mf:
    m += mf - mi
    if hi == hf:
        h = 0
elif mi > mf:
    h -= 1
    m += (60 - mi + mf)
    if  hi == hf:
        h = 23
        d -= 1

#Segundos
if si < sf:
    s += sf - si
    if mi == mf:
        m = 0
        if hi == hf:
            h = 0
elif si > sf:
    m -= 1
    s += (60 - si + sf)
    if mi == mf:
        m = 59
        h -= 1
        if hi == hf:
            h = 23
            d -= 1
elif si == sf:
    s = 0
    if mi == mf:
        m = 0
        if hi == hf:
            h = 0

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')