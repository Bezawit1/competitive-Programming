class Solution(object):
    def mySqrt(self, x):
        if x == 1:
            return 1
        if x == 0 :
            return 0
        left,right= 1 , x
        while left <= right:
            mid = left+(right-left)//2
            square = mid*mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
