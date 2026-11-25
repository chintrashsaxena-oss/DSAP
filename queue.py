class queue:
    def __init__(self):
        self.items = []
#condition to check if the queue is empty
    def IsEmpty(self):
        return self.items == []
#insert an item into the queue
    def insert(self,value):
        self.items.append(value)
#delete an item from the queue
    def delete(self):
        if self.IsEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)
#call the queue class and test the methods
q = queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()