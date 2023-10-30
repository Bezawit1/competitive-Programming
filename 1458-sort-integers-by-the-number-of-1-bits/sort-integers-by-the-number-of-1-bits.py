class Solution(object):
    def sortByBits(self, arr):
        def countBitsOnes(num):
            return bin(num).count('1')
        arr.sort(key=lambda x: (countBitsOnes(x), x))

        return arr