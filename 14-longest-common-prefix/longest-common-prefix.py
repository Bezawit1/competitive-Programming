class Solution(object):
    def longestCommonPrefix(self, strs):
            strs.sort()
            res = ""
            j = len(strs) - 1
            for i in range(len(strs[0])):
                if strs[0][i] == strs[j][i]:
                    res += strs[0][i]
                else:
                    break
            return res
        