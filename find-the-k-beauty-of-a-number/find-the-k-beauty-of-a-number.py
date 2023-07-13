class Solution(object):
    def divisorSubstrings(self, num, k):
        num_str = str(num)
        count = 0

        for i in range(len(num_str) - k + 1):
            substring = int(num_str[i:i+k])
            if substring==0:continue
            if num % substring == 0:
                count += 1

        return count

        