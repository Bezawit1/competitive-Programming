import sys
n = int(input())
phoneBook = {}
for i in range(n):
    name = input().split(' ')
    phoneBook[name[0]] = name[1]


lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str(phoneBook[name]))
    else:
        print('Not found')
