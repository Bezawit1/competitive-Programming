class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        num = 10**9 + 7
        n = len(nums)
        
    
        counts = [0] * n
        
        for start, end in requests:
            counts[start] += 1
            if end + 1 < n:
                counts[end + 1] -= 1
        
    
        for i in range(1, n):
            counts[i] += counts[i - 1]
        
    
        nums.sort()
        counts.sort()
        
    
        total_sum = 0
        for i in range(n):
            total_sum += nums[i] * counts[i]
        
        return total_sum % num

       
        