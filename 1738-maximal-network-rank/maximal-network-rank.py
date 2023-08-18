class Solution(object):
    def maximalNetworkRank(self, n, roads):
        cities = {}
        
        for road in roads:
            for city in road:
                if city not in cities:
                    cities[city] = 0
                cities[city] += 1
        
        n_max = 0
        for i in range(n):
            for j in range(i + 1, n):
                curr_rank = cities.get(i, 0) + cities.get(j, 0)
                if [i, j] in roads or [j, i] in roads:
                    curr_rank -= 1
                n_max = max(n_max, curr_rank)
        
        return n_max