INF = 445678784654
import time
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

	exhaust1 = exhaust2 = False
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
			inOrder2 = False
		
		#print "Value:",data1,data2,"End!", "(Temp1,temp2):",(temp1,temp2)
		if data1 < data2:
			if data1 != INF:
				print data1,
			inOrder1 = True
			#If 1st is exhausted then set the data element to INF and set exhaust to True
			if temp1==None and len(stack1)==0:
				data1 = INF
				exhaust1 = True
		if data1 >= data2:
			if data2 != INF:
				print data2,
			inOrder2 = True
			#If 2nd is exhausted then set the data element to INF and set exhaust to True
			if temp2==None and len(stack2)==0:
				data2 = INF
				exhaust2 = True

		if exhaust1 and exhaust2:
			break
	return		
