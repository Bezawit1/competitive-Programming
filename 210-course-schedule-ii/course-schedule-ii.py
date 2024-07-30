class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        
        graph = defaultdict(list)
        incoming_degree = [0 for _ in range(numCourses)]
        
        # build the graph
        for course,preq in prerequisites:
            graph[preq].append(course)
            incoming_degree[course]+=1
        # initialize queue
        queue = deque()
        order = []
        for course in range(numCourses):
            if incoming_degree[course] == 0:
                queue.append(course)

        while queue:
            current_course = queue.popleft()
            order.append(current_course)

            # decrease the inoming degree of the neighbouring 
            for neighbour in graph[current_course]:
                incoming_degree[neighbour]-=1
                if incoming_degree[neighbour] == 0:
                    queue.append(neighbour)

        return order if len(order) == numCourses else []





        
