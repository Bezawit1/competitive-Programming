class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        hashmap_p = {}
        hashmap_s = {}
        window_size = len(p)
        if len(p) > len(s):
           return [] 

        for char in p:
            hashmap_p[char] = hashmap_p.get(char, 0) + 1

        for i in range(window_size):
            char = s[i]
            hashmap_s[char] = hashmap_s.get(char, 0) + 1

        for i in range(len(s) - window_size + 1 ):
            if hashmap_p == hashmap_s:
                result.append(i)

            if i + window_size < len(s):
                left_char = s[i]
                right_char = s[i + window_size]

                hashmap_s[left_char] -= 1
                if hashmap_s[left_char] == 0:
                    del hashmap_s[left_char]

                hashmap_s[right_char] = hashmap_s.get(right_char, 0) + 1

        return result














            
        