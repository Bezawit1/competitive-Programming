class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        MOD = 10**9 + 7
        while i <= j:
            if nums[i] + nums[j] <= target:
                count += pow(2, j - i, MOD)
                count %= MOD  
                i += 1
            else:
                j -= 1
        return count

        
        


        
        