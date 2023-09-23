class Solution(object):
    def isAnagram(self, s, t):
        hashmap={}
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
      
        