class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 1
        original_can = capacity
        for i in range(len(plants)-1):
            capacity -=plants[i]
            if capacity < plants[i+1]:
                capacity = original_can
                steps+=((i + 1) * 2 ) + 1
            else:steps+=1
            
        return steps


        
        