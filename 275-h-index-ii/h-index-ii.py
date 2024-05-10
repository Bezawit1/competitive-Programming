class Solution(object):
    def hIndex(self, citations):
        left = 0 
        right = len(citations) - 1
        while left <= right:
            mid = left + (right - left)//2
            if citations[mid]>=len(citations) - mid:
                right = mid -1
            else:
                left = mid + 1
        return len(citations) - left
        
        