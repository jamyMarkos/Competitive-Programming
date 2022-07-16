class MyCircularDeque:
    
    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.size = k
        self.ddeque = [None] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.ddeque[self.front] = value
        return True
                    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.ddeque[self.rear] = value
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
        return True
                
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.ddeque[self.front]
        
    def getRear(self) -> int:
        if self.isEmpty() or self.rear < 0:
            return -1
        return self.ddeque[self.rear]
        
    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
         return (((self.front == 0) and (self.rear == self.size-1)) or (self.front == (self.rear + 1)))
       
        


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