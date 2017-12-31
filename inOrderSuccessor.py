def inOrderSuccessor(root,k):
	temp = root
	successor = None
	found = False
	while temp:
		if k == temp.data:
			found = True
			break
		elif k < temp.data:
			successor = temp
			temp = temp.left
		else:
			temp = temp.right
	if found == False:
		print "Element not found"
		return False
	if temp.right:
		temp = temp.right
		while temp.left:
			temp = temp.left
		data = temp.data		
	else:
		data = successor.data
	return data
