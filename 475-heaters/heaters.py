class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0  
        j = 0  

        

        while i < len(houses):
            while j < len(heaters) and houses[i] > heaters[j]:
                j += 1

            if j == len(heaters):
                radius = max(radius, houses[-1] - heaters[-1])
                break

            if j > 0:
                radius = max(radius, min(heaters[j] - houses[i], houses[i] - heaters[j - 1]))
            else:
                radius = max(radius, heaters[j] - houses[i])

            i += 1
        return radius

   
            
       



        