
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = [] # k-values
        for i in range(len(arr)):
            max_index = arr.index(max(arr[:len(arr)-i]))
            print(max_index+1)
            arr[:max_index +1] = arr[:max_index +1][::-1]
            print(arr)
            flips.append(max_index+1)
            print(flips)
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
            print(arr)
            flips.append(len(arr)-i)
        return flips