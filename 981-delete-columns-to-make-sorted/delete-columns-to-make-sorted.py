class Solution(object):
    def minDeletionSize(self, strs):
        cols = []
        count = 0
        for col in range(len(strs[0])):
            columns = [row[col] for row in strs]
            cols.append(columns)
        
        for i in cols:
           
            if i != sorted(i):
                count+=1
        return count
        