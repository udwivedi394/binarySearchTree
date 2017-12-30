import binarySearchTree as binClass

#Main driver program
binST = binClass.BST()
binST.addNode(8)
binST.addNode(3)
binST.addNode(1)
binST.addNode(6)
binST.addNode(4)
binST.addNode(7)
binST.addNode(15)
binST.addNode(10)
binST.addNode(9)
binST.addNode(17)
binST.addNode(16)

binST.inOrder()
binST.levelOrder()
binST.deleteNode(15)
binST.inOrder()
binST.levelOrder()
