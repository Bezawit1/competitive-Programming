class NumArray(object):

    def __init__(self, nums):
        self.prefix_sum = []
        sum = 0
        for i in nums:
            sum+=i
            self.prefix_sum.append(i)

    def sumRange(self, left, right):
        return sum(self.prefix_sum[left : right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)