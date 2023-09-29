class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area_max = 0
        while left < right:
            base = min (height[right] , height[left])
            area_max = max(area_max ,(right- left)* base)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1

            
        return area_max
            

        