class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def postOrder(root):
    if (root != None):
        print(root.data, end = " ")
        postOrder(root.right)
        postOrder(root.left)

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(5)
root.right.right = Node(8)
postOrder(root)