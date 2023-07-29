class Solution(object):
    def isAnagram(self, s, t):
        hashmap={}
        if len(s)!=len(t):
           return False
        for i in s:
            hashmap[i] =hashmap.get(i,0)+1
        for i in t:
            if i in hashmap:
               hashmap[i] -= 1
               if hashmap[i] == 0:
                  del hashmap[i]
            else:
                return False
        return True
      
        
        