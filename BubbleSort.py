def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp=a[j]
                a[j]= a[j + 1] 
                a[j + 1]= temp
                swaps += 1
    
    
   
    print("Array is sorted in " +str(swaps)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[len(a)-1]))
