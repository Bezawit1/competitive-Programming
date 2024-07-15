class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
       

# 1. Sort the tasks array based on enqueue time (tasks[i][0]).
# 2. Initialize a min-heap to store tasks based on processing time and original index.
# 3. Initialize a current_time variable to track the current time.
# 4. Iterate through the tasks array:
#    - Push tasks with the same enqueue time as current_time into the min-heap.
# 5. Initialize an empty list  to store the order of task processing.
# 6. Process tasks using the CPU:
#    - While the min-heap is not empty:
#      - Pop the task with the shortest processing time from the min-heap.
#      - Append the original index of the task to the `order` list.
#      - Update current_time by adding the processing time of the popped task.
#      - Push any tasks with an enqueue time <= current_time into the min-heap.
# 7. Return the  list, which contains the indices of tasks in the order they are processed.
    
#         
        n = len(tasks)
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        heap = []
        i = 0
        curr_time = tasks[0][0]
        res = []


        while i < n:
            if tasks[i][0] == curr_time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]]) 
            else:
                break
            i += 1

        while heap:
            
            processing_time, original_index = heapq.heappop(heap)
            res.append(original_index)
            curr_time += processing_time

            
            while i < n and tasks[i][0] <= curr_time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1

       
            if not heap and i < n:
                curr_time = tasks[i][0]
                while i < n:
                    if tasks[i][0] == curr_time:
                        heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                    else:
                        break
                    i += 1

        return res


        