class Solution(object):
    def isPalindrome(self, s):
        #remove alpha numeric values
        replaced = re.sub(r'[^a-zA-Z0-9]+', '', s)
        newStr = ''
        for i in replaced:
           newStr+=i.lower()
        return newStr == newStr[::-1]
      
        
        