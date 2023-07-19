class Solution(object):
    def minEatingSpeed(self, piles, h):
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            mid_speed = (min_speed + max_speed) // 2
            total_hours = 0

            for bananas in piles:
                total_hours += (bananas - 1) // mid_speed + 1

            if total_hours > h:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed

        return min_speed
        