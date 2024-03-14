class Solution(object):
    def partitionLabels(self, s):
        """
        track the elements and store the index of their last occurence
        find the maximum size by traversing through the array
        when the index and last occurence are equal append and strat from the next index until reached the end of the string
        
        """

        occurence = {}
        res = []
        start_idx = 0
        end_idx = 0
        for i , char in enumerate(s):
            occurence[char] = i
        for i , char in enumerate(s):
            end_idx = max(end_idx , occurence[char])
            if i == end_idx:
                res.append(end_idx - start_idx + 1)
                start_idx = i +1
        return res

        
       
        