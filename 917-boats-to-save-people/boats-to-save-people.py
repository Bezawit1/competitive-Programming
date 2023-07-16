class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count_boats=0
        i=0
        j=len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                count_boats+=1
                i+=1
                j-=1
            else:
                count_boats+=1
                j-=1
                
        return count_boats
            
            
             

        

       