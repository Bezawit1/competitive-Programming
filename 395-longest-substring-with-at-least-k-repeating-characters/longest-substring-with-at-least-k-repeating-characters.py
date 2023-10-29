class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k :
            return 0
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] =  1
            else:
                freq[char] +=1
       
        for idx , char in enumerate (s):
            if freq[char] < k:
                left_substring = self.longestSubstring(s[:idx],k)
                right_substring = self.longestSubstring(s[idx+1:],k)
                return max(left_substring ,right_substring)
        return len(s)
            
        