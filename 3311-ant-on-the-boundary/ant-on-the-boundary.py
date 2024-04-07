class Solution(object):
    def returnToBoundaryCount(self, nums):
        boundary_count = 0
        curr_sum = 0
        for i in nums:
            curr_sum+=i
            if curr_sum ==0:
                boundary_count+=1
        return boundary_count
        