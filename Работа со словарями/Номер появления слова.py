"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/COVcr/nomier-poiavlieniia-slova"
fin = open("input.txt", "r", encoding="utf-8")
my_dict = dict()
n = []
l = fin.read().split('\n')
for i in l:
    s = str(i)
    n += s.split()
for i in n:
    if i in my_dict:
        num = my_dict.get(i)
        my_dict[i] = num + 1
        print(my_dict.get(i), end=' ')
    else:
        my_dict[i] = 0
        print(0, end=' ')
