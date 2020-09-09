"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4JHKe/chastotnyi-analiz"
fin = open('input.txt', encoding='utf8')
d = {}
l = []
for line in fin:
    words = line.strip().split()
    for word in words:
        d[word] = d.get(word, 0) + 1
for key in d:
    b = (-d.get(key), key)
    l.append(b)
l.sort()
for i in l:
    print(i[1])
