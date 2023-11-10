class Solution(object):
    def isPalindrome(self, x):
        stringX =  str(x)
        return stringX ==stringX[::-1]
        