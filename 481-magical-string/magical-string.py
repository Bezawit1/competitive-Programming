class Solution(object):
    def magicalString(self, n):
        s = ["1","2" ,"2"]
        for i in range(2, n):
            if s[-1] == "2":
                s.extend(["1"]*int(s[i]))
            else:
                s.extend(["2"]*int(s[i]))
            if len(s) > n:
                break
        
        return s[:n].count("1")
       
    
       
        