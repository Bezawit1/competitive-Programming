def ehab():
    n = int(input())
    a = list(map(int, input().split()))

    has_odd = False
    has_even = False

    for num in a:
        if num % 2 == 1:
            has_odd = True
        else:
            has_even = True

    if has_odd and has_even:
        a.sort()

    for num in a:
        print(num, end=" ")





ehab()




