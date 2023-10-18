class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        results=[]
        for i in range(n-3):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j]==nums[j-1]:
                   continue
                k=j+1
                l=n-1
                while k<l:
                    curr_sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if curr_sum ==target:
                        results.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        k+=1
                        l-=1
                    elif curr_sum>target:
                        l-=1
                    else:
                        k+=1
        return results
        

        