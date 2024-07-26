class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequent_tasks = Counter(tasks)
        
        most_frequent = max(frequent_tasks.values())
       
        counter = 0
        for i in frequent_tasks.values():
            if i == most_frequent :
                counter = counter + 1
                

        cool_time = (most_frequent - 1) * (n + 1) + counter
        
        return max(cool_time, len(tasks))