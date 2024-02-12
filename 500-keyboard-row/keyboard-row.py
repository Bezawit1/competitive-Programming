class Solution(object):
    def findWords(self, words):
        key1 = {'q','w','e','r','t','y','u','i','o','p'}
        key2 = {'a','s','d','f','g','h','j','k','l'}
        key3 = {'z','x','c','v','b','n','m'}
        res = []
        for i in words:
            word = set(i.lower())
            if (word <= key1) or (word <= key2) or (word <= key3):
               res.append(i)
        return res

        
        