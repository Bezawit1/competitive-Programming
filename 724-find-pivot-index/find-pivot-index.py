class Solution(object):
    def pivotIndex(self, nums):
        prefix_sum=[0]
        left=1
     
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        right = prefix_sum[-1]
        for i in range(1,len(prefix_sum)):
            left_sum=prefix_sum[i-1]
            right_sum=right - prefix_sum[i]
            if right_sum == left_sum:
                return i-1
        return -1
        
        