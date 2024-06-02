class Solution(object):
    def twoCitySchedCost(self, costs):
       
        total_sum_A = sum(i for i,j in costs)
        sorted_difference = sorted(j-i for i , j in costs )
        return total_sum_A + sum(sorted_difference[:(len(costs)//2)])
