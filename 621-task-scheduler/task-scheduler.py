

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [(-freq, task) for task, freq in count.items()] 

        heapify(max_heap) 

        minimum_intervals = 0

        running_batch = []
       
        while max_heap:
            cycle = 0
            running_batch = []
            while max_heap and cycle <= n:
                frequency, task = heappop(max_heap)
                running_batch.append((frequency+1, task))
                cycle += 1
            for frequency, task in running_batch:
                if frequency != 0:
                    heappush(max_heap, (frequency, task))
            if max_heap:
                minimum_intervals += n + 1  # Full cycle including idle times
            else:
                minimum_intervals += cycle  # Last cycle with remaining tasks
            

        return minimum_intervals