class Solution(object):
    def subarraysDivByK(self, nums, k):
        remainder_map={0:1}
        prefix_sum = 0
        count = 0
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) %k
            if prefix_sum in remainder_map:
                count += remainder_map[prefix_sum]
            if prefix_sum in remainder_map:
                remainder_map[prefix_sum] += 1
            else:
                remainder_map[prefix_sum] = 1
        return count