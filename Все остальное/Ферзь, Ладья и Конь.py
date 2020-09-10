'https://acmp.ru/index.asp?main=task&id_task=19'
l = list(map(str, input().split(' ')))
alp = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
desk = []
o_desk = []
s = 0
x_q, y_q = alp.get(l[0][0]), int(l[0][1])
x_r, y_r = alp.get(l[1][0]), int(l[1][1])
x_h, y_h = alp.get(l[2][0]), int(l[2][1])
for i in range(1, 9):
    for j in range(1, 9):
        if i == x_q and j == y_q or i == x_h and j == y_h or i == x_r and j == y_r:
            o_desk.append('#')
        else:
            if x_h + 2 == i and (y_h + 1 == j or y_h - 1 == j):
                o_desk.append('+')
            elif x_h + 1 == i and (y_h + 2 == j or y_h - 2 == j):
                o_desk.append('+')
            elif x_h - 1 == i and (y_h + 2 == j or y_h - 2 == j):
                o_desk.append('+')
            elif x_h - 2 == i and (y_h + 1 == j or y_h - 1 == j):
                o_desk.append('+')
            elif y_r == j and x_r != i or y_q == j and x_q != i:
                o_desk.append('+')
            elif x_r == i and y_r != j or x_q == i and y_q != j:
                o_desk.append('+')
            elif abs(x_q - i) == abs(y_q - j):
                o_desk.append('+')
            else:
                o_desk.append('-')
    desk.append(o_desk)
    s += o_desk.count('+')
    o_desk = []
print(s)
