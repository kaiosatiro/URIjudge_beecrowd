x, y = map(int, input().split(' '))
for i in range(1, y+1, x):
    for a in range(i, i+x):
        if a == i+x-1:
            print(a)
        else:
            print(a, end=' ')