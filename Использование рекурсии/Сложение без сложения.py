def Sum(a, b):
    if b != 0:
        return Sum(a + 1, b - 1)
    else:
        return a

a = int(input())
b = int(input())
if b > a:
    c = a
    a = b
    b = c
print(Sum(a, b))
