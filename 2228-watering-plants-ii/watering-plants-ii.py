class Solution(object):
   def minimumRefill(self, plants, capacityA, capacityB):
        left, right = 0, len(plants) - 1
        waterA, waterB = capacityA, capacityB
        refills = 0
        while left <= right:
			
            if left != right and plants[left] > waterA:
                waterA = capacityA
                refills += 1
			
			
            if left != right and plants[right] > waterB:
                waterB = capacityB
                refills += 1
			
			
            if left == right:
                max_water = max(waterA, waterB)
                if plants[left] > max_water:
                    refills += 1
			
			
            waterA -= plants[left]
            waterB -= plants[right]
            left += 1
            right -= 1
        return refills


        