class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        i = 0
        j = (len(nums) + 1 )//2
        count = 0
        while j < len(nums):
            if 2*nums[i] <=nums[j]:
                count+=2
                i+=1
                j+=1
            
            else:
                j+=1
        return count
         
        


        