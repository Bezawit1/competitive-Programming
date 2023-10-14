class Solution(object):
    def rearrangeArray(self, nums):
        positive_nums = []
        negative_nums = []
        res =[]
        for i in nums:
            if i > 0:
                positive_nums.append(i)
            elif i < 0 :
                negative_nums.append(i)
        for i in range(len(positive_nums)):
            res.append(positive_nums[i])
            res.append(negative_nums[i])
        return res


       

        
        