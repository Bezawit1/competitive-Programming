

for _ in range(int(input())):
    input()
    a = list(set([int(i) for i in input().split()]))
    if len(a) == 1:
        print("YES")
        continue
    a.sort()
    c = 0
    is_sequence = True  
    for i in range(len(a) - 1):
        if a[i] + 1 != a[i + 1]:
            is_sequence = False
            break
    if is_sequence:  
        print("YES")
    else:
        print("NO")
