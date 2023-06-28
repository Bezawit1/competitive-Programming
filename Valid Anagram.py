class Solution(object):
    def isAnagram(self, s, t):
      
        if len(s)!=len(t):
           return False
        character1 = list(s)
        character1.sort()
        character2 =list(t)
        character2.sort()
        joined =''.join(character1)
        joined2 =''.join(character2)
        return joined == joined2
