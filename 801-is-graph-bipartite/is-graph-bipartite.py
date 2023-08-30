class Solution(object):
    def isBipartite(self, graph):
        # coloring method using dfs 
#create array of colors initially 0 it represents uncolored nodes
#create a helper fucntion to traverse each node
        n = len(graph)
        colors = [0] * n 
        def helper(node, color):
            colors[node] = color
            for i in graph[node]:
                if colors[i] == color:#neigbor has the same color
                    return False
                if colors[i] == 0 and not helper(i, -color): # if neigbor is uncolored and not valid results false when called with -color
                    return False
            return True
#main function 
        for node in range(n):
            if colors[node] == 0 and not helper(node, 1):
                return False
        return True

        