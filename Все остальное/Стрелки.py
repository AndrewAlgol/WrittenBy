"https://acmp.ru/index.asp?main=task&id_task=44"
s = str(input())
j = 0
while True:
    if s.find('>>-->') == -1 and s.find('<--<<') != -1:
        s = s[s.find('<--<<') + 4:]
        j += 1
    elif s.find('>>-->') != -1 and s.find('<--<<') == -1:
        s = s[s.find('>>-->') + 4:]
        j += 1
    elif s.find('>>-->') < s.find('<--<<'):
        s = s[s.find('>>-->') + 4:]
        j += 1
    elif s.find('>>-->') > s.find('<--<<'):
        s = s[s.find('<--<<') + 4:]
        j += 1
    else:
        break
print(j)
