class Solution(object):
    def maxScore(self, s):
        sum_ones = s.count('1')
        max_score = 0
        
        sum_zeroes = 0
        
        for i in range(len(s)-1):
            if s[i] == "0":
                sum_zeroes+=1
            else:
                sum_ones-=1
            
            max_score= max(max_score , sum_zeroes+sum_ones)
        
        return max_score
        