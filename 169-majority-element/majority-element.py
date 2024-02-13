class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        max_freq = 0
        max_element = None
        
        for key in count.keys():
            if count[key] > max_freq:
                max_freq = count[key]
                max_element = key
                
        return max_element
                    