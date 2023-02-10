class Node:
    def __init__(self, val = None):    
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        

    def get(self, index: int) -> int:
        count = 0
        cur = self.dummy.next
        while count < index and cur.next:
            count += 1
            cur = cur.next

        if not cur or count < index:
            return -1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = newNode
       

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        i = 0
        cur = self.dummy
        while cur.next and i < index:
            cur = cur.next
            i += 1
        
        if i == index:
            newNode.next = cur.next
            cur.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        i = 0
        cur = self.dummy
        while cur and i < index:
            cur = cur.next
            i += 1
        
        if i == index and cur and cur.next:
            cur.next = cur.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)