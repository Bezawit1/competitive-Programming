class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash_map_word1 = {}
        hash_map_word2 = {}

        for i in range(len(word1)):
            hash_map_word1[word1[i]] = hash_map_word1.get(word1[i] , 0) + 1
   
        for i in range(len(word2)):
            if word2[i] not in hash_map_word1:
                return False
            hash_map_word2[word2[i]] = hash_map_word2.get(word2[i] , 0) + 1
        return sorted(hash_map_word1.values()) == sorted(hash_map_word2.values())
        
         
        
        