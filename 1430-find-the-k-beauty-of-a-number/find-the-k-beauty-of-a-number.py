class Solution(object):
    def divisorSubstrings(self, num, k):
        string_num = str(num)
        
        count = 0
        for i in range(len(string_num) - k + 1):
            left = i
            right = i + k - 1
            
            if int(string_num[left:right+1])!=0:
               if num % int(string_num[left : right + 1]) == 0 :
                   count+=1
        return count


       
        