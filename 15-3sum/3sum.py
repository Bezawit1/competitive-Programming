class Solution(object):
    def threeSum(self, nums):
            nums.sort()
            n = len(nums)
            res = []
        
            for i in range(n  - 2):
                if i > 0 and nums[i] == nums [i -1]:
                    continue
                j = i+1
                k = n -1 
                while j < k:
                    curr_sum = nums[i] + nums[j] + nums [k]
                    if curr_sum == 0:
                        res.append([nums[i], nums[j] , nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j+=1
                        k-=1
                  
                    elif curr_sum  < 0 :
                        j+=1
                    else:
                        k-=1

            return res

            

        


       
        