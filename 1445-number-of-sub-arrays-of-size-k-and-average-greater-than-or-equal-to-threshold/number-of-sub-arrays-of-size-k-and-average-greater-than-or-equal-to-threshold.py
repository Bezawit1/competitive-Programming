class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        curr_sum = sum(arr[:k])  

        for i in range(len(arr) - k + 1):
            left = i
            right = i + k
            if curr_sum >= threshold * k:
                count += 1
            
            if right < len(arr):
                curr_sum = curr_sum - arr[left] + arr[right]

        return count


       
        