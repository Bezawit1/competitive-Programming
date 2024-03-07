class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums)
        i = 0
        j = len(nums)-1
        def reverseList(i , j):
            while i < j :
                nums[i] , nums[j] = nums[j] , nums[i]
                i+=1
                j-=1
        reverseList(i, j)
        reverseList(0 , k-1)
        reverseList(k,j)


        

            
            
           
           

        

        
        