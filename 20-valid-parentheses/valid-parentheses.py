class Solution(object):
    def isValid(self, s):
        stack = []

        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (bracket == ')' and top != '(') or (bracket == ']' and top != '[') or (bracket == '}' and top != '{'):
                    return False

        return not stack
        