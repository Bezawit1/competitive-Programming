class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
       
        totalBottles = numBottles 
        emptyBottles = numBottles
        while emptyBottles >=numExchange :
            fullBottles = emptyBottles // numExchange
            totalBottles += fullBottles
            emptyBottles = emptyBottles % numExchange + fullBottles

        return totalBottles

