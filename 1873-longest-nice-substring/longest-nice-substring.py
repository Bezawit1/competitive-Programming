class Solution(object):
   def longestNiceSubstring(self, s):
    def isPresent(sub):
        for char in sub:
            opp= char.lower() if char.isupper() else char.upper()
            if opp not in sub:
                return False
        return True
    
    longest_substring = ""
    
    for i in range(len(s)):
        for j in range(i + len(longest_substring), len(s) + 1):
            substring = s[i:j]
            if isPresent(substring) and len(substring) > len(longest_substring):
                longest_substring = substring
    
    return longest_substring




        

        
         
        
       