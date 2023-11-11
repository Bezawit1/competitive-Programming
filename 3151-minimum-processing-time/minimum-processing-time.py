class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        tasks.sort()
        processorTime.sort(reverse=True)
        min_Time = 0
        window_size = len(tasks) // len(processorTime)
        j = 0 

        i = window_size - 1
        while j < len(processorTime) and i < len(tasks):
            max_Time = tasks[i] + processorTime[j]
            j += 1
            i += window_size 
            min_Time = max(min_Time, max_Time)
        return min_Time




       
        