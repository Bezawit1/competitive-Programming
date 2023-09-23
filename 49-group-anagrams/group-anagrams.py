class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
    
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        
        return list(hashmap.values())
    #  hashmap={
    #      aet:[eat,tea]
    #  }   
        