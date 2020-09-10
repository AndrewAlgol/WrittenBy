"https://acmp.ru/index.asp?main=task&id_task=34"
num = list(map(int, input().split()))
mes = str(input())
j = 0
s = mes[:num[1]]
i = mes.find(s)
if i == -1:
    i = 0
for i in range(num[0]):
    s = mes[i:i + num[1]]
    if mes.find(s) != -1:
        mes0 = mes[i + 1:]
        if mes0.find(s) != -1:
            j += 1
            print('YES')
            break
if j == 0:
    print('NO')
