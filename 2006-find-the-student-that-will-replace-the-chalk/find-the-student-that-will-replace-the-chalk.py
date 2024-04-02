class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_sum = sum(chalk)
        k%=total_sum
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k-=chalk[i]
        return -1
       