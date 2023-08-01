class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left , right  =  1, max(nums)
       
        while left <=right:
            mid=left + (right - left) //2
            total_sum = sum((num + mid - 1) // mid for num in nums)
            if total_sum <=threshold:
                right = mid -1
            else:
                left = mid +1
        return left


        