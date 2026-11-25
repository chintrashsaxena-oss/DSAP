class deque:
    def __init__(self):
        self.items = []
#condition to check if the queue is empty
    def IsEmpty(self):
        return self.items == []
#insert an item into the queue
    def insertAtEnd(self,value):
        self.items.append(value)
#delete an item from the queue
    def deleteAtFront(self):
        if self.IsEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtEnd(self):
            if self.IsEmpty():
                print("Queue is empty")
            else:
                return self.items.pop()

dq = deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
dq.deleteAtEnd()
dq.deleteAtEnd()