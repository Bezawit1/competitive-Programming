class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0 
        j = 0 
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and secondList[j][0] <= firstList[i][1]:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return res

        