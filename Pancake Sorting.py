class Solution(object):
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for i in range(n):
            max_idx = arr.index(max(arr[:n-i]))
            arr[:max_idx+1] = arr[:max_idx+1][::-1]
            res.append(max_idx+1)
            arr[:n-i] = arr[:n-i][::-1]
            res.append(n-i)
        return res
