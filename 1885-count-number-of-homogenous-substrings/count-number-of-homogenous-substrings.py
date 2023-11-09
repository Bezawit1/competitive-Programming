class Solution(object):
    def countHomogenous(self, s):
        count = len(s)
        unique = set(s)
        if len(unique) == 1:
            return (len(s) * (len(s)+1)//2)% (10**9 + 7)
      
      
        i = 0

        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                count += 1
                j += 1

            i+=1

        return count % (10**9 + 7)

        

        
        