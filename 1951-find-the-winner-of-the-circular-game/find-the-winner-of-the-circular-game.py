class Solution(object):
    def findTheWinner(self, n, k):
            friends = deque(range(1,n + 1))
            while len(friends) > 1:
                for _ in range(k):
                    
                    friends.append(friends.popleft())
                friends.pop()
        
            return friends[0]


    
    
    


        