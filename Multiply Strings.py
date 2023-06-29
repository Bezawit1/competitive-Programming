class Solution(object):
    def multiply(self, num1, num2):
    
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                carry = product // 10
                digit = product % 10
                result[i + j + 1] += digit
                result[i + j] += carry
                if result[i + j + 1] >= 10:
                    carry = result[i + j + 1] // 10
                    result[i + j + 1] %= 10
                    result[i + j] += carry
        
        
        while result[0] == 0:
            result.pop(0)
        
        return ''.join(map(str, result))
