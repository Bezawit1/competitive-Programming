class Solution(object):
    def findMaxAverage(self, nums, k):
        	# SLIDING WINDOW TECHNIQUE
        sums = sum(nums[:k]) #sum of the first k elemnets of the array
        maxSums = sums
        for i in range(len(nums)-k):
            sums -= nums[i]
            sums += nums[i+k]
            maxSums = max(maxSums, sums)
        return maxSums/float(k)
	