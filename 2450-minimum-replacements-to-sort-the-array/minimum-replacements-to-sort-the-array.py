class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        end_val = nums[-1]
        count = 0
        for i in range(len(nums)-2 , -1 ,-1):
            if nums[i] > end_val:
                pieces = (nums[i] - 1)//end_val
                end_val = nums[i]//(pieces+1)
                count+= pieces
            else:
                end_val = nums[i]
        return count
                
            

            
