from c_queue import queueADT

class BinaryTreeNode:
    #defines a node in the tree
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    #Binary Tree is definned with root(BinaryTreeNode type) as the data member
    def __init__(self,data=None):
        if data is None:
            self.root=None
        else:
            self.root=BinaryTreeNode(data)

    #builds a tree in a simple level order fashion
    def insertUsingLevelOrder(self,data):
        newNode=BinaryTreeNode(data)
        if self.root is None:
            self.root=newNode
            return
        #every node is stored in a queue before processing
        que=queueADT.Queue()
        que.enQueue(self.root)
        while(que.size!=0):
            node=que.deQueue()
            if node.left is not None:
                que.enQueue(node.left)
            else:
                node.left=newNode
                return
            if node.right is not None:
                que.enQueue(node.right)
            else:
                node.right=newNode
                return

    #performs a level order print of nodes in a Binary Tree
    def printLevelOrder(self,root=None):
        if root is None:
            return
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

    #performs a preorder traversal on the tree
    def printPreOrder(self,root=None):
        if root is None:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    #performs an inorder traversal on the tree
    def printInOrder(self,root=None):
        if root is None:
            return
        self.printInOrder(root.left)
        print(root.data,end=" ")
        self.printInOrder(root.right)

    #performs a postorder traversal on the tree
    def printPostOrder(self,root=None):
        if root is None:
            return
        self.printPostOrder(root.left)
        self.printPostOrder(root.right)
        print(root.data,end=" ")

    #search an element in the tree(return 1 if found else 0)
    def search(self,root,data):
        if root is None:
            return 0
        if root.data==data:
            return 1
        else:
            temp=self.search(root.left,data)
            if temp==1:
                return 1
            return self.search(root.right,data)


t=BinaryTree()
t.insertUsingLevelOrder(1)
t.insertUsingLevelOrder(2)
t.insertUsingLevelOrder(3)
t.printLevelOrder(t.root)
t.printPreOrder(t.root)
print()
t.printInOrder(t.root)
print()
t.printPostOrder(t.root)
print()
print(t.search(t.root,4))

