class Solution(object): 
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        right = len(piles)-1
        sum = 0
        endindex = int(2 * len(piles) / 3)
        for i in range(1,endindex,2):
            sum+=piles[i]
        return sum
     

      
        