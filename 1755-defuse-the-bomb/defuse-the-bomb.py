class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        res = [0]*n
        org =k
        if k < 0:
            code = code[::-1]
            k *=-1
        
        initial_sum = sum(code[:k])
       
        for i in range(n):
            
            initial_sum+=code[(i+k)%n] - code[i]
            res[i]=(initial_sum)
            
           
        if org < 0:
            res = res[::-1]
        return res

            
    
        
        