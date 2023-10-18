class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0 
        for i in range(len(s) - 3 + 1):
            unique_chars = set(s[i:i+3])
          
            if len(unique_chars) == 3:
                count+=1
        return count

        



       
        