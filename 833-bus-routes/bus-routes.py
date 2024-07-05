class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for bus , bus_stops in enumerate(routes):
            for bus_route in bus_stops:
                graph[bus_route].append(bus)
        queue = deque(graph[source])
        visited = set(graph[source])
        count = 0
        if source == target:
            return 0
        while queue:
            count+=1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if target in routes[curr]:
                    return count
                for route in routes[curr]:
                    for next_bus in graph[route]:
                        if next_bus not in visited:
                            visited.add(next_bus)
                            queue.append(next_bus)
        return -1