class Solution(object):
    def isAdditiveNumber(self, num):
        def is_valid_number(num_str):
            return len(num_str) == 1 or num_str[0] != '0'
        
        def backtrack(idx, num1, num2):
            if idx == len(num):
                return True
            
            for i in range(idx, len(num)):
                if i > idx and num[idx] == "0":
                    continue 
                
                currNumber = num[idx:i+1]
                if num1 is None or num2 is None:
                    if backtrack(i + 1, currNumber, num2):
                        return True
                else:
                    if int(num1) + int(num2) == int(currNumber) and backtrack(i + 1, num2, currNumber):
                        return True
                    if int(currNumber) > int(num1) + int(num2):
                        break
            return False
        
        if len(num) < 3:
            return False
        
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                num1 = num[:i]
                num2 = num[i:j]
                
                if not is_valid_number(num1) or not is_valid_number(num2):
                    continue
                
                if backtrack(j, num1, num2):
                    return True
        
        return False
        