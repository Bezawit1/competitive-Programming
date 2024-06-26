# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left =1 
        right = n
        while left <= right:
            mid_element = left + (right - left)//2
            if guess(mid_element) == -1:
                right = mid_element - 1
            elif guess(mid_element) == 1:
                left = mid_element + 1
            else:
                return mid_element
        return left
        

        