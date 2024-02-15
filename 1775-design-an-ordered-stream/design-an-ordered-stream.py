class OrderedStream(object):

    def __init__(self, n):
        self.stream = [''] * (n + 1)
        self.id= 0
        

    def insert(self, idKey, value):
        self.stream[idKey - 1] = value
        res = []

        while self.stream[self.id]:
            res.append(self.stream[self.id])
            self.id += 1
        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)