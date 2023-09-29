class Solution(object):
    def isPerfectSquare(self, num):
        left , right = 0 , num
        while left <= right:
            mid = left + (right - left)//2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid -1
            else:
                left = mid +1
        return False
    
        
        