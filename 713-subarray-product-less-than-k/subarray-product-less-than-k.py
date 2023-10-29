class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        start_index = 0
        end_index = 0
        countArrays = 0
        product = 1

        while end_index < len(nums):
            product *= nums[end_index]
            while product >= k and start_index <= end_index:
                product /= nums[start_index]
                start_index += 1

            countArrays += end_index - start_index + 1
            end_index += 1

        return countArrays


