def number_of_pairs ():
    t = int(input())
    for i in range(t):
        n ,l , r= map(int , input().split())
        a = list(map(int , input().split()))
        a.sort()
        i = 0
        j = n-1
        res = 0
        while (i < j):
            if a[j]+a[i] < r+1:
                res+=(j - i)
                i+=1
            else:
                j-=1
        left = 0
        right = n-1
        res1 = 0
        while (left < right):
            if a[left]+a[right] < l:
                res1+=(right - left)
                left+= 1
            else:
                right-=1
        print(res - res1)
number_of_pairs()
