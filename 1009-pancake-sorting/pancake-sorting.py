
        
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = [] # k-values
        for i in range(len(arr)):
            max_index = arr.index(max(arr[:len(arr)-i]))
            
            arr[:max_index +1] = arr[:max_index +1][::-1]
          
            flips.append(max_index+1)
            
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
          
            flips.append(len(arr)-i)
        return flips
        