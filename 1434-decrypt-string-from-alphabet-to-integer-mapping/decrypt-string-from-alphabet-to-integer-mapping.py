class Solution(object):
    def freqAlphabets(self, s):
           
        hashmap = {
            '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
            '6': 'f', '7': 'g', '8': 'h', '9': 'i',
            '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm',
            '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q',
            '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
            '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'
        }

        res = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                
                char = hashmap[s[i - 2:i + 1]]
                i -= 3  
            else:
                
                char = hashmap[s[i]]
                i -= 1
            res.append(char)

        
        return ''.join(reversed(res))


       
        