class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1

        if len(arr) < 3:
            return 0

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                left = mid + 1
            else:
                right = mid

        return -1







            

        