class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        min_heap = []
        
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        print(min_heap)
        result = []
        
        
        while min_heap and len(result) < k:
            sum_val, index1, index2 = heappop(min_heap)
          
            result.append([nums1[index1], nums2[index2]])
            
            
            if index2 + 1 < len(nums2):
                heappush(min_heap, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))
        
        return result
