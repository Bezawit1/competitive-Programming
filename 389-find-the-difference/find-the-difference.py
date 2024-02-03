class Solution(object):
    def findTheDifference(self, s, t):
            res = ''
            for i in t:
                if i not in s:
                    res+=i
                else:
                    if s.count(i)!=t.count(i):
                       return i
            return res