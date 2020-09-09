"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/OE01R/otsortirovat-spisok-uchastnikov-po-alfavitu"
fin = open("input.txt", "r", encoding="utf-8")
all_line = []
for line in fin:
    q_b = line[line.rfind(' '):]
    b = line[:line.rfind(' ')]
    c = b[:b.rfind(' ')]
    line = c + q_b
    all_line.append(line[:-1])
all_line.sort()
for i in all_line:
    print(i)
