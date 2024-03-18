class Solution(object):
    def smallestDivisor(self, nums, threshold):
        i =  1
        j = max(nums)
       
        while i <=j:
            mid=i + (j- i) //2
            total_sum = sum((num + mid - 1) // mid for num in nums)
            if total_sum <=threshold:
                j= mid -1
            else:
                i = mid +1
        return i


        