class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start_index = 0
        end_index = 0
        maxLen = 0
        unique = set()
        while end_index <len(s):
            
            if s[end_index] not in unique:
                unique.add(s[end_index])
             
                end_index +=1
                maxLen = max(maxLen , end_index - start_index)
                
            else:
               
                unique.remove(s[start_index])
                start_index +=1
                
             
        return maxLen


            

      
      
        
        