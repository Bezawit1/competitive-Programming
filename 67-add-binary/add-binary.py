class Solution(object):
    def addBinary(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        sum_total = num1 + num2

        result = bin(sum_total)[2:]
        return result
        