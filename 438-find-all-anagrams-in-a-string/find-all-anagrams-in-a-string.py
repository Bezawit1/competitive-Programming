class Solution(object):
    def findAnagrams(self, s, p):
        target = {}
        hash_s = {}
        res = []
        window_size = len(p)
        if len(p) > len(s):
            return []
        for i in p:
            target[i] = target.get(i,0)+1
        for i in range(window_size):
            char = s[i]
            hash_s[char] = hash_s.get(char, 0) + 1
        for i in range(len(s)-window_size + 1):
            if hash_s == target:
                res.append(i)
            
            if i + window_size < len(s):
                char = s[i]
                right = s[i+window_size]
                hash_s[char]-=1
                if hash_s[char] == 0:
                    del hash_s[char]
                hash_s[right] = hash_s.get(right,0) +1
        return res

            
       
        