class Solution(object):
    def uniqueOccurrences(self, arr):
        freq={}
        for i in arr:
            freq[i]= freq.get(i , 0) + 1
        
        for key,val in freq.items():
            for key2,val2 in freq.items():
                if key!=key2 and val==val2:
                    return False
        return True

    