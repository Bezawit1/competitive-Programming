class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ''
        for i in s:
            new_s +=i.lower()
        return new_s
        