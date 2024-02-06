if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    scores.sort()
    unique = set(scores)
    print(list(unique)[-2])
