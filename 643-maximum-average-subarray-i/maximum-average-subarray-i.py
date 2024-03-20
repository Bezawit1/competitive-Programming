class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum = 0
        max_avg = float('-inf')
        curr_sum = sum(nums[:k])
        print(curr_sum)
        for i in range(len(nums)-k + 1):
            left = i 
            right = i+k
            curr_avg =curr_sum/float(k)
            max_avg = max(max_avg ,curr_avg)
            if right  < len(nums):
                curr_sum-=nums[left]
                curr_sum+=nums[right]
                
            
        return max_avg
        

           


       

       