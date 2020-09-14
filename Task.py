def CreateLine(s):
    Line = list()
    numLine = str()
    for i in range(len(s)):
        if s[i] != ' ':
            numLine += s[i]
            if i == len(s) - 1:
                Line.append(int(numLine))
                numLine = str()
        elif s[i] == ' ':
            Line.append(int(numLine))
            numLine = str()
    return Line

def Create():
    Matrix = list()
    Matrix.append(CreateLine(str(input())))
    for i in range(1, len(Matrix[0])):
        Matrix.append(CreateLine(str(input())))
    return Matrix

def FindAndChange(Matrix):
    Min = Matrix[0][0]
    l = 0
    m = 0
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Min > Matrix[i][j]:
                Min = Matrix[i][j]
                l, m = i, j
    Matrix[l][m] *= 10
    return Matrix

def Output(Matrix):
    for i in range(len(Matrix)):
        print(*Matrix[i])
            
def MaxNumDiagonal(Matrix):
    Max = Matrix[0][0]
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if i == j:
                if Max < Matrix[i][j]:
                    Max = Matrix[i][j]
    return Max

def SumDigit(num):
    s = 0
    Len = len(str(num))
    for i in range(Len):
        if i == Len - 1:
            s += (num % 10)
        else:
            s += (num % 10)
            num //= 10
    return s

matrix = Create()                    #создание матрицы
matrixChange = FindAndChange(matrix) #изменение матрицы
Output(matrixChange)                 #вывод матрицы
Max = MaxNumDiagonal(matrixChange)   #максимальное число на гл. диагонали
print('Сумма цифр самого большого числа на главной диагонали ', SumDigit(Max))


s = str(input())
List = list()
word = str()
char = set()

for i in range(len(s)):
    if s[i] != ' ' and s[i] != '':
        word += s[i]
        if i == len(s) - 1 and s[i] != ' ':
            List.append(word)
            word = str()
    elif s[i] != '':
        List.append(word)
        word = str()

maxLen = List[0]

for i in List:
    if i == '':
        continue
    else:
        char.add(i[0])
    if len(maxLen) <= len(i):
        maxLen = i
print('Самое длинное слово - ', maxLen)

char = list(char)
qt = 0
maxQt = 0
maxChar = str()
for i in char:
    for j in List:
        if j != '':
            if i == j[0]:
                qt += 1
    if qt > maxQt:
        maxQt = qt
        maxChar = i
    else:
        qt = 0
print('Буква с которой начинается самое большое количество слов -', maxChar)
        

