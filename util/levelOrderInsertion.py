
from tree.binaryTree import BinaryTree


def insertUsingLevelOrder(root,data,treeType):
    if treeType=="binaryTree":
        newNode=BinaryTree(data)
