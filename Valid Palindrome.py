class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced = re.sub(r'[^a-zA-Z0-9]+', '', s)
        result = ''
        for i in range(len(replaced)):
            result+=replaced[i].lower()
        return result==result[::-1]
