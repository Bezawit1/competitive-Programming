class Solution(object):
    def calPoints(self ,operations):
        stack = []

        for i in operations:
            if i == "+":
                if len(stack) >= 2:
                    a = stack[-1]
                    b = stack[-2]
                    stack.append(a + b)
            elif i == "D":
                if stack:
                    stack.append(2 * stack[-1])
            elif i == "C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(i))

        return sum(stack)

       
        