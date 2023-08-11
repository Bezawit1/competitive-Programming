class Solution(object):
    def minSetSize(self, arr):
        counter = Counter(arr)
        occurence = sorted(counter.values(), reverse=True)
        total_num = 0
        count_num = 0
        for count in occurence:
            total_num += count
            count_num += 1
            if total_num >= len(arr) / 2:
                break
                
        return count_num

    
        