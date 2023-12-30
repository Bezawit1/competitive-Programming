class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range (left , right+ 1):
            isDivisible = True
            n = i
            while n!=0:
                digit = n%10
                if digit == 0:
                    isDivisible = False
                    break
                if i%digit!=0:
                    isDivisible = False
                    break 
                n//=10
              
            if(isDivisible):
                res.append(i)
                print(i)
        return res

        
