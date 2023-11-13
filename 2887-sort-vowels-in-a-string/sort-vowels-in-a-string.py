class Solution(object):
    def sortVowels(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = []

        for i in range(len(s)):
            if s[i].lower() in vowels:
                res.append(s[i])

        res.sort()
        k = 0
        s_list = list(s)

        for i in range(len(s)):
            if s[i].lower() in vowels:
                s_list[i] = res[k]
                k += 1

        return ''.join(s_list)


        
      

