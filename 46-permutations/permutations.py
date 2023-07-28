class Solution(object):
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recursively generate permutations for the rest of the array
                nums[start], nums[i] = nums[i], nums[start]  

        result = []
        backtrack(0)
        return result