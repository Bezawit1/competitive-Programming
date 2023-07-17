class Solution(object):
    def findAnagrams(self, s, p):
        #if length of p is greater than s return empty list
        if len(p)>len(s):
            return []
        
        result=[]
        window_size=len(p)
        hashmap_p={}
        hashmap_s={}

        #initialize hash map p and frequency
        for char in p:
            hashmap_p[char]=hashmap_p.get(char,0)+1
        #initialize the window
        for i in range(window_size):
            char=s[i]
            hashmap_s[char]=hashmap_s.get(char,0)+1
        #update the window
        for i in range(len(s) - window_size + 1):
            #check if both hashmaps are equal if equal append the index i 
            if hashmap_p == hashmap_s:
                result.append(i)
            #after checking there are valid elements left we assign the left and rightmost index
            #so that we can track which element leaves the window and 
            #which will enter

            if i + window_size < len(s):
                left_char=s[i]
                right_char=s[ i + window_size]
                
                hashmap_s[left_char]-=1
                #if the element frequency reaches 0 then its no longer necessary
                if hashmap_s[left_char] == 0:
                    del hashmap_s[left_char]
                #update the right char since the window is moving 
                #the right direction
                hashmap_s[right_char]=hashmap_s.get(right_char,0)+1
       
        return result
















            
        