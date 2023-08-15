class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        left_index = 0
        right_index = n-1
        res=[]
        while left_index < right_index:
            target_sum = numbers[left_index] + numbers[right_index]
            if target_sum == target:
                res.append(left_index + 1)
                res.append(right_index + 1)
                break
            if target_sum > target:
                right_index-=1
            if target_sum < target:
                left_index+=1
        return res
                

        