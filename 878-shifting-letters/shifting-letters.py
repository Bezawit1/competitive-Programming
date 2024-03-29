class Solution(object):
    def shiftingLetters(self, s, shifts):
        curr_sum = 0
        res = [val for val in shifts]
        for i in range(len(s)-1, -1, -1):
            curr_sum = (curr_sum + shifts[i]) % 26
            res[i] = chr(97 + (ord(s[i])-97 + curr_sum)%26)
        return "".join(res)



       
        