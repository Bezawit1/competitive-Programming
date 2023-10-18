class Solution(object):
    def compress(self, chars):
       
        if len(chars) <= 1:
            return len(chars)
        
        result = []
        count = 1
        
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                result.append(chars[i])
                if count > 1:
                    result.extend(list(str(count)))
                count = 1
        
        result.append(chars[-1])
        if count > 1:
            result.extend(list(str(count)))
        
        chars[:] = [] 
        chars.extend(result)
        
        return len(chars)

        