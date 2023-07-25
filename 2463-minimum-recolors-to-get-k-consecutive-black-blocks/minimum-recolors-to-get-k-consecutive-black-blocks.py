class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_ops = float('inf')
        window_size = len(blocks) - k
        

        for i in range(window_size + 1):
            left = i
            right = i + k -1
            subarray = blocks[left:right + 1]
            count = subarray.count('W')
            min_ops = min(min_ops, count)
        return min_ops
            
            
        