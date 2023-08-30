class Solution(object):
    def findCircleNum(self, isConnected):
        totalProvince = 0
        n=len(isConnected)
        visited=[False]*n

        def helper(currCity):
            visited[currCity] = True
            for i in range(n):
                if isConnected[i][currCity] == 1 and not visited[i]:
                    helper(i)
        for city in range(n):
            if not visited[city]:
                helper(city)
                totalProvince += 1
            
        return totalProvince
            



        