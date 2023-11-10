class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        
        def helper(num):
            if '0' in str(num):
                return False

            for digit in str(num):
                if num % int(digit) != 0:
                    return False

            return True

        for i in range(left, right + 1):
            if helper(i):
                res.append(i)

        return res
