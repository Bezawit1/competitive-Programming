class MyQueue(object):

    def __init__(self):
        self.myQueue=[]

    def push(self, x):
        self.myQueue.append(x)

    def pop(self):
        if len(self.myQueue):
        
            return self.myQueue.pop(0)
     
        return False
        
    def peek(self):
        if len(self.myQueue):
            return self.myQueue[0]
     
        

    def empty(self):
        return not len(self.myQueue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()