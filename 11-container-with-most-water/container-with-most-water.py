class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            current_area = min(height[i] , height[j]) * (((j + 1) - (i + 1)))
            max_area = max(current_area , max_area)
            if height[i] < height[j]:
                i+=1
            else:
               j-=1
        return max_area

