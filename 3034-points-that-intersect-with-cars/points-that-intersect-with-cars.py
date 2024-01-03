class Solution(object):
    def numberOfPoints(self, nums):
        intervals = []
        for start, end in sorted(nums):
            if not intervals or start > intervals[-1][1]:
                intervals.append([start, end])
            else:
                intervals[-1][1] = max(intervals[-1][1], end)

        total_length = sum(end - start + 1 for start, end in intervals)

    
        return total_length
                
        

       

      
      

        