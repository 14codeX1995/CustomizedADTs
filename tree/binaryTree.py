from c_queue import queueADT

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,data=None):
        if data is None:
            self.root=None
        else:
            self.root=BinaryTreeNode(data)

    def insertUsingLevelOrder(self,root, data):
        newNode=BinaryTreeNode(data)
        print("newNode-> ",newNode.data)
        if root is None:
            root=newNode
            return root
        que=queueADT.Queue()
        que.enQueue(root)
        while(que.size!=0):
            node=que.deQueue()
            if node.left is not None:
                que.enQueue(node.left)
            else:
                node.left=newNode
                return root
            if node.right is not None:
                que.enQueue(node.right)
            else:
                node.right=newNode
                return root

    def printLevelOrder(self,root=None):
        if root is None:
            print("Tree empty!")
        que=queueADT.Queue()
        que.enQueue(root)
        while(que.size!=0):
            node=que.deQueue()
            print(node.data,end=" ")
            if node.left is not None:
                que.enQueue(node.left)
            if node.right is not None:
                que.enQueue(node.right)
        print()
