class Solution(object):
    def backspaceCompare(self, s, t):
        stack_s = []
        stack_t= []
        for i in s:
            if i == "#" :
                if len(stack_s) > 0:
                   stack_s.pop()
                continue
            else:
                stack_s.append(i)
        for  i in t :
            if i == "#":
                if len(stack_t) > 0:
                    stack_t.pop()
                continue
            else:
                stack_t.append(i)
        return ''.join(stack_s) == ''.join(stack_t)

            

            
       
        