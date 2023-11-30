class Solution(object):
    def maxArea(self, height):
        max_area =  0
        i=0
        j=len(height) -1 
        while i < j :
            if height[i] < height[j]:
                curr_area = height[i]*(j-i)
                i+=1
                max_area = max(max_area , curr_area)
            else:
                curr_area = height[j]*(j-i)
                j-=1
                max_area = max(max_area , curr_area)
        return max_area



        
        