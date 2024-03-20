class Solution(object):
    def totalFruit(self,fruits):
            hash_fruits = {}
            idx = 0 
            max_fruits = 0 
            for i in range(len(fruits)):
                hash_fruits[fruits[i]] = hash_fruits.get(fruits[i] , 0) + 1
                while len(hash_fruits) > 2:
                    hash_fruits[fruits[idx]] -=1
                    if hash_fruits[fruits[idx]] == 0:
                        del hash_fruits[fruits[idx]]
                    idx+=1
                max_fruits = max(max_fruits , i - idx + 1)
            return max_fruits
                


        