class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        prevRow=self.getRow(rowIndex-1)
        current=[1]
        for i in range(len(prevRow)-1):
            current.append(prevRow[i]+prevRow[i+1])
        current.append(1)
        return current
            
        