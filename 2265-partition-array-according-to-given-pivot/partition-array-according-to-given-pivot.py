class Solution(object):
    def pivotArray(self, nums, pivot):
        lower_bound = []
        upper_bound = []
        equal = []
        for num in nums:
            if num < pivot:
                lower_bound.append(num)
            elif num > pivot:
                upper_bound.append(num)
            else:
                equal.append(num)
        merged_list = lower_bound + equal + upper_bound 
        return merged_list
            
                 
        
      