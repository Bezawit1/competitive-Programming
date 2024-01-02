class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for i in nums1:
            idx  = nums2.index(i)
            found = False
            for j in range(idx , len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    found = True
                    break
            if(not found):
                res.append(-1)
        return res
           

      