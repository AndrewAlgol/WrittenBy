'https://acmp.ru/index.asp?main=task&id_task=41'
def countSort(l):
    rez = [0] * 201
    for i in l:
        rez[i + 100] = rez[i + 100] + 1
    for i in range(201):
        print((str(i - 100) + ' ') * rez[i], end='')

n = int(input())
countSort(list(map(int, input().split())))
