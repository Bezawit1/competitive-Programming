class Solution(object):
    def smallestNumber(self, num):
        res = []
        ans = []
        org =num
        if num > 0:
           while num > 0:
               digit = num%10
               num//=10
               res.append(digit)
        res.sort()
        print(res)
        for i in range(len(res)):
            if i == 0 and res[i] ==0:
                for j in range(i+1 , len(res)):
                    if res[j] !=0:
                        res[i],res[j]= res[j],0
                        break

                    
        
        print(res)
       
        if num < 0:
            num=num* -1
            print(num)
            while num > 0:
               digit = num%10
               num//=10
               ans.append(digit)
        ans.sort(reverse=True)
        if res == [] and ans == []:
            return 0
        
        return -1*int("".join(map(str,ans))) if org< 0 else int("".join(map(str,res)))
        
            

           
        