class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.tokens = {}
        self.timeToLive = timeToLive
        
        

    def generate(self, tokenId, currentTime):
        self.tokens[tokenId] = currentTime
        
        

    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens and self.tokens[tokenId]>currentTime - self.timeToLive:   
            self.tokens[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime):
        expired = currentTime - self.timeToLive
        count = 0
        for val in self.tokens.values():
            if val > expired:
                count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)