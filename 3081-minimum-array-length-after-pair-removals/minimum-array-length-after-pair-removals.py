class Solution(object):
    def minLengthAfterRemovals(self, nums):
        left = 0
        right = (len(nums)+1)//2
        count = 0
        while right< len(nums) :
            
            if nums[left] < nums[right]:
                left +=1
                right+=1
                count+=2
            else:
                right +=1
               
                

                
        return len(nums) - count
        