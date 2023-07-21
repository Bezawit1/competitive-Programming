class Solution(object):
    def arrangeCoins(self, n):
        left,right = 1 , n
        counter=0
        while left <= right:
            mid = left + (right - left) //2 
            sum = mid*(mid + 1) //2 
            if sum <= n:
                left = mid+1
                counter = mid
            else:
                right = mid -1
        return counter
