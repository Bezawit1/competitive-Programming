class Solution(object):
    def pivotIndex(self, nums):
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(i+ prefix_sum[-1])
    
        right = prefix_sum[-1]
        left = 0
        while left < len(prefix_sum)-1:
            if right - prefix_sum[left] == prefix_sum[left+1]:
                return left
            left+=1
        return -1
        