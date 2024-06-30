class Solution(object):
    def maxScore(self, s):
        ones = s.count('1')
        zeroes = 0
        max_score = 0
        
        
        
        for i in range(len(s)-1):
            if s[i] == "0":
                zeroes+=1
            else:
                ones-=1
            
            max_score= max(max_score , zeroes+ones)
        
        return max_score
        