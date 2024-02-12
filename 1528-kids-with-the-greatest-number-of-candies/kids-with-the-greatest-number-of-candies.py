class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        res = []
        for i in range (len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res.append(True)
            else:
              res.append(False)
        return res

        