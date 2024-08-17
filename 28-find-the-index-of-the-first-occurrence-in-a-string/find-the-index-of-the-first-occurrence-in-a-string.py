class Solution(object):
    def strStr(self, haystack, needle):
        i=0
        j=0
        m=len(haystack)
        n=len(needle)

        while i<m:
            if(haystack[i]==needle[j]):
                if j==n-1:
                    return i-j
                i+=1
                j+=1
            else:
                i=i-j+1
                j=0
        return -1



        
            
        
       
       