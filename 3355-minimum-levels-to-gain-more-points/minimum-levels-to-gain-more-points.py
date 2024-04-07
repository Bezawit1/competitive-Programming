class Solution(object):
    def minimumLevels(self, possible):
        daniel_score = 0
        count_zeroes = possible.count(0)
        count_ones = possible.count(1)
        bob_score = count_ones - count_zeroes
        for i in range(len(possible) - 1):
            if possible[i] == 0:
                daniel_score-=1
                bob_score+=1
            else:
                daniel_score+=1
                bob_score-=1
            
            if daniel_score > bob_score:
                return i + 1
                break
        return -1


       
        