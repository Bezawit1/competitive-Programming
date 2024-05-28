class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        max_len = 0
        j = 0
        total_sum = 0
        for i in range(len(s)):
           
                total_sum +=abs(ord(s[i]) - ord(t[i]))
                while total_sum > maxCost:
                    total_sum-=abs(ord(s[j]) - ord(t[j]))
                    j+=1
                max_len = max(max_len , i- j + 1)
        return max_len
                    


    
        