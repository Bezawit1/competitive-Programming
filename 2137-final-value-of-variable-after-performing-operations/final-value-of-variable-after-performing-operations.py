class Solution(object):
    def finalValueAfterOperations(self, operations):
            ops = {
            "--X": lambda x: x - 1,
            "X++": lambda x: x + 1,
            "++X": lambda x: x + 1,
            "X--": lambda x: x - 1
             }
            
            val = 0
            res = []
            for i in operations:
                if i in ops:
                    res.append(ops[i](val))
            return sum(res)