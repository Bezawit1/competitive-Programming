class Solution(object):
    def calcEquation(self, equations, values, queries):
        def dfs(node, target, visited):
            if node == target:
                return 1.0
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0

        graph = defaultdict(list)

   
        for i, (numerator, denominator) in enumerate(equations):
            value = values[i]
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1.0 / value))

        answers = []
        for query in queries:
            start, end = query
            if start not in graph or end not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(start, end, set()))

        return answers
        