num, k = map(int, input().split())
def wrong_subtraction(num , k):
    
    while k > 0:
        digit = num%10
        if digit != 0:
            num-=1
        else:
            num=num//10
        k-=1
    print(num)
wrong_subtraction(num , k)
