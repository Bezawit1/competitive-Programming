class Solution:
    def splitString(self, s: str) -> bool:
        split = []
        def backTracking(start):
            if start >= len(s):
                return len(split) >= 2
            for end in range(start, len(s)):
                curr = int(s[start:end+1])
                if not split or split[-1] - curr == 1:
                    split.append(curr)
                    if backTracking(end + 1):
                        return True
                    split.pop()
                
            return False
        return backTracking(0)
