class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            bracket = s[i]
            
            if bracket == '(':
                stack.append(')')
            elif bracket == '[':
                stack.append(']')
            elif bracket == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != bracket:
                    return False

        return not stack
             
                
        
        
        