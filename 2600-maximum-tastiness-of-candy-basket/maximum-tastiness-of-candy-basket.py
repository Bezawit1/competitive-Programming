class Solution(object):
    def maximumTastiness(self, price, k):
        
        price.sort()
        left, right = 0, price[-1] - price[0]
        
        while left < right:
            mid = (left + right + 1) // 2
            if self.valid(price, k, mid):
                left = mid
            else:
                right = mid - 1
                
        return left

    def valid(self, price, k, min_val):
        size = 1
        candy = price[0]
        
        for i in range(1, len(price)):
            if price[i] - candy >= min_val:
                size += 1
                candy = price[i]
                
        return size >= k

       

        