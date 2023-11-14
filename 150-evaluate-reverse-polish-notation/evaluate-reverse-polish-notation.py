class Solution(object):
    def evalRPN(self, tokens):
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(float(a) / b)
        }

        stack = []

        for i in tokens:
            if i in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[i](a, b))
            else:
                stack.append(int(i))

        return stack[0]

