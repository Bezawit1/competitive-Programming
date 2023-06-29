class Solution(object):
    def addSpaces(self, s, spaces):
        newS=[]
        idx=0
        n=len(spaces)
        for i in spaces:
            newS.append(s[idx:i])
            idx=i
        newS.append(s[spaces[len(spaces)-1]:])
        return " ".join(newS)
