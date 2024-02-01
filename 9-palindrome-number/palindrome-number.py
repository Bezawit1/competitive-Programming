class Solution(object):
    def isPalindrome(self, x):
        reversed=0
        num=x
        while x>0:
            digits=x%10
            reversed=digits+reversed*10
            x//=10
          
        return reversed==num
        