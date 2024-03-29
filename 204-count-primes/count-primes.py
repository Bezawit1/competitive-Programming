class Solution(object):
    def countPrimes(self, n):
       
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        count = 0

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

       

        for prime in is_prime:
            if prime:
                count += 1
        return count




       
        
        