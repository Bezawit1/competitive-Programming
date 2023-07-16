class Solution(object):
    def frequencySort(self, s):
        hashMap={}
        for char in s:
            if char in hashMap:
                hashMap[char]+=1
            else:
                hashMap[char]=1
        sorted_chars = sorted(hashMap.keys(), key=lambda x: hashMap[x], reverse=True)
        sorted_string = ''.join(char * hashMap[char] for char in sorted_chars)
        return sorted_string

        