
from queues.queueLinkedList import QueueLinkedList as queue

class TreeNode:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None


newBT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightChild = TreeNode("Cold")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

newBT.left = leftchild
newBT.right = rightChild

leftchild.left = tea
leftchild.right = coffee

# ---------------- DFS

def preOrderTraversal(rootNode: TreeNode):
    if not rootNode:
        return 
    
    print(rootNode.data)

    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

# preOrderTraversal(newBT)

def inOrderTraversal(rootNode: TreeNode):
    if not rootNode:
        return 
    
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

# inOrderTraversal(newBT)

def postOderTraversal(rootNode: TreeNode):

    if not rootNode:
        return 
    
    postOderTraversal(rootNode.left)
    postOderTraversal(rootNode.right)
    print(rootNode.data)

# postOderTraversal(newBT)

# ---------------- BFS

def levelOrderTraversal(rootNode: TreeNode):

    if not rootNode:
        return
    
    custom_queue = queue()
    custom_queue.enqueue(rootNode)
    while not(custom_queue.isempty()):
        root = custom_queue.dequeue()
        print(root.value.data)

        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)

        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)

# levelOrderTraversal(newBT)

def searchBT(rootNode: TreeNode, value):
    # Using level Order Traversal
    if not rootNode:
        return "The BT does not exist"
     
    custom_queue = queue()
    custom_queue.enqueue(rootNode)
    while not(custom_queue.isempty()):
        root = custom_queue.dequeue()
        
        if root.value.data == value:
            return True

        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)

        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)
    
    return False


# print(searchBT(newBT, "Tea"))

 