class Solution(object):
    def pivotIndex(self, nums):

        prefix_sum = [0]
       
        for  i in nums:
            prefix_sum.append(i + prefix_sum[-1])
        left  = 0
        total_sum= prefix_sum[-1]
        for i in range(1,len(prefix_sum)):
            if total_sum- prefix_sum[i] == prefix_sum[left]:
                return left
            left +=1
        return -1
            
       