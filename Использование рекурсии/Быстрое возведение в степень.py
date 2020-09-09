"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/lf4m0/bystroie-vozviedieniie-v-stiepien"
def FastPow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return FastPow(a ** 2, n // 2)
    elif n % 2 != 0:
        return a * FastPow(a, n - 1)
a = float(input())
n = int(input())
print(FastPow(a, n))
