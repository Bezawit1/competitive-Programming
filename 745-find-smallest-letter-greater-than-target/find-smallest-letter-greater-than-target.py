class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 2
        answer = ''
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        while left <= right:
            mid = (left + right)//2
            if letters[mid] > target:
                right = mid - 1
                answer = letters[mid]

            if letters[mid] <= target:
               
                answer = letters[mid+1]
                left = mid + 1
                
            
        return answer
        