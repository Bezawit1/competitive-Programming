class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum = []
        max_len = 0
        curr_sum = 0
        hash_map = {0: -1}  
        for index, num in enumerate(nums):
            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            prefix_sum.append(curr_sum)

        for i in range(len(prefix_sum)):
            if prefix_sum[i] in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum[i]])
            else:
                hash_map[prefix_sum[i]] = i
        return max_len
