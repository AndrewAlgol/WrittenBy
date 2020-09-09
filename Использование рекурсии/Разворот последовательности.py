"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/mfqaz/razvorot-posliedovatiel-nosti"
def turn():
    n = int(input())
    if n != 0:
        turn()
    print(n)
turn()
