class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
            
            length = len(answerKey)
            true_count, false_count = 0, 0 
            max_len = 0
            j = 0

            for i in range(length):
                if answerKey[i] == 'T':
                    true_count += 1
                else:
                    false_count += 1

                while true_count > k and false_count > k:
                    if answerKey[j] == 'T':
                        true_count -= 1
                    else:
                        false_count -= 1
                    j += 1

                max_len = max(max_len, i - j + 1)

            return max_len

       
        