class Solution(object):
    def pivotIndex(self, nums):
  
        prefix_sum = [0]
        for i in range(0,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        print(prefix_sum)
        left = 0
        right_sum = prefix_sum[-1]

        while left < len(prefix_sum) - 1:
            if prefix_sum[left] == right_sum - prefix_sum[left+1]:
                return left 
            left+=1
        return -1

        