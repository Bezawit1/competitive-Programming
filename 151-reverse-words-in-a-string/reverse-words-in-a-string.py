class Solution(object):
    def reverseWords(self, s):
        replaced = s.strip()
        split = replaced.split()
        split.reverse()  
        reversed_str = " ".join(split)
        return reversed_str
        