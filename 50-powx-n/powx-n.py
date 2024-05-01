class Solution(object):
    def myPow(self, x, n):
        if x == 1 or n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 1:
            return x
        if n % 2 == 0:
            product = self.myPow(x, n//2)
            return product * product
        else:
            product = self.myPow(x, (n-1)//2)
            return product * product * x
        