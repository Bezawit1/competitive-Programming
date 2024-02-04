class Solution(object):
    def lengthOfLastWord(self, s):
        stringArray = list(reversed(s.split(' ')))
        print(stringArray)
        for i in range(len(stringArray)):
            if stringArray[i]!="":
                return len(stringArray[i])
                break
        return 0
            
        
