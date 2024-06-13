class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        res = [0 for _ in range(n)]
        for i , j in edges:
            res[j]+=1
        answer = []
        for i in range(n):
            if res[i]==0:
                answer.append(i)
        return answer        