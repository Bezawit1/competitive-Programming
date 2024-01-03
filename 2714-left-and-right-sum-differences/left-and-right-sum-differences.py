class Solution(object):
    def leftRightDifference(self, nums):
            left_sum = [0]
            right_sum = [sum(nums) - nums[0]]
            answer = [abs(left_sum[0] - right_sum[0])]
        
            for i in range(1,len(nums)):
                left_sum.append(nums[i-1] + left_sum[-1])
                right_sum.append(right_sum[-1] - nums[i])
                answer.append(abs(left_sum[i] - right_sum[i]))
            return answer
            
            
        