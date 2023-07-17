class Solution(object):
    def subarraySum(self, nums, k):
        dict = {0: 1}
        frequency = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            difference = current_sum - k
            if difference in dict:
                frequency += dict[difference]
            
            dict[current_sum] = dict.get(current_sum, 0) + 1
        
        return frequency
       