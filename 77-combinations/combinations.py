class Solution(object):
    def combine(self, n, k):
        res = []
        def backTrack(i,candidate):
            if len(candidate) == k:
                res.append(candidate[:])
                return

                
            for num in range(i, n + 1):
                candidate.append(num)
                backTrack(num + 1, candidate)
                candidate.pop()
        backTrack(1,[])
        return res
