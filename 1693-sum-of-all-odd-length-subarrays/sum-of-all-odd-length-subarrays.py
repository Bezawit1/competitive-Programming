class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        odd_sum = 0
        total_sum = sum(arr)
        for i in range(len(arr)):
            for j in range( 1, len(arr) - i + 1 , 2 ):
                end = i + j - 1
                odd_sum += sum(arr[i:end + 1])
        return odd_sum