def insertionSort1(n, arr):
    last=arr[n-1]
    while n > 1 and arr[n-2] > last:
        arr[n-1] = arr[n-2]
        n -= 1
        print(*arr)
    arr[n-1] = last 
    print(*arr)  
