class Solution(object):
    def arrayChange(self, nums, operations):
        
        hashmap = {}
        
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for operation in operations:
            if operation[0] in hashmap:
                index = hashmap[operation[0]]
                nums[index] = operation[1]
                del hashmap[operation[0]]
                hashmap[operation[1]] = index
        
        return nums
