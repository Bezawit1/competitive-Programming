class Solution(object):
    def subsets(self, nums):
        def backT (start_idx, candidates):
       
            answer.append(candidates[:])
            
            
            for i in range(start_idx, len(nums)):
                candidates.append(nums[i])
               
                backT(i + 1, candidates)
               
                candidates.pop()
            
        answer = []
        backT(0, [])
        return answer

        