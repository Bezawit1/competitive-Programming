class Solution(object):
    def pivotArray(self, nums, pivot):
        lower_bound = []
        upper_bound = []
        equal = []
        i = 0 
       
        while i  < len(nums) :
            if nums[i] < pivot:
                lower_bound.append(nums[i])
            elif nums[i] > pivot:
                upper_bound.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            i+=1
        merged_list = lower_bound + equal + upper_bound
        return merged_list
            
                 
        
      