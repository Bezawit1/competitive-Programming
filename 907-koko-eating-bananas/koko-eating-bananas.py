class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid_speed = (left + right) // 2
            total_hours = 0

            for bananas in piles:
                total_hours += (bananas - 1) // mid_speed + 1

            if total_hours > h:
                left = mid_speed + 1
            else:
                right = mid_speed

        return left
        