class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
            answer_sequence = answerKey
            length = len(answer_sequence)
            true_count, false_count = 0, 0 
            max_consecutive_length = 0
            left = 0

            for right_pointer in range(length):
                if answer_sequence[right_pointer] == 'T':
                    true_count += 1
                else:
                    false_count += 1

                while true_count > k and false_count > k:
                    if answer_sequence[left] == 'T':
                        true_count -= 1
                    else:
                        false_count -= 1
                    left += 1

                max_consecutive_length = max(max_consecutive_length, right_pointer - left + 1)

            return max_consecutive_length

       
        