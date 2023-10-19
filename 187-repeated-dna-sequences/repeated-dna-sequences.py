class Solution(object):
    def findRepeatedDnaSequences(self, s):
        hashmap = {}
        if len(s) < 11:
            return []
        arr = []
        for i in range(len(s) - 9):
            left = i
            right = i + 10
            if s[left:right] in hashmap:
                arr.append(s[left:right])
            hashmap[s[left:right]] = s[left:right]

        res = set(arr)
        return list(res)
        

        
        