class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i= 0 
        j = 0
        maxDis = 0
        char_set = set()
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                maxDis = max(maxDis, j - i)
            else:
                char_set.remove(s[i])
                i += 1
           
        return maxDis
        
        

       