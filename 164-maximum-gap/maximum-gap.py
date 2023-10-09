class Solution(object):
    def maximumGap(self ,nums):
        if len(nums) < 2:
            return 0

        min_num= min(nums)
        max_num =  max(nums)
        bucket = max(1, (max_num - min_num) // (len(nums) - 1))
        num_buckets = (max_num - min_num) // bucket + 1
        buckets = [[] for _ in range(num_buckets)]

        for num in nums:
            index = (num - min_num) // bucket
            buckets[index].append(num)

        prev_max = min_num
        max_gap = 0

        for i in range(num_buckets):
            if buckets[i]:
                min_bucket, max_bucket = min(buckets[i]), max(buckets[i])
                max_gap = max(max_gap, min_bucket - prev_max)
                prev_max = max_bucket

        return max_gap


        