class Solution(object):
    def findWinners(self, matches):
        count_losers = 0 
        hashmap = {}
        res =[]
        losers = []
        winners = []
        for i in range(len(matches)) :
            hashmap[matches[i][1]] = hashmap.get(matches[i][1] , 0 ) + 1
        for i in range(len(matches)):
            if matches[i][0] not in hashmap and  matches[i][0] not in winners:
                winners.append(matches[i][0])
        winners =sorted(winners)   
        for key,val in hashmap.items():
            if val == 1:
                losers.append(key)
        losers = sorted(losers)
        return [winners , losers]
            
        
       