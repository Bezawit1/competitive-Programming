class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
      
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i , 0) + 1
       
        sorted_by_frequency = sorted(hash_map.items(), key=lambda x: x[1])

        for key, value in sorted_by_frequency:
            if value <= k:
                k -= value
                del hash_map[key]
            else:
                break
        return len(hash_map)
            
        


