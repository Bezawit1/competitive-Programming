class Solution(object):
    def sumOfThree(self, num):
        if num%3==0:
            val=num//3
            return [val-1,val,val+1]
        return []
