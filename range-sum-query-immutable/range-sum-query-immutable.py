class NumArray(object):

    def __init__(self, nums):
        self.prefix_sum =[]
        sum=0
        for i in nums:
            sum+=i
            self.prefix_sum.append(sum)
        
        

    def sumRange(self, left, right):
        if left >0 and right>0:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        return self.prefix_sum[right] or self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)