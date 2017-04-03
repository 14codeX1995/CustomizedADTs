from queue import queueADT

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,data=None):
        self.root=BinaryTreeNode(data)

    def insertUsingLevelOrder(root, data):

