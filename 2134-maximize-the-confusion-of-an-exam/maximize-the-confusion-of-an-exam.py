class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
            sequence = answerKey
            length = len(sequence)
            true_count, false_count = 0, 0 
            max_consecutive_length = 0
            left = 0

            for right in range(length):
                if sequence[right] == 'T':
                    true_count += 1
                else:
                    false_count += 1

                while true_count > k and false_count > k:
                    if sequence[left] == 'T':
                        true_count -= 1
                    else:
                        false_count -= 1
                    left += 1

                max_consecutive_length = max(max_consecutive_length, right - left + 1)

            return max_consecutive_length

       
        