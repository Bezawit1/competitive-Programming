class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        sorted_balloons = sorted(points, key=lambda x: x[1])
        
        arrow_needed = 1
        end_position = sorted_balloons[0][1]
        
        for balloon in sorted_balloons[1:]:
            start, end = balloon
            if start > end_position:
                arrow_needed += 1
                end_position = end
        
        return arrow_needed


        