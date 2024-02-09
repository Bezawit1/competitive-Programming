def isSubset( a1, a2, n, m):
        dic1 = {}
        dic2 = {}
        
        
        for i in a1:
            dic1[i] = dic1.get(i, 0) + 1
        
       
        for i in a2:
            dic2[i] = dic2.get(i, 0) + 1
        
       
        for i in dic2:
            if dic1.get(i, 0) < dic2[i]:
                return "No"
        
        return "Yes"
