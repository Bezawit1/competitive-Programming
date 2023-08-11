class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        max_heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(max_heap)
    
        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])  
    
        return result 
        
        
       