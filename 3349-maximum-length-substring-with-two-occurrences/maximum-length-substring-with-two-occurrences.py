class Solution(object):
    def maximumLengthSubstring(self, s):
        hash_map = {}
        i , j ,max_len = 0 , 0 ,0
        
        while j < len(s):
            if s[j] not in hash_map:
                hash_map[s[j]] = 0
            
            
            hash_map[s[j]]+=1
            while hash_map[s[j]] > 2:
                hash_map[s[i]]-=1
                if hash_map[s[i]]==0:
                    del hash_map[s[i]]
                i+=1
            max_len = max(max_len , j - i + 1)
            j+=1
        return max_len
        
                
        
            
       
        