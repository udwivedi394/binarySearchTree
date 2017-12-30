import convertBT2LL as bT2DLL
#Time Complexity: O(n)
#Space Complexity: O(n)
def findSumPair01(root, k):
	stack = []
	temp = root

	inOrder = []
	#InOrder Traversal of BST and storing all the values in inOrder
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			
			inOrder.append(temp.data)
			temp = temp.right

		if temp==None and len(stack)==0:
			break
	
	#As the inOrder traversal of BST is always sorted, below approach can be used to search pair in O(n) time
	low = 0
	high = len(inOrder)-1

	while low < high:
		curSum = inOrder[low]+inOrder[high]
		if curSum == k:
			print "\nFound:",(inOrder[low],inOrder[high])
			return True
		elif curSum < k:
			low += 1
		else:
			high -= 1
	print "\nNot found!"
	return False

#Time Complexity: O(n)
#Space Complexity: O(1)
#But this approach modifies the original BST into DLL
def findSumPair02(root,k):
	#This function converts the BT into circular DLL inOrder fashion
	#Left Child equals to previous Node and right child points to next Node in DLL
	head = bT2DLL.convertBT2DLL(root)
	temp = head
	tail = head.left

	while temp!=tail:
		curSum = temp.data+tail.data

		if curSum == k:
			print "\nFound:",(temp.data,tail.data)
			return True
		elif curSum < k:
			temp = temp.right
		else:
			tail = tail.left
	print "\nNot found!"
	return False
