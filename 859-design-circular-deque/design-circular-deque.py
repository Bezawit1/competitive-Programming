class MyCircularDeque(object):

    def __init__(self, k):
        self.size = k
        self.queue = []
        
        

    def insertFront(self, value):
        if len(self.queue)==self.size:
            return False
        self.queue.insert(0,value)
        return True
        
        

    def insertLast(self, value):
        if self.isFull():
            return False
        self.queue.append(value)
        return True
        

    def deleteFront(self):
        if self.queue:
            self.queue.pop(0)
            return True
        return False
        

    def deleteLast(self):
        if self.queue:
            self.queue.pop(-1)
            return True
        return False
        

    def getFront(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1
        
        

    def getRear(self):
        if self.queue:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        if self.queue:
            return False
        return True
        

    def isFull(self):
        return len(self.queue)==self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()