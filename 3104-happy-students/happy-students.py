class Solution(object):
    def countWays(self, nums):
        count_group = 1
        nums.sort()
        if nums[0] !=0:
            count_group+=1
        for i in range(len(nums)-1):
            if nums[i] < i+1 < nums[i+1]:
                count_group+=1
        return count_group
        

        
        