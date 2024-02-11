class Solution(object):
    def majorityElement(self, nums):
        freq = len(nums)//3
        counts = Counter(nums)
        res = []

        for num,count in counts.items():
            if count>freq:
                res.append(num)
        return res
        