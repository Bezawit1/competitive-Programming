def countingSort(arr):
    # Write your code here
    counter=[]
    for i in range(100):
        count=0
        for k in range(len(arr)):
            if arr[k]==i:
                count+=1
        counter.append(count)
    return counter
