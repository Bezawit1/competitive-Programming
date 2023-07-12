class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        if n<1:
            return False
        while(n%4==0):
            return self.isPowerOfFour(n/4)

        

        