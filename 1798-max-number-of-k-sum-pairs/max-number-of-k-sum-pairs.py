class Solution(object):
    def maxOperations(self, nums, k):
        i=0
        j=len(nums)-1
        count=0
        nums.sort()
        while i<j:
            if nums[i]+nums[j] == k:
                count+= 1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]>k:
                j-=1
        return count


        