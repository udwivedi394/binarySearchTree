class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def addNode(self,data):
		if self.root == None:
			self.root = Node(data)
			return
		
		temp = self.root
		while temp:
			prevNode = temp
			if data < temp.data:
				temp = temp.left
			elif data >= temp.data:
				temp = temp.right

		if data < prevNode.data:
			prevNode.left = Node(data)
		else:
			prevNode.right = Node(data)
		return

	def inOrder(self):
		if self.root == None:
			print "Nothing to print"
			return
		print "\nIn Order:",
		stack = []
		temp = self.root

		while 1:
			while temp:
				stack.append(temp)
				temp = temp.left

			while temp == None and len(stack):
				temp = stack.pop()
				print temp.data,
				temp = temp.right

			if temp == None and len(stack)==0:
				break
		return

	def levelOrder(self):
		if self.root == None:
			print "No Tree"
			return
		print "\nLevel Order:"
		queue = []
		temp = self.root
		queue.append(temp)
		
		while len(queue):
			n = len(queue)
			while n:
				temp = queue.pop(0)
				
				if temp.left:
					queue.append(temp.left)
				if temp.right:
					queue.append(temp.right)
				print temp.data,
				n -= 1
			print
		return

	#Returns the previous Node if del_operation is True
	#Return None if data is on Root node or the data not found
	def searchData(self,data,del_operation):
		temp = self.root
		prevNode = None
		print
		while temp:
			if temp.data == data:
				print "%d found!"%(data)
				if del_operation:
					return prevNode
				return True
			prevNode = temp
			if data < temp.data:
				temp = temp.left
			else:
				temp = temp.right
		print "%d not present"%(data)
		if del_operation:
			return None
		return False
	
	#Complicated operation
	def deleteNode(self,data):
		prevNode = self.searchData(data,True)
		if prevNode == None and self.root.data != data:
			print "Node to be deleted not found!"
			return False
		left = True
		if prevNode == None:
			node = self.root
		elif data < prevNode.data:
			node = prevNode.left
		elif data > prevNode.data:
			node = prevNode.right
			left = False

		#If No children or only 1 child and we are not deleting root
		if prevNode and ((node.left == None) ^ (node.right == None) or node.left == None):
			print "I'm coming here"
			if left:
				prevNode.left = node.left
			else:
				prevNode.right = node.right
			return
		
		#To handle root case, and node with 2 children
		if prevNode==None:
			if node.left == None and node.right == None:
				self.root = None
			elif node.left == None:
				self.root = node.right
			elif node.right == None:
				self.root = node.left
			return

		temp = node.right
		prevNode = node

		#Find the minimum in right Subtree of node to be deleted
		#As the right subtree is also BST, the minimum node of entire subtree will be the left most leaf
		while temp and temp.left:
			#Keep track of previous node of leaf node
			prevNode = temp
			temp = temp.left

		#Swap the data with the node to be deleted
		node.data ^= temp.data
		temp.data ^= node.data
		node.data ^= temp.data

		#Set free the left Most leaf node
		prevNode.left = None
		return None
	
	#Function to search kth Node in the BST
	def searchKthNode(self,k):
		stack = []
		temp = self.root

		while 1:
			while temp:
				stack.append(temp)
				temp = temp.left

			while temp==None and len(stack):
				temp = stack.pop()
				k -= 1

				if k <= 0:
					print temp.data,
					return
				temp = temp.right

			if temp==None and len(stack)==0:
				break
		return

	#Returns the inOrder Successor of given node k
	def inOrderSuccessor(self,k):
		temp = self.root
		successor = None
		found = False
		while temp:
			if k == temp.data:
				found = True
				break
			#If going in left then current node will be successor
			elif k < temp.data:
				successor = temp
				temp = temp.left
			else:
				temp = temp.right
		if found == False:
			print "Element not found"
			return False
		if successor == None:
			print "Last Node, no successor present!"
			return False

		#If for the found node, right subtree exists
		if temp.right:
			#Return the minimum value in the right subtree
			#Which will be the left most node of the subtree
			temp = temp.right
			while temp.left:
				temp = temp.left
			return temp.data
		#If no subtree exists then return the successor data
		return successor.data
	
	def getRoot(self):
		return self.root
