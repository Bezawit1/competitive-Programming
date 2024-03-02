class Solution(object):
    def intersect(self, nums1, nums2):

        if len(nums1) <= len(nums2):
            shorter_arr = nums1
            longer_arr = nums2
        else:
            shorter_arr = nums2
            longer_arr = nums1

   
        counts = {}
        for num in shorter_arr:
            counts[num] = counts.get(num, 0) + 1

        # Find common elements and count occurrences
        result = []
        for num in longer_arr:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]

        return result

