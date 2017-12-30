INF = 445678784654
#Prints the 2 BST in sorted order
#Time Complexity: O(m+n)
#Space Complexity: O(log m + log n)
def merge2BST(root1, root2):
	stack1 = []
	stack2 = []
	
	inOrder1 = True
	inOrder2 = True

	temp1 = root1
	temp2 = root2

	data1 = None
	data2 = None

	last = True
	while 1:
		#Retrive the next inOrder element of BST1 
		while inOrder1:
			while temp1:
				stack1.append(temp1)
				temp1 = temp1.left

			if len(stack1):
				temp1 = stack1.pop()
				data1 = temp1.data		
				temp1 = temp1.right
			
			if temp1 == None and len(stack1)==0:
				print data2,

			inOrder1 = False

		#Retrive the next inOrder element of BST2 
		while inOrder2:
			while temp2:
				stack2.append(temp2)
				temp2 = temp2.left

			if len(stack2):
				temp2 = stack2.pop()
				data2 = temp2.data		
				temp2 = temp2.right
			
			if temp2 == None and len(stack2)==0:
				print data1,
			inOrder2 = False
	
		if data1 < data2:
			print data1,
			inOrder1 = True
		elif data1 > data2:
			print data2,
			inOrder2 = True
	
		print "Value:",data1,data2,"End!"
		#If traversal of 1st BST is complete
		if (temp1 == None and len(stack1)==0):
			if last:
				#print data2,
				last = False

			#No more travserals for BST 1
			inOrder1 = False
			#Check if 2nd BST is remaining
			if temp2:
				#Set the data representative of 1st BST to infinity
				data1 = INF
				#Open up the traversal of 2nd BST
				inOrder2 = True

		#Similar identical conditions apply for 2nd BST
		if (temp2 == None and len(stack2)==0):
			if last:
				#print data1,
				last = False
			inOrder2 = False
			if temp1:
				data2 = INF
				inOrder1 = True
		
		#If both the BST's have been completely traversed, break the outer loop
		if inOrder1 == False and inOrder2 == False:
			break
	return		
