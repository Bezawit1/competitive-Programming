class Solution(object):
    def findMaxAverage(self, nums, k):
        	
        currSum = sum(nums[:k]) 
        maxSum = currSum
        for i in range(len(nums)-k):
            currSum -= nums[i]
            currSum += nums[i+k]
            maxSum = max(maxSum, currSum)
        return maxSum/float(k)
	