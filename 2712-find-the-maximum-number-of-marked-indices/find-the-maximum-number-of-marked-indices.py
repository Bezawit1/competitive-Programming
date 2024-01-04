class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        i = 0
        j =( len(nums) + 1 )//2
        count = 0
        while j < len(nums):
            if nums[i]*2 <= nums[j]:
                count+=2
                i+=1
                
            j+=1
        return count



 
       
        