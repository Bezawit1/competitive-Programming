class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        res = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(i)
            else:
                hashmap[sorted_str]=[i]
        print(hashmap)
        return list(hashmap.values())
      