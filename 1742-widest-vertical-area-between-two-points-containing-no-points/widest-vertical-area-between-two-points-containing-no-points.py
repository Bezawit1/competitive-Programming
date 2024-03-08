class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        sorted_points = sorted(points , key= lambda x:x[0])
        diff = 0
        for i in range(len(sorted_points) - 1):
            diff = max(diff , abs(sorted_points[i][0]   - sorted_points[i+1][0]))   
        return diff
        