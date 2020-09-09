n = int(input())
my_dict = dict()
с_my_dict = dict()
for i in range(n):
    s = input().split()
    my_dict[s[0]] = s[1]
    с_my_dict[s[1]] = s[0]
syn = input()
if syn in my_dict:
    print(my_dict.get(syn))
else:
    print(с_my_dict.get(syn))
