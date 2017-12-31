import binarySearchTree as binClass
import searchPairwithSum as sPair
import merge2BST as mrgBST
import inOrderSuccessor as inOrdSuc

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
#binST.deleteNode(15)
binST.inOrder()
binST.levelOrder()

#sPair.findSumPair01(binST.getRoot(),33)
sPair.findSumPair03(binST.getRoot(),33)
print
#sPair.findSumPair02(binST.getRoot(),33)

bst1 = binClass.BST()
"""
for i in range(21,10,-2):
	bst1.addNode(i)
print "First BST:",bst1.inOrder()
"""
bst1.addNode(3)
bst1.addNode(1)
bst1.addNode(5)

bst2 = binClass.BST()
"""
for i in range(30,40,2):
	bst2.addNode(i)
print "Second BST:",bst2.inOrder()
"""
bst2.addNode(4)
bst2.addNode(2)
bst2.addNode(6)
mrgBST.merge2BST(bst1.getRoot(),bst2.getRoot())

print "\nNew Search:"
binST.searchKthNode(0)

print "\nSuccessor:",binST.inOrderSuccessor(17)
