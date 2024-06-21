class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, req in prerequisites:
            graph[course].append(req)
        
    
        visited = [0] * numCourses
        
    
        def dfs(course):
            if visited[course] == -1:
                return False  
            if visited[course] == 1:
                return True   
            
            visited[course] = -1  
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited[course] = 1  
            return True
        
    
        for i in range(numCourses):
            if not dfs(i):
                return False 
        
        return True 
            
        