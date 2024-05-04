class Solution(object):
    def countGoodNumbers(self, n):
        mod=n%2
        res=1
        n-=mod
        res=pow(20,n//2,10**9+7)
            
        if mod==1:
            res*=5
        return res%(10**9 +7)
            


        

      