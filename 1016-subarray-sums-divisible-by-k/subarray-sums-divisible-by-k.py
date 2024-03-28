class Solution(object):
    def subarraysDivByK(self, nums, k):
        hash_map={0:1}
        prefix_sum = 0
        count = 0
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) %k
            if prefix_sum in hash_map:
                count +=hash_map[prefix_sum]
            if prefix_sum in hash_map:
               hash_map[prefix_sum] += 1
            else:
               hash_map[prefix_sum] = 1
        return count