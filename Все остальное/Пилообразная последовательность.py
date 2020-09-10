""
n = int(input())
'https://acmp.ru/index.asp?main=task&id_task=20'
l = list(map(int, input().split()))
rez = []

if n == 1:
    print(1)
elif n == 2:
    if l[0] == l[1]:
        print(1)
    else:
        print(2)
else:
    if l[0] > l[1]:
        k = 0
        j = 2
    elif l[0] < l[1]:
        k = 1
        j = 2
    elif l[0] == l[1]:
        j = 1
    
    for i in range(1, n - 1):
        if l[i] < l[i + 1] and k == 0:
            j += 1
            k = 1
            if i + 1 == n - 1:
                rez.append(j)
        elif l[i] > l[i + 1] and k == 1:
            j += 1
            k = 0
            if i + 1 == n - 1:
                rez.append(j)
        elif l[i] > l[i + 1] and k == 0:
            rez.append(j)
            j = 2
            k = 0
        elif l[i] < l[i + 1] and k == 1:
            rez.append(j)
            j = 2
            k = 1
        elif l[i] == l[i + 1]:
            rez.append(j)
            j = 1
            if i + 1 != n - 1:
                if l[i + 1] > l[i + 2]:
                    k = 1
                elif l[i + 1] < l[i + 2]:
                    k = 0
        
    print(max(rez))
