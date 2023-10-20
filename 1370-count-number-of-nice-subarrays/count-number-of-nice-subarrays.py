class Solution(object):
    def numberOfSubarrays(self, nums, k):
       
        odd = []  
        curr_rem = 0 
        count = 0  

        for num in nums:
            curr_rem += num % 2
            odd.append(curr_rem)

        prefix_sum = {0: 1}  
        for num in odd:
            if num - k in prefix_sum:
                count += prefix_sum[num - k]
            if num not in prefix_sum:
                prefix_sum[num] = 1
            else:
                prefix_sum[num] += 1

        return count







