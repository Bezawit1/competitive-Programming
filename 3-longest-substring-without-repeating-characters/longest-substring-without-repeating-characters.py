class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap={}
        maxLen=0
        left=0
        

        
        for i in range(len(s)):
            char=s[i]
            if char in hashmap and hashmap[char]>=left :
                left = hashmap[char] + 1  
                  
            hashmap[char]=i
            curr_len = i-left+1
            maxLen=max(maxLen,curr_len)

        return maxLen 



       