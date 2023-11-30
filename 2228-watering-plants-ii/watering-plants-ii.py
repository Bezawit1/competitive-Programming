class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        i = 0
        j = len(plants) - 1
        orgA = capacityA
        orgB = capacityB
        counter = 0
        while i <= j :
            if i!=j:
               
                if capacityA < plants[i]:
                    counter+=1
                    capacityA = orgA

                if capacityB < plants[j]:
                    counter+=1
                    capacityB = orgB
            if i == j:
                max_water = max(capacityA, capacityB)
                if plants[i] > max_water:
                        counter += 1
            capacityA-=plants[i]
            capacityB-=plants[j]
            i+=1
            j-=1
        return counter


        
        
        