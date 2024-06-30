class Solution(object):
    def kthLargestNumber(self, nums, k):
        sorted_nums = sorted(map(int, nums), reverse=True) 
        return str(sorted_nums[k-1])
        