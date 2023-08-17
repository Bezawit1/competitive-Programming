class Solution(object):
    def isSubsequence(self, s, t):
        s_idx = 0
        t_idx = 0
        ls=len(s)
        lt=len(t)
        while s_idx < ls and t_idx < lt:
            if s[s_idx] == t[t_idx]:
                s_idx+=1
            t_idx+=1
        return s_idx == ls
            
       