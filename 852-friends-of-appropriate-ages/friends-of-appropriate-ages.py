

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = Counter(ages)  
        requests = 0
      
        for ageA in age_count:
            countA = age_count[ageA]
            
            for ageB in age_count:
                if ageB <= 0.5 * ageA + 7: 
                    continue
                if ageB > ageA:   
                    continue
                
                requests += countA * age_count[ageB]  
                if ageA == ageB:
                    requests -= countA  # Remove self-requests

        return requests
