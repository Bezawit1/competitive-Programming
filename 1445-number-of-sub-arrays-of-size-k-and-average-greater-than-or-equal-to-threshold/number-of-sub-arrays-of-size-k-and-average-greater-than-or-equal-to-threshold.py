class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        curr_sum = sum(arr[:k])  

        for i in range(len(arr) - k + 1):
            if curr_sum >= threshold * k:
                count += 1

            if i + k < len(arr):
                curr_sum = curr_sum - arr[i] + arr[i + k]

        return count


       
        