class Solution(object):
    def is_palindrome(self, s):
        return s == s[::-1]

    def checkPalindromeFormation(self, a, b):
        def palindrome(s1, s2):
            i, j = 0, len(s2) - 1
            while i < j:
                if s1[i] != s2[j]:
                    break
                i += 1
                j -= 1
            return self.is_palindrome(s1[i:j+1]) or self.is_palindrome(s2[i:j+1])

        return palindrome(a, b) or palindrome(b, a)
