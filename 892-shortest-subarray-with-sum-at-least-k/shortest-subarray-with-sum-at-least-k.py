from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        queue = deque()
        prefix_sum = [0] * (len(nums) + 1)
        min_len = float('inf')
        
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        for i in range(len(prefix_sum)):
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()
            
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_len = min(min_len, i - queue.popleft())
            
            queue.append(i)
        
        return -1 if min_len == float('inf') else min_len


        
        