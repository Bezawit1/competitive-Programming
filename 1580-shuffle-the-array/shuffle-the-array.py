class Solution(object):
    def shuffle(self, nums, n):
        i =0
        j=n
        arr=[]
        while i<j and j<len(nums):
            arr.append(nums[i])
            arr.append(nums[j])
            i+=1
            j+=1
        return arr
        