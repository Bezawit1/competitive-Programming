class Solution(object):
    def findJudge(self, n, trust):
        trust_people= []
        count ={} 
        for i,j in trust:
            trust_people.append(i)
            if j in count:
                count[j] +=1
            else:
                count[j] =1
        for i in range(1,n+1):
            if i not in trust_people and count.get(i,0) == n-1:
                return i
        return -1
       
            

        