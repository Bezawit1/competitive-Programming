class Solution(object):
    def waysToMakeFair(self, nums):
        def isFair(index):
            even_before_removal = even_prefix_sum[index]
            even_after_removal = even_prefix_sum[-1] - even_prefix_sum[index + 1]
            
            odd_before_removal = odd_prefix_sum[index]
            odd_after_removal = odd_prefix_sum[-1] - odd_prefix_sum[index + 1]
            
            return even_before_removal + odd_after_removal == odd_before_removal + even_after_removal
        
        even_prefix_sum, odd_prefix_sum = [0], [0]
        for i in range(len(nums)):
            if i % 2:
                odd_prefix_sum.append(odd_prefix_sum[-1] + nums[i])
                even_prefix_sum.append(even_prefix_sum[-1])
            else:
                even_prefix_sum.append(even_prefix_sum[-1] + nums[i])
                odd_prefix_sum.append(odd_prefix_sum[-1])
        
        count_fair_indices = 0
        for i in range(len(nums)):
            if isFair(i):
                count_fair_indices += 1
        
        return count_fair_indices

