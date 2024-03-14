class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        i = 0 
        j = 0 
        players.sort()
        trainers.sort()
        count = 0
        while i < len(players):
            while j < len(trainers) and i < len(players):
                if players[i]<=trainers[j]:
                    count+=1
                    j+=1
                    i+=1
                else:
                    j+=1
            i+=1
        return count

       
        