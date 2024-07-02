

class Solution(object):
    def edgeScore(self, edges):
        graph = defaultdict(list)
        max_sum = 0
        max_key = None
        
        for i, edge in enumerate(edges):
            graph[edge].append(i)
        
        for key, val in graph.items():
            current_sum = sum(val)
            if current_sum > max_sum:
                max_sum = current_sum
                max_key = key
            elif current_sum == max_sum:
                if max_key is None or key < max_key:
                    max_key = key
        
        return max_key

