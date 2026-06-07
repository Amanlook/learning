

class TreeNode:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None


newBT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.left = leftchild
newBT.right = rightChild

def preOrderTraversal(rootNode: TreeNode):
    if not rootNode:
        return 
    
    print(rootNode.data)

    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

preOrderTraversal(newBT)