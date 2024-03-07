class Solution(object):
    def judgeSquareSum(self, c):
            i , j = 0 , int(sqrt(c))
          
            while i <=j :
                product = i*i + j*j
                if product == c:
                    return True
                elif product < c:
                    i+=1
                else:
                    j-=1
            return False
            

        