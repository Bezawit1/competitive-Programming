class Solution(object):
   def judgeSquareSum(self , c):
        i, j = 0, int(c ** 0.5)  
        while i <= j:
            current_sum = i * i + j * j
            if current_sum == c:
                return True
            elif current_sum < c:
                i += 1
            else:
                j -= 1
        return False



                
            