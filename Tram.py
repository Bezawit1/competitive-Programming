def tram ():
    num = int(input())
    max_num = 0
    max_sum = 0
    for i in range(num):
        a , b =  map(int , input().split())
        max_sum +=(b - a)
        max_num = max(max_num , max_sum)
    print(max_num)
tram()
        
