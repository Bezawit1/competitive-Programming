#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        if len(A) != len(B):
               return False
    
   
        hashA = {}
        hashB = {}
          
        for i in A:
           hashA[i] = hashA.get(i, 0) + 1
            
            
        for i in B:
            hashB[i] = hashB.get(i, 0) + 1
            
            
        return hashA == hashB
        
        #return: True or False
        
        #code here
