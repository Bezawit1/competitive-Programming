class Solution(object):
    def winnerOfGame(self, colors):
        n = len(colors)
        if n < 3:
            return False
        left = 0
        right = 0
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == "A":
                left += 1

            if colors[i - 1] == colors[i] == colors[i + 1] == "B":
                right += 1

        return left > right
