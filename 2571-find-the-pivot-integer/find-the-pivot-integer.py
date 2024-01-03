class Solution(object):
    def pivotInteger(self, n):
        prefix_sum = [0]
        for i in range(1 ,n+1):
            prefix_sum.append(i + prefix_sum[-1])
        left = 0
        right = prefix_sum[-1]
        for i in range(1,len(prefix_sum)):
            if prefix_sum[i] == right - prefix_sum[left]:
                return i
            left+=1
        return -1

    
        

        