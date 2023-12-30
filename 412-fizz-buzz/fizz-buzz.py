class Solution(object):
    def fizzBuzz(self, n):
        newA = []
        for i in range (1,n+1):
            if i%3 == 0 and i%5 ==0:
                newA.append("FizzBuzz")
            elif i%5 == 0:
               newA.append ("Buzz")
            elif i%3 == 0:
               newA.append("Fizz")
            else:
                newA.append(str(i))
        return newA


        
        