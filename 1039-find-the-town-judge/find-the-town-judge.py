class Solution(object):
    def findJudge(self, n, trust):
        trust_people=[0]*(n + 1)
        trust_count = [0] * (n + 1)


        for i ,j in trust:
            trust_people[i] += 1
            trust_count[j] += 1
        for i in range(1,n + 1):
            if trust_people[i] ==0 and trust_count[i] == n-1:
                return i
        return -1
        


