class Solution(object):
    def largestAltitude(self, gain):
        prefix_sum = [0]*len(gain)
        maxAltitude=0
        for i in range(len(gain)):
            prefix_sum.append(prefix_sum[-1]+gain[i])
            maxAltitude=max(prefix_sum[-1],maxAltitude)
        
        return maxAltitude
       