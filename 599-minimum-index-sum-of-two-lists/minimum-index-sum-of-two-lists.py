class Solution(object):
    def findRestaurant(self, list1, list2):
        min_index = float('inf')
        res =[]
        for i  in range (len(list1)):
            for j in range(len(list2)):
               if list1[i] == list2[j]: 
                if  i + j < min_index:
                 
                    min_index = i + j
                    if res:
                       res.pop()
                       res.append(list2[j])
                       break
                if i + j == min_index:
                    res.append(list2[j])
                  

              
        return res
      
        