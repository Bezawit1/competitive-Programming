class Solution(object):
    def totalFruit(self,fruits):
            hash_fruits = {}
            start_index = 0 
            maxDis =0 
            for i in range(len(fruits)):
                hash_fruits[fruits[i]] = hash_fruits.get(fruits[i] , 0) + 1
                while len(hash_fruits) > 2:
                    hash_fruits[fruits[start_index]] -=1
                    if hash_fruits[fruits[start_index]] == 0:
                        del hash_fruits[fruits[start_index]]
                    start_index+=1
                maxDis = max(maxDis , i - start_index + 1)
            return maxDis
                


        