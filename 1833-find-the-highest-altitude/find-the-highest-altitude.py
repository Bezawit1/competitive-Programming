class Solution(object):
    def largestAltitude(self, gain):
        prefix_sum = [0]*len(gain)
        for i in range(len(gain)):
            prefix_sum.append(prefix_sum[-1]+gain[i])
        maxAltitude=max(prefix_sum)
        return maxAltitude
       