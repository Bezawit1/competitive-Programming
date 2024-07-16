class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        remaining = k - numOnes - numZeros
        if remaining <= 0:
            return numOnes
        return numOnes - remaining 

            

        