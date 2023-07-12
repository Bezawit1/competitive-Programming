class Solution(object):
    def isPowerOfThree(self, n):
        while(n%3==0 and n>0):
            return self.isPowerOfThree(n/3)
        return n==1

       