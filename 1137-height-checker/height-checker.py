class Solution(object):
    def heightChecker(self, heights):
        real = list(heights)
        expected = sorted(heights)
        count = 0
        
        for i in range(len(expected)):
            if real[i] != expected[i]:
                count += 1
                
        return count
