class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total_sum = 1
        patches_needed = 0
        idx = 0
        while total_sum <= n:
            if  idx <len(nums) and nums[idx]<=total_sum :
                total_sum+=nums[idx]
                idx+=1
            else:
                total_sum+=total_sum
                patches_needed+=1
        return patches_needed
        

        