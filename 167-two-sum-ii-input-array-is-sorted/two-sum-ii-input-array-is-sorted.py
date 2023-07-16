class Solution(object):
    def twoSum(self, numbers, target):
        rightIndex=0
        leftIndex=len(numbers)-1
        res=[]
        while rightIndex<leftIndex:
            sum=numbers[rightIndex]+numbers[leftIndex]
            if sum<target:
                rightIndex+=1
            elif sum>target:
                leftIndex-=1
            elif sum==target:
                res.append(rightIndex+1)
                res.append(leftIndex+1)
                
                break
        return res
      

       