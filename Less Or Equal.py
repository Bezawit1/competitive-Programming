n, k = map(int, input().split())
sequence = list(map(int, input().split()))

def find_x(n, k, sequence):
    sequence.sort()

    if k == 0:
        return -1 if sequence[0] == 1 else 1
    elif k == n:
        return sequence[-1]
    elif sequence[k - 1] == sequence[k]:
        return -1
    else:
        return sequence[k - 1]





result = find_x(n, k, sequence)
print(result)
