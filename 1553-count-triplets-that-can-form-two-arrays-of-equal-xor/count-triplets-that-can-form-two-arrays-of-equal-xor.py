class Solution(object):
    def countTriplets(self, arr):
      
        n = len(arr)
        
       
        prefixXOR = [0] * (n + 1)
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]
        
        count = 0
        for i in range(n):
           
            for j in range(i + 1, n):
                for k in range(j,n):
                    if prefixXOR [j] ^ prefixXOR [i] == prefixXOR[k+1]^ prefixXOR[j]:
                        count+=1
        return count
                  
        