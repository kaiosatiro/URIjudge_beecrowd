while True:
    try:
        n = int(input())
        m,l = map(int, input().split(' '))

        m_dic = {}
        l_dic = {}

        for i in range(1, m+1):
            m_dic[i] = list(map(int, input().split(' ')))
        for i in range(1, l+1):
            l_dic[i] = list(map(int, input().split(' ')))

        cm, cl = map(int, input().split(' '))
        a = int(input())
        m = m_dic[cm][a-1]
        l = l_dic[cl][a-1]

        if m > l:
            print('Marcos')
        elif l > m:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break