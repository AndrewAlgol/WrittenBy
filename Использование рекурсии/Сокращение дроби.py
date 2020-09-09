"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/q1gm9/sokratitie-drob"
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    a = gcd(n, m)
    return n // a, m // a
n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
