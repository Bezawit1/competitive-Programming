class Solution(object):
    def maxTurbulenceSize(self, arr):
        
        maximum_length = -float('inf')
        left, right = 0, 0
        prev, prev_diff = None, None

        while right < len(arr):
            current = arr[right]
            right += 1

            window_size = right - left

            if window_size == 1:
                prev, prev_diff = current, None
            elif window_size == 2:
                if current == prev:
                    left = right - 1
                    prev_diff = None
                else:
                    prev_diff = current - prev
                prev = current
            else:
                if current == prev:
                    left = right - 1
                    prev, prev_diff = current, None
                elif prev_diff * (current - prev) >= 0:
                    left = right - 2
                    prev, prev_diff = current, current - prev
                else:
                    prev, prev_diff = current, current - prev
            
            maximum_length = max(maximum_length, right - left)
        
        return maximum_length
