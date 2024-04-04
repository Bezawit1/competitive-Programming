class Solution(object):
    def vowelStrings(self, words, queries):
        count = 0
        prefix_sum = []
        hash_map={
            'a':1,
            'e':1,
            'i':1,
            'o':1,
            'u':1}
        for i in range(len(words)):
            if words[i][0] in hash_map and words[i][-1] in hash_map:
                prefix_sum.append(1)
            else:
                prefix_sum.append(0)
        res = []
        curr_sum = 0
        answer = []
        for i in prefix_sum:
            curr_sum+=i
            res.append(curr_sum)
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]
            
            if left ==0:
                answer.append(res[right] - 0)
            else:
                answer.append(res[right] - res[left-1])
        return answer
        
        
        

       
        