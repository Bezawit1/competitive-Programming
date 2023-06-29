class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        sum = 0
        start_index = 1
        end_index = int(2 * len(piles) / 3)

        while start_index < end_index:
            sum += piles[start_index]
            start_index += 2

        return sum
