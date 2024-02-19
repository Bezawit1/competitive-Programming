class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        num = 2
        while num <=n:
            if num == n:
                 return True
            num*=2
        return False
       
        