"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9KkLv/sriednii-ball-po-klassam"
fin = open("input.txt", "r", encoding="utf-8")
s9 = []
s10 = []
s11 = []
for line in fin:
    for i in range(len(line)):
        if line[i] == '9':
            s9.append(int(line[i + 1:]))
            break
        elif line[i] == '1' and line[i + 1] == '0':
            s10.append(int(line[i + 2:]))
            break
        elif line[i] == '1' and line[i + 1] == '1':
            s11.append(int(line[i + 2:]))
            break
print(sum(s9)/len(s9), sum(s10)/len(s10), sum(s11)/len(s11), sep=' ')
