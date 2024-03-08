class Solution(object):
    def compress(self, chars):
        counter = 1
        res = []
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                    counter +=1
            else:
                res.append(chars[i])
                if counter >1:
                    res.extend(list(str(counter))) 
                counter = 1
        res.append(chars[-1]) 
        if counter >1:
            res.extend(list(str(counter)))  
        chars[:] = []
        chars.extend(res)
      
        return len(chars)
           
                

        

       

        