class Solution(object):
    def largestOddNumber(self, num):
        new_num  = int(num)
        while new_num:
            if new_num%2 == 1:
                return str(new_num)
            else:
               new_num//=10
        return ""
        