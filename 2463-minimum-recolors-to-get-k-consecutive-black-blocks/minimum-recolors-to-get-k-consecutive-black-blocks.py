class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_ops = len(blocks)
        count = 0
        for i in range(len(blocks) - k + 1):
            left = i
            right = i + k - 1
            for num in blocks[left : right + 1]:
                if num == 'W':
                    count+=1
            min_ops = min(min_ops , count)
            count = 0
        return  min_ops


            
        
        