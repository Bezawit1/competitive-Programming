class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        original_sum = 0
        for  i in range(len(nums)+1):
            original_sum +=i
        
        missing_num = original_sum - sum(nums)
        print(original_sum , sum(nums))
        return missing_num
       
        