class MinStack:

    def __init__(self):
        self.stack = []
        self.top_ = -1
        self.min_ = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_ += 1
        
        # if not self.stack or val < self.min_:
            
        

    def pop(self) -> None:
        self.stack.pop(self.top_)
        self.top_ -= 1
        

    def top(self) -> int:
        return self.stack[self.top_]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()